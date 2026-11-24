# Method and measurement contract — CAI-011

## Evaluated proposition

Independent per-call caps cannot bound aggregate task work; an atomic shared budget prevents the constructed retry and fan-out workloads from exceeding their declared allowance.

## Experimental unit and corpus

A unit is one authored fixture evaluated under one profile. Six scenario types × six synthetic identity contexts produce 36 fixtures; three profiles produce 108 condition trials. Contexts change identifiers and selected graph sizes; they are not sampled deployments. The same fixtures are paired across conditions. There is no blind vendor holdout or externally registered analysis plan.

| Scenario | Declared expected behavior |
|---|---|
| normal_graph | Allowed effect |
| fanout | No forbidden effect |
| retries | No forbidden effect |
| concurrent | No forbidden effect |
| oversized_call | No effect (negative control) |
| cancelled_task | No effect (negative control) |

## Independent variable

The enforcement profile changes the checks listed below. Other fixture intent remains fixed.

- **vulnerable:** Per-call cap with independent node attribution.
- **partial:** Per-call cap and parent task attribution, without aggregate enforcement.
- **guarded:** Atomic parent-task budget reservation and local cap.

## Primary outcome

Total charged normalized units exceeding the declared task budget; legitimate graph completion is reported separately.

The binary `observed_effect` field is compared with the fixture's independent `expected_effect`. Positive cases expect the legitimate effect. Adversarial and negative-control cases expect its absence. Outcomes are corroborated by the backend-specific observation and execution trace. Their meanings differ across studies; counts must not be pooled as a production risk metric.

## Secondary measurements and controls

Report retained legitimate effects, negative-control failures, expectation matches, and partial-control outcomes separately. Test replays are not independent samples. For the cache study, latency and membership discrimination are separate from namespace hits. The budget study uses known normalized work costs, not currency.

## Execution, evidence, and decision rule

Run in the pinned isolated environment described in [REPRODUCIBILITY.md](REPRODUCIBILITY.md). Accept a mechanism demonstration only when the seeded profile reaches the actual endpoint, the guarded profile matches all declared labels, and the positive control remains useful. Archive raw rows, trace receipts, regression output, runtime metadata, and source hashes. Preserve any unexpected observation as a failed or inconclusive result rather than changing labels to fit it.

## What was not measured

Units are declared synthetic costs, not dollars, tokens, cloud billing, or actual reasoning effort. Node costs are known before admission. There is no live autonomous planner, probabilistic usage estimator, mid-flight cancellation, or distributed ledger race.

No prevalence estimate or confidence interval is attached to curated attack proportions. The exploratory cache bootstrap quantifies variability over its generated prefixes only, not over deployments, hardware, or models.
