# Tool design and implemented local prototype — CAI-003

## Implemented artifact

[src/study.py](src/study.py) exposes `evaluate(case, mode)` and returns an observed effect, trace, and backend-specific observation. [The runner](tools/run_study.py) evaluates the published fixtures, exports evidence, and runs behavioral tests. This is an executable research prototype, not a production scanner.

## Production tool still proposed

**MCP authorization conformance suite** needs an authorized implementation adapter, a policy-intent contract, versioned identity/resource schemas, and an independent labeled workload. No installable production adapter or detection-coverage claim is provided.

## Boundary to enforce

`Accept implies ValidSignature AND IntendedIssuer AND Fresh AND SubjectMatchesCaller AND ClientMatches AND AudienceMatches AND HandleOwnerMatches.`

## Proposed input and output contract

Require authenticated principal/tenant context, target version, expected policy, relevant state revision, and sanitized observations. Reject missing context as inconclusive. Findings should report verified preconditions, actual effect, configuration/source hashes, confidence, and remediation. A broad role, absent label, or model sentence alone is not proof of exploitability.

## Detection and remediation workflow

Trace the untrusted input to the endpoint, identify the missing binding, reproduce it with a negative and positive control, and compare a corrected gate. Measure false positives and legitimate workflow loss before deployment. Run protocol-conformant authorization cases against a scoped proxy with real resource indicators, consent lifecycle, and protocol-version requirements.

## Coverage limits

The artifact is a two-part HMAC-signed JSON fixture, not an interoperable JWT. There is no browser OAuth flow, complete MCP server, consent UI, token endpoint, PKCE test, or third-party proxy assessment. Intended delegation requires a distinct documented contract.
