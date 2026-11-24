# Threat model and boundary — CAI-009

## Assets and trust roots

A value actually read from the tenant record in SQLite storage. is the protected effect. The lab's policy, trusted principal/tenant identity, authorized origin, and corrected gate are trusted. Fixture markers, user-selected targets, candidate plans, and derived records are synthetic and may be untrusted as declared by their case type.

## Attacker-controlled surface

The adversary can supply the fields represented by the named adversarial fixtures. They cannot change the guarded code, trusted policy, lab signing key, or expected labels. The public synthetic signing key is a test input, not a credential used by an external service.

## Security invariant

`Read(event, tenant) implies ValidEnvelope(event) AND tenant=AuthenticatedTenant(event) AND RequestedTenant=AuthenticatedTenant(event).`

Ingress signs an envelope that separates the authenticated tenant from the user-supplied target tenant. The queue consumer has broad storage capability. Signature and freshness checks reject corrupt or expired envelopes yet still allow cross-tenant payload access. A retry repeats the same mistake. Binding the requested target to the authenticated envelope tenant prevents the read.

## In-scope observations

The lab measures local authorization decisions and their actual local effects, with positive and negative controls. No protocol-wide or vendor-wide property is inferred.

## Exclusions and assumptions

The queue is a local Python Queue; there is no cloud event service, distributed delivery, producer IAM assessment, replay-attack prevention, or exactly-once claim. Cryptographic fixtures are not a production messaging format.

The policy oracle is authored, relevant trusted identities are available to the gate, and missing authority fails closed in the corrected profile. The fixture environment does not include compromised operating-system trust roots or arbitrary execution inside the gate.

## Conditional impact and severity

A corresponding real implementation could expose the protected endpoint only if the same prerequisites hold. No CVSS score, CVE, bounty award, customer incident, or provider severity is assigned from this lab. Determine scope and impact from observed target behavior in a later authorized study.
