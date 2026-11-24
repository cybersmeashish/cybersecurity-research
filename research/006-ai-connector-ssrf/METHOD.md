# Method and measurement contract — CAI-006

## Evaluated proposition

Initial destination approval does not constrain later HTTP connections unless every redirect and the actual connected address remain inside the allowlist.

## Experimental unit and corpus

A unit is one authored fixture evaluated under one profile. Six scenario types × six synthetic identity contexts produce 36 fixtures; three profiles produce 108 condition trials. Contexts change identifiers and selected graph sizes; they are not sampled deployments. The same fixtures are paired across conditions. There is no blind vendor holdout or externally registered analysis plan.

| Scenario | Declared expected behavior |
|---|---|
| allowed | Allowed effect |
| redirect_internal | No forbidden effect |
| redirect_allowed | Allowed effect |
| dns_change | No forbidden effect |
| forbidden_initial | No effect (negative control) |
| plain_internal | No effect (negative control) |

## Independent variable

The enforcement profile changes the checks listed below. Other fixture intent remains fixed.

- **vulnerable:** Only the initial resolved destination is approved.
- **partial:** Each advertised redirect hostname is checked, but connection resolution can differ.
- **guarded:** Checked address pinned to the connection; every redirect destination validated.

## Primary outcome

An actual request recorded by the internal loopback HTTP canary.

The binary `observed_effect` field is compared with the fixture's independent `expected_effect`. Positive cases expect the legitimate effect. Adversarial and negative-control cases expect its absence. Outcomes are corroborated by the backend-specific observation and execution trace. Their meanings differ across studies; counts must not be pooled as a production risk metric.

## Secondary measurements and controls

Report retained legitimate effects, negative-control failures, expectation matches, and partial-control outcomes separately. Test replays are not independent samples. For the cache study, latency and membership discrimination are separate from namespace hits. The budget study uses known normalized work costs, not currency.

## Execution, evidence, and decision rule

Run in the pinned isolated environment described in [REPRODUCIBILITY.md](REPRODUCIBILITY.md). Accept a mechanism demonstration only when the seeded profile reaches the actual endpoint, the guarded profile matches all declared labels, and the positive control remains useful. Archive raw rows, trace receipts, regression output, runtime metadata, and source hashes. Preserve any unexpected observation as a failed or inconclusive result rather than changing labels to fit it.

## What was not measured

Both endpoints are loopback fixtures; public DNS rebinding, IPv6, HTTPS certificate binding, proxies, metadata credential extraction, and a production connector were not tested. Resolution changes are adapter-controlled. The harness forbids destinations outside its two loopback addresses and port.

No prevalence estimate or confidence interval is attached to curated attack proportions. The exploratory cache bootstrap quantifies variability over its generated prefixes only, not over deployments, hardware, or models.
