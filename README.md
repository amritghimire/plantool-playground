# plantool-playground

A disposable, deterministic repository for checking PlanTool Engineering OS against
real GitHub issues, approval gates, CI and PRs. It is not the PlanTool source tree.

Requires Python 3.12+ and a POSIX shell (macOS/Linux). No dependencies, API keys,
network calls, database or server are required by this fixture.

```sh
python3 --version
./scripts/check.sh
python3 -m playground Ada
```

To choose an installed interpreter: `PYTHON=python3.12 ./scripts/check.sh`.
Tests use unittest; CLI smoke checks run afterward. Any failed check returns nonzero.
See [system-test.md](docs/system-test.md) for reproducible system runs and issue order.

Feature acceptance scenarios intentionally fail until their matching issues are
implemented. They are separate from the passing baseline; do not weaken or delete them.
