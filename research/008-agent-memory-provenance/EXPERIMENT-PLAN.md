# Experiment execution record — CAI-008

The initial proposal has been expanded into an executed controlled local study. The measured phase is defined in [METHOD.md](METHOD.md); broader implementation-level validation remains future work.

- Executed fixtures: 36.
- Executed profiles: vulnerable, partial, guarded.
- Fixture-condition trials: 108.
- Regression methods: 6.
- Live-provider experiments: 0.
- Model calls: 0.

- **vulnerable:** Lossy structured compaction with trusted default for missing labels.
- **partial:** First-compaction label retention without complete lineage enforcement.
- **guarded:** Root-origin authorization and preserved derivation chain.

## Measured scope

Dropping trust or derivation metadata can authorize a structured recalled instruction that lacked authority at ingestion; checking an intact authorized root prevents the effect.

## Ground truth and evidence

[Fixtures](lab/fixtures.json) contain expected labels before execution. [Raw results](evidence/results.csv) contain observations. [Traces](evidence/traces.json) identify the endpoint reached. [Source manifest](evidence/source-manifest.json) pins inputs.

## Original hypothesis status

Structured provenance mechanism supported; semantic/LLM memory poisoning not evaluated.

## Deferred experiments

Measure provenance survival and enforcement in an owned semantic memory implementation across repeated compaction, eviction, and policy revision. Any live target needs explicit ownership/program scope. A larger legitimate workload, implementation survey, adversarial holdout corpus, and independent reproduction are pending.
