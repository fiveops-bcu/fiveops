# FiveOps - Operations Engineer Contribution

**Name:** Aissatou Diallo

**Module:** CMP6237 - DevOps and Enterprise Automation

**Branch:** feature/operations-monitoring

## Role and Responsibilities

My role focuses on monitoring the Evolving Ltd
application, identifying service failures and
supporting recovery when deployments fail.

My assigned responsibilities include:

- Configuring Prometheus and Grafana.
- Configuring alert rules and Alertmanager.
- Centralising logs using Loki and Grafana Alloy.
- Developing and documenting rollback procedures.
- Planning PostgreSQL backup and recovery tests.
- Configuring scheduled shutdowns for idle resources.
- Recording monitoring and recovery test results.

## Progress - 23 November 2026

- Joined the FiveOps GitHub organisation.
- Cloned the team repository.
- Configured my Git identity.
- Created the operations monitoring branch.
- Prepared the initial monitoring configuration.

## Progress - 26 November 2026

### Completed

- Developed the Ansible Node Exporter installation playbook.
- Configured Prometheus server monitoring.
- Configured Blackbox Exporter application health checks.
- Created server and application failure alert rules.
- Configured Alertmanager for alert management.
- Created a Docker Compose monitoring stack.
- Configured Grafana dashboard provisioning.
- Validated the Grafana dashboard JSON syntax.
- Documented the rollback and recovery procedure.
- Created a monitoring and recovery test plan.
- Committed and pushed monitoring files to GitHub.
- Integrated the latest main branch changes locally.

### Pending

- Confirm monitoring VM access and permissions.
- Confirm application server IP addresses.
- Install and verify Node Exporter.
- Deploy and validate the monitoring stack.
- Test application failure detection and recovery.
- Verify automatic deployment rollback with the team.
- Complete centralised logging, database recovery
  testing and scheduled shutdown tasks.
- Record live testing evidence.

## Evidence

- Ansible playbook: ansible/playbooks/agents.yml
- Prometheus: monitoring/prometheus/prometheus.yml
- Alert rules: monitoring/prometheus/alerts.yml
- Blackbox Exporter: monitoring/blackbox/blackbox.yml
- Alertmanager: monitoring/alertmanager/alertmanager.yml
- Docker Compose: monitoring/docker-compose.yml
- Grafana dashboard: monitoring/grafana/dashboards/fiveops.json
- Rollback plan: docs/operations/rollback.md
- Test plan: docs/operations/monitoring-test-plan.md

## Progress - 27 November 2026

### Completed

- Established secure SSH access to the monitoring VM.
- Verified connectivity to the TEST application.
- Verified Node Exporter and Flask application metrics.
- Updated Prometheus targets for the TEST environment.
- Deployed the four monitoring containers using Docker Compose.
- Validated Prometheus and Alertmanager configurations.
- Confirmed all three Prometheus targets were UP.
- Verified live infrastructure and application metrics in Grafana.
- Confirmed Alertmanager accessibility.
- Investigated an unexpected application interruption.
- Confirmed Prometheus detected the failed health check.
- Recorded the interruption timestamps and alert state.
- Communicated the monitoring findings to Abdi.
- Captured screenshots for operational evaluation and Viva 2.
- Prepared evaluation results documentation for Targets 02, 07 and 08.
- Coordinated with team members regarding outstanding evaluation tasks.

### Outstanding Tasks

- Configure and verify Discord notifications with Yasin.
- Complete three coordinated alert delivery tests.
- Complete three rollback drills with Abdi.
- Document PostgreSQL recovery results.
- Confirm the Jenkins idle shutdown and startup configuration.
- Verify scheduled shutdown following team approval.
- Confirm outstanding centralised logging requirements.
- Finalise evaluation results and supporting evidence.

## Current Implementation Status

The monitoring stack has been successfully deployed and
verified in the TEST environment. Prometheus, Grafana,
Alertmanager and Blackbox Exporter are operational.

Application and infrastructure metrics have been verified.
An unexpected application interruption was successfully
detected and documented.

Discord notification delivery, controlled recovery tests,
database recovery and scheduled shutdown verification
remain pending team coordination.

Production monitoring remains outside the current
verification scope until infrastructure details are confirmed.

Additional evidence: docs/operations/evaluation-results.md

## Independent Peer Review - 27 November 2026

- Reviewed all seven documentation files in PR #44.
- Checked documentation consistency, risk management, release traceability and Viva 2 preparation.
- Provided written feedback on the latest monitoring progress.
- Highlighted the BCU DLP restriction affecting Teams notifications.
- Formally approved PR #44, which was subsequently merged into main.

Evidence: https://github.com/fiveops-bcu/fiveops/pull/44
