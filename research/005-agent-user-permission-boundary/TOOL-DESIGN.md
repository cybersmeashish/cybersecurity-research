# Proposed tool — Agent user-permission gateway

**Implementation status:** design only. No runnable scanner, installation command, or validated detection coverage is provided.

## Inputs

Trusted caller identity, task ID, final action/resource, user policy, agent policy, and delegation context.

## Minimum analysis workflow

1. Resolve caller identity from trusted authentication.
2. Authorize caller and workload on the actual action/resource.
3. Preserve user scope through delegation and log denials.

Reject missing context explicitly. A permissive configuration alone does not prove exploitability.

## Findings and outputs

Per-action decisions and task-to-cloud-action audit traces.

Include target/tool version, declared policy, verified preconditions, provenance, confidence, and remediation. Distinguish static possibilities, synthetic observations, and actual implementation behavior.

## Evaluation and milestones

Use the [experiment plan](EXPERIMENT-PLAN.md) with flawed and corrected fixtures. Measure false positives, labeled false negatives, and legitimate-workflow success. Publish unsupported cases as limitations.

1. Define adapter contracts and evidence schema.
2. Implement one synthetic fixture and corrected control.
3. Extend to all planned cases and missing-context handling.
4. Add an implementation adapter after separate scope authorization.
5. Obtain independent reproduction before a vulnerability claim.
