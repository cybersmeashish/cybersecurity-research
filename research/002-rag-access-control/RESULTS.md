# Measured results — CAI-002

**Evidence stage:** local controlled synthetic experiment. [Runtime record](evidence/summary.json) · [Data](evidence/results.csv) · [Traces](evidence/traces.json).

| Condition | Forbidden effects / adversarial cases | Legitimate effects / positive cases | Negative-control failures | Policy matches / all cases |
|---|---|---|---|---|
| vulnerable | 18/18 | 12/12 | 0/6 | 18/36 |
| partial | 12/18 | 12/12 | 0/6 | 24/36 |
| guarded | 0/18 | 12/12 | 0/6 | 36/36 |

The guarded profile matched every declared label and retained all positive cases in this corpus. The deliberately flawed profile is a positive failure control, so its count is not a discovery-rate estimate. The partial profile tests only its stated local control. Identical counts do not imply independently tested vendor equivalence.

**Endpoint:** Delivery of the unique protected marker in a returned answer.

**Interpretation:** Constructed local mechanism supported; implementation-level and population claims not established.

## Unmeasured outcomes

No vector database, Azure search service, model-generated summary, asynchronous index propagation, conversation erasure, or customer corpus was tested. Revocation is an immediate SQLite transaction, so no claim about a provider synchronization deadline is supported.

There is no confirmed new provider vulnerability or measured production sensitivity/specificity. See [the claim-to-evidence register](CLAIM-EVIDENCE.md).
