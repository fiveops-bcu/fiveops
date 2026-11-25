One file per team member.

## Who is who on GitHub

Viva 2 is marked individually, so every commit, review and PR must be traceable to a named person. Some members' commits appear under a different name from their GitHub account.

| Team member | Role | GitHub account | Commit names seen in history | Record |
|---|---|---|---|---|
| Yasin Mohammed Miah | Team Leader | `ymmiah` | Yasin Mohammed Miah | [yasin.md](yasin.md) |
| Arkadiusz Borkowski | CI/CD Engineer | `ArkadiuszB850414` | ArkadiuszB850414 | [arkadiusz.md](arkadiusz.md) |
| Abdisalan Mohamed | Platform Engineer | `AbdiAwil` | Abdisalan Mohamed, AbdiAwil | [abdisalan.md](abdisalan.md) |
| Fadumo Ibrahim | Quality and Security Engineer | `lashent` | Fadumo Ibrahim, lashent | [fadumo.md](fadumo.md) |
| Aissatou Diallo | Operations Engineer | `AissatouDiallo224` | Aissatou, Aissatou Diallo, AissatouDiallo224 | [aissatou.md](aissatou.md) |

Five early commits on branches `arkadiusz-docker` and `arkadiusz-app-tests` (15–16 November) show the author as `unknown` because Git's name was not set on that machine. That work reached `main` through Arkadiusz's PRs, for example [#3](https://github.com/fiveops-bcu/fiveops/pull/3) and [#6](https://github.com/fiveops-bcu/fiveops/pull/6), which carry his account.

To keep future commits consistent, each member runs once on every computer they use:

```bash
git config --global user.name  "Full Name"
git config --global user.email "ID+username@users.noreply.github.com"
```

(GitHub shows your no-reply address under Settings → Emails.)
