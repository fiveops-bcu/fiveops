# FiveOps Monitoring Test Plan

## Purpose

This test plan defines how the monitoring system
will be verified to ensure that server metrics,
application availability and alerts are monitored.

## Testing Requirements

- Access to the monitoring VM.
- Node Exporter running on application servers.
- Monitoring containers running.
- Network connectivity between the VMs.
- Approval before performing failure tests.

## Test Cases

| ID | Test | Expected Result | Status |
|---|---|---|---|
| T01 | Check monitoring containers | All four containers are running | Passed (27 Nov 2026) |
| T02 | Check Node Exporter | Server metrics are accessible | Passed (27 Nov 2026) |
| T03 | Check Prometheus targets | Configured targets show UP | Passed (27 Nov 2026) |
| T04 | Check Grafana dashboard | Live monitoring metrics are displayed | Passed (27 Nov 2026) |
| T05 | Check application health | HTTP 200 and probe_success equals 1 | Passed (27 Nov 2026) |
| T06 | Simulate approved test application failure | ApplicationDown alert fires | Pending |
| T07 | Check Alertmanager | Critical alert is displayed | Pending |
| T08 | Restore test application | Application recovers and alert resolves | Pending |
| T09 | Verify automatic deployment rollback with team | Previous stable version is restored | Pending |

## Evidence Collection

Screenshots will be collected during testing
to demonstrate monitoring, failure detection,
alert management and recovery.

## Safety Considerations

Failure tests must be performed in the test
environment with team approval.

Production services must not be interrupted
without authorisation.

## Current Status

The monitoring stack was deployed and verified on 27 November 2026.
Initial TEST monitoring checks passed successfully.
Discord notification delivery and controlled recovery tests remain pending.

## Additional Evaluation Requirements

- Verify that Prometheus collects Flask application metrics.
- Conduct three independent alert delivery trials.
- Confirm each alert reaches the approved Discord channel within five minutes.
- Conduct three controlled rollback trials with team approval.
- Confirm the slowest rollback takes less than ten minutes.
- Verify the previous application version and health after each rollback.
- Verify scheduled TEST VM shutdown using scheduler history and VM power state.
- Record actual timings, outcomes, failures and supporting evidence.

Initial monitoring results have been recorded. Remaining evaluation results require coordinated live testing.
