# FiveOps risk register

**Owner:** Yasin Mohammed Miah

**Baseline date:** 20 November 2026 (initial ratings are planning judgements; review with team)

**Scale:** Likelihood = Low/Medium/High; Impact = Low/Medium/High. Risk status does not imply mitigation was tested.

| ID | Risk and effect | Likelihood | Impact | Planned mitigation | Owner | Status / next evidence |
|---|---|---|---|---|---|---|
| R-01 | Four Vagrant VMs rely on one laptop; hardware failure interrupts CI and demonstration | Medium | High | Keep all configuration in Git, capture build evidence, and prepare a recoverable host/hosted alternative | Abdisalan | Open; record `vagrant status`, provision recaps, fallback host |
| R-02 | Disabling SSH host-key checking in a lab permits host impersonation if copied into a real deployment | Low | Medium | Restrict any lab-only exception, verify host keys in real deployments, document boundary | Fadumo | Open; confirm whether this exception actually appears in deployed config |
| R-03 | Membership of `docker` group effectively grants host-root access; a compromised job can control server | Medium | High | Minimise privileges, isolate builds, use trusted PR source and restricted agents; keep Jenkins credentials segregated | Fadumo / Abdisalan | Open; review `common.yml` and `jenkins.yml` before external deployment |
| R-04 | Secrets pushed to a public repository may remain exposed in Git history | Medium | High | `.gitignore`, full-history Gitleaks, protected credentials, immediate rotation on disclosure | Fadumo | Partial: [PR #8](https://github.com/fiveops-bcu/fiveops/pull/8) merged; scan/rotation evidence missing |
| R-05 | Multiple new tools and distributed work create integration delays and knowledge gaps | High | Medium | Small reviewed PRs, runbooks, paired explanation and short demonstrations | Yasin | Open; record follow-ups and member hand-offs |
| R-06 | Jenkins is defined in code but not reachable to team; no repeatable green pipeline | High | High | Validate Vagrant host, decide shared hosted option, run real Jenkins build | Abdisalan / Arkadiusz | Open; as of 20 Nov, run URL/provision evidence not available in repo |
| R-07 | Security gates may be omitted from Jenkins, allowing unscanned changes/images | High | High | Agree Gitleaks, Bandit, Trivy and pytest gates; require reported checks | Fadumo / Arkadiusz | Open; current `Jenkinsfile` only checks out and runs Docker tests |
| R-08 | Missing or unverified monitoring/rollback leads to undetected failures or slow recovery | Medium | High | Implement alert rules, run three detection/rollback trials, record evidence | Aissatou | Open; no monitoring directory on verified `main` |
| R-09 | Risk of untraceable task ownership when infrastructure files are committed by another role | Medium | Medium | Keep actual authorship, write clear hand-off and confirm understanding in viva | Yasin / Abdisalan | Partial: [PR #9](https://github.com/fiveops-bcu/fiveops/pull/9) authored by Yasin, reviewed by Abdisalan; hand-off demo pending |
| R-10 | Submitted documents may assert feedback, test results or stakeholder agreement that cannot be evidenced | Medium | High | Separate planned/self-reported from verified outcomes; obtain tutor feedback and review | Yasin | Open; Viva 1 comments must be imported from original source |

## Review and escalation

1. Reassess likelihood and impact whenever the triggering event changes.
2. Add actual dates, issue links, mitigation test results and decisions as evidence becomes available.
3. Escalate a leaked credential immediately; revoke/rotate it before any cosmetic repository clean-up.
4. If one person cannot complete an assigned task, document the hand-off and accept/decline decision without personal judgement.
5. Cross-reference the release targets in [`evaluation.md`](evaluation.md).
