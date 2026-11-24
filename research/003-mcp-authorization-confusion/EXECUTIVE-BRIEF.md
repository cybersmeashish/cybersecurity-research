# Executive research brief — CAI-003

## Decision supported by the study

Investigate whether a selected implementation enforces this boundary: **Valid signatures and expiry do not authorize a principal/client/resource mismatch; all bindings required by the declared proxy contract must hold.**

In the constructed local corpus, the seeded profile produced 24/24 forbidden effects and the guarded profile produced none. The corrected profile retained 6/6 legitimate effects. This supports a local control design; it is not a provider finding or a deployment risk estimate.

## Conditional business impact

If the same unchecked transition exists in a production system, the relevant impact is execution receipt from the mock downstream resource. Scope depends on the actual trusted role, data sensitivity, and workflow contract.

## Practical next investment

Run protocol-conformant authorization cases against a scoped proxy with real resource indicators, consent lifecycle, and protocol-version requirements.

## Confidence and constraints

Constructed local mechanism supported; implementation-level and population claims not established. The artifact is a two-part HMAC-signed JSON fixture, not an interoperable JWT. There is no browser OAuth flow, complete MCP server, consent UI, token endpoint, PKCE test, or third-party proxy assessment. Intended delegation requires a distinct documented contract. Independent review and production validation remain pending.
