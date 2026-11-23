# FiveOps secrets inventory

Prepared by: Fadumo Ibrahim
Updated: 23 November 2026
Related pull request: #14
Board issue: pending identification and linking.

This inventory documents planned arrangements. Ownership does not automatically grant access. Proposed access and storage must be verified with the team. No secret values are included.

| Secret name / ID | Purpose | Planned storage | Owner | Who can read / Access | Rotation |
| --- | --- | --- | --- | --- | --- |
| github-access | Jenkins repository access and reporting checks | Jenkins Credentials | Arkadiusz | Proposed: authorised Jenkins jobs and credential administrators; pending verification | 90 days proposed; team agreement pending |
| ghcr-push | Push container images to GHCR | Jenkins Credentials | Arkadiusz | Proposed: image-publishing Jenkins job and credential administrators; pending verification | 90 days proposed; team agreement pending |
| deploy-ssh | Ansible login to servers | Jenkins Credentials | Abdisalan | Proposed: deployment job and authorised credential administrators; pending verification | If leaked; routine schedule pending agreement |
| ansible-vault-pass | Decrypt Ansible Vault files | Jenkins Credentials for automation; recovery storage pending team agreement | Fadumo | Proposed: deployment job; named recovery custodians and administrator access pending verification | If leaked; routine schedule pending agreement |
| vault_db_password | Database access; separate values for test and production | Ansible Vault for each environment | Fadumo | Proposed: deployment process and application runtime for the relevant environment; pending verification | If leaked; routine schedule pending agreement |
| vault_ghcr_read_token | Allow servers to pull container images | Ansible Vault for test and production | Abdisalan | Proposed: deployment process and authorised image-pull processes on target servers; pending verification | 90 days proposed; team agreement pending |
| vault_grafana_admin_password | Grafana administrator access | Ansible Vault for monitoring | Aissatou | Proposed: monitoring provisioning process and named Grafana administrators; pending verification | If leaked; routine schedule pending agreement |

## Vault password storage and recovery

Jenkins Credentials is the proposed operational store so the authorised deployment job can decrypt the vault files.

The earlier password-manager entry was intended as a recovery copy if the Jenkins credential became unavailable. It was not evidence that a second copy had been created or approved.

Before creating a recovery copy, the team must agree its approved storage location, named custodians, access restrictions and recovery procedure. A personal password manager is not recorded as approved storage.

If the password is exposed, rotation must include rekeying the affected vault files and updating the approved operational and recovery copies.

## Verification and traceability

- Arkadiusz reported creating github-access; its configuration and effective access still require verification.
- Confirm all four Jenkins credential IDs, job access and administrator permissions on the shared instance.
- Confirm the vault password storage, access and recovery arrangement with the team.
- The proposed 90-day periods came from the Checkpoint 2 plan; team approval and implementation remain unverified.
- Identify the relevant GitHub board issue and link it to PR #14.
- Record confirmations and supporting evidence in this PR before marking these arrangements verified.

## Handling rules

- Never include passwords, tokens, private keys or recovery codes in this file.
- Do not send secret values through chat or email.
- Revoke or rotate exposed secrets, inform the owner and record the incident in the risk log.
