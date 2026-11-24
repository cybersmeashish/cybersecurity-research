# Threat model and boundary — CAI-008

## Assets and trust roots

A later-session mock write action derived from a recalled record. is the protected effect. The lab's policy, trusted principal/tenant identity, authorized origin, and corrected gate are trusted. Fixture markers, user-selected targets, candidate plans, and derived records are synthetic and may be untrusted as declared by their case type.

## Attacker-controlled surface

The adversary can supply the fields represented by the named adversarial fixtures. They cannot change the guarded code, trusted policy, lab signing key, or expected labels. The public synthetic signing key is a test input, not a credential used by an external service.

## Security invariant

`Authority(derived memory) cannot exceed the authority of its verified origin; missing or broken lineage grants no authority.`

The memory store retains structured source and summary records. A deliberately permissive consumer defaults a missing trust label to trusted. Partial compaction preserves a first-stage label but loses it in a second compaction or accepts an unbound claimed label. A later session recalls the stored record without the original text. The guarded path traverses parents to an authorized operator-origin source and rejects missing roots.

## In-scope observations

The lab measures local authorization decisions and their actual local effects, with positive and negative controls. No protocol-wide or vendor-wide property is inferred.

## Exclusions and assumptions

Compaction copies structured fields; it is not natural-language summarization. No LLM, embedding retriever, semantic trigger optimization, long-running deployment, or real user memory was tested. The result concerns provenance mechanics, not model-level memory-poisoning susceptibility.

The policy oracle is authored, relevant trusted identities are available to the gate, and missing authority fails closed in the corrected profile. The fixture environment does not include compromised operating-system trust roots or arbitrary execution inside the gate.

## Conditional impact and severity

A corresponding real implementation could expose the protected endpoint only if the same prerequisites hold. No CVSS score, CVE, bounty award, customer incident, or provider severity is assigned from this lab. Determine scope and impact from observed target behavior in a later authorized study.
