# Experiment execution record — CAI-003

The initial proposal has been expanded into an executed controlled local study. The measured phase is defined in [METHOD.md](METHOD.md); broader implementation-level validation remains future work.

- Executed fixtures: 36.
- Executed profiles: vulnerable, partial, guarded.
- Fixture-condition trials: 108.
- Regression methods: 6.
- Live-provider experiments: 0.
- Model calls: 0.

- **vulnerable:** Signature, issuer, and expiry checks.
- **partial:** The same checks plus caller/subject binding.
- **guarded:** All declared subject, client, audience, and handle-owner bindings.

## Measured scope

Valid signatures and expiry do not authorize a principal/client/resource mismatch; all bindings required by the declared proxy contract must hold.

## Ground truth and evidence

[Fixtures](lab/fixtures.json) contain expected labels before execution. [Raw results](evidence/results.csv) contain observations. [Traces](evidence/traces.json) identify the endpoint reached. [Source manifest](evidence/source-manifest.json) pins inputs.

## Original hypothesis status

Constructed local mechanism supported; implementation-level and population claims not established.

## Deferred experiments

Run protocol-conformant authorization cases against a scoped proxy with real resource indicators, consent lifecycle, and protocol-version requirements. Any live target needs explicit ownership/program scope. A larger legitimate workload, implementation survey, adversarial holdout corpus, and independent reproduction are pending.
