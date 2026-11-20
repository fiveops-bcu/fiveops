# FiveOps team charter

**Project:** Evolving Ltd support-ticket application and DevOps delivery demonstration

**Module:** CMP6237 — DevOps and Enterprise Automation, Birmingham City University

**Prepared by:** Yasin Mohammed Miah, Team Leader

**Document status:** Draft for team agreement; not evidence that all five members have signed off

**Last reviewed:** 20 November 2026

## Purpose and scope

FiveOps is demonstrating how a small application change can move from an identifiable contributor through a reviewed GitHub pull request, automated checks and a reproducible delivery environment. The proof of concept is a Flask support-ticket API with customer and ticket operations. The agreed project direction includes Jenkins, Docker, PostgreSQL, Vagrant, Ansible and operational monitoring. We will distinguish code/configuration already merged from infrastructure and pipeline behaviour not yet demonstrated.

## Team, primary roles and hand-offs

| Member | Primary responsibility | Work products and hand-off | Review responsibility |
|---|---|---|---|
| **Yasin Mohammed Miah** | Team Leader; application integration and acceptance | Repository governance, sprint/feedback/decision/risk/evaluation records, README, demonstration coordination | Reviews Arkadiusz's PRs; receives Aissatou's review |
| **Arkadiusz Borkowski** | CI/CD Engineer | Docker image/test configuration, Jenkinsfile, build/test/scan/publish evidence; hands CI results to Yasin and Fadumo | Reviews Abdisalan's PRs |
| **Abdisalan Mohamed** | Platform Engineer | Vagrant VMs, Ansible baseline/Jenkins provisioning, repeatability evidence; provides Jenkins service to Arkadiusz | Reviews Fadumo's PRs |
| **Fadumo Ibrahim** | Quality and Security Engineer | Access audit, branch protection checks, Gitleaks, Bandit/Trivy gate definitions, secrets inventory, Jenkins credentials and security evidence | Reviews Aissatou's PRs |
| **Aissatou Diallo** | Operations and Monitoring Engineer | Prometheus/Grafana/log and alert configuration, rollback/idle evidence; also supports audit/review logbook | Reviews Yasin's PRs |

These are the roles in the Checkpoint 2 team playbooks. A role reassignment requires a recorded discussion, an agreed owner, a hand-off, and an entry in `docs/decision-log.md`; it is **not** already approved by this charter. PR #9 was created under Yasin's GitHub account and reviewed by Abdisalan, but its `common.yml` and `jenkins.yml` cover Abdisalan's platform domain. Git authorship remains factual and must not be rewritten solely to make the responsibility table look correct.

## Ways of working (proposed for explicit team confirmation)

1. **One source of truth:** `https://github.com/fiveops-bcu/fiveops` and its PRs/issues. The project board should show Backlog, Ready, In progress, In review and Done; do not claim a board exists until its URL is recorded.
2. **Accountability:** each person uses their own GitHub login and 2FA. No shared administrator logins. Do not post secrets in Teams, PRs or screenshots.
3. **Branch and review:** create a task branch from `main`; write a small PR explaining the change, how tested, evidence, and next action. Obtain an independent substantive written review before merge. Assigned rotation above is the planned default.
4. **Definition of Done:** follow `docs/definition-of-done.md`. An approval is not proof of successful automated tests; keep those as separate evidence.
5. **Communication:** report completed work, next step and blockers in the team channel. A block affecting another person's task should be raised promptly, with the failing command or redacted log.
6. **Fair responsibility changes:** check availability privately, give reasonable opportunities to respond, agree coverage with the team and record the outcome without personal accusations.
7. **Evaluation:** use target IDs 01–08 from `docs/evaluation.md`; never record a target as passed until a measurement exists.
8. **Security:** least privilege, review of dependencies and protected credentials. A lab shortcut (for example Docker group access) is recorded as a risk, not treated as production hardening.

## Handoffs and dependencies

`GitHub source + protected main → Abdisalan's reproducible Jenkins host → Arkadiusz's CI stages → Fadumo's gates/credentials → deployment evidence → Aissatou's monitoring/rollback evidence → Yasin's final traceability and assessment review.`

A separate GitHub Actions option has been discussed as an interim cloud CI method; implementing it is **not** evidence that the required Jenkinsfile has run. The hosting decision and any approved change must be added to `docs/decision-log.md`.

## Team approval record

| Member | Reviewed on | Agreed / requested change | PR or meeting evidence |
|---|---|---|---|
| Yasin Mohammed Miah | Pending | Pending | Pending |
| Arkadiusz Borkowski | Pending | Pending | Pending |
| Abdisalan Mohamed | Pending | Pending | Pending |
| Fadumo Ibrahim | Pending | Pending | Pending |
| Aissatou Diallo | Pending | Pending | Pending |

*No signatures or team confirmations have been assumed.*
