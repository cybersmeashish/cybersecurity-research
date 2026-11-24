from pathlib import Path
import argparse,csv,hashlib,json,platform,random,socket,sys,time,unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
import study

def auc(rows):
    positives=[-r['elapsed_ns'] for r in rows if r['resident_in_A']];negatives=[-r['elapsed_ns'] for r in rows if not r['resident_in_A']]
    return sum((p>n)+0.5*(p==n) for p in positives for n in negatives)/(len(positives)*len(negatives))

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    fixtures=json.loads((ROOT/'lab/fixtures.json').read_text());rows=[];traces=[]
    for mode in ['vulnerable','partial','guarded']:
        for case in fixtures['cases']:
            result=study.evaluate(case,mode)
            row={k:case[k] for k in ['case_id','type','kind','expected_effect']};row.update(mode=mode,observed_effect=bool(result['effect']),expectation_match=bool(result['effect'])==case['expected_effect']);rows.append(row)
            traces.append(dict(row,trace=result['trace'],observation=result['observation']))
    conditions={}
    for mode in ['vulnerable','partial','guarded']:
        selected=[r for r in rows if r['mode']==mode];positive=[r for r in selected if r['kind']=='positive'];attacks=[r for r in selected if r['kind']=='adversarial'];negative=[r for r in selected if r['kind']=='negative_control']
        conditions[mode]={'trials':len(selected),'positive_cases':len(positive),'positive_effects':sum(r['observed_effect'] for r in positive),'adversarial_cases':len(attacks),'unauthorized_effects':sum(r['observed_effect'] for r in attacks),'negative_control_cases':len(negative),'negative_control_failures':sum(r['observed_effect'] for r in negative),'expectation_matches':sum(r['expectation_match'] for r in selected)}
    suite=unittest.defaultTestLoader.discover(str(ROOT/'tests'),pattern='test_*.py');report_file=args.out/'tests.txt'
    with report_file.open('w') as stream:
        test_result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
    if not test_result.wasSuccessful():raise SystemExit('Behavioral regression failed; see '+str(report_file))
    if conditions['guarded']['expectation_matches']!=len(fixtures['cases']):raise SystemExit('Guarded case expectations do not match')
    with (args.out/'results.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    (args.out/'traces.json').write_text(json.dumps(traces,indent=2)+'\n')
    manifest={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for folder in ['src','tests','tools','lab'] for p in sorted((ROOT/folder).rglob('*')) if p.is_file() and p.suffix in ['.py','.json']}
    (args.out/'source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    summary={'study_id':fixtures['study_id'],'evidence_stage':'controlled local synthetic experiment','experimental_conditions':conditions,'fixture_cases':len(fixtures['cases']),'condition_trials':len(rows),'regression_methods':test_result.testsRun,'runtime':{'python':platform.python_version(),'os':platform.system(),'architecture':platform.machine()},'generated_at_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'live_provider_experiments':0,'model_calls':0,'confirmed_provider_vulnerabilities':0,'global_novelty_established':False}
    if hasattr(study,'timing_experiment'):
        timing=study.timing_experiment();metrics={};rng=random.Random(12345)
        for mode in ['vulnerable','partial','guarded']:
            subset=[r for r in timing if r['mode']==mode];positive=[r for r in subset if r['resident_in_A']];negative=[r for r in subset if not r['resident_in_A']];boot=[]
            for _ in range(400):boot.append(auc([rng.choice(positive) for _ in positive]+[rng.choice(negative) for _ in negative]))
            boot.sort();metrics[mode]={'held_out_prefixes':len(subset),'roc_auc':auc(subset),'auc_bootstrap_95_interval':[boot[9],boot[389]],'balanced_accuracy':sum(r['predicted_resident']==r['resident_in_A'] for r in subset)/len(subset),'cross_tenant_cache_hits':sum(r['cache_hit_ground_truth'] for r in subset),'unit':'independent synthetic prefix; one first probe per prefix'}
        with (args.out/'timing.csv').open('w',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=list(timing[0]));writer.writeheader();writer.writerows(timing)
        (args.out/'timing-metrics.json').write_text(json.dumps(metrics,indent=2)+'\n');summary['timing']=metrics
    isolation={}
    for key,path in [('workspace_read_only',ROOT/'readonly-probe.tmp'),('root_read_only',Path('/readonly-probe.tmp'))]:
        try:path.write_text('probe');path.unlink();isolation[key]=False
        except OSError:isolation[key]=True
    try:s=socket.create_connection(('198.51.100.1',443),timeout=0.2);s.close();isolation['external_network_unreachable']=False
    except OSError:isolation['external_network_unreachable']=True
    summary['isolation']=isolation
    if not all(isolation.values()):raise SystemExit('Required lab isolation missing')
    (args.out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({'study_id':summary['study_id'],'fixtures':summary['fixture_cases'],'trials':summary['condition_trials'],'regression_methods':summary['regression_methods'],'conditions':conditions},indent=2))
if __name__=='__main__':main()
