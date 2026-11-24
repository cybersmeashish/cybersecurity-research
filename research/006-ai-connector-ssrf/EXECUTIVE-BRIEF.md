# Executive research brief — CAI-006

## Decision supported by the study

Investigate whether a selected implementation enforces this boundary: **Initial destination approval does not constrain later HTTP connections unless every redirect and the actual connected address remain inside the allowlist.**

In the constructed local corpus, the seeded profile produced 12/12 forbidden effects and the guarded profile produced none. The corrected profile retained 12/12 legitimate effects. This supports a local control design; it is not a provider finding or a deployment risk estimate.

## Conditional business impact

If the same unchecked transition exists in a production system, the relevant impact is an actual request recorded by the internal loopback http canary. Scope depends on the actual trusted role, data sensitivity, and workflow contract.

## Practical next investment

Extend the owned test harness to IPv6, HTTPS redirects, proxy behavior, and a selected connector, with synthetic metadata responses only.

## Confidence and constraints

Constructed local mechanism supported; implementation-level and population claims not established. Both endpoints are loopback fixtures; public DNS rebinding, IPv6, HTTPS certificate binding, proxies, metadata credential extraction, and a production connector were not tested. Resolution changes are adapter-controlled. The harness forbids destinations outside its two loopback addresses and port. Independent review and production validation remain pending.
