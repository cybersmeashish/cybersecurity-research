# Interpretation and implications — CAI-008

## Mechanistic explanation

The memory store retains structured source and summary records. A deliberately permissive consumer defaults a missing trust label to trusted. Partial compaction preserves a first-stage label but loses it in a second compaction or accepts an unbound claimed label. A later session recalls the stored record without the original text. The guarded path traverses parents to an authorized operator-origin source and rejects missing roots.

## Why the partial control matters

The partial profile produced 12/24 forbidden effects while preserving 6/6 legitimate effects. It changes a specific check, not the declared policy. The corrected gate aligns the final effect with that policy. A production integration must expose the same trusted context to implement the gate.

## Alternative explanations

The flawed profiles were deliberately constructed to exercise known classes; their failure is not evidence of prevalence or novelty. The corrected code was authored with knowledge of this corpus, so unseen attack families and complex legitimate workflows remain a threat to generalization. Nominal identity contexts do not remove that bias.

## Engineering decision

Treat the gate as a local reference implementation. Validate policy intent and prerequisites before recommending a production change. Measure false positives, legitimate workflow loss, latency, and operational failure behavior with an independent corpus. Do not infer security from a schema, signature, or shared-role authorization alone when the declared boundary needs additional context.

## Original question remains bounded

Structured provenance mechanism supported; semantic/LLM memory poisoning not evaluated. Compaction copies structured fields; it is not natural-language summarization. No LLM, embedding retriever, semantic trigger optimization, long-running deployment, or real user memory was tested. The result concerns provenance mechanics, not model-level memory-poisoning susceptibility.
