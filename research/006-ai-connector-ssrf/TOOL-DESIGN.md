# Proposed tool — AI connector egress test suite

**Implementation status:** design only. No runnable scanner, installation command, or validated detection coverage is provided.

## Inputs

Connector adapter, destination policy, controlled resolver, redirect fixtures, and canary endpoint.

## Minimum analysis workflow

1. Record actual connected destinations at every hop.
2. Test content fetching and metadata discovery.
3. Distinguish attempted requests from actual internal contact.

Reject missing context explicitly. A permissive configuration alone does not prove exploitability.

## Findings and outputs

Destination-chain traces tied to the explicit egress policy.

Include target/tool version, declared policy, verified preconditions, provenance, confidence, and remediation. Distinguish static possibilities, synthetic observations, and actual implementation behavior.

## Evaluation and milestones

Use the [experiment plan](EXPERIMENT-PLAN.md) with flawed and corrected fixtures. Measure false positives, labeled false negatives, and legitimate-workflow success. Publish unsupported cases as limitations.

1. Define adapter contracts and evidence schema.
2. Implement one synthetic fixture and corrected control.
3. Extend to all planned cases and missing-context handling.
4. Add an implementation adapter after separate scope authorization.
5. Obtain independent reproduction before a vulnerability claim.
