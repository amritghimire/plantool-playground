# Reproducible Engineering OS run

## Prepare once

Merge the fixture bootstrap PR first. In the local checkout configured in PlanTool:

```sh
git switch main
git pull --ff-only
./scripts/check.sh
./scripts/verify-scenario.sh baseline
```

Use Python 3.12+; set PYTHON to its executable if python3 is older. No pip install
is needed. Scripts change to the repository root and can run from any directory.
Do not reset/delete your PlanTool database, worker checkpoints or GitHub history.

Install the latest PlanTool fixes, confirm Worker Ready, execution enabled and
verified role routes. Configure the App, project checkout, owner allowlist and
provider policy in the application. An old frozen scheduler, scan and issue need
separate eligible Owner recovery; a Git pull does not unfreeze them.

## First issue, then a three-item sprint

Start with docs issue #1 after bootstrap. It remains docs-only: docs/testing.md and
a README link, with a known check command. Recover its failed triage if needed.
For immediate planning an allowlisted owner can post `/plantool urgent` as a new
whole-line issue comment. Do not edit an old command or invent approval hashes.

Read the App's new plan and approve using the exact current-hash command it posts.
Watch role attempts, workspace discussion, graph history and gates. Expect evidence
for actual commands, scoped keyed tasks and an App PR. Wait for current-head CI and
submit the owner Approve review only after inspecting the PR. Use App-provided
milestone commands if Standard/Strict gates apply. These are real model calls and
may consume subscription/cloud quota; local fixture checks do not.

After the first happy path, use docs, slug and JSON-output issues as independent
small sprint candidates (if docs is already complete, use the CI issue instead).
Each needs a prepared plan before it is eligible for a sprint snapshot. Known,
frozen or unplanned issues are not automatically candidates. An empty sprint is
valid. Approve only the latest tracking snapshot with commands posted by the App.
Do not create your own Sprint tracking issue; PlanTool owns it.

## Acceptance commands

| Scenario | Command | Bootstrap result |
| --- | --- | --- |
| Passing baseline | ./scripts/verify-scenario.sh baseline | Pass |
| Docs issue | ./scripts/verify-scenario.sh docs | Fail until docs/testing.md is written |
| Slug helper issue | ./scripts/verify-scenario.sh slug | Fail until helper is implemented |
| JSON CLI issue | ./scripts/verify-scenario.sh json | Fail until --json is implemented |

Each implementation adds regression tests under tests/; ./scripts/check.sh must
remain green. Scenario commands fail on unmet requirements, never skip or fabricate
success. They cover a minimum acceptance contract; reviewers still assess full scope.

## CI and evidence

CI runs on Ubuntu and macOS with Python 3.12 on main pushes, PRs and manual dispatch.
After checks first appear, require `playground (ubuntu-latest)` and
`playground (macos-latest)` in the main ruleset. Add plantool/policy only after the
App first publishes it. Use PR reviews and dismiss stale approvals. The owner
configures repository protection; no script changes it or merges automatically.

Record issue/PR URLs, plan hash, head SHA, selected model, duration, command exit
codes and evidence links. Passing unit tests is not proof that the whole Engineering
OS loop passed. Record provider failures and native checks separately.

## Recovery and scope checks

- A failed provider may use bounded fallback; historical failures do not establish
  a current global outage. Do not Repair a healthy worker for a result-schema error.
- Stop All must stop execution; resuming still needs owner authorization.
- Workspace owner replies are scope context, never approval. Stale plan hashes and
  old-head PR approvals must not release work.
- Keep negative authority/recovery experiments separate from the first happy path;
  do not change allowlists, create fake evidence or erase history to force progress.
- Agent PRs must not alter acceptance scripts or weaken checks to make a feature pass.
