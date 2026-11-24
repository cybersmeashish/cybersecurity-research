# Interpretation and implications — CAI-006

## Mechanistic explanation

Two real HTTP servers occupy distinct loopback addresses at one port. A public fixture redirects to the internal canary. A controlled resolver separately returns a permitted address at validation and an internal address at connection time. Checking each advertised hostname stops the explicit redirect but misses the address transition. The guarded transport pins the initially checked address and validates later resolved destinations before connecting.

## Why the partial control matters

The partial profile produced 6/12 forbidden effects while preserving 12/12 legitimate effects. It changes a specific check, not the declared policy. The corrected gate aligns the final effect with that policy. A production integration must expose the same trusted context to implement the gate.

## Alternative explanations

The flawed profiles were deliberately constructed to exercise known classes; their failure is not evidence of prevalence or novelty. The corrected code was authored with knowledge of this corpus, so unseen attack families and complex legitimate workflows remain a threat to generalization. Nominal identity contexts do not remove that bias.

## Engineering decision

Treat the gate as a local reference implementation. Validate policy intent and prerequisites before recommending a production change. Measure false positives, legitimate workflow loss, latency, and operational failure behavior with an independent corpus. Do not infer security from a schema, signature, or shared-role authorization alone when the declared boundary needs additional context.

## Original question remains bounded

Constructed local mechanism supported; implementation-level and population claims not established. Both endpoints are loopback fixtures; public DNS rebinding, IPv6, HTTPS certificate binding, proxies, metadata credential extraction, and a production connector were not tested. Resolution changes are adapter-controlled. The harness forbids destinations outside its two loopback addresses and port.
