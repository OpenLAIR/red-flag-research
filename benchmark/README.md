# Red-flag Research Source-Review Benchmark — ICLR 2027 diagnostic set (v0.3.0)

**20 anonymized target papers · 34 target–source pairs · human labels for every target.**
A small diagnostic set for testing systems that check whether a paper's content corresponds to earlier public work without clear attribution.

> **About these results.** Red-flag Research is a research project that screens conference submissions automatically. A **Source review recommended** label means the system found passages, numbers or tables that closely match an earlier public paper without a clear attribution, so a person should compare the two papers side by side.
> It is **not** a finding of plagiarism, misconduct or bad faith. It has not been reviewed by the conference, the authors or any integrity committee. The system uses language models and can be wrong: shared authors, an earlier version of the same work, a cited dataset or a common baseline can all explain matching text, and the system may not see them. A paper without a label has not been cleared either.
> Benchmark cases are anonymized before release.

> **Think a result is wrong?** If you are an author and believe a result about your paper is wrong, email **red.flag.autoresearch@gmail.com**. We will correct it right away, and we take the result off the live page and the public data while we check.

## Contents

| Path | What it is |
|---|---|
| `data/cases.jsonl` | One record per target paper: case id, anonymized text path, page count, pairs, human label, annotation focus |
| `data/pairs.jsonl` | One record per target–source pair: source key, distribution class, source title and versioned URL (when not withheld) |
| `data/labels.jsonl` | Human label per target, the initial draft label and its basis, and the annotation action |
| `cases/Cnn/target.md` | Anonymized text of the target paper (OCR of the submitted PDF, page-delimited) |
| `cases/Cnn/evidence.json` | Paired evidence spans: anonymized target excerpts and source excerpts with page numbers and locators |
| `cases/Cnn/review_points.json` | 60 evidence locations prepared for human review (target page, source page, quotes) |
| `sources/` | CC BY 4.0 source papers: PDF, extracted text and attribution |
| `licenses/sources.json`, `SOURCES.md` | License, version and SHA-256 of every source paper |
| `baselines/`, `BASELINES.md` | Outputs of our screening pipeline and their scores |
| `docs/ANNOTATION_GUIDELINES.md` | How the labels were assigned |
| `docs/METRICS.md` | Metric definitions |
| `ANONYMIZATION.md`, `ANONYMIZATION_SCAN.json` | What was removed, the residual risks, and the scan result |
| `tools/` | `evaluate.py`, `fetch_sources.py`, `validate_release.py` (Python 3.9+, standard library only) |

## Quick start

```bash
python3 tools/validate_release.py          # structure, links, licenses, checksums
python3 tools/fetch_sources.py             # download the 13 link-only source PDFs and check SHA-256
python3 tools/evaluate.py --pred baselines/jev_paper_final.jsonl
```

`baselines/` holds saved outputs of our screening system, and the tools above need only Python's standard library.

A prediction file has one line per case: `{"case_id": "C01", "label": "no_source_finding", "scores": {"source_review_recommended": 0.1}}`.

## Task and labels

One case is one target paper and the candidate sources our pipeline retrieved for it. The label applies to the target paper and covers only the listed candidates.

| Label key | Display name | Meaning | Cases |
|---|---|---|---:|
| `source_review_recommended` | Source review recommended | Distinctive content corresponds to an earlier public paper without adequate attribution, and the annotator found no benign explanation among those checked | 2 |
| `same_work_preprint` | Same paper (preprint) | A candidate source is a preprint or earlier version of the same work | 2 |
| `no_source_finding` | No source finding | Among the listed candidates, the correspondences checked have a benign explanation or none was found. This is not a clearance of the paper | 16 |
| `inconclusive` | Inconclusive | Evidence is insufficient to decide. Available to systems; no gold label uses it in this release | 0 |

## How the set was built

- **Targets.** ICLR 2027 submissions publicly posted on OpenReview. Nineteen come from a random sample of 50 submissions that our pipeline screened in October 2026; they were selected to emphasize source comparison and disagreement between models, not at random. The twentieth was added by the annotator as a known positive case, replacing one negative case.
- **Sources.** Candidate sources were retrieved by the pipeline (arXiv and OpenReview). Each case keeps one or two candidates, 34 pairs in total.
- **Text.** Target text is OCR of the submitted PDF. Source text consists of excerpts extracted from arXiv HTML or PDF; it is not the complete paper.
- **Labels.** A single annotator (a project member) reviewed all 20 cases on 2026-10-15. Initial draft labels had been derived from the pipeline's outputs; the annotator confirmed 16 and changed 4 (from inconclusive to no source finding). Rationales are in `data/labels.jsonl`.

## Intended use

- Diagnosing source-attribution screening systems: which kinds of correspondence they flag, miss or misread, and how they handle preprints and disclosed reuse.
- Comparing systems on the same small, fully documented set, with the caveats below.

**Out of scope.** Do not use this set to estimate how common unattributed reuse is, to rank venues or authors, to train a system that labels individual papers without human review, or to attempt to identify the anonymized targets or their authors.

## Limitations

- **One annotator.** No inter-annotator agreement was measured. Labels reflect one person's judgment on the listed candidates only.
- **Two positives.** With 2 `source_review_recommended` cases, recall can take only the values 0, 0.5 or 1 and every rate has a very wide confidence interval. Report counts, not just rates.
- **Non-random, model-influenced selection.** Cases were chosen from pipeline outputs and draft labels were derived from them. The included baselines are therefore not independent of the labels, and scores on this set overstate their real-world performance.
- **Limited source coverage.** A label covers only the listed candidates; other sources may exist. `no_source_finding` does not clear a paper.
- **Extraction noise.** OCR and HTML extraction can drop or garble formulas, tables and figure text. Page numbers refer to the original PDFs; target PDFs are not distributed.
- **Partial text for some sources.** Thirteen sources are link-only and two are withheld (see below), so their excerpts are not included.

## Anonymization

Target PDFs are not distributed. Titles, OpenReview identifiers and links, submission numbers, short system names taken from the titles (and their spelled-out forms), other system, benchmark and dataset names the targets introduce, and target PDF hashes were replaced by case ids (`[TITLE Cnn]`, `[NAME Cnn]`, `[ID Cnn]`); other URLs in target text, except bibliographic hosts, were replaced by `[URL REDACTED]`. Case ids were assigned in random order. Two sources that are preprints of their own targets are withheld for the same reason. Details and the scan result are in [ANONYMIZATION.md](ANONYMIZATION.md).

**Residual risk.** Anonymization reduces but does not remove the chance of re-identification. The remaining text is verbatim and searchable, and names of individual modules inside a method were not replaced. Our live screening broadcast is **not** anonymized and shows paper titles: anyone who saw a target–source pair there can match it to a case here. Please do not attempt to re-identify targets. If you are an author and believe your paper is in this set, contact us (below).

## Licenses

- **Annotations, labels, metadata and documentation** written by us: [CC BY 4.0](LICENSE-ANNOTATIONS.md).
- **Code** in `tools/`: [Apache-2.0](LICENSE-CODE).
- **Source papers**: each keeps its own license; see [SOURCES.md](SOURCES.md). The 19 CC BY 4.0 sources are redistributed with attribution and a description of changes. The 13 sources under the arXiv non-exclusive license or CC BY-NC-SA 4.0 are not redistributed: we give the versioned URL and SHA-256, and `tools/fetch_sources.py` downloads them. Two same-work sources are withheld.
- **Target texts** are derived from submissions posted on OpenReview under CC BY 4.0. They are redistributed in modified (anonymized, text-only) form; attribution is withheld for now to protect double-blind review. Authors who want to be credited for their text, or want it removed, can contact red.flag.autoresearch@gmail.com.

Inclusion of a paper records only that our pipeline compared it with another paper. It is not a statement about that paper.

## Corrections and takedown

Email **red.flag.autoresearch@gmail.com** with the case id (or the paper, if you are its author) and what is wrong. We will:

1. acknowledge the request and remove the case or source from the public data while we check;
2. correct or remove the record and publish a new version with a changelog entry stating what changed (without identifying the paper);
3. reply with the outcome.

Removed content can persist in earlier git commits and forks that we do not control; we will ask the hosting platform to purge cached views where possible.

## Versions

- **v0.3.0 (2026-10-15)** — first public release. Anonymized, license-separated rebuild of the internal v0.2.0 set; labels unchanged. Built by an internal script; its inputs, including the case-id mapping, are kept private.

## Citation

See CITATION.cff at the repository root.
