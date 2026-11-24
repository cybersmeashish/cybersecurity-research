# Limitations and unsupported conclusions — CAI-004

## Implementation fidelity

No GitHub repository was deleted or transferred, and no external OIDC issuer or cloud STS was invoked. Claim lifecycles and ownership transitions are supplied fixtures; actual issuer guarantees must be established separately.

## Dataset and observer bias

The author designed the vulnerable profiles, corrected profiles, and fixture oracle. The corpus is purposive and small. Six synthetic contexts are identifier variations, not independent organizations. Neither independent reproduction nor peer review has occurred. A deliberately seeded flaw verifies observability, not discovery capability.

## Measurement boundaries

The fixture counts are descriptive. They do not estimate real-world attack frequency, vulnerability prevalence, scanner precision/recall, or production reliability. Regression replays are not extra independent experiments. The original broad hypothesis is evaluated only to the extent stated in the local proposition. Model susceptibility, provider behavior, and monetary impact are not inferred from deterministic surrogates.

## Reproduction variability

Source and fixture hashes and expected outcome rows should match. Timestamps, ephemeral HTTP ports, CPU timing, runtime scheduling, and bootstrap summaries can vary. Timing results require repeated independent runs and realistic noise before stronger claims.

## Publication and novelty

Primary-source retrieval verifies reference identity, not exhaustive related-work coverage. No new vulnerability class, CVE, bounty, operational incident, or globally novel result is claimed. Literature and implementation surveys remain pending.

## Next evidence needed

Select one issuer/cloud pairing, document its immutable claim guarantees, and validate allowed lifecycle events in owned repositories.
