# Cloud and AI security research portfolio

Ten separate research packages expanded from the original hypotheses. Each has a full paper, threat model, method, actual local experiments, raw evidence, tested source, controls, claim register, related work, limits, reproducibility, tool design, and future validation protocol.

**Evidence stage:** controlled local synthetic studies. The ten packages contain 360 authored fixtures, 1,080 fixture-condition trials, and 60 behavioral regression methods. The cache package adds 192 held-out timing probes and 96 calibration probes. Regression replays and setup work are not counted as extra independent research samples. No model calls, live-provider experiments, or confirmed provider vulnerabilities are claimed.

| Research | Paper | Fixtures | Condition trials | Regression methods |
|---|---|---|---|---|
| CAI-002 | [Authorization lineage in RAG-derived artifacts](002-rag-access-control/PAPER.md) | 36 | 108 | 6 |
| CAI-003 | [Principal binding across multi-user MCP authorization flows](003-mcp-authorization-confusion/PAPER.md) | 36 | 108 | 6 |
| CAI-004 | [Identity lifecycle hazards in workload federation policies](004-workload-identity-federation/PAPER.md) | 36 | 108 | 6 |
| CAI-005 | [User-bound authorization for cloud actions executed by AI agents](005-agent-user-permission-boundary/PAPER.md) | 36 | 108 | 6 |
| CAI-006 | [Destination validation across AI connector fetch chains](006-ai-connector-ssrf/PAPER.md) | 36 | 108 | 6 |
| CAI-007 | [Action-level impact of adversarial logs on SOC agents](007-soc-log-prompt-injection/PAPER.md) | 36 | 108 | 6 |
| CAI-008 | [Trust provenance through agent-memory summarization](008-agent-memory-provenance/PAPER.md) | 36 | 108 | 6 |
| CAI-009 | [Tenant authorization through serverless event chains](009-serverless-tenant-event-flows/PAPER.md) | 36 | 108 | 6 |
| CAI-010 | [Tenant enforcement of inference prefix-cache isolation](010-inference-cache-isolation/PAPER.md) | 36 | 108 | 6 |
| CAI-011 | [End-to-end budget enforcement across agent execution graphs](011-agent-execution-budgets/PAPER.md) | 36 | 108 | 6 |

## Conclusions and scope

The deliberately permissive profiles expose the constructed boundary mechanisms; corrected profiles match all authored policy labels. These counts describe the provided corpus, not real-world prevalence, model attack-success rates, or a production benchmark. The SOC and memory studies use structured replay/compaction, and the cache study uses CPU work rather than a GPU inference deployment. Read each paper's evaluated local proposition and limitations before using its conclusions.

[Shared validation protocol](HYPOTHESIS-VALIDATION.md) · [Machine-readable index](cloud-ai-security-hypotheses.json) · [Primary-source retrieval register](hypothesis-source-review.json).
