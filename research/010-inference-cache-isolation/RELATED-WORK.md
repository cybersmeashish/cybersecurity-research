# Related work — CAI-010

| Reference | Established scope used here | Local question |
|---|---|---|
| [S1](SOURCES.md#s1) | Prefix cache keys and cache-salt support for isolating reuse. | A cache namespace derived only from a caller-controlled salt can share prefix state across tenants; a trusted tenant namespace prevents cross-tenant cache hits in this fixture model. |
| [S2](SOURCES.md#s2) | Agent authorization, memory trust, delegation, and bounded autonomy. | A cache namespace derived only from a caller-controlled salt can share prefix state across tenants; a trusted tenant namespace prevents cross-tenant cache hits in this fixture model. |

The source scope is limited to the referenced guidance or paper. Official recommendations are not measurements of deployment prevalence. Research papers do not validate an untested extension. No exhaustive survey or systematic-review claim is made.

[The repository's earlier AIA-001 paper](../001-cloud-ai-infrastructure/studies/001-ai-infrastructure-authority-bindings/PAPER.md) provides a related authority-binding synthesis and separate synthetic experiments. Its results are not imported as evidence for this package.
