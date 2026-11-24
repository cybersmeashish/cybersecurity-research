# Experiment plan — CAI-006

**Execution status:** not started. All cases below are planned. Follow the [shared validation protocol](../HYPOTHESIS-VALIDATION.md).

## Required harness and variables

An isolated test network, controlled resolver, redirect fixture, internal canary, and emulated metadata endpoint; no real metadata credentials.

**Independent variables:** Redirect chain, DNS changes, IP family, connected address, validation timing, and fetch path.

Start with owned synthetic data and mock actions. Later live validation requires explicit target/method authorization and cost limits. This proposal grants no authorization to attack a service.

Record versions, configuration, fixtures, seeds, expected policy, and verified preconditions before trials.

## Planned case matrix

| Case | Condition | Procedure |
|---|---|---|
| 1 | Positive baseline | Fetch a permitted external fixture. |
| 2 | Redirect transition | Redirect that fixture toward an internal canary. |
| 3 | Resolution transition | Use controlled differing answers at validation and connection time. |
| 4 | Discovery path | Apply destination checks to mock authorization metadata discovery. |
| 5 | Mitigation | Validate actual destinations and every redirect hop against the policy. |

## Measurements

- Internal canary requests received
- Forbidden response-marker exposure
- Allowed-fetch success
- Coverage of fetch and discovery paths

Deterministic evaluators must cover the declared fixture matrix. Model-driven experiments require independent inputs and repeated trials with pre-registered sample size, success margin, and stopping rules. Do not count repeated measurements of one input as independent cases.

## Decision criteria

**Supports the hypothesis:** The canary records a connector-initiated request forbidden by the declared policy.

**Evidence against it:** No forbidden destination is contacted and allowed fetches succeed.

Negative results apply only to tested versions and conditions. Synthetic behavior does not establish provider behavior.

## Confounders

Explicitly permitted private integrations, proxy behavior, DNS-fixture errors, and connection attempts mistaken for successful contact.

## Evidence and current results

Record case ID, expected/observed decisions, actual resource effect, controls, configuration/fixture hashes, seed, and sanitized traces. Model wording alone is insufficient evidence of a protected action.

- Executed trials: **0**.
- Observed vulnerabilities: **none established**.
- Mitigation effectiveness: **not measured**.
- Independent reproduction: **pending**.
