# Shared hypothesis validation and evidence protocol

Applies to the ten proposals in [the research portfolio](CLOUD-AI-SECURITY-HYPOTHESES.md). The controlled local phase is now recorded in each package; this protocol also governs future implementation validation.

## Define a bounded claim

Select an implementation, version, configuration, and explicit security policy. Record attacker control, prerequisites, exclusions, and expected legitimate behavior. Survey primary prior work and vendor guidance before claiming novelty.

## Run controlled local experiments

Use the repository's OrbStack container and persistent volume. Use synthetic identities, mock effects, and fake markers. Include authorized positive, forbidden negative, intentionally flawed, corrected, and missing-context cases as appropriate. No live attacks, provider provisioning, or customer data are authorized by these proposals.

Enumerate deterministic fixtures. For stochastic models, pair inputs, repeat trials on independent cases, record seeds, and pre-register sample size and decision rules. Timing experiments require held-out prefixes and controls for clustered measurements, workload, and noise.

## Establish an actual effect

Model prose and tool selection alone do not prove unauthorized execution. Record served protected data, executed mock actions, contacted canaries, or charged work. Verify denials, propagation windows, policy intent, and provenance. Measure legitimate-workflow utility and false positives as well as attack success.

## Preserve bounded evidence

Trial fields: research/case IDs, target version, configuration/fixture hashes, seed, initiating principal, expected/observed decision, actual effect, control, sanitized trace, and timestamp. Publish synthetic fixtures and redacted evidence; exclude real secrets and customer records.

Label results as static possibilities, synthetic observations, authorized implementation observations, or independently reproduced findings. Record negative and failed trials. Local assumptions do not establish provider defaults.

## Scope later implementation validation

Obtain explicit ownership or program authorization for named targets and test methods. Define rate, cost, and stop limits. Document resource ownership. Coordinate disclosure of confirmed issues before publishing sensitive exploit details.

## Verify publication

Run final checks with source mounted read-only in a separate container. Hash reviewed files and compare before publication. Preserve unrelated remote content, reject a moving main branch, and verify published bytes. Documentation verification is not an experiment or tool implementation.

## Executed local phase

Each package records its evaluated local proposition, fixture matrix, three profiles, effect traces, source hashes, runtime isolation, and claim exclusions. External model/provider validation remains pending; local measurements must not be relabeled as those results.
