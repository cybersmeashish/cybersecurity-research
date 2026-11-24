# Cybersecurity Research

By [Ashish Srivastava](https://github.com/cybersmeashish). Research, defensive frameworks and reproducible evidence for cloud and AI infrastructure security.

## Two self-contained workspaces

| Folder | Content and evidence stage |
|---|---|
| [research/001-cloud-ai-infrastructure](research/001-cloud-ai-infrastructure/README.md) | The complete AIA-001 authority-binding study: paper, code, 144 synthetic cases, 24 local mock-runtime cases, provider comparisons, sources and limitations. All original study material is collected here. |
| [frameworks/proactive-threat-hunting](frameworks/proactive-threat-hunting/README.md) | A proactive hunting operating framework covering 13 telemetry domains, 17 hunt procedures, reusable templates, normalized reference queries and locally tested synthetic scenarios. |

[Research paper](research/001-cloud-ai-infrastructure/studies/001-ai-infrastructure-authority-bindings/PAPER.md) · [Threat-hunting method](frameworks/proactive-threat-hunting/docs/OPERATING-MODEL.md) · [Hunt catalog](frameworks/proactive-threat-hunting/HUNT-CATALOG.md) · [Publication/relocation evidence](migration/README.md).

Research observations, candidate investigation leads and confirmed operational incidents are different evidence stages. The research does not claim new provider vulnerabilities. The framework's SQL is tested against its own local schema, with no live customer hunt or production SIEM validation claimed. [Preparation provenance](PROVENANCE.md).

## Reproduce and extend

Use the [OrbStack workflow](AGENTS.md), [research reproduction](research/001-cloud-ai-infrastructure/lab/README.md) and [hunt laboratory](frameworks/proactive-threat-hunting/lab/README.md). Final verification runs both workspaces with external networking disabled and the source mounted read-only.

[Contribution protocol](CONTRIBUTING.md) · [Security reporting](SECURITY.md) · [Portfolio index](portfolio-index.json).

## Ten cloud and AI security research packages

[Browse the full research portfolio](research/CLOUD-AI-SECURITY-HYPOTHESES.md): ten separate papers with threat models, executable local labs, raw evidence, controls, tool designs, references, and reproduction instructions.

The packages report 1,080 controlled fixture-condition trials and 60 regression methods. They are bounded synthetic studies; no live-provider vulnerability or model-level validation is claimed.
