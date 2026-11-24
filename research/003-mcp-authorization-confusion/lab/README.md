# Local laboratory — CAI-003

[Reproduction instructions](../REPRODUCIBILITY.md) · [Fixture corpus](fixtures.json) · [Methods](../METHOD.md).

A signed-artifact proxy study of principal, client, audience, and handle ownership

The artifact is a two-part HMAC-signed JSON fixture, not an interoperable JWT. There is no browser OAuth flow, complete MCP server, consent UI, token endpoint, PKCE test, or third-party proxy assessment. Intended delegation requires a distinct documented contract.

No externally reachable endpoint or real credential is required. The SSRF package binds only its two loopback canaries.
