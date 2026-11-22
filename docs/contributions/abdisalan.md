
# Abdisalan Mohamed — Platform Engineer

Project: FiveOps — DevOps and Enterprise Automation
Progress date: 22 November 2026

## 1. Completed Tasks

- Installed and configured Jenkins on the BCU Ubuntu VMware VM.
- Verified that Jenkins is running successfully.
- Configured Docker access for the Jenkins service account.
- Enabled and tested SSH connectivity.
- Verified connectivity between Windows and Ubuntu.
- Configured Windows port forwarding for Jenkins.
- Configured private HTTPS access using Tailscale Serve.
- Successfully tested the Jenkins HTTPS endpoint.
- Set up remote access for Arkadiusz and Yasin.

## 2. GitHub Contributions

- PR #5: Vagrant infrastructure configuration (merged).
- Compared existing Ansible playbooks with merged PR #9.

## 3. Work in Progress

- Fadumo's remote Jenkins access.
- GHCR integration and permissions.
- Ansible deploy.yml configuration.
- Test and production deployment.
- Automatic rollback and recovery testing.
- Infrastructure idempotency testing.

## 4. Technical Limitations

Jenkins currently runs on the BCU Ubuntu VMware VM.
The planned four-VM infrastructure has not yet been
verified.

Remote access depends on the Windows host, VMware
guest and Tailscale services remaining operational.

## 5. Next Actions

1. Give Fadumo access to Jenkins.
2. Coordinate security credentials with Fadumo.
3. Support Arkadiusz's Jenkins pipeline integration.
4. Implement and test Ansible deployment.
5. Collect screenshots, logs and evaluation evidence.
