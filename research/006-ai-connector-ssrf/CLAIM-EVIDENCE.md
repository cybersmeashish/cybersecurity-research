# Claim-to-evidence register — CAI-006

| Claim ID | Claim | Evidence stage | Evidence |
|---|---|---|---|
| CAI-006-E1 | The seeded permissive profile produced 12 forbidden effects in 12 authored adversarial cases. | direct local synthetic observation | [results.csv](evidence/results.csv) · [traces.json](evidence/traces.json) |
| CAI-006-E2 | The guarded profile matched all 36 declared policy labels and preserved 12 positive effects. | bounded local control result | [summary.json](evidence/summary.json) · [tests.txt](evidence/tests.txt) |
| CAI-006-E3 | The partial profile retained 6 forbidden effects. | local control comparison | [results.csv](evidence/results.csv) |
| CAI-006-H1 | A connector validating only an initial URL or DNS answer can contact a forbidden internal destination after a redirect or changed resolution alters the actual connection target. | original research hypothesis; only stated local subclaim evaluated | Not established by this experiment |

The [machine-readable ledger](evidence/claim-ledger.json) records exclusions for every claim. To inspect an observation, filter [results.csv](evidence/results.csv) by `mode` and `type`, then locate the same `case_id` in [traces.json](evidence/traces.json). Every measured endpoint must be corroborated by a receipt or backend observation.

No evidence is fabricated for a named product. Missing implementation evidence is explicitly pending.
