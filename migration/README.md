# Research relocation and publication evidence

All 40 files from the original AIA-001 repository version now have destinations within `research/001-cloud-ai-infrastructure`. Shared license/ignore files also remain at the repository root. Relative package links and source/data layout are retained. Canonical absolute reproduction paths were updated and evidence regenerated after the move.

[research-001-relocation.json](research-001-relocation.json) records the original source commit, old/new paths and SHA-256 hashes, distinguishing unchanged source from documented path/evidence updates. The original commit remains in Git history; no history rewrite is performed.

[verification.json](verification.json) records both package test runs, local-link checks and source-manifest consistency. Publication separately verifies the complete final GitHub file set and exact bytes, rejects unexpected removals and refuses a moving main branch. The ledger is a content trace, not an authenticity signature or peer review.

The former main paper path retains a short navigation stub to preserve its public permalink; the actual paper and supporting content live in the research package.
