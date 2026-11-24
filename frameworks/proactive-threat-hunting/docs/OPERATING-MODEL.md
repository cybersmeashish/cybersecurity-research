# Conducting a proactive hunt

1. **Define the business question.** Identify critical assets, allowed actors/actions, exposure and the behavior under examination. Write the hypothesis and alternative explanations before selecting a query. Use the hunt charter.
2. **Agree scope and owners.** Record tenant/account/project/namespace, systems, analysis window, permitted telemetry access, data owner, hunt lead and incident decision owner. Queries and collection are separate responsibilities.
3. **Establish observability.** Verify collector/source coverage, schema version, required event fields, heartbeat, ingestion delay, identity joins and clock uncertainty. Record actual retention and disabled/unavailable feeds. Missing evidence can make the hunt inconclusive.
4. **Freeze the baseline and snapshot.** Use a time-bounded baseline that ends before the hunt window. Document onboarding/retention gaps, expected seasonality, approved changes and entity populations. Never let future events or post-snapshot ingestion train the baseline.
5. **Execute the procedure.** Preserve query version, parameters, exact data window and source record references. Use bounded joins on canonical identity plus tenant and object/workload context; timestamp proximity alone is not proof of causation.
6. **Corroborate candidates.** Retrieve minimal necessary raw evidence, verify identity/delegation, effective authorization and business entitlement, compare asset/owner/change records and investigate follow-on behavior. A novelty score or indicator match is a starting point.
7. **Disposition and escalate.** Record supported suspicious behavior, benign explanation, unresolved evidence or confirmed incident using the organization's criteria. Escalate confirmed or urgent material through the established incident owner; the framework does not perform automated containment.
8. **Improve and repeat.** Convert validated patterns into tested detections/control changes, add missed/benign fixtures, close telemetry gaps, measure time/coverage and schedule a targeted follow-up. Retain decisions, limitations and owner acceptance.

Required artifacts: charter, telemetry coverage record, baseline definition, versioned procedure/query, candidate evidence references, case disposition and executive summary. These support traceability; they do not establish forensic admissibility or compliance by themselves.
