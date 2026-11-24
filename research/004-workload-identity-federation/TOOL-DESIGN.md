# Proposed tool — OIDC trust-policy lifecycle auditor

**Implementation status:** design only. No runnable scanner, installation command, or validated detection coverage is provided.

## Inputs

Infrastructure or exported trust policy, issuer schema, attribute mapping, ownership context, and expected stable IDs.

## Minimum analysis workflow

1. Identify mutable-name bindings without stable restrictions.
2. Construct a counterexample against declared trust intent.
3. Report uncertainty when issuer guarantees or ownership context are unavailable.

Reject missing context explicitly. A permissive configuration alone does not prove exploitability.

## Findings and outputs

Policy, relevant claims, lifecycle counterexample, and suggested stable binding.

Include target/tool version, declared policy, verified preconditions, provenance, confidence, and remediation. Distinguish static possibilities, synthetic observations, and actual implementation behavior.

## Evaluation and milestones

Use the [experiment plan](EXPERIMENT-PLAN.md) with flawed and corrected fixtures. Measure false positives, labeled false negatives, and legitimate-workflow success. Publish unsupported cases as limitations.

1. Define adapter contracts and evidence schema.
2. Implement one synthetic fixture and corrected control.
3. Extend to all planned cases and missing-context handling.
4. Add an implementation adapter after separate scope authorization.
5. Obtain independent reproduction before a vulnerability claim.
