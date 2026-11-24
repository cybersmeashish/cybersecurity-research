# Local laboratory — CAI-006

[Reproduction instructions](../REPRODUCIBILITY.md) · [Fixture corpus](fixtures.json) · [Methods](../METHOD.md).

Actual loopback HTTP redirects with a controlled resolution adapter

Both endpoints are loopback fixtures; public DNS rebinding, IPv6, HTTPS certificate binding, proxies, metadata credential extraction, and a production connector were not tested. Resolution changes are adapter-controlled. The harness forbids destinations outside its two loopback addresses and port.

No externally reachable endpoint or real credential is required. The SSRF package binds only its two loopback canaries.
