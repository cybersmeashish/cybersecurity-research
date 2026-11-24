# Local laboratory — CAI-005

[Reproduction instructions](../REPRODUCIBILITY.md) · [Fixture corpus](fixtures.json) · [Methods](../METHOD.md).

A user-bound tool gateway study using a SQLite cloud API

There is no live IAM simulator, provider role assumption, autonomous LLM tool selection, or distributed delegation service. The study covers human-initiated user-bound requests; autonomous service tasks may legitimately use a different authorization policy.

No externally reachable endpoint or real credential is required. The SSRF package binds only its two loopback canaries.
