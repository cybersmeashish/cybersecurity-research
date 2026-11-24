import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from hunt_engine import evaluate,epoch
FIX=json.loads((ROOT/'lab/fixtures.json').read_text());PACK=json.loads((ROOT/'hunt-pack.json').read_text())
def data(case='H07-positive'):
    selected=next(c for c in FIX['cases'] if c['id']==case)
    return copy.deepcopy({'window':FIX['window'],'source_health':FIX['source_health'],'iocs':FIX['iocs'],'events':FIX['baseline_events']+selected['events']})
def assessment(result,hid):return next(a for a in result['assessments'] if a['hunt_id']==hid)
class HuntingBoundaryTests(unittest.TestCase):
    def test_all_seeded_positive_and_benign_scenarios(self):
        for case in FIX['cases']:
            with self.subTest(case=case['id']):
                result=evaluate(data(case['id']))
                self.assertEqual(result['hunt_ids_with_candidates'],case['expected_hunt_ids'])
                self.assertFalse(result['inconclusive_hunt_ids'])

    def test_cross_tenant_events_do_not_correlate(self):
        d=data();d['events'][-1]['tenant_id']='synthetic-tenant-B'
        self.assertEqual(assessment(evaluate(d),'H07')['candidate_count'],0)

    def test_identity_local_name_or_wrong_runtime_cannot_join(self):
        d=data();d['events'][-1]['principal_id']='similar-display-name'
        self.assertEqual(assessment(evaluate(d),'H07')['candidate_count'],0)

    def test_same_raw_id_in_different_tenants_is_not_deduplicated(self):
        d=data('H02-positive');other=copy.deepcopy(d['events'][-1]);other['tenant_id']='synthetic-tenant-B';d['events'].append(other)
        result=evaluate(d);self.assertEqual(assessment(result,'H02')['candidate_count'],2)
        self.assertEqual(result['normalization']['identical_duplicates_removed'],0)

    def test_replayed_failures_do_not_inflate_burst(self):
        d=data('H03-negative');failure=next(e for e in d['events'] if e['action']=='login_failure');d['events']+=[copy.deepcopy(failure) for _ in range(4)]
        result=evaluate(d);self.assertEqual(assessment(result,'H03')['candidate_count'],0)
        self.assertEqual(result['normalization']['identical_duplicates_removed'],4)

    def test_conflicting_event_identity_is_inconclusive(self):
        d=data('H02-positive');other=copy.deepcopy(d['events'][-1]);other['sha256']='b'*64;d['events'].append(other)
        result=evaluate(d);self.assertEqual(assessment(result,'H02')['status'],'inconclusive_coverage')
        self.assertEqual(result['normalization']['conflicting_scoped_keys'],1)

    def test_naive_clock_and_non_boolean_approval_are_rejected(self):
        for field,value in [('timestamp','2026-11-24T08:01:00'),('approved','false')]:
            d=data('H04-positive');d['events'][-1][field]=value
            with self.subTest(field=field):
                result=evaluate(d);self.assertEqual(assessment(result,'H04')['status'],'inconclusive_coverage')
                self.assertTrue(result['normalization']['quarantined_records'])

    def test_missing_sensor_is_not_no_threat(self):
        d=data('H05-negative');d['source_health']=[s for s in d['source_health'] if s['domain']!='email']
        a=assessment(evaluate(d),'H05');self.assertEqual(a['status'],'inconclusive_coverage');self.assertFalse(a['query_executed'])

    def test_missing_join_or_policy_mapping_is_inconclusive(self):
        for cid,field,hid in [('H09-positive','delegator_id','H09'),('H14-positive','out_of_scope','H14'),('H04-positive','approved','H04')]:
            d=data(cid);d['events'][-1].pop(field)
            with self.subTest(field=field):self.assertEqual(assessment(evaluate(d),hid)['status'],'inconclusive_coverage')

    def test_future_event_does_not_pollute_baseline(self):
        d=data('H01-positive');future=copy.deepcopy(d['events'][-1]);future['event_id']='future-same-pattern';future['timestamp']='2026-11-24T10:01:00Z';future['ingested_at']='2026-11-24T10:01:10Z';d['events'].append(future)
        result=evaluate(d);self.assertEqual(assessment(result,'H01')['candidate_count'],1)
        self.assertEqual(result['normalization']['excluded_records']['outside_event_window'],1)

    def test_event_ingested_after_snapshot_is_not_visible(self):
        d=data('H07-positive');d['events'][-1]['ingested_at']='2026-11-24T09:01:00Z'
        a=assessment(evaluate(d),'H07');self.assertEqual(a['status'],'inconclusive_coverage');self.assertFalse(a['candidates'])

    def test_reverse_time_correlation_is_not_a_lead(self):
        d=data('H07-positive');d['events'][-1]['timestamp']='2026-11-24T08:00:30Z';d['events'][-1]['ingested_at']='2026-11-24T08:00:40Z'
        self.assertEqual(assessment(evaluate(d),'H07')['candidate_count'],0)

    def test_expired_or_revoked_ioc_does_not_match(self):
        for field,value in [('valid_until','2026-11-24T08:00:00Z'),('revoked',True)]:
            d=data('H02-positive');d['iocs'][0][field]=value
            with self.subTest(field=field):self.assertEqual(assessment(evaluate(d),'H02')['candidate_count'],0)

    def test_insufficient_baseline_does_not_assert_novelty(self):
        d=data('H01-positive');d['events']=[e for e in d['events'] if not (e['domain']=='endpoint' and e['action']=='baseline_observed')]
        self.assertEqual(assessment(evaluate(d),'H01')['status'],'inconclusive_coverage')

    def test_stale_sensor_and_large_clock_uncertainty_are_inconclusive(self):
        for field,value in [('last_heartbeat','2026-11-24T08:00:00Z'),('clock_uncertainty_seconds',300)]:
            d=data('H06-positive');s=next(s for s in d['source_health'] if s['domain']=='identity');s[field]=value
            with self.subTest(field=field):self.assertEqual(assessment(evaluate(d),'H06')['status'],'inconclusive_coverage')

    def test_query_path_cannot_escape_framework(self):
        pack=copy.deepcopy(PACK);pack['hunts'][0]['query']='../../../../AGENTS.md'
        with self.assertRaises(ValueError):evaluate(data('H01-positive'),pack)

    def test_absent_indicator_registry_is_inconclusive(self):
        d=data('H02-negative');d['iocs']=[]
        self.assertEqual(assessment(evaluate(d),'H02')['status'],'inconclusive_coverage')

    def test_input_order_does_not_change_hunt_assessment(self):
        d=data('H03-positive');before=evaluate(d)['assessments'];d['events'].reverse()
        self.assertEqual(evaluate(d)['assessments'],before)

    def test_known_baseline_relationship_suppresses_only_its_novelty(self):
        d=data('H01-positive');seen=copy.deepcopy(d['events'][-1]);seen['event_id']='known-pattern';seen['timestamp']='2026-11-23T08:10:00Z';seen['ingested_at']='2026-11-23T08:10:10Z';d['events'].append(seen)
        self.assertEqual(assessment(evaluate(d),'H01')['candidate_count'],0)
if __name__=='__main__':unittest.main()
