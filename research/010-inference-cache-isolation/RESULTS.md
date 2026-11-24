# Measured results — CAI-010

**Evidence stage:** local controlled synthetic experiment. [Runtime record](evidence/summary.json) · [Data](evidence/results.csv) · [Traces](evidence/traces.json).

| Condition | Forbidden effects / adversarial cases | Legitimate effects / positive cases | Negative-control failures | Policy matches / all cases |
|---|---|---|---|---|
| vulnerable | 18/18 | 6/6 | 0/12 | 18/36 |
| partial | 6/18 | 6/6 | 0/12 | 30/36 |
| guarded | 0/18 | 6/6 | 0/12 | 36/36 |

The guarded profile matched every declared label and retained all positive cases in this corpus. The deliberately flawed profile is a positive failure control, so its count is not a discovery-rate estimate. The partial profile tests only its stated local control. Identical counts do not imply independently tested vendor equivalence.

**Endpoint:** A cross-tenant cache hit; timing discrimination is a separately measured endpoint.

**Interpretation:** Synthetic namespace and timing mechanism supported; production LLM-serving leakage not evaluated.

## Exploratory timing results

| Condition | Held-out ROC-AUC | 95% empirical bootstrap interval | Balanced accuracy | Cross-tenant hits / 64 probes |
|---|---|---|---|---|
| vulnerable | 1.0000 | [1.0000, 1.0000] | 1.0000 | 32 |
| partial | 1.0000 | [1.0000, 1.0000] | 1.0000 | 32 |
| guarded | 0.6401 | [0.4849, 0.7637] | 0.5000 | 0 |

Each condition used 32 own-tenant warm/cold calibration probes and 64 different held-out prefixes. The order was seeded and randomized. Each held-out prefix received one first probe. The empirical interval resamples positive and negative prefixes 400 times; it is exploratory and not a preregistered confirmatory test. The guarded AUC interval includes 0.5 in the published run. Zero cross-tenant cache hits and 0.5 threshold accuracy do not establish absence of other timing effects. CPU warmup and scheduling remain confounders. See [raw timing data](evidence/timing.csv) and [timing metrics](evidence/timing-metrics.json).

## Unmeasured outcomes

There are no KV tensors, GPU, vLLM server, network jitter, batching, or model inference. Cold work is 1,200 SHA-256 iterations, so the timing separation is artificial. The corrected timing AUC remains an exploratory observation; zero cross-tenant hits does not prove all side channels absent.

There is no confirmed new provider vulnerability or measured production sensitivity/specificity. See [the claim-to-evidence register](CLAIM-EVIDENCE.md).
