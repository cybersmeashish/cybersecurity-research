# Documented defaults and configuration traps

These are a dated documentation review, not newly discovered defaults or observations from deployed providers. The word "default" always needs a service, operation, creation path and configuration context.

| Scope | Documented behavior | Review implication | Source | Tested here? |
|---|---|---|---|---|
| Kubernetes networking | Pods initially lack directional isolation; ingress and egress policies are independent. | Observe outbound restriction independently, including additional allow policies and enforcement. | [K8S-NET](SOURCES.md) | Modeled only; no CNI |
| Kubernetes identity | Assigned service-account credentials mount unless disabled; default-account RBAC is limited. | Token availability is not proof of privilege. Check identity scope and token validity. | [K8S-SA](SOURCES.md) | Modeled only; no cluster |
| Azure ML resource creation | The reviewed documentation says auto-created ACR enables its admin account. | Review that creation path and disable unnecessary registry admin credentials. | [AZ-IDENTITY](SOURCES.md) | Documentation only |
| Azure ML shared resources | Data-isolation defaults differ for standalone default workspaces and hub/project workspaces. | Record workspace kind and isolation state rather than treating all AML workspaces alike. | [AZ-IDENTITY](SOURCES.md) | Documentation only |
| Vertex AI identity modes | Default custom training and prediction use different identities. Prediction default access is limited to supplied artifacts. | Avoid assigning training-agent privilege assumptions to prediction containers. | [GCP-IDENTITY](SOURCES.md) | Documentation only |
| AWS SageMaker networking | VPC selection and training-container network isolation are separate controls. | Record both settings and approved service/output paths. | [AWS-TRAIN](SOURCES.md) | Modeled only; no AWS job |

A supported default can be appropriate for one workload and unsafe in a different trust context. Review the complete chain and business entitlement before asserting a vulnerability. There is no assertion that all listed defaults are inherently insecure or universally enabled.
