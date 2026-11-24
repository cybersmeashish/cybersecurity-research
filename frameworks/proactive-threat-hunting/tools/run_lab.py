from pathlib import Path
import argparse,collections,csv,errno,hashlib,io,json,os,platform,socket,sqlite3,sys,unittest
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from hunt_engine import evaluate

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 fixtures=json.loads((ROOT/'lab/fixtures.json').read_text());rows=[]
 for case in fixtures['cases']:
  d={'window':fixtures['window'],'source_health':fixtures['source_health'],'iocs':fixtures['iocs'],'events':fixtures['baseline_events']+case['events']}
  result=evaluate(d);matched=result['hunt_ids_with_candidates']==case['expected_hunt_ids'] and not result['inconclusive_hunt_ids'];assert matched,case['id']
  rows.append({'case_id':case['id'],'expected_hunt_ids':case['expected_hunt_ids'],'actual_hunt_ids':result['hunt_ids_with_candidates'],'matches_expected':matched,'candidate_count':result['candidate_count']})
 demo=evaluate(json.loads((ROOT/'lab/demo.json').read_text()));assert len(demo['hunt_ids_with_candidates'])==17 and not demo['inconclusive_hunt_ids']
 stream=io.StringIO();suite=unittest.defaultTestLoader.discover(str(ROOT/'tests'));result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
 (a.out/'tests.txt').write_text(stream.getvalue());assert result.wasSuccessful(),stream.getvalue()
 sock=socket.socket();sock.settimeout(2)
 try:sock.connect(('198.51.100.1',443));raise AssertionError('Unexpected external networking')
 except OSError as error:assert error.errno==errno.ENETUNREACH;network_errno=error.errno
 finally:sock.close()
 summary={'framework':'Proactive Threat Hunting','version':'0.1','generated_at_utc':datetime.now(timezone.utc).isoformat(),'hunt_cards':17,'telemetry_domains':13,'synthetic_scenarios':len(rows),'positive_scenarios':sum(bool(x['expected_hunt_ids']) for x in rows),'benign_or_broken_chain_scenarios':sum(not x['expected_hunt_ids'] for x in rows),'all_scenario_expectations_match':True,'combined_demo_candidate_leads':demo['candidate_count'],'regression_test_methods':result.testsRun,'runtime':{'python':platform.python_version(),'sqlite':sqlite3.sqlite_version,'os':platform.system(),'architecture':platform.machine()},'isolation':{'network_errno':network_errno,'external_network_unreachable':True,'root_read_only':bool(os.statvfs('/').f_flag & os.ST_RDONLY),'workspace_read_only':bool(os.statvfs(str(ROOT)).f_flag & os.ST_RDONLY)},'live_customer_hunts':0,'production_query_validation':'Not performed; only local normalized SQLite queries tested','scope':'Synthetic reference consistency and security-boundary tests, not detection sensitivity/specificity or attacker attribution'}
 for name,data in [('scenario-results.json',rows),('demo-results.json',demo),('summary.json',summary)]:
  (a.out/name).write_text(json.dumps(data,indent=2)+'\n')
 with (a.out/'scenario-results.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['case_id','expected_hunt_ids','actual_hunt_ids','candidate_count','matches_expected'])
  for r in rows:w.writerow([r['case_id'],';'.join(r['expected_hunt_ids']),';'.join(r['actual_hunt_ids']),r['candidate_count'],r['matches_expected']])
 manifest={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.rglob('*')) if p.is_file() and not any(x in p.parts for x in ('__pycache__','evidence')) and not p.name.endswith('.pyc')}
 (a.out/'source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
