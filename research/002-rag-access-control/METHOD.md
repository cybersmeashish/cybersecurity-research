# Method and measurement contract — CAI-002

## Evaluated proposition

A derived artifact must be authorized at serving time against its current source permissions, not only against the permissions used when creating it.

## Experimental unit and corpus

A unit is one authored fixture evaluated under one profile. Six scenario types × six synthetic identity contexts produce 36 fixtures; three profiles produce 108 condition trials. Contexts change identifiers and selected graph sizes; they are not sampled deployments. The same fixtures are paired across conditions. There is no blind vendor holdout or externally registered analysis plan.

| Scenario | Declared expected behavior |
|---|---|
| direct_allowed | Allowed effect |
| direct_denied | No effect (negative control) |
| cached_foreign | No forbidden effect |
| summary_foreign | No forbidden effect |
| revoked_cache | No forbidden effect |
| cached_allowed | Allowed effect |

## Independent variable

The enforcement profile changes the checks listed below. Other fixture intent remains fixed.

- **vulnerable:** Initial source ACL only; artifacts served without current lineage checks.
- **partial:** Principal-scoped answer cache; summaries and same-principal revocation remain unchecked.
- **guarded:** Current source ACL checked before all artifact delivery.

## Primary outcome

Delivery of the unique protected marker in a returned answer.

The binary `observed_effect` field is compared with the fixture's independent `expected_effect`. Positive cases expect the legitimate effect. Adversarial and negative-control cases expect its absence. Outcomes are corroborated by the backend-specific observation and execution trace. Their meanings differ across studies; counts must not be pooled as a production risk metric.

## Secondary measurements and controls

Report retained legitimate effects, negative-control failures, expectation matches, and partial-control outcomes separately. Test replays are not independent samples. For the cache study, latency and membership discrimination are separate from namespace hits. The budget study uses known normalized work costs, not currency.

## Execution, evidence, and decision rule

Run in the pinned isolated environment described in [REPRODUCIBILITY.md](REPRODUCIBILITY.md). Accept a mechanism demonstration only when the seeded profile reaches the actual endpoint, the guarded profile matches all declared labels, and the positive control remains useful. Archive raw rows, trace receipts, regression output, runtime metadata, and source hashes. Preserve any unexpected observation as a failed or inconclusive result rather than changing labels to fit it.

## What was not measured

No vector database, Azure search service, model-generated summary, asynchronous index propagation, conversation erasure, or customer corpus was tested. Revocation is an immediate SQLite transaction, so no claim about a provider synchronization deadline is supported.

No prevalence estimate or confidence interval is attached to curated attack proportions. The exploratory cache bootstrap quantifies variability over its generated prefixes only, not over deployments, hardware, or models.
