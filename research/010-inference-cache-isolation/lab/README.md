# Local laboratory — CAI-010

[Reproduction instructions](../REPRODUCIBILITY.md) · [Fixture corpus](fixtures.json) · [Methods](../METHOD.md).

Synthetic CPU prefix caching and held-out timing probes

There are no KV tensors, GPU, vLLM server, network jitter, batching, or model inference. Cold work is 1,200 SHA-256 iterations, so the timing separation is artificial. The corrected timing AUC remains an exploratory observation; zero cross-tenant hits does not prove all side channels absent.

No externally reachable endpoint or real credential is required. The SSRF package binds only its two loopback canaries.
