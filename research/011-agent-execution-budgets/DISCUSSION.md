# Interpretation and implications — CAI-011

## Mechanistic explanation

Each admitted node performs real local hashing work with a declared cost. Call caps are enforced in every profile. Independent calls can all pass while their sum exceeds the task budget. Retaining a parent ID alone does not enforce a cap. The guarded scheduler locks budget reservation before executing sequential or concurrent work.

## Why the partial control matters

The partial profile produced 18/18 forbidden effects while preserving 6/6 legitimate effects. It changes a specific check, not the declared policy. The corrected gate aligns the final effect with that policy. A production integration must expose the same trusted context to implement the gate.

## Alternative explanations

The flawed profiles were deliberately constructed to exercise known classes; their failure is not evidence of prevalence or novelty. The corrected code was authored with knowledge of this corpus, so unseen attack families and complex legitimate workflows remain a threat to generalization. Nominal identity contexts do not remove that bias.

## Engineering decision

Treat the gate as a local reference implementation. Validate policy intent and prerequisites before recommending a production change. Measure false positives, legitimate workflow loss, latency, and operational failure behavior with an independent corpus. Do not infer security from a schema, signature, or shared-role authorization alone when the declared boundary needs additional context.

## Original question remains bounded

Local accounting mechanism supported; reasoning-driven cost amplification and currency impact not measured. Units are declared synthetic costs, not dollars, tokens, cloud billing, or actual reasoning effort. Node costs are known before admission. There is no live autonomous planner, probabilistic usage estimator, mid-flight cancellation, or distributed ledger race.
