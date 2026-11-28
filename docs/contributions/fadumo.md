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

## 28 November 2026 — Security validation and remediation

### Bandit negative security test

- Created an isolated test branch, `test/security-bandit-negative`, to validate the automated Bandit security gate without introducing insecure code into main.
- Introduced a controlled Python security issue using `subprocess` with `shell=True`.
- Jenkins Build #2, executed on 27 November 2026, detected a HIGH-severity B602 issue associated with CWE-78.
- The security gate correctly failed the build and prevented Docker image creation.
- Application tests reported no failures, demonstrating that functional testing alone is insufficient to identify security weaknesses.
- Test commit: [110eaa2](https://github.com/fiveops-bcu/fiveops/commit/110eaa2).
- Result: PASS — expected security rejection demonstrated.

### Bandit remediation and recovery test

- Removed the temporary insecure Python file on 28 November 2026.
- Jenkins Build #3 completed successfully in 31 seconds with no application test failures.
- Security reports for Bandit, Gitleaks and Trivy were generated and archived.
- Cleanup commit: [d4676ae](https://github.com/fiveops-bcu/fiveops/commit/d4676ae).
- Preserved Jenkins Builds #2 and #3 using the permanent build retention option and added descriptions explaining their purpose and results.
- Result: PASS — successful pipeline recovery following remediation.

### Gitleaks negative security test

- Created a separate test branch, `test/security-gitleaks-negative`, to evaluate secret detection.
- Used synthetic test data only. No genuine credentials were introduced.
- Initial test commit: [db0639c](https://github.com/fiveops-bcu/fiveops/commit/db0639c).
- Updated test commit: [857a016](https://github.com/fiveops-bcu/fiveops/commit/857a016).
- Jenkins Builds #3 and #4 completed successfully rather than producing the expected security rejection.
- Result: INCONCLUSIVE — negative security gate behaviour was not demonstrated.
- Removed the temporary test file following validation.
- Neither security test branch is intended to be merged into main.

### Security validation summary

| Security control | Result |
| --- | --- |
| Bandit normal scan | Passed |
| Bandit negative test | Passed — build correctly blocked |
| Bandit recovery test | Passed |
| Gitleaks normal scan | Passed |
| Gitleaks negative test | Inconclusive |
| Trivy image security gate | Passed under the configured vulnerability policy |
| Integrated TEST deployment | Passed in main Build #19 |

### Critical evaluation and remaining recommendations

The Bandit negative and recovery tests demonstrate that automated security controls can prevent insecure code from progressing through the CI/CD pipeline and allow development to resume following remediation.

However, the Gitleaks negative test highlights a limitation in the current validation evidence. A successful scan does not guarantee that every possible secret format will be detected. Further investigation of detection rules, exclusions and test fixtures is recommended.

The remaining unfixed container vulnerabilities should continue to be monitored. Jenkins authorization, credential permissions and repository administration controls also require further verification before Target 04 can be recorded as fully satisfied.

Overall, the implemented security gates provide an additional layer of protection beyond functional testing. The results demonstrate practical security validation, remediation and recovery while recognising the limitations of automated scanning.

### Evidence retained

- Jenkins main Build #19 and archived security reports.
- Bandit negative Build #2 and recovery Build #3.
- GitHub test and remediation commits.
- Gitleaks negative test build results.
- GitHub contribution and pull request history.

All deliberately introduced security test files were removed from the current versions of their isolated test branches. Synthetic test data remains in Git history, and these branches must not be merged into main.



