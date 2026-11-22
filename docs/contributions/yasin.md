# Contribution record — Yasin Mohammed Miah (Team Leader)

**Last updated:** 20 November 2026

**Programme:** BSc (Hons) Computing (Level 6 Top-up), Birmingham City University

**Project:** FiveOps — CMP6237 / Evolving Ltd

## Done, with verifiable GitHub evidence

- **14 November:** Established initial repository content and documentation structure (README, PR template, `.gitattributes` and team-evidence folders). See [Git history](https://github.com/fiveops-bcu/fiveops/commits/main).
- **15 November:** Submitted pinned dependency files in [PR #1](https://github.com/fiveops-bcu/fiveops/pull/1), merged with recorded reviews.
- **15–16 November:** Reviewed Arkadiusz's changes, including [PR #2](https://github.com/fiveops-bcu/fiveops/pull/2), [PR #3](https://github.com/fiveops-bcu/fiveops/pull/3), [PR #4](https://github.com/fiveops-bcu/fiveops/pull/4), and [PR #6](https://github.com/fiveops-bcu/fiveops/pull/6). GitHub contains review submissions and approvals; these are **not** evidence that Jenkins executed successfully.
- **15–16 November:** Reviewed/approved [PR #5](https://github.com/fiveops-bcu/fiveops/pull/5), [PR #7](https://github.com/fiveops-bcu/fiveops/pull/7) and [PR #8](https://github.com/fiveops-bcu/fiveops/pull/8) as recorded in GitHub. The planned review rotation differs in places from actual recorded reviewers; this record states actual activity.
- **18 November:** Submitted [PR #9](https://github.com/fiveops-bcu/fiveops/pull/9) with `ansible/playbooks/common.yml` and `jenkins.yml`. **Abdisalan reviewed and approved**; the code belongs to the Platform Engineer's technical domain. Keep Git attribution unchanged and require Abdisalan to explain the playbooks at Viva 2.

## Prepared for peer review — not yet merged

- `docs/team-charter.md`, `docs/definition-of-done.md`, `docs/decision-log.md`, `docs/risk-log.md`, `docs/feedback-log.md`, and `docs/evaluation.md` (targets 01–08).
- `docs/sprints/sprint-1.md` and `docs/sprints/sprint-2.md` with accurately dated replan.
- This contribution record and an expanded `README.md`.

**Important:** Preparing these files locally is not equivalent to merging a PR. After they have been committed and reviewed, update this section with the actual PR number, date and review evidence.

## In progress

- Make reviewable assessment records available in GitHub, with Aissatou's written feedback and source references.
- Check the protected-main settings against the playbook; confirm stale-review dismissal, conversation resolution and Jenkins status enforcement when the check exists.
- Coordinate and evidence a real shared Jenkins build and its integration with the Flask application.

## Next toward Viva 2 (planned 4 December 2026)

1. Obtain the tutor's actual Viva 1 comments and record one feedback action/decision per point (criterion 7).
2. Confirm the project-board URL, assign outstanding work and publish an honest Sprint 2 hand-off.
3. Run a versioned end-to-end change with Arkadiusz and Abdisalan and measure target 01; target is under 20 minutes excluding approved human wait.
4. Obtain independently verifiable pytest/Jenkins, Gitleaks, Bandit, Trivy, Vault and monitoring/rollback evidence.
5. Rehearse the demo with all members and prepare the 2-minute personal explanation.

## My part in the application

I lead project governance, requirements and acceptance, and coordinate application integration with the CI/CD, platform, security and operations streams. PR #6 carrying the Flask source was **authored by Arkadiusz**, even though application leadership was assigned to me. We must credit his actual code contribution accurately.

## Blockers and dependencies

- Shared Jenkins service status and four-VM Vagrant build are not evidenced in the inspected repository.
- Original Viva 1 feedback is unavailable in the materials currently inspected; its content must not be fabricated.
- Monitoring, rollback and timed evaluation depend on working integrated services.
- PR #9's platform technical explanation needs a direct hand-off from Yasin to Abdisalan with a demo of the playbooks.

## My two-minute explanation (draft; adjust after validation)

> I coordinated the FiveOps repository and peer-review workflow, submitted our pinned requirements and added the missing common/Jenkins Ansible playbooks in PR #9, with Abdisalan's review. My current focus is finishing traceable checkpoint documentation and linking our next release to actual CI and evaluation evidence. Our main blocker is demonstrating a shared Jenkins pipeline and reproducible infrastructure rather than only having configuration in Git. Before Viva 2 I will record the tutor's feedback, measure a complete release and coordinate a documented hand-off across all five roles.
