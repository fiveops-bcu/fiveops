
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
## Progress Update — 24 November 2026

### Completed Infrastructure Work

- Created and started the FiveOps Ubuntu 24.04 test VM using Vagrant and VMware Workstation.
- Confirmed connectivity between the Jenkins server (`192.168.174.128`) and test server (`192.168.174.129`).
- Created the `deploy` account and configured secure SSH public-key authentication.
- Verified Ansible connectivity using the ping module.
- Verified Ansible administrator access to the test server.
- Installed Docker and Docker Compose using Ansible.
- Executed `common.yml` successfully against the test environment.
- Verified Docker access without sudo for the deployment account.
- Completed an Ansible idempotency test with **6 successful tasks, 0 changes, 0 failures and 0 unreachable hosts**.
- Downloaded the latest FiveOps application source separately to overcome Git fetch timeouts.

### Work Remaining

- Develop and test the Ansible `deploy.yml` playbook.
- Deploy the Flask application and PostgreSQL database to the test VM.
- Verify the application `/health` endpoint.
- Integrate deployments with Jenkins and GHCR.
- Create and configure the production VM.
- Implement production approval, rollback and recovery testing.
- Collect screenshots and deployment evidence.

### Current Progress

Estimated Platform Engineer progress: approximately 60%.

The infrastructure for the test environment is working. Application deployment, production configuration and pipeline integration remain incomplete.

### Next Milestone

Deploy the FiveOps application to the test environment and verify a successful health-check response.
