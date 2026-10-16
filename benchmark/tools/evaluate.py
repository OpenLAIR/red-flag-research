#!/usr/bin/env python3
"""Score case-level predictions against the human labels.

Usage:
    python3 tools/evaluate.py --pred my_predictions.jsonl [--gold data/labels.jsonl] [--out metrics.json]

Prediction file: one JSON object per line,
    {"case_id": "C01", "label": "<label key>", "scores": {"source_review_recommended": 0.8}}
`label` is one of the keys below; `scores` is optional. Cases missing from the
file are scored as missing (treated as not flagged and reported separately).
See docs/METRICS.md for definitions.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

LABELS = ['no_source_finding', 'same_work_preprint', 'source_review_recommended', 'inconclusive']
POSITIVE = 'source_review_recommended'
RELATION = {'source_review_recommended', 'same_work_preprint'}
MISSING = 'missing'


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]


def wilson(k: int, n: int, z: float = 1.959964) -> list[float] | None:
    if n == 0:
        return None
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return [round(max(0.0, centre - half), 4), round(min(1.0, centre + half), 4)]


def ratio(k: int, n: int) -> float | None:
    return round(k / n, 4) if n else None


def binary_block(gold: dict, pred: dict, gold_pos: set, pred_pos: set) -> dict:
    tp = fp = fn = tn = 0
    for cid, g in gold.items():
        gp = g in gold_pos
        pp = pred.get(cid, MISSING) in pred_pos
        if gp and pp:
            tp += 1
        elif pp:
            fp += 1
        elif gp:
            fn += 1
        else:
            tn += 1
    precision = ratio(tp, tp + fp)
    recall = ratio(tp, tp + fn)
    f1 = (round(2 * precision * recall / (precision + recall), 4)
          if precision is not None and recall is not None and (precision + recall) > 0 else
          (0.0 if precision is not None and recall is not None else None))
    return {
        'tp': tp, 'fp': fp, 'fn': fn, 'tn': tn,
        'precision': precision, 'precision_wilson95': wilson(tp, tp + fp),
        'recall': recall, 'recall_wilson95': wilson(tp, tp + fn),
        'f1': f1,
        'false_positive_rate': ratio(fp, fp + tn), 'false_positive_rate_wilson95': wilson(fp, fp + tn),
    }


def auroc(gold: dict, scores: dict) -> dict:
    pos = [scores[c] for c, g in gold.items() if g == POSITIVE and c in scores]
    neg = [scores[c] for c, g in gold.items() if g != POSITIVE and c in scores]
    if not pos or not neg:
        return {'auroc': None, 'n_pos_scored': len(pos), 'n_neg_scored': len(neg)}
    wins = sum(1.0 if p > n else 0.5 if p == n else 0.0 for p in pos for n in neg)
    return {'auroc': round(wins / (len(pos) * len(neg)), 4),
            'n_pos_scored': len(pos), 'n_neg_scored': len(neg)}


def evaluate(gold_rows: list[dict], pred_rows: list[dict]) -> dict:
    gold = {r['case_id']: r['label'] for r in gold_rows}
    pred: dict[str, str] = {}
    scores: dict[str, float] = {}
    problems = []
    for r in pred_rows:
        cid = r.get('case_id')
        if cid not in gold:
            problems.append(f'unknown case_id {cid!r}')
            continue
        if cid in pred:
            problems.append(f'duplicate prediction for {cid}')
            continue
        label = r.get('label')
        if label is None:
            continue  # explicit null = missing
        if label not in LABELS:
            problems.append(f'invalid label {label!r} for {cid}')
            continue
        pred[cid] = label
        s = (r.get('scores') or {}).get(POSITIVE)
        if isinstance(s, (int, float)):
            scores[cid] = float(s)
    if problems:
        raise SystemExit('prediction file errors:\n  ' + '\n  '.join(problems))

    cols = LABELS + [MISSING]
    confusion = {g: {p: 0 for p in cols} for g in LABELS}
    for cid, g in gold.items():
        confusion[g][pred.get(cid, MISSING)] += 1
    correct = sum(1 for cid, g in gold.items() if pred.get(cid) == g)
    return {
        'n_cases': len(gold),
        'gold_counts': {k: sum(1 for g in gold.values() if g == k) for k in LABELS},
        'n_predicted': len(pred),
        'n_missing': len(gold) - len(pred),
        'n_inconclusive_predictions': sum(1 for p in pred.values() if p == 'inconclusive'),
        'primary_source_review_recommended': binary_block(gold, pred, {POSITIVE}, {POSITIVE}),
        'secondary_any_source_relation': binary_block(gold, pred, RELATION, RELATION),
        'exact_label_accuracy': ratio(correct, len(gold)),
        'exact_label_correct': correct,
        'confusion_gold_by_pred': confusion,
        'ranking_source_review_recommended': auroc(gold, scores),
    }


def main(argv: list[str] | None = None) -> None:
    root = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--pred', required=True, type=Path)
    ap.add_argument('--gold', type=Path, default=root / 'data' / 'labels.jsonl')
    ap.add_argument('--out', type=Path)
    args = ap.parse_args(argv)
    result = evaluate(read_jsonl(args.gold), read_jsonl(args.pred))
    text = json.dumps(result, indent=1)
    if args.out:
        args.out.write_text(text + '\n', encoding='utf-8')
    print(text)


if __name__ == '__main__':
    main(sys.argv[1:])
