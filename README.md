# FiveOps — DevOps and Enterprise Automation

**CMP6237 · Birmingham City University · BSc (Hons) Computing (Level 6 Top-up)**

**Client case:** Evolving Ltd

**Team Leader:** Yasin Mohammed Miah

**Status snapshot:** 26 November 2026 (main at `12e7093`); implementation is a coursework proof of concept, not a deployed production service.

## What FiveOps is building

FiveOps is a five-person DevOps team working on a small Flask support-ticket API and its delivery process. The expected flow is: a contributor pushes a branch → an independent reviewer checks the pull request → Jenkins runs tests and security gates → a versioned container image can be published and deployed → operational checks and evaluation evidence trace the result back to the change.

**Implementation status is deliberately separated from the target architecture.** `main` now contains the application and tests, a Jenkinsfile with Gitleaks, Docker Compose tests (coverage gate 80%), Bandit, image build, Trivy, GHCR publishing, an Ansible TEST deployment with automatic rollback, and a production approval stage that is off by default (`ENABLE_PRODUCTION_DEPLOY`). **Monitoring configuration is now merged** ([PR #42](https://github.com/fiveops-bcu/fiveops/pull/42)); live monitoring and notification delivery remain unverified. [PR #43](https://github.com/fiveops-bcu/fiveops/pull/43) reports a healthy TEST deployment of `b219a76` and a matching GHCR digest; the linked Jenkins build and complete release trace are still pending. **Outstanding:** Jenkins status reporting, a working production deployment, notification delivery, timed rollback drills, idle shutdown and measured results for targets 01–08.

## Team and contributions

| Member | Primary area |
|---|---|
| Yasin Mohammed Miah | Team Lead: repo governance, acceptance, evaluation and documentation |
| Arkadiusz Borkowski | CI/CD, Docker, Jenkins pipeline and build evidence |
| Abdisalan Mohamed | Vagrant/VirtualBox and Ansible infrastructure |
| Fadumo Ibrahim | Quality, secret scanning, security gates and access controls |
| Aissatou Diallo | Monitoring, alerting, rollback, idle-server scheduling and review support |

See [`docs/team-charter.md`](docs/team-charter.md) for the planned reviewer rotation, and the individual files under [`docs/contributions/`](docs/contributions/). Actual authorship remains as shown on GitHub: PR #6 (app/tests) was authored by Arkadiusz; PR #9 (Ansible playbooks) by Yasin and reviewed by Abdisalan.

## Repository layout

```text
app/                        Flask application, models and ticket routes
tests/                      Unit and PostgreSQL integration tests
Dockerfile                  Runtime container image
docker-compose.test.yml      PostgreSQL + pytest test services
Jenkinsfile                 Scans, tests, image build, GHCR push, TEST deploy, gated PROD
Vagrantfile                 Four Ubuntu 24.04 local VMs
ansible/inventory/           Vagrant/test/prod/monitoring inventories
ansible/playbooks/           Baseline, Jenkins installer, site, deploy (TEST) and deploy-prod
docs/                       Assessment records, sprint summaries, evidence, contributions
.github/                    Pull request template
requirements.txt            Application dependencies
requirements-dev.txt        Test and development dependencies
```

## Architecture — implemented and planned

```text
Developer branch → GitHub PR → review → protected main
                        |
                        v
              Jenkins multibranch job (planned shared host)
                        |
         checkout → Docker Compose + PostgreSQL tests (in Jenkinsfile)
                        |
         Gitleaks → Bandit → Docker image → Trivy (in Jenkinsfile)
                        |
              GHCR tagged image (reported TEST pull; complete release evidence pending)
                        |
      TEST deploy with rollback (in Jenkinsfile) → PROD (gated; fix pending)
                        |
             Prometheus/Grafana/Alertmanager (merged; live validation pending)
```

The four local Ubuntu VMs are defined in `Vagrantfile`:

| VM | Host-only IP | Memory | vCPU |
|---|---|---:|---:|
| Jenkins | 192.168.56.10 | 3072 MB | 2 |
| Test | 192.168.56.11 | 1536 MB | 1 |
| Production | 192.168.56.12 | 1536 MB | 1 |
| Monitoring | 192.168.56.13 | 2048 MB | 2 |

These private addresses work only with the relevant host-only VM network. Do not expose an unconfigured Jenkins controller publicly.

## Quick start — local Python

Prerequisites: Python 3.11+ (repository Docker images use Python 3.12), Git, and a working development environment.

```bash
git clone https://github.com/fiveops-bcu/fiveops.git
cd fiveops
python -m venv .venv
# Git Bash on Windows:
source .venv/Scripts/activate
# Linux/macOS:
# source .venv/bin/activate
python -m pip install -r requirements-dev.txt
export DATABASE_URL='sqlite:///fiveops-local.db' # Git Bash/Linux; demo only
python -m flask --app 'app:create_app()' run --host 127.0.0.1 --port 5000
```

For PowerShell, activate with `.venv\Scripts\Activate.ps1` and set `$env:DATABASE_URL='sqlite:///fiveops-local.db'`. The app uses `DATABASE_URL` outside test mode; `app.create_app()` calls `db.create_all()` for this proof of concept. Use migrations and hardened secrets handling in a real service.

Available HTTP paths from the source:

- `GET /health` — checks DB availability and responds with a JSON status.
- `GET /version` — reports `APP_VERSION` or `dev`.
- `POST /customers` — creates a customer with validated name/email.
- `POST /tickets`, `GET /tickets`, `PATCH /tickets/<id>` — ticket create/list/status update.
- `GET /metrics` — Prometheus metrics enabled when the app is not in testing mode.

**Security limitation:** These lab API endpoints do not implement user authentication/authorisation; do not expose the API or real personal data to the public internet.

## Run tests

```bash
python -m pytest --cov=app --cov-fail-under=80
```

The local unit test suite uses an in-memory SQLite database; the PostgreSQL integration test skips when `TEST_DATABASE_URL` is unset. For the complete Docker Compose test run, install Docker Desktop/Engine with Compose and run:

```bash
docker compose -f docker-compose.test.yml up --build \
  --abort-on-container-exit --exit-code-from tests
docker compose -f docker-compose.test.yml down -v --remove-orphans
```

Compose starts a disposable PostgreSQL instance, passes `TEST_DATABASE_URL`, and writes JUnit/Coverage reports into `reports/`. PR #4 contains **Arkadiusz's reported local** result of 13 tests and 97.09% coverage; this is not by itself a current independently verified Jenkins run.

## Provision Jenkins VM with Vagrant and Ansible

Host prerequisites: VirtualBox 7.x, Vagrant, enabled Intel VT-x/AMD-V and sufficient RAM (four VMs allocate approximately 8 GiB combined, plus host overhead).

```bash
vagrant validate
vagrant box add bento/ubuntu-24.04 --provider virtualbox
vagrant up jenkins
vagrant ssh jenkins -c 'systemctl is-active jenkins'
vagrant status
```

The `ansible_local` provisioner in `Vagrantfile` calls `ansible/playbooks/site.yml`, which imports `common.yml` and `jenkins.yml`. Both playbooks were merged in [PR #9](https://github.com/fiveops-bcu/fiveops/pull/9). Once installed, the lab Jenkins page is planned at `http://192.168.56.10:8080` **from the VM host laptop**.

The four-server build and second-run idempotence check have **not** been evidenced in this repository. When hardware permits, run `vagrant up`, record `vagrant status`, and `vagrant provision jenkins` with a complete `PLAY RECAP`. Investigate unexpected changes instead of assuming `changed=0`.

## Jenkins CI status and dependencies

The current `Jenkinsfile` runs Gitleaks, Docker Compose tests against PostgreSQL 17 (coverage gate 80%), Bandit, an image build tagged with the 7-character commit, and Trivy; on `main` it pushes the image to GHCR and deploys it to TEST with Ansible, then waits for approval before PROD when `ENABLE_PRODUCTION_DEPLOY` is ticked. Still to do and evidence: Jenkins commit statuses on GitHub PRs (so `protect-main` can require them), the PROD stage's database secret and rollback, pinned scanner versions on the Jenkins server, and a linked Jenkins run for one traced release.

Credentials and vault files must **never** be committed in plaintext. Jenkins credentials, environment-level vaults and access matrix remain a Fadumo/Arkadiusz security task. Note that membership of the Docker group grants very high privileges; isolate CI jobs before any internet-facing deployment.

## Assessment evidence and plans

- [`docs/README.md`](docs/README.md) — complete document index
- [`docs/sprints/sprint-2.md`](docs/sprints/sprint-2.md) — Checkpoint 2 goal, verified PRs, slippage and replan
- [`docs/evaluation.md`](docs/evaluation.md) — business targets **01–08**, methods, pass marks and evidence register
- [`docs/feedback-log.md`](docs/feedback-log.md) — Viva 1 feedback template; original feedback not yet provided
- [`docs/risk-log.md`](docs/risk-log.md) and [`docs/decision-log.md`](docs/decision-log.md)
- [`docs/definition-of-done.md`](docs/definition-of-done.md) and [`docs/team-charter.md`](docs/team-charter.md)

**Project status is evidence-based.** The presence of YAML, Jenkinsfile, screenshots or approved PRs does not automatically demonstrate a successful Jenkins, VM, monitoring or deployment trial.
