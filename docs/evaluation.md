# FiveOps evaluation plan — targets 01–08

**Owner:** Yasin Mohammed Miah

**Checkpoint 2 baseline:** 20 November 2026

**Status:** Assessment methods, pass marks and owners defined; measured results remain **not yet verified**. The 20 and 27 November integration sessions are planned test opportunities, not completed tests.

| ID | Business need | Repeatable method | Pass criterion | Accountable owner(s) | Evidence to capture | Result |
|---|---|---|---|---|---|---|
| **01** | Repeatable deployment under 20 minutes | From a traceable commit, time build/test/scan/image/deploy/health; exclude only documented human approval waiting time | **Under 20 minutes** elapsed | Arkadiusz, Abdisalan | Jenkins stage timestamps, PR, image tag, service health and stopwatch log | **Pending** |
| **02** | Roll back a defective release within 10 minutes | Carry out **three** timed rollback drills using an earlier tested image | Slowest of three drills **under 10 minutes** | Aissatou | Three drill timestamps, old/new image tags and service health | **Pending** |
| **03** | Every production change is traceable | For every release, trace commit → PR → named review → passing checks → image tag → `/version` or deployment record | **Every release traceable** with no missing link | Yasin | PR links, Jenkins logs, registry and `/version` | **Pending** |
| **04** | No shared administrator accounts; least privilege | Audit GitHub, Jenkins and VM users/groups; verify individual accounts and 2FA wherever supported | No shared administrator logins; appropriate least privilege and team 2FA | Fadumo | Redacted access matrix and account audit | **Pending** |
| **05** | Servers reproducible from source | Provision each VM from versioned Ansible; run provisioning twice and rebuild one VM | Second run `changed=0` and rebuild restores expected services | Abdisalan | Vagrant status, two Ansible PLAY RECAP outputs, rebuild log | **Pending** |
| **06** | No deployment without passing tests | Inspect every release against the associated tests, coverage and pipeline decision | No release without green tests; coverage **≥80%** | Fadumo, Yasin | Jenkins build history, JUnit and coverage XML | **Pending** |
| **07** | Failure alert within five minutes | Stop app or simulate outage and time three independent alerts to team channel | Each of three alerts arrives **within 5 minutes** | Aissatou | Alertmanager/Prometheus times, notification timestamps | **Pending** |
| **08** | Non-production machines off when idle | Observe automated test-VM shutdown and collect nightly scheduled job history | Test VM switches off on the agreed nightly schedule | Aissatou | Scheduler job history and VM power state | **Pending** |

## Measurement register (fill with actual data only)

| Trial date | Target ID | Commit / deployed image | Started (UTC) | Ended (UTC) | Net elapsed | Outcome | Evidence URL | Tested by |
|---|---|---|---|---|---|---|---|---|
| Pending | 01–08 | — | — | — | — | Not run / not evidenced | — | — |

## Protocol for target 01 — end-to-end deployment timing

1. Choose a reviewed PR and record its merge commit (or the allowed triggering commit), test environment and baseline application version.
2. Record the timer start at the agreed point in the pipeline; if subtracting human approval wait, preserve both the raw and excluded time spans.
3. Capture checkout, Gitleaks, tests/coverage, Bandit, Docker build, Trivy, GHCR push, deployment and health-check timestamps separately. If a stage is not implemented, the complete target is **not met**, not assumed.
4. Record the timer finish only when the deployed service answers the documented health/version checks.
5. Calculate `elapsed = finish − start − documented approval wait`; identify network/cold-start and other limitations.
6. Store screenshots/logs with secrets redacted under `docs/evidence/` and link the source build URL.

## Evaluation limitations as of 20 November 2026

- A [Docker/PostgreSQL local-test evidence document](evidence/arkadiusz-docker-tests.md) reports 13 passing tests and 97.09% coverage; this is **not** a verified hosted Jenkins gate or end-to-end deployment timing.
- The current `Jenkinsfile` on `main` contains checkout and Docker test stages; full security scans, image publishing, and automated deployment are not evidenced in that file.
- `Vagrantfile`, `common.yml` and `jenkins.yml` are versioned, but a successful four-VM provision, second `changed=0` run and deployment timing are not evidenced in the inspected repository.
- The operations monitoring, three rollback drills and nightly idle shutdown remain to be demonstrated.

## Acceptance and reporting

Record the method, actual inputs, date, output and failures (including failed runs). A result passes only if the corresponding target is measured and supported by a traceable file or log. Use the target IDs in sprint retrospectives and the final Viva 2 demonstration.
