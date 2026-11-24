# Executive research brief — CAI-008

## Decision supported by the study

Investigate whether a selected implementation enforces this boundary: **Dropping trust or derivation metadata can authorize a structured recalled instruction that lacked authority at ingestion; checking an intact authorized root prevents the effect.**

In the constructed local corpus, the seeded profile produced 24/24 forbidden effects and the guarded profile produced none. The corrected profile retained 6/6 legitimate effects. This supports a local control design; it is not a provider finding or a deployment risk estimate.

## Conditional business impact

If the same unchecked transition exists in a production system, the relevant impact is a later-session mock write action derived from a recalled record. Scope depends on the actual trusted role, data sensitivity, and workflow contract.

## Practical next investment

Measure provenance survival and enforcement in an owned semantic memory implementation across repeated compaction, eviction, and policy revision.

## Confidence and constraints

Structured provenance mechanism supported; semantic/LLM memory poisoning not evaluated. Compaction copies structured fields; it is not natural-language summarization. No LLM, embedding retriever, semantic trigger optimization, long-running deployment, or real user memory was tested. The result concerns provenance mechanics, not model-level memory-poisoning susceptibility. Independent review and production validation remain pending.
