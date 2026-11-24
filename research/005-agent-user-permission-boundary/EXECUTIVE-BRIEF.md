# Executive research brief — CAI-005

## Decision supported by the study

Investigate whether a selected implementation enforces this boundary: **A correctly privileged workload must also enforce the initiating user policy on the final action and resource in a user-bound execution contract.**

In the constructed local corpus, the seeded profile produced 24/24 forbidden effects and the guarded profile produced none. The corrected profile retained 6/6 legitimate effects. This supports a local control design; it is not a provider finding or a deployment risk estimate.

## Conditional business impact

If the same unchecked transition exists in a production system, the relevant impact is a served record value or a committed update in the mock api database. Scope depends on the actual trusted role, data sensitivity, and workflow contract.

## Practical next investment

Instrument one authorized agent framework so caller identity, task ID, final action, and resource scope can be evaluated at the tool boundary.

## Confidence and constraints

Constructed local mechanism supported; implementation-level and population claims not established. There is no live IAM simulator, provider role assumption, autonomous LLM tool selection, or distributed delegation service. The study covers human-initiated user-bound requests; autonomous service tasks may legitimately use a different authorization policy. Independent review and production validation remain pending.
