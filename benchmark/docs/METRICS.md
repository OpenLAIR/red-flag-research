# Metrics

`tools/evaluate.py` scores one case-level prediction per target against `data/labels.jsonl`.

## Input

One JSON object per line: `case_id`, `label` (one of `no_source_finding`, `same_work_preprint`, `source_review_recommended`, `inconclusive`, or `null`), and optionally `scores.source_review_recommended` (a number; higher means more likely). A case that is absent or has `label: null` is **missing**. Unknown case ids, duplicates and invalid labels are errors.

## Primary: `source_review_recommended` detection

Positive class: gold `source_review_recommended`. A prediction is positive only if its label is `source_review_recommended`; `inconclusive`, other labels and missing predictions count as negative (not flagged).

- **TP / FP / FN / TN** — always report the counts. There are 2 gold positives and 18 gold negatives.
- **Precision** = TP / (TP + FP); undefined (null) when nothing is flagged.
- **Recall** = TP / (TP + FN).
- **F1** = harmonic mean of precision and recall (0 when both are 0; null if precision is undefined).
- **False-positive rate** = FP / (FP + TN): the share of non-positive cases that were flagged. On a screening task that names papers this matters as much as recall.
- Each rate comes with a **Wilson 95% interval**. With 2 positives these intervals are very wide; do not compare systems on point estimates alone.

## Secondary: any source relation

Positive class: gold `source_review_recommended` or `same_work_preprint`; prediction positive if its label is either of these. This credits a system that detects a strong correspondence but cannot tell a preprint from unattributed reuse (the included baselines cannot output `same_work_preprint`).

## Exact-label accuracy and confusion matrix

Share of cases whose predicted label equals the gold label (`inconclusive` and missing are never correct, since no gold label is `inconclusive`). The confusion matrix has gold labels as rows and predicted labels plus `missing` as columns.

## Ranking

If scores are given, **AUROC** for `source_review_recommended` over the cases that have a score (Mann–Whitney; ties count 0.5). With 2 positives AUROC takes few distinct values; report `n_pos_scored` and `n_neg_scored` with it.

## Also report

- Number of `inconclusive` predictions and missing cases (abstention).
- Which candidate sources your system saw. Labels cover only the listed candidates; a system that retrieves other sources may find correspondences the labels do not cover.
- Whether your system used anything that could reveal target identities (it should not).
