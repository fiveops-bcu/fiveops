# Release trace — targets 01, 03 and 06

**Owner:** Yasin Mohammed Miah (Team Leader) · **Contributors:** Arkadiusz (Jenkins, GHCR), Abdisalan (deployment), Fadumo (gates)

**Status:** Template, not yet filled. Fill in **one row per real release**, only from evidence you can link. Leave a cell blank rather than estimate it.

## How to run one traced release

1. Pick a small, real change from the board (for example, a wording fix in `/health` JSON or a docs change that still triggers the pipeline).
2. Start a stopwatch the moment the PR is **merged to `main`**. Write the UTC time down.
3. In Jenkins, open the `main` build for that commit. Copy its URL and the duration of each stage from Pipeline Graph View.
4. When TEST is healthy, run `curl -s http://<test-host>:8000/version` and `curl -s http://<test-host>:8000/health`. Save the output.
5. If production is in scope, note the time the approval prompt appeared and the time it was approved. Approval wait is **excluded** from target 01.
6. Stop the stopwatch when `/version` on the last environment returns the new 7-character tag.
7. Save screenshots to `docs/evidence/` as `T01-<tag>-<what>.png`. No tokens, passwords or webhook URLs on screen.

## Target 01 — commit to live in under 20 minutes

| Commit (7) | PR | Merged (UTC) | Jenkins build URL | Build + test + scan (min) | TEST healthy (UTC) | Approval wait (min, excluded) | PROD healthy (UTC) | Elapsed excl. approval (min) | Pass < 20? |
|---|---|---|---|---:|---|---:|---|---:|---|
| | | | | | | | | | |

## Target 03 — every release traceable

A release passes only if **every** link below exists and points at the same commit.

| Commit (7) | PR and named approver | Jenkins build (tests, Gitleaks, Bandit, Trivy green) | GHCR image and digest | `/version` on TEST | `/version` on PROD | `releases.log` line | Complete? |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Target 06 — no deployment without passing tests

| Check | How to prove it | Evidence file or link | Result |
|---|---|---|---|
| Tests and ≥ 80% coverage run on every build | JUnit and `coverage.xml` archived on the Jenkins build | | |
| A failing test stops the pipeline before deploy | Open a test PR that breaks one test; Jenkins shows red and no deploy stage runs | | |
| A red PR cannot merge | Jenkins check required in `protect-main`; screenshot of the blocked merge button | | |

## Interim release observation — 26 November (reported; not a target pass)

| Field | Recorded observation |
|---|---|
| Source revision | `b219a76` (PR #41 merged 26 Nov at 19:15:55 UTC) |
| PR and review | [PR #41](https://github.com/fiveops-bcu/fiveops/pull/41), approved by AbdiAwil |
| Deployment handover | [PR #43](https://github.com/fiveops-bcu/fiveops/pull/43), merged 26 Nov |
| TEST | Healthy and running `b219a76` according to PR #43 |
| GHCR | Running digest matches pull digest according to PR #43; exact digest and raw output still needed |
| Monitoring | TEST Node Exporter HTTP 200 reported from monitoring VM |
| Jenkins | Successful build number, URL, stage timings and artifacts pending |
| Production | Disabled during reported deployment; no production result claimed |
| Acceptance | Targets 01, 03 and 06 remain pending |

The latest repository commit at review is `12e7093`; it is not the reported deployed revision. Do not substitute the current main SHA for the earlier deployed release. Keep the measurement tables empty until the required raw evidence is available.

## Notes and failures

Record anything that went wrong, which gate caught it and how it was fixed. Failed runs count as evidence too.
