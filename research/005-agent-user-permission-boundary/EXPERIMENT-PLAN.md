# Experiment execution record — CAI-005

The initial proposal has been expanded into an executed controlled local study. The measured phase is defined in [METHOD.md](METHOD.md); broader implementation-level validation remains future work.

- Executed fixtures: 36.
- Executed profiles: vulnerable, partial, guarded.
- Fixture-condition trials: 108.
- Regression methods: 6.
- Live-provider experiments: 0.
- Model calls: 0.

- **vulnerable:** Shared service authority without caller authorization.
- **partial:** Read-only tool allowlist without resource ownership checks.
- **guarded:** Caller action/resource authorization at the gateway.

## Measured scope

A correctly privileged workload must also enforce the initiating user policy on the final action and resource in a user-bound execution contract.

## Ground truth and evidence

[Fixtures](lab/fixtures.json) contain expected labels before execution. [Raw results](evidence/results.csv) contain observations. [Traces](evidence/traces.json) identify the endpoint reached. [Source manifest](evidence/source-manifest.json) pins inputs.

## Original hypothesis status

Constructed local mechanism supported; implementation-level and population claims not established.

## Deferred experiments

Instrument one authorized agent framework so caller identity, task ID, final action, and resource scope can be evaluated at the tool boundary. Any live target needs explicit ownership/program scope. A larger legitimate workload, implementation survey, adversarial holdout corpus, and independent reproduction are pending.
