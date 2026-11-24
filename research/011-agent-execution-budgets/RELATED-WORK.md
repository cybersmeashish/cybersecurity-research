# Related work — CAI-011

| Reference | Established scope used here | Local question |
|---|---|---|
| [S1](SOURCES.md#s1) | Reasoning-cost amplification; accounting across execution graphs is the extension proposed here. | Independent per-call caps cannot bound aggregate task work; an atomic shared budget prevents the constructed retry and fan-out workloads from exceeding their declared allowance. |
| [S2](SOURCES.md#s2) | Agent authorization, memory trust, delegation, and bounded autonomy. | Independent per-call caps cannot bound aggregate task work; an atomic shared budget prevents the constructed retry and fan-out workloads from exceeding their declared allowance. |

The source scope is limited to the referenced guidance or paper. Official recommendations are not measurements of deployment prevalence. Research papers do not validate an untested extension. No exhaustive survey or systematic-review claim is made.

[The repository's earlier AIA-001 paper](../001-cloud-ai-infrastructure/studies/001-ai-infrastructure-authority-bindings/PAPER.md) provides a related authority-binding synthesis and separate synthetic experiments. Its results are not imported as evidence for this package.
