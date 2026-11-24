# AIA-001: Who authorizes the runtime?

## A comparative study of authority bindings in cloud and AI infrastructure

**Publisher:** Ashish Srivastava · **Version:** 0.1 · **Date:** 24 November 2026  
**Preparation:** AI-assisted synthesis and implementation; executable results and limitations are published. Independent review pending.

### Abstract

Cloud-hosted AI systems combine human requesters, workload identities, mutable artifacts, data services, retrieval components and tool actions. Reviewing their permissions separately can leave the intended caller-to-action boundary unexplained. This study proposes five organizing categories for authority-binding failures, compares documented identity behavior across AWS, Azure, Google Cloud and Kubernetes, and publishes eight synthetic attack-chain models. Every primitive precondition is removed and made unknown in counterfactual cases. A separate local ACL experiment demonstrates a denied caller obtaining an out-of-scope record via a broadly authorized workload, and compares controls at admission, identity, output, data authorization and artifact consumption. Results establish behavior of the published reference model and mock backend. They do not establish novel provider flaws, real-world prevalence, prompt-injection efficacy or production control effectiveness.

### 1. Problem and original contribution

The central question is: **which actor is authorized for the actual operation performed under the effective runtime identity?** Runtime permission, caller permission and business entitlement are separate inputs. Delegation can be intentional and safe; a violated business boundary must be shown before naming a failure.

The original artifacts are a common evidence vocabulary, explicit AND-precondition graphs, a reusable dataset of counterfactuals, a tri-state implementation and executable local traces. The underlying risk mechanisms have prior art. [Novelty assessment](NOVELTY.md) records the bounded review and remaining uncertainty.

### 2. Sources and comparison

The primary-source register distinguishes each document's supported claim from an inference or untested assumption. Documentation was reviewed on 24 November 2026; exact versions and effective deployed controls require separate observation.

- AWS training selects an execution role; passing it requires appropriate caller permission. Check service trust, effective role scope and workload/output control independently. [AWS-IAM, AWS-TRAIN](SOURCES.md)
- Azure ML supports multiple data-authentication paths. Intentional compute-identity delegation should be evaluated against the organization's workload boundary. [AZ-IDENTITY](SOURCES.md)
- Vertex AI custom service-account attachment requires actAs; training, prediction and batch modes must be distinguished. [GCP-IDENTITY](SOURCES.md)
- Kubernetes workload creation, token availability, service-account privilege and network enforcement are separate questions. [K8S-SA, K8S-RBAC, K8S-NET](SOURCES.md)

No provider-specific control is asserted equivalent to another merely because the local graphs have similar shapes. See the provider worksheets for evidence required to replace synthetic assumptions.

### 3. Proposed taxonomy

| Candidate | Hypothesis under test | Required distinction |
|---|---|---|
| AB-01: delegated runtime authority drift | Controlled workload executes with an authority inconsistent with the caller's permitted business outcome. | Intended delegation versus an unauthorized outcome |
| AB-02: artifact-to-runtime authority drift | A changed consumed artifact inherits an approved runtime identity. | Artifact name/reference versus the actual admitted content |
| AB-03: retrieval authorization detachment | Retrieval uses shared authority without preserving document entitlement. | Retriever access versus caller access |
| AB-04: ingress-to-egress assurance substitution | Private ingress is incorrectly treated as outbound assurance. | Declared entry point versus observed disclosure route |
| AB-05: agent action authority detachment | Tool permission substitutes for requester authorization. | Tool capability versus actor entitlement |

These category names are proposed here as an organizing taxonomy. Global novelty of the classes is not established. [Class register](candidate-classes.csv)

### 4. Method

Each path is an acyclic graph of three rules. Each rule is an AND over its prerequisites. Primitive values are true, false or unknown. A known absent necessary condition blocks the path; absent evidence cannot confirm one. The engine rejects invalid dependencies, truthy non-booleans and attempts to supply derived authority nodes.

The dataset includes full-path baselines, one proposed control per chain, legitimate-delegation cases, each-condition ablation, each-condition missing evidence and known denial with another unknown. [Method](METHOD.md), [chains](chains.json), [fixtures](fixtures.json)

The separate runtime experiment uses deterministic tenant records, a job-entry path and a broad local runtime identity. Four profile labels share one backend. Controls bind actor entitlement, runtime scope, permitted output, effective read access or artifact digest. [Implementation](../../src/local_runtime.py)

### 5. Results

The measured results are generated by the checked-in runner and published as [the results report](RESULTS.md), [CSV](../../evidence/results.csv), [graph traces](../../evidence/graph-results.json) and [runtime audit traces](../../evidence/runtime-results.json). These are local synthetic observations, not account assessments.

One crucial distinction is between preventing a read and preventing its return: the disclosure-boundary control can stop the output after the mock runtime has already read the record. The control's successful final-target result therefore does not prove that internal data access was authorized. The legitimate-workload test checks that actor/digest controls can still admit a permitted same-tenant operation.

### 6. Implications for reviews and detection

Review each requester-to-runtime edge along with effective data permission, consumed artifact, business entitlement and permitted output. Record unknowns explicitly. Correlate the workload creation event, selected identity, artifact metadata, runtime data/action logs and output destination; evidence design must retain both actor and runtime identity. Provider logging availability and retention require separate validation.

An artifact digest alone is not trusted provenance; SLSA's verification baseline includes trust and provenance expectations. Downstream tool authorization should be enforced independently of a model-generated request. [SLSA-VERIFY, OWASP-AGENCY](SOURCES.md)

### 7. Limits and next experiment

No cloud infrastructure was provisioned. No live role escalation, cluster token usage, packet forwarding, LLM behavior or production hardening was measured. Fixture agreement is not a real-world detection-accuracy metric. The documented defaults register is separate from the experimental inputs. [Limitations](LIMITATIONS.md), [defaults](DEFAULTS.md)

Next: perform scoped provider validation using explicitly authorized synthetic resources; collect original actor/runtime policy and event evidence; attempt each path and negative control; review broader prior art; obtain independent reproduction. A provider-native unexpected authorization result would be triaged through coordinated disclosure before public exploit details are released. [Validation protocol](VALIDATION-PROTOCOL.md)

### References and research provenance

[Primary sources](SOURCES.md) · [Preparation provenance](../../PROVENANCE.md) · [Source manifest](../../evidence/source-manifest.json) · [Reproduction workflow](../../lab/README.md)
