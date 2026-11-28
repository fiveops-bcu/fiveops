# FiveOps Monitoring Deployment

## Prerequisites

- Authorised access to the monitoring VM.
- Docker and Docker Compose installed.
- Confirmed test and production server addresses.
- Node Exporter installed on application servers.
- Network connectivity between the VMs.

## Deployment Procedure

1. Access the monitoring VM using SSH.
2. Retrieve the operations monitoring branch.
3. Update Prometheus targets with confirmed addresses.
4. Navigate to the monitoring directory.
5. Validate the Docker Compose configuration:

   docker compose config

6. Start the monitoring services:

   docker compose up -d

7. Verify container status:

   docker compose ps

8. Check container logs if required:

   docker compose logs --tail=50

## Monitoring Interfaces

- Prometheus: port 9090
- Grafana: port 3000
- Alertmanager: port 9093

Access these interfaces through authorised SSH
port forwarding.

## Verification

- Confirm Prometheus targets are UP.
- Confirm Grafana displays live metrics.
- Verify application health monitoring.
- Test alerts and recovery with team approval.
- Record results in the monitoring test plan.

## Discord Alert Notifications

Discord was selected as the alternative notification
channel following the university's Microsoft Teams
DLP restriction and team lead approval.

- Store the webhook URL outside the Git repository.
- Use the private ~/.fiveops-secrets/discord_url file.
- Restrict access to the webhook secret.
- Mount the secret into Alertmanager as read-only.
- Verify that the Alertmanager container can read the
  secret without exposing its contents.
- Validate the Alertmanager configuration before deployment.
- Verify firing and recovery notifications in Discord.
- Never include webhook credentials in GitHub or screenshots.

## Current Status

The monitoring stack was successfully deployed on
the monitoring VM on 27 November 2026.

Prometheus, Grafana, Alertmanager and Blackbox Exporter
were running successfully. All three TEST monitoring
targets were verified as UP, and Grafana displayed
live application and infrastructure metrics.

The Discord notification configuration has been
prepared and committed. Live deployment and notification
delivery verification remain pending.

Production monitoring remains outside the current
verified deployment scope.

Further testing requires monitoring VM availability
and coordination with the project team.
