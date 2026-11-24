# Interpretation and implications — CAI-003

## Mechanistic explanation

All profiles check a synthetic artifact signature, issuer, and expiry. Deliberately omitted bindings permit a resource operation even though the artifact belongs to a different user, client, resource audience, or workflow owner. Adding subject validation alone leaves other bindings unresolved.

## Why the partial control matters

The partial profile produced 18/24 forbidden effects while preserving 6/6 legitimate effects. It changes a specific check, not the declared policy. The corrected gate aligns the final effect with that policy. A production integration must expose the same trusted context to implement the gate.

## Alternative explanations

The flawed profiles were deliberately constructed to exercise known classes; their failure is not evidence of prevalence or novelty. The corrected code was authored with knowledge of this corpus, so unseen attack families and complex legitimate workflows remain a threat to generalization. Nominal identity contexts do not remove that bias.

## Engineering decision

Treat the gate as a local reference implementation. Validate policy intent and prerequisites before recommending a production change. Measure false positives, legitimate workflow loss, latency, and operational failure behavior with an independent corpus. Do not infer security from a schema, signature, or shared-role authorization alone when the declared boundary needs additional context.

## Original question remains bounded

Constructed local mechanism supported; implementation-level and population claims not established. The artifact is a two-part HMAC-signed JSON fixture, not an interoperable JWT. There is no browser OAuth flow, complete MCP server, consent UI, token endpoint, PKCE test, or third-party proxy assessment. Intended delegation requires a distinct documented contract.
