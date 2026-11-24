# Proposed tool — SOC-agent adversarial regression suite

**Implementation status:** design only. No runnable scanner, installation command, or validated detection coverage is provided.

## Inputs

Labeled incidents, permitted attacker fields, handling rules, mock tools, and model/version configuration.

## Minimum analysis workflow

1. Build paired cases with factual evidence held constant.
2. Record ticket state and actual tool calls.
3. Compare schema-only and action-policy controls.

Reject missing context explicitly. A permissive configuration alone does not prove exploitability.

## Findings and outputs

Paired outcomes, recall metrics, and minimal failing fixtures.

Include target/tool version, declared policy, verified preconditions, provenance, confidence, and remediation. Distinguish static possibilities, synthetic observations, and actual implementation behavior.

## Evaluation and milestones

Use the [experiment plan](EXPERIMENT-PLAN.md) with flawed and corrected fixtures. Measure false positives, labeled false negatives, and legitimate-workflow success. Publish unsupported cases as limitations.

1. Define adapter contracts and evidence schema.
2. Implement one synthetic fixture and corrected control.
3. Extend to all planned cases and missing-context handling.
4. Add an implementation adapter after separate scope authorization.
5. Obtain independent reproduction before a vulnerability claim.
