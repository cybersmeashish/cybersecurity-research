# Tool design and implemented local prototype — CAI-004

## Implemented artifact

[src/study.py](src/study.py) exposes `evaluate(case, mode)` and returns an observed effect, trace, and backend-specific observation. [The runner](tools/run_study.py) evaluates the published fixtures, exports evidence, and runs behavioral tests. This is an executable research prototype, not a production scanner.

## Production tool still proposed

**OIDC trust-policy lifecycle auditor** needs an authorized implementation adapter, a policy-intent contract, versioned identity/resource schemas, and an independent labeled workload. No installable production adapter or detection-coverage claim is provided.

## Boundary to enforce

`Map(claims, role) implies claims.issuer=I AND claims.audience=A AND claims.repository_id=R AND claims.owner_id=O.`

## Proposed input and output contract

Require authenticated principal/tenant context, target version, expected policy, relevant state revision, and sanitized observations. Reject missing context as inconclusive. Findings should report verified preconditions, actual effect, configuration/source hashes, confidence, and remediation. A broad role, absent label, or model sentence alone is not proof of exploitability.

## Detection and remediation workflow

Trace the untrusted input to the endpoint, identify the missing binding, reproduce it with a negative and positive control, and compare a corrected gate. Measure false positives and legitimate workflow loss before deployment. Select one issuer/cloud pairing, document its immutable claim guarantees, and validate allowed lifecycle events in owned repositories.

## Coverage limits

No GitHub repository was deleted or transferred, and no external OIDC issuer or cloud STS was invoked. Claim lifecycles and ownership transitions are supplied fixtures; actual issuer guarantees must be established separately.
