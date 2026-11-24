# CAI-011 — End-to-end budget enforcement across agent execution graphs

**Status:** proposed research, version 0.1. **Area:** Cloud + AI. **Priority:** 10/10. **Prepared:** 2026-11-24.

No experiments have been run for this proposal and no tool is implemented. No new vulnerability, provider defect, global novelty, or independent validation is claimed.

## Testable hypothesis

Per-request limits fail to bound aggregate task consumption when reasoning, retries, fan-out, and delegation are charged independently without a shared task budget.

**Null hypothesis:** All task-linked work stays within one budget plus a pre-specified maximum in-flight allowance.

## Threat model

- **Protected assets:** Compute, tokens, tool capacity, and task-attributed spending.
- **Attacker capability:** A legitimate requester controlling task content or retrieved text, without budget-administration rights.
- **Security boundary:** One authorized task does not create unaccounted work through retries or delegation.

## Proposed contribution and prior art

Extend reasoning-cost research to accounting across execution graphs; use cost units before currency claims.

[Primary prior work](SOURCES.md) motivates the threat model; it does not establish this hypothesis in a selected implementation. Prior-art survey and version selection remain pending.

## Intended deliverables

1. A reproducible controlled test harness and bounded evidence.
2. A prototype **Agent execution-budget controller**, evaluated for false positives and legitimate-workflow utility.
3. A scoped finding or negative result identifying tested versions and limitations.

## Research documents

- [Experiment plan](EXPERIMENT-PLAN.md)
- [Proposed tool design](TOOL-DESIGN.md)
- [Sources](SOURCES.md)
- [Machine-readable record](research.json)
- [Shared validation protocol](../HYPOTHESIS-VALIDATION.md)
- [Research portfolio](../CLOUD-AI-SECURITY-HYPOTHESES.md)
