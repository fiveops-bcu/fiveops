# FiveOps Centralised Logging

## Purpose

Centralised logging supports application troubleshooting,
incident investigation and operational monitoring.

## Architecture

- Grafana Alloy collects TEST application container logs.
- Loki receives and stores application logs.
- Grafana provides an interface for viewing and querying logs.

## Security Considerations

- Restrict log collection to the authorised TEST environment.
- Obtain approval before accessing the Docker socket.
- Treat Docker socket access as privileged access.
- Use an approved private connection between Alloy and Loki.
- Do not publicly expose the unauthenticated Loki endpoint.
- Avoid collecting or exposing sensitive application data.

## Verification

- Validate the Loki and Alloy configurations.
- Confirm Loki is running on the monitoring VM.
- Confirm Alloy is running on the TEST VM.
- Verify connectivity between Alloy and Loki.
- Confirm TEST application logs appear in Grafana.
- Capture redacted screenshots for evaluation and Viva 2.

## Current Status

Configuration and deployment files have been prepared
and committed to GitHub.

Live deployment and end-to-end verification remain
pending VM availability and team authorisation.

## Logging Test Cases

| ID | Test | Expected Result | Status |
|---|---|---|---|
| L01 | Validate Loki configuration | No configuration errors | Pending |
| L02 | Validate Alloy configuration | No configuration errors | Pending |
| L03 | Check Loki service | Loki is running and ready | Pending |
| L04 | Check Alloy service | Alloy is running successfully | Pending |
| L05 | Verify private connectivity | Alloy can securely reach Loki | Pending |
| L06 | Verify Grafana data source | Loki connection is successful | Pending |
| L07 | Query TEST application logs | Application logs appear in Grafana | Pending |
| L08 | Verify log labels | TEST environment and app service labels are present | Pending |

## Evidence Requirements

- Loki and Alloy service status.
- Successful Grafana Loki data source connection.
- TEST application logs displayed in Grafana Explore.
- Actual verification timestamps and test outcomes.
- Redacted screenshots without sensitive information.
