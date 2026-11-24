# Azure / Azure Machine Learning

**Evidence status:** documentation comparison and synthetic model. No live provider/cluster experiment.

## Documented behavior

Managed compute may intentionally access data that the submitting user cannot directly read. Data-authentication mode determines the relevant principal. Source identifiers: [AZ-IDENTITY](../studies/001-ai-infrastructure-authority-bindings/SOURCES.md).

## Synthetic chain prerequisites

- `actor_can_submit_job`
- `actor_can_use_selected_compute`
- `actor_controls_job_code`
- `compute_identity_available`
- `runtime_data_read_effective_allow`
- `unapproved_disclosure_path_allowed`
- `caller_outside_business_entitlement`

## Evidence to collect for an authorized environment review

Record actual job and step identity, compute use authorization, credential-bearing datastore versus identity mode, runtime effective data assignments, storage restrictions and output channels. Review the actual workspace/registry creation settings rather than inferred global defaults.

## Interpretation limits

The model does not assert that a submitter can assign a new managed identity, mutate an existing endpoint identity or bypass Entra authorization. Intentional delegated compute access can be valid business policy.

The proposed classes and chain shape are the study's synthesis, rather than vendor acknowledgments. [Method](../studies/001-ai-infrastructure-authority-bindings/METHOD.md) · [Full graphs](../studies/001-ai-infrastructure-authority-bindings/chains.json) · [Future validation](../studies/001-ai-infrastructure-authority-bindings/VALIDATION-PROTOCOL.md).
