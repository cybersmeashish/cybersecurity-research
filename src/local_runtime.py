"""Local deterministic authority-binding experiment using synthetic records.

A shared ACL backend is intentionally used; profile names are labels and do not
emulate cloud APIs. No shell, remote endpoint, token, SDK or LLM is involved.
"""
from __future__ import annotations
from dataclasses import dataclass
import hashlib

@dataclass(frozen=True)
class Policy:
    caller_binding: bool = False
    scoped_runtime: bool = False
    egress_allowed: bool = True
    effective_runtime_read: bool = True
    trusted_digest: str | None = None

class LocalRuntime:
    def __init__(self, policy: Policy):
        self.policy = policy
        self.records = {"tenant-a": "SYNTHETIC:A:PUBLIC", "tenant-b": "SYNTHETIC:B:RESTRICTED"}
        self.audit = []

    def direct_read(self, actor, tenant):
        allowed = actor == tenant
        self.audit.append({"operation": "direct_read", "allowed": allowed, "actor": actor, "tenant": tenant})
        return self.records[tenant] if allowed else None

    def run_job(self, actor, tenant, artifact_bytes):
        actual_digest = hashlib.sha256(artifact_bytes).hexdigest()
        if self.policy.trusted_digest is not None and actual_digest != self.policy.trusted_digest:
            self.audit.append({"operation": "admit_artifact", "allowed": False, "reason": "digest mismatch"})
            return None
        if self.policy.caller_binding and actor != tenant:
            self.audit.append({"operation": "admit_job", "allowed": False, "reason": "actor entitlement"})
            return None
        if not self.policy.effective_runtime_read or (self.policy.scoped_runtime and tenant != "tenant-a"):
            self.audit.append({"operation": "runtime_read", "allowed": False, "reason": "effective data scope"})
            return None
        self.audit.append({"operation": "runtime_read", "allowed": True, "tenant": tenant})
        if not self.policy.egress_allowed:
            self.audit.append({"operation": "return_output", "allowed": False, "reason": "disclosure boundary"})
            return None
        self.audit.append({"operation": "return_output", "allowed": True})
        return self.records[tenant]

def run_runtime_experiment():
    payload = b"synthetic-unapproved-workload-v2"
    approved = hashlib.sha256(b"synthetic-approved-workload-v1").hexdigest()
    policies = {
        "baseline": (Policy(), True),
        "actor_binding": (Policy(caller_binding=True), False),
        "runtime_scope": (Policy(scoped_runtime=True), False),
        "disclosure_boundary": (Policy(egress_allowed=False), False),
        "effective_data_deny": (Policy(effective_runtime_read=False), False),
        "digest_binding": (Policy(trusted_digest=approved), False),
    }
    results = []
    for profile in ("AWS", "Azure", "Google Cloud", "Kubernetes"):
        for condition, (policy, expected) in policies.items():
            runtime = LocalRuntime(policy)
            direct = runtime.direct_read("tenant-a", "tenant-b")
            output = runtime.run_job("tenant-a", "tenant-b", payload)
            disclosure = output == "SYNTHETIC:B:RESTRICTED"
            assert direct is None
            assert disclosure == expected
            results.append({"profile_label": profile, "condition": condition,
                            "direct_access_denied": direct is None,
                            "unauthorized_output_returned": disclosure,
                            "expected_output_returned": expected,
                            "matches_expected": disclosure == expected,
                            "audit": runtime.audit,
                            "scope": "one shared mock backend; profiles are not independent provider experiments"})
    return results
