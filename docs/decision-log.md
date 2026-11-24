# FiveOps decision log

**Maintainer:** Yasin Mohammed Miah

**Originally recorded:** 20 November 2026
**Last evidence update:** 24 November 2026

**Interpretation:** These are retrospective records of the documented design, not invented minutes of a meeting. Original decision dates and team sign-off require confirmation.

| ID | Recorded | Decision / current approach | Alternative / trade-off | Reason | Status and evidence | Owner |
|---|---|---|---|---|---|---|
| D-01 | 2026-11-20 | Use public `fiveops-bcu/fiveops` repository with named accounts | Private repo | Visible PR review and shared source | **Implemented:** [repository](https://github.com/fiveops-bcu/fiveops); ask tutor to confirm public is acceptable | Yasin |
| D-02 | 2026-11-20 | Vagrant/VirtualBox to define four Ubuntu VMs | Terraform/cloud-first infrastructure | Repeatable lab machines suited to course resources | **Initial four-VM VirtualBox design remains in the versioned `Vagrantfile`:** [PR #5](https://github.com/fiveops-bcu/fiveops/pull/5). The team subsequently used VMware for the running Jenkins/test VMs; see D-11. Full original four-VM runtime reproduction remains pending | Abdisalan |
| D-03 | 2026-11-20 | Jenkins remains the primary assessed CI technology | GitHub Actions only | Team plan and assessment demonstration require Jenkinsfile execution | **Code implemented only:** `Jenkinsfile` from [PR #6](https://github.com/fiveops-bcu/fiveops/pull/6); no verified shared Jenkins run | Arkadiusz |
| D-04 | 2026-11-20 | Poll GitHub from private Jenkins server (proposed 1-minute interval) | Inbound public webhook | A laptop/host-only VM is not accessible to GitHub webhooks without additional exposure | **Planned, not configured/verified** | Arkadiusz |
| D-05 | 2026-11-20 | Tag approved images by 7-character Git commit and store in GHCR | Mutable latest-only tags | Traceable build-to-image relationship | **Planned:** pipeline publish stages/registry evidence outstanding | Arkadiusz |
| D-06 | 2026-11-20 | Store CI secrets in Jenkins Credentials and server secrets in Ansible Vault | Secrets in source code or chat | Restrict access and avoid accidental disclosure | **Planned:** inventory/vault/credential evidence outstanding | Fadumo |
| D-07 | 2026-11-20 | Use Grafana Alloy for log collection | Promtail | Team plan selects Alloy for the supported logging design | **Planned:** monitoring configuration not in `main` | Aissatou |
| D-08 | 2026-11-20 | Pin the planned Trivy scanner version to 0.69.3 until reviewed | Automatically updating scanner | Reproducible security gate and controlled supply-chain change | **Planned:** verify compatibility and published scan version before implementation | Fadumo / Arkadiusz |
| D-09 | 2026-11-20 | Retain the Flask app, with a simple static page as contingency | Dropping the deliverable or hiding failing checks | Keeps a demonstrable end-to-end element possible if app integration is blocked | **Contingency only; not activated**. Team playbook reports tutor confirmation on 14 Nov; original tutor note not independently available | Yasin |
| D-10 | 2026-11-20 | Consider hosted GitHub Actions for immediate shared tests while retaining Jenkins evidence | Depend entirely on one member's laptop | Team access to CI when the local Jenkins VM is offline | **Proposal only:** no workflow exists on verified `main`; decide with team/tutor | Yasin / Arkadiusz |
| D-11 | 2026-11-24 (retrospectively recorded) | **Current lab implementation uses VMware:** Jenkins runs on an Ubuntu VMware VM, made privately accessible with Tailscale Serve; a Vagrant-created Ubuntu 24.04 test VM now runs in VMware Workstation | Continue using the four-VM VirtualBox lab exactly as originally specified | Available BCU/local VMware environment supports private Jenkins access and a reachable test VM; avoids exposing Jenkins publicly | **Observed platform implementation, not proof of a formally approved whole-team scope change.** [PR #13](https://github.com/fiveops-bcu/fiveops/pull/13) reports Jenkins/Tailscale setup; [PR #23](https://github.com/fiveops-bcu/fiveops/pull/23) reports test VM, SSH, Docker, Ansible and an idempotency check (6 successful tasks, `changed=0`, `failed=0`, `unreachable=0`). The versioned four-VM `Vagrantfile` still specifies `virtualbox`; deployment, full rebuild and tutor/team approval of any provider change remain to be documented | Abdisalan (implementation), Yasin (decision record) |

## Implications of D-11

- Keep the original VirtualBox design visible in Git history; do not claim all four original VMs have been migrated or reproduced.
- Abdisalan should document the exact VMware provider/host, VM provisioning commands, Tailscale Serve access architecture, permission controls, persistence/recovery plan and evidence without revealing credentials.
- Confirm the provider change and any assessment implications with the team and tutor; record the approval date separately once obtained.
- Verify the second Ansible run and subsequent rebuild with actual redacted command output before claiming evaluation target 05 is met.

## Decision changes and recording protocol

- Record **date of approval** separately from the date a retrospective row was written.
- For each new decision, link a meeting note, PR or issue, note the rejected alternative, and state its impact on security and assessment scope.
- If the team moves Jenkins to cloud hosting, record the provider, cost/free limits, administrative owner, private access, rollback plan, and how Vagrant/Ansible evidence remains satisfied.
- Do not change another contributor's historical Git author attribution. PR #9 was authored by Yasin and reviewed by Abdisalan; its playbook operational ownership remains assigned to Abdisalan unless the team changes it explicitly.
