# Threat model and boundary — CAI-004

## Assets and trust roots

A successful local mapping to the synthetic cloud role. is the protected effect. The lab's policy, trusted principal/tenant identity, authorized origin, and corrected gate are trusted. Fixture markers, user-selected targets, candidate plans, and derived records are synthetic and may be untrusted as declared by their case type.

## Attacker-controlled surface

The adversary can supply the fields represented by the named adversarial fixtures. They cannot change the guarded code, trusted policy, lab signing key, or expected labels. The public synthetic signing key is a test input, not a credential used by an external service.

## Security invariant

`Map(claims, role) implies claims.issuer=I AND claims.audience=A AND claims.repository_id=R AND claims.owner_id=O.`

A name-only rule cannot distinguish a recreated identity from its predecessor. An owner restriction narrows the trust domain but still permits same-owner repository recreation. Name-based profiles also reject a legitimate rename, whereas stable identifiers preserve the intended identity through that rename. This exposes both excess trust and unnecessary denial in one policy model.

## In-scope observations

The lab measures local authorization decisions and their actual local effects, with positive and negative controls. No protocol-wide or vendor-wide property is inferred.

## Exclusions and assumptions

No GitHub repository was deleted or transferred, and no external OIDC issuer or cloud STS was invoked. Claim lifecycles and ownership transitions are supplied fixtures; actual issuer guarantees must be established separately.

The policy oracle is authored, relevant trusted identities are available to the gate, and missing authority fails closed in the corrected profile. The fixture environment does not include compromised operating-system trust roots or arbitrary execution inside the gate.

## Conditional impact and severity

A corresponding real implementation could expose the protected endpoint only if the same prerequisites hold. No CVSS score, CVE, bounty award, customer incident, or provider severity is assigned from this lab. Determine scope and impact from observed target behavior in a later authorized study.
