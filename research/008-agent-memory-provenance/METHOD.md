# Method and measurement contract — CAI-008

## Evaluated proposition

Dropping trust or derivation metadata can authorize a structured recalled instruction that lacked authority at ingestion; checking an intact authorized root prevents the effect.

## Experimental unit and corpus

A unit is one authored fixture evaluated under one profile. Six scenario types × six synthetic identity contexts produce 36 fixtures; three profiles produce 108 condition trials. Contexts change identifiers and selected graph sizes; they are not sampled deployments. The same fixtures are paired across conditions. There is no blind vendor holdout or externally registered analysis plan.

| Scenario | Declared expected behavior |
|---|---|
| trusted_instruction | Allowed effect |
| raw_lowtrust | No effect (negative control) |
| summary_lost_label | No forbidden effect |
| double_compaction | No forbidden effect |
| unbound_derivation | No forbidden effect |
| evicted_source | No forbidden effect |

## Independent variable

The enforcement profile changes the checks listed below. Other fixture intent remains fixed.

- **vulnerable:** Lossy structured compaction with trusted default for missing labels.
- **partial:** First-compaction label retention without complete lineage enforcement.
- **guarded:** Root-origin authorization and preserved derivation chain.

## Primary outcome

A later-session mock write action derived from a recalled record.

The binary `observed_effect` field is compared with the fixture's independent `expected_effect`. Positive cases expect the legitimate effect. Adversarial and negative-control cases expect its absence. Outcomes are corroborated by the backend-specific observation and execution trace. Their meanings differ across studies; counts must not be pooled as a production risk metric.

## Secondary measurements and controls

Report retained legitimate effects, negative-control failures, expectation matches, and partial-control outcomes separately. Test replays are not independent samples. For the cache study, latency and membership discrimination are separate from namespace hits. The budget study uses known normalized work costs, not currency.

## Execution, evidence, and decision rule

Run in the pinned isolated environment described in [REPRODUCIBILITY.md](REPRODUCIBILITY.md). Accept a mechanism demonstration only when the seeded profile reaches the actual endpoint, the guarded profile matches all declared labels, and the positive control remains useful. Archive raw rows, trace receipts, regression output, runtime metadata, and source hashes. Preserve any unexpected observation as a failed or inconclusive result rather than changing labels to fit it.

## What was not measured

Compaction copies structured fields; it is not natural-language summarization. No LLM, embedding retriever, semantic trigger optimization, long-running deployment, or real user memory was tested. The result concerns provenance mechanics, not model-level memory-poisoning susceptibility.

No prevalence estimate or confidence interval is attached to curated attack proportions. The exploratory cache bootstrap quantifies variability over its generated prefixes only, not over deployments, hardware, or models.
