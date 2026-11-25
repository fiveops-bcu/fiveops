# Contribution record: Fadumo Ibrahim (Quality and Security Engineer)



## Done, with evidence

- 16 November 2026: Enabled two-factor authentication and accessed the FiveOps repository.

- 16 November 2026: Cloned the repository, configured my Git identity and created the contrib-fadumo branch.

- - 24–25 November 2026: Reviewed the deployment playbook, security configuration and project evaluation requirements.

- Completed local Gitleaks repository scanning to check for exposed secrets.

- Installed and tested Bandit 1.9.4 against the application source code. The scan reported no security findings.

- Conducted controlled positive and negative Bandit tests to verify that HIGH-severity findings trigger a non-zero exit code.

- Completed local Trivy filesystem and misconfiguration scanning, including controlled failure testing.

- Generated JSON security reports for Bandit and Trivy.

- Implemented automated Gitleaks, Bandit and Trivy security stages in the Jenkinsfile, including failure thresholds and automatic JSON report archiving.

- Created [PR #26](https://github.com/fiveops-bcu/fiveops/pull/26), which was merged into main on 25 November 2026.

- Investigated Jenkins security branch build #1 and main build #10. Identified that Gitleaks was unavailable in the Jenkins execution environment.

- Confirmed that the pipeline stopped following the Gitleaks execution failure, preventing subsequent stages from running without security verification.

- Collaborated with Abdisalan to confirm installation of Gitleaks 8.30.1, Bandit 1.9.4 and Trivy 0.69.3 on the Jenkins server.

- Inspected Jenkins user accounts, authorization settings and credential inventory as part of the Target 04 access audit.

- Identified unrestricted permissions for authenticated Jenkins users as a least-privilege concern requiring further review.

- Identified a GitHub HTTP 403 commit-status error requiring investigation of token permissions.

- Coordinated with Arkadiusz regarding Task #16 security verification and outstanding integration requirements.

- Evidence: [Security pipeline PR #26](https://github.com/fiveops-bcu/fiveops/pull/26) and local security testing records. 



## In progress

- Task #16: Validate Gitleaks, Bandit and Trivy within the Jenkins pipeline following the installation reported by Abdisalan.
- Confirm security failure thresholds and verify automatic JSON report generation and archiving.
- Investigate the GitHub HTTP 403 commit-status error with the team.
- Complete the Target 04 access audit covering GitHub, Jenkins and virtual machine accounts.
- Coordinate secure GHCR publishing credentials and encrypted Ansible Vault configuration.

## Next, towards Viva 2

- Run a full Jenkins validation build once the server becomes available.
- Verify that security failures prevent subsequent pipeline stages from executing.
- Confirm the agreed scanner versions and document the vulnerability database version.
- Review team permissions, branch protection, individual accounts and two-factor authentication.
- Complete outstanding pull request reviews and provide constructive security feedback.
- Collect redacted screenshots, security reports and build references for Viva 2.

## Current blockers

- Jenkins validation is pending server availability.
- GitHub repository administration settings require assistance from an authorised administrator.
- GHCR publishing credentials and final security gate approval remain outstanding.
- Target 04 cannot yet be recorded as passed.



## My part in the web app

- Check the controls that protect the support-ticket app, its secrets and its delivery pipeline.



## Blockers

- Jenkins tasks depend on server availability and coordination with Arkadiusz and Abdisalan.

- Team permissions and branch protection still need to be verified.


## Progress update: 23 November 2026

### Completed
- Secret-file ignore rules merged through PR #8. All nine sample paths passed git check-ignore.
- On 22 November, Gitleaks 8.30.1 scanned 41 commits across fetched branches and reported no leaks.
- On 23 November, a direct push to main was rejected with GH013: changes must go through a pull request. Removed the local empty test commit afterwards.
- Confirmed the test configuration contains an 80% coverage threshold. This was a configuration check, not a successful Jenkins run.

### Awaiting review
- PR #14 adds the planned seven-secret inventory. Actual storage and permissions still require confirmation with the owners.

### Remaining work
- Coordinate Gitleaks, Bandit and Trivy pipeline gates with Arkadiusz; no references appeared in the three configuration files checked.
- Verify team-wide 2FA and push protection with Yasin.
- Coordinate Jenkins credentials, encrypted vault files and access permissions with the team.
- Review Aissatou's pull request and leave written feedback.
- Add screenshots to docs/evidence through a pull request. Screenshots are collected separately but are not yet linked here.

This update supersedes the earlier planned status for the ignore rules, secret scan and branch-protection check.
