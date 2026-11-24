# Local laboratory — CAI-002

[Reproduction instructions](../REPRODUCIBILITY.md) · [Fixture corpus](fixtures.json) · [Methods](../METHOD.md).

A SQLite study of source permissions, cached answers, and summary lineage

No vector database, Azure search service, model-generated summary, asynchronous index propagation, conversation erasure, or customer corpus was tested. Revocation is an immediate SQLite transaction, so no claim about a provider synchronization deadline is supported.

No externally reachable endpoint or real credential is required. The SSRF package binds only its two loopback canaries.
