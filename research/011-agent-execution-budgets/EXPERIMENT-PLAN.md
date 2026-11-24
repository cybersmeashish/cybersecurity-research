# Experiment plan — CAI-011

**Execution status:** not started. All cases below are planned. Follow the [shared validation protocol](../HYPOTHESIS-VALIDATION.md).

## Required harness and variables

A deterministic execution-graph simulator, normalized cost units, configurable retries/fan-out, and an atomic budget ledger.

**Independent variables:** Depth, fan-out, retry policy, local cap, task attribution, concurrency, and cancellation.

Start with owned synthetic data and mock actions. Later live validation requires explicit target/method authorization and cost limits. This proposal grants no authorization to attack a service.

Record versions, configuration, fixtures, seeds, expected policy, and verified preconditions before trials.

## Planned case matrix

| Case | Condition | Procedure |
|---|---|---|
| 1 | Bounded baseline | Run a normal graph with known total usage. |
| 2 | Independent caps | Build repeated or nested work with each call below its own cap. |
| 3 | Concurrent fan-out | Measure reservation races across branches. |
| 4 | Timeout/retry | Ensure timed-out and retried work is charged to the originating task. |
| 5 | Mitigation | Reserve budget atomically and stop unstarted work at the aggregate limit. |

## Measurements

- Total cost units divided by task budget
- Overshoot versus allowed in-flight reservation
- Legitimate task success
- Unattributed work and cancellation delay

Deterministic evaluators must cover the declared fixture matrix. Model-driven experiments require independent inputs and repeated trials with pre-registered sample size, success margin, and stopping rules. Do not count repeated measurements of one input as independent cases.

## Decision criteria

**Supports the hypothesis:** Total usage exceeds the declared aggregate allowance while each call obeys its local cap; the shared ledger prevents excess on matched work.

**Evidence against it:** Consumption remains within the task budget and explicit in-flight allowance across the matrix.

Negative results apply only to tested versions and conditions. Synthetic behavior does not establish provider behavior.

## Confounders

Incomplete telemetry, delayed billing, price changes, intentionally unbounded tasks, and uncounted committed work.

## Evidence and current results

Record case ID, expected/observed decisions, actual resource effect, controls, configuration/fixture hashes, seed, and sanitized traces. Model wording alone is insufficient evidence of a protected action.

- Executed trials: **0**.
- Observed vulnerabilities: **none established**.
- Mitigation effectiveness: **not measured**.
- Independent reproduction: **pending**.
