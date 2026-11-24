# Measured results — AIA-001 version 0.1

Measured in an isolated, read-only OrbStack container on 24 November 2026. The [summary](../../evidence/summary.json) records the exact UTC timestamp, runtime, source manifest and network-isolation result.

## Synthetic graph experiment

| Measure | Observed result |
|---|---:|
| Candidate organizing categories | 5 |
| Explicit-precondition attack-chain models | 8 |
| Synthetic fixture cases | 144 |
| Reachable stated targets | 8 |
| Blocked stated targets | 76 |
| Unknown because evidence is missing | 60 |
| Fixture expectations matched | 144 / 144 |
| Security-boundary regression test methods | 13 |

| Fixture family | Cases | Interpretation |
|---|---:|---|
| Full-path baseline | 8 | All necessary synthetic preconditions hold |
| Single proposed control | 8 | One necessary precondition deliberately absent |
| Control enforcement unknown | 8 | Missing control observation keeps outcome unknown |
| Legitimate delegation | 8 | No business-entitlement violation for the stated target |
| Each-condition ablation | 52 | Each necessary primitive precondition is individually removed |
| Each-condition missing evidence | 52 | Each necessary primitive fact is individually unknown |
| Known denial with another unknown | 8 | Known absent prerequisite blocks this specific path |

Fixture matching is a consistency/regression result, not a measurement of vulnerability prevalence or real-world detection accuracy. No real IAM export was evaluated.

## Local runtime experiment

The experiment has **six unique policy conditions**. The same mock backend is run with four explanatory profile labels, giving 24 cases. These are not independent implementations of four providers.

| Condition | Cases | Synthetic tenant-B output returned to tenant-A |
|---|---:|---:|
| Broad delegated baseline | 4 | 4 |
| Actor-entitlement binding | 4 | 0 |
| Scoped runtime data authority | 4 | 0 |
| Disclosure-boundary restriction | 4 | 0 |
| Effective runtime data denial | 4 | 0 |
| Admitted artifact digest binding | 4 | 0 |

Direct tenant-A access to the tenant-B record was denied in every case. All five control conditions interrupted the final output in this local program. The disclosure-boundary condition still recorded a permitted internal read before rejecting the output. Therefore preventing final disclosure does not establish authorized internal access. A separate regression test preserved a legitimate same-tenant job with actor and artifact binding enabled.

## Research findings within this scope

**F1 — Caller restriction is not a sufficient model condition for runtime restriction.** The local delegated path returned an out-of-scope synthetic record despite denied direct caller access. The relevant review unit includes caller, controllable workload, selected identity and business entitlement.

**F2 — Controls at different boundaries can produce the same final outcome with different internal consequences.** Actor and runtime controls interrupt earlier stages; output restriction can leave the read intact. Review stage-specific traces rather than only a final success/deny counter.

**F3 — Missing evidence must remain distinguishable from denied access.** The 60 unknown cases retain an undecided target. Known absent conditions can still block a specific path without resolving all other unknowns.

**F4 — Network entry-point annotations do not prove outbound control.** Toggling the graph's private-ingress annotation did not change an otherwise allowed egress path. This demonstrates the model's evidence contract, not Kubernetes CNI behavior.

Provider vulnerabilities confirmed: **0**. Live provider experiments: **0**. Global novelty of the candidate category names: **not established**. All scope limits are in [LIMITATIONS.md](LIMITATIONS.md).
