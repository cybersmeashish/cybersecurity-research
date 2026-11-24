# CAI-007 — Action-level impact of adversarial logs on SOC agents

**Status:** proposed research, version 0.1. **Area:** Cloud + AI. **Priority:** 6/10. **Prepared:** 2026-11-24.

No experiments have been run for this proposal and no tool is implemented. No new vulnerability, provider defect, global novelty, or independent validation is claimed.

## Testable hypothesis

Attacker-controlled log text can cause a SOC agent to suppress a seeded incident or execute forbidden mock remediation even when its output conforms to a required schema.

**Null hypothesis:** Adversarial log fields do not alter protected handling beyond factual event content and pre-registered baseline variability.

## Threat model

- **Protected assets:** Incident integrity, alert visibility, triage priority, and remediation rights.
- **Attacker capability:** An actor controlling ordinary logged strings but not SOC instructions or remediation policy.
- **Security boundary:** Log evidence does not become authority to change SOC decisions or actions.

## Proposed contribution and prior art

Measure actual handling and action outcomes separately from schema validity and output wording.

[Primary prior work](SOURCES.md) motivates the threat model; it does not establish this hypothesis in a selected implementation. Prior-art survey and version selection remain pending.

## Intended deliverables

1. A reproducible controlled test harness and bounded evidence.
2. A prototype **SOC-agent adversarial regression suite**, evaluated for false positives and legitimate-workflow utility.
3. A scoped finding or negative result identifying tested versions and limitations.

## Research documents

- [Experiment plan](EXPERIMENT-PLAN.md)
- [Proposed tool design](TOOL-DESIGN.md)
- [Sources](SOURCES.md)
- [Machine-readable record](research.json)
- [Shared validation protocol](../HYPOTHESIS-VALIDATION.md)
- [Research portfolio](../CLOUD-AI-SECURITY-HYPOTHESES.md)
