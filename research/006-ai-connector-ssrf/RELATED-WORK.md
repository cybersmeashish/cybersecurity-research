# Related work — CAI-006

| Reference | Established scope used here | Local question |
|---|---|---|
| [S1](SOURCES.md#s1) | Confused-deputy risks, token audience validation, token passthrough, and SSRF defenses. | Initial destination approval does not constrain later HTTP connections unless every redirect and the actual connected address remain inside the allowlist. |
| [S2](SOURCES.md#s2) | Implementation security controls; vulnerable deployment prevalence is not established. | Initial destination approval does not constrain later HTTP connections unless every redirect and the actual connected address remain inside the allowlist. |

The source scope is limited to the referenced guidance or paper. Official recommendations are not measurements of deployment prevalence. Research papers do not validate an untested extension. No exhaustive survey or systematic-review claim is made.

[The repository's earlier AIA-001 paper](../001-cloud-ai-infrastructure/studies/001-ai-infrastructure-authority-bindings/PAPER.md) provides a related authority-binding synthesis and separate synthetic experiments. Its results are not imported as evidence for this package.
