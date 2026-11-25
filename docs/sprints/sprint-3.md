# Sprint 3 summary (16–29 November 2026) — Integration

**Prepared:** 25 November 2026 (mid-sprint; to be completed after the internal demo on 29 November)

**Team Leader:** Yasin Mohammed Miah

**Sprint goal:** Get one shared Jenkins pipeline running against the merged application, implement the four gates, deploy to TEST and PROD, start monitoring and rollback, and collect trial data for targets 01–08.

## Merged so far (16–25 November)

| Deliverable | PR | Author → approver of record | State |
|---|---|---|---|
| Application code and automated tests | [#6](https://github.com/fiveops-bcu/fiveops/pull/6) | Arkadiusz | Merged 16 Nov |
| Fadumo contribution record; secret ignore rules | [#7](https://github.com/fiveops-bcu/fiveops/pull/7), [#8](https://github.com/fiveops-bcu/fiveops/pull/8) | Fadumo | Merged 16 Nov |
| Common baseline and Jenkins playbooks | [#9](https://github.com/fiveops-bcu/fiveops/pull/9) | Yasin → Abdisalan | Merged 18 Nov |
| Checkpoint documentation | [#10](https://github.com/fiveops-bcu/fiveops/pull/10) | Yasin → Abdisalan | Merged 22 Nov |
| Docker image build stage | [#12](https://github.com/fiveops-bcu/fiveops/pull/12) | Arkadiusz | Merged 23 Nov |
| Planned secrets inventory | [#14](https://github.com/fiveops-bcu/fiveops/pull/14) | Fadumo | Merged 23 Nov |
| Contribution and progress records | [#13](https://github.com/fiveops-bcu/fiveops/pull/13), [#15](https://github.com/fiveops-bcu/fiveops/pull/15), [#17](https://github.com/fiveops-bcu/fiveops/pull/17), [#22](https://github.com/fiveops-bcu/fiveops/pull/22), [#23](https://github.com/fiveops-bcu/fiveops/pull/23), [#24](https://github.com/fiveops-bcu/fiveops/pull/24), [#32](https://github.com/fiveops-bcu/fiveops/pull/32), [#34](https://github.com/fiveops-bcu/fiveops/pull/34) | Each member | Merged 22–25 Nov |
| Ansible TEST deployment with PostgreSQL and health checks | [#25](https://github.com/fiveops-bcu/fiveops/pull/25) | Abdisalan | Merged 25 Nov |
| Gitleaks, Bandit and Trivy gates | [#26](https://github.com/fiveops-bcu/fiveops/pull/26) | Fadumo | Merged 25 Nov |
| GHCR publishing, Ansible deploy of GHCR images | [#27](https://github.com/fiveops-bcu/fiveops/pull/27), [#28](https://github.com/fiveops-bcu/fiveops/pull/28) | Arkadiusz (conflict fix by Yasin in #28) | Merged 25 Nov |
| Production playbook and manual approval stage | [#29](https://github.com/fiveops-bcu/fiveops/pull/29), [#30](https://github.com/fiveops-bcu/fiveops/pull/30) | Arkadiusz | Merged 25 Nov |
| Jenkins image transfer + Ansible TEST deploy with automatic rollback | [#31](https://github.com/fiveops-bcu/fiveops/pull/31), [#33](https://github.com/fiveops-bcu/fiveops/pull/33) | Abdisalan (reconcile commit by Yasin in #31) | Merged 25 Nov |
| Target 04 access-control audit | [#35](https://github.com/fiveops-bcu/fiveops/pull/35) | Fadumo | Merged 25 Nov |
| Production path fix; production deploy off by default | [#36](https://github.com/fiveops-bcu/fiveops/pull/36) | Yasin → Abdisalan | Merged 25 Nov |

Approver names for each PR are recorded on GitHub; this table does not replace that record.

## Open at 25 November, with owners

| Gap | Why it matters | Owner | Issue |
|---|---|---|---|
| Monitoring stack is on branch `feature/operations-monitoring` with no PR | No monitoring in the demo without it (target 07) | Aissatou, reviewed by Fadumo | [#20](https://github.com/fiveops-bcu/fiveops/issues/20) |
| Alertmanager receiver has no Teams destination | Alerts fire but reach nobody (target 07) | Aissatou | #20 |
| PROD stage passes no database secret; `deploy-prod.yml` has no rollback and reports `production` instead of the commit | Production deployment will stop at validation; traceability breaks (targets 01, 02, 03) | Arkadiusz with Abdisalan | [#16](https://github.com/fiveops-bcu/fiveops/issues/16), [#18](https://github.com/fiveops-bcu/fiveops/issues/18) |
| Jenkins posts no commit status to GitHub (HTTP 403 noted by Fadumo) | `protect-main` cannot require a passing build (target 06) | Fadumo with Arkadiusz; Yasin adds the required check | [#19](https://github.com/fiveops-bcu/fiveops/issues/19) |
| Production approval has no `submitter` restriction | Any Jenkins user can approve (target 04) | Arkadiusz | #16 |
| Rollback and idle Jenkins jobs not built | Targets 02 and 08 cannot be measured | Aissatou | #20 |
| Scanner versions not installed or pinned on the Jenkins server | A rebuilt server breaks the pipeline (targets 05, 06) | Abdisalan | #18 |
| No measured results for targets 01–08 | Viva 2 needs real timings and evidence | All; Yasin coordinates | [#21](https://github.com/fiveops-bcu/fiveops/issues/21) |

## Replan to the internal demo (Sunday 29 November)

1. **Thu 26 Nov:** monitoring PR opened and reviewed; PROD stage and approver fixes raised; Jenkins token for commit statuses created.
2. **Fri 27 Nov, Integration Friday 14:00:** one change travels PR → Jenkins check → GHCR → TEST → approval → PROD. Record it in [`release-trace-target-01-03-06.md`](../evidence/release-trace-target-01-03-06.md).
3. **Sat 28 Nov:** Teams receiver live; three alert drills (07) and three rollback drills (02); idle job running (08).
4. **Sun 29 Nov:** timed rehearsal in the Viva 2 order; complete this summary with the outcome.

## Still to record at sprint end

- Which gaps above closed, with PR links and evidence files.
- Any target not met, the reason and the next step.
- Written review of this summary by Aissatou before merge.
