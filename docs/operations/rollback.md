# FiveOps Rollback and Recovery Plan

## Purpose

This document describes the automated application
rollback mechanism, operational recovery procedure
and verified TEST recovery evaluation.

## Failure Detection

Jenkins and Ansible verify application health and
the expected application version during deployment.

Prometheus and Alertmanager provide independent
monitoring and alert notifications.

Formal alert notification timing is evaluated
separately under Evaluation Target 07.

## Automated Rollback Implementation

The shared Ansible deployment playbook implements
automatic rollback using a block and rescue structure.

Before deployment, Ansible checks the existing
application health and preserves the healthy
Docker Compose configuration.

If deployment validation fails, Ansible:

1. Checks that a healthy previous release exists.
2. Restores the last known-good Compose configuration.
3. Restarts the previous application release.
4. Verifies application health.
5. Records the rollback in the release history.
6. Reports the original deployment as failed.

Immutable GHCR image digests support reproducible
release restoration.

Production integration was merged through PR #46.
Production runtime recovery remains untested.

## Controlled TEST Recovery Evaluation

Date: 27 November 2026

Evaluation Target 02 requires three successful
application rollback drills, each under 10 minutes.

The tests used an isolated copy of deploy.yml with
a deliberate failure injected after successful
candidate version verification.

The original Ansible rescue mechanism was unchanged.

A protected configuration and PostgreSQL backup
was created before testing.

Competing deployments were paused in coordination
with the CI/CD engineer.

### Release Configuration

- Environment: TEST
- Original healthy release: 55b27ab
- Controlled deployment candidate: 737512f
- Expected recovered release: 55b27ab

### Jenkins Evaluation Results

Diagnostic job: FiveOps-TEST-Rollback-Drill

| Build | Completion UTC | Duration | Result |
|---|---|---:|---|
| #1 | 21:26:19 | 15 seconds | PASS |
| #2 | 21:33:03 | 15 seconds | PASS |
| #3 | 21:36:04 | 14 seconds | PASS |

- Successful drills: 3/3
- Success rate: 100%
- Average duration: 14.67 seconds
- Slowest duration: 15 seconds
- Maximum permitted duration: 600 seconds
- Evaluation Target 02: PASS

All three diagnostic Jenkins builds succeeded.

Ansible returned exit code 2 as expected because
the original deployment deliberately failed.

Jenkins reported diagnostic success only after
verifying the automatic rollback and recovered state.

### Verified Recovery Conditions

All three drills confirmed:

- Controlled deployment failure detected.
- Automatic Ansible rollback executed.
- Original application version restored.
- Original immutable image reference restored.
- Application health endpoint returned OK.
- PostgreSQL was accepting connections.
- Total drill duration remained under 10 minutes.

### Independent Server Evidence

Verified directly on TEST at 21:38:59 UTC.

```text
2026-11-27T21:26:18Z ROLLBACK 737512f FAILED - PREVIOUS_VERSION RESTORED
2026-11-27T21:33:02Z ROLLBACK 737512f FAILED - PREVIOUS_VERSION RESTORED
2026-11-27T21:36:03Z ROLLBACK 737512f FAILED - PREVIOUS_VERSION RESTORED

LAST GOOD VERSION:
55b27ab

APPLICATION HEALTH:
{"status":"ok"}

APPLICATION VERSION:
{"version":"55b27ab"}

DATABASE STATUS:
/var/run/postgresql:5432 - accepting connections
```

## Manual Recovery Procedure

If automatic rollback fails:

1. Identify the failure using Jenkins and server logs.
2. Prevent competing deployments.
3. Notify the responsible team members.
4. Identify the verified last known-good release.
5. Obtain the required environment-specific approval.
6. Restore the verified configuration using the
   approved recovery procedure.
7. Verify application health, version, image reference
   and database availability.
8. Check monitoring and record the recovery outcome.

Do not delete persistent database volumes during
application rollback.

## PostgreSQL Recovery

Separate database recovery tests completed on
27 November 2026 demonstrated successful logical
backup restoration using a synthetic dataset.

The populated database restoration took 874 ms.

SHA-256 comparisons confirmed matching source
and restored customer and ticket data.

These results represent database restoration,
not application rollback timing.

## Security Considerations

- Only authorised team members may perform recovery.
- Credentials must not be committed to source control.
- Recovery configuration backups must remain protected.
- Production changes require the approved release process.
- Diagnostic jobs must be disabled after evaluation,
  while retaining build history for evidence.

## Evaluation Limitations

The measured durations include candidate deployment,
controlled failure, automatic rollback and final
verification using locally available container images.

These tests do not measure exact application downtime,
complete infrastructure disaster recovery or production
recovery performance.

Database availability was verified after each drill;
continuous database availability was not measured.

Production runtime validation, fresh infrastructure
rebuild testing and formal alert notification timing
remain outstanding.

## Current Implementation Status

- Automated application rollback: implemented.
- TEST rollback evaluation: passed.
- Evaluation Target 02: achieved.
- Production integration: merged, runtime unverified.
- Formal alert notification evaluation: outstanding.
