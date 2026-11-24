# Experiment execution record — CAI-011

The initial proposal has been expanded into an executed controlled local study. The measured phase is defined in [METHOD.md](METHOD.md); broader implementation-level validation remains future work.

- Executed fixtures: 36.
- Executed profiles: vulnerable, partial, guarded.
- Fixture-condition trials: 108.
- Regression methods: 6.
- Live-provider experiments: 0.
- Model calls: 0.

- **vulnerable:** Per-call cap with independent node attribution.
- **partial:** Per-call cap and parent task attribution, without aggregate enforcement.
- **guarded:** Atomic parent-task budget reservation and local cap.

## Measured scope

Independent per-call caps cannot bound aggregate task work; an atomic shared budget prevents the constructed retry and fan-out workloads from exceeding their declared allowance.

## Ground truth and evidence

[Fixtures](lab/fixtures.json) contain expected labels before execution. [Raw results](evidence/results.csv) contain observations. [Traces](evidence/traces.json) identify the endpoint reached. [Source manifest](evidence/source-manifest.json) pins inputs.

## Original hypothesis status

Local accounting mechanism supported; reasoning-driven cost amplification and currency impact not measured.

## Deferred experiments

Integrate conservative reservations with an owned agent runtime and reconcile observed tokens/tool charges, including committed work and cancellation. Any live target needs explicit ownership/program scope. A larger legitimate workload, implementation survey, adversarial holdout corpus, and independent reproduction are pending.
