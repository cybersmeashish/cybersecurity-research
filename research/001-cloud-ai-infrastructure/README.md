# Cybersecurity Research

Original, reproducible research on the security boundaries of cloud and AI infrastructure. Published by [Ashish Srivastava](https://github.com/cybersmeashish).

## First study: AIA-001 — Who authorizes the runtime?

**A comparative study of authority bindings across AWS, Azure, Google Cloud, Kubernetes, IAM, networking, AI artifacts, RAG and agent tools.**

The research proposes five organizing categories for misconfiguration compositions and tests eight attack-chain models with positive, negative, control and missing-evidence cases. A runnable local experiment demonstrates how a caller denied direct access can still receive an out-of-scope synthetic record through a broadly authorized workload, and how different controls change the result.

**Evidence status:** original synthesis and synthetic local experiments. The categories are candidate taxonomy, not established new vulnerability classes. No live cloud environment was exploited, no provider vulnerability was confirmed, and no peer review, customer deployment or bug bounty award is claimed. Documented defaults are identified separately from test assumptions.

| Read or use | Artifact |
|---|---|
| Main research paper | [Study](studies/001-ai-infrastructure-authority-bindings/PAPER.md) |
| Decision for CEOs/CISOs | [Executive brief](studies/001-ai-infrastructure-authority-bindings/EXECUTIVE-BRIEF.md) |
| Proposed categories and prior art | [Class register](studies/001-ai-infrastructure-authority-bindings/candidate-classes.csv) · [Novelty assessment](studies/001-ai-infrastructure-authority-bindings/NOVELTY.md) |
| Provider-specific prerequisites | [AWS](providers/aws.md) · [Azure](providers/azure.md) · [Google Cloud](providers/google-cloud.md) · [Kubernetes](providers/kubernetes.md) |
| Documented defaults | [Defaults register](studies/001-ai-infrastructure-authority-bindings/DEFAULTS.md) |
| Reusable scenarios | [Chains](studies/001-ai-infrastructure-authority-bindings/chains.json) · [Synthetic fixtures](studies/001-ai-infrastructure-authority-bindings/fixtures.json) |
| Machine-readable findings | [Results](evidence/results.csv) · [Summary](evidence/summary.json) · [Runtime traces](evidence/runtime-results.json) |
| Sources and limitations | [Primary-source register](studies/001-ai-infrastructure-authority-bindings/SOURCES.md) · [Limitations](studies/001-ai-infrastructure-authority-bindings/LIMITATIONS.md) |

## Reproduce

No cloud account, credential, model, SDK or third-party Python package is required. Use [the pinned isolated container workflow](lab/README.md). The graph tool accepts synthetic evidence only in version 0.1; it is not an IAM export parser or infrastructure vulnerability scanner.

## Research program

Extend this study through scoped provider experiments, independent reproduction, evidence-backed novelty review and coordinated disclosure when an actual previously unknown issue is confirmed. See [research backlog](RESEARCH-BACKLOG.md), [contribution protocol](CONTRIBUTING.md), [security reporting](SECURITY.md) and [preparation provenance](PROVENANCE.md).
