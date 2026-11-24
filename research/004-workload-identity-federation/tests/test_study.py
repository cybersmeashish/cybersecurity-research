from pathlib import Path
import json,sys,unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
import study
CASES=json.loads((ROOT/'lab/fixtures.json').read_text())['cases']
class BoundaryRegression(unittest.TestCase):
    def test_guarded_preserves_all_positive_effects(self):
        for case in CASES:
            if case['kind']=='positive':
                with self.subTest(case=case['case_id']):self.assertTrue(study.evaluate(case,'guarded')['effect'])
    def test_guarded_blocks_all_adversarial_effects(self):
        for case in CASES:
            if case['kind']=='adversarial':
                with self.subTest(case=case['case_id']):self.assertFalse(study.evaluate(case,'guarded')['effect'])
    def test_guarded_handles_negative_controls(self):
        for case in CASES:
            if case['kind']=='negative_control':
                with self.subTest(case=case['case_id']):self.assertFalse(study.evaluate(case,'guarded')['effect'])
    def test_seeded_vulnerable_boundary_is_observable(self):
        failures=[case for case in CASES if case['kind']=='adversarial' and study.evaluate(case,'vulnerable')['effect']]
        self.assertGreater(len(failures),0,'Positive attack control must actually reach the protected effect')
    def test_protected_effect_has_a_trace(self):
        for case in CASES:
            result=study.evaluate(case,'guarded');self.assertTrue(result['trace']);self.assertIn('backend',result['observation'])
    def test_fixture_ids_and_ground_truth_are_complete(self):
        self.assertEqual(len(CASES),len({c['case_id'] for c in CASES}));self.assertEqual({c['kind'] for c in CASES},{'positive','adversarial','negative_control'})
if __name__=='__main__':unittest.main()
