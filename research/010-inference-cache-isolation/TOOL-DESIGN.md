# Proposed tool — Inference-cache isolation auditor

**Implementation status:** design only. No runnable scanner, installation command, or validated detection coverage is provided.

## Inputs

Gateway adapter, owned tenant identities, namespace configuration, randomized membership schedule, and timing observations.

## Minimum analysis workflow

1. Verify namespaces derive from trusted tenant identity.
2. Test caller overrides across namespaces.
3. Analyze held-out membership using clustered confidence intervals.

Reject missing context explicitly. A permissive configuration alone does not prove exploitability.

## Findings and outputs

Isolation conformance and bounded membership-leakage estimates, not full prompt recovery.

Include target/tool version, declared policy, verified preconditions, provenance, confidence, and remediation. Distinguish static possibilities, synthetic observations, and actual implementation behavior.

## Evaluation and milestones

Use the [experiment plan](EXPERIMENT-PLAN.md) with flawed and corrected fixtures. Measure false positives, labeled false negatives, and legitimate-workflow success. Publish unsupported cases as limitations.

1. Define adapter contracts and evidence schema.
2. Implement one synthetic fixture and corrected control.
3. Extend to all planned cases and missing-context handling.
4. Add an implementation adapter after separate scope authorization.
5. Obtain independent reproduction before a vulnerability claim.
