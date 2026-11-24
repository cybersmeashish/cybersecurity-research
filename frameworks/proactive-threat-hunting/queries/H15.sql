SELECT e.tenant_id, e.principal_id AS entity_id, e.event_id AS evidence_ids FROM events e WHERE e.phase=1 AND e.domain='cicd' AND e.action='artifact_consumed' AND e.digest<>e.approved_digest;
