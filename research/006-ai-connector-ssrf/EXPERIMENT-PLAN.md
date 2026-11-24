# Experiment execution record — CAI-006

The initial proposal has been expanded into an executed controlled local study. The measured phase is defined in [METHOD.md](METHOD.md); broader implementation-level validation remains future work.

- Executed fixtures: 36.
- Executed profiles: vulnerable, partial, guarded.
- Fixture-condition trials: 108.
- Regression methods: 6.
- Live-provider experiments: 0.
- Model calls: 0.

- **vulnerable:** Only the initial resolved destination is approved.
- **partial:** Each advertised redirect hostname is checked, but connection resolution can differ.
- **guarded:** Checked address pinned to the connection; every redirect destination validated.

## Measured scope

Initial destination approval does not constrain later HTTP connections unless every redirect and the actual connected address remain inside the allowlist.

## Ground truth and evidence

[Fixtures](lab/fixtures.json) contain expected labels before execution. [Raw results](evidence/results.csv) contain observations. [Traces](evidence/traces.json) identify the endpoint reached. [Source manifest](evidence/source-manifest.json) pins inputs.

## Original hypothesis status

Constructed local mechanism supported; implementation-level and population claims not established.

## Deferred experiments

Extend the owned test harness to IPv6, HTTPS redirects, proxy behavior, and a selected connector, with synthetic metadata responses only. Any live target needs explicit ownership/program scope. A larger legitimate workload, implementation survey, adversarial holdout corpus, and independent reproduction are pending.
