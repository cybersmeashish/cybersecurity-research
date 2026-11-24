# Experiment plan — CAI-003

**Execution status:** not started. All cases below are planned. Follow the [shared validation protocol](../HYPOTHESIS-VALIDATION.md).

## Required harness and variables

Two users, two clients, one proxy, two mock resources, and an isolated authorization server.

**Independent variables:** User/client pairing, audience, consent-cache key, handle ownership, expiry, logout, and revocation.

Start with owned synthetic data and mock actions. Later live validation requires explicit target/method authorization and cost limits. This proposal grants no authorization to attack a service.

Record versions, configuration, fixtures, seeds, expected policy, and verified preconditions before trials.

## Planned case matrix

| Case | Condition | Procedure |
|---|---|---|
| 1 | Positive baseline | Each user completes their own consent and invokes a permitted tool. |
| 2 | Principal mismatch | Present user A's synthetic workflow handle while authenticated as user B. |
| 3 | Client/resource mismatch | Use own mock tokens against a different client or resource audience. |
| 4 | Lifecycle | Repeat matched and mismatched requests after logout, expiry, and revocation. |
| 5 | Mitigation | Enforce principal ownership, resource audience, and client-specific consent. |

## Measurements

- Unauthorized tool invocations by mismatch class
- Accepted foreign workflow handles
- Authorized-flow completion rate
- False positives for intended delegation

Deterministic evaluators must cover the declared fixture matrix. Model-driven experiments require independent inputs and repeated trials with pre-registered sample size, success margin, and stopping rules. Do not count repeated measurements of one input as independent cases.

## Decision criteria

**Supports the hypothesis:** A forbidden mock action executes or another principal's protected marker is returned.

**Evidence against it:** All mismatches are rejected and documented delegation works.

Negative results apply only to tested versions and conditions. Synthetic behavior does not establish provider behavior.

## Confounders

Intentionally shared clients, public tools, documented delegation, protocol-version differences, and fixture issuer errors.

## Evidence and current results

Record case ID, expected/observed decisions, actual resource effect, controls, configuration/fixture hashes, seed, and sanitized traces. Model wording alone is insufficient evidence of a protected action.

- Executed trials: **0**.
- Observed vulnerabilities: **none established**.
- Mitigation effectiveness: **not measured**.
- Independent reproduction: **pending**.
