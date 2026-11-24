# Proposed tool — RAG authorization lineage tester

**Implementation status:** design only. No runnable scanner, installation command, or validated detection coverage is provided.

## Inputs

Application adapter, identity/ACL matrix, marker manifest, permission events, and derivation/cache configuration.

## Minimum analysis workflow

1. Run matched queries under allowed and denied identities.
2. Trace chunks, summaries, and cached answers back to source ACLs.
3. Confirm propagation completion before reporting a revocation bypass.

Reject missing context explicitly. A permissive configuration alone does not prove exploitability.

## Findings and outputs

Principal, source ID, response path, permission revision, marker evidence, and reproduction steps.

Include target/tool version, declared policy, verified preconditions, provenance, confidence, and remediation. Distinguish static possibilities, synthetic observations, and actual implementation behavior.

## Evaluation and milestones

Use the [experiment plan](EXPERIMENT-PLAN.md) with flawed and corrected fixtures. Measure false positives, labeled false negatives, and legitimate-workflow success. Publish unsupported cases as limitations.

1. Define adapter contracts and evidence schema.
2. Implement one synthetic fixture and corrected control.
3. Extend to all planned cases and missing-context handling.
4. Add an implementation adapter after separate scope authorization.
5. Obtain independent reproduction before a vulnerability claim.
