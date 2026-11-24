# Proposed tool — Agent execution-budget controller

**Implementation status:** design only. No runnable scanner, installation command, or validated detection coverage is provided.

## Inputs

Task/parent IDs, execution graph, normalized usage, budget, reservations, and cancellation events.

## Minimum analysis workflow

1. Charge retries and children to one task ledger.
2. Reserve maximum in-flight usage before execution.
3. Record exhaustion and cancel unstarted branches.

Reject missing context explicitly. A permissive configuration alone does not prove exploitability.

## Findings and outputs

Task ledger, overshoot findings, and legitimate-workflow comparisons.

Include target/tool version, declared policy, verified preconditions, provenance, confidence, and remediation. Distinguish static possibilities, synthetic observations, and actual implementation behavior.

## Evaluation and milestones

Use the [experiment plan](EXPERIMENT-PLAN.md) with flawed and corrected fixtures. Measure false positives, labeled false negatives, and legitimate-workflow success. Publish unsupported cases as limitations.

1. Define adapter contracts and evidence schema.
2. Implement one synthetic fixture and corrected control.
3. Extend to all planned cases and missing-context handling.
4. Add an implementation adapter after separate scope authorization.
5. Obtain independent reproduction before a vulnerability claim.
