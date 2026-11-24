# Interpretation and implications — CAI-004

## Mechanistic explanation

A name-only rule cannot distinguish a recreated identity from its predecessor. An owner restriction narrows the trust domain but still permits same-owner repository recreation. Name-based profiles also reject a legitimate rename, whereas stable identifiers preserve the intended identity through that rename. This exposes both excess trust and unnecessary denial in one policy model.

## Why the partial control matters

The partial profile produced 6/12 forbidden effects while preserving 6/12 legitimate effects. It changes a specific check, not the declared policy. The corrected gate aligns the final effect with that policy. A production integration must expose the same trusted context to implement the gate.

## Alternative explanations

The flawed profiles were deliberately constructed to exercise known classes; their failure is not evidence of prevalence or novelty. The corrected code was authored with knowledge of this corpus, so unseen attack families and complex legitimate workflows remain a threat to generalization. Nominal identity contexts do not remove that bias.

## Engineering decision

Treat the gate as a local reference implementation. Validate policy intent and prerequisites before recommending a production change. Measure false positives, legitimate workflow loss, latency, and operational failure behavior with an independent corpus. Do not infer security from a schema, signature, or shared-role authorization alone when the declared boundary needs additional context.

## Original question remains bounded

Constructed local mechanism supported; implementation-level and population claims not established. No GitHub repository was deleted or transferred, and no external OIDC issuer or cloud STS was invoked. Claim lifecycles and ownership transitions are supplied fixtures; actual issuer guarantees must be established separately.
