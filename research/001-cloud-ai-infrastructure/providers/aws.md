# AWS / SageMaker and IAM

**Evidence status:** documentation comparison and synthetic model. No live provider/cluster experiment.

## Documented behavior

The documented training job selects RoleArn and requires PassRole. Passing the role is different from directly assuming it. Source identifiers: [AWS-IAM, AWS-TRAIN](../studies/001-ai-infrastructure-authority-bindings/SOURCES.md).

## Synthetic chain prerequisites

- `actor_can_submit_job`
- `actor_can_pass_selected_role`
- `same_account_passrole`
- `service_trust_allows_role`
- `actor_controls_job_code`
- `runtime_data_read_effective_allow`
- `unapproved_disclosure_path_allowed`
- `caller_outside_business_entitlement`

## Evidence to collect for an authorized environment review

Review selected role ARN, caller effective job and PassRole scope, trust, boundaries/organization controls, training code, effective data scope and all output destinations. Verify network-isolation configuration separately from VPC selection.

## Interpretation limits

PassRole alone is insufficient. There is no standalone PassRole API event; correlate the service operation receiving the role. The study does not attempt cross-account passing or deploy a training job.

The proposed classes and chain shape are the study's synthesis, rather than vendor acknowledgments. [Method](../studies/001-ai-infrastructure-authority-bindings/METHOD.md) · [Full graphs](../studies/001-ai-infrastructure-authority-bindings/chains.json) · [Future validation](../studies/001-ai-infrastructure-authority-bindings/VALIDATION-PROTOCOL.md).
