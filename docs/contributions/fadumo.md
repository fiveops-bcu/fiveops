# Contribution record: Fadumo Ibrahim (Quality and Security Engineer)



## Done, with evidence

- 16 November 2026: Enabled two-factor authentication and accessed the FiveOps repository.

- 16 November 2026: Cloned the repository, configured my Git identity and created the contrib-fadumo branch.

- Pull request number and repository evidence links will be added once available.



## In progress

- Create and submit this contribution record for review by Abdisalan, due 16 November 2026.



## Next, towards Viva 2

- Check team access and main branch protection, due 16 November 2026, to support least privilege and reviewed changes.

- Check .gitignore and scan the full Git history with Gitleaks, due 16 November 2026, to prevent exposed secrets.

- Create the secrets inventory without secret values, due 16 November 2026.

- Coordinate Jenkins credentials, encrypted vault files and security gates with the team before Viva 2.

- Review Aissatou's pull requests and leave written feedback before Checkpoint 2.



## My part in the web app

- Check the controls that protect the support-ticket app, its secrets and its delivery pipeline.



## Blockers

- Jenkins tasks depend on server availability and coordination with Arkadiusz and Abdisalan.

- Team permissions and branch protection still need to be verified.


## Progress update: 23 November 2026

### Completed
- Secret-file ignore rules merged through PR #8. All nine sample paths passed git check-ignore.
- On 22 November, Gitleaks 8.30.1 scanned 41 commits across fetched branches and reported no leaks.
- On 23 November, a direct push to main was rejected with GH013: changes must go through a pull request. Removed the local empty test commit afterwards.
- Confirmed the test configuration contains an 80% coverage threshold. This was a configuration check, not a successful Jenkins run.

### Awaiting review
- PR #14 adds the planned seven-secret inventory. Actual storage and permissions still require confirmation with the owners.

### Remaining work
- Coordinate Gitleaks, Bandit and Trivy pipeline gates with Arkadiusz; no references appeared in the three configuration files checked.
- Verify team-wide 2FA and push protection with Yasin.
- Coordinate Jenkins credentials, encrypted vault files and access permissions with the team.
- Review Aissatou's pull request and leave written feedback.
- Add screenshots to docs/evidence through a pull request. Screenshots are collected separately but are not yet linked here.

This update supersedes the earlier planned status for the ignore rules, secret scan and branch-protection check.
