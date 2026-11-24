import copy
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from authority_graph import evaluate, evaluate_fixture, validate_chain
from local_runtime import LocalRuntime, Policy, run_runtime_experiment
S=ROOT/'studies/001-ai-infrastructure-authority-bindings'
CHAINS={c['id']:c for c in json.loads((S/'chains.json').read_text())}
FIXTURES=json.loads((S/'fixtures.json').read_text())

class BoundaryTests(unittest.TestCase):
    def test_dataset_expected_outcomes(self):
        for fixture in FIXTURES:
            with self.subTest(fixture=fixture['id']):
                self.assertTrue(evaluate_fixture(CHAINS,fixture)['matches_expected'])

    def test_missing_evidence_cannot_confirm_path(self):
        for chain in CHAINS.values():
            with self.subTest(chain=chain['id']):
                result=evaluate(chain,{})
                self.assertEqual(result['outcome'],'unknown')
                self.assertEqual(len(result['missing_facts']),len(chain['fact_definitions']))

    def test_each_necessary_condition_can_block(self):
        for chain in CHAINS.values():
            for key in chain['fact_definitions']:
                with self.subTest(chain=chain['id'],key=key):
                    values={name:True for name in chain['fact_definitions']};values[key]=False
                    self.assertEqual(evaluate(chain,values)['outcome'],'blocked')

    def test_explicit_data_denial_blocks_other_unknowns(self):
        chain=CHAINS['aws-training'];values={key:None for key in chain['fact_definitions']}
        values['runtime_data_read_effective_allow']=False
        self.assertEqual(evaluate(chain,values)['outcome'],'blocked')

    def test_reject_derived_node_override(self):
        chain=CHAINS['aws-training']
        with self.assertRaises(ValueError):evaluate(chain,{'job_runtime_obtained':True})

    def test_reject_truthy_non_boolean_evidence(self):
        chain=CHAINS['aws-training'];key=next(iter(chain['fact_definitions']))
        for value in (1,'true',[],{}):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):evaluate(chain,{key:value})

    def test_reject_cycle_and_unknown_dependency(self):
        for requirement in ('job_runtime_obtained','nonexistent'):
            chain=copy.deepcopy(CHAINS['aws-training']);chain['rules'][0]['requires']=[requirement]
            with self.subTest(requirement=requirement):
                with self.assertRaises(ValueError):validate_chain(chain)

    def test_reject_duplicate_or_empty_preconditions(self):
        for requires in ([],['actor_can_submit_job','actor_can_submit_job']):
            chain=copy.deepcopy(CHAINS['aws-training']);chain['rules'][0]['requires']=requires
            with self.subTest(requires=requires):
                with self.assertRaises(ValueError):validate_chain(chain)

    def test_live_evidence_cannot_be_labelled_as_lab_results(self):
        fixture=copy.deepcopy(FIXTURES[0]);fixture['evidence_kind']='live_cloud'
        with self.assertRaises(ValueError):evaluate_fixture(CHAINS,fixture)

    def test_private_ingress_annotation_does_not_block_egress(self):
        chain=copy.deepcopy(CHAINS['k8s-egress']);facts={key:True for key in chain['fact_definitions']}
        before=evaluate(chain,facts)['outcome'];chain['context_annotations']['private_ingress_present']=False
        self.assertEqual(before,'reachable');self.assertEqual(evaluate(chain,facts)['outcome'],before)

    def test_local_authority_bindings_and_controls(self):
        rows=run_runtime_experiment()
        self.assertEqual(len(rows),24)
        self.assertEqual(sum(r['unauthorized_output_returned'] for r in rows),4)
        self.assertTrue(all(r['direct_access_denied'] and r['matches_expected'] for r in rows))

    def test_legitimate_job_survives_actor_and_digest_controls(self):
        import hashlib
        artifact=b'approved'
        r=LocalRuntime(Policy(caller_binding=True,scoped_runtime=True,trusted_digest=hashlib.sha256(artifact).hexdigest()))
        self.assertEqual(r.run_job('tenant-a','tenant-a',artifact),'SYNTHETIC:A:PUBLIC')

    def test_output_block_does_not_erase_internal_read(self):
        r=LocalRuntime(Policy(egress_allowed=False))
        self.assertIsNone(r.run_job('tenant-a','tenant-b',b'workload'))
        self.assertTrue(any(x['operation']=='runtime_read' and x['allowed'] for x in r.audit))

if __name__=='__main__':unittest.main()
