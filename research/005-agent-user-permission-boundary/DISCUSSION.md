# Interpretation and implications — CAI-005

## Mechanistic explanation

The mock service role can read and write both records. A user is allowed only to read an owned record. Tool-name restrictions block writes but still permit a read of the wrong resource. The guarded gateway checks the actual operation and target using the authenticated caller context, including the delegated-task fixture.

## Why the partial control matters

The partial profile produced 6/24 forbidden effects while preserving 6/6 legitimate effects. It changes a specific check, not the declared policy. The corrected gate aligns the final effect with that policy. A production integration must expose the same trusted context to implement the gate.

## Alternative explanations

The flawed profiles were deliberately constructed to exercise known classes; their failure is not evidence of prevalence or novelty. The corrected code was authored with knowledge of this corpus, so unseen attack families and complex legitimate workflows remain a threat to generalization. Nominal identity contexts do not remove that bias.

## Engineering decision

Treat the gate as a local reference implementation. Validate policy intent and prerequisites before recommending a production change. Measure false positives, legitimate workflow loss, latency, and operational failure behavior with an independent corpus. Do not infer security from a schema, signature, or shared-role authorization alone when the declared boundary needs additional context.

## Original question remains bounded

Constructed local mechanism supported; implementation-level and population claims not established. There is no live IAM simulator, provider role assumption, autonomous LLM tool selection, or distributed delegation service. The study covers human-initiated user-bound requests; autonomous service tasks may legitimately use a different authorization policy.
