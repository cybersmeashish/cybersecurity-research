# Experiment plan — CAI-007

**Execution status:** not started. All cases below are planned. Follow the [shared validation protocol](../HYPOTHESIS-VALIDATION.md).

## Required harness and variables

Paired synthetic incidents, a schema-constrained workflow, labeled expected handling, and mock ticket/remediation tools.

**Independent variables:** Log field, instruction placement, schema enforcement, tool policy, and event complexity.

Start with owned synthetic data and mock actions. Later live validation requires explicit target/method authorization and cost limits. This proposal grants no authorization to attack a service.

Record versions, configuration, fixtures, seeds, expected policy, and verified preconditions before trials.

## Planned case matrix

| Case | Condition | Procedure |
|---|---|---|
| 1 | Clean baseline | Handle a seeded incident containing ordinary strings. |
| 2 | Paired adversarial log | Change only an attacker-controllable text field and compare handling. |
| 3 | Schema control | Enforce the output schema without adding action authorization. |
| 4 | Action-policy control | Enforce remediation policy outside the model. |
| 5 | Benign variation | Change non-instructional strings to estimate normal variability. |

## Measurements

- Seeded incidents incorrectly suppressed
- Forbidden mock remediation executed
- Clean-incident recall
- False-positive rate and triage time

Deterministic evaluators must cover the declared fixture matrix. Model-driven experiments require independent inputs and repeated trials with pre-registered sample size, success margin, and stopping rules. Do not count repeated measurements of one input as independent cases.

## Decision criteria

**Supports the hypothesis:** A paired trial changes protected incident state or executes a forbidden action with factual evidence held constant.

**Evidence against it:** Adversarial fields do not change protected handling beyond the pre-registered tolerance.

Negative results apply only to tested versions and conditions. Synthetic behavior does not establish provider behavior.

## Confounders

Ambiguous incident labels, stochastic decisions, factual log changes, pre-existing low recall, and prose mistaken for executed actions.

## Evidence and current results

Record case ID, expected/observed decisions, actual resource effect, controls, configuration/fixture hashes, seed, and sanitized traces. Model wording alone is insufficient evidence of a protected action.

- Executed trials: **0**.
- Observed vulnerabilities: **none established**.
- Mitigation effectiveness: **not measured**.
- Independent reproduction: **pending**.
