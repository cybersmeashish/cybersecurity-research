# Measured results — CAI-008

**Evidence stage:** local controlled synthetic experiment. [Runtime record](evidence/summary.json) · [Data](evidence/results.csv) · [Traces](evidence/traces.json).

| Condition | Forbidden effects / adversarial cases | Legitimate effects / positive cases | Negative-control failures | Policy matches / all cases |
|---|---|---|---|---|
| vulnerable | 24/24 | 6/6 | 0/6 | 12/36 |
| partial | 12/24 | 6/6 | 0/6 | 24/36 |
| guarded | 0/24 | 6/6 | 0/6 | 36/36 |

The guarded profile matched every declared label and retained all positive cases in this corpus. The deliberately flawed profile is a positive failure control, so its count is not a discovery-rate estimate. The partial profile tests only its stated local control. Identical counts do not imply independently tested vendor equivalence.

**Endpoint:** A later-session mock write action derived from a recalled record.

**Interpretation:** Structured provenance mechanism supported; semantic/LLM memory poisoning not evaluated.

## Unmeasured outcomes

Compaction copies structured fields; it is not natural-language summarization. No LLM, embedding retriever, semantic trigger optimization, long-running deployment, or real user memory was tested. The result concerns provenance mechanics, not model-level memory-poisoning susceptibility.

There is no confirmed new provider vulnerability or measured production sensitivity/specificity. See [the claim-to-evidence register](CLAIM-EVIDENCE.md).
