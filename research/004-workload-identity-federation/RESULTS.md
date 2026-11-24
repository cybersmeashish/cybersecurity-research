# Measured results — CAI-004

**Evidence stage:** local controlled synthetic experiment. [Runtime record](evidence/summary.json) · [Data](evidence/results.csv) · [Traces](evidence/traces.json).

| Condition | Forbidden effects / adversarial cases | Legitimate effects / positive cases | Negative-control failures | Policy matches / all cases |
|---|---|---|---|---|
| vulnerable | 12/12 | 6/12 | 0/12 | 18/36 |
| partial | 6/12 | 6/12 | 0/12 | 24/36 |
| guarded | 0/12 | 12/12 | 0/12 | 36/36 |

The guarded profile matched every declared label and retained all positive cases in this corpus. The deliberately flawed profile is a positive failure control, so its count is not a discovery-rate estimate. The partial profile tests only its stated local control. Identical counts do not imply independently tested vendor equivalence.

**Endpoint:** A successful local mapping to the synthetic cloud role.

**Interpretation:** Constructed local mechanism supported; implementation-level and population claims not established.

## Unmeasured outcomes

No GitHub repository was deleted or transferred, and no external OIDC issuer or cloud STS was invoked. Claim lifecycles and ownership transitions are supplied fixtures; actual issuer guarantees must be established separately.

There is no confirmed new provider vulnerability or measured production sensitivity/specificity. See [the claim-to-evidence register](CLAIM-EVIDENCE.md).
