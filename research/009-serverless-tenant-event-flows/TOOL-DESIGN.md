# Proposed tool — Serverless tenant-flow scanner

**Implementation status:** design only. No runnable scanner, installation command, or validated detection coverage is provided.

## Inputs

Application source, infrastructure definitions, event schemas, ingress identity mapping, and declared tenant policy.

## Minimum analysis workflow

1. Trace tenant identity across ingress, queue, consumer, and storage.
2. Identify authorization relying on unbound payload fields.
3. Report missing context instead of asserting an exploit from broad IAM alone.

Reject missing context explicitly. A permissive configuration alone does not prove exploitability.

## Findings and outputs

Source-to-resource paths, binding gaps, and synthetic counterexamples.

Include target/tool version, declared policy, verified preconditions, provenance, confidence, and remediation. Distinguish static possibilities, synthetic observations, and actual implementation behavior.

## Evaluation and milestones

Use the [experiment plan](EXPERIMENT-PLAN.md) with flawed and corrected fixtures. Measure false positives, labeled false negatives, and legitimate-workflow success. Publish unsupported cases as limitations.

1. Define adapter contracts and evidence schema.
2. Implement one synthetic fixture and corrected control.
3. Extend to all planned cases and missing-context handling.
4. Add an implementation adapter after separate scope authorization.
5. Obtain independent reproduction before a vulnerability claim.
