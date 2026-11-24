# CAI-003 — Principal binding across multi-user MCP authorization flows

**Status:** proposed research, version 0.1. **Area:** AI. **Priority:** 2/10. **Prepared:** 2026-11-24.

No experiments have been run for this proposal and no tool is implemented. No new vulnerability, provider defect, global novelty, or independent validation is claimed.

## Testable hypothesis

A multi-user MCP proxy with incomplete binding among user, client, session, consent, and token audience can accept an authorization artifact created for a different principal or client.

**Null hypothesis:** Authorization artifacts remain bound to their intended principal, client, resource, and lifecycle state.

## Threat model

- **Protected assets:** Tool permissions, consent state, downstream tokens, and user-specific results.
- **Attacker capability:** A legitimate user or registered client controlling its own requests, without another user's credentials.
- **Security boundary:** Proxy authorization state retains the correct user, client, and resource bindings.

## Proposed contribution and prior art

Find implementation-specific binding failures; confused-deputy and token-passthrough classes are documented prior art.

[Primary prior work](SOURCES.md) motivates the threat model; it does not establish this hypothesis in a selected implementation. Prior-art survey and version selection remain pending.

## Intended deliverables

1. A reproducible controlled test harness and bounded evidence.
2. A prototype **MCP authorization conformance suite**, evaluated for false positives and legitimate-workflow utility.
3. A scoped finding or negative result identifying tested versions and limitations.

## Research documents

- [Experiment plan](EXPERIMENT-PLAN.md)
- [Proposed tool design](TOOL-DESIGN.md)
- [Sources](SOURCES.md)
- [Machine-readable record](research.json)
- [Shared validation protocol](../HYPOTHESIS-VALIDATION.md)
- [Research portfolio](../CLOUD-AI-SECURITY-HYPOTHESES.md)
