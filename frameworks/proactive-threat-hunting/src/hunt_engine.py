"""Local coverage-aware reference hunts. No telemetry collection or response actions.

Queries use this simplified normalized schema, not a native provider or SIEM.
Candidate associations require analyst corroboration; no attacker attribution.
"""
from __future__ import annotations
import argparse,collections,hashlib,json,sqlite3
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SCHEMA=json.loads((ROOT/'schema/event-schema.json').read_text())
STRINGS=SCHEMA['typed_optional']['strings'];INTS=SCHEMA['typed_optional']['nonnegative_integers'];BOOLS=SCHEMA['typed_optional']['booleans']
DOMAINS={'endpoint','identity','email','cloud-aws','cloud-azure','cloud-gcp','kubernetes','network','dns','saas','ai','cicd','backup'}
COLUMNS=['event_id','tenant_id','source','domain','ts','ingested','action']+STRINGS+INTS+BOOLS+['phase']

def epoch(value):
    if not isinstance(value,str):raise ValueError('Timestamp must be a string')
    instant=datetime.fromisoformat(value.replace('Z','+00:00'))
    if instant.tzinfo is None:raise ValueError('Naive timestamp; timezone evidence missing')
    return int(instant.astimezone(timezone.utc).timestamp())

def validate_event(event):
    if not isinstance(event,dict):raise ValueError('Event must be an object')
    if set(event)-(set(SCHEMA['required'])|set(STRINGS+INTS+BOOLS)):raise ValueError('Unsupported normalized fields')
    for key in SCHEMA['required']:
        if not isinstance(event.get(key),str) or not event[key] or len(event[key])>1024:raise ValueError('Invalid required field: '+key)
    if event['domain'] not in DOMAINS:raise ValueError('Unsupported domain')
    if '|' in event['event_id']:raise ValueError('Invalid event reference delimiter')
    for key in STRINGS:
        value=event.get(key)
        if value is not None and (not isinstance(value,str) or not value or len(value)>1024):raise ValueError('Invalid string: '+key)
    for key in INTS:
        value=event.get(key)
        if value is not None and (type(value) is not int or value<0):raise ValueError('Invalid integer: '+key)
    if event.get('dest_port') is not None and event['dest_port']>65535:raise ValueError('Invalid port')
    for key in BOOLS:
        value=event.get(key)
        if value is not None and type(value) is not bool:raise ValueError('Invalid boolean: '+key)
    for key in ('sha256','digest','approved_digest'):
        value=event.get(key)
        if value is not None and (len(value)!=64 or any(c not in '0123456789abcdef' for c in value)):raise ValueError('Invalid SHA256: '+key)
    return epoch(event['timestamp']),epoch(event['ingested_at'])

def evaluate(dataset,pack=None):
    pack=pack or json.loads((ROOT/'hunt-pack.json').read_text());window=dataset['window']
    start=epoch(window['window_start']);end=epoch(window['window_end']);baseline=epoch(window['baseline_start'])
    if not baseline<start<end:raise ValueError('Invalid windows')
    minimum=window.get('min_baseline_events',2);max_lag=window.get('max_ingestion_lag_seconds',120);max_clock=window.get('max_clock_uncertainty_seconds',30)
    if any(type(v) is not int or v<0 for v in (minimum,max_lag,max_clock)) or minimum<1:raise ValueError('Invalid quality thresholds')
    by_key={};conflicts=set();quarantine=[];duplicates=0;issues=collections.defaultdict(list);excluded=collections.Counter()
    for index,event in enumerate(dataset['events']):
        domain=event.get('domain') if isinstance(event,dict) else None
        try:ts,ingested=validate_event(event)
        except (ValueError,TypeError) as error:
            quarantine.append({'record_index':index,'domain':domain,'reason':str(error)});issues[domain if domain in DOMAINS else '*'].append('Rejected record: '+str(error));continue
        key=(event['tenant_id'],event['source'],domain,event['event_id']);canonical=json.dumps(event,sort_keys=True,separators=(',',':'))
        if key in conflicts:continue
        if key in by_key:
            if by_key[key][0]==canonical:duplicates+=1
            else:
                conflicts.add(key);by_key.pop(key);issues[domain].append('Conflicting scoped event id');quarantine.append({'record_index':index,'domain':domain,'reason':'Conflicting scoped event id'})
            continue
        by_key[key]=(canonical,event,ts,ingested)
    rows=[];references={}
    for key,(_,event,ts,ingested) in sorted(by_key.items()):
        if not baseline<=ts<end:excluded['outside_event_window']+=1;continue
        if ingested>end:excluded['not_visible_at_assessment_time']+=1;issues[event['domain']].append('Event ingested after assessment snapshot');continue
        if ingested<ts or ingested-ts>max_lag:issues[event['domain']].append('Ingestion lag or clock outside bounds')
        ref=hashlib.sha256(json.dumps(key).encode()).hexdigest()
        references[ref]={'event_id':event['event_id'],'tenant_id':event['tenant_id'],'source':event['source'],'domain':event['domain'],'timestamp':event['timestamp']}
        row={'event_id':ref,'tenant_id':event['tenant_id'],'source':event['source'],'domain':event['domain'],'ts':ts,'ingested':ingested,'action':event['action'],'phase':int(ts>=start)}
        for field in STRINGS+INTS+BOOLS:
            value=event.get(field);row[field]=int(value) if type(value) is bool else value
        rows.append(row)
    db=sqlite3.connect(':memory:');db.row_factory=sqlite3.Row;text_fields=set(['event_id','tenant_id','source','domain','action']+STRINGS)
    db.execute('CREATE TABLE events ('+','.join(name+' '+('TEXT' if name in text_fields else 'INTEGER') for name in COLUMNS)+')')
    db.executemany('INSERT INTO events VALUES ('+','.join('?' for _ in COLUMNS)+')',[[r[c] for c in COLUMNS] for r in rows])
    db.execute('CREATE TABLE iocs (kind TEXT,value TEXT,valid_from INTEGER,valid_until INTEGER,revoked INTEGER,source TEXT)');indicator_issues=[]
    for indicator in dataset.get('iocs',[]):
        try:
            if indicator.get('kind')!='sha256' or not isinstance(indicator.get('value'),str) or len(indicator['value'])!=64 or any(c not in '0123456789abcdef' for c in indicator['value']):raise ValueError('Invalid/unsupported IOC')
            if type(indicator.get('revoked')) is not bool or not isinstance(indicator.get('source'),str) or not indicator['source']:raise ValueError('IOC provenance or revocation missing')
            begins=epoch(indicator['valid_from']);expires=epoch(indicator['valid_until'])
            if expires<begins:raise ValueError('Invalid IOC interval')
            db.execute('INSERT INTO iocs VALUES (?,?,?,?,?,?)',(indicator['kind'],indicator['value'],begins,expires,int(indicator['revoked']),indicator['source']))
        except (ValueError,TypeError,KeyError) as error:indicator_issues.append(str(error))
    active=db.execute('SELECT COUNT(*) FROM iocs WHERE revoked=0 AND valid_from<=? AND valid_until>=?',(end,end)).fetchone()[0]
    if active==0:indicator_issues.append('No active indicator-registry evidence at assessment time')
    health={};duplicate_health=set()
    for item in dataset.get('source_health',[]):
        domain=item.get('domain')
        if domain in health:duplicate_health.add(domain)
        health[domain]=item
    allowed={sqlite3.SQLITE_SELECT,sqlite3.SQLITE_READ,sqlite3.SQLITE_FUNCTION,sqlite3.SQLITE_RECURSIVE}
    db.set_authorizer(lambda action,a,b,c,d:sqlite3.SQLITE_OK if action in allowed else sqlite3.SQLITE_DENY)
    assessments=[]
    for hunt in pack['hunts']:
        domains=hunt['required_domains'];gaps=[];uncertainties=[]
        for domain in domains:
            gaps.extend(issues.get(domain,[]));gaps.extend(issues.get('*',[]));item=health.get(domain)
            if item is None or domain in duplicate_health:gaps.append('Missing or ambiguous source health: '+domain);continue
            try:
                if epoch(item['coverage_start'])>start or epoch(item['coverage_end'])<end:gaps.append('Incomplete hunt-window coverage: '+domain)
                if not end-300<=epoch(item['last_heartbeat'])<=end:gaps.append('Stale or future heartbeat: '+domain)
                clock=item.get('clock_uncertainty_seconds')
                if type(clock) is not int or clock<0 or clock>max_clock:gaps.append('Clock uncertainty unsupported: '+domain)
                else:uncertainties.append(clock)
                if hunt['requires_baseline']:
                    count=sum(r['domain']==domain and r['phase']==0 for r in rows)
                    if item.get('baseline_complete') is not True or epoch(item['coverage_start'])>baseline or count<minimum:gaps.append('Baseline coverage/volume insufficient: '+domain)
            except (ValueError,TypeError,KeyError):gaps.append('Invalid source-health record: '+domain)
        if hunt['id']=='H02':gaps.extend(indicator_issues)
        for row in rows:
            if row['phase']==1 and row['domain'] in domains:
                for field in hunt['required_fields_by_action'].get(row['action'],[]):
                    if row.get(field) is None:gaps.append('Required mapping absent: '+row['domain']+'/'+row['action']+'/'+field)
        gaps=sorted(set(gaps));candidates=[]
        if not gaps:
            query=(ROOT/hunt['query']).resolve()
            if not query.is_relative_to(ROOT) or not query.is_file():raise ValueError('Query outside framework')
            sql=query.read_text().strip()
            if not sql.upper().startswith(('SELECT ','WITH ')):raise ValueError('Only read-only local queries supported')
            params={'window_end':end,'min_order_gap':2*max(uncertainties,default=0) if hunt['requires_ordering'] else 0};seen=set()
            for item in db.execute(sql,params).fetchall():
                refs=sorted(set(item['evidence_ids'].split('|')));signature=(item['tenant_id'],item['entity_id'],tuple(refs))
                if signature in seen:continue
                seen.add(signature);candidates.append({'hunt_id':hunt['id'],'tenant_id':item['tenant_id'],'entity_id':item['entity_id'],'evidence':[references[r] for r in refs],'interpretation':'Candidate association; corroboration required'})
        candidates.sort(key=lambda c:(c['tenant_id'],c['entity_id'],json.dumps(c['evidence'],sort_keys=True)))
        status='inconclusive_coverage' if gaps else ('candidate_leads' if candidates else 'no_lead_in_observed_data')
        assessments.append({'hunt_id':hunt['id'],'title':hunt['title'],'status':status,'query_executed':not gaps,'coverage_gaps':gaps,'candidate_count':len(candidates),'candidates':candidates,'decision_scope':'Only this observed window/schema; no clear-of-compromise conclusion'})
    db.close()
    return {'scope':'Synthetic local reference; no live telemetry or production detection claim','window':window,'assessments':assessments,'normalization':{'accepted_in_window_or_baseline':len(rows),'identical_duplicates_removed':duplicates,'conflicting_scoped_keys':len(conflicts),'quarantined_records':quarantine,'excluded_records':dict(excluded)},'candidate_count':sum(a['candidate_count'] for a in assessments),'hunt_ids_with_candidates':[a['hunt_id'] for a in assessments if a['candidate_count']],'inconclusive_hunt_ids':[a['hunt_id'] for a in assessments if a['status']=='inconclusive_coverage']}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    result=evaluate(json.loads(a.input.read_text()));a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'candidates':result['candidate_count'],'inconclusive_hunts':result['inconclusive_hunt_ids']}))
if __name__=='__main__':main()
