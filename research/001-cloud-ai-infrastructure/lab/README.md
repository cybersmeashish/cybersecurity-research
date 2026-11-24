# Reproduce the isolated reference study

Requires Docker/OrbStack and the pinned Python image. No cloud credentials, paid services or package installation. Canonical source is in container `cybersecurity-research-dev`, volume `cybersecurity-research-workspace`, folder `/workspaces/cybersecurity-research/repo/research/001-cloud-ai-infrastructure`. Use the existing volume when continuing this workspace.

## Existing canonical workspace

```sh
docker --context orbstack run --rm --network none --read-only --user 1000:1000 \
  --cap-drop ALL --security-opt no-new-privileges --cpus 1 --memory 512m --pids-limit 64 \
  --tmpfs /tmp:rw,nosuid,nodev,size=128m \
  --mount source=cybersecurity-research-workspace,target=/workspaces,readonly \
  --workdir /workspaces/cybersecurity-research/repo/research/001-cloud-ai-infrastructure \
  python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b \
  python -B tools/run_study.py --out /tmp/aia-001
```

The summary prints to stdout. For retaining temporary evidence, run without `--rm` using an explicit temporary container name, copy `/tmp/aia-001` out, then remove that temporary container. Keep the persistent development volume.

## Fresh public clone

Clone this repository into an empty local review folder, then initialize a new named volume and copy only the source into a container workspace. Use container `docker cp`, not a home-directory/credential/socket mount. Give the workspace to UID 1000. Run the command above with that new volume and workspace path. Do not reuse or overwrite another project's volume.

Image identity: `python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b`. Expected runtime: Python 3.12.16, Linux; recorded architecture is aarch64 for the published run. This pinned old image is a reproducibility input, not a current production base-image security recommendation.

## What the run proves

The runner executes the synthetic fixtures, deterministic runtime cases and security-boundary regression methods. It confirms external networking is unavailable using a documentation-range address, records read-only state, and hashes the source. It does not prove provider IAM/networking behavior, real-world detection accuracy or cloud vulnerability discovery.

Exact reproduction compares the graph and runtime result files. Timestamp, OS/architecture and verification-environment fields may legitimately differ.
