# Baselines

Outputs of the screening pipeline that produced this set, scored with `tools/evaluate.py`. No model was rerun for this release. These numbers come from 20 cases with 2 positives; they show how the metrics behave and are not estimates of real-world accuracy. See docs/METRICS.md for definitions.

## `jev_paper_final`

Jev (jev-1.13.0) paper-level final verdict, with probabilities. Not run on one case (scored as missing).

| Metric | Value |
|---|---|
| Cases predicted / missing | 19 / 1 |
| Inconclusive predictions | 13 |
| Primary: TP / FP / FN / TN | 1 / 4 / 1 / 14 |
| Primary: precision (Wilson 95%) | 0.20 [0.0362, 0.6245] |
| Primary: recall (Wilson 95%) | 0.50 [0.0945, 0.9055] |
| Primary: F1 | 0.29 |
| Primary: false-positive rate | 0.22 [0.09, 0.4521] |
| Secondary (any source relation): precision / recall | 0.60 / 0.75 |
| Exact-label accuracy | 0.10 (2/20) |
| AUROC on `source_review_recommended` score | 0.94 |

## `qwen_paper_final`

Qwen paper-level final verdict (categorical). Not run on one case (scored as missing).

| Metric | Value |
|---|---|
| Cases predicted / missing | 19 / 1 |
| Inconclusive predictions | 14 |
| Primary: TP / FP / FN / TN | 1 / 4 / 1 / 14 |
| Primary: precision (Wilson 95%) | 0.20 [0.0362, 0.6245] |
| Primary: recall (Wilson 95%) | 0.50 [0.0945, 0.9055] |
| Primary: F1 | 0.29 |
| Primary: false-positive rate | 0.22 [0.09, 0.4521] |
| Secondary (any source relation): precision / recall | 0.60 / 0.75 |
| Exact-label accuracy | 0.05 (1/20) |
| AUROC on `source_review_recommended` score | – |

## `qwen_b_pair_aggregate`

Pair-level Qwen B verdicts aggregated per case: flagged if any pair is flagged; inconclusive if any pair is inconclusive or invalid; otherwise no source finding.

| Metric | Value |
|---|---|
| Cases predicted / missing | 20 / 0 |
| Inconclusive predictions | 4 |
| Primary: TP / FP / FN / TN | 2 / 2 / 0 / 16 |
| Primary: precision (Wilson 95%) | 0.50 [0.15, 0.85] |
| Primary: recall (Wilson 95%) | 1.00 [0.3424, 1.0] |
| Primary: F1 | 0.67 |
| Primary: false-positive rate | 0.11 [0.031, 0.328] |
| Secondary (any source relation): precision / recall | 0.75 / 0.75 |
| Exact-label accuracy | 0.70 (14/20) |
| AUROC on `source_review_recommended` score | – |

Per-pair outputs of every condition (Jev hidden, Jev visible control, Qwen A, Qwen B) are in `baselines/pair_level_outputs.jsonl`. A null probability means the model returned none; it is not zero.
