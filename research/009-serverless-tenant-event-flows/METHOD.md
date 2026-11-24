# Method and measurement contract — CAI-009

## Evaluated proposition

Signature and producer authenticity do not authorize a tenant value inside the producer-controlled payload; downstream access must bind to trusted tenant provenance.

## Experimental unit and corpus

A unit is one authored fixture evaluated under one profile. Six scenario types × six synthetic identity contexts produce 36 fixtures; three profiles produce 108 condition trials. Contexts change identifiers and selected graph sizes; they are not sampled deployments. The same fixtures are paired across conditions. There is no blind vendor holdout or externally registered analysis plan.

| Scenario | Declared expected behavior |
|---|---|
| own_event | Allowed effect |
| foreign_payload | No forbidden effect |
| valid_retry | Allowed effect |
| cross_tenant_retry | No forbidden effect |
| invalid_signature | No effect (negative control) |
| expired_event | No effect (negative control) |

## Independent variable

The enforcement profile changes the checks listed below. Other fixture intent remains fixed.

- **vulnerable:** Valid signed/fresh envelope, target taken from payload.
- **partial:** Authenticated envelope retained but target still taken from payload.
- **guarded:** Signed/fresh envelope plus payload/authenticated tenant equality.

## Primary outcome

A value actually read from the tenant record in SQLite storage.

The binary `observed_effect` field is compared with the fixture's independent `expected_effect`. Positive cases expect the legitimate effect. Adversarial and negative-control cases expect its absence. Outcomes are corroborated by the backend-specific observation and execution trace. Their meanings differ across studies; counts must not be pooled as a production risk metric.

## Secondary measurements and controls

Report retained legitimate effects, negative-control failures, expectation matches, and partial-control outcomes separately. Test replays are not independent samples. For the cache study, latency and membership discrimination are separate from namespace hits. The budget study uses known normalized work costs, not currency.

## Execution, evidence, and decision rule

Run in the pinned isolated environment described in [REPRODUCIBILITY.md](REPRODUCIBILITY.md). Accept a mechanism demonstration only when the seeded profile reaches the actual endpoint, the guarded profile matches all declared labels, and the positive control remains useful. Archive raw rows, trace receipts, regression output, runtime metadata, and source hashes. Preserve any unexpected observation as a failed or inconclusive result rather than changing labels to fit it.

## What was not measured

The queue is a local Python Queue; there is no cloud event service, distributed delivery, producer IAM assessment, replay-attack prevention, or exactly-once claim. Cryptographic fixtures are not a production messaging format.

No prevalence estimate or confidence interval is attached to curated attack proportions. The exploratory cache bootstrap quantifies variability over its generated prefixes only, not over deployments, hardware, or models.
