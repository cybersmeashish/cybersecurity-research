SELECT e.tenant_id, e.workload_id AS entity_id, e.event_id AS evidence_ids FROM events e WHERE e.phase=1 AND e.domain='kubernetes' AND e.action='pod_created' AND e.is_privileged=1 AND e.approved=0;
