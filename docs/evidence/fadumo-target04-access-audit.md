# Target 04 – Access Control and Least Privilege Audit

**Auditor:** Fadumo Ibrahim  
**Role:** Quality and Security Engineer  
**Project:** FiveOps – Evolving Ltd  
**Audit date:** 25 November 2026  
**Status:** Partially verified – further validation required

## 1. Audit objective

The purpose of this audit is to verify that GitHub, Jenkins and virtual machine access is managed through individual accounts, appropriate permissions and two-factor authentication wherever supported.

The audit supports Target 04 of the FiveOps evaluation plan.

## 2. Access control findings

| Control | Observation | Status |
| --- | --- | --- |
| GitHub individual account | Personal account used to access the repository. | Verified for own account |
| GitHub two-factor authentication | Enabled on my individual account. | Verified for own account |
| Main branch protection | Direct commits restricted; changes submitted through pull requests. | Verified for own account |
| Repository administration | Repository administration options unavailable to my account. | Restricted access observed |
| Jenkins individual accounts | Account and authorization settings inspected. | Further verification required |
| Jenkins least privilege | Broad permissions for authenticated users identified as a security concern. | Improvement required |
| Jenkins administrator account | Build history shows activity initiated by an account named admin. Shared use has not been established. | Further verification required |
| Jenkins credentials | Existing GitHub, SSH, sudo and Ansible Vault credential entries inspected without accessing secret values. | Partially verified |
| GHCR publishing | Dedicated publishing credential not yet verified. | Pending |
| Virtual machine access | Individual accounts, groups and sudo permissions require further auditing. | Pending |
| Team-wide 2FA | Confirmation required for all relevant team members. | Pending |

## 3. Identified risks and recommendations

### Excessive Jenkins permissions

Broad permissions may allow authenticated users to modify pipeline configurations or access sensitive administrative functions beyond their responsibilities.

Recommendation: Implement role-based or matrix-based authorization and assign permissions according to individual responsibilities.

### Administrator accountability

An administrator account appears in Jenkins build history. This does not establish whether the account is shared.

Recommendation: Confirm administrator account ownership and ensure privileged activities are attributable to named individuals.

### Credential protection

Jenkins credentials are present, but their effective permissions and availability to untrusted builds require further verification.

Recommendation: Restrict credential access to authorised jobs, apply least privilege and prevent secrets from appearing in repositories or build logs.

### GitHub integration

An HTTP 403 commit-status error was identified during Jenkins investigation.

Recommendation: Review the integration token permissions and grant only the access required to publish commit statuses.

## 4. Evidence

- GitHub protected branch notification.
- GitHub restricted repository settings.
- Jenkins account and authorization inspection.
- Jenkins credential inventory inspection.
- Jenkins build history.
- Security pipeline [PR #26](https://github.com/fiveops-bcu/fiveops/pull/26).

Redacted screenshots will be added following evidence review. No passwords, private keys or token values are included in this audit.

## 5. Outstanding validation

- Confirm GitHub team membership and assigned roles.
- Verify two-factor authentication across relevant team accounts.
- Confirm Jenkins administrator ownership and individual permissions.
- Review VM users, groups and sudo privileges with Abdisalan.
- Verify GHCR credential permissions and trusted-build restrictions.
- Retest access controls following approved configuration changes.

## 6. Audit conclusion

The initial audit demonstrates that GitHub branch protection and restricted repository administration are operating for the audited account.

However, Jenkins least privilege, administrator accountability, team-wide two-factor authentication and virtual machine access require further verification.

Target 04 remains partially verified and cannot yet be recorded as passed.

## 7. References

- [FiveOps evaluation plan](../evaluation.md)
- [FiveOps definition of done](../definition-of-done.md)
- [FiveOps secrets inventory](../secrets-inventory.md)
- [NIST SP 800-53 Rev. 5 – Security and Privacy Controls](https://doi.org/10.6028/NIST.SP.800-53r5)
- [Jenkins security documentation](https://www.jenkins.io/doc/book/security/)
