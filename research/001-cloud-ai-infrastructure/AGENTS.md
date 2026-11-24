# Canonical development workflow

Use OrbStack explicitly: `docker --context orbstack`. Canonical development container: `cybersecurity-research-dev`; persistent volume: `cybersecurity-research-workspace`; workspace: `/workspaces/cybersecurity-research`.

Run source edits, study analysis, tests and artifact generation inside this repository-specific container. Host copies are for review and guarded publication only. Keep root read-only, UID 1000, no external networking, capabilities dropped, no-new-privileges, bounded resources and a temporary result directory. Never mount home directories, credentials or the Docker socket. Preserve persistent volumes.

Run final verification with the workspace mounted read-only. Source manifest and reviewed file hashes must match before publication. Preserve unrelated existing remote files, reject a moving main branch and verify published bytes. Do not provision a cloud environment or run live attacks from this synthetic study without explicit scope and the future-validation protocol.

Do not label hypotheses or mock results as new provider vulnerabilities. Keep documented defaults, model assumptions, local results and observed provider behavior separate.
