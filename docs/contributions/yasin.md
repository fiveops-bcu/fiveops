# Contribution record — Yasin Mohammed Miah (Team Leader)

**Last updated:** 25 November 2026

**Programme:** BSc (Hons) Computing (Level 6 Top-up), Birmingham City University

**Project:** FiveOps — CMP6237 / Evolving Ltd

## Done, with verifiable GitHub evidence

- **14 November:** Established initial repository content and documentation structure (README, PR template, `.gitattributes` and team-evidence folders). See [Git history](https://github.com/fiveops-bcu/fiveops/commits/main).
- **15 November:** Submitted pinned dependency files in [PR #1](https://github.com/fiveops-bcu/fiveops/pull/1), merged with recorded reviews.
- **15–16 November:** Reviewed Arkadiusz's changes, including [PR #2](https://github.com/fiveops-bcu/fiveops/pull/2), [PR #3](https://github.com/fiveops-bcu/fiveops/pull/3), [PR #4](https://github.com/fiveops-bcu/fiveops/pull/4), and [PR #6](https://github.com/fiveops-bcu/fiveops/pull/6). GitHub contains review submissions and approvals; these are **not** evidence that Jenkins executed successfully.
- **15–16 November:** Reviewed/approved [PR #5](https://github.com/fiveops-bcu/fiveops/pull/5), [PR #7](https://github.com/fiveops-bcu/fiveops/pull/7) and [PR #8](https://github.com/fiveops-bcu/fiveops/pull/8) as recorded in GitHub. The planned review rotation differs in places from actual recorded reviewers; this record states actual activity.
- **18 November:** Submitted [PR #9](https://github.com/fiveops-bcu/fiveops/pull/9) with `ansible/playbooks/common.yml` and `jenkins.yml`. **Abdisalan reviewed and approved**; the code belongs to the Platform Engineer's technical domain. Keep Git attribution unchanged and require Abdisalan to explain the playbooks at Viva 2.
- **22 November:** Submitted [PR #10](https://github.com/fiveops-bcu/fiveops/pull/10) covering team charter, Definition of Done, decision and risk logs, feedback log, evaluation plan (targets 01–08), sprint summaries, my contribution record and README expansion. **Abdisalan (`AbdiAwil`) approved it on 22 November and it was merged into `main` at 17:41 UTC.** This demonstrates documentation and review completion, not successful CI/deployment.
- **23 November:** Created or coordinated task assignments across [issues #16](https://github.com/fiveops-bcu/fiveops/issues/16), [#18](https://github.com/fiveops-bcu/fiveops/issues/18), [#19](https://github.com/fiveops-bcu/fiveops/issues/19), [#20](https://github.com/fiveops-bcu/fiveops/issues/20) and [#21](https://github.com/fiveops-bcu/fiveops/issues/21). Reviewed the team's merged application, CI/CD, security and operations documentation contributions; see GitHub's PR review history for the actual reviewer.
- **24 November:** Reviewed and approved Abdisalan's [PR #23](https://github.com/fiveops-bcu/fiveops/pull/23), documenting VMware-based test infrastructure and an Ansible idempotency observation. Abdisalan remains the implementer and technical owner of the platform work.
- **24–25 November:** Submitted [PR #24](https://github.com/fiveops-bcu/fiveops/pull/24) (team-lead record, VMware decision D-11 and interim evaluation observations), merged 25 November.
- **25 November:** Resolved integration conflicts so the CI/CD and platform branches could merge: commit `ff7fee1` (Jenkinsfile conflict with latest `main`) inside Arkadiusz's [PR #28](https://github.com/fiveops-bcu/fiveops/pull/28), and commit `495df9b` (reconcile GHCR publishing with the Ansible TEST deployment and rollback) inside Abdisalan's [PR #31](https://github.com/fiveops-bcu/fiveops/pull/31). Both PRs keep their original authors; I merged them.
- **25 November:** Submitted [PR #36](https://github.com/fiveops-bcu/fiveops/pull/36) (correct the production playbook path; production deployment parameter `ENABLE_PRODUCTION_DEPLOY`, off by default). Approved by Abdisalan (`AbdiAwil`) and merged.
- **25 November (correction to PR #36):** the PR description states that Jenkins was green and that production approval is restricted to authorised users. GitHub shows **no Jenkins check** on the PR, and the `input` step in `Jenkinsfile` has **no `submitter` restriction**. Both remain open actions (Fadumo/Arkadiusz for status reporting; Arkadiusz for the approver list) and must not be cited as evidence until fixed.
- **25 November:** Carried out a repository audit against the Build Overview (all 32 branches compared with `main`; tests and Bandit re-run locally: 12 passed, 1 PostgreSQL test skipped without a database, 97% coverage, no HIGH findings). Findings were shared with the team as a prioritised fix list.

## Documentation merged and independently reviewed

- [PR #10](https://github.com/fiveops-bcu/fiveops/pull/10), approved by Abdisalan and merged on **22 November 2026**, includes `docs/team-charter.md`, `docs/definition-of-done.md`, `docs/decision-log.md`, `docs/risk-log.md`, `docs/feedback-log.md`, `docs/evaluation.md`, both sprint summaries, this contribution file and an expanded `README.md`.
- The documents establish project governance and evaluation methods; the tutor's Viva 1 feedback and measured end-to-end evaluation results remain outstanding.
- This 24 November correction updates the record of previously merged work; it is not evidence that a new demonstration or test took place.

## In progress

- Create the GitHub Projects board, link issues #16 and #18–21, and close each issue with its merged PR.
- Check `protect-main`: enable stale-approval dismissal and conversation resolution now; require the Jenkins status check once Jenkins can post commit statuses (Fadumo's token, issue #19).
- Collect the Jenkins build link (Arkadiusz), GHCR image digest (Arkadiusz) and `/health` + `/version` output from TEST (Abdisalan) for one commit, and record them in [`release-trace-target-01-03-06.md`](../evidence/release-trace-target-01-03-06.md).
- Review the follow-up PRs for the production stage (same `deploy.yml`, database secret, rollback) and the approver list.

## Next toward Viva 2 (planned 4 December 2026)

1. Keep the Viva 1 feedback log pending until the tutor's actual feedback arrives; then record a sourced action or decision for each point (criterion 7).
2. Confirm the project-board URL, assign outstanding work and keep the Sprint 3 summary current ([`sprint-3.md`](../sprints/sprint-3.md)).
3. Run a versioned end-to-end change with Arkadiusz and Abdisalan and measure target 01; target is under 20 minutes excluding approved human wait.
4. Obtain independently verifiable pytest/Jenkins, Gitleaks, Bandit, Trivy, Vault and monitoring/rollback evidence.
5. Rehearse the demo with all members and prepare the 2-minute personal explanation.

## My part in the application

I lead project governance, requirements and acceptance, and coordinate application integration with the CI/CD, platform, security and operations streams. PR #6 carrying the Flask source was **authored by Arkadiusz**, even though application leadership was assigned to me. We must credit his actual code contribution accurately.

## Blockers and dependencies

- Abdisalan reports an operational Jenkins VMware VM with private Tailscale access and a Vagrant/VMware test VM in [PR #13](https://github.com/fiveops-bcu/fiveops/pull/13) and [PR #23](https://github.com/fiveops-bcu/fiveops/pull/23). Linked production deployment and CI evidence are still outstanding.
- Jenkins does not yet post commit statuses to GitHub (no checks on any merged PR), so `protect-main` cannot require a passing build.
- The production stage in `Jenkinsfile` passes no database secret to `deploy-prod.yml`, and that playbook has no rollback and reports `APP_VERSION: production` instead of the commit. Production deployment and Target 03 traceability depend on this fix.
- Aissatou's monitoring stack (branch `feature/operations-monitoring`) is not yet on `main`, and its Alertmanager receiver has no Teams destination.
- Original Viva 1 feedback is unavailable in the materials currently inspected; its content must not be fabricated.
- Monitoring, rollback and timed evaluation depend on working integrated services.
- PR #9's platform technical explanation needs a direct hand-off from Yasin to Abdisalan with a demo of the playbooks.

## My two-minute explanation (draft; adjust after validation)

> I lead FiveOps: I set up the organisation, repository and review workflow, wrote our pinned requirements and the baseline Ansible playbooks, and keep the governance and evaluation records. On 25 November I resolved the conflicts that let the CI/CD and platform work merge, gated production behind an explicit parameter, and audited the repository against our plan. That audit found four gaps, and I assigned each to an owner: production deployment, alert delivery, Jenkins reporting to GitHub, and monitoring on `main`. My evidence for Viva 2 is one release traced end to end, from commit to PR, build, image and the version running on the server, timed against our 20-minute target. Where we fall short, I will say so and show the next step.
