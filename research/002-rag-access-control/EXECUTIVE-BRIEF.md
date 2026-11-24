# Executive research brief — CAI-002

## Decision supported by the study

Investigate whether a selected implementation enforces this boundary: **A derived artifact must be authorized at serving time against its current source permissions, not only against the permissions used when creating it.**

In the constructed local corpus, the seeded profile produced 18/18 forbidden effects and the guarded profile produced none. The corrected profile retained 12/12 legitimate effects. This supports a local control design; it is not a provider finding or a deployment risk estimate.

## Conditional business impact

If the same unchecked transition exists in a production system, the relevant impact is delivery of the unique protected marker in a returned answer. Scope depends on the actual trusted role, data sensitivity, and workflow contract.

## Practical next investment

Validate permission propagation and derived-artifact lineage in one explicitly authorized RAG stack, including its documented update interval.

## Confidence and constraints

Constructed local mechanism supported; implementation-level and population claims not established. No vector database, Azure search service, model-generated summary, asynchronous index propagation, conversation erasure, or customer corpus was tested. Revocation is an immediate SQLite transaction, so no claim about a provider synchronization deadline is supported. Independent review and production validation remain pending.
