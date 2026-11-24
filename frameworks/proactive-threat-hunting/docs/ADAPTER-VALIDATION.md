# Adapting the reference model to real telemetry

No production adapter or native SIEM query is implemented or validated in version 0.1. SQL queries target the checked-in SQLite schema. Before translating to KQL, SPL, ES|QL, SQL or another platform, verify schema/product version, available connectors/license, actual event semantics, timestamp fields and joins. Compare raw events against independently known test actions and benign controls.

| Domain | Evidence families | Important normalization limitation |
|---|---|---|
| Endpoint | Process, file, registry, authentication and EDR network events | PID reuse, ancestry, sensor gaps, user/session and signed binary context |
| Identity | Sign-ins, MFA/conditional access, directory audit, consent and privilege | Immutable tenant-scoped subjects, actual session/device, explicit approval |
| Email | Delivery, URL click, mailbox audit, forwarding/rule changes | Human/scanner clicks, actual mailbox identity and rule scope |
| AWS | CloudTrail management and selected data events, service job event, object/flow logs | Selected role, runtime and workload correlation; `iam:PassRole` is not a separate API event |
| Azure | Activity Log, Entra sign-in/audit, resource logs such as Key Vault | Control-plane grant does not supply secret-read evidence; grantor differs from grantee |
| Google Cloud | Admin Activity, explicitly available Data Access, delegation/authorization | Preserve original/effective actor; do not assume all Data Access logs are enabled |
| Kubernetes | Audit policy/level/stage, admission, runtime and CNI logs | Metadata-only audit may not expose requested privileged settings; requested is not necessarily running |
| Network/DNS | Flow, proxy, resolver and authenticated management telemetry | NAT, direction, process/source attribution, blocked/allowed and resolver scope |
| SaaS | Admin, consent, session and export activity | Provider subject/app scope, actual data objects and approved export purpose |
| AI | Retrieval lineage, policy gate, model/tool request and output audit | Deterministic entitlement evidence, actor/runtime separation, no prompt/response content needed by default |
| CI/CD | Approval, digest/provenance, runner and actual artifact consumption | Consumed digest versus tag, trusted verifier and publisher context |
| Backup | Protection config, delete/retention, restore and independent audit | Intentional lifecycle changes versus disabled recovery; test restoration separately |

Acceptance: positive seed is found; benign operation preserved; cross-tenant/time joins fail safely; missing required telemetry remains inconclusive; duplicates do not inflate a signal; expired IOC rejected; true source/retention/ingest limitations are recorded. Preserve platform-specific validation evidence rather than importing the local lab's pass counts.
