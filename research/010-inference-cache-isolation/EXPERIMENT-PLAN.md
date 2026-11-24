# Experiment plan — CAI-010

**Execution status:** not started. All cases below are planned. Follow the [shared validation protocol](../HYPOTHESIS-VALIDATION.md).

## Required harness and variables

An isolated two-tenant inference setup, cache namespaces, randomized membership fixtures, and timing recorder.

**Independent variables:** Partitioning, salt ownership, warm/cold state, concurrency, jitter, and prefix length.

Start with owned synthetic data and mock actions. Later live validation requires explicit target/method authorization and cost limits. This proposal grants no authorization to attack a service.

Record versions, configuration, fixtures, seeds, expected policy, and verified preconditions before trials.

## Planned case matrix

| Case | Condition | Procedure |
|---|---|---|
| 1 | Shared-cache baseline | Warm prefixes in A, then measure B requests. |
| 2 | Isolation control | Assign server-side namespaces by authenticated tenant. |
| 3 | Salt manipulation | Test whether B can override or collide with A's namespace. |
| 4 | Held-out/noise | Randomize membership and load; evaluate unseen independent prefixes. |
| 5 | Utility control | Verify answer correctness and same-tenant reuse. |

## Measurements

- Held-out membership ROC-AUC and balanced accuracy
- Confidence interval versus chance
- Same-tenant cache benefit
- Cross-tenant hits and throughput impact

Deterministic evaluators must cover the declared fixture matrix. Model-driven experiments require independent inputs and repeated trials with pre-registered sample size, success margin, and stopping rules. Do not count repeated measurements of one input as independent cases.

## Decision criteria

**Supports the hypothesis:** Held-out membership accuracy exceeds a pre-registered margin under independent prefixes/noise and diminishes with isolation.

**Evidence against it:** No cross-tenant reuse exists or an adequately powered test finds accuracy indistinguishable from chance.

Negative results apply only to tested versions and conditions. Synthetic behavior does not establish provider behavior.

## Confounders

Batching, GPU scheduling, network jitter, server load, global warming, train/test prefix leakage, and unintended telemetry.

## Evidence and current results

Record case ID, expected/observed decisions, actual resource effect, controls, configuration/fixture hashes, seed, and sanitized traces. Model wording alone is insufficient evidence of a protected action.

- Executed trials: **0**.
- Observed vulnerabilities: **none established**.
- Mitigation effectiveness: **not measured**.
- Independent reproduction: **pending**.
