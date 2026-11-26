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

## Current Status

Deployment and live testing are pending
infrastructure access and permissions.
