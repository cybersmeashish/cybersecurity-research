# CAI-005 — User-bound authorization for cloud actions executed by AI agents

**Status:** proposed research, version 0.1. **Area:** Cloud + AI. **Priority:** 4/10. **Prepared:** 2026-11-24.

No experiments have been run for this proposal and no tool is implemented. No new vulnerability, provider defect, global novelty, or independent validation is claimed.

## Testable hypothesis

An agent using a shared cloud role without enforcing its initiating user's rights can execute an action denied to that user even when the workload role is correctly authorized.

**Null hypothesis:** Every action is authorized by both the user policy and agent workload policy.

## Threat model

- **Protected assets:** Cloud records and administrative operations exposed through agent tools.
- **Attacker capability:** A low-privilege authenticated requester who cannot change IAM or the agent role.
- **Security boundary:** Workload capability remains constrained by the requesting user's authority.

## Proposed contribution and prior art

Evaluate propagation at framework-to-tool boundaries; shared-role authorization risk itself is established.

[Primary prior work](SOURCES.md) motivates the threat model; it does not establish this hypothesis in a selected implementation. Prior-art survey and version selection remain pending.

## Intended deliverables

1. A reproducible controlled test harness and bounded evidence.
2. A prototype **Agent user-permission gateway**, evaluated for false positives and legitimate-workflow utility.
3. A scoped finding or negative result identifying tested versions and limitations.

## Research documents

- [Experiment plan](EXPERIMENT-PLAN.md)
- [Proposed tool design](TOOL-DESIGN.md)
- [Sources](SOURCES.md)
- [Machine-readable record](research.json)
- [Shared validation protocol](../HYPOTHESIS-VALIDATION.md)
- [Research portfolio](../CLOUD-AI-SECURITY-HYPOTHESES.md)
