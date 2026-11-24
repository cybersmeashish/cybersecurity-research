# Experiment execution record — CAI-002

The initial proposal has been expanded into an executed controlled local study. The measured phase is defined in [METHOD.md](METHOD.md); broader implementation-level validation remains future work.

- Executed fixtures: 36.
- Executed profiles: vulnerable, partial, guarded.
- Fixture-condition trials: 108.
- Regression methods: 6.
- Live-provider experiments: 0.
- Model calls: 0.

- **vulnerable:** Initial source ACL only; artifacts served without current lineage checks.
- **partial:** Principal-scoped answer cache; summaries and same-principal revocation remain unchecked.
- **guarded:** Current source ACL checked before all artifact delivery.

## Measured scope

A derived artifact must be authorized at serving time against its current source permissions, not only against the permissions used when creating it.

## Ground truth and evidence

[Fixtures](lab/fixtures.json) contain expected labels before execution. [Raw results](evidence/results.csv) contain observations. [Traces](evidence/traces.json) identify the endpoint reached. [Source manifest](evidence/source-manifest.json) pins inputs.

## Original hypothesis status

Constructed local mechanism supported; implementation-level and population claims not established.

## Deferred experiments

Validate permission propagation and derived-artifact lineage in one explicitly authorized RAG stack, including its documented update interval. Any live target needs explicit ownership/program scope. A larger legitimate workload, implementation survey, adversarial holdout corpus, and independent reproduction are pending.
