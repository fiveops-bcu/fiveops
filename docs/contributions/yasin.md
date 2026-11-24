# Contribution record — Yasin Mohammed Miah (Team Leader)

**Last updated:** 24 November 2026

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

## Documentation merged and independently reviewed

- [PR #10](https://github.com/fiveops-bcu/fiveops/pull/10), approved by Abdisalan and merged on **22 November 2026**, includes `docs/team-charter.md`, `docs/definition-of-done.md`, `docs/decision-log.md`, `docs/risk-log.md`, `docs/feedback-log.md`, `docs/evaluation.md`, both sprint summaries, this contribution file and an expanded `README.md`.
- The documents establish project governance and evaluation methods; the tutor's Viva 1 feedback and measured end-to-end evaluation results remain outstanding.
- This 24 November correction updates the record of previously merged work; it is not evidence that a new demonstration or test took place.

## In progress

- Collect actual reviewer comments and independent evidence for integration; request Aissatou's written review on the next Team Leader documentation PR.
- Check the protected-main settings against the playbook; confirm stale-review dismissal, conversation resolution and Jenkins status enforcement when the check exists.
- Coordinate and evidence a real shared Jenkins build and its integration with the Flask application.

## Next toward Viva 2 (planned 4 December 2026)

1. Keep the Viva 1 feedback log pending until the tutor's actual feedback arrives; then record a sourced action or decision for each point (criterion 7).
2. Confirm the project-board URL, assign outstanding work and publish an honest Sprint 2 hand-off.
3. Run a versioned end-to-end change with Arkadiusz and Abdisalan and measure target 01; target is under 20 minutes excluding approved human wait.
4. Obtain independently verifiable pytest/Jenkins, Gitleaks, Bandit, Trivy, Vault and monitoring/rollback evidence.
5. Rehearse the demo with all members and prepare the 2-minute personal explanation.

## My part in the application

I lead project governance, requirements and acceptance, and coordinate application integration with the CI/CD, platform, security and operations streams. PR #6 carrying the Flask source was **authored by Arkadiusz**, even though application leadership was assigned to me. We must credit his actual code contribution accurately.

## Blockers and dependencies

- Abdisalan reports an operational Jenkins VMware VM with private Tailscale access and a Vagrant/VMware test VM in [PR #13](https://github.com/fiveops-bcu/fiveops/pull/13) and [PR #23](https://github.com/fiveops-bcu/fiveops/pull/23). Full four-VM provisioning, application deployment and linked production-style CI evidence are still outstanding.
- Original Viva 1 feedback is unavailable in the materials currently inspected; its content must not be fabricated.
- Monitoring, rollback and timed evaluation depend on working integrated services.
- PR #9's platform technical explanation needs a direct hand-off from Yasin to Abdisalan with a demo of the playbooks.

## My two-minute explanation (draft; adjust after validation)

> I coordinated the FiveOps repository and peer-review workflow, submitted our pinned requirements and added the missing common/Jenkins Ansible playbooks in PR #9, with Abdisalan's review. My checkpoint documentation was merged in PR #10 following Abdisalan's approval; my current focus is linking a version-controlled change to actual CI, deployment and evaluation evidence. Our main blocker is demonstrating a shared Jenkins pipeline and reproducible infrastructure rather than only having configuration in Git. Before Viva 2 I will record the tutor's feedback, measure a complete release and coordinate a documented hand-off across all five roles.
