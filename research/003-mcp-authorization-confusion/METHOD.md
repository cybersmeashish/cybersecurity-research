# Method and measurement contract — CAI-003

## Evaluated proposition

Valid signatures and expiry do not authorize a principal/client/resource mismatch; all bindings required by the declared proxy contract must hold.

## Experimental unit and corpus

A unit is one authored fixture evaluated under one profile. Six scenario types × six synthetic identity contexts produce 36 fixtures; three profiles produce 108 condition trials. Contexts change identifiers and selected graph sizes; they are not sampled deployments. The same fixtures are paired across conditions. There is no blind vendor holdout or externally registered analysis plan.

| Scenario | Declared expected behavior |
|---|---|
| allowed | Allowed effect |
| expired | No effect (negative control) |
| foreign_subject | No forbidden effect |
| foreign_client | No forbidden effect |
| wrong_audience | No forbidden effect |
| foreign_handle | No forbidden effect |

## Independent variable

The enforcement profile changes the checks listed below. Other fixture intent remains fixed.

- **vulnerable:** Signature, issuer, and expiry checks.
- **partial:** The same checks plus caller/subject binding.
- **guarded:** All declared subject, client, audience, and handle-owner bindings.

## Primary outcome

Execution receipt from the mock downstream resource.

The binary `observed_effect` field is compared with the fixture's independent `expected_effect`. Positive cases expect the legitimate effect. Adversarial and negative-control cases expect its absence. Outcomes are corroborated by the backend-specific observation and execution trace. Their meanings differ across studies; counts must not be pooled as a production risk metric.

## Secondary measurements and controls

Report retained legitimate effects, negative-control failures, expectation matches, and partial-control outcomes separately. Test replays are not independent samples. For the cache study, latency and membership discrimination are separate from namespace hits. The budget study uses known normalized work costs, not currency.

## Execution, evidence, and decision rule

Run in the pinned isolated environment described in [REPRODUCIBILITY.md](REPRODUCIBILITY.md). Accept a mechanism demonstration only when the seeded profile reaches the actual endpoint, the guarded profile matches all declared labels, and the positive control remains useful. Archive raw rows, trace receipts, regression output, runtime metadata, and source hashes. Preserve any unexpected observation as a failed or inconclusive result rather than changing labels to fit it.

## What was not measured

The artifact is a two-part HMAC-signed JSON fixture, not an interoperable JWT. There is no browser OAuth flow, complete MCP server, consent UI, token endpoint, PKCE test, or third-party proxy assessment. Intended delegation requires a distinct documented contract.

No prevalence estimate or confidence interval is attached to curated attack proportions. The exploratory cache bootstrap quantifies variability over its generated prefixes only, not over deployments, hardware, or models.
