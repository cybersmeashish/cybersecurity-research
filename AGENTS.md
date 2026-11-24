# Canonical workflow

Use `docker --context orbstack` explicitly. Development container: `cybersecurity-research-dev`; persistent volume: `cybersecurity-research-workspace`; canonical root: `/workspaces/cybersecurity-research/repo`.

Research package: `research/001-cloud-ai-infrastructure`. Hunting package: `frameworks/proactive-threat-hunting`. Keep package-local relative links and reproduction instructions correct after any movement.

All edits, analysis, code, tests and artifacts run inside this repository-specific OrbStack container. Host copies are for review and guarded publishing only. Keep the root read-only, use UID 1000, drop capabilities, enforce no-new-privileges, bound resources and disable external networking for lab execution. Do not mount home folders, credentials or the Docker socket. Preserve the persistent volume.

Run both package verifiers against a read-only workspace; regenerate their evidence and source manifests when source changes. Do not present synthetic tests as live provider exploits, operational hunt results or a real-world detection benchmark. Raw event/reference identifiers and source-health assumptions need documented normalization; maintain tenant and canonical principal boundaries.

For a relocation publication, validate the exact original remote file set and hashes, enumerate each removed old path and corresponding destination, preserve Git history, refuse unexpected deletion or moving main, and verify every resulting public file. Do not force-push.
