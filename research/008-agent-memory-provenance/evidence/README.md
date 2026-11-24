# Evidence inventory — CAI-008

| Artifact | Meaning |
|---|---|
| [summary.json](summary.json) | Condition counts, runtime, isolation, and scope |
| [results.csv](results.csv) | One row per fixture-condition trial |
| [traces.json](traces.json) | Actual local decision/effect trace keyed by case and mode |
| [tests.txt](tests.txt) | Six behavioral regression methods |
| [source-manifest.json](source-manifest.json) | SHA-256 of executed source, tests, runner, and fixtures |
| [claim-ledger.json](claim-ledger.json) | Claims, evidence stages, and exclusions |
| [findings.json](findings.json) | Bounded machine-readable local findings |

These files were copied from the read-only verification container's temporary output. They are actual local execution artifacts, not results from a cloud provider or language model. Fixtures are intentionally constructed; there is no prevalence benchmark. Timing extensions, where present, are documented in [RESULTS.md](../RESULTS.md).
