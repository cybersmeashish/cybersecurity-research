# Measured results — CAI-009

**Evidence stage:** local controlled synthetic experiment. [Runtime record](evidence/summary.json) · [Data](evidence/results.csv) · [Traces](evidence/traces.json).

| Condition | Forbidden effects / adversarial cases | Legitimate effects / positive cases | Negative-control failures | Policy matches / all cases |
|---|---|---|---|---|
| vulnerable | 12/12 | 12/12 | 0/12 | 24/36 |
| partial | 12/12 | 12/12 | 0/12 | 24/36 |
| guarded | 0/12 | 12/12 | 0/12 | 36/36 |

The guarded profile matched every declared label and retained all positive cases in this corpus. The deliberately flawed profile is a positive failure control, so its count is not a discovery-rate estimate. The partial profile tests only its stated local control. Identical counts do not imply independently tested vendor equivalence.

**Endpoint:** A value actually read from the tenant record in SQLite storage.

**Interpretation:** Constructed local mechanism supported; implementation-level and population claims not established.

## Unmeasured outcomes

The queue is a local Python Queue; there is no cloud event service, distributed delivery, producer IAM assessment, replay-attack prevention, or exactly-once claim. Cryptographic fixtures are not a production messaging format.

There is no confirmed new provider vulnerability or measured production sensitivity/specificity. See [the claim-to-evidence register](CLAIM-EVIDENCE.md).
