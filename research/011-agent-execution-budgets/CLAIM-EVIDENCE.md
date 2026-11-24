# Claim-to-evidence register — CAI-011

| Claim ID | Claim | Evidence stage | Evidence |
|---|---|---|---|
| CAI-011-E1 | The seeded permissive profile produced 18 forbidden effects in 18 authored adversarial cases. | direct local synthetic observation | [results.csv](evidence/results.csv) · [traces.json](evidence/traces.json) |
| CAI-011-E2 | The guarded profile matched all 36 declared policy labels and preserved 6 positive effects. | bounded local control result | [summary.json](evidence/summary.json) · [tests.txt](evidence/tests.txt) |
| CAI-011-E3 | The partial profile retained 18 forbidden effects. | local control comparison | [results.csv](evidence/results.csv) |
| CAI-011-H1 | Per-request limits fail to bound aggregate task consumption when reasoning, retries, fan-out, and delegation are charged independently without a shared task budget. | original research hypothesis; only stated local subclaim evaluated | Not established by this experiment |

The [machine-readable ledger](evidence/claim-ledger.json) records exclusions for every claim. To inspect an observation, filter [results.csv](evidence/results.csv) by `mode` and `type`, then locate the same `case_id` in [traces.json](evidence/traces.json). Every measured endpoint must be corroborated by a receipt or backend observation.

No evidence is fabricated for a named product. Missing implementation evidence is explicitly pending.
