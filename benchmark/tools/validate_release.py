#!/usr/bin/env python3
"""Check the structure and integrity of this benchmark release.

Usage:
    python3 tools/validate_release.py [--skip-checksums]

Checks: required files, record counts and schemas, label vocabulary, links
between cases, pairs, labels, evidence and the source manifest, the
distribution class of every source against its license, bundled-file hashes,
checksums.sha256, absence of target PDFs, and the public wording rules.
Prints one line per failed check and exits non-zero on any failure.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

LABELS = {'no_source_finding', 'same_work_preprint', 'source_review_recommended', 'inconclusive'}
GOLD_LABELS = LABELS - {'inconclusive'}
DISTRIBUTIONS = {'included', 'link_only', 'withheld'}
REDISTRIBUTABLE = {'CC BY 4.0'}
REQUIRED = [
    'README.md', 'LICENSE-ANNOTATIONS.md', 'LICENSE-CODE', 'SOURCES.md', 'ANONYMIZATION.md',
    'BASELINES.md', 'checksums.sha256', 'data/cases.jsonl', 'data/pairs.jsonl', 'data/labels.jsonl',
    'licenses/sources.json', 'docs/ANNOTATION_GUIDELINES.md', 'docs/METRICS.md',
    'tools/evaluate.py', 'tools/fetch_sources.py', 'tools/validate_release.py',
    'baselines/results.json',
]
# Words the public text must not use (data-card policy). Paper texts under
# cases/*/target.md and sources/*/text.md are third-party content and exempt,
# as is the approved disclaimer sentence.
BANNED = re.compile(r'launder|plagiar|YES_SUSPECTED|NO_SUPPORTED|paper-laundry', re.I)
APPROVED = 'It is **not** a finding of plagiarism, misconduct or bad faith.'
CJK = re.compile('[\\u3040-\\u30ff\\u3400-\\u4dbf\\u4e00-\\u9fff\\uac00-\\ud7af]')


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]


def main(argv: list[str] | None = None) -> int:
    root = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--root', type=Path, default=root)
    ap.add_argument('--skip-checksums', action='store_true')
    args = ap.parse_args(argv)
    root = args.root
    errors: list[str] = []
    err = errors.append

    for rel in REQUIRED:
        if not (root / rel).is_file():
            err(f'missing required file {rel}')
    if errors:
        print('\n'.join(errors))
        return 1

    cases = read_jsonl(root / 'data/cases.jsonl')
    pairs = read_jsonl(root / 'data/pairs.jsonl')
    labels = read_jsonl(root / 'data/labels.jsonl')
    manifest = json.loads((root / 'licenses/sources.json').read_text(encoding='utf-8'))
    sources = {s['source_key']: s for s in manifest['sources']}

    case_ids = [c['case_id'] for c in cases]
    if len(case_ids) != len(set(case_ids)):
        err('duplicate case_id in data/cases.jsonl')
    if not all(re.fullmatch(r'C\d{2}', c) for c in case_ids):
        err('case_id must look like C01')
    pair_ids = [p['pair_id'] for p in pairs]
    if len(pair_ids) != len(set(pair_ids)):
        err('duplicate pair_id in data/pairs.jsonl')
    pairs_by_case: dict[str, list[str]] = {}
    for p in pairs:
        pairs_by_case.setdefault(p['case_id'], []).append(p['pair_id'])
        if p['case_id'] not in case_ids:
            err(f'pair {p["pair_id"]} has unknown case {p["case_id"]}')
        src = sources.get(p['source_key'])
        if src is None:
            err(f'pair {p["pair_id"]} has source_key not in manifest: {p["source_key"]}')
        elif src['distribution'] != p['source_distribution']:
            err(f'pair {p["pair_id"]} distribution disagrees with manifest')
    for c in cases:
        if sorted(c['pair_ids']) != sorted(pairs_by_case.get(c['case_id'], [])):
            err(f'case {c["case_id"]} pair_ids disagree with data/pairs.jsonl')
        if c['n_pairs'] != len(c['pair_ids']):
            err(f'case {c["case_id"]} n_pairs wrong')
        cdir = root / 'cases' / c['case_id']
        for rel in (c['target_text'], c['evidence'], c['review_points']):
            if not (root / rel).is_file():
                err(f'case {c["case_id"]} missing {rel}')
        if list(cdir.glob('*.pdf')):
            err(f'case {c["case_id"]} contains a PDF; target PDFs must not be distributed')
        ev = json.loads((root / c['evidence']).read_text(encoding='utf-8'))
        if sorted(e['pair_id'] for e in ev['pairs']) != sorted(c['pair_ids']):
            err(f'case {c["case_id"]} evidence pairs disagree with case record')
        for e in ev['pairs']:
            for side in ('target', 'source'):
                for s in e['spans'][side]:
                    t = s.get('text')
                    if t is not None and hashlib.sha256(t.encode('utf-8')).hexdigest() != s['text_sha256']:
                        err(f'{c["case_id"]} span {s["span_id"]} text_sha256 mismatch')
            src = sources.get(e['source_key'], {})
            if src.get('distribution') != 'included' and any(s.get('text') for s in e['spans']['source']):
                err(f'{c["case_id"]} {e["pair_id"]}: source text present for a non-redistributable source')

    by_case = {r['case_id']: r for r in labels}
    if sorted(by_case) != sorted(case_ids):
        err('labels.jsonl does not cover exactly the cases in cases.jsonl')
    for r in labels:
        if r['label'] not in GOLD_LABELS:
            err(f'label {r["label"]!r} for {r["case_id"]} not in gold vocabulary')
        if r.get('initial_label') not in LABELS:
            err(f'initial_label {r.get("initial_label")!r} for {r["case_id"]} not in vocabulary')
    for c in cases:
        if by_case.get(c['case_id'], {}).get('label') != c['label']:
            err(f'case {c["case_id"]} label disagrees with labels.jsonl')

    used = {p['source_key'] for p in pairs}
    if used != set(sources):
        err(f'manifest sources differ from sources used by pairs: {sorted(used ^ set(sources))}')
    for key, s in sources.items():
        if s['distribution'] not in DISTRIBUTIONS:
            err(f'{key}: unknown distribution {s["distribution"]}')
            continue
        if s['distribution'] == 'withheld':
            if any(s.get(k) for k in ('identifier', 'title', 'download_url', 'sha256')):
                err(f'{key}: withheld source exposes identifying fields')
            if (root / 'sources' / key).exists():
                err(f'{key}: withheld source has files')
            continue
        if s['distribution'] == 'included':
            if s['license'] not in REDISTRIBUTABLE:
                err(f'{key}: included but license is {s["license"]}')
            for kind in ('pdf', 'text', 'attribution'):
                if not (root / s['files'][kind]).is_file():
                    err(f'{key}: missing {kind} file')
            pdf = root / s['files']['pdf']
            if pdf.is_file() and sha256_file(pdf) != s['sha256']:
                err(f'{key}: bundled PDF sha256 differs from manifest')
        if s['distribution'] == 'link_only':
            if s['license'] in REDISTRIBUTABLE:
                err(f'{key}: redistributable license but link-only')
            if (root / 'sources' / key).exists() and any(
                    f.name not in ('paper.pdf', 'paper.pdf.mismatch') for f in (root / 'sources' / key).iterdir()):
                err(f'{key}: link-only source has bundled files')
            if not re.fullmatch(r'[0-9a-f]{64}', s.get('sha256') or ''):
                err(f'{key}: link-only source lacks sha256')
            if not re.search(r'v\d+$', s.get('download_url', '')) and s.get('platform') == 'arxiv':
                err(f'{key}: arXiv download URL is not versioned')

    for path in sorted(root.rglob('*')):
        if not path.is_file() or path.suffix not in ('.md', '.json', '.jsonl', '.py', '.txt', ''):
            continue
        rel = path.relative_to(root).as_posix()
        if rel.startswith('sources/') and rel.endswith('/text.md'):
            continue
        text = path.read_text(encoding='utf-8', errors='replace')
        paper_text = rel.startswith('cases/')
        if CJK.search(text) and not paper_text:
            err(f'{rel}: contains CJK characters (public text must be English)')
        if paper_text or rel == 'tools/validate_release.py':
            continue
        for m in BANNED.finditer(text.replace(APPROVED, '')):
            err(f'{rel}: banned public wording {m.group(0)!r}')
            break

    if not args.skip_checksums:
        listed = {}
        for line in (root / 'checksums.sha256').read_text(encoding='utf-8').splitlines():
            digest, rel = line.split('  ', 1)
            listed[rel] = digest
        # Files that tools/fetch_sources.py downloads for link-only sources are not part of the release.
        fetched = {f'sources/{k}/' for k, s in sources.items() if s['distribution'] == 'link_only'}
        actual = {rel for rel in (p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file())
                  if rel != 'checksums.sha256' and not any(rel.startswith(f) for f in fetched)
                  and '__pycache__' not in rel}
        if set(listed) != actual:
            err(f'checksums.sha256 file list differs: {sorted(set(listed) ^ actual)[:10]}')
        for rel, digest in listed.items():
            if (root / rel).is_file() and sha256_file(root / rel) != digest:
                err(f'checksum mismatch: {rel}')

    summary = {
        'cases': len(cases), 'pairs': len(pairs),
        'labels': {k: sum(1 for r in labels if r['label'] == k) for k in sorted(GOLD_LABELS)},
        'sources': {d: sum(1 for s in sources.values() if s['distribution'] == d) for d in sorted(DISTRIBUTIONS)},
    }
    print(json.dumps(summary))
    if errors:
        print(f'{len(errors)} error(s):')
        print('\n'.join(errors))
        return 1
    print('OK')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
