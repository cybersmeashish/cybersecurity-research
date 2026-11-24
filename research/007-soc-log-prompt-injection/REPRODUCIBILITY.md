# Reproduce CAI-007

No cloud credential, model, SDK, third-party Python package, or paid service is required. Source, fixtures, and runner are inside this folder.

## Existing canonical workspace

Use the pinned image, persistent volume, and source mounted read-only. The command below executes synthetic local code and writes temporary evidence.

```sh
docker --context orbstack run --rm --network none --read-only --user 1000:1000 \
 --cap-drop ALL --security-opt no-new-privileges --cpus 1 --memory 512m --pids-limit 64 \
 --tmpfs /tmp:rw,nosuid,nodev,size=128m \
 --mount source=cybersecurity-research-workspace,target=/workspaces,readonly \
 --workdir /workspaces/cybersecurity-research/repo/research/007-soc-log-prompt-injection \
 python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b \
 python3 -B tools/run_study.py --out /tmp/reproduction
```

With `--rm`, temporary evidence disappears after exit. To retain evidence, start a named isolated container with `sleep infinity`, run the runner through `docker exec`, and stream `tar` output from `/tmp/reproduction` before removing the temporary container. Preserve the named workspace volume. Do not mount host credentials, home directories, or the Docker socket.

## Fresh public source

Copy a public clone into a new named volume and give UID 1000 access, using container copy/transfer operations. Substitute that volume and source path in the command. Do not overwrite another project's workspace. Run project code only in the container.

## Expected checks

36 fixtures, 108 condition trials, six passing regression methods, 36/36 guarded policy matches, and all isolation flags true. Compare semantic outcome rows and tested source hashes with [published evidence](evidence/README.md). Timing, timestamps, ports, and scheduling details can vary. A rerun supports local reproducibility only, not provider behavior.
