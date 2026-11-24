# CAI-002 — Authorization lineage in RAG-derived artifacts

**Status:** proposed research, version 0.1. **Area:** Cloud + AI. **Priority:** 1/10. **Prepared:** 2026-11-24.

No experiments have been run for this proposal and no tool is implemented. No new vulnerability, provider defect, global novelty, or independent validation is claimed.

## Testable hypothesis

A RAG application enforcing access only at initial retrieval, without equivalent checks on cached answers or derived summaries, can return a protected synthetic marker to a denied principal after the documented authorization synchronization window.

**Null hypothesis:** Cached and derived responses remain scoped to the requesting principal and current source permissions in every tested case.

## Threat model

- **Protected assets:** Tenant documents, private answers, permission metadata, and derived artifacts.
- **Attacker capability:** An authenticated tenant user who can submit queries but cannot change another tenant's ACLs.
- **Security boundary:** Source authorization survives chunking, summarization, cache lookup, and response delivery.

## Proposed contribution and prior art

Survey current cache and summary implementations for lost authorization lineage; document filtering itself is established prior art.

[Primary prior work](SOURCES.md) motivates the threat model; it does not establish this hypothesis in a selected implementation. Prior-art survey and version selection remain pending.

## Intended deliverables

1. A reproducible controlled test harness and bounded evidence.
2. A prototype **RAG authorization lineage tester**, evaluated for false positives and legitimate-workflow utility.
3. A scoped finding or negative result identifying tested versions and limitations.

## Research documents

- [Experiment plan](EXPERIMENT-PLAN.md)
- [Proposed tool design](TOOL-DESIGN.md)
- [Sources](SOURCES.md)
- [Machine-readable record](research.json)
- [Shared validation protocol](../HYPOTHESIS-VALIDATION.md)
- [Research portfolio](../CLOUD-AI-SECURITY-HYPOTHESES.md)
