# CAI-008 — Trust provenance through agent-memory summarization

**Status:** proposed research, version 0.1. **Area:** AI. **Priority:** 7/10. **Prepared:** 2026-11-24.

No experiments have been run for this proposal and no tool is implemented. No new vulnerability, provider defect, global novelty, or independent validation is claimed.

## Testable hypothesis

A summarizer dropping source trust labels can promote low-trust instructions into authoritative recalled guidance, causing a forbidden later-session action without the original adversarial input being present.

**Null hypothesis:** Source trust boundaries remain effective after summarization and recall.

## Threat model

- **Protected assets:** Persistent memory, recalled guidance, and future tool decisions.
- **Attacker capability:** A contributor to a low-trust memory source, without trusted-policy or memory-administration access.
- **Security boundary:** Summarization does not increase source authority.

## Proposed contribution and prior art

Evaluate trust-label survival through memory compaction; general memory poisoning is prior art.

[Primary prior work](SOURCES.md) motivates the threat model; it does not establish this hypothesis in a selected implementation. Prior-art survey and version selection remain pending.

## Intended deliverables

1. A reproducible controlled test harness and bounded evidence.
2. A prototype **Agent memory provenance validator**, evaluated for false positives and legitimate-workflow utility.
3. A scoped finding or negative result identifying tested versions and limitations.

## Research documents

- [Experiment plan](EXPERIMENT-PLAN.md)
- [Proposed tool design](TOOL-DESIGN.md)
- [Sources](SOURCES.md)
- [Machine-readable record](research.json)
- [Shared validation protocol](../HYPOTHESIS-VALIDATION.md)
- [Research portfolio](../CLOUD-AI-SECURITY-HYPOTHESES.md)
