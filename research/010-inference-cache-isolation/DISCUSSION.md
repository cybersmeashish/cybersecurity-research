# Interpretation and implications — CAI-010

## Mechanistic explanation

The cache stores a deterministic CPU work result keyed by namespace and prefix. Global sharing exposes hits. Caller-provided salts avoid accidental sharing when distinct but allow chosen-salt collisions. A trusted tenant partition separates the state. The timing experiment calibrates a threshold on the caller's own known warm/cold prefixes and probes 64 different prefixes once per condition, with randomized order and another tenant's residency as ground truth.

## Why the partial control matters

The partial profile produced 6/18 forbidden effects while preserving 6/6 legitimate effects. It changes a specific check, not the declared policy. The corrected gate aligns the final effect with that policy. A production integration must expose the same trusted context to implement the gate.

## Alternative explanations

The flawed profiles were deliberately constructed to exercise known classes; their failure is not evidence of prevalence or novelty. The corrected code was authored with knowledge of this corpus, so unseen attack families and complex legitimate workflows remain a threat to generalization. Nominal identity contexts do not remove that bias.

## Engineering decision

Treat the gate as a local reference implementation. Validate policy intent and prerequisites before recommending a production change. Measure false positives, legitimate workflow loss, latency, and operational failure behavior with an independent corpus. Do not infer security from a schema, signature, or shared-role authorization alone when the declared boundary needs additional context.

## Original question remains bounded

Synthetic namespace and timing mechanism supported; production LLM-serving leakage not evaluated. There are no KV tensors, GPU, vLLM server, network jitter, batching, or model inference. Cold work is 1,200 SHA-256 iterations, so the timing separation is artificial. The corrected timing AUC remains an exploratory observation; zero cross-tenant hits does not prove all side channels absent.
