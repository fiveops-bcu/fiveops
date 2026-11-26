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

## Current Implementation Status

Monitoring configuration and documentation have
been prepared. Live deployment and testing remain
pending infrastructure access and permissions.
