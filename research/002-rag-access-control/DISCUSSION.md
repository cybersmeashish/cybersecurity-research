# Interpretation and implications — CAI-002

## Mechanistic explanation

The source query checks an ACL table, but the cache or summary path can return an already materialized marker without consulting that table. Cache-key scoping stops reuse by a different principal while leaving same-principal revocation and unscoped summaries exposed. The guarded path reevaluates the current source ACL before delivering an artifact.

## Why the partial control matters

The partial profile produced 12/18 forbidden effects while preserving 12/12 legitimate effects. It changes a specific check, not the declared policy. The corrected gate aligns the final effect with that policy. A production integration must expose the same trusted context to implement the gate.

## Alternative explanations

The flawed profiles were deliberately constructed to exercise known classes; their failure is not evidence of prevalence or novelty. The corrected code was authored with knowledge of this corpus, so unseen attack families and complex legitimate workflows remain a threat to generalization. Nominal identity contexts do not remove that bias.

## Engineering decision

Treat the gate as a local reference implementation. Validate policy intent and prerequisites before recommending a production change. Measure false positives, legitimate workflow loss, latency, and operational failure behavior with an independent corpus. Do not infer security from a schema, signature, or shared-role authorization alone when the declared boundary needs additional context.

## Original question remains bounded

Constructed local mechanism supported; implementation-level and population claims not established. No vector database, Azure search service, model-generated summary, asynchronous index propagation, conversation erasure, or customer corpus was tested. Revocation is an immediate SQLite transaction, so no claim about a provider synchronization deadline is supported.
