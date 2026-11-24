# Executive research brief — CAI-004

## Decision supported by the study

Investigate whether a selected implementation enforces this boundary: **A valid issuer and audience combined with a reusable repository name can map a replacement identity to the intended cloud principal; stable repository and owner IDs avoid that mapping in the declared fixture model.**

In the constructed local corpus, the seeded profile produced 12/12 forbidden effects and the guarded profile produced none. The corrected profile retained 12/12 legitimate effects. This supports a local control design; it is not a provider finding or a deployment risk estimate.

## Conditional business impact

If the same unchecked transition exists in a production system, the relevant impact is a successful local mapping to the synthetic cloud role. Scope depends on the actual trusted role, data sensitivity, and workflow contract.

## Practical next investment

Select one issuer/cloud pairing, document its immutable claim guarantees, and validate allowed lifecycle events in owned repositories.

## Confidence and constraints

Constructed local mechanism supported; implementation-level and population claims not established. No GitHub repository was deleted or transferred, and no external OIDC issuer or cloud STS was invoked. Claim lifecycles and ownership transitions are supplied fixtures; actual issuer guarantees must be established separately. Independent review and production validation remain pending.
