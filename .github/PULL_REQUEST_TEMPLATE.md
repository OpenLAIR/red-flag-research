<!-- Thanks for contributing! Please read CONTRIBUTING.md first. -->

## What and why

<!-- What does this change, and why? Link the issue: "Closes #123". -->

## Type of change

- [ ] Bug fix
- [ ] New feature or improvement to the tools
- [ ] Evaluation or metric change (`benchmark/tools/evaluate.py`, `benchmark/docs/METRICS.md`)
- [ ] Data or documentation
- [ ] CI

## How I tested it

<!-- Commands you ran and their result. -->

- [ ] `python3 benchmark/tools/validate_release.py` passes
- [ ] `python3 benchmark/tools/evaluate.py` runs on the three scored baselines (see CONTRIBUTING.md)
- [ ] I added or updated tests for the changed behavior, where the tools have them

## Evaluation or metric changes only

<!-- Required when the "Evaluation or metric change" box is ticked. See CONTRIBUTING.md. -->

- `evaluate.py` output for each baseline before → after:
- Which numbers changed and why:

## Checklist

- [ ] No API keys, provider headers, `.env` files or absolute local paths in the change or in this description
- [ ] No benchmark target paper titles or links (cases are anonymized), and no paper named as suspected
- [ ] Public wording follows CONTRIBUTING.md (no "plagiarism", "misconduct" or "laundering" in output)
- [ ] Every commit is signed off (`git commit -s`) under the [DCO](https://developercertificate.org/)
- [ ] Code is contributed under Apache-2.0 and data under CC BY 4.0, as described in CONTRIBUTING.md
