# Threat model and boundary — CAI-010

## Assets and trust roots

A cross-tenant cache hit; timing discrimination is a separately measured endpoint. is the protected effect. The lab's policy, trusted principal/tenant identity, authorized origin, and corrected gate are trusted. Fixture markers, user-selected targets, candidate plans, and derived records are synthetic and may be untrusted as declared by their case type.

## Attacker-controlled surface

The adversary can supply the fields represented by the named adversarial fixtures. They cannot change the guarded code, trusted policy, lab signing key, or expected labels. The public synthetic signing key is a test input, not a credential used by an external service.

## Security invariant

`CacheKey includes a trusted tenant partition so another tenant cannot select the same namespace by choosing a salt.`

The cache stores a deterministic CPU work result keyed by namespace and prefix. Global sharing exposes hits. Caller-provided salts avoid accidental sharing when distinct but allow chosen-salt collisions. A trusted tenant partition separates the state. The timing experiment calibrates a threshold on the caller's own known warm/cold prefixes and probes 64 different prefixes once per condition, with randomized order and another tenant's residency as ground truth.

## In-scope observations

The lab measures local authorization decisions and their actual local effects, with positive and negative controls. No protocol-wide or vendor-wide property is inferred.

## Exclusions and assumptions

There are no KV tensors, GPU, vLLM server, network jitter, batching, or model inference. Cold work is 1,200 SHA-256 iterations, so the timing separation is artificial. The corrected timing AUC remains an exploratory observation; zero cross-tenant hits does not prove all side channels absent.

The policy oracle is authored, relevant trusted identities are available to the gate, and missing authority fails closed in the corrected profile. The fixture environment does not include compromised operating-system trust roots or arbitrary execution inside the gate.

## Conditional impact and severity

A corresponding real implementation could expose the protected endpoint only if the same prerequisites hold. No CVSS score, CVE, bounty award, customer incident, or provider severity is assigned from this lab. Determine scope and impact from observed target behavior in a later authorized study.
