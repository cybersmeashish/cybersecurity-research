# CAI-009 — Tenant authorization through serverless event chains

**Status:** proposed research, version 0.1. **Area:** Cloud. **Priority:** 8/10. **Prepared:** 2026-11-24.

No experiments have been run for this proposal and no tool is implemented. No new vulnerability, provider defect, global novelty, or independent validation is claimed.

## Testable hypothesis

A privileged consumer trusting an unbound tenant identifier in an event payload can access another tenant's synthetic resource despite correct direct-access restrictions on the producer.

**Null hypothesis:** Downstream resource actions remain bound to authenticated tenant provenance and permitted producer scope.

## Threat model

- **Protected assets:** Tenant records, event integrity, queues, function privileges, and storage authorization.
- **Attacker capability:** A tenant submitting valid events through authorized ingress, without access to another tenant's storage.
- **Security boundary:** An event handoff does not turn user-supplied tenant labels into authorization.

## Proposed contribution and prior art

Combine infrastructure permissions with tenant-provenance flows; cross-component serverless analysis is prior art.

[Primary prior work](SOURCES.md) motivates the threat model; it does not establish this hypothesis in a selected implementation. Prior-art survey and version selection remain pending.

## Intended deliverables

1. A reproducible controlled test harness and bounded evidence.
2. A prototype **Serverless tenant-flow scanner**, evaluated for false positives and legitimate-workflow utility.
3. A scoped finding or negative result identifying tested versions and limitations.

## Research documents

- [Experiment plan](EXPERIMENT-PLAN.md)
- [Proposed tool design](TOOL-DESIGN.md)
- [Sources](SOURCES.md)
- [Machine-readable record](research.json)
- [Shared validation protocol](../HYPOTHESIS-VALIDATION.md)
- [Research portfolio](../CLOUD-AI-SECURITY-HYPOTHESES.md)
