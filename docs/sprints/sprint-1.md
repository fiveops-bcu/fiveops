# Sprint 1 — mobilisation and hand-off into Checkpoint 2

**Scope:** First project mobilisation, repository ownership, team roles and architecture hand-off

**Calendar dates:** Formal Sprint 1 boundaries not evidenced in the inspected source materials; team to confirm

**Prepared retrospectively:** 20 November 2026

**Coordinator:** Yasin Mohammed Miah

## Initial goal

Establish a shared source repository and delivery conventions so the FiveOps team can turn the Viva 1 proposal into separately reviewed application, CI, platform, security and operations tasks.

## Verified implementation carried into Checkpoint 2

- Repository `fiveops-bcu/fiveops` has a Git history and an initial `README.md`, `.gitattributes`, PR template, `.gitignore` and evidence/contribution/sprint folder READMEs.
- Requirements and development-test dependencies entered via [PR #1](https://github.com/fiveops-bcu/fiveops/pull/1), merged **15 November 2026** (included here as *hand-off evidence*, not an assertion about the unconfirmed Sprint 1 dates).
- The documented team plan names five primary roles, with a rotation for written PR review. The charter in `../team-charter.md` awaits explicit sign-off.

## What was incomplete at the hand-off

| Requirement | Gap and impact | Replan / owner |
|---|---|---|
| Team charter and Definition of Done | No formal tracked documents on previous `main` | Yasin: submit these documents in a reviewed PR |
| Risk and decision records | Key design choices and their residual risks had not been recorded in `docs/` | Yasin: baseline dated registers and invite team review |
| Feedback-to-backlog traceability | Original Viva 1 feedback notes are needed before item-level action links can be made | Yasin: collect source notes, then assign linked feedback issues |
| Board URL and sprint evidence | An agreed board link and dated screenshot were not found in inspected repository | Yasin: create/verify board, then link screenshot |
| Automated integration evidence | Configuration work planned but not proven by Jenkins at mobilisation | Abdisalan / Arkadiusz: establish CI host and pipeline |

## Lessons and next increment

A repository skeleton enabled contribution, but written acceptance criteria and a single visible task board were not yet demonstrated. For Checkpoint 2, prioritise reviewed implementation PRs and truthful proof of tests and configuration rather than treating code presence as a completed delivery. See the dated [`Sprint 2 summary`](sprint-2.md).

## Evidence and review status

- [Repository commits](https://github.com/fiveops-bcu/fiveops/commits/main)
- [PR #1](https://github.com/fiveops-bcu/fiveops/pull/1)
- Sprint 1 team retrospective and sign-off: **not yet provided**.
