# Related work — CAI-003

| Reference | Established scope used here | Local question |
|---|---|---|
| [S1](SOURCES.md#s1) | Confused-deputy risks, token audience validation, token passthrough, and SSRF defenses. | Valid signatures and expiry do not authorize a principal/client/resource mismatch; all bindings required by the declared proxy contract must hold. |
| [S2](SOURCES.md#s2) | Validation and audience binding; the local prototype is not standards certification. | Valid signatures and expiry do not authorize a principal/client/resource mismatch; all bindings required by the declared proxy contract must hold. |
| [S3](SOURCES.md#s3) | Authorization-flow threat models; no complete OAuth implementation is tested. | Valid signatures and expiry do not authorize a principal/client/resource mismatch; all bindings required by the declared proxy contract must hold. |
| [S4](SOURCES.md#s4) | Implementation security controls; vulnerable deployment prevalence is not established. | Valid signatures and expiry do not authorize a principal/client/resource mismatch; all bindings required by the declared proxy contract must hold. |

The source scope is limited to the referenced guidance or paper. Official recommendations are not measurements of deployment prevalence. Research papers do not validate an untested extension. No exhaustive survey or systematic-review claim is made.

[The repository's earlier AIA-001 paper](../001-cloud-ai-infrastructure/studies/001-ai-infrastructure-authority-bindings/PAPER.md) provides a related authority-binding synthesis and separate synthetic experiments. Its results are not imported as evidence for this package.
