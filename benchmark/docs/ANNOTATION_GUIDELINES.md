# Annotation guidelines

English translation of the guidelines used for the human labels (original in Chinese, 2026-10-14; label names updated to the public vocabulary). Case names in the original are replaced by case ids.

The unit of annotation is one target paper together with its listed candidate sources. Each case receives exactly one label, with the evidence that supports it.

| Label | When to use it | What to record |
|---|---|---|
| `same_work_preprint` (Same paper (preprint)) | There is evidence that the target and a public source are versions of the same work (preprint or earlier submission). The project's initial rule used an official same-title match; the annotator should also check the text and the version relationship. | The corresponding source and the title/version evidence. If a different source raises a separate substantive issue, record that as well. |
| `source_review_recommended` (Source review recommended) | Distinctive methods, data, results or research text are substantively reused and presented as the target's own contribution, and citation, explicitly stated inheritance, a shared prior work or a same-author version cannot explain the verified correspondence. | Exact target and source locations, the reused content, how the target states its contribution, where attribution appears, and the benign explanations that were ruled out. |
| `no_source_finding` (No source finding) | For the source comparisons checked, specific evidence supports legitimate inheritance or citation, a different mechanism, or a correspondence that does not amount to unattributed reuse. | The benign explanation and its location in the text; the range of sources actually checked. |
| `inconclusive` (Inconclusive) | Source, version or key context is insufficient, or conflicting evidence is unresolved, so none of the three labels above can be chosen reliably. | The open points, the missing evidence and where to look next. |

## Suggested order

1. Read the target abstract and contributions; note what it actually claims as new.
2. Read each candidate source and the key paired evidence. Check method steps, table numbers, data construction and specific wording.
3. In the full target text, check the corresponding passages, related work, references and any version statement. An excerpt without a citation does not mean the full paper has no citation.
4. Check for shared prior work, ordinary citation and disclosed inheritance. A shared dataset, a standard formula or the same topic is not enough on its own for `source_review_recommended`.
5. Choose the label and record the evidence ids or pages that support it, with a rationale. If the case cannot be resolved, label it `inconclusive` and say why.
6. Only after the first judgment, expand the existing label and model outputs. If you then change your judgment, state the new basis.

## Cases needing particular care

- **C13**: the annotator designated this pair as a positive case. Re-check trajectory replay and environment completion, the number of training environments, the experimental protocol and the attribution of results; record where the target's newly claimed components end and shared content begins.
- **C20**: check correspondence and attribution of the graph structure, entity learning and retrieval planning, and in the abstract, contributions and related work.
- **C16**: a saved primary-text review found explicitly stated inheritance from a shared prior work (TinyHistory) and disclosure of public data. Read the shared-prior-work explanation before judging; the earlier model scores remain recorded.
- **C03**: the paper-level and pair-level model outputs disagree. Check the evidence locations of the original final verdict against the actual candidate material; do not decide from the scores alone.
- **C08, C18**: first check the same-title and same-work version relationship. For C18, two Qwen pair outputs failed validation of their attribution citations; the original probabilities are kept.

## Annotation record

Each record contains at least `case_id`, `label`, `annotator`, `confidence`, `evidence_refs` and `rationale`. The review interface also stored the first judgment, whether model outputs were opened, and modification times. Confidence is the annotator's own estimate and must not be copied from model probabilities.

Two independent annotators, followed by adjudication of disagreements against the papers, are recommended. In this release a single annotator labeled all 20 cases. Repeated reviews keep separate records and never overwrite saved model outputs. A `no_source_finding` label covers only the candidate comparisons listed for the case; if the candidate set is insufficient to judge, use `inconclusive` and say so.
