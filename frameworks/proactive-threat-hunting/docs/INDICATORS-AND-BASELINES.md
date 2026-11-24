# Known indicators and first-observed behavior

## Indicator handling

An IOC needs a type, exact normalized value, provenance, validity interval, revocation state and investigation context. Use current permitted sources, document licensing/use restrictions, review confidence and collisions, and retire revoked/stale indicators. The local version matches only synthetic SHA-256 indicators. Matching requires that the IOC was valid at the event and remains valid at the analysis snapshot; revoked indicators never match.

The checked-in hashes are fake test values. They are not intelligence about real malicious files and must not be imported as a production threat feed. A match is a lead to verify file/process/session evidence, not confirmed compromise.

## Baseline handling

Build baselines from a sufficiently retained and representative pre-hunt window, with entity/tenant scope, change records and sensor continuity. Mark new sensors, unseen entities and seasonal maintenance explicitly. Use observed distributions for production thresholds rather than treating any first observation as malicious.

The reference queries examine first-observed process ancestry, devices, caller/runtime relationships, administration destinations, DNS destinations and SaaS applications. They also test known high-impact policy/change conditions. The lab's three-failure, three-new-domain and one-megabyte thresholds are arbitrary illustrative settings. They have not been calibrated to a real enterprise.

Do not call a behavior globally new because it is absent from a small local baseline. Rarity can identify a useful review target while a legitimate change explains it. A production novelty system needs held-out realistic data, drift review, adversarial tests, analyst feedback and measured workload/false-positive costs.

A baseline may already contain attacker activity or be poisoned by manipulated telemetry. Review known incident periods, source integrity and long-lived anomalous behavior; do not equate historical frequency with permission. Preserve raw evidence and use independent business/identity signals to challenge normalization.

With no active, attributable indicator registry at the assessment snapshot, the IOC procedure is inconclusive; a zero-match output cannot establish that indicator coverage exists.
