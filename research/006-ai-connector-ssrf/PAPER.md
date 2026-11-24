# CAI-006: Destination validation across AI connector fetch chains

## Actual loopback HTTP redirects with a controlled resolution adapter

Ashish Srivastava · Version 0.2 · 2026-11-24 · Controlled local research report; independent review pending.

## Abstract

This study examines a specific authorization boundary using a small, executable local system. The tested proposition is: Initial destination approval does not constrain later HTTP connections unless every redirect and the actual connected address remain inside the allowlist. Three implementations are compared against the same 36 authored fixtures: a seeded permissive profile, a partial control, and a guarded profile. Across 108 condition trials, the permissive profile produced 12 forbidden effects in 12 adversarial cases; the partial profile retained 6. The guarded profile blocked all authored forbidden effects while preserving 12/12 legitimate effects. Six behavioral regression methods also passed. The evidence is a controlled mechanism demonstration, not a population benchmark. Both endpoints are loopback fixtures; public DNS rebinding, IPv6, HTTPS certificate binding, proxies, metadata credential extraction, and a production connector were not tested. Resolution changes are adapter-controlled. The harness forbids destinations outside its two loopback addresses and port.

## 1. Problem and motivation

Security checks often exist at one point in a workflow while the protected effect occurs later or under a different authority. The relevant question is whether the declared policy remains binding at that later effect. Checking a representation or accepting a prior decision does not automatically preserve authorization across transformations, reuse, handoffs, or execution. This report investigates that distinction with explicit inputs, expected policy labels, and observable effects rather than relying on descriptive model output.

Primary guidance and prior research establish the background risk; they do not validate this local implementation. See [the annotated related-work review](RELATED-WORK.md) and [source register](SOURCES.md). The study contribution is a self-contained fixture corpus, executable control comparison, and traceable evidence for the bounded proposition. It is not a claim that the underlying attack class is new.

## 2. Research questions and hypotheses

**Original portfolio hypothesis:** A connector validating only an initial URL or DNS answer can contact a forbidden internal destination after a redirect or changed resolution alters the actual connection target.

**Evaluated local proposition:** Initial destination approval does not constrain later HTTP connections unless every redirect and the actual connected address remain inside the allowlist.

**Original null:** Each connection and redirect hop remains within the declared destination policy.

**Operational local null:** the seeded implementation does not cross the declared boundary on any authored forbidden case, or the guarded control cannot preserve both boundary enforcement and positive-case behavior. This is a deterministic corpus check, not a statistical population null. For the cache timing extension, membership discrimination is evaluated separately and descriptively.

**Hypothesis status:** Constructed local mechanism supported; implementation-level and population claims not established. A successful constructed failure establishes that the mechanism is possible in the code provided, not that an unexamined product is affected.

## 3. System and threat model

The protected endpoint is **An actual request recorded by the internal loopback HTTP canary.**. Inputs and expected labels are recorded in [the fixture corpus](lab/fixtures.json). The attacker controls only the fields defined by each fixture; the trusted policy and corrected gate are outside attacker control. No real credential, customer data, cloud account, or production service appears in the lab.

```mermaid
flowchart LR
    A["User-selected URL"] --> B["Redirect or resolver transition"]
    B --> C["Per-connection destination gate"]
    C --> D["Loopback internal canary"]
```

**Formal boundary:** `Every connection uses a canonical destination approved for that hop; a validated address is pinned to the connection.`

The formula expresses the experiment's declared policy. Its assumptions and scope are documented in [the threat model](THREAT-MODEL.md); it is not a proof about all implementations of a protocol.

## 4. Mechanism and experimental conditions

Two real HTTP servers occupy distinct loopback addresses at one port. A public fixture redirects to the internal canary. A controlled resolver separately returns a permitted address at validation and an internal address at connection time. Checking each advertised hostname stops the explicit redirect but misses the address transition. The guarded transport pins the initially checked address and validates later resolved destinations before connecting.

- **vulnerable:** Only the initial resolved destination is approved.
- **partial:** Each advertised redirect hostname is checked, but connection resolution can differ.
- **guarded:** Checked address pinned to the connection; every redirect destination validated.

The partial profile is included to distinguish a narrow control from enforcement at the complete effect boundary. Where the partial profile has the same failure counts as the permissive profile, the experiment does not imply a statistical difference; it shows that the particular added metadata or check did not resolve the authored mismatch.

## 5. Method

The corpus contains six named scenario types in six synthetic identity contexts. Case IDs and policy labels are specified independently of the returned observation. Every fixture runs once in each condition, yielding 108 corpus trials. Reexecutions performed by the regression methods are control checks and are not counted as independent research samples.

The runner observes an actual local effect, records decision steps, exports CSV rows and JSON traces, and hashes the source inputs. Six regression methods cover legitimate effects, adversarial effects, negative controls, the seeded failure, trace presence, and fixture completeness. These tests are behavioral assertions about the declared boundary; they do not certify a production implementation.

Execution used a pinned Python 3.12.16 image on Linux/aarch64, UID 1000, a read-only root and source volume, bounded CPU/memory, dropped capabilities, no-new-privileges, and disabled external networking. Temporary results were written outside source. The SSRF lab uses actual loopback HTTP, which remains available inside the isolated container. No external attack ran. Source hashes are in [the tested-input manifest](evidence/source-manifest.json).

The design is exploratory and was not externally preregistered. Fixture proportions deliberately favor boundary coverage. Repeated nominal contexts do not establish deployment frequency or independent prevalence observations. See [methods](METHOD.md) for variable definitions and controls.

## 6. Results

| Condition | Forbidden effects / adversarial cases | Legitimate effects / positive cases | Negative-control failures | Policy matches / all cases |
|---|---|---|---|---|
| vulnerable | 12/12 | 12/12 | 0/12 | 24/36 |
| partial | 6/12 | 12/12 | 0/12 | 30/36 |
| guarded | 0/12 | 12/12 | 0/12 | 36/36 |

Counts are literal observations in this authored corpus. A forbidden effect is defined by the endpoint and fixture policy, not by a narrative claim or by the presence of an attack-like string. The guarded profile matched 36/36 expected policy labels; zero observed corpus failures is not a universal robustness guarantee.

[CSV observations](evidence/results.csv), [effect traces](evidence/traces.json), [summary](evidence/summary.json), and [regression output](evidence/tests.txt) permit row-level inspection. [The claim register](CLAIM-EVIDENCE.md) separates direct evidence from interpretation and pending hypotheses.

## 7. Discussion and engineering implications

The practical implication is conditional: if an implementation has the same unchecked transition and the same authority assumptions, enforcement at the final boundary is a candidate remedy. The local comparison makes that transition inspectable. It does not justify labeling an existing service vulnerable without verifying its actual preconditions and effects.

The guarded profile's retained positive cases show that a complete denial of all operations was not needed for this corpus. They do not demonstrate broad usability, latency, or throughput. The observed results should motivate an implementation-specific investigation with broader legitimate workflows, versioned policies, and missing-context handling. The original proposed production tool remains a design; the runnable artifact is a local prototype and test harness.

## 8. Validity and limitations

Both endpoints are loopback fixtures; public DNS rebinding, IPv6, HTTPS certificate binding, proxies, metadata credential extraction, and a production connector were not tested. Resolution changes are adapter-controlled. The harness forbids destinations outside its two loopback addresses and port.

Additional limitations are shared across studies: the author defined both mechanisms and fixtures; no independent reproduction or blind holdout implementation was assessed; six contexts are nominal variations, not randomly sampled organizations; the workload intentionally contains known flawed configurations; and source retrieval is not an exhaustive literature search. [LIMITATIONS.md](LIMITATIONS.md) identifies which conclusions remain unsupported.

## 9. Conclusion and next validation

The executed local system provides bounded evidence for the stated mechanism and a corrected boundary under its declared policy. It neither establishes global novelty nor confirms a provider defect. Extend the owned test harness to IPv6, HTTPS redirects, proxy behavior, and a selected connector, with synthetic metadata responses only. The next phase must follow [the validation protocol](VALIDATION-PROTOCOL.md) and retain failed and negative results.

## References and reproducibility

[Annotated primary sources](SOURCES.md) · [Related work](RELATED-WORK.md) · [Reproduction instructions](REPRODUCIBILITY.md) · [Preparation provenance](PROVENANCE.md) · [Citation metadata](CITATION.cff).
