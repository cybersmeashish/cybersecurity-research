# CAI-010 — Tenant enforcement of inference prefix-cache isolation

**Status:** proposed research, version 0.1. **Area:** Cloud + AI. **Priority:** 9/10. **Prepared:** 2026-11-24.

No experiments have been run for this proposal and no tool is implemented. No new vulnerability, provider defect, global novelty, or independent validation is claimed.

## Testable hypothesis

A gateway omitting tenant cache partitioning or allowing another tenant's cache salt enables above-chance inference of whether a chosen prompt prefix was processed by that tenant.

**Null hypothesis:** Cross-tenant prefix membership cannot be distinguished above the pre-registered chance baseline under tested load and noise.

## Threat model

- **Protected assets:** Prompt-prefix membership and inference timing; full prompt reconstruction is outside this initial scope.
- **Attacker capability:** A tenant observing only their own requests and latency, without server telemetry or another tenant's requests.
- **Security boundary:** Shared caching does not expose another tenant's request membership.

## Proposed contribution and prior art

Test gateway enforcement of existing cache isolation; cache timing risk and salting mechanisms are established.

[Primary prior work](SOURCES.md) motivates the threat model; it does not establish this hypothesis in a selected implementation. Prior-art survey and version selection remain pending.

## Intended deliverables

1. A reproducible controlled test harness and bounded evidence.
2. A prototype **Inference-cache isolation auditor**, evaluated for false positives and legitimate-workflow utility.
3. A scoped finding or negative result identifying tested versions and limitations.

## Research documents

- [Experiment plan](EXPERIMENT-PLAN.md)
- [Proposed tool design](TOOL-DESIGN.md)
- [Sources](SOURCES.md)
- [Machine-readable record](research.json)
- [Shared validation protocol](../HYPOTHESIS-VALIDATION.md)
- [Research portfolio](../CLOUD-AI-SECURITY-HYPOTHESES.md)
