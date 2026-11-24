# Limits of version 0.1

- This is a proactive-hunting framework and a normalized local reference implementation. It performs no collection, cloud/API calls, endpoint actions, customer investigation or automated response.
- All fixtures, indicators, identities, source-health declarations and authorization tags are synthetic. Matching intended fixture outputs is consistency/regression evidence, not detection precision/recall, real-world false-positive rates or coverage of previously unseen attackers.
- No native KQL/SPL/other SIEM syntax, live connector, real IAM policy, EDR product or customer logging configuration was validated.
- Baseline and ingest/heartbeat/clock thresholds are illustrative. Two domain records do not constitute a representative enterprise baseline. First-observed means absent from the provided pre-hunt sample.
- Source-health declarations are trusted inputs. Their credibility must be established with actual collector configuration, known test events and counters. Gating conservatively stops hunts with missing evidence and can miss useful partial-data leads.
- Canonical identity, runtime/delegator joins, sensitivity, scope and approval fields need validated mappings/enrichment. Incorrect enrichment can create both false leads and blind spots. The engine cannot infer effective provider authorization.
- Timestamp proximity and ATT&CK context do not establish causality or attribution. The queries cover bounded example hypotheses; attackers and valid operations may take different paths.
- The IOC model supports synthetic hashes only. The implementation is not an intelligence-feed client, forensic evidence signing system or operational threat-intelligence platform.

Production adoption requires authorized scope, actual platform/schema validation, calibrated representative baselines, independent review and operational evidence. No compliance or clear-of-compromise conclusion follows from this reference lab.
