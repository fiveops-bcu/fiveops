# FiveOps Definition of Done

**Owner:** Yasin Mohammed Miah, Team Leader

**Status:** Proposed working criteria; apply to future PRs after team review

**Last updated:** 20 November 2026

## 1. Every repository change

- [ ] The task has an identifiable owner and a link to a board card or issue where available.
- [ ] The change is committed on a task branch, never pushed directly to protected `main`.
- [ ] The PR describes **what changed**, **why**, **how tested**, **evidence**, and **limitations / next steps**.
- [ ] No tokens, passwords, private keys, sensitive logs, real customer data or plaintext vault files are included.
- [ ] Another team member leaves a substantive written review, comments are resolved or recorded, and at least one required approval is granted.
- [ ] Supporting documentation and the contributor's record are updated when appropriate.
- [ ] The PR is merged using the repository's permitted strategy; the merge is traceable to the PR and commit.

## 2. Application and database code

- [ ] Relevant Flask endpoint/model behaviour is exercised by tests, including validation and common failures.
- [ ] `python -m pytest --cov=app --cov-fail-under=80` passes against the checked-out revision; save timestamp, commit and logs.
- [ ] PostgreSQL integration tests pass using `docker compose -f docker-compose.test.yml up --abort-on-container-exit --exit-code-from tests`, with database clean-up afterwards.
- [ ] Credentials are passed by environment/secure store, not embedded in code or logs.
- [ ] Database schema/init behaviour is understood; `db.create_all()` is a demonstration convenience and not a migration strategy.

## 3. CI/CD and security (release gate; not a claim of completion)

- [ ] Jenkins has actually run the checked-out `Jenkinsfile` from a pull request; attach the run URL and commit SHA.
- [ ] **Gitleaks:** the agreed full-history scan completes without a confirmed leaked secret.
- [ ] **pytest:** every test passes and coverage is at least 80%.
- [ ] **Bandit:** no unresolved HIGH-severity issue in `app/` (findings assessed, not silently ignored).
- [ ] **Trivy:** no unresolved fixable HIGH/CRITICAL container vulnerability under the documented scan policy; scan and database/tool versions are recorded.
- [ ] Required statuses are enforced by `protect-main` only after the actual checks have appeared and passed at least once.
- [ ] Publishing to GHCR, if implemented, occurs only from approved/trusted builds and produces a traceable commit-tagged image.
- [ ] No deployment or registry publishing is asserted solely because a stage was written in a Jenkinsfile.

## 4. Infrastructure and operations

- [ ] Provisioning is defined in Git (`Vagrantfile`, inventories and Ansible playbooks) and reproducible on the documented host.
- [ ] First provision ends with `failed=0`; second provision demonstrates `changed=0`, or any changes are explained with evidence.
- [ ] The test, production and monitoring environments are separately identified; credentials use Jenkins Credentials and encrypted Ansible Vault.
- [ ] Monitoring/alert rules are demonstrated rather than just listed in a plan.
- [ ] Rollback and idle-shutdown operation is measured against targets 02 and 08 when those facilities are implemented.

## 5. Documentation-only PRs

A documentation-only change needs correct facts, accurate links, no secrets, and an independent review. CI may be unavailable at early checkpoints; the PR must say so plainly. Do **not** state `Jenkins green` when no Jenkins run exists.

## 6. Acceptance authority and exceptions

The PR reviewer verifies the change; Yasin coordinates scope and evidence; Fadumo verifies security rules; Arkadiusz verifies CI configuration; Abdisalan confirms host provisioning; Aissatou confirms operational observations. Exceptions to a gate require an explicit decision and risk entry, including residual risk and compensating controls. No team member can retroactively claim an unperformed test as done.

**Evidence index:** `docs/sprints/sprint-2.md` and `docs/evaluation.md`.
