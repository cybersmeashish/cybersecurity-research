# Tool design and implemented local prototype — CAI-007

## Implemented artifact

[src/study.py](src/study.py) exposes `evaluate(case, mode)` and returns an observed effect, trace, and backend-specific observation. [The runner](tools/run_study.py) evaluates the published fixtures, exports evidence, and runs behavioral tests. This is an executable research prototype, not a production scanner.

## Production tool still proposed

**SOC-agent adversarial regression suite** needs an authorized implementation adapter, a policy-intent contract, versioned identity/resource schemas, and an independent labeled workload. No installable production adapter or detection-coverage claim is provided.

## Boundary to enforce

`Execute(plan) implies SchemaValid(plan) AND IncidentPolicyAllows(caller, target, action, state).`

## Proposed input and output contract

Require authenticated principal/tenant context, target version, expected policy, relevant state revision, and sanitized observations. Reject missing context as inconclusive. Findings should report verified preconditions, actual effect, configuration/source hashes, confidence, and remediation. A broad role, absent label, or model sentence alone is not proof of exploitability.

## Detection and remediation workflow

Trace the untrusted input to the endpoint, identify the missing binding, reproduce it with a negative and positive control, and compare a corrected gate. Measure false positives and legitimate workflow loss before deployment. Freeze a model/version, paired event corpus, and prompting policy; measure actual model-produced actions before replaying them through these gates.

## Coverage limits

No LLM ran and no attack-success rate for prompt injection was measured. Adversarial log wording and compromised plans are authored stimuli, not observed model outputs. This experiment validates downstream action control conditional on a bad plan; it does not establish the log-to-model causal step.
