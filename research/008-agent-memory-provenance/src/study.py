import json,sqlite3

def evaluate(case,mode):
    t=case['type'];trusted=t=='trusted_instruction';db=sqlite3.connect(':memory:');db.execute('CREATE TABLE memory(id TEXT PRIMARY KEY, record TEXT)')
    source={'kind':'source','origin':'operator' if trusted else 'retrieval','trust':'trusted' if trusted else 'low','action':'write','parent':None}
    db.execute('INSERT INTO memory VALUES(?,?)',('source',json.dumps(source)));current='source';trace=[{'step':'session_1_ingestion','origin':source['origin'],'trust':source['trust']}]
    depth=0 if t=='raw_lowtrust' else (2 if t=='double_compaction' else 1)
    for i in range(depth):
        prev=json.loads(db.execute('SELECT record FROM memory WHERE id=?',(current,)).fetchone()[0])
        rec={'kind':'summary','action':prev['action'],'parent':current}
        if mode=='guarded' or (mode=='partial' and i==0):rec['trust']=prev.get('trust','trusted')
        if t=='unbound_derivation' and mode!='guarded':rec.update(parent=None,trust='trusted')
        name='summary-'+str(i);db.execute('INSERT INTO memory VALUES(?,?)',(name,json.dumps(rec)));current=name;trace.append({'step':'structured_compaction','record':rec})
    if t=='evicted_source':db.execute('DELETE FROM memory WHERE id=?',('source',))
    recalled=json.loads(db.execute('SELECT record FROM memory WHERE id=?',(current,)).fetchone()[0])
    def authorized_root(key,seen=None):
        seen=set() if seen is None else seen
        if key in seen:return False
        seen.add(key);row=db.execute('SELECT record FROM memory WHERE id=?',(key,)).fetchone()
        if not row:return False
        rec=json.loads(row[0])
        if rec['kind']=='source':return rec.get('origin')=='operator' and rec.get('trust')=='trusted'
        return bool(rec.get('parent')) and authorized_root(rec['parent'],seen)
    allowed=authorized_root(current) if mode=='guarded' else recalled.get('trust','trusted')=='trusted'
    effects=[]
    if allowed:effects.append({'session':2,'action':'write','synthetic_target':'record'})
    trace.extend([{'step':'new_session_recall','record':recalled,'original_text_supplied':False},{'step':'provenance_gate','allowed':allowed,'effects':effects}]);db.close()
    return {'effect':bool(effects),'trace':trace,'observation':{'later_action_executed':bool(effects),'backend':'structured SQLite memory compaction and replayed action; no language model or semantic summary'}}
