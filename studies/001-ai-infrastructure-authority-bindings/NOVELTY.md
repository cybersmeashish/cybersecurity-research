# Novelty and prior-art assessment

The five category names in this study are proposed organizing terms. They are not claims that the underlying behaviors were first discovered here. AWS already documents the authority conferred by passing roles; Kubernetes documents workload-creation escalation risks; OWASP already covers excessive tool permissions and shared privileged identities. The Azure and Google identity modes are documented product behavior.

The original contribution is a common, explicit-precondition comparison; a reusable three-state model that distinguishes absent evidence from denied access; per-precondition counterfactuals; and a local authorization experiment with published traces. These contributions have not received independent review.

The source search was bounded to nine primary documentation pages reviewed on 24 November 2026. It did not systematically search conference proceedings, CVE databases, commercial cloud-security tools, all bug-bounty disclosures or all prior taxonomies. Therefore global novelty cannot be concluded.

| Proposal | Existing explanation | Remaining research question |
|---|---|---|
| AB-01 runtime authority drift | Role delegation, confused-deputy risk, RBAC workload authority | Can an evidence-binding schema reveal missed paths in reviewed real AI platforms? |
| AB-02 artifact authority drift | Software supply-chain and admission-time integrity risk | Which artifact and runtime-identity combinations are under-observed in real AI pipelines? |
| AB-03 retrieval detachment | Missing object/tenant authorization and privileged service identity | Can original-document entitlement be maintained through extraction, chunks, indexes and cached answers? |
| AB-04 ingress/egress substitution | Independent network directions and incomplete assurance | Can measurement distinguish effective egress restriction from declared network configuration? |
| AB-05 agent action detachment | Excessive agency and downstream authorization gaps | What policy contract makes actor, action and tool identity traceable through multiple agents? |

A future claim of a new class requires a broader prior-art review, a precise distinguishing mechanism, independent review and reproducible provider evidence. A future provider finding requires the vendor/version/configuration, all prerequisites, observable unauthorized impact, negative controls and the relevant disclosure process. No CVE, CVSS score, provider acknowledgment or HackerOne submission exists for this study.
