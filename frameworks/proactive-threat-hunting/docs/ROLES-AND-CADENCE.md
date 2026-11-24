# Roles, cadence and executive reporting

| Role | Responsibility |
|---|---|
| Hunt lead | Hypothesis, scope, procedure, analysis, evidence and disposition |
| Telemetry/platform owner | Actual source configuration, field availability, health and retention |
| Identity/application owner | Canonical subject mapping, approvals and business entitlement |
| Incident decision owner | Escalation and response authority |
| Data/evidence owner | Access, minimization, retention and sharing rules |
| Reviewer | Challenge the explanation, test blind spots and approve closure |

Example cadence: review telemetry changes and priority hypotheses weekly; run a bounded hunt cycle; review candidate/coverage gaps with owners; report validated findings and invest in repeatable detections. Scope duration follows actual data readiness and access, not a guaranteed detection deadline.

Measure: required-domain coverage and freshness; completed versus inconclusive hunts; candidates reviewed; corroborated suspicious/incident cases; documented benign alternatives; collection-to-analysis delay; analyst effort; recurrence; and validated control/detection changes. Do not substitute raw alert count, IOC count or synthetic pass percentage for business outcomes.

Executive reporting should name the business decision, observed evidence, uncertainty, affected scope, owner and next investment. Use the executive brief template; report no confirmed incidents unless evidence supports that statement.
