# Experiment execution record — CAI-010

The initial proposal has been expanded into an executed controlled local study. The measured phase is defined in [METHOD.md](METHOD.md); broader implementation-level validation remains future work.

- Executed fixtures: 36.
- Executed profiles: vulnerable, partial, guarded.
- Fixture-condition trials: 108.
- Regression methods: 6.
- Live-provider experiments: 0.
- Model calls: 0.

- **vulnerable:** Global namespace.
- **partial:** Caller-controlled salt only.
- **guarded:** Trusted tenant combined with caller salt.

## Measured scope

A cache namespace derived only from a caller-controlled salt can share prefix state across tenants; a trusted tenant namespace prevents cross-tenant cache hits in this fixture model.

## Ground truth and evidence

[Fixtures](lab/fixtures.json) contain expected labels before execution. [Raw results](evidence/results.csv) contain observations. [Traces](evidence/traces.json) identify the endpoint reached. [Source manifest](evidence/source-manifest.json) pins inputs.

## Original hypothesis status

Synthetic namespace and timing mechanism supported; production LLM-serving leakage not evaluated.

## Deferred experiments

Use a scoped inference deployment with real scheduling/noise, trusted gateway identities, fresh held-out prefixes, and a pre-registered sample-size calculation. Any live target needs explicit ownership/program scope. A larger legitimate workload, implementation survey, adversarial holdout corpus, and independent reproduction are pending.
