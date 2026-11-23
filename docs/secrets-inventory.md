# FiveOps secrets inventory

Prepared by: Fadumo Ibrahim
Updated: 23 November 2026
Related pull request: #14
Board issue: pending identification and linking.

Source: Yasin Miah, FiveOps Checkpoint 2 plan, version 1, 14 November 2026, page 7.

Storage and rotation below follow the plan. Actual access and implementation remain subject to verification. Ownership does not automatically grant access. No secret values are included.

| Secret name / ID | Purpose | Storage specified in plan | Owner | Who can read / Access | Rotation specified in plan |
| --- | --- | --- | --- | --- | --- |
| github-access | Repository access and reporting checks | Jenkins Credentials | Arkadiusz | Proposed: authorised Jenkins jobs and credential administrators; pending verification | 90 days; current team confirmation pending |
| ghcr-push | Push images to GHCR | Jenkins Credentials | Arkadiusz | Proposed: publishing job and credential administrators; pending verification | 90 days; current team confirmation pending |
| deploy-ssh | Ansible login to servers | Jenkins Credentials | Abdisalan | Proposed: deployment job and authorised credential administrators; pending verification | If leaked |
| ansible-vault-pass | Decrypt vault files | Jenkins Credentials and Fadumo's password manager | Fadumo | Proposed: deployment job; administrator access and recovery custodians pending verification | If leaked |
| vault_db_password | Database access; separate test and production values | Ansible Vault for each environment | Fadumo | Proposed: deployment process and relevant application runtime; pending verification | If leaked |
| vault_ghcr_read_token | Pull container images | Ansible Vault for test and production | Abdisalan | Proposed: deployment and authorised image-pull processes; pending verification | 90 days; current team confirmation pending |
| vault_grafana_admin_password | Grafana administrator access | Ansible Vault for monitoring | Aissatou | Proposed: provisioning process and named Grafana administrators; pending verification | If leaked |

## Vault password storage and recovery

Page 7 of Yasin's plan specifies both Jenkins Credentials and Fadumo's password manager for ansible-vault-pass.

The Jenkins copy supports automated decryption. The password-manager copy is intended for recovery if the operational copy becomes unavailable. This explains the purpose of keeping both; the plan does not specify a detailed recovery procedure.

The team must verify actual storage, authorised users, password-manager access controls, recovery custodians and the recovery procedure. This inventory does not claim those checks are complete or grant additional access.

If exposed, rotate the password by rekeying affected vault files and updating the operational and recovery copies.

## Rotation and traceability

- The 90-day periods for github-access, ghcr-push and vault_ghcr_read_token are specified in Yasin's plan.
- Current team confirmation, rotation dates and implementation still require verification.
- Arkadiusz reported creating github-access; its configuration and effective access remain to be checked.
- Verify all four Jenkins credential IDs and access restrictions on the shared instance.
- Obtain the relevant board issue link from Yasin or Abdisalan and link it to PR #14.
- Record team confirmations and Jenkins evidence before marking these items verified.

## Handling rules

- Never include passwords, tokens, private keys or recovery codes in this file.
- Do not send secret values through chat or email.
- Revoke or rotate exposed secrets, inform the owner and record the incident in the risk log.
