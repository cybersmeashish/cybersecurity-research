# Method and evidence semantics

## Research questions

RQ1: Which individually acceptable-looking permissions compose into an unauthorized AI workload outcome?
RQ2: Which single controls interrupt the stated paths, and where does sensitive access remain after disclosure is blocked?
RQ3: How should a reviewer represent missing identity/network evidence without treating it as a failure or an approval?

## Unit of analysis

A chain has primitive facts, three ordered rules and an unauthorized target. A rule requires every listed fact or earlier derived node. All sources must be reviewer-normalized: effective data authorization includes relevant resource policy, explicit denies, organization controls and runtime-specific constraints. The engine does not compute those decisions.

`true` means the necessary precondition is deliberately present in the synthetic fixture. `false` means it is deliberately absent. `null` or an omitted primitive fact means evidence is missing. A rule is reachable only when all its inputs are true; any false input blocks it; otherwise it is unknown. Derived nodes cannot be supplied as input, and malformed/cyclic rule sets are rejected.

A control-removal fixture sets one necessary fact false. A missing-evidence fixture sets it null. Every primitive condition is individually removed and individually made unknown. A legitimate-delegation fixture removes the business-policy violation. A mixed-denial fixture shows that a known absent necessary condition can block this specific path even while other evidence is missing.

## Two separate experiments

**Graph experiment:** evaluate the published eight-chain fixture set. Expected labels express the model's stated contract. Preserve every decision trace and primitive fact identifier. Do not interpret pass counts as a provider detection benchmark.

**Local runtime experiment:** deny tenant-A direct access to a synthetic tenant-B record; admit a job running under a broader mock identity; observe whether a result is returned. Compare actor binding, runtime scope, disclosure restriction, effective data denial and artifact digest binding. The same backend is labelled with four profiles solely to explain the comparison.

## Reproducibility and controls

Pin the container image by digest; run with network disabled, read-only root/workspace, an unprivileged user and a temporary result directory. Record Python, architecture, timestamp, actual test methods and a SHA-256 manifest of source inputs. Use the checked-in runner to regenerate results. Compare graph/runtime results deterministically; summary timestamps legitimately differ.

## Interpretation rules

- `reachable` is a synthetic witness, not a confirmed cloud compromise.
- `blocked` applies only to the stated target/path and current model.
- `unknown` calls for additional evidence, not a severity score.
- A documentation statement is not an observed lab result.
- A proposed taxonomy name is not proof of novel vulnerability discovery.
