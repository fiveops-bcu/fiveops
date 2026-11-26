# Task 16 – Security Pipeline Validation

**Author:** Fadumo Ibrahim

**Role:** Quality and Security Engineer

**Date:** 25 November 2026

**Status:** Partially verified – Jenkins validation pending

## 1. Objective

Verify that Gitleaks, Bandit and Trivy operate correctly within the FiveOps Jenkins CI/CD pipeline and prevent insecure changes from progressing towards deployment.

## 2. Security tool versions

| Tool | Reported Jenkins version | Purpose |
|---|---|---|
| Gitleaks | 8.30.1 | Detect exposed secrets |
| Bandit | 1.9.4 | Identify Python security issues |
| Trivy | 0.69.3 | Detect container vulnerabilities |

Installation and availability were reported by Abdisalan. Independent pipeline validation remains outstanding.

## 3. Local security testing

- Gitleaks: Local repository history scan reported no detected secrets.
- Bandit: Scanned 108 lines of application code with no security findings.
- Bandit negative test: Detected a deliberately introduced HIGH severity issue and returned exit code 1.
- Trivy: Local filesystem scanning reported no HIGH or CRITICAL findings.
- Trivy negative test: Detected an insecure Dockerfile configuration and returned exit code 1.

Local Trivy testing used version 0.76.2. Container image scanning remains outstanding because Docker was unavailable in the local environment.

## 4. Proposed failure thresholds

| Tool | Failure condition |
|---|---|
| Gitleaks | Detection of an unapproved secret |
| Bandit | HIGH severity security finding |
| Trivy | Fixable HIGH or CRITICAL container vulnerability |

Final team agreement and Jenkins verification are required.

## 5. JSON reporting

The Jenkinsfile includes report generation and automatic artifact archiving for:

- `security-reports/gitleaks.json`
- `security-reports/bandit.json`
- `security-reports/trivy.json`

Local Bandit and Trivy JSON reports were generated. Successful generation and archiving of all three reports within Jenkins remain to be verified.

## 6. Jenkins investigation

Main build #10 failed because Gitleaks was unavailable in the Jenkins execution environment.

The pipeline stopped and subsequent stages were skipped, demonstrating that an execution failure prevented further pipeline progression.

Abdisalan subsequently reported that all three security tools had been installed.

A new validation build is required to confirm successful execution.

## 7. Outstanding validation

- [ ] Verify all three scanner versions within Jenkins.
- [ ] Complete the repository history scan.
- [ ] Verify Bandit HIGH severity failure behaviour.
- [ ] Verify Trivy container vulnerability failure behaviour.
- [ ] Confirm JSON report generation and archiving.
- [ ] Record scanner and vulnerability database versions.
- [ ] Investigate the GitHub HTTP 403 commit-status error.
- [ ] Confirm secure GHCR publishing credentials.
- [ ] Obtain team approval of security thresholds.

## 8. Evidence

- [Security pipeline implementation – PR #26](https://github.com/fiveops-bcu/fiveops/pull/26)
- [Task #16](https://github.com/fiveops-bcu/fiveops/issues/16)
- Local security testing records.
- Jenkins main build #10 investigation.

## 9. Conclusion

The security stages have been implemented, and local testing provides initial evidence of security detection and failure behaviour. Full Jenkins integration testing remains necessary before Task #16 can be recorded as complete.
