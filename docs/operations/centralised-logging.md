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
