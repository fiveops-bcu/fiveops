# Contribution record: Fadumo Ibrahim (Quality and Security Engineer)

## Done, with evidence

### 16 November 2026 — Repository setup

- Enabled two-factor authentication and accessed the FiveOps repository.
- Cloned the repository, configured my Git identity and created the `contrib-fadumo` branch.

### 24–25 November 2026 — Security implementation and testing

- Reviewed the deployment playbook, security configuration and project evaluation requirements.
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

### 27 November 2026 — Integrated security validation

- Investigated Jenkins main build #18, which failed with exit code 2 during Trivy execution.
- Distinguished the Trivy execution failure from a vulnerability threshold failure.
- Identified a separate GitHub HTTP 403 commit-status error associated with personal access token permissions.
- Manually initiated Jenkins main build #19 to validate the integrated CI/CD pipeline.
- Confirmed that build #19 completed successfully in 58 seconds using commit `12e7093`.
- Verified successful execution of the Gitleaks security scan, automated Docker tests, Bandit security scan and Trivy container image scan.
- Confirmed that all 13 automated tests passed without failures.
- Verified that security scanning completed successfully before container image publication and TEST deployment.
- Confirmed automatic generation and archiving of security reports and build artifacts.

### Vulnerability remediation and residual risk

- Reviewed the Trivy container vulnerability results and verified remediation of the identified fixable vulnerabilities affecting `libzstd1` and `zlib1g`.
- Confirmed remediation of CVE-2026-124851 and CVE-2026-85091.
- Verified the updated package versions:
  - `libzstd1`: 1.5.7+dfsg-1+deb13u1
  - `zlib1g`: 1.3.dfsg+really1.3.1-1+deb13u1
- Confirmed that the final Trivy scan reported zero fixable HIGH-severity vulnerabilities and zero CRITICAL vulnerabilities.
- Identified 53 remaining unfixed HIGH-severity findings associated with 13 distinct CVEs.
- Recognised that the `--ignore-unfixed` configuration allows deployment when no applicable security fixes are available. These findings remain a residual security risk and require continued monitoring.
- Verified that passing the configured security gate does not mean that the container image is entirely vulnerability-free.

### Container publication and TEST deployment verification

- Verified successful publication of the container image to GitHub Container Registry (GHCR).
- Confirmed generation and archiving of the SHA-256 image digest, supporting image integrity and deployment traceability.
- Reviewed the GHCR authentication process, including disabled shell tracing and temporary Docker credential configuration.
- Identified Docker's temporary unencrypted credential storage warning as an area for further security review.
- Verified successful Ansible deployment to the TEST environment.
- Confirmed successful PostgreSQL and application configuration.
- Verified that the application health check completed successfully.
- Confirmed that the deployment recorded the last successful application version and deployment timestamp.
- Reviewed the Ansible execution summary: `ok=13`, `changed=5`, `unreachable=0`, `failed=0`.
- Confirmed that the Production Approval and Deploy to PROD stages were skipped. No production deployment was performed during build #19.

### Evidence

- [Security pipeline implementation — PR #26](https://github.com/fiveops-bcu/fiveops/pull/26)
- [FiveOps GitHub repository](https://github.com/fiveops-bcu/fiveops)
- Jenkins main build #18 — failure investigation.
- Jenkins main build #19 — successful integrated security validation and TEST deployment.
- Jenkins pipeline stage screenshots.
- Local positive and negative security testing records.
- Trivy vulnerability remediation and residual-risk evidence.
- Archived Jenkins build #19 artifacts:
  - `coverage.xml`
  - `bandit.json`
  - `gitleaks.json`
  - `trivy.json`
  - `image-digest.txt`

## In progress

- Task #16: Integrated security scanning successfully validated in Jenkins build #19. Final task documentation and formal closure remain to be confirmed.
- Complete the Target 04 access audit covering GitHub, Jenkins and virtual machine accounts.
- Investigate the GitHub HTTP 403 commit-status error with the team.
- Review Jenkins authorization settings against the principle of least privilege.
- Verify secure management of GHCR credentials and encrypted Ansible Vault configuration.
- Document residual container vulnerabilities and recommended monitoring arrangements.
- Consolidate security evidence for project evaluation and Viva 2.

## Next, towards Viva 2

- Complete the Target 04 access-control assessment.
- Confirm repository permissions, branch protection, individual accounts and two-factor authentication arrangements.
- Document the agreed scanner versions and vulnerability database information.
- Collect integrated negative-test evidence demonstrating that detected security violations prevent image publication and deployment.
- Review residual vulnerability management and future remediation requirements.
- Complete outstanding pull request reviews and provide constructive security feedback.
- Organise redacted screenshots, security reports and Jenkins build references.
- Prepare to explain and defend security gate implementation, vulnerability remediation, testing outcomes and remaining limitations during Viva 2.

## Current blockers

- GitHub repository administration settings require assistance from an authorised administrator.
- Resolution of the GitHub HTTP 403 commit-status error has not yet been confirmed.
- Jenkins least-privilege authorization requires further review.
- Target 04 cannot yet be recorded as fully passed.
- Integrated negative security gate testing requires further evidence.
- Remaining unfixed vulnerabilities require monitoring until suitable patches become available.

## My part in the web app

As Quality and Security Engineer, my responsibilities include verifying the security controls that protect the support-ticket application, its source code, dependencies, credentials and automated delivery pipeline.

My contribution includes implementing automated security gates, conducting controlled security tests, reviewing access controls, verifying vulnerability remediation and collecting evidence of successful security validation before application deployment.

The successful execution of Jenkins build #19 demonstrates that automated security scanning, application testing, container publication and TEST deployment can operate together within the integrated CI/CD pipeline. However, continued vulnerability monitoring, access-control improvements and further negative testing remain necessary to strengthen the overall security posture.
