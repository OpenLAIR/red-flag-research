# Contributing

Thank you for helping improve Red-flag Research. This repository holds the
project's benchmark and its tools; we welcome bug reports, fixes, new features,
data fixes and corrections. This is a research project, so careful reports and small,
well-tested changes help most.

- [Ways to contribute](#ways-to-contribute)
- [Set up and run the checks](#set-up-and-run-the-checks)
- [Code conventions](#code-conventions)
- [Submitting a pull request](#submitting-a-pull-request)
- [Sign your commits (DCO)](#sign-your-commits-dco)
- [Changes to the evaluation tools or metrics](#changes-to-the-evaluation-tools-or-metrics)
- [Contributing data](#contributing-data)
- [What happens after you open an issue or pull request](#what-happens-after-you-open-an-issue-or-pull-request)
- [License of contributions](#license-of-contributions)

## Ways to contribute

Open an issue with the matching form on the
[new issue page](https://github.com/OpenLAIR/red-flag-research/issues/new/choose):

| You want to | Use |
| --- | --- |
| Report something that does not work | **Bug report** |
| Suggest a new feature or an improvement to the benchmark or its tools | **Feature request** |
| Tell us a result about a specific paper pair is wrong | Email **red.flag.autoresearch@gmail.com** — never a public issue ([corrections process](docs/CORRECTIONS.md)) |
| Fix a label or evidence location in an existing case, or report a data problem | **Fix a benchmark case** |
| Propose a new case (a pair of papers you think needs source review) | Email **red.flag.autoresearch@gmail.com** — never a public issue |
| Report a security problem or an exposed credential | Do not open an issue; follow [SECURITY.md](SECURITY.md) |

Please search existing issues first, write in English, and do not post
personal information, credentials or unpublished manuscripts. Do not name a
paper you suspect in a public issue: a public issue would read as an
accusation before anyone has compared the papers. Send suspected cases to
**red.flag.autoresearch@gmail.com** instead.

Wrong-result reports come by e-mail only and are handled separately from
issues. We correct a wrong result right away and take the result off the live
page and the public data while we check; see
[docs/CORRECTIONS.md](docs/CORRECTIONS.md). Public issues are for problems with
the benchmark, its data and its tools.

## Set up and run the checks

You need Python 3.9 or later and git. The benchmark tools use only the
standard library.

```bash
git clone https://github.com/OpenLAIR/red-flag-research.git
cd red-flag-research

# Structure, links, licenses and checksums of the release.
python3 benchmark/tools/validate_release.py

# Score the saved baselines against the human labels.
python3 benchmark/tools/evaluate.py --pred benchmark/baselines/jev_paper_final.jsonl
python3 benchmark/tools/evaluate.py --pred benchmark/baselines/qwen_paper_final.jsonl
python3 benchmark/tools/evaluate.py --pred benchmark/baselines/qwen_b_pair_aggregate.jsonl
```

Continuous integration runs the same commands on Python 3.10 and 3.13 for every
pull request, and checks that every commit is signed off (see
[Sign your commits](#sign-your-commits-dco)). A pull request can be merged only
after CI passes.

## Code conventions

- Match the style of the surrounding code: naming, comment density and idiom.
- Python: standard library only unless a dependency has been agreed in an
  issue first; PEP 8 layout; `pathlib` for paths; UTF-8 text files with LF line
  endings (see `.gitattributes`).
- No absolute local paths. Resolve paths relative to the repository root or read
  them from a documented environment variable or command-line option.
- No credentials, `.env` files, provider response headers or raw provider
  responses that have not been checked for secrets. Credentials are read from
  environment variables only.
- Tools must not call a model; only `fetch_sources.py` uses the network, and
  CI does not run it.
- Every behavior change comes with a test that fails before the change and
  passes after it.
- Public wording: results are **Source review recommended**, **No source
  finding**, **Inconclusive** or **Same paper (preprint)**. Do not describe a
  result as plagiarism, misconduct or "laundering" in code, docs or output.

## Submitting a pull request

1. For anything larger than a typo, open an issue first so we can agree on the
   approach before you write code.
2. Fork the repository and create a branch from `main`.
3. Make one focused change per pull request; keep unrelated formatting out.
4. Run the tests above and make sure they pass.
5. Sign off every commit (`git commit -s`); see
   [Sign your commits](#sign-your-commits-dco).
6. Open the pull request and fill in the template: what changed, why, how you
   tested it, and the linked issue.
7. A maintainer reviews it. Address comments with new signed-off commits; we
   squash them when merging and keep every `Signed-off-by` line.
8. The pull request is merged when CI passes and the required reviewers have
   approved it (see [MAINTAINERS.md](MAINTAINERS.md)).

## Sign your commits (DCO)

We use the [Developer Certificate of Origin 1.1](https://developercertificate.org/)
(DCO) instead of a contributor license agreement. By adding a sign-off line to a
commit, you certify that you wrote the change or otherwise have the right to
submit it under the project's licenses:

```text
Signed-off-by: Your Name <you@example.com>
```

Use your real name and an e-mail address you can be reached at. The easiest
way is to commit with `-s`:

```bash
git commit -s -m "Fix the evidence offset check"
```

Every commit in a pull request needs a sign-off. If you forgot it:

```bash
# Last commit only
git commit --amend --no-edit -s

# Every commit on your branch since main
git rebase --signoff main
git push --force-with-lease
```

CI checks every pull request: each commit except merge commits and commits by
GitHub bots needs a `Signed-off-by` line with the commit author's e-mail
address, and the pull request cannot be merged until the **DCO sign-off** check
passes. To run the same check locally before you push:

```bash
scripts/check_dco.sh main HEAD
```

Data contributions made through an issue form are covered by the license
checkbox in the form; data contributed in a pull request is covered by the
sign-off.

## Changes to the evaluation tools or metrics

A pull request that changes how predictions are scored (`benchmark/tools/evaluate.py`,
`benchmark/docs/METRICS.md`) must show its effect in the pull request
description: the output of `evaluate.py` for each scored baseline
(`jev_paper_final`, `qwen_paper_final`, `qwen_b_pair_aggregate`) before and
after the change, and which numbers changed
and why. Metric changes also need a maintainer review and a changelog entry.

## Contributing data

Benchmark files are checksummed and their bytes must stay exact, so do not edit
files under `benchmark/` by hand.

**Corrections to an existing case** (label, evidence location or other data
problem): open a **Fix a benchmark case** issue that gives:

- the case id only — benchmark cases are anonymized, so never the paper's
  title or link;
- the evidence location (page, section, table or line) and what it shows;
- your proposed label or change and your reasoning, following the
  [annotation guidelines](benchmark/docs/ANNOTATION_GUIDELINES.md).

**New cases**: email **red.flag.autoresearch@gmail.com** with public links and versions of
both papers, the evidence locations, your reasoning and each paper's license.
Do not open a public issue or pull request that names a paper you suspect.
Maintainers check the pair privately; if it becomes a case, it is anonymized
like the others.

Maintainers review contributions, rebuild the release with the project's build scripts
and credit you in the release notes (by name or anonymously, as you prefer).

## What happens after you open an issue or pull request

[MAINTAINERS.md](MAINTAINERS.md) describes who triages, how fast we aim to
reply, which labels we use and how pull requests are merged.

## License of contributions

By contributing, you agree that:

- code contributions are licensed under the [Apache License 2.0](LICENSE);
- data contributions (annotations, labels, evidence locations, rationales and
  other project-authored data) are licensed under
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/);
- papers and other third-party material you point to keep their own licenses;
  you license only what you wrote, and you tell us each paper's license.

You confirm this for each commit with a DCO sign-off (see
[Sign your commits](#sign-your-commits-dco)). You keep the copyright in your
contribution; there is no contributor license agreement.
