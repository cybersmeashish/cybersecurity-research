# Method and measurement contract — CAI-005

## Evaluated proposition

A correctly privileged workload must also enforce the initiating user policy on the final action and resource in a user-bound execution contract.

## Experimental unit and corpus

A unit is one authored fixture evaluated under one profile. Six scenario types × six synthetic identity contexts produce 36 fixtures; three profiles produce 108 condition trials. Contexts change identifiers and selected graph sizes; they are not sampled deployments. The same fixtures are paired across conditions. There is no blind vendor holdout or externally registered analysis plan.

| Scenario | Declared expected behavior |
|---|---|
| allowed_read | Allowed effect |
| denied_write | No forbidden effect |
| wrong_resource | No forbidden effect |
| indirect_write | No forbidden effect |
| delegated_write | No forbidden effect |
| denied_direct | No effect (negative control) |

## Independent variable

The enforcement profile changes the checks listed below. Other fixture intent remains fixed.

- **vulnerable:** Shared service authority without caller authorization.
- **partial:** Read-only tool allowlist without resource ownership checks.
- **guarded:** Caller action/resource authorization at the gateway.

## Primary outcome

A served record value or a committed update in the mock API database.

The binary `observed_effect` field is compared with the fixture's independent `expected_effect`. Positive cases expect the legitimate effect. Adversarial and negative-control cases expect its absence. Outcomes are corroborated by the backend-specific observation and execution trace. Their meanings differ across studies; counts must not be pooled as a production risk metric.

## Secondary measurements and controls

Report retained legitimate effects, negative-control failures, expectation matches, and partial-control outcomes separately. Test replays are not independent samples. For the cache study, latency and membership discrimination are separate from namespace hits. The budget study uses known normalized work costs, not currency.

## Execution, evidence, and decision rule

Run in the pinned isolated environment described in [REPRODUCIBILITY.md](REPRODUCIBILITY.md). Accept a mechanism demonstration only when the seeded profile reaches the actual endpoint, the guarded profile matches all declared labels, and the positive control remains useful. Archive raw rows, trace receipts, regression output, runtime metadata, and source hashes. Preserve any unexpected observation as a failed or inconclusive result rather than changing labels to fit it.

## What was not measured

There is no live IAM simulator, provider role assumption, autonomous LLM tool selection, or distributed delegation service. The study covers human-initiated user-bound requests; autonomous service tasks may legitimately use a different authorization policy.

No prevalence estimate or confidence interval is attached to curated attack proportions. The exploratory cache bootstrap quantifies variability over its generated prefixes only, not over deployments, hardware, or models.
