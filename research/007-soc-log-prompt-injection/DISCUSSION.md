# Interpretation and implications — CAI-007

## Mechanistic explanation

The fixture supplies clean and adversarially motivated candidate plans explicitly. The lab does not derive a plan from the log with an LLM. It validates the plan schema and commits accepted actions to a SQLite incident store. Tenant-target checks prevent a foreign target but do not prevent closing a critical incident or disabling its alert. The independent incident policy blocks those actions.

## Why the partial control matters

The partial profile produced 12/18 forbidden effects while preserving 12/12 legitimate effects. It changes a specific check, not the declared policy. The corrected gate aligns the final effect with that policy. A production integration must expose the same trusted context to implement the gate.

## Alternative explanations

The flawed profiles were deliberately constructed to exercise known classes; their failure is not evidence of prevalence or novelty. The corrected code was authored with knowledge of this corpus, so unseen attack families and complex legitimate workflows remain a threat to generalization. Nominal identity contexts do not remove that bias.

## Engineering decision

Treat the gate as a local reference implementation. Validate policy intent and prerequisites before recommending a production change. Measure false positives, legitimate workflow loss, latency, and operational failure behavior with an independent corpus. Do not infer security from a schema, signature, or shared-role authorization alone when the declared boundary needs additional context.

## Original question remains bounded

Downstream action control supported; LLM log-to-action susceptibility not evaluated. No LLM ran and no attack-success rate for prompt injection was measured. Adversarial log wording and compromised plans are authored stimuli, not observed model outputs. This experiment validates downstream action control conditional on a bad plan; it does not establish the log-to-model causal step.
