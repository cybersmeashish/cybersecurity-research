# Kubernetes / RBAC, admission and networking

**Evidence status:** documentation comparison and synthetic model. No live provider/cluster experiment.

## Documented behavior

Workload creation can confer namespace/service-account authority. Token availability, its validity and effective permissions are separate prerequisites. Source identifiers: [K8S-SA, K8S-RBAC, K8S-NET](../studies/001-ai-infrastructure-authority-bindings/SOURCES.md).

## Synthetic chain prerequisites

- `actor_can_create_workload`
- `admission_allows_selected_service_account`
- `actor_controls_job_code`
- `service_account_token_available_and_valid`
- `runtime_data_read_effective_allow`
- `unapproved_disclosure_path_allowed`
- `caller_outside_business_entitlement`

## Evidence to collect for an authorized environment review

Record effective create/patch/exec scope, actual serviceAccountName, admission decisions, service-account bindings, token audience/binding/expiry, reachable APIs and effective networking. Observe the selected network implementation and additive egress rules.

## Interpretation limits

Default service accounts are not default administrators. Ingress restriction does not imply egress restriction. This research does not create a cluster, decode credentials or validate CNI packet behavior.

The proposed classes and chain shape are the study's synthesis, rather than vendor acknowledgments. [Method](../studies/001-ai-infrastructure-authority-bindings/METHOD.md) · [Full graphs](../studies/001-ai-infrastructure-authority-bindings/chains.json) · [Future validation](../studies/001-ai-infrastructure-authority-bindings/VALIDATION-PROTOCOL.md).
