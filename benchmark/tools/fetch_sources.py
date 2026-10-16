#!/usr/bin/env python3
"""Download the link-only source papers and check their SHA-256.

Some source papers cannot be redistributed under their license. For those,
licenses/sources.json gives a versioned URL, the byte size and the SHA-256 of
the file we used. This script downloads each one and compares hashes.

Usage:
    python3 tools/fetch_sources.py                 # link-only sources -> sources/<key>/paper.pdf
    python3 tools/fetch_sources.py --verify-included   # also re-hash the bundled PDFs
    python3 tools/fetch_sources.py --only arxiv-2609.04148

Exit status is non-zero if any download fails or any hash differs. A hash
mismatch keeps the file as paper.pdf.mismatch so you can inspect it: arXiv
occasionally re-renders a version, in which case the text should still agree.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
import urllib.request
from pathlib import Path

USER_AGENT = 'benchmark-source-fetch/0.3.0 (research use)'
DELAY_S = 3.0  # be polite to arXiv


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    tmp = dest.with_name(dest.name + '.part')
    with urllib.request.urlopen(req, timeout=120) as r, tmp.open('wb') as f:
        while True:
            chunk = r.read(1 << 20)
            if not chunk:
                break
            f.write(chunk)
    tmp.replace(dest)


def main(argv: list[str] | None = None) -> int:
    root = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--manifest', type=Path, default=root / 'licenses' / 'sources.json')
    ap.add_argument('--out-dir', type=Path, default=root / 'sources')
    ap.add_argument('--only', action='append', default=[], help='source_key to fetch (repeatable)')
    ap.add_argument('--verify-included', action='store_true', help='also hash the redistributed PDFs')
    ap.add_argument('--force', action='store_true', help='re-download even if a matching file exists')
    args = ap.parse_args(argv)

    manifest = json.loads(args.manifest.read_text(encoding='utf-8'))
    failures = 0
    for src in manifest['sources']:
        key = src['source_key']
        if args.only and key not in args.only:
            continue
        dist = src['distribution']
        if dist == 'included' and args.verify_included:
            path = root / src['files']['pdf']
            ok = path.exists() and sha256_file(path) == src['sha256']
            print(f'{"OK  " if ok else "FAIL"} included  {key}')
            failures += not ok
            continue
        if dist != 'link_only':
            continue
        dest = args.out_dir / key / 'paper.pdf'
        if dest.exists() and not args.force and sha256_file(dest) == src['sha256']:
            print(f'OK   cached    {key}')
            continue
        try:
            download(src['download_url'], dest)
            time.sleep(DELAY_S)
        except Exception as exc:  # network errors are reported, not raised
            print(f'FAIL download  {key}: {exc}')
            failures += 1
            continue
        got = sha256_file(dest)
        if got == src['sha256']:
            print(f'OK   fetched   {key} ({src["version"]})')
        else:
            bad = dest.with_name('paper.pdf.mismatch')
            dest.replace(bad)
            print(f'FAIL sha256    {key}: expected {src["sha256"]}, got {got} (kept {bad})')
            failures += 1
    print(f'done: {failures} problem(s)')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
