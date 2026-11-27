# Abdisalan Mohamed - Platform Engineer Contribution Record
# Record TEST deployment and monitoring handoff and the description Related to #18.

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

## Progress Update — 25 November 2026

### Completed and Verified

- Deployed the FiveOps Flask application and PostgreSQL to the VMware test VM using Ansible.
- Verified application health with HTTP 200 and {"status":"ok"}.
- Configured Jenkins SSH, sudo and Ansible Vault credentials.
- Successfully tested Jenkins-triggered Ansible deployment.
- Configured the GHCR publishing credential `ghcr-push` in Jenkins.
- Verified Gitleaks 8.30.1 runs under the Jenkins service account.
- Created PR #31 for Jenkins image transfer and Ansible integration.
- Created PR #33 for draft automatic rollback functionality.
- Added Ansible block/rescue recovery logic and release logging.
- Passed Ansible syntax and Git formatting checks.
- Verified the previous Docker image is available on the test VM.
- Created and verified the root-protected Compose recovery backup.
- Created a PostgreSQL backup and verified its archive catalogue.
- Configured Tailscale on the test VM and created an individual Linux account for the Operations Engineer.

### Outstanding Work

- Complete and measure a controlled automatic rollback test.
- Integrate GHCR image publishing and deployment with Arkadiusz.
- Provision production and monitoring VMs when resources permit.
- Complete infrastructure rebuild evidence and deployment measurements.
- Obtain reviews and approval for PR #31 and PR #33.

### Pull Requests

- PR #25: Ansible test deployment (merged).
- PR #31: Jenkins–Ansible integration (open).
- PR #33: Automatic rollback implementation (open; testing pending).

No successful automatic rollback or full production deployment is claimed at this stage.

## Platform Engineering Progress - 27 November 2026

### 1. TEST Infrastructure and GHCR Deployment

Verified the operational VMware TEST environment,
Jenkins and Ansible deployment integration, PostgreSQL
persistent storage and application health.

- TEST server: fiveops-test
- TEST IP: 192.168.174.129
- Previous healthy release: b219a76
- Latest verified release: 12e7093
- PostgreSQL version: 17
- Persistent database volume: fiveops_pgdata

Verified release records:

```text
2026-11-26T20:35:59Z DEPLOY b219a76 SUCCESS
2026-11-27T17:51:46Z DEPLOY 12e7093 SUCCESS
```

Both GHCR images and their respective Compose
configurations were available for recovery testing.

### 2. Secure Production Deployment Integration

Implemented the production integration changes in:

- Branch: platform/production-integration
- Commit: bfd1775

Implementation includes:

- Shared Ansible deployment logic.
- Immutable container image digest support.
- Separate production credential references.
- Restricted production approval.
- Application health and version validation.
- Automatic rollback logic.
- Production inventory safety validation.

Ansible syntax and Jenkinsfile validation passed.

A negative safety test correctly rejected an empty
production inventory.

Live production deployment remains unverified due
to host memory limitations. Production must remain
disabled until configuration, review and runtime
validation are completed.

### 3. PostgreSQL Backup and Recovery

Created and validated a fresh PostgreSQL backup.

Performed logical database restoration into separate
temporary databases without overwriting the live
FiveOps database.

Populated recovery test results:

```text
RESTORATION SUCCESSFUL
Recovery duration: 874 milliseconds
```

- Two fictional customer records recovered.
- Three fictional support tickets recovered.
- Customer-ticket relationships preserved.
- Database constraints restored.
- Live database record counts remained unchanged.
- Both temporary recovery databases removed.

SHA-256 integrity verification:

```text
TABLE: customer
DATA INTEGRITY: PASS

TABLE: ticket
DATA INTEGRITY: PASS

ALL TABLE DATA INTEGRITY CHECKS PASSED
```

The measured result demonstrates logical recovery
of a small synthetic dataset within the existing
PostgreSQL instance, not full server disaster recovery.

### 4. Ansible Configuration Drift Investigation

Identified an outdated TEST inventory address and
resolved connectivity using an environment-specific
inventory override.

Original Ansible check-mode result:

```text
test : ok=6 changed=1 unreachable=0 failed=0
```

The predicted change concerned the Jenkins deployment
public key.

Compared the repository key, authorised TEST key
and active Jenkins credential fingerprints.

A temporary Jenkins diagnostic pipeline confirmed
that the active Jenkins SSH credential matched
the currently authorised TEST deployment key.

No private keys were exposed or changed.

### 5. Environment-Specific Deployment Configuration

Implemented the deploy_public_key_file variable
to support environment-specific public-key selection.

- Branch: platform/environment-specific-deploy-key
- Commit: 37a6207

Updated README.md with configuration instructions
and validation evidence.

The legacy public-key fallback remains for backwards
compatibility and must be verified before use.

### 6. Infrastructure Idempotency

Corrected Ansible check-mode result:

```text
test : ok=6 changed=0 unreachable=0 failed=0
```

First actual provisioning run:

```text
Fri Nov 27 07:27:50 PM UTC 2026
test : ok=6 changed=0 unreachable=0 failed=0
```

Second actual provisioning run:

```text
Fri Nov 27 07:28:57 PM UTC 2026
test : ok=6 changed=0 unreachable=0 failed=0
```

Final application verification:

```text
Fri Nov 27 07:29:26 PM UTC 2026
{"status":"ok"}
{"version":"12e7093"}
```

Both actual provisioning executions demonstrated
idempotency on the existing TEST virtual machine.

A fresh VM rebuild remains outstanding.

### 7. Team Collaboration

Coordinated with Arkadiusz regarding Jenkins
deployment credentials, release verification
and controlled recovery testing.

Coordinated with Aissatou regarding Prometheus,
Grafana, Alertmanager and planned alert tests.

Monitoring readiness was reported by Aissatou.
Formal alert notification and application rollback
timing tests remain outstanding.

### 8. Evaluation Status

- Target 01: Deployment timing evidence pending.
- Target 02: Database recovery verified; three
  timed application rollback drills pending.
- Target 03: Two identifiable GHCR releases verified.
- Target 04: Deployment credential verification
  completed; wider access audit pending.
- Target 05: Ansible idempotency demonstrated;
  fresh VM rebuild pending.
- Target 06: CI/CD testing evidence requires
  confirmation from the responsible engineer.
- Target 07: Three alert notification tests pending.
- Target 08: Automated idle shutdown verification
  pending.

### 9. Outstanding Platform Engineering Work

- Complete coordinated application rollback drills.
- Support coordinated alert notification testing.
- Complete fresh VM rebuild verification.
- Complete production runtime validation when
  sufficient infrastructure resources are available.
- Resolve remaining inventory portability issues.
- Obtain peer review of submitted technical changes.
- Prepare demonstration and Viva 2 evidence.
