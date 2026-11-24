# Measured results — CAI-005

**Evidence stage:** local controlled synthetic experiment. [Runtime record](evidence/summary.json) · [Data](evidence/results.csv) · [Traces](evidence/traces.json).

| Condition | Forbidden effects / adversarial cases | Legitimate effects / positive cases | Negative-control failures | Policy matches / all cases |
|---|---|---|---|---|
| vulnerable | 24/24 | 6/6 | 0/6 | 12/36 |
| partial | 6/24 | 6/6 | 0/6 | 30/36 |
| guarded | 0/24 | 6/6 | 0/6 | 36/36 |

The guarded profile matched every declared label and retained all positive cases in this corpus. The deliberately flawed profile is a positive failure control, so its count is not a discovery-rate estimate. The partial profile tests only its stated local control. Identical counts do not imply independently tested vendor equivalence.

**Endpoint:** A served record value or a committed update in the mock API database.

**Interpretation:** Constructed local mechanism supported; implementation-level and population claims not established.

## Unmeasured outcomes

There is no live IAM simulator, provider role assumption, autonomous LLM tool selection, or distributed delegation service. The study covers human-initiated user-bound requests; autonomous service tasks may legitimately use a different authorization policy.

There is no confirmed new provider vulnerability or measured production sensitivity/specificity. See [the claim-to-evidence register](CLAIM-EVIDENCE.md).
