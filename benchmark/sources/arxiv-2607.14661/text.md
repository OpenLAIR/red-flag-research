# SmartRAG: Native Graph-Based RAG for Mobile Device

## B-0d01d2c4ed591c

https://arxiv.org/html/2607.14661v2#chars-42864-43552

## Appendix A LLM-as-judger protocol

We assess factual correctness using an LLM-as-judger approach ([Zheng et al., 2024](#bib.bib19)). Given a question, a reference answer (or set of acceptable answers), and the model’s prediction, a judge LLM (Claude Haiku 4.5) determines whether the prediction is factually correct under a strict rubric. The judge outputs a binary correctness label per sample; we report the mean across all samples as Correctness (Cr, %). SQuAD-style F1 is computed as standard token-level precision–recall against reference answers. All models are evaluated under identical inference budgets: 4096 token context, top-KK=8 retrieval cutoff, and Q6\_K quantization.

## B-0e3ab95f42d721

https://arxiv.org/html/2607.14661v2#chars-48801-50652

#### Interpretation of the comparison.

We emphasize that these baselines are included as strong and relevant points of comparison, not as strawmen. InstructRAG targets denoising under noisy retrieval; TruthfulRAG targets factual conflict resolution with KG support; and StableRAG targets repeatability and robustness to retrieval variation. These are all reasonable objectives, and each may be better aligned than SmartRAG with other deployment scenarios. Our comparison should therefore be read narrowly: under a unified compact-backbone, quantized, llama.cpp-based setting, SmartRAG is more effective for the particular combination of goals studied in this paper—namely, persistent structured memory, repeated evidence composition, and end-to-end QA under edge-style resource constraints. We do not claim that the released original forms of these methods are inferior in general, nor that they were designed for the same deployment target as SmartRAG.

![[LOGO]](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)

## B-1242eb83f5799e

https://arxiv.org/html/2607.14661v2#chars-8512-9087

#### On-device LLMs.

Recent advances in quantization ([Frantar et al., 2023](#bib.bib26)) and efficient inference engines ([Gerganov, 2023](#bib.bib27)) have made it feasible to run billion-parameter models on mobile hardware ([Xu and others, 2024](#bib.bib5)). Models such as Qwen3 ([Qwen Team, 2025](#bib.bib7)) and Llama 3 ([Grattafiori and others, 2024](#bib.bib6)) offer compact variants targeting edge deployment. However, these efforts focus on the *inference engine* and do not address the *memory* and *continuous adaptation* requirements of a personal assistant.

## B-13067a3c0343d9

https://arxiv.org/html/2607.14661v2#chars-20414-21820

### 3.3 Memory: MRGraph

MRGraph is a three-layer on-device knowledge graph designed for continual writes and efficient retrieval with explicit provenance.

Layer 1: Entity–paragraph graph. The paragraph is the atomic unit for both writing and retrieval. Each paragraph node stores raw content, an in-document index, a pointer to the source document, and an embedding vector. Entity nodes are deduplicated via stable name hashing and linked to paragraphs through association edges. Relations are stored as keyed edges with observation counts to prevent uncontrolled graph growth. Ingestion follows an *evidence-first, structure-second* principle: extracted triplets are first aligned to their best-matching paragraphs, then materialized as relation edges, ensuring every structured fact remains traceable.

Layer 2: Abstraction layer. Above entities, we maintain semantic clusters whose centroids are updated with smoothing as new entities arrive. An anchor–centroid drift metric detects and prevents topic drift. Cluster summaries are maintained incrementally during normal operation, with higher-quality refinement triggered during idle-and-charging periods.

Layer 3: Runtime raw-text view. At query time, retrieved paragraph evidence and the local graph neighborhood are assembled into a context bounded by a token budget, providing the Thinking module with both structured and unstructured evidence.

## B-1985089762a69f

https://arxiv.org/html/2607.14661v2#chars-31238-32442

#### Comparison with RAG baselines.

The baseline pattern also reflects the different objectives of the compared methods. InstructRAG explicitly learns denoising through self-synthesized rationales, StableRAG mitigates permutation sensitivity by aggregating reasoning across multiple retrieval orders, and TruthfulRAG focuses on resolving factual conflicts through triple extraction, KG retrieval, and conflict-aware filtering. These are all meaningful objectives, but they place more burden on the generator’s ability to denoise, aggregate, or filter evidence. Under the smaller Qwen3-1.7B regime, such additional reasoning or filtering stages may not pay off as reliably as direct flat retrieval, which helps explain why these baselines often underperform Naïve RAG there. Under Ministral3-3B, however, the stronger compact backbone appears better able to benefit from these extra mechanisms, so the same baselines become consistently stronger than Naïve RAG. SmartRAG differs in that it does not rely primarily on one-shot denoising or conflict filtering; instead, it combines persistent structured memory with hybrid retrieval, which appears to be more robust across both compact backbone families.

## B-1e2ae220e6994f

https://arxiv.org/html/2607.14661v2#chars-19287-20414

#### Triplet discovery.

Extracted entities are initially categorized into coarse types. For unseen entities, we extract stable semantic vectors via a frozen lightweight embedder and store them in a local vector database. When the count exceeds a threshold, agglomerative clustering with Ward linkage ([Ward, 1963](#bib.bib17)) groups semantically similar mentions. For clusters A,BA,B with sizes |A|,|B||A|,|B| and embedding centroids 𝝁A,𝝁B\boldsymbol{\mu}\_{A},\boldsymbol{\mu}\_{B},

|  |  |  |  |
| --- | --- | --- | --- |
|  | d⁡(A,B)=|A|⋅|B||A|+|B|​∥𝝁A−𝝁B∥22.d(A,B)=\frac{|A|\cdot|B|}{|A|+|B|}\,\lVert\boldsymbol{\mu}\_{A}-\boldsymbol{\mu}\_{B}\rVert\_{2}^{2}. |  | (9) |

Given threshold ϵ>0\epsilon>0, we iteratively merge clusters: whenever some pair (A,B)(A,B) satisfies d⁡(A,B)<ϵd(A,B)<\epsilon, merge them; stop when no such pair remains (all surviving clusters are pairwise at least ϵ\epsilon-separated under dd). The Thinking module then assigns category labels to large coherent clusters. For known-type entities, a lightweight relation classifier identifies relations, producing triplets written into MRGraph.

## B-20adb04a102bd7

https://arxiv.org/html/2607.14661v2#chars-11161-12627

### 3.1 Architecture overview

The SmartRAG architecture ([Figure 1](#S3.F1 "In 3.1 Architecture overview ‣ 3 Method ‣ SmartRAG: Native Graph-Based RAG for Mobile Device")) consists of four interacting modules. The Perception module transforms unstructured text into structured knowledge via EvoNER (an on-device NER component, [Section 3.2](#S3.SS2 "3.2 Perception: EvoNER and entity discovery ‣ 3 Method ‣ SmartRAG: Native Graph-Based RAG for Mobile Device")) and a lightweight relation classifier, producing entity–relation triplets. The Memory module organizes these triplets into MRGraph, a persistent knowledge structure that binds entities and relations to their source paragraphs for provenance ([Section 3.3](#S3.SS3 "3.3 Memory: MRGraph ‣ 3 Method ‣ SmartRAG: Native Graph-Based RAG for Mobile Device")). At query time, the Focus module retrieves and ranks relevant evidence through a hybrid pipeline combining graph traversal, lexical matching, and dense semantic search ([Section 3.4](#S3.SS4 "3.4 Focus: hybrid retrieval ‣ 3 Method ‣ SmartRAG: Native Graph-Based RAG for Mobile Device")). The Thinking module invokes the on-device LLM only for high-value semantic operations: labeling emerging entity types, planning multi-hop retrieval, and synthesizing final answers ([Section 3.5](#S3.SS5 "3.5 Thinking: LLM-driven semantic operations ‣ 3 Method ‣ SmartRAG: Native Graph-Based RAG for Mobile Device")).

![Refer to caption](2607.14661v2/system.png)

## B-2234c0bdd8613b

https://arxiv.org/html/2607.14661v2#chars-12627-12676

### 3.2 Perception: EvoNER and entity discovery

## B-24daf31dc3e674

https://arxiv.org/html/2607.14661v2#chars-33304-38434

### 4.3 On-device feasibility

A central question for SmartRAG is whether the *entire* pipeline remains usable when memory construction, retrieval, and answer generation are all executed on-device. To answer this, we profile two smartphone platforms with two different model sizes, and separately measure the end-to-end RAG pipeline. [Table 2](#S4.T2 "In 4.3 On-device feasibility ‣ 4 Experiments ‣ SmartRAG: Native Graph-Based RAG for Mobile Device") defines shorthand labels S0–S3 for each hardware–backbone pair, which are used throughout this section.

|  |  |  |
| --- | --- | --- |
|  | Qwen3-1.7B | Qwen3-4B |
| OnePlus 15 (Snapdragon 8 Elite Gen 5, 16 GB) | S0 | S1 |
| OnePlus 13 (Snapdragon 8 Elite, 16 GB) | S2 | S3 |

In general, the measurements reveal a clear usability boundary. While both backbones can be executed on-device, the 1.7B model remains in the practically deployable regime, whereas the 4B model substantially weakens interactivity once the full retrieval-augmented pipeline is taken into account.

We first examine resource usage during triplet extraction and QA. As summarized in [Table 3](#S4.T3 "In 4.3 On-device feasibility ‣ 4 Experiments ‣ SmartRAG: Native Graph-Based RAG for Mobile Device"), the 4B backbone consistently incurs a substantially heavier memory footprint than 1.7B on both devices. This gap appears in both triplet extraction and end-to-end QA, where the 1.7B settings remain around the 4–5.5 GB range while the 4B settings rise to roughly 6.5–6.8 GB. This difference matters because SmartRAG runs as a full on-device pipeline, with model weights, retrieval-conditioned prefilling, and runtime memory operations sharing the same limited mobile memory budget.

More broadly, the measured power remains relatively low because we intentionally adopt a conservative system configuration: we prioritize stable long-term execution so that SmartRAG can remain deployable as a persistent on-device system. This choice leaves some hardware capacity unused, which in turn contributes to the non-trivial TTFT observed in the full QA setting.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Config | Triplet Extraction | | QA | |
| PSS Memory (MB) | Power (W) | PSS Memory (MB) | Power (W) |
| S0 | 5527.31 | 4.74 | 4149.72 | 2.85 |
| S1 | 6717.55 | 4.77 | 6803.68 | 5.36 |
| S2 | 5099.07 | 2.93 | 4153.38 | 2.12 |
| S3 | 6643.01 | 2.37 | 6512.62 | 2.12 |

The more decisive separation appears in latency, shown in [Figure 2](#S4.F2 "In 4.3 On-device feasibility ‣ 4 Experiments ‣ SmartRAG: Native Graph-Based RAG for Mobile Device"). Question decomposition remains comparatively light-weight across all settings. For the S0 configuration (Snapdragon 8 Elite Gen 5 with Qwen3-1.7B), the median decomposition TTFT is 1.32 s1.32\text{\,}\mathrm{s}, which confirms that this planning stage remains near the low-second regime. By contrast, full QA is much more expensive because the model must absorb retrieved evidence before decoding the answer. Under the same S0 setting, the median QA TTFT rises to 36.9 s36.9\text{\,}\mathrm{s}, indicating that the dominant latency cost comes from retrieval-conditioned prefilling rather than from the decomposition step itself. The 4B settings (S1 and S3) are visibly slower in [Figure 2](#S4.F2 "In 4.3 On-device feasibility ‣ 4 Experiments ‣ SmartRAG: Native Graph-Based RAG for Mobile Device"), moving further away from an interactive operating point.

The same conclusion is reinforced by the generation stage in [Figure 3](#S4.F3 "In 4.3 On-device feasibility ‣ 4 Experiments ‣ SmartRAG: Native Graph-Based RAG for Mobile Device"). In the S0 runlog, the median decoding time is 8.11 s8.11\text{\,}\mathrm{s} for question decomposition and 8.55 s8.55\text{\,}\mathrm{s} for QA, while the mean QA decoding time is higher (14.81 s14.81\text{\,}\mathrm{s}) because answer lengths vary substantially across samples. This pattern again suggests that the main systems bottleneck is not the decomposition step itself, nor even decoding alone, but the long prefilling stage required by retrieval-conditioned QA. More broadly, [Figure 3](#S4.F3 "In 4.3 On-device feasibility ‣ 4 Experiments ‣ SmartRAG: Native Graph-Based RAG for Mobile Device") shows the same qualitative ordering across devices and backbone sizes: the 1.7B backbone decodes faster than 4B, and the smaller configurations remain more favorable for end-to-end deployment.

The memory, TTFT, and decoding measurements explain why we standardize on the 1.7B backbone in the main accuracy experiments. Although the 4B model is technically executable on smartphones, its larger memory footprint, much longer retrieval-conditioned prefilling time, and slower generation place it beyond a practically interactive regime for end-to-end on-device RAG. We also note that system software still matters: even under closely related Snapdragon-class hardware, OS scheduling and runtime policies can noticeably affect realized throughput. The reported numbers should therefore be interpreted as conservative end-to-end baselines for deployable on-device operation rather than absolute hardware limits.

## B-34f8cd06f38b1e

https://arxiv.org/html/2607.14661v2#chars-18461-19287

#### Three-stage parameter-efficient updates.

To accommodate the unpredictability of mobile scheduling, we adopt a three-stage optimization schedule with progressively increasing trainable capacity. Let Θ\Theta denote all parameters, Θhead\Theta\_{\mathrm{head}} non-encoder parameters (heads and adapters), and Θtop​K\Theta\_{\mathrm{top}K} the top-KK Transformer blocks (counted from the output side):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Θ1=Θhead,Θ2=Θhead∪Θtop​K,Θ3=Θ.\Theta\_{1}=\Theta\_{\mathrm{head}},\quad\Theta\_{2}=\Theta\_{\mathrm{head}}\cup\Theta\_{\mathrm{top}K},\quad\Theta\_{3}=\Theta. |  | (8) |

Stage 1 adapts only heads; Stage 2 adds partial encoder layers; Stage 3 allows brief full-model consolidation at a low learning rate. Training may stop after any stage if the device budget is exhausted.

## B-3caed8478c998c

https://arxiv.org/html/2607.14661v2#chars-46966-47922

#### TruthfulRAG.

TruthfulRAG is a KG-based framework for resolving factual-level conflicts in RAG, whose pipeline includes knowledge-graph generation, graph retrieval, and entropy-based filtering before final response generation. In our evaluation, we preserved this overall conflict-aware graph-processing logic while replacing the original model-serving setup with the same compact quantized backbones and llama.cpp backend used elsewhere in the paper. Because TruthfulRAG contains additional graph-construction and filtering stages beyond a standard lightweight RAG loop, we did not deploy it as an end-to-end real-phone pipeline. Instead, we evaluate it in the same cloud-side simulation environment as the other RAG baselines. This makes the comparison more controlled at the backbone and inference level, while acknowledging that TruthfulRAG was originally designed for a somewhat different operating point than a strict mobile deployment target.

## B-3cdfec626d2a71

https://arxiv.org/html/2607.14661v2#chars-24882-24900

## 4 Experiments

## B-43658d80e57ce0

https://arxiv.org/html/2607.14661v2#chars-28166-30565

### 4.2 Main results: structured memory improves small-backbone QA under on-device constraints

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Base Model | Method | TriviaQA | | NQ | | HotpotQA | | MultiHopQA | |
|  |  | Cr | F1 | Cr | F1 | Cr | F1 | Cr | F1 |
| Qwen3 | | | | | | | | | |
| LLM-only (no retrieval) | | | | | | | | | |
|  | Qwen3-1.7B | 22.10 | 21.52 | 9.10 | 10.17 | 14.15 | 13.00 | 22.00 | 19.18 |
|  | Qwen3-4B | 28.70 | 37.66 | 23.15 | 19.95 | 24.00 | 22.29 | 30.05 | 29.29 |
|  | Qwen3-32B | 51.45 | 42.26 | 40.15 | 35.92 | 33.25 | 30.56 | 31.54 | 32.69 |
| Retrieval-augmented (1.7B) | | | | | | | | | |
|  | Naïve RAG | 47.00 | 36.31 | 62.24 | 37.23 | 41.55 | 37.80 | 45.66 | 34.58 |
|  | InstructRAG | 43.15 | 22.67 | 41.30 | 34.99 | 33.90 | 26.15 | 13.90 | 12.94 |
|  | StableRAG | 45.16 | 21.89 | 17.30 | 11.14 | 41.15 | 26.11 | 5.05 | 0.75 |
|  | TruthfulRAG | 47.10 | 22.86 | 45.10 | 26.38 | 40.71 | 25.51 | 19.95 | 12.64 |
|  | SmartRAG (ours) | 50.00 | 48.68 | 66.68 | 54.84 | 63.93 | 51.27 | 50.17 | 41.86 |
| Ministral3 | | | | | | | | | |
| LLM-only (no retrieval) | | | | | | | | | |
|  | Ministral3-3B | 35.84 | 28.27 | 24.43 | 18.81 | 16.98 | 19.19 | 17.33 | 26.56 |
|  | Ministral3-14B | 60.70 | 60.87 | 37.80 | 34.55 | 22.40 | 25.34 | 20.12 | 31.45 |
| Retrieval-augmented (3B) | | | | | | | | | |
|  | Naïve RAG | 41.71 | 33.02 | 42.99 | 32.02 | 36.96 | 27.08 | 15.95 | 14.81 |
|  | InstructRAG | 50.25 | 28.74 | 50.60 | 45.39 | 42.65 | 37.41 | 28.75 | 26.27 |
|  | StableRAG | 15.95 | 10.86 | 27.35 | 18.11 | 44.03 | 32.94 | 13.71 | 9.07 |
|  | TruthfulRAG | 47.86 | 25.52 | 53.00 | 31.31 | 47.86 | 35.38 | 43.20 | 33.67 |
|  | SmartRAG (ours) | 59.74 | 36.76 | 63.86 | 54.07 | 66.74 | 46.08 | 57.60 | 43.37 |

[Table 1](#S4.T1 "In 4.2 Main results: structured memory improves small-backbone QA under on-device constraints ‣ 4 Experiments ‣ SmartRAG: Native Graph-Based RAG for Mobile Device") compares SmartRAG against both LLM-only capacity references and lightweight retrieval baselines across the Qwen3 and Ministral3 families. Overall, SmartRAG delivers the clearest gains on NQ, HotpotQA, and MultiHopQA, while remaining competitive on TriviaQA. This pattern is consistent across both model families, suggesting that the main benefit of SmartRAG lies in structured evidence acquisition and composition.

## B-44a99f4ca370d3

https://arxiv.org/html/2607.14661v2#chars-41660-42303

#### Limitations.

(1) The current planner is heuristic and does not uniformly benefit all question types; learned planning strategies could address this. (2) On-device QA latency, while acceptable for the 1.7B backbone, is dominated by retrieval-conditioned prefilling and would benefit from evidence compression techniques. (3) Typed NER remains low in AI and Politics despite surface gains; improving type-consistent discovery and clustering is still a major lever, even when Token-F1 and Hit@1 already move in the right direction. (4) Our evaluation is limited to English-language benchmarks; multilingual adaptation remains future work.

## B-46a239fde439b3

https://arxiv.org/html/2607.14661v2#chars-43827-44818

## Appendix C Baseline implementation details and deployment notes

To make the comparison with prior RAG baselines as fair and transparent as possible, we implemented Naïve RAG, InstructRAG, StableRAG, and TruthfulRAG under a unified evaluation backend and quantization setting. In all cases, we used the same llama.cpp inference backend and the same model quantization scheme as in our main experiments, and instantiated the baselines with the same compact backbone families reported in [Table 1](#S4.T1 "In 4.2 Main results: structured memory improves small-backbone QA under on-device constraints ‣ 4 Experiments ‣ SmartRAG: Native Graph-Based RAG for Mobile Device"). This appendix clarifies an important distinction: unlike SmartRAG, these baselines were *not* profiled as end-to-end real-phone deployments. Instead, they were executed in a cloud-side simulation environment designed to match the same inference backend, quantized models, and retrieval budget as closely as possible.

## B-4ad93730dfc61e

https://arxiv.org/html/2607.14661v2#chars-263-1788

###### Abstract

Deploying large language models (LLMs) as personal assistants on mobile devices demands privacy, low latency, and offline availability, yet the computational cost of giant models clashes with strict edge-hardware budgets. We argue that this tension cannot be resolved by model compression alone; it requires decomposing on-device intelligence into complementary functional roles. We present SmartRAG, a fully on-device framework that organizes an intelligent assistant around four coordinated modules—*Perception*, *Memory*, *Focus*, and *Thinking*. At the core of SmartRAG is EvoNER, a continually learnable named-entity recognizer that incrementally expands its label inventory through teacher-distilled updates, enabling the system to absorb previously unseen entity types without retraining the backbone LLM. Extracted knowledge is stored in MRGraph, a three-layer provenance-preserving knowledge graph, and retrieved at query time through a hybrid pipeline combining graph traversal, lexical matching, and dense semantic search. The on-device LLM is invoked only for high-value semantic operations—labeling, planning, and answer synthesis—keeping inference costs bounded. Experiments on four QA benchmarks (TriviaQA, Natural Questions, HotpotQA, MultiHopQA) show that SmartRAG with a quantized 1.7B-parameter backbone achieves multi-hop reasoning performance competitive with models up to 18×\times larger, while running entirely on commodity smartphones within practical memory and latency envelopes.

## B-5b58cfac109160

https://arxiv.org/html/2607.14661v2#chars-40423-40990

#### The retrieval–precision trade-off.

Our analysis of the HotpotQA gap between SmartRAG and Naïve RAG reveals a fundamental trade-off in graph-structured retrieval. While graph traversal introduces relationships between nodes that enhance multi-hop reasoning, it also surfaces structurally related but contextually peripheral evidence. For open-ended questions where direct vector matching suffices, this can decrease recall. Intelligent search strategies that dynamically balance graph depth against retrieval precision represent a promising research direction.

## B-70a8cc01464149

https://arxiv.org/html/2607.14661v2#chars-44818-46099

#### Why these baselines were not deployed as real-phone end-to-end systems.

Our goal in the baseline comparison is to evaluate answer quality under a matched compact-backbone regime, rather than to claim that every baseline is equally suitable for direct mobile deployment. The original formulations of InstructRAG, StableRAG, and TruthfulRAG introduce additional stages that make them difficult to treat as drop-in phone pipelines. InstructRAG explicitly denoises retrieved contents through self-synthesized rationales and supports both in-context learning (ICL) and supervised fine-tuning (SFT). TruthfulRAG introduces additional KG-oriented processing steps, including knowledge-graph construction, graph retrieval, and entropy-based filtering. StableRAG emphasizes repeatability, frozen retrieval, and structured output normalization, with a pipeline that depends on OpenAI-style generation and embedding calls together with a persistent retrieval store. These original designs are meaningful in their intended settings, but they differ substantially from a single-pass compact on-device assistant stack. For this reason, we treat them as *reference RAG baselines evaluated under a matched backend and quantization setup*, rather than as directly deployable mobile systems.

## B-843ad00f5e7965

https://arxiv.org/html/2607.14661v2#chars-9087-9934

#### Retrieval-augmented generation.

RAG ([Lewis et al., 2020](#bib.bib1)) augments LLMs with external knowledge at inference time. Dense passage retrieval ([Karpukhin et al., 2020](#bib.bib25)) provides the standard retrieval backbone. Self-RAG ([Asai et al., 2024](#bib.bib2)) internalizes retrieval behaviors through specialized training, and xRAG ([Cheng et al., 2024](#bib.bib3)) compresses retrieved context into compact representations. Graph-based approaches ([Edge et al., 2024](#bib.bib4)) organize retrieved knowledge into structured graphs for improved multi-hop reasoning. Multi-hop QA methods ([Trivedi et al., 2023](#bib.bib22); [Press et al., 2023](#bib.bib23)) interleave retrieval with chain-of-thought reasoning. Most of these systems assume cloud-scale compute; our work targets their adaptation to strict on-device budgets.

## B-8d2b0d5db70e0f

https://arxiv.org/html/2607.14661v2#chars-50652-51991

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile
support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the
methods listed below:

**Tip:** You can select the relevant text first, to include it in your report.

Our team has already identified [the following issues](https://github.com/arXiv/html_feedback/issues). We appreciate your time reviewing and reporting rendering errors we
may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability
should not be a barrier to accessing research. Thank you for your continued support in championing open access for
all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a [list of packages that need conversion](https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML), and welcome [developer contributions](https://github.com/brucemiller/LaTeXML/issues).

![Simons Foundation](/static/base/1.0.1/images/funders/simons-foundation.png)
![Simons Foundation International](/static/base/1.0.1/images/funders/simons-foundation-international.png)
![Schmidt Sciences](/static/base/1.0.1/images/funders/schmidt-sciences.png)

## B-8d3d850949620b

https://arxiv.org/html/2607.14661v2#chars-11148-11161

## 3 Method

## B-8e4ac2f62a66a0

https://arxiv.org/html/2607.14661v2#chars-12676-14346

#### Span-based NER with character injection.

We design EvoNER (Evolutionary Named Entity Recognition) to satisfy four on-device requirements: lightweight co-existence with the LLM, accurate entity boundary and type prediction, robustness to out-of-vocabulary surface forms, and support for continual label expansion. Given an input sentence, we encode it into sub-word representations and enumerate candidate spans from word-start positions up to a maximum width WW:

|  |  |  |  |
| --- | --- | --- | --- |
|  | r=(i,j),1≤i≤j≤n,(j−i+1)≤W,r=(i,j),\qquad 1\leq i\leq j\leq n,\qquad(j-i+1)\leq W, |  | (1) |

where rr denotes a candidate span, ii and jj are its inclusive word-level start and end indices, nn is the sentence length in words, and WW caps span width (W=10W{=}10 in our implementation), yielding O⁡(n​W)O(nW) candidates instead of all O⁡(n2)O(n^{2}) spans. To improve robustness to misspellings and rare surface forms, we augment the contextual representation with a character-level feature injected at the first subword of each word:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐡t=[𝐞t;mt⋅𝐜⁡(t)],\mathbf{h}\_{t}=[\mathbf{e}\_{t}\,;\,m\_{t}\cdot\mathbf{c}(t)], |  | (2) |

where 𝐡t\mathbf{h}\_{t} is the final representation at subword position tt, 𝐞t\mathbf{e}\_{t} is the Transformer contextual embedding at tt, mt∈{0,1}m\_{t}\in\{0,1\} is 11 on the first subword of a word and 00 otherwise, 𝐜⁡(t)\mathbf{c}(t) is the character-level embedding aligned with that word, and [;][\,;\,] denotes concatenation. Each candidate span is represented using boundary features, element-wise interaction, and a learned width embedding, then passed to a classifier.

## B-8e9655f82ae766

https://arxiv.org/html/2607.14661v2#chars-30565-31238

#### SmartRAG is most effective on knowledge-intensive and evidence-composition benchmarks.

Across both backbone families, the clearest gains of SmartRAG appear on NQ, HotpotQA, and MultiHopQA, where it consistently ranks at or near the top within each block. By contrast, TriviaQA is more mixed: SmartRAG remains competitive, but its advantage is less uniform than on the other three benchmarks. This pattern suggests that SmartRAG is especially effective when answering requires retrieving, organizing, and composing dispersed evidence, whereas direct open-domain factoid questions can often be handled well by larger parametric models or simpler retrieval strategies.

## B-979d183332b632

https://arxiv.org/html/2607.14661v2#chars-8493-8512

## 2 Related work

## B-988677d0b80ba8

https://arxiv.org/html/2607.14661v2#chars-15766-18461

#### Incremental learning with teacher distillation.

When new entity types emerge, EvoNER must incorporate the supervision without degrading performance on existing types. We pair the reserved-label design with teacher-guided distillation on the base-label subspace only. Let Ω⁡(x)\Omega(x) be the set of candidate spans in sentence xx. The task loss matches offline training:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒtask=ℒspan+12​(ℒstart+ℒend),\mathcal{L}\_{\mathrm{task}}=\mathcal{L}\_{\mathrm{span}}+\tfrac{1}{2}\big(\mathcal{L}\_{\mathrm{start}}+\mathcal{L}\_{\mathrm{end}}\big), |  | (4) |

where ℒspan\mathcal{L}\_{\mathrm{span}} is masked span classification over candidates and ℒstart,ℒend\mathcal{L}\_{\mathrm{start}},\mathcal{L}\_{\mathrm{end}} are auxiliary boundary losses on mention endpoints. The full incremental objective is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒinc=ℒtask+λKD​ℒKD,\mathcal{L}\_{\mathrm{inc}}=\mathcal{L}\_{\mathrm{task}}+\lambda\_{\mathrm{KD}}\,\mathcal{L}\_{\mathrm{KD}}, |  | (5) |

with λKD\lambda\_{\mathrm{KD}} trading stability against plasticity. For each span r∈Ω⁡(x)r\in\Omega(x), let ℓrT,base,ℓrS,base∈ℝ1+nbase\boldsymbol{\ell}\_{r}^{T,\mathrm{base}},\boldsymbol{\ell}\_{r}^{S,\mathrm{base}}\in\mathbb{R}^{1+n\_{\mathrm{base}}} denote teacher and student logits *restricted to the base subspace*, where nbasen\_{\mathrm{base}} is the number of deployed base entity types (the leading dimension accounts for the no-entity logit). With temperature TkdT\_{\mathrm{kd}} and confidence threshold τ\tau, define the gate

|  |  |  |  |
| --- | --- | --- | --- |
|  | mr=𝕀[max1≤k≤1+nbase[softmax(ℓrT,base/Tkd)]k≥τ],m\_{r}=\mathbb{I}\!\left[\max\_{1\leq k\leq 1+n\_{\mathrm{base}}}\big[\mathrm{softmax}\big(\boldsymbol{\ell}\_{r}^{T,\mathrm{base}}/T\_{\mathrm{kd}}\big)\big]\_{k}\geq\tau\right], |  | (6) |

i.e., the gate is on when the teacher’s peak probability on base classes exceeds τ\tau.
The distillation loss is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒKD=Tkd2∑r∈Ω⁡(x)mr+ϵ∑r∈Ω⁡(x)mrKL(softmax(ℓrT,base/Tkd)∥softmax(ℓrS,base/Tkd)),\mathcal{L}\_{\mathrm{KD}}=\frac{T\_{\mathrm{kd}}^{2}}{\sum\_{r\in\Omega(x)}m\_{r}+\epsilon}\sum\_{r\in\Omega(x)}m\_{r}\,\mathrm{KL}\!\left(\mathrm{softmax}\!\big(\boldsymbol{\ell}\_{r}^{T,\mathrm{base}}/T\_{\mathrm{kd}}\big)\,\big\|\,\mathrm{softmax}\!\big(\boldsymbol{\ell}\_{r}^{S,\mathrm{base}}/T\_{\mathrm{kd}}\big)\right), |  | (7) |

where ϵ\epsilon avoids division by zero. Reserved logits are *not* distilled, so new types remain plastic while the teacher anchors old boundaries. The teacher is frozen for an entire incremental round, then the updated student may become the next teacher.

## B-9dc4c954e9a761

https://arxiv.org/html/2607.14661v2#chars-209-263

# SmartRAG: Native Graph-Based RAG for Mobile Device

## B-9ea4107ea40291

https://arxiv.org/html/2607.14661v2#chars-32442-33304

#### Compact backbones versus larger capacity references.

The goal of SmartRAG is to improve what compact backbones can achieve under strict on-device constraints. [Table 1](#S4.T1 "In 4.2 Main results: structured memory improves small-backbone QA under on-device constraints ‣ 4 Experiments ‣ SmartRAG: Native Graph-Based RAG for Mobile Device") reflects this trade-off clearly. Larger standalone models still remain strongest on some direct factoid settings, most notably Qwen3-32B and Ministral3-14B on TriviaQA. At the same time, SmartRAG repeatedly matches or exceeds these larger LLM-only references on NQ, HotpotQA, and MultiHopQA. In conclusion, these results support the central claim of the paper: under device constraints, improving memory construction and evidence organization can be at least as important as increasing the parameter count alone.

## B-a7be0fdab4df79

https://arxiv.org/html/2607.14661v2#chars-38434-38838

### 4.4 Ablation study

Using MultiHopQA as the test set, we ablate three core components of SmartRAG: MRGraph (no\_MRGraph), the LLM-based retrieval planner (no\_THINKING\_PLAN), and the hybrid retrieval design (no\_Hybrid\_Retrieval, i.e., graph-only retrieval). The results are shown in [Figure 4](#S4.F4 "In 4.4 Ablation study ‣ 4 Experiments ‣ SmartRAG: Native Graph-Based RAG for Mobile Device").

## B-a8a13eab5ff992

https://arxiv.org/html/2607.14661v2#chars-46099-46966

#### InstructRAG.

InstructRAG is a framework that explicitly denoises retrieved contents by generating rationales, and supports both in-context learning (ICL) and supervised fine-tuning (SFT). In our experiments, we implemented the method as described in the original paper, replacing the original serving stack with the same quantized compact backbones and llama.cpp backend used in our main experiments. We did not attempt to reproduce the original large-scale fine-tuning regime; instead, we adapted the method to the same compact-backbone comparison regime used for the other baselines. We therefore interpret the resulting numbers as measuring how well the *InstructRAG-style denoising strategy* transfers to compact quantized backbones under a unified inference setting, rather than as a claim about the maximum achievable performance of the original method.

## B-b3e3d047020192

https://arxiv.org/html/2607.14661v2#chars-43552-43827

## Appendix B Device specifications

|  |  |  |
| --- | --- | --- |
|  | OnePlus 13 | OnePlus 15 |
| SoC | Snapdragon 8 Elite | Snapdragon 8 Elite Gen 5 |
| RAM | 16 GB LPDDR5X | 16 GB LPDDR5X |
| Storage | 256 GB UFS 4.0 | 256 GB UFS 4.0 |
| OS | ColorOS 16 | ColorOS 16 |

## B-be724150551840

https://arxiv.org/html/2607.14661v2#chars-38838-39945

#### Key findings.

As shown in [Figure 4](#S4.F4 "In 4.4 Ablation study ‣ 4 Experiments ‣ SmartRAG: Native Graph-Based RAG for Mobile Device"), the full SmartRAG system achieves the best performance, with a Token-F1 of 0.5484. Removing MRGraph causes the largest degradation, dropping Token-F1 to 0.4151, which indicates that the structured memory module is the most important component for downstream multi-hop QA in this setting. Disabling the Thinking planner also reduces performance to 0.5069, suggesting that explicit multi-hop planning improves evidence acquisition even when the remaining retrieval and answering pipeline is preserved. Replacing hybrid retrieval with graph-only retrieval further lowers Token-F1 to 0.4749, showing that graph traversal alone is insufficient and that SmartRAG benefits from combining graph-based signals with complementary retrieval channels. Overall, the ablation results support the full SmartRAG design: structured memory, planning, and hybrid retrieval each make non-trivial contributions, and their combination yields the strongest end-to-end QA performance.

## B-c032d87a18e6cc

https://arxiv.org/html/2607.14661v2#chars-39945-40423

## 5 Discussion and conclusion

We have presented SmartRAG, an on-device architecture for adaptive question answering that decomposes intelligence into four coordinated functional roles. By shifting continuous adaptation to efficient structured computation and reserving LLM inference for high-value semantic operations, SmartRAG achieves multi-hop reasoning performance competitive with substantially larger cloud-based models while running entirely on commodity smartphones.

## B-cbf17e0cd34617

https://arxiv.org/html/2607.14661v2#chars-42743-42849

## Acknowledgments and Disclosure of Funding

Acknowledgments will be added in the camera-ready version.

## B-d08a6933f4f2be

https://arxiv.org/html/2607.14661v2#chars-23623-24882

### 3.5 Thinking: LLM-driven semantic operations

The on-device LLM is treated as a reusable semantic engine invoked only for operations requiring high-level language understanding, through four roles:

Labeling. For entity clusters that cannot be confidently typed, the LLM proposes new type names. Let ℳ\mathcal{M} denote the multiset of mentions awaiting labels; cluster​(ℳ)\text{cluster}(\mathcal{M}) groups them into clusters, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​𝒯=LLM​(cluster​(ℳ))\Delta\mathcal{T}=\text{LLM}\big(\text{cluster}(\mathcal{M})\big) |  | (10) |

returns a set of new type strings Δ​𝒯\Delta\mathcal{T} for coherent clusters. Semantically dispersed clusters are rejected to avoid polluting the type space.

Summarization. The knowledge graph is periodically clustered into communities, and the LLM produces summaries re-inserted as upper-layer paragraphs, forming a self-compressing memory loop.

Planning. Complex questions are decomposed into multi-hop retrieval plans before evidence acquisition, reducing search ambiguity under strict on-device budgets.

Answering. The LLM generates responses conditioned on retrieved evidence, constrained to structured schemas that favor extractive grounding to reduce hallucination.

## B-d337f8b4583a8d

https://arxiv.org/html/2607.14661v2#chars-1788-8493

## 1 Introduction

In recent years, as the application of large language models (LLMs) in real-world interactive tasks continues to deepen, memory is gradually emerging as a critical capability in LLM system determining whether the system can support long-term personalization, continuous knowledge updates, and contextually consistent reasoning. This issue is of particular significance for on-device scenarios, as the core value of such deployments lies precisely in data locality, privacy protection, and personalized services capabilities that inherently require the system to establish and maintain a local memory built around the user’s private data, device-local content, and environmental context. Given the strict constraints on system-memory (i.e., RAM usage and runtime memory footprint on edge devices), power consumption, and latency budgets inherent to devices, heavyweight LLMs are difficult to deploy directly; furthermore, relying solely on the limited parametric memory of lightweight models often proves insufficient to support continuous updates, user customization, and knowledge-intensive reasoning. Retrieval-Augmented Generation (RAG) addresses this challenge by integrating LLMs with external, non-parametric memory, thereby providing a memory mechanism that is updatable, structured, and more easily personalized; consequently, it is widely regarded as a highly promising solution.

Although on-device RAG has recently achieved preliminary progress, most existing methods remain centered on naive vector retrieval—that is, relying on semantic similarity between queries and document snippets to facilitate memory access. While this paradigm is well-suited for handling problems involving local matching, it struggles to address complex queries that require cross-segment evidence aggregation, entity linking, and multi-step reasoning. To address this limitation, on-cloud RAG research has begun to leverage graph structures to enhance the retrieval process, explicitly modeling the connections between entities, relations, and evidence to improve multi-hop question-answering capabilities. However, the majority of existing graph-based RAG methods are built upon powerful models, relying heavily on models with tens of billions of parameters to execute critical steps such as graph construction, summarization, and relation organization. While this premise may hold true in cloud-based environments, it clearly fails in on-device scenarios: on-device systems simply cannot bear the computational, latency, energy, and cost overheads associated with models of such scale.

Based on this issue, we believe that the key to on-device RAG lies not in directly compressing cloud-based graph RAGs onto the device, but in rethinking how structured memory should be built and utilized under resource-constrained conditions. In other words, graph construction capabilities do not necessarily stem from the generation capabilities of super-powerful models; they can also arise from more sophisticated system architecture design. By rationally dividing module responsibilities, controlling the granularity of knowledge organization, and designing incrementally evolving memory formation mechanisms, lightweight components can also gradually build a structured knowledge foundation that supports complex reasoning. Unlike traditional graph-based RAG methods, our approach emphasizes a systematic decoupling of knowledge extraction, memory organization, and reasoning support, allowing these processes to be collaboratively completed by multiple lightweight modules under on-device constraints. This provides an implementation path for on-device RAGs that differs from the cloud paradigm.

However, several key technical challenges remain to be addressed before this approach can be truly implemented on device. First, due to budget constraints related to system-memory, power consumption, and latency, only lightweight models are deployable on device. These models are insufficient in open environments to identify unknown entities, long-tail concepts, and new knowledge, making it difficult to directly construct high-quality structured knowledge like large cloud-based models. Therefore, the system must possess the ability to discover, aggregate, and continuously absorb unseen entities. Furthermore, complex queries often require entity association tracing and multi-step retrieval across multiple pieces of evidence. However, edge scenarios cannot rely on powerful models to repeatedly perform query decomposition, path planning, and graph exploration. This makes achieving structured focus for complex problems within a limited budget another core challenge. Finally, even after relevant evidence has been retrieved, lightweight generation models struggle to reliably complete reasoning within lengthy and noisy contexts. Therefore, a controlled evidence organization method is needed to confine the final generation to a compact and high-value context.

Based on this understanding, we propose SmartRAG, a structured RAG framework for on-device scenarios. Its core objective is to build external memory capable of supporting complex reasoning under lightweight models and limited resources. Unlike existing methods that rely on powerful models to directly complete graph construction and graph-based reasoning, SmartRAG decouples knowledge extraction, memory organization, retrieval focus, and answer generation through modular design, enabling these processes to operate collaboratively under edge-side constraints. Thus, SmartRAG transforms the structured knowledge capability from LLMs capability into a system architecture problem, providing a more practical implementation method for on-device RAGs.

Our contributions are as follows:

We identify the core feasibility problem of on-device structured RAG: complex reasoning requires structured and updatable memory, but existing graph-construction pipelines depend too heavily on powerful LLMs to remain sustainable on edge devices.

We present SmartRAG, an on-device structured RAG method that reallocates high-frequency memory writing to lightweight trainable components while reserving the LLM for sparse, high-value semantic operations.

We develop EvoNER, a continually learnable entity recognizer that absorbs previously unseen semantic categories through lightweight incremental updates, enabling the system to recognize and organize emerging concepts without retraining the backbone LLM.

We integrate provenance-preserving structured memory and hybrid retrieval into a full on-device pipeline, and demonstrate on real smartphones that this design yields strong end-to-end QA performance under strict device constraints.

## B-d59547366aa08b

https://arxiv.org/html/2607.14661v2#chars-9934-10669

#### Named entity recognition and continual learning.

Span-based NER ([Yu et al., 2020](#bib.bib20); [Fu et al., 2021](#bib.bib21)) formulates entity detection as span classification over enumerated candidates, avoiding the label dependency of sequential taggers. Continual learning for NER ([Monaikul et al., 2021](#bib.bib10)) addresses the challenge of absorbing new entity types without forgetting old ones, commonly using knowledge distillation ([Hinton et al., 2015](#bib.bib9)) or regularization ([Kirkpatrick et al., 2017](#bib.bib8)). Our EvoNER combines span-based detection with a reserved-label classifier and teacher-distilled incremental updates, specifically designed for on-device expansion of the entity vocabulary.

## B-db3f089150a0a4

https://arxiv.org/html/2607.14661v2#chars-21820-23623

### 3.4 Focus: hybrid retrieval

At query time, the Thinking module decomposes the question into a retrieval plan 𝒫=(e0,{rh,th}h=1H)\mathcal{P}=(e\_{0},\{r\_{h},t\_{h}\}\_{h=1}^{H}), where e0e\_{0} is the seed entity, HH is the number of hops, and for each hop h∈{1,…,H}h\in\{1,\ldots,H\}, rhr\_{h} is a natural-language relation phrase (e.g., “*published in*”) and tht\_{h} is the desired target entity type for that hop.

Stage 1: Plan-guided multi-hop text retrieval. For each hop, the system constructs local queries by combining the current center entity with the relation phrase, retrieves candidate paragraphs using fused lexical and dense similarity scores, and selects evidence under a token budget via maximal marginal relevance (MMR). Retrieved paragraphs are used to infer next-hop entity centers.

Stage 2: Graph-structured augmentation. Bridge entities from Stage 1 seed a graph traversal. For each node, we compare its concatenation with the query against abstraction-layer summaries, select top-ranked clusters, and perform top-down retrieval to expand the subgraph. Personalized PageRank ([Page et al., 1999](#bib.bib24)) estimates node importance, and connected subgraph blocks are assembled with supporting paragraphs.

Stage 3: Full-document fallback. If the first two stages provide insufficient evidence, global retrieval over documents provides a last-resort mechanism. Because on-device context length is limited, entities inevitably split across paragraphs; full-document fallback recovers these cross-boundary references.

Finally, retrieved evidence is post-processed: local context windows around entity mentions are extracted, sentence-level compression removes redundancy, and hash-based deduplication filters near-duplicates before packing the final context for the LLM.

## B-ddfd5bdf886001

https://arxiv.org/html/2607.14661v2#chars-14346-15766

#### Reserved-label mechanism for continual expansion.

A key requirement for continual on-device learning is adding new entity types without reinitializing the classifier. We pre-allocate a fixed label capacity and partition the span classifier into a *base* head (no-entity label plus deployed entity types) and *reserved* rows for future types. For span (i,j)(i,j) with pooled representation 𝐳i​j∈ℝd\mathbf{z}\_{ij}\in\mathbb{R}^{d}, logits decompose as

|  |  |  |  |
| --- | --- | --- | --- |
|  | [ℓi​jbaseℓi​jresv]=[𝐖base𝐖resv]​𝐳i​j+[𝐛base𝐛resv],ℓi​j=[ℓi​jbase;ℓi​jresv],\begin{bmatrix}\boldsymbol{\ell}^{\text{base}}\_{ij}\\ \boldsymbol{\ell}^{\text{resv}}\_{ij}\end{bmatrix}=\begin{bmatrix}\mathbf{W}\_{\text{base}}\\ \mathbf{W}\_{\text{resv}}\end{bmatrix}\mathbf{z}\_{ij}+\begin{bmatrix}\mathbf{b}\_{\text{base}}\\ \mathbf{b}\_{\text{resv}}\end{bmatrix},\qquad\boldsymbol{\ell}\_{ij}=[\boldsymbol{\ell}^{\text{base}}\_{ij}\,;\,\boldsymbol{\ell}^{\text{resv}}\_{ij}], |  | (3) |

where 𝐖base,𝐛base\mathbf{W}\_{\text{base}},\mathbf{b}\_{\text{base}} (resp. 𝐖resv,𝐛resv\mathbf{W}\_{\text{resv}},\mathbf{b}\_{\text{resv}}) are base (resp. reserved) weights and biases. Reserved slots are initialized inactive (𝐛resv≪0\mathbf{b}\_{\text{resv}}\ll 0, 𝐖resv≈𝟎\mathbf{W}\_{\text{resv}}\approx\mathbf{0}). When new types are discovered, each is mapped to an unused reserved row without changing output dimensionality.

## B-e0d187de04fb07

https://arxiv.org/html/2607.14661v2#chars-42849-42864

## References

## B-e1199166ad5e2d

https://arxiv.org/html/2607.14661v2#chars-10669-11148

#### Knowledge graphs for LLMs.

The integration of knowledge graphs with LLMs ([Ji et al., 2022](#bib.bib11); [Pan et al., 2024](#bib.bib12)) has attracted growing attention. LLM-driven KG construction ([Edge et al., 2024](#bib.bib4)) achieves high-quality extraction but requires large models. Our approach separates the extraction pipeline into a lightweight, trainable perception layer and a sparse LLM control plane, achieving predictable ingestion cost on mobile devices.

## B-e23792316c9a3d

https://arxiv.org/html/2607.14661v2#chars-0-209

##### Report GitHub Issue

Content selection saved. Describe the issue below:

![](/static/base/1.0.1/images/icons/smileybones-small.svg)
![arXiv logo](/static/base/1.0.1/images/arxiv-logo-primary-light.svg)

## B-e48fb03788ea66

https://arxiv.org/html/2607.14661v2#chars-24900-28166

### 4.1 Setup

We use two compact LLM families in this work: Qwen3 ([Qwen Team, 2025](#bib.bib7)) and Ministral3 ([Liu and others, 2026](#bib.bib28)). Both are quantized to Q6\_K via llama.cpp ([Gerganov, 2023](#bib.bib27)). All offline one-time preparation, including quantization, LoRA training, and dataset pre-processing, is performed on a cloud server with two NVIDIA RTX A6000 GPUs, while the full online SmartRAG pipeline—memory ingestion, indexing, retrieval, and answer generation—runs entirely on-device. For multi-hop retrieval planning, we train a task-specific LoRA decomposer ([Hu et al., 2022](#bib.bib18)) on a self-constructed dataset derived from MultiHopQA and HotpotQA, where decomposition targets are generated offline using Claude Opus 4.6 and then filtered by rules with manual verification. The decomposer is used only to generate retrieval plans; final answers are always produced by the quantized backbone conditioned on retrieved evidence. All on-device experiments are conducted on two real smartphones: OnePlus 13 (Snapdragon 8 Elite, 16 GB RAM) and OnePlus 15 (Snapdragon 8 Elite Gen 5, 16 GB RAM).

We evaluate on four QA benchmarks: TriviaQA ([Joshi et al., 2017](#bib.bib13)), Natural Questions ([Kwiatkowski et al., 2019](#bib.bib14)), HotpotQA ([Yang et al., 2018](#bib.bib15)), and MultiHopQA ([Ho et al., 2020](#bib.bib16)). Baselines are divided into two groups. For LLM-only comparison, we evaluate generation without retrieval using Qwen3-1.7B, Qwen3-4B, Qwen3-32B, Ministral3-3B, and Ministral3-14B. Among these, Qwen3-1.7B, Qwen3-4B, and Ministral3-3B represent the compact-model regime that is executable on-device, with 1.7B/3B corresponding to practically deployable scales and 4B serving as a larger but still runnable case. By contrast, Qwen3-32B and Ministral3-14B are treated as large-model capacity references, allowing us to contextualize how far SmartRAG extends the capability of compact backbones. For RAG, we evaluate Naïve RAG ([Lewis et al., 2020](#bib.bib1)), InstructRAG ([Wei et al., 2024](#bib.bib29)), StableRAG ([Zhang et al., 2026](#bib.bib30)), and TruthfulRAG ([Liu et al., 2026](#bib.bib31)), instantiated with two lightweight backbones, Qwen3-1.7B and Ministral3-3B, to match the compact-model regime targeted in this work. These baselines are compared under the same inference budget and retrieval context constraints; additional details on their cloud-side simulation setting are provided in [Appendix C](#A3 "Appendix C Baseline implementation details and deployment notes ‣ SmartRAG: Native Graph-Based RAG for Mobile Device").

We report two complementary metrics. Correctness (Cr) measures whether a prediction is factually correct with respect to the reference answer, using an LLM-as-judger protocol ([Zheng et al., 2024](#bib.bib19)) under a fixed rubric. Token-F1 measures token-level overlap between prediction and reference using a rule-based normalization and matching procedure. Together, these metrics capture both factual validity and surface-level answer overlap. Full evaluation details, including the judge prompt and the Token-F1 computation procedure, are provided in [Appendix A](#A1 "Appendix A LLM-as-judger protocol ‣ SmartRAG: Native Graph-Based RAG for Mobile Device").

## B-eaed2274c7e1ac

https://arxiv.org/html/2607.14661v2#chars-47922-48801

#### StableRAG.

StableRAG is a method designed to improve repeatability and robustness in RAG systems, mitigating retrieval-permutation-induced hallucinations through stable retrieval ordering and structured rendering. In our experiments, we retained the stability-oriented evaluation logic described in the original paper while replacing the original serving configuration with the same compact quantized backbones and llama.cpp backend used in the rest of the paper. As with TruthfulRAG and InstructRAG, we treat the resulting system as a *simulated reference implementation under matched inference conditions*, not as a true smartphone deployment. This distinction is important because StableRAG is primarily designed to study response stability and retrieval repeatability, whereas SmartRAG is optimized for persistent structured memory and end-to-end on-device execution.

## B-f255d5de676ee4

https://arxiv.org/html/2607.14661v2#chars-42303-42743

#### Broader impact.

SmartRAG enables privacy-preserving personal assistants that operate entirely on-device without sending user data to the cloud. While this is broadly positive for user privacy, we note that any system capable of building detailed personal knowledge graphs raises data governance concerns if the device is compromised. Appropriate encryption and access control mechanisms should complement the on-device architecture.

## B-fd3ebd815f3bd6

https://arxiv.org/html/2607.14661v2#chars-40990-41660

#### Why not LLM-native extraction?

Although a fully LLM-native extraction pipeline could reduce modular error accumulation and support richer predicate structures, our profiling shows that even query-time RAG prefilling can push TTFT to the minute scale on commodity smartphones. Making LLMs the primary writer of a continuously updated knowledge graph would introduce unacceptable latency and energy costs, and would require on-device training capabilities that remain impractical. The separation into a lightweight, trainable perception layer and a sparse LLM control plane yields predictable ingestion costs while retaining LLM expressivity where it matters most.

## B-ocr-02495bcdb782a6

B PDF page 12

Elias Frantar, Saleh Ashkboos, Torsten Hoefler, and Dan Alistarh. GPTQ: Accurate post-training quantization for generative pre-trained transformers. International Conference on Learning Representations, 2023.

Jinlan Fu, Xuanjing Huang, and Pengfei Liu. SpanNER: Named entity re-/recognition as span prediction. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics, pages 7183–7195, 2021.

Georgi Gerganov. llama.cpp. GitHub repository, 2023. https://github.com/ggerganov/llama.cpp.

Aaron Grattafiori et al. The Llama 3 herd of models. arXiv preprint arXiv:2407.21783, 2024.

Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. Distilling the knowledge in a neural network. In NIPS Deep Learning and Representation Learning Workshop, 2015.

Xanh Ho, Anh-Khoa Duong Nguyen, Saku Sugawara, and Akiko Aizawa. Constructing a multi-hop QA dataset for comprehensive evaluation of reasoning steps. In Proceedings of the 28th International Conference on Computational Linguistics, pages 6609–6625, 2020.

Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. LoRA: Low-rank adaptation of large language models. In International Conference on Learning Representations, 2022.

Shaoxiong Ji, Shirui Pan, Erik Cambria, Pekka Marttinen, and Philip S Yu. A survey on knowledge graphs: Representation, acquisition, and applications. IEEE Transactions on Neural Networks and Learning Systems, 33(2):494–514, 2022.

Mandar Joshi, Eunsol Choi, Daniel S Weld, and Luke Zettlemoyer. TriviaQA: A large scale distantly supervised challenge dataset for reading comprehension. In Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics, pages 1601–1611, 2017.

Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen-tau Yih. Dense passage retrieval for open-domain question answering. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing, pages 6769–6781, 2020.

James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A Rusu, Kieran Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, Demis Hassabis, Claudia Clopath, Dharshan Kumaran, and Raia Hadsell. Overcoming catastrophic forgetting in neural networks. In Proceedings of the National Academy of Sciences, volume 114, pages 3521–3526, 2017.

Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, et al. Natural questions: A benchmark for question answering research. Transactions of the Association for Computational Linguistics, 7:452–466, 2019.

Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, and Douwe Kiela. Retrieval-augmented generation for knowledge-intensive NLP tasks. In Advances in Neural Information Processing Systems, volume 33, pages 9459–9474, 2020.

A. H. Liu et al. Ministral 3. arXiv preprint arXiv:2601.08584, 2026a.

Shuyi Liu, Yuming Shang, and Xi Zhang. Truthfulrag: Resolving factual-level conflicts in retrieval-augmented generation with knowledge graphs. In Proceedings of the AAAI Conference on Artificial Intelligence, 2026b.

Natawut Monaikul, Giuseppe Castellucci, Simone Filice, and Oleg Rokhlenko. Continual learning for named entity recognition. Proceedings of the AAAI Conference on Artificial Intelligence, 35(15):13570–13577, 2021.

Lawrence Page, Sergey Brin, Rajeev Motwani, and Terry Winograd. The PageRank citation ranking: Bringing order to the web. Stanford InfoLab Technical Report, 1999.

Shirui Pan, Linhao Luo, Yufei Wang, Chen Chen, Jiapu Wang, and Xindong Wu. Unifying large language models and knowledge graphs: A roadmap. IEEE Transactions on Knowledge and Data Engineering, 2024.

Ofir Press, Muru Zhang, Sewon Min, Ludwig Schmidt, Noah A Smith, and Mike Lewis. Measuring and narrowing the compositionality gap in language models. In Findings of the Association for Computational Linguistics: EMNLP 2023, 2023.

Qwen Team. Qwen3 technical report. arXiv preprint arXiv:2505.09388, 2025.

## B-ocr-0eb6934e14358a

B PDF page 3

- We develop EvoNER, a continually learnable entity recognizer that absorbs previously unseen semantic categories through lightweight incremental updates, enabling the system to recognize and organize emerging concepts without retraining the backbone LLM.
- We integrate provenance-preserving structured memory and hybrid retrieval into a full on-device pipeline, and demonstrate on real smartphones that this design yields strong end-to-end QA performance under strict device constraints.

## 2 Related work

On-device LLMs. Recent advances in quantization [Frantar et al., 2023] and efficient inference engines [Gerganov, 2023] have made it feasible to run billion-parameter models on mobile hardware [Xu et al., 2024]. Models such as Qwen3 [Qwen Team, 2025] and Llama 3 [Grattafiori et al., 2024] offer compact variants targeting edge deployment. However, these efforts focus on the inference engine and do not address the memory and continuous adaptation requirements of a personal assistant.

Retrieval-augmented generation. RAG [Lewis et al., 2020] augments LLMs with external knowledge at inference time. Dense passage retrieval [Karpukhin et al., 2020] provides the standard retrieval backbone. Self-RAG [Asai et al., 2024] internalizes retrieval behaviors through specialized training, and xRAG [Cheng et al., 2024] compresses retrieved context into compact representations. Graph-based approaches [Edge et al., 2024] organize retrieved knowledge into structured graphs for improved multi-hop reasoning. Multi-hop QA methods [Trivedi et al., 2023, Press et al., 2023] interleave retrieval with chain-of-thought reasoning. Most of these systems assume cloud-scale compute; our work targets their adaptation to strict on-device budgets.

Named entity recognition and continual learning. Span-based NER [Yu et al., 2020, Fu et al., 2021] formulates entity detection as span classification over enumerated candidates, avoiding the label dependency of sequential taggers. Continual learning for NER [Monaikul et al., 2021] addresses the challenge of absorbing new entity types without forgetting old ones, commonly using knowledge distillation [Hinton et al., 2015] or regularization [Kirkpatrick et al., 2017]. Our EvoNER combines span-based detection with a reserved-label classifier and teacher-distilled incremental updates, specifically designed for on-device expansion of the entity vocabulary.

Knowledge graphs for LLMs. The integration of knowledge graphs with LLMs [Ji et al., 2022, Pan et al., 2024] has attracted growing attention. LLM-driven KG construction [Edge et al., 2024] achieves high-quality extraction but requires large models. Our approach separates the extraction pipeline into a lightweight, trainable perception layer and a sparse LLM control plane, achieving predictable ingestion cost on mobile devices.

## 3 Method

### 3.1 Architecture overview

The SmartRAG architecture (Figure 1) consists of four interacting modules. The Perception module transforms unstructured text into structured knowledge via EvoNER (an on-device NER component, Section 3.2) and a lightweight relation classifier, producing entity–relation triplets. The Memory module organizes these triplets into MRGraph, a persistent knowledge structure that binds entities and relations to their source paragraphs for provenance (Section 3.3). At query time, the Focus module retrieves and ranks relevant evidence through a hybrid pipeline combining graph traversal, lexical matching, and dense semantic search (Section 3.4). The Thinking module invokes the on-device LLM only for high-value semantic operations: labeling emerging entity types, planning multi-hop retrieval, and synthesizing final answers (Section 3.5).

### 3.2 Perception: EvoNER and entity discovery

Span-based NER with character injection. We design EvoNER (Evolutionary Named Entity Recognition) to satisfy four on-device requirements: lightweight co-existence with the LLM, accurate entity boundary and type prediction, robustness to out-of-vocabulary surface forms, and support for

## B-ocr-2378415ccce858

B PDF page 11

![img-5.jpeg](img-5.jpeg)

Figure 4: Ablation results on NQ. We compare the full SmartRAG system with variants removing MRGraph, the Thinking planner, or the hybrid retrieval design. Token-F1 is reported as the primary downstream QA metric.

The retrieval–precision trade-off. Our analysis of the HotpotQA gap between SmartRAG and Naïve RAG reveals a fundamental trade-off in graph-structured retrieval. While graph traversal introduces relationships between nodes that enhance multi-hop reasoning, it also surfaces structurally related but contextually peripheral evidence. For open-ended questions where direct vector matching suffices, this can decrease recall. Intelligent search strategies that dynamically balance graph depth against retrieval precision represent a promising research direction.

Why not LLM-native extraction? Although a fully LLM-native extraction pipeline could reduce modular error accumulation and support richer predicate structures, our profiling shows that even query-time RAG prefilling can push TTFT to the minute scale on commodity smartphones. Making LLMs the primary writer of a continuously updated knowledge graph would introduce unacceptable latency and energy costs, and would require on-device training capabilities that remain impractical. The separation into a lightweight, trainable perception layer and a sparse LLM control plane yields predictable ingestion costs while retaining LLM expressivity where it matters most.

Limitations. (1) The current planner is heuristic and does not uniformly benefit all question types; learned planning strategies could address this. (2) On-device QA latency, while acceptable for the 1.7B backbone, is dominated by retrieval-conditioned prefilling and would benefit from evidence compression techniques. (3) Typed NER remains low in AI and Politics despite surface gains; improving type-consistent discovery and clustering is still a major lever, even when Token-F1 and Hit@1 already move in the right direction. (4) Our evaluation is limited to English-language benchmarks; multilingual adaptation remains future work.

Broader impact. SmartRAG enables privacy-preserving personal assistants that operate entirely on-device without sending user data to the cloud. While this is broadly positive for user privacy, we note that any system capable of building detailed personal knowledge graphs raises data governance concerns if the device is compromised. Appropriate encryption and access control mechanisms should complement the on-device architecture.

## Acknowledgments and Disclosure of Funding

Acknowledgments will be added in the camera-ready version.

## References

Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, and Hannaneh Hajishirzi. Self-RAG: Learning to retrieve, generate, and critique through self-reflection. In International Conference on Learning Representations, 2024.

Xin Cheng, Linzhe Luo, Hao Huang, Shuai Li, Daliang Wang, Yankai Lin, Zhiyuan Chen, and Maosong Sun. xRAG: Extreme context compression for retrieval-augmented generation with one token. In arXiv preprint arXiv:2405.13792, 2024.

Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven Truitt, and Jonathan Larson. From local to global: A graph RAG approach to query-focused summarization. In arXiv preprint arXiv:2404.16130, 2024.

## B-ocr-588dcaee7910d3

B PDF page 8

Table 1: Correctness (Cr, %) and F1 (%) on four QA benchmarks. SmartRAG uses a quantized Qwen3-1.7B backbone running entirely on-device. Models ≥8B are evaluated on A6000 as capacity references. Within each base-model block, the best result in each column is shown in bold and the second-best in underlined.

[tbl-0.html](tbl-0.html)

StableRAG mitigates permutation sensitivity by aggregating reasoning across multiple retrieval orders, and TruthfulRAG focuses on resolving factual conflicts through triple extraction, KG retrieval, and conflict-aware filtering. These are all meaningful objectives, but they place more burden on the generator's ability to denoise, aggregate, or filter evidence. Under the smaller Qwen3-1.7B regime, such additional reasoning or filtering stages may not pay off as reliably as direct flat retrieval, which helps explain why these baselines often underperform Naïve RAG there. Under Ministral3-3B, however, the stronger compact backbone appears better able to benefit from these extra mechanisms, so the same baselines become consistently stronger than Naïve RAG. SmartRAG differs in that it does not rely primarily on one-shot denoising or conflict filtering; instead, it combines persistent structured memory with hybrid retrieval, which appears to be more robust across both compact backbone families.

Compact backbones versus larger capacity references. The goal of SmartRAG is to improve what compact backbones can achieve under strict on-device constraints. Table 1 reflects this trade-off clearly. Larger standalone models still remain strongest on some direct factoid settings, most notably Qwen3-32B and Ministral3-14B on TriviaQA. At the same time, SmartRAG repeatedly matches or exceeds these larger LLM-only references on NQ, HotpotQA, and MultiHopQA. In conclusion, these results support the central claim of the paper: under device constraints, improving memory construction and evidence organization can be at least as important as increasing the parameter count alone.

### 4.3 On-device feasibility

A central question for SmartRAG is whether the entire pipeline remains usable when memory construction, retrieval, and answer generation are all executed on-device. To answer this, we profile two smartphone platforms with two different model sizes, and separately measure the end-to-end

[OCR table id=tbl-0.html; page=8]
<table><tr><td rowspan="2">Base Model</td><td rowspan="2">Method</td><td colspan="2">TriviaQA</td><td colspan="2">NQ</td><td colspan="2">HotpotQA</td><td colspan="2">MultiHopQA</td></tr><tr><td>Cr</td><td>F1</td><td>Cr</td><td>F1</td><td>Cr</td><td>F1</td><td>Cr</td><td>F1</td></tr><tr><td colspan="10">Qwen3</td></tr><tr><td colspan="10">LLM-only (no retrieval)</td></tr><tr><td></td><td>Qwen3-1.7B</td><td>22.10</td><td>21.52</td><td>9.10</td><td>10.17</td><td>14.15</td><td>13.00</td><td>22.00</td><td>19.18</td></tr><tr><td></td><td>Qwen3-4B</td><td>28.70</td><td>37.66</td><td>23.15</td><td>19.95</td><td>24.00</td><td>22.29</td><td>30.05</td><td>29.29</td></tr><tr><td></td><td>Qwen3-32B</td><td>51.45</td><td>42.26</td><td>40.15</td><td>35.92</td><td>33.25</td><td>30.56</td><td>31.54</td><td>32.69</td></tr><tr><td colspan="10">Retrieval-augmented (1.7B)</td></tr><tr><td></td><td>Naïve RAG</td><td>47.00</td><td>36.31</td><td>62.24</td><td>37.23</td><td>41.55</td><td>37.80</td><td>45.66</td><td>34.58</td></tr><tr><td></td><td>InstructRAG</td><td>43.15</td><td>22.67</td><td>41.30</td><td>34.99</td><td>33.90</td><td>26.15</td><td>13.90</td><td>12.94</td></tr><tr><td></td><td>StableRAG</td><td>45.16</td><td>21.89</td><td>17.30</td><td>11.14</td><td>41.15</td><td>26.11</td><td>5.05</td><td>0.75</td></tr><tr><td></td><td>TruthfulRAG</td><td>47.10</td><td>22.86</td><td>45.10</td><td>26.38</td><td>40.71</td><td>25.51</td><td>19.95</td><td>12.64</td></tr><tr><td></td><td>SmartRAG (ours)</td><td>50.00</td><td>48.68</td><td>66.68</td><td>54.84</td><td>63.93</td><td>51.27</td><td>50.17</td><td>41.86</td></tr><tr><td colspan="10">Ministral3</td></tr><tr><td colspan="10">LLM-only (no retrieval)</td></tr><tr><td></td><td>Ministral3-3B</td><td>35.84</td><td>28.27</td><td>24.43</td><td>18.81</td><td>16.98</td><td>19.19</td><td>17.33</td><td>26.56</td></tr><tr><td></td><td>Ministral3-14B</td><td>60.70</td><td>60.87</td><td>37.80</td><td>34.55</td><td>22.40</td><td>25.34</td><td>20.12</td><td>31.45</td></tr><tr><td colspan="10">Retrieval-augmented (3B)</td></tr><tr><td></td><td>Naïve RAG</td><td>41.71</td><td>33.02</td><td>42.99</td><td>32.02</td><td>36.96</td><td>27.08</td><td>15.95</td><td>14.81</td></tr><tr><td></td><td>InstructRAG</td><td>50.25</td><td>28.74</td><td>50.60</td><td>45.39</td><td>42.65</td><td>37.41</td><td>28.75</td><td>26.27</td></tr><tr><td></td><td>StableRAG</td><td>15.95</td><td>10.86</td><td>27.35</td><td>18.11</td><td>44.03</td><td>32.94</td><td>13.71</td><td>9.07</td></tr><tr><td></td><td>TruthfulRAG</td><td>47.86</td><td>25.52</td><td>53.00</td><td>31.31</td><td>47.86</td><td>35.38</td><td>43.20</td><td>33.67</td></tr><tr><td></td><td>SmartRAG (ours)</td><td>59.74</td><td>36.76</td><td>63.86</td><td>54.07</td><td>66.74</td><td>46.08</td><td>57.60</td><td>43.37</td></tr></table>

## B-ocr-77aa76de74890f

B PDF page 14

**Why these baselines were not deployed as real-phone end-to-end systems.** Our goal in the baseline comparison is to evaluate answer quality under a matched compact-backbone regime, rather than to claim that every baseline is equally suitable for direct mobile deployment. The original formulations of InstructRAG, StableRAG, and TruthfulRAG introduce additional stages that make them difficult to treat as drop-in phone pipelines. InstructRAG explicitly denoises retrieved contents through self-synthesized rationales and supports both in-context learning (ICL) and supervised fine-tuning (SFT). TruthfulRAG introduces additional KG-oriented processing steps, including knowledge-graph construction, graph retrieval, and entropy-based filtering. StableRAG emphasizes repeatability, frozen retrieval, and structured output normalization, with a pipeline that depends on OpenAI-style generation and embedding calls together with a persistent retrieval store. These original designs are meaningful in their intended settings, but they differ substantially from a single-pass compact on-device assistant stack. For this reason, we treat them as *reference RAG baselines evaluated under a matched backend and quantization setup*, rather than as directly deployable mobile systems.

**InstructRAG.** InstructRAG is a framework that explicitly denoises retrieved contents by generating rationales, and supports both in-context learning (ICL) and supervised fine-tuning (SFT). In our experiments, we implemented the method as described in the original paper, replacing the original serving stack with the same quantized compact backbones and llama.cpp backend used in our main experiments. We did not attempt to reproduce the original large-scale fine-tuning regime; instead, we adapted the method to the same compact-backbone comparison regime used for the other baselines. We therefore interpret the resulting numbers as measuring how well the *InstructRAG-style denoising strategy* transfers to compact quantized backbones under a unified inference setting, rather than as a claim about the maximum achievable performance of the original method.

**TruthfulRAG.** TruthfulRAG is a KG-based framework for resolving factual-level conflicts in RAG, whose pipeline includes knowledge-graph generation, graph retrieval, and entropy-based filtering before final response generation. In our evaluation, we preserved this overall conflict-aware graph-processing logic while replacing the original model-serving setup with the same compact quantized backbones and llama.cpp backend used elsewhere in the paper. Because TruthfulRAG contains additional graph-construction and filtering stages beyond a standard lightweight RAG loop, we did not deploy it as an end-to-end real-phone pipeline. Instead, we evaluate it in the same cloud-side simulation environment as the other RAG baselines. This makes the comparison more controlled at the backbone and inference level, while acknowledging that TruthfulRAG was originally designed for a somewhat different operating point than a strict mobile deployment target.

**StableRAG.** StableRAG is a method designed to improve repeatability and robustness in RAG systems, mitigating retrieval-permutation-induced hallucinations through stable retrieval ordering and structured rendering. In our experiments, we retained the stability-oriented evaluation logic described in the original paper while replacing the original serving configuration with the same compact quantized backbones and llama.cpp backend used in the rest of the paper. As with TruthfulRAG and InstructRAG, we treat the resulting system as a *simulated reference implementation under matched inference conditions*, not as a true smartphone deployment. This distinction is important because StableRAG is primarily designed to study response stability and retrieval repeatability, whereas SmartRAG is optimized for persistent structured memory and end-to-end on-device execution.

**Interpretation of the comparison.** We emphasize that these baselines are included as strong and relevant points of comparison, not as strawmen. InstructRAG targets denoising under noisy retrieval; TruthfulRAG targets factual conflict resolution with KG support; and StableRAG targets repeatability and robustness to retrieval variation. These are all reasonable objectives, and each may be better aligned than SmartRAG with other deployment scenarios. Our comparison should therefore be read narrowly: under a unified compact-backbone, quantized, llama.cpp-based setting, SmartRAG is more effective for the particular combination of goals studied in this paper—namely, persistent structured memory, repeated evidence composition, and end-to-end QA under edge-style resource constraints. We do not claim that the released original forms of these methods are inferior in general, nor that they were designed for the same deployment target as SmartRAG.

## B-ocr-828a5bbe429c4d

B PDF page 7

Answering. The LLM generates responses conditioned on retrieved evidence, constrained to structured schemas that favor extractive grounding to reduce hallucination.

## 4 Experiments

### 4.1 Setup

We use two compact LLM families in this work: Qwen3 [Qwen Team, 2025] and Ministral3 [Liu et al., 2026a]. Both are quantized to Q6_K via llama.cpp [Gerganov, 2023]. All offline one-time preparation, including quantization, LoRA training, and dataset pre-processing, is performed on a cloud server with two NVIDIA RTX A6000 GPUs, while the full online SmartRAG pipeline—memory ingestion, indexing, retrieval, and answer generation—runs entirely on-device. For multi-hop retrieval planning, we train a task-specific LoRA decomposer [Hu et al., 2022] on a self-constructed dataset derived from MultiHopQA and HotpotQA, where decomposition targets are generated offline using Claude Opus 4.6 and then filtered by rules with manual verification. The decomposer is used only to generate retrieval plans; final answers are always produced by the quantized backbone conditioned on retrieved evidence. All on-device experiments are conducted on two real smartphones: OnePlus 13 (Snapdragon 8 Elite, 16 GB RAM) and OnePlus 15 (Snapdragon 8 Elite Gen 5, 16 GB RAM).

We evaluate on four QA benchmarks: TriviaQA [Joshi et al., 2017], Natural Questions [Kwiatkowski et al., 2019], HotpotQA [Yang et al., 2018], and MultiHopQA [Ho et al., 2020]. Baselines are divided into two groups. For LLM-only comparison, we evaluate generation without retrieval using Qwen3-1.7B, Qwen3-4B, Qwen3-32B, Ministral3-3B, and Ministral3-14B. Among these, Qwen3-1.7B, Qwen3-4B, and Ministral3-3B represent the compact-model regime that is executable on-device, with 1.7B/3B corresponding to practically deployable scales and 4B serving as a larger but still runnable case. By contrast, Qwen3-32B and Ministral3-14B are treated as large-model capacity references, allowing us to contextualize how far SmartRAG extends the capability of compact backbones. For RAG, we evaluate Naïve RAG [Lewis et al., 2020], InstructRAG [Wei et al., 2024], StableRAG [Zhang et al., 2026], and TruthfulRAG [Liu et al., 2026b], instantiated with two lightweight backbones, Qwen3-1.7B and Ministral3-3B, to match the compact-model regime targeted in this work. These baselines are compared under the same inference budget and retrieval context constraints; additional details on their cloud-side simulation setting are provided in Section C.

We report two complementary metrics. Correctness (Cr) measures whether a prediction is factually correct with respect to the reference answer, using an LLM-as-judger protocol [Zheng et al., 2024] under a fixed rubric. Token-F1 measures token-level overlap between prediction and reference using a rule-based normalization and matching procedure. Together, these metrics capture both factual validity and surface-level answer overlap. Full evaluation details, including the judge prompt and the Token-F1 computation procedure, are provided in Section A.

### 4.2 Main results: structured memory improves small-backbone QA under on-device constraints

Table 1 compares SmartRAG against both LLM-only capacity references and lightweight retrieval baselines across the Qwen3 and Ministral3 families. Overall, SmartRAG delivers the clearest gains on NQ, HotpotQA, and MultiHopQA, while remaining competitive on TriviaQA. This pattern is consistent across both model families, suggesting that the main benefit of SmartRAG lies in structured evidence acquisition and composition.

SmartRAG is most effective on knowledge-intensive and evidence-composition benchmarks. Across both backbone families, the clearest gains of SmartRAG appear on NQ, HotpotQA, and MultiHopQA, where it consistently ranks at or near the top within each block. By contrast, TriviaQA is more mixed: SmartRAG remains competitive, but its advantage is less uniform than on the other three benchmarks. This pattern suggests that SmartRAG is especially effective when answering requires retrieving, organizing, and composing dispersed evidence, whereas direct open-domain factoid questions can often be handled well by larger parametric models or simpler retrieval strategies.

Comparison with RAG baselines. The baseline pattern also reflects the different objectives of the compared methods. InstructRAG explicitly learns denoising through self-synthesized rationales,

## B-ocr-84acfb4fd1287a

B PDF page 13

Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot, and Ashish Sabharwal. Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics, pages 10014–10037, 2023.

Joe H Ward. Hierarchical grouping to optimize an objective function. Journal of the American Statistical Association, 58(301):236–244, 1963.

Zhepei Wei, Wei-Lin Chen, and Yu Meng. Instructrag: Instructing retrieval-augmented generation via self-synthesized rationales. arXiv preprint arXiv:2406.13629, 2024.

Jiajun Xu et al. On-device language model: A comprehensive review. In arXiv preprint arXiv:2409.00088, 2024.

Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William W Cohen, Ruslan Salakhutdinov, and Christopher D Manning. HotpotQA: A dataset for diverse, explainable multi-hop question answering. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, pages 2369–2380, 2018.

Juntao Yu, Bernd Bohnet, and Massimo Poesio. Named entity recognition as dependency parsing. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 6470–6476, 2020.

Qianchi Zhang, Hainan Zhang, Liang Pang, Hongwei Zheng, and Zhiming Zheng. Stable-rag: Mitigating retrieval-permutation-induced hallucinations in retrieval-augmented generation. arXiv preprint arXiv:2601.02993, 2026.

Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P Xing, Hao Zhang, Joseph E Gonzalez, and Ion Stoica. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. In Advances in Neural Information Processing Systems, volume 36, 2024.

## A LLM-as-judger protocol

We assess factual correctness using an LLM-as-judger approach [Zheng et al., 2024]. Given a question, a reference answer (or set of acceptable answers), and the model's prediction, a judge LLM (Claude Haiku 4.5) determines whether the prediction is factually correct under a strict rubric. The judge outputs a binary correctness label per sample; we report the mean across all samples as Correctness (Cr, %). SQuAD-style F1 is computed as standard token-level precision-recall against reference answers. All models are evaluated under identical inference budgets: 4096 token context, top-K=8 retrieval cutoff, and Q6_K quantization.

## B Device specifications

Table 4: Evaluation device specifications.

[tbl-3.html](tbl-3.html)

## C Baseline implementation details and deployment notes

To make the comparison with prior RAG baselines as fair and transparent as possible, we implemented Naïve RAG, InstructRAG, StableRAG, and TruthfulRAG under a unified evaluation backend and quantization setting. In all cases, we used the same llama.cpp inference backend and the same model quantization scheme as in our main experiments, and instantiated the baselines with the same compact backbone families reported in Table 1. This appendix clarifies an important distinction: unlike SmartRAG, these baselines were not profiled as end-to-end real-phone deployments. Instead, they were executed in a cloud-side simulation environment designed to match the same inference backend, quantized models, and retrieval budget as closely as possible.

[OCR table id=tbl-3.html; page=13]
<table><tr><td></td><td>OnePlus 13</td><td>OnePlus 15</td></tr><tr><td>SoC</td><td>Snapdragon 8 Elite</td><td>Snapdragon 8 Elite Gen 5</td></tr><tr><td>RAM</td><td>16 GB LPDDR5X</td><td>16 GB LPDDR5X</td></tr><tr><td>Storage</td><td>256 GB UFS 4.0</td><td>256 GB UFS 4.0</td></tr><tr><td>OS</td><td>ColorOS 16</td><td>ColorOS 16</td></tr></table>

## B-ocr-97c1b1728a346c

B PDF page 2

Although on-device RAG has recently achieved preliminary progress, most existing methods remain centered on naive vector retrieval—that is, relying on semantic similarity between queries and document snippets to facilitate memory access. While this paradigm is well-suited for handling problems involving local matching, it struggles to address complex queries that require cross-segment evidence aggregation, entity linking, and multi-step reasoning. To address this limitation, on-cloud RAG research has begun to leverage graph structures to enhance the retrieval process, explicitly modeling the connections between entities, relations, and evidence to improve multi-hop question-answering capabilities. However, the majority of existing graph-based RAG methods are built upon powerful models, relying heavily on models with tens of billions of parameters to execute critical steps such as graph construction, summarization, and relation organization. While this premise may hold true in cloud-based environments, it clearly fails in on-device scenarios: on-device systems simply cannot bear the computational, latency, energy, and cost overheads associated with models of such scale.

Based on this issue, we believe that the key to on-device RAG lies not in directly compressing cloud-based graph RAGs onto the device, but in rethinking how structured memory should be built and utilized under resource-constrained conditions. In other words, graph construction capabilities do not necessarily stem from the generation capabilities of super-powerful models; they can also arise from more sophisticated system architecture design. By rationally dividing module responsibilities, controlling the granularity of knowledge organization, and designing incrementally evolving memory formation mechanisms, lightweight components can also gradually build a structured knowledge foundation that supports complex reasoning. Unlike traditional graph-based RAG methods, our approach emphasizes a systematic decoupling of knowledge extraction, memory organization, and reasoning support, allowing these processes to be collaboratively completed by multiple lightweight modules under on-device constraints. This provides an implementation path for on-device RAGs that differs from the cloud paradigm.

However, several key technical challenges remain to be addressed before this approach can be truly implemented on device. First, due to budget constraints related to system-memory, power consumption, and latency, only lightweight models are deployable on device. These models are insufficient in open environments to identify unknown entities, long-tail concepts, and new knowledge, making it difficult to directly construct high-quality structured knowledge like large cloud-based models. Therefore, the system must possess the ability to discover, aggregate, and continuously absorb unseen entities. Furthermore, complex queries often require entity association tracing and multi-step retrieval across multiple pieces of evidence. However, edge scenarios cannot rely on powerful models to repeatedly perform query decomposition, path planning, and graph exploration. This makes achieving structured focus for complex problems within a limited budget another core challenge. Finally, even after relevant evidence has been retrieved, lightweight generation models struggle to reliably complete reasoning within lengthy and noisy contexts. Therefore, a controlled evidence organization method is needed to confine the final generation to a compact and high-value context.

Based on this understanding, we propose **SmartRAG**, a structured RAG framework for on-device scenarios. Its core objective is to build external memory capable of supporting complex reasoning under lightweight models and limited resources. Unlike existing methods that rely on powerful models to directly complete graph construction and graph-based reasoning, SmartRAG decouples knowledge extraction, memory organization, retrieval focus, and answer generation through modular design, enabling these processes to operate collaboratively under edge-side constraints. Thus, SmartRAG transforms the structured knowledge capability from LLMs capability into a system architecture problem, providing a more practical implementation method for on-device RAGs.

Our contributions are as follows:

- We identify the core feasibility problem of on-device structured RAG: complex reasoning requires structured and updatable memory, but existing graph-construction pipelines depend too heavily on powerful LLMs to remain sustainable on edge devices.
- We present **SmartRAG**, an on-device structured RAG method that reallocates high-frequency memory writing to lightweight trainable components while reserving the LLM for sparse, high-value semantic operations.

## B-ocr-9f5146285c2007

B PDF page 10

![img-1.jpeg](img-1.jpeg)

![img-2.jpeg](img-2.jpeg)

Figure 2: Time to first token (TTFT) under configurations S0–S3. Left: QA TTFT. Right: question decomposition TTFT. Bars show median values and error bars indicate interquartile range.

![img-3.jpeg](img-3.jpeg)

![img-4.jpeg](img-4.jpeg)

Figure 3: Decoding speed under configurations S0–S3. Left: QA decoding speed. Right: question decomposition decoding speed. Bars show median values and error bars indicate interquartile range.

be interpreted as conservative end-to-end baselines for deployable on-device operation rather than absolute hardware limits.

### 4.4 Ablation study

Using MultiHopQA as the test set, we ablate three core components of SmartRAG: MRGraph (no_MRGraph), the LLM-based retrieval planner (no_THINKING_PLAN), and the hybrid retrieval design (no_Hybrid_Retrieval, i.e., graph-only retrieval). The results are shown in Figure 4.

Key findings. As shown in Figure 4, the full SmartRAG system achieves the best performance, with a Token-F1 of 0.5484. Removing MRGraph causes the largest degradation, dropping Token-F1 to 0.4151, which indicates that the structured memory module is the most important component for downstream multi-hop QA in this setting. Disabling the Thinking planner also reduces performance to 0.5069, suggesting that explicit multi-hop planning improves evidence acquisition even when the remaining retrieval and answering pipeline is preserved. Replacing hybrid retrieval with graph-only retrieval further lowers Token-F1 to 0.4749, showing that graph traversal alone is insufficient and that SmartRAG benefits from combining graph-based signals with complementary retrieval channels. Overall, the ablation results support the full SmartRAG design: structured memory, planning, and hybrid retrieval each make non-trivial contributions, and their combination yields the strongest end-to-end QA performance.

## 5 Discussion and conclusion

We have presented SmartRAG, an on-device architecture for adaptive question answering that decomposes intelligence into four coordinated functional roles. By shifting continuous adaptation to efficient structured computation and reserving LLM inference for high-value semantic operations, SmartRAG achieves multi-hop reasoning performance competitive with substantially larger cloud-based models while running entirely on commodity smartphones.

## B-ocr-c05c017a3b2aa0

B PDF page 6

### 3.3 Memory: MRGraph

MRGraph is a three-layer on-device knowledge graph designed for continual writes and efficient retrieval with explicit provenance.

Layer 1: Entity–paragraph graph. The paragraph is the atomic unit for both writing and retrieval. Each paragraph node stores raw content, an in-document index, a pointer to the source document, and an embedding vector. Entity nodes are deduplicated via stable name hashing and linked to paragraphs through association edges. Relations are stored as keyed edges with observation counts to prevent uncontrolled graph growth. Ingestion follows an evidence-first, structure-second principle: extracted triplets are first aligned to their best-matching paragraphs, then materialized as relation edges, ensuring every structured fact remains traceable.

Layer 2: Abstraction layer. Above entities, we maintain semantic clusters whose centroids are updated with smoothing as new entities arrive. An anchor–centroid drift metric detects and prevents topic drift. Cluster summaries are maintained incrementally during normal operation, with higher-quality refinement triggered during idle-and-charging periods.

Layer 3: Runtime raw-text view. At query time, retrieved paragraph evidence and the local graph neighborhood are assembled into a context bounded by a token budget, providing the Thinking module with both structured and unstructured evidence.

### 3.4 Focus: hybrid retrieval

At query time, the Thinking module decomposes the question into a retrieval plan $\mathcal{P} = (e_0, \{r_h, t_h\}_{h=1}^H)$, where $e_0$ is the seed entity, $H$ is the number of hops, and for each hop $h \in \{1, \ldots, H\}$, $r_h$ is a natural-language relation phrase (e.g., “published in”) and $t_h$ is the desired target entity type for that hop.

Stage 1: Plan-guided multi-hop text retrieval. For each hop, the system constructs local queries by combining the current center entity with the relation phrase, retrieves candidate paragraphs using fused lexical and dense similarity scores, and selects evidence under a token budget via maximal marginal relevance (MMR). Retrieved paragraphs are used to infer next-hop entity centers.

Stage 2: Graph-structured augmentation. Bridge entities from Stage 1 seed a graph traversal. For each node, we compare its concatenation with the query against abstraction-layer summaries, select top-ranked clusters, and perform top-down retrieval to expand the subgraph. Personalized PageRank [Page et al., 1999] estimates node importance, and connected subgraph blocks are assembled with supporting paragraphs.

Stage 3: Full-document fallback. If the first two stages provide insufficient evidence, global retrieval over documents provides a last-resort mechanism. Because on-device context length is limited, entities inevitably split across paragraphs; full-document fallback recovers these cross-boundary references.

Finally, retrieved evidence is post-processed: local context windows around entity mentions are extracted, sentence-level compression removes redundancy, and hash-based deduplication filters near-duplicates before packing the final context for the LLM.

### 3.5 Thinking: LLM-driven semantic operations

The on-device LLM is treated as a reusable semantic engine invoked only for operations requiring high-level language understanding, through four roles:

Labeling. For entity clusters that cannot be confidently typed, the LLM proposes new type names. Let $\mathcal{M}$ denote the multiset of mentions awaiting labels; cluster($\mathcal{M}$) groups them into clusters, and

$$\Delta\mathcal{T} = \text{LLM}(\text{cluster}(\mathcal{M})) \tag{10}$$

returns a set of new type strings $\Delta\mathcal{T}$ for coherent clusters. Semantically dispersed clusters are rejected to avoid polluting the type space.

Summarization. The knowledge graph is periodically clustered into communities, and the LLM produces summaries re-inserted as upper-layer paragraphs, forming a self-compressing memory loop.

Planning. Complex questions are decomposed into multi-hop retrieval plans before evidence acquisition, reducing search ambiguity under strict on-device budgets.

## B-ocr-cf29735c24ed0c

B PDF page 9

Table 2: Device-backbone combinations for on-device profiling. Each pair is denoted S0–S3.

[tbl-1.html](tbl-1.html)

Table 3: Average PSS memory and power consumption across device-backbone configurations. S0–S3 follow the mapping in Table 2.

[tbl-2.html](tbl-2.html)

RAG pipeline. Table 2 defines shorthand labels S0–S3 for each hardware–backbone pair, which are used throughout this section.

In general, the measurements reveal a clear usability boundary. While both backbones can be executed on-device, the 1.7B model remains in the practically deployable regime, whereas the 4B model substantially weakens interactivity once the full retrieval-augmented pipeline is taken into account.

We first examine resource usage during triplet extraction and QA. As summarized in Table 3, the 4B backbone consistently incurs a substantially heavier memory footprint than 1.7B on both devices. This gap appears in both triplet extraction and end-to-end QA, where the 1.7B settings remain around the 4–5.5 GB range while the 4B settings rise to roughly 6.5–6.8 GB. This difference matters because SmartRAG runs as a full on-device pipeline, with model weights, retrieval-conditioned prefilling, and runtime memory operations sharing the same limited mobile memory budget.

More broadly, the measured power remains relatively low because we intentionally adopt a conservative system configuration: we prioritize stable long-term execution so that SmartRAG can remain deployable as a persistent on-device system. This choice leaves some hardware capacity unused, which in turn contributes to the non-trivial TTFT observed in the full QA setting.

The more decisive separation appears in latency, shown in Figure 2. Question decomposition remains comparatively light-weight across all settings. For the S0 configuration (Snapdragon 8 Elite Gen 5 with Qwen3-1.7B), the median decomposition TTFT is 1.32 s, which confirms that this planning stage remains near the low-second regime. By contrast, full QA is much more expensive because the model must absorb retrieved evidence before decoding the answer. Under the same S0 setting, the median QA TTFT rises to 36.9 s, indicating that the dominant latency cost comes from retrieval-conditioned prefilling rather than from the decomposition step itself. The 4B settings (S1 and S3) are visibly slower in Figure 2, moving further away from an interactive operating point.

The same conclusion is reinforced by the generation stage in Figure 3. In the S0 runlog, the median decoding time is 8.11 s for question decomposition and 8.55 s for QA, while the mean QA decoding time is higher (14.81 s) because answer lengths vary substantially across samples. This pattern again suggests that the main systems bottleneck is not the decomposition step itself, nor even decoding alone, but the long prefilling stage required by retrieval-conditioned QA. More broadly, Figure 3 shows the same qualitative ordering across devices and backbone sizes: the 1.7B backbone decodes faster than 4B, and the smaller configurations remain more favorable for end-to-end deployment.

The memory, TTFT, and decoding measurements explain why we standardize on the 1.7B backbone in the main accuracy experiments. Although the 4B model is technically executable on smartphones, its larger memory footprint, much longer retrieval-conditioned prefilling time, and slower generation place it beyond a practically interactive regime for end-to-end on-device RAG. We also note that system software still matters: even under closely related Snapdragon-class hardware, OS scheduling and runtime policies can noticeably affect realized throughput. The reported numbers should therefore

[OCR table id=tbl-1.html; page=9]
<table><tr><td></td><td>Qwen3-1.7B</td><td>Qwen3-4B</td></tr><tr><td>OnePlus 15 (Snapdragon 8 Elite Gen 5, 16 GB)</td><td>S0</td><td>S1</td></tr><tr><td>OnePlus 13 (Snapdragon 8 Elite, 16 GB)</td><td>S2</td><td>S3</td></tr></table>

[OCR table id=tbl-2.html; page=9]
<table><tr><td rowspan="2">Config</td><td colspan="2">Triplet Extraction</td><td colspan="2">QA</td></tr><tr><td>PSS Memory (MB)</td><td>Power (W)</td><td>PSS Memory (MB)</td><td>Power (W)</td></tr><tr><td>S0</td><td>5527.31</td><td>4.74</td><td>4149.72</td><td>2.85</td></tr><tr><td>S1</td><td>6717.55</td><td>4.77</td><td>6803.68</td><td>5.36</td></tr><tr><td>S2</td><td>5099.07</td><td>2.93</td><td>4153.38</td><td>2.12</td></tr><tr><td>S3</td><td>6643.01</td><td>2.37</td><td>6512.62</td><td>2.12</td></tr></table>

## B-ocr-d27efd32deb918

B PDF page 1

arXiv:2607.14661v2 [cs.AI] 18 Jul 2026

# SmartRAG: Native Graph-Based RAG for Mobile Device

Zhihan Jiang \( ^{1} \) , Meng Li \( ^{1} \) , Shenghao Liu \( ^{2} \) , Keran Li \( ^{1} \) , Ruiben Zhou \( ^{1} \)

Wei Wang \( ^{1} \) , Xianjun Deng \( ^{2} \) , Shuai Wang \( ^{3} \) , Haipeng Dai \( ^{1} \)

\( ^{1} \) Nanjing University  \( ^{2} \) HUST  \( ^{3} \) Southeast University

zhihan_jiang@smail.nju.edu.cn, meng@nju.edu.cn

## Abstract

Deploying large language models (LLMs) as personal assistants on mobile devices demands privacy, low latency, and offline availability, yet the computational cost of giant models clashes with strict edge-hardware budgets. We argue that this tension cannot be resolved by model compression alone; it requires decomposing on-device intelligence into complementary functional roles. We present SmartRAG, a fully on-device framework that organizes an intelligent assistant around four coordinated modules—Perception, Memory, Focus, and Thinking. At the core of SmartRAG is EvoNER, a continually learnable named-entity recognizer that incrementally expands its label inventory through teacher-distilled updates, enabling the system to absorb previously unseen entity types without retraining the backbone LLM. Extracted knowledge is stored in MRGraph, a three-layer provenance-preserving knowledge graph, and retrieved at query time through a hybrid pipeline combining graph traversal, lexical matching, and dense semantic search. The on-device LLM is invoked only for high-value semantic operations—labeling, planning, and answer synthesis—keeping inference costs bounded. Experiments on four QA benchmarks (TriviaQA, Natural Questions, HotpotQA, MultiHopQA) show that SmartRAG with a quantized 1.7B-parameter backbone achieves multi-hop reasoning performance competitive with models up to  \( 18\times \)  larger, while running entirely on commodity smartphones within practical memory and latency envelopes.

## 1 Introduction

In recent years, as the application of large language models (LLMs) in real-world interactive tasks continues to deepen, memory is gradually emerging as a critical capability in LLM system determining whether the system can support long-term personalization, continuous knowledge updates, and contextually consistent reasoning. This issue is of particular significance for on-device scenarios, as the core value of such deployments lies precisely in data locality, privacy protection, and personalized services capabilities that inherently require the system to establish and maintain a local memory built around the user's private data, device-local content, and environmental context. Given the strict constraints on system-memory (i.e., RAM usage and runtime memory footprint on edge devices), power consumption, and latency budgets inherent to devices, heavyweight LLMs are difficult to deploy directly; furthermore, relying solely on the limited parametric memory of lightweight models often proves insufficient to support continuous updates, user customization, and knowledge-intensive reasoning. Retrieval-Augmented Generation (RAG) addresses this challenge by integrating LLMs with external, non-parametric memory, thereby providing a memory mechanism that is updatable, structured, and more easily personalized; consequently, it is widely regarded as a highly promising solution.

## B-ocr-f434991128744c

B PDF page 4

![img-0.jpeg](img-0.jpeg)

Figure 1: Overview of the SmartRAG architecture. Incoming text flows through Perception (EvoNER + relation extraction) into Memory (MRGraph), which is queried by Focus (hybrid retrieval) and consumed by Thinking (LLM-driven planning and answer generation). Dashed arrows indicate asynchronous background processes (clustering, incremental training).

continual label expansion. Given an input sentence, we encode it into sub-word representations and enumerate candidate spans from word-start positions up to a maximum width W:

$$r = (i, j), \quad 1 \leq i \leq j \leq n, \quad (j - i + 1) \leq W, \tag{1}$$

where r denotes a candidate span, i and j are its inclusive word-level start and end indices, n is the sentence length in words, and W caps span width (W=10 in our implementation), yielding O(nW) candidates instead of all O(n^2) spans. To improve robustness to misspellings and rare surface forms, we augment the contextual representation with a character-level feature injected at the first subword of each word:

$$\mathbf{h}_t = [\mathbf{e}_t; m_t \cdot \mathbf{c}(t)], \tag{2}$$

where h_t is the final representation at subword position t, e_t is the Transformer contextual embedding at t, m_t \in \{0, 1\} is 1 on the first subword of a word and 0 otherwise, c(t) is the character-level embedding aligned with that word, and [;] denotes concatenation. Each candidate span is represented using boundary features, element-wise interaction, and a learned width embedding, then passed to a classifier.

**Reserved-label mechanism for continual expansion.** A key requirement for continual on-device learning is adding new entity types without reinitializing the classifier. We pre-allocate a fixed label capacity and partition the span classifier into a base head (no-entity label plus deployed entity types) and reserved rows for future types. For span (i, j) with pooled representation z_{ij} \in \mathbb{R}^d, logits

## B-ocr-fe38f3ef67bd80

B PDF page 5

decompose as

$$\left[ \begin{array} { l } { \ell _ { i j } ^ { \mathrm { b a s e } } } \\ { \ell _ { i j } ^ { \mathrm { r e s v } } } \end{array} \right] = \left[ \begin{array} { l } { \mathbf { W } _ { \mathrm { b a s e } } } \\ { \mathbf { W } _ { \mathrm { r e s v } } } \end{array} \right] \mathbf { z } _ { i j } + \left[ \begin{array} { l } { \mathbf { b } _ { \mathrm { b a s e } } } \\ { \mathbf { b } _ { \mathrm { r e s v } } } \end{array} \right] , \qquad \ell _ { i j } = [ \ell _ { i j } ^ { \mathrm { b a s e } } ; \ell _ { i j } ^ { \mathrm { r e s v } } ] ,$$

where $\mathbf{W}_{\mathrm{base}}$, $\mathbf{b}_{\mathrm{base}}$ (resp. $\mathbf{W}_{\mathrm{resv}}$, $\mathbf{b}_{\mathrm{resv}}$) are base (resp. reserved) weights and biases. Reserved slots are initialized inactive ($\mathbf{b}_{\mathrm{resv}} \ll 0$, $\mathbf{W}_{\mathrm{resv}} \approx \mathbf{0}$). When new types are discovered, each is mapped to an unused reserved row without changing output dimensionality.

**Incremental learning with teacher distillation.** When new entity types emerge, EvoNER must incorporate the supervision without degrading performance on existing types. We pair the reserved-label design with teacher-guided distillation on the base-label subspace only. Let $\Omega(x)$ be the set of candidate spans in sentence $x$. The task loss matches offline training:

$$\mathcal { L } _ { \mathrm { t a s k } } = \mathcal { L } _ { \mathrm { s p a n } } + \textstyle { \frac { 1 } { 2 } } \left( \mathcal { L } _ { \mathrm { s t a r t } } + \mathcal { L } _ { \mathrm { e n d } } \right) ,$$

where $\mathcal{L}_{\mathrm{span}}$ is masked span classification over candidates and $\mathcal{L}_{\mathrm{start}}$, $\mathcal{L}_{\mathrm{end}}$ are auxiliary boundary losses on mention endpoints. The full incremental objective is

$$\mathcal { L } _ { \mathrm { i n c } } = \mathcal { L } _ { \mathrm { t a s k } } + \lambda _ { \mathrm { K D } } \mathcal { L } _ { \mathrm { K D } } ,$$

with $\lambda_{\mathrm{KD}}$ trading stability against plasticity. For each span $r \in \Omega(x)$, let $\ell_r^{T,\mathrm{base}}$, $\ell_r^{S,\mathrm{base}} \in \mathbb{R}^{1+n_{\mathrm{base}}}$ denote teacher and student logits restricted to the base subspace, where $n_{\mathrm{base}}$ is the number of deployed base entity types (the leading dimension accounts for the no-entity logit). With temperature $T_{\mathrm{kd}}$ and confidence threshold $\tau$, define the gate

$$m _ { r } = \mathbb { I } \left[ \operatorname* { m a x } _ { 1 \leq k \leq 1 + n _ { \mathrm { b a s e } } } \left[ \operatorname { s o f t m a x } \left( \ell _ { r } ^ { T , \mathrm { b a s e } } / T _ { \mathrm { k d } } \right) \right] _ { k } \geq \tau \right] ,$$

i.e., the gate is on when the teacher's peak probability on base classes exceeds $\tau$. The distillation loss is

$$\mathcal { L } _ { \mathrm { K D } } = \frac { T _ { \mathrm { k d } } ^ { 2 } } { \sum _ { r \in \Omega ( x ) } m _ { r } + \epsilon } \sum _ { r \in \Omega ( x ) } m _ { r } \operatorname { K L } \left( \operatorname { s o f t m a x } \left( \ell _ { r } ^ { T , \mathrm { b a s e } } / T _ { \mathrm { k d } } \right) \parallel \operatorname { s o f t m a x } \left( \ell _ { r } ^ { S , \mathrm { b a s e } } / T _ { \mathrm { k d } } \right) \right) ,$$

where $\epsilon$ avoids division by zero. Reserved logits are not distilled, so new types remain plastic while the teacher anchors old boundaries. The teacher is frozen for an entire incremental round, then the updated student may become the next teacher.

**Three-stage parameter-efficient updates.** To accommodate the unpredictability of mobile scheduling, we adopt a three-stage optimization schedule with progressively increasing trainable capacity. Let $\Theta$ denote all parameters, $\Theta_{\mathrm{head}}$ non-encoder parameters (heads and adapters), and $\Theta_{\mathrm{top}K}$ the top-$K$ Transformer blocks (counted from the output side):

$$\Theta _ { 1 } = \Theta _ { \mathrm { h e a d } } , \quad \Theta _ { 2 } = \Theta _ { \mathrm { h e a d } } \cup \Theta _ { \mathrm { t o p } K } , \quad \Theta _ { 3 } = \Theta .$$

Stage 1 adapts only heads; Stage 2 adds partial encoder layers; Stage 3 allows brief full-model consolidation at a low learning rate. Training may stop after any stage if the device budget is exhausted.

**Triplet discovery.** Extracted entities are initially categorized into coarse types. For unseen entities, we extract stable semantic vectors via a frozen lightweight embedder and store them in a local vector database. When the count exceeds a threshold, agglomerative clustering with Ward linkage [Ward, 1963] groups semantically similar mentions. For clusters $A, B$ with sizes $|A|, |B|$ and embedding centroids $\mu_A, \mu_B$,

$$d ( A , B ) = { \frac { | A | \cdot | B | } { | A | + | B | } } \left\| \pmb { \mu } _ { A } - \pmb { \mu } _ { B } \right\| _ { 2 } ^ { 2 } .$$

Given threshold $\epsilon > 0$, we iteratively merge clusters: whenever some pair $(A, B)$ satisfies $d(A, B) < \epsilon$, merge them; stop when no such pair remains (all surviving clusters are pairwise at least $\epsilon$-separated under $d$). The Thinking module then assigns category labels to large coherent clusters. For known-type entities, a lightweight relation classifier identifies relations, producing triplets written into MRGraph.
