# Contribution protocol

Place research studies under `research/` and reusable operating frameworks under `frameworks/`. Keep each contribution self-contained, with a question/hypothesis, source register, assumptions, runnable instructions, data, positive/negative controls, evidence and limitations.

For hunts, define business scope, telemetry coverage, canonical identity/tenant joins, baseline/window boundaries, required fields, benign alternatives, investigation evidence and disposition. Treat a candidate as an investigative lead until corroborated. Missing telemetry must not become a clean bill of health. Include approved/benign operations so a rule is not "effective" merely because it flags every event.

Native SIEM queries and provider adapters must be labelled unvalidated until tested against the actual product version, enabled tables/connectors and representative data. Submit synthetic fixtures rather than client records or credentials. Report non-public issues via SECURITY.md. Use the canonical container workflow and disclose material AI assistance.
