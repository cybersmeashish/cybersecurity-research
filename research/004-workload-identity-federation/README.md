# CAI-004 — Identity lifecycle hazards in workload federation policies

**Status:** proposed research, version 0.1. **Area:** Cloud. **Priority:** 3/10. **Prepared:** 2026-11-24.

No experiments have been run for this proposal and no tool is implemented. No new vulnerability, provider defect, global novelty, or independent validation is claimed.

## Testable hypothesis

A trust policy authorizing mutable or reusable identity names without equivalent stable-ID restrictions can map a distinct post-lifecycle workload to the previously trusted cloud principal.

**Null hypothesis:** Only the intended stable workload maps to the principal before and after the tested lifecycle events.

## Threat model

- **Protected assets:** Cloud roles, CI deployment privileges, and repository-to-cloud trust.
- **Attacker capability:** An owner of their own test repositories or identities, without issuer signing keys or victim access.
- **Security boundary:** A valid issuer signature does not replace verification of the intended stable workload identity.

## Proposed contribution and prior art

Convert documented identity-mapping hazards into contextual policy findings with lifecycle counterexamples.

[Primary prior work](SOURCES.md) motivates the threat model; it does not establish this hypothesis in a selected implementation. Prior-art survey and version selection remain pending.

## Intended deliverables

1. A reproducible controlled test harness and bounded evidence.
2. A prototype **OIDC trust-policy lifecycle auditor**, evaluated for false positives and legitimate-workflow utility.
3. A scoped finding or negative result identifying tested versions and limitations.

## Research documents

- [Experiment plan](EXPERIMENT-PLAN.md)
- [Proposed tool design](TOOL-DESIGN.md)
- [Sources](SOURCES.md)
- [Machine-readable record](research.json)
- [Shared validation protocol](../HYPOTHESIS-VALIDATION.md)
- [Research portfolio](../CLOUD-AI-SECURITY-HYPOTHESES.md)
