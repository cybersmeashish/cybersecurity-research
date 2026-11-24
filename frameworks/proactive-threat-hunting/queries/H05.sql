SELECT e.tenant_id, e.principal_id AS entity_id, e.event_id AS evidence_ids FROM events e WHERE e.phase=1 AND e.domain='email' AND e.action='external_forward_created' AND e.approved=0;
