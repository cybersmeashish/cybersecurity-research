"""Run the source-defined synthetic study and write verifiable local results."""
from pathlib import Path
import argparse, collections, csv, errno, hashlib, io, json, os, platform, socket, sys, unittest
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from authority_graph import evaluate_fixture
from local_runtime import run_runtime_experiment
S=ROOT/'studies/001-ai-infrastructure-authority-bindings'

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    a.out.mkdir(parents=True,exist_ok=True)
    chains={x['id']:x for x in json.loads((S/'chains.json').read_text())}
    fixtures=json.loads((S/'fixtures.json').read_text())
    assert len(chains)==8 and len({f['id'] for f in fixtures})==len(fixtures)
    rows=[evaluate_fixture(chains,f) for f in fixtures]
    assert all(r['matches_expected'] for r in rows)
    runtime=run_runtime_experiment()
    stream=io.StringIO();suite=unittest.defaultTestLoader.discover(str(ROOT/'tests'),pattern='test_*.py')
    result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
    (a.out/'tests.txt').write_text(stream.getvalue())
    assert result.wasSuccessful(),stream.getvalue()
    sock=socket.socket();sock.settimeout(2)
    try:
        sock.connect(('198.51.100.1',443))
        raise AssertionError('Unexpected external networking')
    except OSError as e:
        isolation_errno=e.errno
        assert isolation_errno==errno.ENETUNREACH,('Expected network-none; got',e.errno)
    finally:sock.close()
    def readonly(path):return bool(os.statvfs(path).f_flag & os.ST_RDONLY)
    summary={'study_id':'AIA-001','generated_at_utc':datetime.now(timezone.utc).isoformat(),
      'chains':len(chains),'candidate_classes':5,'primary_sources':len(json.loads((S/'sources.json').read_text())),
      'synthetic_fixture_cases':len(rows),'outcomes':dict(collections.Counter(r['outcome'] for r in rows)),
      'all_fixture_expectations_match':True,'unit_test_methods':result.testsRun,
      'local_runtime_cases':len(runtime),'local_runtime_baseline_disclosures':sum(r['unauthorized_output_returned'] for r in runtime),
      'local_runtime_control_cases':sum(r['condition']!='baseline' for r in runtime),
      'local_runtime_control_disclosures':sum(r['unauthorized_output_returned'] for r in runtime if r['condition']!='baseline'),
      'runtime_profiles':'One shared mock ACL backend with four labels; not four independent cloud environments',
      'runtime':{'python':platform.python_version(),'os':platform.system(),'architecture':platform.machine()},
      'isolation':{'network_probe_destination':'198.51.100.1:443 (documentation address)','errno':isolation_errno,
                   'external_network_unreachable':True,'root_read_only':readonly('/'),'workspace_read_only':readonly(str(ROOT))},
      'live_provider_experiments':0,'new_provider_vulnerabilities_confirmed':0,'novelty_status':'candidate taxonomy; global novelty not established',
      'scope':'Original comparative synthesis and synthetic experiments; no deployed AWS/Azure/Google Cloud/Kubernetes exploit validation'}
    for name,data in [('graph-results.json',rows),('runtime-results.json',runtime),('summary.json',summary)]:
        (a.out/name).write_text(json.dumps(data,indent=2)+'\n')
    with (a.out/'results.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['fixture_id','chain_id','outcome','expected_outcome','matches_expected','missing_facts','false_facts'])
        for r in rows:w.writerow([r['fixture_id'],r['chain_id'],r['outcome'],r['expected_outcome'],r['matches_expected'],';'.join(r['missing_facts']),';'.join(r['false_facts'])])
    manifest={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.rglob('*'))
      if p.is_file() and not any(x in p.parts for x in ('.git','__pycache__','evidence')) and not p.name.endswith('.pyc')}
    (a.out/'source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
