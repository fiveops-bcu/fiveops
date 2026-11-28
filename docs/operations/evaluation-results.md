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
| Discord notification delivery | Pending |

## Target 07 - Alert Delivery Tests

Required: Each notification must arrive within five minutes.

| Trial | Failure time (UTC) | Discord notification time (UTC) | Elapsed time | Result |
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

## Unexpected Application Interruption - 27 November 2026

An unexpected application interruption was reported during
deployment verification.

- Failed health check observed: 17:51:45 UTC.
- Successful health check observed: 17:52:00 UTC.
- ApplicationDown alert entered the pending state.
- No firing alert was observed.
- All four monitoring containers remained running.
- Findings were communicated to Abdi.

The interruption appears to have been shorter than the
configured one-minute alert threshold. The exact outage
duration could not be established from the query intervals.

This incident demonstrates successful failure detection
but does not count towards the three Target 07 notification
trials because Teams notification delivery was not verified.

Evidence: Aissatou_Unexpected_Application_Interruption.png

## Teams Notification Configuration Restriction

On 27 November 2026, the Power Automate method was attempted following coordination with Yasin.

The Microsoft Teams connection was established successfully and the "Send webhook alerts to a channel" workflow was created.

However, the workflow was suspended because the university's Tenant-Wide-DLP policy restricts the TeamsWebhookRequestReceived API.

This organisational security restriction prevented the webhook notification integration from being completed.

The existing Prometheus, Grafana and Alertmanager monitoring services remain unchanged.

An alternative approved notification method is awaiting agreement with the team. Target 07 alert-delivery testing remains pending.
