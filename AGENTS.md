# Playground agent instructions

Read README.md and docs/system-test.md first. Work only on the assigned issue.
Python 3.12+ standard library only; no pip/npm downloads, real APIs, credentials or models.

Required checks for every change:
```
./scripts/check.sh
```
Also run the issue's named scenario; feature scenarios intentionally fail until implemented.
Add meaningful regression tests, preserve existing behavior, and record exact commands/results.
Do not disable tests, weaken CI, alter approval rules, use real user data or modify unrelated issues.
Use task keys and `plantool task done <item> T<n>` when running under Engineering OS.
Research/planning does not require a pre-existing approved plan; implementation does.
A frozen item or old provider failure is not evidence that all projects are unavailable.
Owner workspace replies clarify scope; they never approve plans, milestones or PRs.
