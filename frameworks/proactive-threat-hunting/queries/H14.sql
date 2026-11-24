SELECT e.tenant_id, e.principal_id AS entity_id, e.event_id AS evidence_ids FROM events e WHERE e.phase=1 AND e.domain='ai' AND e.action IN ('retrieval','tool_action') AND e.out_of_scope=1;
