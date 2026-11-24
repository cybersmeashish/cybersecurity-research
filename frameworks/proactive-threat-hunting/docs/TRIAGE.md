# Candidate triage and disposition

For each candidate, preserve query/version/window, scoped source record identifiers and coverage quality. Verify the actual principal/session, object/workload, requested operation, effective scope and approved business purpose. Collect enough raw telemetry to resolve the hypothesis while minimizing unnecessary personal/content data.

| State | Evidence required | Next step |
|---|---|---|
| Candidate lead | Query association or indicator match | Corroborate raw source and context |
| Benign explained | Evidence supports an approved or expected alternative | Record explanation, improve baseline/tuning without hiding future risk |
| Suspicious supported | Multiple corroborating observations support unauthorized or abnormal behavior | Escalate to the incident owner under the existing process |
| Confirmed incident | Organization's incident criteria met by evidence | Preserve evidence and follow incident response authority |
| Inconclusive | Required field, coverage, identity, timing or approval evidence absent | Name owner, missing evidence and follow-up; do not mark clean |

Temporal association is not proof of causal linkage. ATT&CK context is not actor attribution. A blocked final outcome may still leave unauthorized internal access. Document alternative explanations and uncertainties alongside the lead.

A case closure needs reviewer, date, evidence references, rationale and remaining limitations. A hunt with no leads says only that the configured procedures found none in sufficiently observed data/window. It cannot rule out compromise or unmodeled behavior.
