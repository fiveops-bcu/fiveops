# Sprint 2 summary (2–15 November 2026) — Checkpoint 2

**Prepared:** 20 November 2026 (retrospective, not a claim of a meeting on 15 November)

**Team Leader:** Yasin Mohammed Miah

**Sprint goal:** Establish shared, reviewed repository work and the first viable CI/CD chain for the Evolving Ltd support-ticket app.

## Done during the documented Sprint 2 window (through 15 November)

| Deliverable | PR / evidence | Confirmed state |
|---|---|---|
| Application and development requirements | [PR #1](https://github.com/fiveops-bcu/fiveops/pull/1), merged 15 Nov | Merged; peer reviews recorded |
| Arkadiusz individual contribution record | [PR #2](https://github.com/fiveops-bcu/fiveops/pull/2), merged 15 Nov | Merged; some historic incorrect PR references remained in content |
| Dockerfile, `.dockerignore`, PostgreSQL test Compose | [PR #3](https://github.com/fiveops-bcu/fiveops/pull/3), merged 15 Nov | Code merged; standalone PR build could not be reproduced until app source was integrated |
| Docker/PostgreSQL local results documentation | [PR #4](https://github.com/fiveops-bcu/fiveops/pull/4), merged 15 Nov | Documentation and image `docs/evidence/docker-postgres-test-results.png`; local result reported, independent Jenkins run not evidenced |
| Four-VM Vagrantfile, inventories and deploy public key | [PR #5](https://github.com/fiveops-bcu/fiveops/pull/5), merged 15 Nov | Code merged; VM provisioning not verified by PR description |

## Not done by the planned 15 November end, and why

| Planned outcome | What slipped / dependency | Corrective action and next owner |
|---|---|---|
| Full Flask source and tests on `main` | Source was on a separate branch while Docker PR entered first | [PR #6](https://github.com/fiveops-bcu/fiveops/pull/6) merged on **16 Nov**; Arkadiusz and Yasin to verify integration evidence |
| Security ignore rules and Fadumo record | Security work and contributor documentation continued after the sprint | [PR #7](https://github.com/fiveops-bcu/fiveops/pull/7) and [PR #8](https://github.com/fiveops-bcu/fiveops/pull/8) merged on **16 Nov**; Gitleaks/Vault/credentials still outstanding |
| Common and Jenkins Ansible playbooks | Vagrantfile depended on initially absent imported playbooks | [PR #9](https://github.com/fiveops-bcu/fiveops/pull/9) merged **18 Nov**; Abdisalan to demonstrate reproducible provisioning |
| Green shared Jenkins PR pipeline and registry image | Jenkins hosting/unlock, credentials and scans not verified | Abdisalan → Arkadiusz → Fadumo; capture actual run URL and status |
| Security, monitoring and rollback evidence | Full gate/monitoring configuration not present in reviewed `main` | Fadumo/Arkadiusz/Aissatou; submit separate PRs and evidence |
| Charter, DoD, feedback, decision, risk and evaluation docs | Team Leader evidence had not been committed | Drafts prepared 20 Nov for Aissatou's review; original Viva 1 feedback still required |

## Evidence index

- Contribution files: [`docs/contributions/`](../contributions/)
- Docker local-test evidence: [`arkadiusz-docker-tests.md`](../evidence/arkadiusz-docker-tests.md), [`docker-postgres-test-results.png`](../evidence/docker-postgres-test-results.png)
- Feedback mapping: [`docs/feedback-log.md`](../feedback-log.md) — **awaiting original feedback**
- Evaluation targets: [`docs/evaluation.md`](../evaluation.md) — **results pending**
- Risks and decisions: [`risk-log.md`](../risk-log.md), [`decision-log.md`](../decision-log.md)
- First successful shared Jenkins build: **not evidenced in current repository**; do not point to a non-existent `A5-green-pr.png`.

## Progress recorded after Sprint 2

PRs #6–#9 were merged on **16–18 November**. Those are follow-on implementation results, not retrospectively counted as 15 November completion.

## Next goal (16–29 November 2026)

Get one shared Jenkins pipeline running against the merged application, implement and verify all four gates, provision the test/production/monitoring environments to the documented standard, start monitoring and rollback demonstrations, and collect trial data for evaluation targets 01–08.

## Blockers and replan

1. **Shared CI host:** choose and verify local/cloud host; do not assume GitHub Actions proves Jenkinsfile execution. **Owner:** Abdisalan and Arkadiusz.
2. **Security gate dependencies:** no Gitleaks/Bandit/Trivy or Vault evidence on `main`. **Owner:** Fadumo and Arkadiusz.
3. **Feedback source:** actual Viva 1 comments/deck not available in the audited GitHub repo. **Owner:** Yasin to request and map them.
4. **Operations:** no monitoring implementation or timed alert/rollback data on `main`. **Owner:** Aissatou.
5. **Team presentation:** arrange a dated run-through and record attendance rather than inventing a past rehearsal.

**Review:** Request Aissatou's written review before merging this retrospective document.
