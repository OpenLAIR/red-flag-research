#!/usr/bin/env bash
# Check that every non-merge commit in BASE..HEAD carries a Developer Certificate
# of Origin sign-off ("Signed-off-by: Name <email>") matching its author e-mail.
# Commits authored by GitHub bots (e.g. Dependabot) are skipped.
#
# Usage: scripts/check_dco.sh <base> [<head>]   e.g. scripts/check_dco.sh origin/main HEAD
set -euo pipefail

base="${1:?usage: check_dco.sh <base> [<head>]}"
head="${2:-HEAD}"
missing=0
checked=0

for commit in $(git rev-list --no-merges "$base..$head"); do
  author="$(git log -1 --format='%ae' "$commit")"
  case "$author" in
    *'[bot]@users.noreply.github.com') continue ;;
  esac
  checked=$((checked + 1))
  if ! git log -1 --format='%(trailers:key=Signed-off-by,valueonly)' "$commit" | grep -qiF "<$author>"; then
    echo "::error::Commit $(git rev-parse --short "$commit") has no Signed-off-by line matching its author e-mail."
    missing=$((missing + 1))
  fi
done

if [ "$missing" -ne 0 ]; then
  echo "$missing of $checked commit(s) are not signed off."
  echo "Sign off with 'git commit -s' (fix existing commits with 'git rebase --signoff <base>')."
  echo "See CONTRIBUTING.md, section 'Sign your commits (DCO)'."
  exit 1
fi
echo "All $checked commit(s) are signed off."
