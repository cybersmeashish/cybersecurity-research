# CAI-005 — User-bound authorization for cloud actions executed by AI agents

**A user-bound tool gateway study using a SQLite cloud API**

Version 0.2 · Author: Ashish Srivastava · Prepared 2026-11-24 · Evidence: controlled local synthetic study.

Constructed local mechanism supported; implementation-level and population claims not established. This package contains executed code and measured local evidence. It does not claim a new provider vulnerability, peer review, or a production scanner.

## Main result

The intentionally permissive profile produced **24/24** forbidden effects. The guarded profile produced **0/24**, retained **6/6** legitimate effects, and matched all 36 fixture policy labels. These are authored boundary cases, not deployment prevalence estimates.

## Research components

| Component | Read or run |
|---|---|
| Full research paper | [PAPER.md](PAPER.md) |
| Executive decision brief | [EXECUTIVE-BRIEF.md](EXECUTIVE-BRIEF.md) |
| Threat model and formal boundary | [THREAT-MODEL.md](THREAT-MODEL.md) |
| Methods and experiment plan | [METHOD.md](METHOD.md) · [EXPERIMENT-PLAN.md](EXPERIMENT-PLAN.md) |
| Measured results and interpretation | [RESULTS.md](RESULTS.md) · [DISCUSSION.md](DISCUSSION.md) |
| Claim-to-evidence register | [CLAIM-EVIDENCE.md](CLAIM-EVIDENCE.md) · [Raw evidence](evidence/README.md) |
| Runnable local prototype | [Source](src/study.py) · [Runner](tools/run_study.py) · [Fixtures](lab/fixtures.json) · [Tests](tests/test_study.py) |
| Reproduction | [REPRODUCIBILITY.md](REPRODUCIBILITY.md) · [Lab instructions](lab/README.md) |
| Related work and novelty | [RELATED-WORK.md](RELATED-WORK.md) · [SOURCES.md](SOURCES.md) · [NOVELTY.md](NOVELTY.md) |
| Limits and future validation | [LIMITATIONS.md](LIMITATIONS.md) · [VALIDATION-PROTOCOL.md](VALIDATION-PROTOCOL.md) |
| Tool engineering and roadmap | [TOOL-DESIGN.md](TOOL-DESIGN.md) · [RESEARCH-ROADMAP.md](RESEARCH-ROADMAP.md) |
| Provenance and citation | [PROVENANCE.md](PROVENANCE.md) · [CITATION.cff](CITATION.cff) · [Metadata](research.json) |

[Portfolio index](../CLOUD-AI-SECURITY-HYPOTHESES.md). Runtime source and fixtures are self-contained in this folder. Shared references are navigation only.
