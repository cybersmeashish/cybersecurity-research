# Limits and threats to validity

1. The graph is a deliberately simplified acyclic AND-precondition reference model. It is not a full IAM, Azure RBAC, Kubernetes authorization, policy-language or network evaluator. Effective permissions are inputs, not results of parsing real policies.
2. Fixtures are authored examples with expected results defined by the stated model. Matching them checks consistency and implementation behavior; it does not estimate real-world vulnerability prevalence, sensitivity or specificity.
3. The runtime experiment uses one local synthetic ACL backend. Four provider labels do not constitute four provider implementations or independent replications. No AWS, Azure, Google Cloud or Kubernetes API is called.
4. Cloud identities, service agents, trust policies, account/project boundaries, permission boundaries, organization policy, denies, token validity and managed-network enforcement are collapsed into explicit inputs. Uncollected evidence must remain unknown.
5. Broader compute authority is often intentional, particularly for curated ML workloads. A business-entitlement boundary and controllable unauthorized operation are required before treating delegation as a failure.
6. Artifact binding demonstrates a digest mismatch, not signatures, provenance verification, trusted builders or end-to-end SLSA compliance.
7. RAG selection and agent action requests are deterministic local cases. No embedding model, generative model, model obedience, prompt-injection success rate, hallucination rate or latency is measured.
8. Network constraints in the runtime are application-level decisions. The network-none container check proves the experiment's own isolation, not effectiveness of a Kubernetes CNI, VPC, private endpoint or cloud egress policy.
9. The graphs cover one stated path each. A blocked path does not establish a secure environment, and an egress block does not undo internal unauthorized reading or prevent approved-channel leakage.
10. Source pages are moving documentation reviewed on 24 November 2026. Recheck specific versions and deployed configuration. The primary-source review was not exhaustive prior-art research.

Independent reproduction and live, authorized provider validation remain future work. This version is not a compliance assessment, production-hardening guarantee or original zero-day disclosure.
