# Tool design and implemented local prototype — CAI-010

## Implemented artifact

[src/study.py](src/study.py) exposes `evaluate(case, mode)` and returns an observed effect, trace, and backend-specific observation. [The runner](tools/run_study.py) evaluates the published fixtures, exports evidence, and runs behavioral tests. This is an executable research prototype, not a production scanner.

## Production tool still proposed

**Inference-cache isolation auditor** needs an authorized implementation adapter, a policy-intent contract, versioned identity/resource schemas, and an independent labeled workload. No installable production adapter or detection-coverage claim is provided.

## Boundary to enforce

`CacheKey includes a trusted tenant partition so another tenant cannot select the same namespace by choosing a salt.`

## Proposed input and output contract

Require authenticated principal/tenant context, target version, expected policy, relevant state revision, and sanitized observations. Reject missing context as inconclusive. Findings should report verified preconditions, actual effect, configuration/source hashes, confidence, and remediation. A broad role, absent label, or model sentence alone is not proof of exploitability.

## Detection and remediation workflow

Trace the untrusted input to the endpoint, identify the missing binding, reproduce it with a negative and positive control, and compare a corrected gate. Measure false positives and legitimate workflow loss before deployment. Use a scoped inference deployment with real scheduling/noise, trusted gateway identities, fresh held-out prefixes, and a pre-registered sample-size calculation.

## Coverage limits

There are no KV tensors, GPU, vLLM server, network jitter, batching, or model inference. Cold work is 1,200 SHA-256 iterations, so the timing separation is artificial. The corrected timing AUC remains an exploratory observation; zero cross-tenant hits does not prove all side channels absent.
