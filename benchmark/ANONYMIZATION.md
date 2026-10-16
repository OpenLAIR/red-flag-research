# Anonymization

The 20 targets are ICLR 2027 submissions under double-blind review. This release removes what would identify them directly and documents what remains.

## Removed or replaced

| Item | Treatment |
|---|---|
| Target PDFs, page images, PDF hashes | Not distributed |
| Target titles, title segments and runs of six or more consecutive title words in any text | `[TITLE Cnn]` |
| Short system names that form the first part of a title, their spelled-out forms, and other system, benchmark or dataset names a target introduces (reviewed by hand) | `[NAME Cnn]` |
| OpenReview ids, forum/PDF links, submission numbers, internal case and pair ids | `[ID Cnn]` |
| URLs in target text other than bibliographic hosts (arXiv, DOI, ACL Anthology, PMLR, NeurIPS proceedings) | `[URL REDACTED]` |
| Sources that are preprints of their own target (2) | Withheld: no identifier, title, URL or hash |
| Model reasoning traces, run logs, archived pipeline artifacts, review pages | Not distributed |
| Case order | Case ids assigned in random order |
| Annotator | Pseudonym `annotator-1` |

Text hashes in the release (`text_sha256`, `quote_sha256`) are computed on the anonymized text, except for excerpts of link-only sources, where the hash of the withheld excerpt lets you confirm an excerpt you extract yourself.

## Checks

- An automated scan of every released file against the private list of target identifiers, titles, title segments and title word runs, short names, hashes and withheld sources, and against all 43,008 ICLR 2027 OpenReview submission ids except the five that appear as sources. The count-only result is in [`ANONYMIZATION_SCAN.json`](ANONYMIZATION_SCAN.json); the patterns themselves are private because they would identify the targets.
- A manual spot check of three cases (target text, evidence, review points, label record) before release.

## Residual risk

- The anonymized text is verbatim and searchable. Names of individual modules or components inside a method, and distinctive sentences, were not replaced.
- Five source papers are other ICLR 2027 submissions (labelled on OpenReview as CC BY 4.0); they are sources, not targets, and are identified.
- Our live screening broadcast is not anonymized and shows paper titles. Anyone who saw a target–source pair there can match it to a case here.
- Page counts and section structure are kept.

Please do not attempt to re-identify targets. Authors who believe their paper is included can ask for correction or removal: see the README.
