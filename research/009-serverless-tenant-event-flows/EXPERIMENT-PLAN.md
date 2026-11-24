# Experiment execution record — CAI-009

The initial proposal has been expanded into an executed controlled local study. The measured phase is defined in [METHOD.md](METHOD.md); broader implementation-level validation remains future work.

- Executed fixtures: 36.
- Executed profiles: vulnerable, partial, guarded.
- Fixture-condition trials: 108.
- Regression methods: 6.
- Live-provider experiments: 0.
- Model calls: 0.

- **vulnerable:** Valid signed/fresh envelope, target taken from payload.
- **partial:** Authenticated envelope retained but target still taken from payload.
- **guarded:** Signed/fresh envelope plus payload/authenticated tenant equality.

## Measured scope

Signature and producer authenticity do not authorize a tenant value inside the producer-controlled payload; downstream access must bind to trusted tenant provenance.

## Ground truth and evidence

[Fixtures](lab/fixtures.json) contain expected labels before execution. [Raw results](evidence/results.csv) contain observations. [Traces](evidence/traces.json) identify the endpoint reached. [Source manifest](evidence/source-manifest.json) pins inputs.

## Original hypothesis status

Constructed local mechanism supported; implementation-level and population claims not established.

## Deferred experiments

Trace one owned API-to-queue-to-function workflow, including dead-letter paths, retry context, and storage authorization. Any live target needs explicit ownership/program scope. A larger legitimate workload, implementation survey, adversarial holdout corpus, and independent reproduction are pending.
