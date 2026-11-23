# FiveOps secrets inventory



Prepared by: Fadumo Ibrahim

Updated: 23 November 2026



This inventory records the planned secrets from the Checkpoint 2 instructions. Their creation and storage still need to be verified with the owners. No secret values are recorded here.



| Secret name / ID | Purpose | Planned storage | Owner | Rotation |

| --- | --- | --- | --- | --- |

| github-access | Jenkins repository access and reporting checks | Jenkins Credentials | Arkadiusz | Every 90 days |

| ghcr-push | Push container images to GHCR | Jenkins Credentials | Arkadiusz | Every 90 days |

| deploy-ssh | Ansible login to servers | Jenkins Credentials | Abdisalan | If leaked |

| ansible-vault-pass | Decrypt Ansible Vault files | Jenkins Credentials and Fadumo's password manager | Fadumo | If leaked |

| vault_db_password | Database access; different passwords for test and production | Ansible Vault for each environment | Fadumo | If leaked |

| vault_ghcr_read_token | Allow servers to pull container images | Ansible Vault for test and production | Abdisalan | Every 90 days |

| vault_grafana_admin_password | Grafana administrator access | Ansible Vault for monitoring | Aissatou | If leaked |



## Handling rules



- Never include passwords, tokens, private keys or recovery codes in this file.

- Do not send secret values through chat or email.

- If a secret is exposed, revoke or rotate it immediately, inform its owner and record the incident in the risk log.

- Confirm actual storage and access permissions with each owner before marking the setup complete.

