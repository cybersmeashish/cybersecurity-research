# Primary-source register

References checked on 24 November 2026. These references support platform/event semantics and technique context; the local hunt logic, thresholds and fixtures are the framework contribution. No external source text is reproduced.

## MITRE — MITRE ATT&CK

[Official reference](https://attack.mitre.org/)

Supported reference scope: Behavior vocabulary and technique context; a mapping is not proof of attacker identity.

## CISA — Best practices for event logging and threat detection

[Official reference](https://www.cisa.gov/resources-tools/resources/best-practices-event-logging-and-threat-detection)

Supported reference scope: Logging and centralized visibility guidance; local source-health evidence is still required.

## MDE — Advanced hunting overview

[Official reference](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview)

Supported reference scope: Defender hunting across supported security domains; table availability depends on product, connector and license.

## AWS — CloudTrail userIdentity element

[Official reference](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html)

Supported reference scope: Principal, session and delegation context in CloudTrail; selected runtime identity needs separate service/data events.

## AZURE — Azure Activity Log schema

[Official reference](https://learn.microsoft.com/en-us/azure/azure-monitor/platform/activity-log-schema)

Supported reference scope: Control-plane actor, resource and correlation metadata; data-plane reads require additional resource logs.

## GCP — Understanding audit logs

[Official reference](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs)

Supported reference scope: Audit authentication, authorization and operation context; delegated actor evidence must be preserved.

## GCP-DATA — Configure Data Access audit logs

[Official reference](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)

Supported reference scope: Data Access logging configuration must be checked rather than assumed.

## K8S — Auditing

[Official reference](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)

Supported reference scope: Audit policies/stages determine which request fields are observable; Metadata alone does not show full pod settings.

## OCSF — Open Cybersecurity Schema Framework

[Official reference](https://github.com/ocsf/ocsf-schema)

Supported reference scope: An optional normalization reference; this lab uses its own simplified schema and does not claim OCSF conformance.

## T1114.003 — Email Forwarding Rule

[Official reference](https://attack.mitre.org/techniques/T1114/003/)

Supported reference scope: Context for mailbox forwarding hunts, subject to the actual observed behavior.

## T1059.001 — PowerShell

[Official reference](https://attack.mitre.org/techniques/T1059/001/)

Supported reference scope: Context for the process-interpreter hunt; process name alone does not establish malicious use.

## T1078 — Valid Accounts

[Official reference](https://attack.mitre.org/techniques/T1078/)

Supported reference scope: Context for identity hunts; a new device or failed login is not by itself account compromise.

## T1490 — Inhibit System Recovery

[Official reference](https://attack.mitre.org/techniques/T1490/)

Supported reference scope: Context for recovery-control changes; legitimate maintenance is a required alternative explanation.

[Retrieval metadata](../source-review.json) records successful HTTP status, original/resolved URL, retrieval time and content digest. Raw page caches remain outside the public repository. [Machine-readable register](../sources.json).

AWS PassRole context additionally derives from the existing research [primary-source register](../../../research/001-cloud-ai-infrastructure/studies/001-ai-infrastructure-authority-bindings/SOURCES.md). There is no standalone PassRole API event to query. Source availability does not establish that a production connector is enabled or a query is validated.
