# Experiment execution record — CAI-007

The initial proposal has been expanded into an executed controlled local study. The measured phase is defined in [METHOD.md](METHOD.md); broader implementation-level validation remains future work.

- Executed fixtures: 36.
- Executed profiles: vulnerable, partial, guarded.
- Fixture-condition trials: 108.
- Regression methods: 6.
- Live-provider experiments: 0.
- Model calls: 0.

- **vulnerable:** Schema validation without semantic action authorization.
- **partial:** Schema and local target checks.
- **guarded:** Schema, target scope, and incident/action policy.

## Measured scope

A schema-valid but unauthorized candidate action can change incident state unless an independent action policy rejects it.

## Ground truth and evidence

[Fixtures](lab/fixtures.json) contain expected labels before execution. [Raw results](evidence/results.csv) contain observations. [Traces](evidence/traces.json) identify the endpoint reached. [Source manifest](evidence/source-manifest.json) pins inputs.

## Original hypothesis status

Downstream action control supported; LLM log-to-action susceptibility not evaluated.

## Deferred experiments

Freeze a model/version, paired event corpus, and prompting policy; measure actual model-produced actions before replaying them through these gates. Any live target needs explicit ownership/program scope. A larger legitimate workload, implementation survey, adversarial holdout corpus, and independent reproduction are pending.
