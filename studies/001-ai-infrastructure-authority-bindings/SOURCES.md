# Primary-source register

Reviewed on **24 November 2026**. These nine pages are a bounded documentation basis. Their original statements, the authoring inference and the local test result are different kinds of evidence. No external source text is reproduced.

## AWS-IAM — Grant a user permissions to pass a role to an AWS service

Publisher: AWS · [Read source](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)

Supported scope: Passing a role is controlled by iam:PassRole; scope approved roles and services. Passing roles across accounts is not directly supported. PassRole itself is not a separately logged API operation.

Does not establish: A working escalation path without job permissions, service trust, runtime control and effective data permissions.

## AWS-TRAIN — CreateTrainingJob API

Publisher: AWS · [Read source](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)

Supported scope: Training jobs specify RoleArn and require caller PassRole permission. VPC configuration and network isolation are separate settings.

Does not establish: That every role or training container has broad data access, or that cloud execution was tested here.

## AZ-IDENTITY — Set up authentication between Azure Machine Learning and other services

Publisher: Microsoft · [Read source](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-identity-based-service-authentication?view=azureml-api-2)

Supported scope: Job data access can use compute identity, user identity or stored credentials. Compute identity may intentionally read data unavailable directly to a scientist. Autocreated ACR enables its admin account; workspace-kind-specific data isolation defaults differ.

Does not establish: That managed-identity execution is itself unauthorized, or that these defaults are identical for every workspace creation path.

## GCP-IDENTITY — Use a custom service account

Publisher: Google Cloud · [Read source](https://docs.cloud.google.com/vertex-ai/docs/general/custom-service-account)

Supported scope: Attaching a custom runtime service account requires actAs. Default custom training and prediction identities differ; prediction defaults should not be assumed to grant general data access. Batch inference data access has a documented service-agent exception.

Does not establish: Equivalent privileges across Vertex AI modes or a tested project-specific escalation.

## K8S-SA — Service Accounts

Publisher: Kubernetes · [Read source](https://kubernetes.io/docs/concepts/security/service-accounts/)

Supported scope: Assigned service-account credentials are mounted unless disabled. Modern projected tokens rotate and have binding/audience constraints. Default service accounts have limited default RBAC rights.

Does not establish: Administrator rights from the default service account or token validity without its checks.

## K8S-RBAC — Role Based Access Control Good Practices

Publisher: Kubernetes · [Read source](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)

Supported scope: Workload creation can expose namespace resources and service-account privileges. Namespace trust separation and least privilege matter.

Does not establish: Every pod creator can use every identity; admission and other effective controls must be checked.

## K8S-NET — Network Policies

Publisher: Kubernetes · [Read source](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

Supported scope: Ingress and egress isolation are independent. Pods start non-isolated for either direction; applicable allow policies combine. Enforcement requires a supporting network implementation.

Does not establish: That a policy file is enforced, that it authorizes an application operation, or that behavior is identical for hostNetwork, NAT and existing connections.

## OWASP-AGENCY — Excessive Agency, published 2025 edition

Publisher: OWASP · [Read source](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html)

Supported scope: Generic privileged tool identities and insufficient downstream authorization can enable damaging agent actions.

Does not establish: An LLM attack success rate, new vulnerability class, or the latest OWASP category numbering.

## SLSA-VERIFY — Verifying artifacts, specification v1.1

Publisher: SLSA · [Read source](https://slsa.dev/spec/v1.1/verifying-artifacts)

Supported scope: Artifact verification includes trusted identity, signature, subject digest and expected provenance values.

Does not establish: That a digest check alone establishes trusted provenance or that this lab implements SLSA verification.

Machine-readable register: [sources.json](sources.json). URLs are moving documentation; recheck exact deployment/version before applying the comparison.

[Retrieval receipt](source-review.json) records HTTP status, original/resolved URL, retrieval time and raw HTML digest for all nine sources. Raw documentation is cached privately in the development workspace and is not redistributed. The Google custom-service-account page redirected from its Vertex AI URL to Gemini Enterprise Agent Platform machine-learning documentation on the review date; the study does not infer undocumented API equivalence.
