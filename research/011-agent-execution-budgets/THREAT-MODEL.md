# Threat model and boundary — CAI-011

## Assets and trust roots

Total charged normalized units exceeding the declared task budget; legitimate graph completion is reported separately. is the protected effect. The lab's policy, trusted principal/tenant identity, authorized origin, and corrected gate are trusted. Fixture markers, user-selected targets, candidate plans, and derived records are synthetic and may be untrusted as declared by their case type.

## Attacker-controlled surface

The adversary can supply the fields represented by the named adversarial fixtures. They cannot change the guarded code, trusted policy, lab signing key, or expected labels. The public synthetic signing key is a test input, not a credential used by an external service.

## Security invariant

`Sum of admitted task-linked cost units is at most the task budget when reservation is atomic and every child is attributed to the task.`

Each admitted node performs real local hashing work with a declared cost. Call caps are enforced in every profile. Independent calls can all pass while their sum exceeds the task budget. Retaining a parent ID alone does not enforce a cap. The guarded scheduler locks budget reservation before executing sequential or concurrent work.

## In-scope observations

The lab measures local authorization decisions and their actual local effects, with positive and negative controls. No protocol-wide or vendor-wide property is inferred.

## Exclusions and assumptions

Units are declared synthetic costs, not dollars, tokens, cloud billing, or actual reasoning effort. Node costs are known before admission. There is no live autonomous planner, probabilistic usage estimator, mid-flight cancellation, or distributed ledger race.

The policy oracle is authored, relevant trusted identities are available to the gate, and missing authority fails closed in the corrected profile. The fixture environment does not include compromised operating-system trust roots or arbitrary execution inside the gate.

## Conditional impact and severity

A corresponding real implementation could expose the protected endpoint only if the same prerequisites hold. No CVSS score, CVE, bounty award, customer incident, or provider severity is assigned from this lab. Determine scope and impact from observed target behavior in a later authorized study.
