# Local laboratory — CAI-007

[Reproduction instructions](../REPRODUCIBILITY.md) · [Fixture corpus](fixtures.json) · [Methods](../METHOD.md).

Controlled candidate-output replay, not an LLM prompt-injection benchmark

No LLM ran and no attack-success rate for prompt injection was measured. Adversarial log wording and compromised plans are authored stimuli, not observed model outputs. This experiment validates downstream action control conditional on a bad plan; it does not establish the log-to-model causal step.

No externally reachable endpoint or real credential is required. The SSRF package binds only its two loopback canaries.
