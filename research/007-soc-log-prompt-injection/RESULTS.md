# Measured results — CAI-007

**Evidence stage:** local controlled synthetic experiment. [Runtime record](evidence/summary.json) · [Data](evidence/results.csv) · [Traces](evidence/traces.json).

| Condition | Forbidden effects / adversarial cases | Legitimate effects / positive cases | Negative-control failures | Policy matches / all cases |
|---|---|---|---|---|
| vulnerable | 18/18 | 12/12 | 0/6 | 18/36 |
| partial | 12/18 | 12/12 | 0/6 | 24/36 |
| guarded | 0/18 | 12/12 | 0/6 | 36/36 |

The guarded profile matched every declared label and retained all positive cases in this corpus. The deliberately flawed profile is a positive failure control, so its count is not a discovery-rate estimate. The partial profile tests only its stated local control. Identical counts do not imply independently tested vendor equivalence.

**Endpoint:** A committed disposition or alert action in the mock incident store.

**Interpretation:** Downstream action control supported; LLM log-to-action susceptibility not evaluated.

## Unmeasured outcomes

No LLM ran and no attack-success rate for prompt injection was measured. Adversarial log wording and compromised plans are authored stimuli, not observed model outputs. This experiment validates downstream action control conditional on a bad plan; it does not establish the log-to-model causal step.

There is no confirmed new provider vulnerability or measured production sensitivity/specificity. See [the claim-to-evidence register](CLAIM-EVIDENCE.md).
