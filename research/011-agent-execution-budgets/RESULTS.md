# Measured results — CAI-011

**Evidence stage:** local controlled synthetic experiment. [Runtime record](evidence/summary.json) · [Data](evidence/results.csv) · [Traces](evidence/traces.json).

| Condition | Forbidden effects / adversarial cases | Legitimate effects / positive cases | Negative-control failures | Policy matches / all cases |
|---|---|---|---|---|
| vulnerable | 18/18 | 6/6 | 0/12 | 18/36 |
| partial | 18/18 | 6/6 | 0/12 | 18/36 |
| guarded | 0/18 | 6/6 | 0/12 | 36/36 |

The guarded profile matched every declared label and retained all positive cases in this corpus. The deliberately flawed profile is a positive failure control, so its count is not a discovery-rate estimate. The partial profile tests only its stated local control. Identical counts do not imply independently tested vendor equivalence.

**Endpoint:** Total charged normalized units exceeding the declared task budget; legitimate graph completion is reported separately.

**Interpretation:** Local accounting mechanism supported; reasoning-driven cost amplification and currency impact not measured.

## Unmeasured outcomes

Units are declared synthetic costs, not dollars, tokens, cloud billing, or actual reasoning effort. Node costs are known before admission. There is no live autonomous planner, probabilistic usage estimator, mid-flight cancellation, or distributed ledger race.

There is no confirmed new provider vulnerability or measured production sensitivity/specificity. See [the claim-to-evidence register](CLAIM-EVIDENCE.md).
