# Cloud and AI security research hypotheses

Ten separate proposals for vulnerability discovery and security tools, prepared on 2026-11-24. Each folder contains a threat model, testable hypothesis, experiment plan, proposed tool, sources, and metadata.

**Evidence status:** proposals only; zero executed experiments and zero confirmed provider vulnerabilities in this collection. Implementation selection, prior-art review, and validation remain pending.

## Research folders

| Priority | Research | Area | Proposed tool |
|---|---|---|---|
| 1 | [CAI-002 — Authorization lineage in RAG-derived artifacts](002-rag-access-control/README.md) | Cloud + AI | RAG authorization lineage tester |
| 2 | [CAI-003 — Principal binding across multi-user MCP authorization flows](003-mcp-authorization-confusion/README.md) | AI | MCP authorization conformance suite |
| 3 | [CAI-004 — Identity lifecycle hazards in workload federation policies](004-workload-identity-federation/README.md) | Cloud | OIDC trust-policy lifecycle auditor |
| 4 | [CAI-005 — User-bound authorization for cloud actions executed by AI agents](005-agent-user-permission-boundary/README.md) | Cloud + AI | Agent user-permission gateway |
| 5 | [CAI-006 — Destination validation across AI connector fetch chains](006-ai-connector-ssrf/README.md) | Cloud + AI | AI connector egress test suite |
| 6 | [CAI-007 — Action-level impact of adversarial logs on SOC agents](007-soc-log-prompt-injection/README.md) | Cloud + AI | SOC-agent adversarial regression suite |
| 7 | [CAI-008 — Trust provenance through agent-memory summarization](008-agent-memory-provenance/README.md) | AI | Agent memory provenance validator |
| 8 | [CAI-009 — Tenant authorization through serverless event chains](009-serverless-tenant-event-flows/README.md) | Cloud | Serverless tenant-flow scanner |
| 9 | [CAI-010 — Tenant enforcement of inference prefix-cache isolation](010-inference-cache-isolation/README.md) | Cloud + AI | Inference-cache isolation auditor |
| 10 | [CAI-011 — End-to-end budget enforcement across agent execution graphs](011-agent-execution-budgets/README.md) | Cloud + AI | Agent execution-budget controller |

## Starting priorities

Priorities are editorial judgments about practical research value, not measured vulnerability prevalence. Start with RAG or MCP for application-focused work, or workload identity federation for cloud-focused work. Cache timing requires more specialized infrastructure and statistical controls.

## Shared resources

- [Validation and evidence protocol](HYPOTHESIS-VALIDATION.md)
- [Machine-readable portfolio index](cloud-ai-security-hypotheses.json)
- [Retrieved source register](hypothesis-source-review.json)

Earlier studies retain their separate evidence status; their results do not validate these proposals.
