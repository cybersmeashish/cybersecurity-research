# Proposed tool — MCP authorization conformance suite

**Implementation status:** design only. No runnable scanner, installation command, or validated detection coverage is provided.

## Inputs

Protocol version, user/client fixtures, mock issuer, resource audiences, and intended delegation policy.

## Minimum analysis workflow

1. Validate user, client, audience, and handle ownership at each step.
2. Exercise consent cache, expiry, logout, and revocation.
3. Separate intended delegation from principal substitution.

Reject missing context explicitly. A permissive configuration alone does not prove exploitability.

## Findings and outputs

Conformance matrix and sanitized replay traces, without token values.

Include target/tool version, declared policy, verified preconditions, provenance, confidence, and remediation. Distinguish static possibilities, synthetic observations, and actual implementation behavior.

## Evaluation and milestones

Use the [experiment plan](EXPERIMENT-PLAN.md) with flawed and corrected fixtures. Measure false positives, labeled false negatives, and legitimate-workflow success. Publish unsupported cases as limitations.

1. Define adapter contracts and evidence schema.
2. Implement one synthetic fixture and corrected control.
3. Extend to all planned cases and missing-context handling.
4. Add an implementation adapter after separate scope authorization.
5. Obtain independent reproduction before a vulnerability claim.
