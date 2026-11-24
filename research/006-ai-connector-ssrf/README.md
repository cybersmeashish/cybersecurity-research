# CAI-006 — Destination validation across AI connector fetch chains

**Status:** proposed research, version 0.1. **Area:** Cloud + AI. **Priority:** 5/10. **Prepared:** 2026-11-24.

No experiments have been run for this proposal and no tool is implemented. No new vulnerability, provider defect, global novelty, or independent validation is claimed.

## Testable hypothesis

A connector validating only an initial URL or DNS answer can contact a forbidden internal destination after a redirect or changed resolution alters the actual connection target.

**Null hypothesis:** Each connection and redirect hop remains within the declared destination policy.

## Threat model

- **Protected assets:** Internal services, metadata-like endpoints, and connector response data.
- **Attacker capability:** A user controlling a supplied fetch or discovery URL, without internal-network privileges.
- **Security boundary:** Selecting an external URL does not grant internal-network access.

## Proposed contribution and prior art

Evaluate consistent enforcement across AI fetch and discovery paths; SSRF is established prior art.

[Primary prior work](SOURCES.md) motivates the threat model; it does not establish this hypothesis in a selected implementation. Prior-art survey and version selection remain pending.

## Intended deliverables

1. A reproducible controlled test harness and bounded evidence.
2. A prototype **AI connector egress test suite**, evaluated for false positives and legitimate-workflow utility.
3. A scoped finding or negative result identifying tested versions and limitations.

## Research documents

- [Experiment plan](EXPERIMENT-PLAN.md)
- [Proposed tool design](TOOL-DESIGN.md)
- [Sources](SOURCES.md)
- [Machine-readable record](research.json)
- [Shared validation protocol](../HYPOTHESIS-VALIDATION.md)
- [Research portfolio](../CLOUD-AI-SECURITY-HYPOTHESES.md)
