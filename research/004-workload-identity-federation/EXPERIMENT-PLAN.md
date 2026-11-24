# Experiment execution record — CAI-004

The initial proposal has been expanded into an executed controlled local study. The measured phase is defined in [METHOD.md](METHOD.md); broader implementation-level validation remains future work.

- Executed fixtures: 36.
- Executed profiles: vulnerable, partial, guarded.
- Fixture-condition trials: 108.
- Regression methods: 6.
- Live-provider experiments: 0.
- Model calls: 0.

- **vulnerable:** Issuer, audience, and mutable repository name.
- **partial:** The same rule plus a stable owner restriction.
- **guarded:** Issuer, audience, stable repository ID, and stable owner ID.

## Measured scope

A valid issuer and audience combined with a reusable repository name can map a replacement identity to the intended cloud principal; stable repository and owner IDs avoid that mapping in the declared fixture model.

## Ground truth and evidence

[Fixtures](lab/fixtures.json) contain expected labels before execution. [Raw results](evidence/results.csv) contain observations. [Traces](evidence/traces.json) identify the endpoint reached. [Source manifest](evidence/source-manifest.json) pins inputs.

## Original hypothesis status

Constructed local mechanism supported; implementation-level and population claims not established.

## Deferred experiments

Select one issuer/cloud pairing, document its immutable claim guarantees, and validate allowed lifecycle events in owned repositories. Any live target needs explicit ownership/program scope. A larger legitimate workload, implementation survey, adversarial holdout corpus, and independent reproduction are pending.
