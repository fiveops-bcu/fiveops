# FiveOps Operational Evaluation Results

## Monitoring Verification

| Component | Result |
|---|---|
| Monitoring containers | Passed |
| Prometheus targets | All three UP |
| Grafana infrastructure metrics | Passed |
| Grafana application metrics | Passed |
| Alertmanager accessibility | Passed |
| Prometheus alert rules | Loaded successfully |
| Teams notification delivery | Pending |

## Target 07 - Alert Delivery Tests

Required: Each notification must arrive within five minutes.

| Trial | Failure time (UTC) | Teams notification time (UTC) | Elapsed time | Result |
|---|---|---|---|---|
| 1 | Pending | Pending | Pending | Pending |
| 2 | Pending | Pending | Pending | Pending |
| 3 | Pending | Pending | Pending | Pending |

## Target 02 - Rollback Tests

Required: Each rollback must complete within ten minutes.

| Trial | Original version | Restored version | Start time (UTC) | Recovery time (UTC) | Duration | Result |
|---|---|---|---|---|---|---|
| 1 | Pending | Pending | Pending | Pending | Pending | Pending |
| 2 | Pending | Pending | Pending | Pending | Pending | Pending |
| 3 | Pending | Pending | Pending | Pending | Pending | Pending |

## PostgreSQL Recovery

- Restoration outcome: Pending
- Application health: Pending
- Supporting evidence: Pending

## Target 08 - Automated Idle Shutdown

- Jenkins job: Pending confirmation
- Shutdown schedule: Pending
- Startup schedule: Pending
- Execution history: Pending
- VM power state verification: Pending

## Evaluation Summary

Live monitoring has been successfully verified.
Alert delivery, rollback, database recovery and
scheduled shutdown results remain pending.
