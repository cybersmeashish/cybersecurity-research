# Experiment plan — CAI-009

**Execution status:** not started. All cases below are planned. Follow the [shared validation protocol](../HYPOTHESIS-VALIDATION.md).

## Required harness and variables

A local API/queue/function/storage workflow, two tenant partitions, producer identities, and service-role policies.

**Independent variables:** Payload tenant, authenticated tenant, event provenance, consumer privileges, retries, and replay.

Start with owned synthetic data and mock actions. Later live validation requires explicit target/method authorization and cost limits. This proposal grants no authorization to attack a service.

Record versions, configuration, fixtures, seeds, expected policy, and verified preconditions before trials.

## Planned case matrix

| Case | Condition | Procedure |
|---|---|---|
| 1 | Direct denial | Confirm tenant A cannot directly read tenant B data. |
| 2 | Authorized event | Submit an A event targeting A storage. |
| 3 | Payload substitution | Change only the user-controlled tenant field to B. |
| 4 | Retry/replay | Check binding across consumer retries and replay. |
| 5 | Mitigation | Bind tenant provenance at ingress and enforce it at resource access. |

## Measurements

- Cross-tenant storage actions
- Authorized event completion
- Identity lineage retained per hop
- Scanner precision on annotated flows

Deterministic evaluators must cover the declared fixture matrix. Model-driven experiments require independent inputs and repeated trials with pre-registered sample size, success margin, and stopping rules. Do not count repeated measurements of one input as independent cases.

## Decision criteria

**Supports the hypothesis:** A cross-tenant mock storage action executes through the event chain with the lost binding identified.

**Evidence against it:** Every payload/provenance mismatch is blocked while legitimate workflows succeed.

Negative results apply only to tested versions and conditions. Synthetic behavior does not establish provider behavior.

## Confounders

Explicit administrative workflows, spoofable fixture ingress, intentionally shared resources, and service-role fixture errors.

## Evidence and current results

Record case ID, expected/observed decisions, actual resource effect, controls, configuration/fixture hashes, seed, and sanitized traces. Model wording alone is insufficient evidence of a protected action.

- Executed trials: **0**.
- Observed vulnerabilities: **none established**.
- Mitigation effectiveness: **not measured**.
- Independent reproduction: **pending**.
