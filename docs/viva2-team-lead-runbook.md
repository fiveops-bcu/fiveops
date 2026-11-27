# FiveOps — Team Leader playbook completion and Viva 2 runbook

**Owner:** Yasin Mohammed Miah · Task [#21](https://github.com/fiveops-bcu/fiveops/issues/21)
**Repository review:** 26 November 2026, main `12e7093`
**Status:** Prepared plan; no rehearsal or live verification claimed.

## Checkpoint 2 individual playbook reconciliation

Based on the original individual playbook (14 November, Part 1 steps 1–7, Part 2 steps 1–8 and Part 3). Retain actual authorship and distinguish repository proof from unverified actions.

| Requirement | Evidence / current status | Remaining action |
|---|---|---|
| Organisation access, named Git identity and 2FA | Named GitHub commits and PRs exist; individual 2FA and organisation access audit not independently verified | Obtain redacted People/2FA evidence with Fadumo |
| Repository skeleton and review workflow | `.gitattributes`, PR template and Sprint 1 documents exist; PR #10 merged | Confirm squash-only and automatic branch deletion settings; retain review evidence |
| Protect main | Active ruleset with one approval, linear history, deletion and force-push restrictions | Enable stale approval dismissal, conversation resolution; verify bypass policy and record rejected push evidence without bypassing rules |
| Load project board | Five role issues exist; #18 closed | Link actual board and check step-level cards and feedback issues |
| Three reviewed application PRs | PR #1 is Yasin's requirements work; PR #6 is Arkadiusz's app and tests. Original three-PR/reviewer plan not demonstrated | Record actual division of work; do not claim or manufacture historical PRs |
| Own local and PostgreSQL test evidence | Team-reported 13 tests and 97.09% coverage; prior personal local run documented with PostgreSQL skipped | Run the approved Docker Compose test suite and preserve actual redacted output |
| Contribution record and written review | Existing contribution file and PR history; review partner in original playbook was Aissatou | Request Aissatou's written review on this documentation PR; document any agreed review rotation change |
| Four documents and Sprint 2 summary | Merged through PR #10 | Maintain accurate current risk, decision, evaluation and sprint records; original tutor feedback still required |
| Compulsory Jenkins check | No reported required status at review | Coordinate actual Jenkins check context with Arkadiusz/Fadumo, then require it; demonstrate red/pending PR is blocked |
| Run-through and individual defence | Preparation only | Record attendance, actual timings, blockers and review feedback |

## Integration and assessment schedule

- 27 Nov, 14:00: integration session (documented in Sprint 3).
- 28 Nov: planned alert and rollback drills.
- 29 Nov: planned internal demonstration and timed rehearsal.
- 30 Nov: proposed code freeze, subject to team confirmation.
- 1–3 Dec: proposed evidence consolidation and rehearsal.
- 4 Dec: planned Viva 2 and peer review assessment date; confirm appointment on Moodle.

## Demo sequence (30-minute rehearsal, suggested allocation)

| Minutes | Lead | Evidence |
|---|---|---|
| 0–4 | Yasin | Client problem, scope, architecture, issues, actual acceptance criteria |
| 4–10 | Arkadiusz | Reviewed change, Jenkins checkout, tests, coverage, security gates, GHCR digest |
| 10–15 | Abdisalan | Versioned IaC, actual VMware configuration, TEST health and version, deployment safety |
| 15–20 | Fadumo | Scanner results, negative test, credentials, least privilege, status gate |
| 20–25 | Aissatou | Live monitoring, alert delivery and recovery measurements if available |
| 25–30 | Yasin and team | Release trace, limitations, eight targets, prioritised next work |

Keep production disabled unless the team has verified the production credentials, approval authority, network scope and recovery procedure. Use synthetic data and redact secrets from all screenshots.

## Evidence to obtain

Original playbook filenames: `L1-people.png`, `L3-push-rejected.png`, `L4-board.png`, `Y5-pytest-coverage.png`, `Y5-postgres-run.png`; use actual dated screenshots only. Also capture Jenkins build URL and commit, JUnit and coverage, scanner reports, image digest, TEST `/health` and `/version`, approval/rollback and notification records where performed. Keep raw evidence linked from `docs/evaluation.md` and `docs/evidence/release-trace-target-01-03-06.md`. No evaluation target is passed at this review.

## Personal defence draft

My contribution is the governance and integration of FiveOps. I established the repository and documentation, submitted pinned requirements and baseline Ansible playbooks, resolved the CI/CD and platform conflicts in PRs #28 and #31, and corrected the production deployment path and opt-in gate in PR #36. I coordinate evidence from every role, rather than claiming the team's technical contributions as my own. The remaining priority is to enforce passing Jenkins checks and demonstrate a traceable release with measured results. I will explain any incomplete tests and their impact on the client instead of claiming an unverified production-ready system.
