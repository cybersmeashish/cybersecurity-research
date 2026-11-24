# Google Cloud / ML custom training

**Evidence status:** documentation comparison and synthetic model. No live provider/cluster experiment.

## Documented behavior

Custom training identity selection requires actAs and relevant workload permissions. Default training, prediction and batch behavior must be reviewed separately. Source identifiers: [GCP-IDENTITY](../studies/001-ai-infrastructure-authority-bindings/SOURCES.md).

## Synthetic chain prerequisites

- `actor_can_submit_job`
- `actor_can_act_as_selected_account`
- `actor_controls_job_code`
- `platform_service_agent_setup_allows_runtime`
- `runtime_data_read_effective_allow`
- `unapproved_disclosure_path_allowed`
- `caller_outside_business_entitlement`

## Evidence to collect for an authorized environment review

Record caller job permission, actAs on the precise service account, service-agent setup, runtime data grants, project constraints, mode-specific behavior and permitted output routes. Include any service agent still accessing data for the chosen mode.

## Interpretation limits

Do not treat default prediction identity as a general data administrator. This model chooses a custom training identity and makes no claim that actAs alone permits an arbitrary platform operation.

The proposed classes and chain shape are the study's synthesis, rather than vendor acknowledgments. [Method](../studies/001-ai-infrastructure-authority-bindings/METHOD.md) · [Full graphs](../studies/001-ai-infrastructure-authority-bindings/chains.json) · [Future validation](../studies/001-ai-infrastructure-authority-bindings/VALIDATION-PROTOCOL.md).

## Documentation route observed during this review

On 24 November 2026 the Vertex AI custom-service-account URL redirected to Google's Gemini Enterprise Agent Platform machine-learning documentation. The current resolved URL, retrieval time and content digest are preserved in [source-review.json](../studies/001-ai-infrastructure-authority-bindings/source-review.json). This study compares the stated custom-training identity mechanism; it does not infer product/API equivalence from the redirect.
