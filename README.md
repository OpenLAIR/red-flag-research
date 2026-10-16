# Red-flag Research

**Live, open-source screening for automated-research attacks on peer review.**

Project site and live broadcast: <https://openlair.github.io/red-flag-research.github.io/>

Red-flag Research is a research project that screens conference submissions for
passages, numbers or tables that closely match an earlier public paper without
clear attribution. When it finds such a match, it labels the pair
**Source review recommended**, which means a person should compare the two papers
side by side. The label is not a finding of plagiarism or misconduct (see
[About these results](#about-these-results)).

This repository publishes the project's **benchmark**: an anonymized diagnostic
set of ICLR 2027 target papers with candidate sources, evidence locations, human
labels, saved baseline outputs and evaluation tools. The
screening pipeline itself is not part of this release.

| Path | Contents |
| --- | --- |
| [`benchmark/`](benchmark/README.md) | The benchmark release and its data card |
| [`benchmark/tools/`](benchmark/tools/) | Validation, source download and evaluation tools (Python standard library only) |
| [`docs/CORRECTIONS.md`](docs/CORRECTIONS.md) | How to report a wrong result about a paper |

## Quick start

The tools need Python 3.9 or later and only the standard library.

```bash
git clone https://github.com/OpenLAIR/red-flag-research.git
cd red-flag-research

# Check the release: structure, links, licenses and checksums.
python3 benchmark/tools/validate_release.py

# Download the source papers that may not be redistributed, and check their SHA-256.
python3 benchmark/tools/fetch_sources.py

# Score a prediction file against the human labels.
python3 benchmark/tools/evaluate.py --pred benchmark/baselines/jev_paper_final.jsonl
```

The [data card](benchmark/README.md) describes the task, the labels, the
prediction format, how the set was built, its limitations and the
anonymization.

## About these results

**About these results.** Red-flag Research is a research project that screens
conference submissions automatically. A **Source review recommended** label
means the system found passages, numbers or tables that closely match an
earlier public paper without a clear attribution, so a person should compare
the two papers side by side.

It is **not** a finding of plagiarism, misconduct or bad faith. It has not been
reviewed by the conference, the authors or any integrity committee. The system
uses language models and can be wrong: shared authors, an earlier version of
the same work, a cited dataset or a common baseline can all explain matching
text, and the system may not see them. A paper without a label has not been
cleared either.

Benchmark cases are anonymized before release.

**Think a result is wrong?** If you are an author and believe a result about
your paper is wrong, email **red.flag.autoresearch@gmail.com**. We will correct it right
away, and we take the result off the live page and the public data while we
check.

## License

- Code (the tools and scripts) is licensed under the [Apache License 2.0](LICENSE).
- Annotations, labels, metadata and documentation written by this project are
  licensed under [CC BY 4.0](benchmark/LICENSE-ANNOTATIONS.md).
- Source papers keep their own licenses; see
  [`benchmark/SOURCES.md`](benchmark/SOURCES.md). Papers that may not be
  redistributed are not included; `fetch_sources.py` downloads them from their
  original location.

## Contributing

Contributions to the benchmark and its tools are welcome.

- [CONTRIBUTING.md](CONTRIBUTING.md) explains how to run the checks, the
  conventions, DCO sign-off and how to open a pull request.
- [Open an issue](https://github.com/OpenLAIR/red-flag-research/issues/new/choose)
  with one of the forms: bug report, feature request, wrong result about a
  paper, or fix to a benchmark case.
- [MAINTAINERS.md](MAINTAINERS.md) describes how we triage, review and merge.
- To report a wrong result about your paper privately, see
  [docs/CORRECTIONS.md](docs/CORRECTIONS.md).
- To report a vulnerability or an exposed credential, see
  [SECURITY.md](SECURITY.md).

## Citation

If you use the benchmark, please cite it as described in
[CITATION.cff](CITATION.cff). GitHub shows a "Cite this repository" button
generated from that file.
