# Local laboratory — CAI-009

[Reproduction instructions](../REPRODUCIBILITY.md) · [Fixture corpus](fixtures.json) · [Methods](../METHOD.md).

Signed local queue messages and tenant-scoped storage access

The queue is a local Python Queue; there is no cloud event service, distributed delivery, producer IAM assessment, replay-attack prevention, or exactly-once claim. Cryptographic fixtures are not a production messaging format.

No externally reachable endpoint or real credential is required. The SSRF package binds only its two loopback canaries.
