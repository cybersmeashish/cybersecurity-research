# Local laboratory — CAI-008

[Reproduction instructions](../REPRODUCIBILITY.md) · [Fixture corpus](fixtures.json) · [Methods](../METHOD.md).

Structured memory compaction and later-session authorization

Compaction copies structured fields; it is not natural-language summarization. No LLM, embedding retriever, semantic trigger optimization, long-running deployment, or real user memory was tested. The result concerns provenance mechanics, not model-level memory-poisoning susceptibility.

No externally reachable endpoint or real credential is required. The SSRF package binds only its two loopback canaries.
