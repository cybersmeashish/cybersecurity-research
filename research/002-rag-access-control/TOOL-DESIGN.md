# Tool design and implemented local prototype — CAI-002

## Implemented artifact

[src/study.py](src/study.py) exposes `evaluate(case, mode)` and returns an observed effect, trace, and backend-specific observation. [The runner](tools/run_study.py) evaluates the published fixtures, exports evidence, and runs behavioral tests. This is an executable research prototype, not a production scanner.

## Production tool still proposed

**RAG authorization lineage tester** needs an authorized implementation adapter, a policy-intent contract, versioned identity/resource schemas, and an independent labeled workload. No installable production adapter or detection-coverage claim is provided.

## Boundary to enforce

`Serve(u, artifact, t) implies Allow(u, d, t) for every protected source d in Lineage(artifact).`

## Proposed input and output contract

Require authenticated principal/tenant context, target version, expected policy, relevant state revision, and sanitized observations. Reject missing context as inconclusive. Findings should report verified preconditions, actual effect, configuration/source hashes, confidence, and remediation. A broad role, absent label, or model sentence alone is not proof of exploitability.

## Detection and remediation workflow

Trace the untrusted input to the endpoint, identify the missing binding, reproduce it with a negative and positive control, and compare a corrected gate. Measure false positives and legitimate workflow loss before deployment. Validate permission propagation and derived-artifact lineage in one explicitly authorized RAG stack, including its documented update interval.

## Coverage limits

No vector database, Azure search service, model-generated summary, asynchronous index propagation, conversation erasure, or customer corpus was tested. Revocation is an immediate SQLite transaction, so no claim about a provider synchronization deadline is supported.
