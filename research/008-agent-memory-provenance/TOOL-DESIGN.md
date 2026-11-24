# Proposed tool — Agent memory provenance validator

**Implementation status:** design only. No runnable scanner, installation command, or validated detection coverage is provided.

## Inputs

Memory export, source trust labels, derivation links, summary events, and recall/action traces.

## Minimum analysis workflow

1. Check summary source and trust lineage.
2. Detect increased authority in derived memory.
3. Replay later tasks against policy-constrained mock actions.

Reject missing context explicitly. A permissive configuration alone does not prove exploitability.

## Findings and outputs

Lineage-loss findings and cross-session reproduction traces.

Include target/tool version, declared policy, verified preconditions, provenance, confidence, and remediation. Distinguish static possibilities, synthetic observations, and actual implementation behavior.

## Evaluation and milestones

Use the [experiment plan](EXPERIMENT-PLAN.md) with flawed and corrected fixtures. Measure false positives, labeled false negatives, and legitimate-workflow success. Publish unsupported cases as limitations.

1. Define adapter contracts and evidence schema.
2. Implement one synthetic fixture and corrected control.
3. Extend to all planned cases and missing-context handling.
4. Add an implementation adapter after separate scope authorization.
5. Obtain independent reproduction before a vulnerability claim.
