# Measured results — CAI-006

**Evidence stage:** local controlled synthetic experiment. [Runtime record](evidence/summary.json) · [Data](evidence/results.csv) · [Traces](evidence/traces.json).

| Condition | Forbidden effects / adversarial cases | Legitimate effects / positive cases | Negative-control failures | Policy matches / all cases |
|---|---|---|---|---|
| vulnerable | 12/12 | 12/12 | 0/12 | 24/36 |
| partial | 6/12 | 12/12 | 0/12 | 30/36 |
| guarded | 0/12 | 12/12 | 0/12 | 36/36 |

The guarded profile matched every declared label and retained all positive cases in this corpus. The deliberately flawed profile is a positive failure control, so its count is not a discovery-rate estimate. The partial profile tests only its stated local control. Identical counts do not imply independently tested vendor equivalence.

**Endpoint:** An actual request recorded by the internal loopback HTTP canary.

**Interpretation:** Constructed local mechanism supported; implementation-level and population claims not established.

## Unmeasured outcomes

Both endpoints are loopback fixtures; public DNS rebinding, IPv6, HTTPS certificate binding, proxies, metadata credential extraction, and a production connector were not tested. Resolution changes are adapter-controlled. The harness forbids destinations outside its two loopback addresses and port.

There is no confirmed new provider vulnerability or measured production sensitivity/specificity. See [the claim-to-evidence register](CLAIM-EVIDENCE.md).
