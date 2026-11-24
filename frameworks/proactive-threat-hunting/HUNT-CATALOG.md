# Hunt catalog

All procedures produce candidate leads for corroboration. These reference queries target the local normalized schema.

| ID | Procedure | Domains | Baseline required |
|---|---|---|---|
| [H01](hunts/H01.md) | Rare script-interpreter parent | endpoint | True |
| [H02](hunts/H02.md) | Active indicator match in process telemetry | endpoint | False |
| [H03](hunts/H03.md) | Failure burst followed by new-device success | identity | True |
| [H04](hunts/H04.md) | Privileged identity grant outside approved change | identity | False |
| [H05](hunts/H05.md) | Unapproved external mailbox forwarding | email | False |
| [H06](hunts/H06.md) | Suspicious email click followed by new-device sign-in | email, identity | True |
| [H07](hunts/H07.md) | First-observed AWS AI runtime followed by sensitive data access | cloud-aws | True |
| [H08](hunts/H08.md) | Azure role grant followed by sensitive secret read | cloud-azure | False |
| [H09](hunts/H09.md) | Google service-account delegation followed by data read | cloud-gcp | False |
| [H10](hunts/H10.md) | Unapproved privileged Kubernetes workload | kubernetes | False |
| [H11](hunts/H11.md) | First-observed lateral administration destination | network | True |
| [H12](hunts/H12.md) | Burst of first-observed DNS destinations | dns | True |
| [H13](hunts/H13.md) | Large SaaS export through first-observed application | saas | True |
| [H14](hunts/H14.md) | AI retrieval or tool action outside logged policy scope | ai | False |
| [H15](hunts/H15.md) | Consumed artifact differs from approved digest | cicd | False |
| [H16](hunts/H16.md) | Unapproved recovery protection change | backup | False |
| [H17](hunts/H17.md) | Unapproved cloud audit logging change | cloud-aws, cloud-azure, cloud-gcp | False |
