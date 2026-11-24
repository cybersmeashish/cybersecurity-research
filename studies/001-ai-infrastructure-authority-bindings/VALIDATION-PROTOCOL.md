# Future provider validation protocol

Status: proposed; no live experiment has been performed or funded.

1. Record authorization, account/subscription/project/namespace scope, owner, synthetic data, service/version, quotas and teardown plan. Use isolated resources with no production trust or sensitive data.
2. State the business policy first: which actor may run which workload on which data, return which output and call which tool. Intentional compute delegation alone is not a bug.
3. Record all effective authorization controls and identity modes. For AWS include passing/using the role, service trust and account constraints; for Azure record the actual job/data credential path; for Google separate custom training, prediction and service-agent exceptions; for Kubernetes record admission, service account, token validity and RBAC.
4. Collect the actual admitted artifact digest and consumed digest. Separately observe private ingress, egress, approved output channels and network implementation. Do not infer enforcement from a manifest or private-endpoint flag.
5. Establish direct-access denial, exercise the permitted synthetic job and collect the exact returned canary or denied operation. Do not probe third-party destinations or use real client records.
6. Remove each proposed prerequisite/control separately. Exercise an intended same-tenant operation. Preserve raw, redacted timestamps, requests, policies, returned identifiers and audit events.
7. Label outcomes: confirmed unauthorized provider outcome; blocked specific path; legitimate delegation; insufficient evidence; or unexpected behavior needing vendor triage.
8. Repeat from a clean configuration, obtain independent reproduction, broaden prior-art review and handle any non-public issue through the appropriate disclosure channel before publication.

Before live validation, extend the versioned schema and tests. The version-0.1 graph tool deliberately accepts only synthetic fixtures and cannot convert them into provider findings.
