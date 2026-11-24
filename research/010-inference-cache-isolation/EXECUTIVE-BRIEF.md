# Executive research brief — CAI-010

## Decision supported by the study

Investigate whether a selected implementation enforces this boundary: **A cache namespace derived only from a caller-controlled salt can share prefix state across tenants; a trusted tenant namespace prevents cross-tenant cache hits in this fixture model.**

In the constructed local corpus, the seeded profile produced 18/18 forbidden effects and the guarded profile produced none. The corrected profile retained 6/6 legitimate effects. This supports a local control design; it is not a provider finding or a deployment risk estimate.

## Conditional business impact

If the same unchecked transition exists in a production system, the relevant impact is a cross-tenant cache hit; timing discrimination is a separately measured endpoint. Scope depends on the actual trusted role, data sensitivity, and workflow contract.

## Practical next investment

Use a scoped inference deployment with real scheduling/noise, trusted gateway identities, fresh held-out prefixes, and a pre-registered sample-size calculation.

## Confidence and constraints

Synthetic namespace and timing mechanism supported; production LLM-serving leakage not evaluated. There are no KV tensors, GPU, vLLM server, network jitter, batching, or model inference. Cold work is 1,200 SHA-256 iterations, so the timing separation is artificial. The corrected timing AUC remains an exploratory observation; zero cross-tenant hits does not prove all side channels absent. Independent review and production validation remain pending.
