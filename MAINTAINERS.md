# Maintaining Red-flag Research

Status: proposed process, to be confirmed by the team before release.

## Roles

| Area | Owner | Reviews |
| --- | --- | --- |
| Triage (weekly rotation) | Red-flag Research team (red.flag.autoresearch@gmail.com) | Labels new issues and pull requests, assigns an owner, closes duplicates |
| Corrections (wrong-result reports and the contact e-mail) | Red-flag Research team (red.flag.autoresearch@gmail.com) | Takes results down, coordinates the check, replies to authors |
| Benchmark data and tools | Red-flag Research team (red.flag.autoresearch@gmail.com) | `benchmark/` (data, tools, annotation guidelines, metrics) |
| Security | Red-flag Research team (red.flag.autoresearch@gmail.com) | Private vulnerability reports, credential exposure |

At least two people should be able to act on corrections and security reports,
so that one absence never delays a takedown.

## Response targets

| Item | First response | Then |
| --- | --- | --- |
| Wrong-result report (e-mail or issue) | Take the result down when read; reply within 1 working day | Corrected or explained within 5 working days |
| Security report | 5 working days (as in `SECURITY.md`) | Fix or mitigation plan agreed with the reporter |
| Bug report | 5 working days | Labelled and prioritised at the next weekly triage |
| Feature request or data contribution | Next weekly triage | Accepted, declined with a reason, or marked `help wanted` |
| Pull request | First review within 7 days | Re-review within 3 working days after each update |

## Labels

| Label | Meaning |
| --- | --- |
| `type: bug` / `type: feature` / `type: data` / `type: docs` | Kind of issue (set by the issue forms) |
| `type: correction` | Wrong-result report; handled by the corrections owner, not in normal triage |
| `priority: urgent` / `priority: high` / `priority: normal` / `priority: low` | Urgency |
| `status: needs triage` | New; nobody has looked yet |
| `status: needs info` | Waiting for the reporter; closed after 30 days without a reply |
| `status: accepted` / `status: wontfix` / `status: duplicate` | Triage outcome |
| `area: benchmark` / `area: tools` / `area: docs` / `area: ci` | Part of the project |
| `good first issue` / `help wanted` | Open for outside contributors |

## Merging pull requests

- Every pull request needs passing CI (`.github/workflows/ci.yml`) and one
  approving review from a maintainer; branch protection enforces both.
- Evaluation or metric changes need the before/after results described in
  `CONTRIBUTING.md`, an approval from the benchmark owner, a second
  maintainer's approval and a changelog entry.
- Data changes are applied by the benchmark owner with the project scripts,
  never by editing checksummed files by hand; the release notes credit the
  contributor.
- Merge with **squash and merge**; the squash message states what changed and
  why and keeps the contributor's authorship and any sign-off lines.
- Maintainers do not merge their own pull requests without a second review,
  except for emergency takedowns, which are reviewed afterwards.

## Weekly triage

Once a week (proposed: Monday), the triage owner:

1. Labels every issue and pull request in `status: needs triage`.
2. Checks that every `type: correction` item has been taken down and answered.
3. Pings owners of pull requests waiting for review more than 7 days.
4. Closes `status: needs info` items older than 30 days with a note.
5. Picks up to three items for `good first issue` or `help wanted`.
6. Records a short summary (new, closed, open corrections, open pull requests)
   in the team notes.

## Releases

- Version the code and the benchmark with semantic versioning; a benchmark
  label change is a minor version, a schema change a major version.
- Each release has notes that list corrections (without naming papers), data
  contributions with credit, and evaluation changes with their effect on the
  baselines.
