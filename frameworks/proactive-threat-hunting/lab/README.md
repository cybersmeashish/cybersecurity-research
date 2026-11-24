# Reproduce the synthetic hunt lab

The local laboratory uses 34 scenarios: 17 intended candidate seeds and 17 benign/broken-chain comparisons. These are curated examples, not an independent operational detection benchmark. All identities, hashes, domains, approvals and source-health records are synthetic.

Run the pinned image against the existing canonical workspace with network disabled and the volume read-only:

```sh
docker --context orbstack run --rm --network none --read-only --user 1000:1000 \
 --cap-drop ALL --security-opt no-new-privileges --cpus 1 --memory 512m --pids-limit 64 \
 --tmpfs /tmp:rw,nosuid,nodev,size=128m \
 --mount source=cybersecurity-research-workspace,target=/workspaces,readonly \
 --workdir /workspaces/cybersecurity-research/repo \
 python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b \
 python -B frameworks/proactive-threat-hunting/tools/run_lab.py --out /tmp/hunt-lab
```

To retain temporary output, use an explicit temporary container name without `--rm`, copy `/tmp/hunt-lab` with `docker cp`, then remove that temporary container. Preserve the development volume. A fresh public clone needs a new named volume and copied source, never a credentials/home/socket mount; see the repository workflow.

For a single demo:

```sh
python -B frameworks/proactive-threat-hunting/src/hunt_engine.py \
 --input frameworks/proactive-threat-hunting/lab/demo.json --out /tmp/hunt-demo.json
```

Run this second command inside the same isolated environment. It outputs candidate associations and quality status, not incident verdicts. No third-party Python dependency, cloud credential, external intelligence feed or paid service is required.

Expected summary: 17 procedures, 13 domains, 34 matching scenario expectations, 17 demo candidate leads and 19 security-boundary regression methods. [Fixture definition](fixtures.json) · [Demo data](demo.json) · [Limitations](../docs/LIMITATIONS.md).
