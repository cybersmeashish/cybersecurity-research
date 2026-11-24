# Experiment plan — CAI-002

**Execution status:** not started. All cases below are planned. Follow the [shared validation protocol](../HYPOTHESIS-VALIDATION.md).

## Required harness and variables

Two tenant identities, document ACLs, unique fake markers, an instrumented retriever, a summary store, and a controllable answer cache.

**Independent variables:** Caller, source ACL, cache key, artifact lineage, permission revision, and invalidation state.

Start with owned synthetic data and mock actions. Later live validation requires explicit target/method authorization and cost limits. This proposal grants no authorization to attack a service.

Record versions, configuration, fixtures, seeds, expected policy, and verified preconditions before trials.

## Planned case matrix

| Case | Condition | Procedure |
|---|---|---|
| 1 | Positive baseline | An allowed user retrieves a document and its derived answer. |
| 2 | Cross-principal cache | Prime the answer cache as user A, then query as denied user B. |
| 3 | Derived summary | Query a summary derived from sources with different access groups. |
| 4 | Revocation | Revoke access, confirm enforcement and documented propagation completion, then reuse cached or summarized artifacts. |
| 5 | Mitigation | Scope artifacts by identity and recheck source lineage before serving. |

## Measurements

- Forbidden-marker disclosure rate by response path
- Authorized-answer success rate
- Enforcement latency beyond the documented propagation window
- Added authorization latency and cache-hit-rate change

Deterministic evaluators must cover the declared fixture matrix. Model-driven experiments require independent inputs and repeated trials with pre-registered sample size, success margin, and stopping rules. Do not count repeated measurements of one input as independent cases.

## Decision criteria

**Supports the hypothesis:** A reproducible protected marker is served to a denied principal, with the ACL state and bypassed path verified.

**Evidence against it:** Every denied response path remains blocked while allowed queries succeed.

Negative results apply only to tested versions and conditions. Synthetic behavior does not establish provider behavior.

## Confounders

Eventual consistency, previously downloaded data, intentionally public sources, model memorization, and summaries containing only public facts.

## Evidence and current results

Record case ID, expected/observed decisions, actual resource effect, controls, configuration/fixture hashes, seed, and sanitized traces. Model wording alone is insufficient evidence of a protected action.

- Executed trials: **0**.
- Observed vulnerabilities: **none established**.
- Mitigation effectiveness: **not measured**.
- Independent reproduction: **pending**.
