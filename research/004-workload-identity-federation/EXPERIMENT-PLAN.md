# Experiment plan — CAI-004

**Execution status:** not started. All cases below are planned. Follow the [shared validation protocol](../HYPOTHESIS-VALIDATION.md).

## Required harness and variables

A synthetic OIDC issuer, policy evaluator, sample infrastructure definitions, and fixtures with stable IDs and mutable names.

**Independent variables:** Issuer, subject mapping, stable IDs, ownership conditions, lifecycle event, and audience.

Start with owned synthetic data and mock actions. Later live validation requires explicit target/method authorization and cost limits. This proposal grants no authorization to attack a service.

Record versions, configuration, fixtures, seeds, expected policy, and verified preconditions before trials.

## Planned case matrix

| Case | Condition | Procedure |
|---|---|---|
| 1 | Positive baseline | Accept the intended issuer and stable workload identifiers. |
| 2 | Name recreation | Evaluate a valid synthetic fixture with the same name and a different stable ID. |
| 3 | Ownership change | Compare repository-only and organization-bound policies after a simulated transfer. |
| 4 | Negative control | Reject unrelated issuer or audience fixtures. |
| 5 | Mitigation | Require stable identifiers and scoped ownership conditions. |

## Measurements

- Unexpected principal mappings per policy pattern
- Legitimate-workload acceptance
- False positives for intentionally reusable identities
- Infrastructure-format coverage

Deterministic evaluators must cover the declared fixture matrix. Model-driven experiments require independent inputs and repeated trials with pre-registered sample size, success margin, and stopping rules. Do not count repeated measurements of one input as independent cases.

## Decision criteria

**Supports the hypothesis:** A local evaluator maps a distinct lifecycle fixture to a principal intended for the original identity.

**Evidence against it:** All distinct-identity fixtures are rejected while legitimate identities succeed.

Negative results apply only to tested versions and conditions. Synthetic behavior does not establish provider behavior.

## Confounders

Provider claim semantics, issuer guarantees, ownership constraints, and deliberately broad policies.

## Evidence and current results

Record case ID, expected/observed decisions, actual resource effect, controls, configuration/fixture hashes, seed, and sanitized traces. Model wording alone is insufficient evidence of a protected action.

- Executed trials: **0**.
- Observed vulnerabilities: **none established**.
- Mitigation effectiveness: **not measured**.
- Independent reproduction: **pending**.
