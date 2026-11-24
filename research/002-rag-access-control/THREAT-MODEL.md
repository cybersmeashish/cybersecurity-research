# Threat model and boundary — CAI-002

## Assets and trust roots

Delivery of the unique protected marker in a returned answer. is the protected effect. The lab's policy, trusted principal/tenant identity, authorized origin, and corrected gate are trusted. Fixture markers, user-selected targets, candidate plans, and derived records are synthetic and may be untrusted as declared by their case type.

## Attacker-controlled surface

The adversary can supply the fields represented by the named adversarial fixtures. They cannot change the guarded code, trusted policy, lab signing key, or expected labels. The public synthetic signing key is a test input, not a credential used by an external service.

## Security invariant

`Serve(u, artifact, t) implies Allow(u, d, t) for every protected source d in Lineage(artifact).`

The source query checks an ACL table, but the cache or summary path can return an already materialized marker without consulting that table. Cache-key scoping stops reuse by a different principal while leaving same-principal revocation and unscoped summaries exposed. The guarded path reevaluates the current source ACL before delivering an artifact.

## In-scope observations

The lab measures local authorization decisions and their actual local effects, with positive and negative controls. No protocol-wide or vendor-wide property is inferred.

## Exclusions and assumptions

No vector database, Azure search service, model-generated summary, asynchronous index propagation, conversation erasure, or customer corpus was tested. Revocation is an immediate SQLite transaction, so no claim about a provider synchronization deadline is supported.

The policy oracle is authored, relevant trusted identities are available to the gate, and missing authority fails closed in the corrected profile. The fixture environment does not include compromised operating-system trust roots or arbitrary execution inside the gate.

## Conditional impact and severity

A corresponding real implementation could expose the protected endpoint only if the same prerequisites hold. No CVSS score, CVE, bounty award, customer incident, or provider severity is assigned from this lab. Determine scope and impact from observed target behavior in a later authorized study.
