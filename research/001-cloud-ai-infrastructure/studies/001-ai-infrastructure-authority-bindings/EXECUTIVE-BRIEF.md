# Executive decision brief: bind business authority to AI execution

**Decision:** require evidence that the requester, selected runtime identity, consumed artifact, protected data/action and output route agree with the approved business scope before admitting an AI workload.

**Operational consequence:** a user can be denied direct data access while their allowed job uses a broader identity. This can be an intentional operating model; the security question is whether controlled code or requested actions can produce a result outside the user's approved scope. Private ingress and scoped caller accounts do not settle that question by themselves.

**Measured result:** see [RESULTS.md](RESULTS.md) for the generated local counts. The mock baseline returns a protected synthetic record through delegated runtime authority, while individual actor, runtime, output, effective-permission and digest controls interrupt that stated final outcome. Output restriction can still leave an internal read, requiring separate review.

**Evidence boundary:** eight reference-model chains and one local mock backend. Four provider labels are illustrative; actual AWS/Azure/Google Cloud/Kubernetes behavior was not tested. New provider vulnerabilities confirmed: zero. No novelty, certification, client-delivery or compliance claim is made.

**Next investment:** authorize one contained provider experiment with synthetic data and a low-cost quota; nominate workload, IAM, network and AI application owners; retain effective policies, deployment settings, admitted digests and decision logs; obtain independent reproduction. Admission failures must preserve enough context to explain actor, intended action and selected identity.

**Acceptance evidence for the next stage:** denied direct access; a reproducible unauthorized delegated outcome or a correctly denied path; an observed effective control; a permitted same-tenant operation; remaining unknowns and scope. Agree dates and resources separately. This version is research evidence, not a production assessment.
