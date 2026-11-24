# Telemetry coverage and identity normalization

The [matrix](../telemetry-matrix.csv) names likely source families and evidence gaps. A source listed here is not evidence that a customer's feed is enabled, licensed, retained or complete.

## Coverage contract

Record the covered time range, collector heartbeat, retention, filters/sampling, ingestion delay, clock uncertainty, tenant scope and required-field availability. Check delivery with independent known events and counters. Provider settings can disable data-plane logs even when control-plane audit exists. A heartbeat declares collector availability; it does not prove every required event type is captured.

The local engine requires a source-health record per required domain. Stale/missing/ambiguous records, incomplete windows, insufficient required baseline, bad typed values, conflicting event IDs, absent query fields and out-of-bounds timing yield `inconclusive_coverage` without executing that hunt. This conservative gating can suppress useful partial evidence; analysts can pursue separately scoped partial-data investigations while retaining the gap.

## Normalized schema

[event-schema.json](../schema/event-schema.json) is a simplified local model, **not OCSF conformance**. The version accepts timezone-aware event/ingest timestamps, tenant/source/domain/action identifiers, canonical principals, assets, selected runtime/delegated identities, workload IDs, typed evidence fields and optional authorization/change context.

Do not join on display name, email local-part or IP address alone. Preserve full provider subject identity and tenant/account/project namespace. The AWS job caller and runtime role are separate actors; Azure role assigner and grantee are separate; Google delegation evidence may identify an originating principal beyond the effective service account. Absent join evidence remains a coverage gap.

`approved=false`, `is_sensitive` and `out_of_scope` are reviewer-normalized/enriched facts. They are not universally supplied by provider logs. False means a known explicit decision, not a missing ticket. For AI, out-of-scope requires a deterministic policy observation with verified actor/document/tool context, not an LLM-generated accusation.

## Reference data handling

Deduplicate exact repeats by tenant, source, domain and original event ID. Reject conflicting records sharing that key. Preserve distinct same-ID records from different tenants. Emit evidence references bound to those scoped keys. Retain event and ingest time separately; exclude future events and flag records unavailable at the frozen assessment snapshot.

The synthetic lab uses a 24-hour baseline, two baseline records per domain, a five-minute heartbeat tolerance, 120-second ingest limit and 30-second maximum clock uncertainty. These are demonstration settings, **not production recommendations**. Temporal queries require a minimum separation equal to twice the maximum observed clock uncertainty. Source/coverage declarations are supplied inputs, not automated verification of a collector.
