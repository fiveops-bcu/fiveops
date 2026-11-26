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

## Notes and failures

Record anything that went wrong, which gate caught it and how it was fixed. Failed runs count as evidence too.
