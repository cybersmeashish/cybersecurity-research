# Executive research brief — CAI-011

## Decision supported by the study

Investigate whether a selected implementation enforces this boundary: **Independent per-call caps cannot bound aggregate task work; an atomic shared budget prevents the constructed retry and fan-out workloads from exceeding their declared allowance.**

In the constructed local corpus, the seeded profile produced 18/18 forbidden effects and the guarded profile produced none. The corrected profile retained 6/6 legitimate effects. This supports a local control design; it is not a provider finding or a deployment risk estimate.

## Conditional business impact

If the same unchecked transition exists in a production system, the relevant impact is total charged normalized units exceeding the declared task budget; legitimate graph completion is reported separately. Scope depends on the actual trusted role, data sensitivity, and workflow contract.

## Practical next investment

Integrate conservative reservations with an owned agent runtime and reconcile observed tokens/tool charges, including committed work and cancellation.

## Confidence and constraints

Local accounting mechanism supported; reasoning-driven cost amplification and currency impact not measured. Units are declared synthetic costs, not dollars, tokens, cloud billing, or actual reasoning effort. Node costs are known before admission. There is no live autonomous planner, probabilistic usage estimator, mid-flight cancellation, or distributed ledger race. Independent review and production validation remain pending.
