# Executive research brief — CAI-007

## Decision supported by the study

Investigate whether a selected implementation enforces this boundary: **A schema-valid but unauthorized candidate action can change incident state unless an independent action policy rejects it.**

In the constructed local corpus, the seeded profile produced 18/18 forbidden effects and the guarded profile produced none. The corrected profile retained 12/12 legitimate effects. This supports a local control design; it is not a provider finding or a deployment risk estimate.

## Conditional business impact

If the same unchecked transition exists in a production system, the relevant impact is a committed disposition or alert action in the mock incident store. Scope depends on the actual trusted role, data sensitivity, and workflow contract.

## Practical next investment

Freeze a model/version, paired event corpus, and prompting policy; measure actual model-produced actions before replaying them through these gates.

## Confidence and constraints

Downstream action control supported; LLM log-to-action susceptibility not evaluated. No LLM ran and no attack-success rate for prompt injection was measured. Adversarial log wording and compromised plans are authored stimuli, not observed model outputs. This experiment validates downstream action control conditional on a bad plan; it does not establish the log-to-model causal step. Independent review and production validation remain pending.
