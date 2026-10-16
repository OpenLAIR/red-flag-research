# Assessment of Generative Named Entity Recognition in the Era of Large Language Models

## B-10004f43b1df3c

https://arxiv.org/html/2601.17898v1#chars-42567-44833

### A.2 Task Descriptions for Different Output Formats

We designed five distinct task descriptions corresponding to the output formats. These descriptions explicitly constrain the generation behavior of the LLMs. Table [9](#A1.T9 "Table 9 ‣ A.2 Task Descriptions for Different Output Formats ‣ Appendix A Full Instructions for Different Datasets ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models") details the specific prompt templates used for each format.

|  |  |
| --- | --- |
| Output Format | Task Description |
| Inline Bracketed | Your task is to identify all named entities in the input sentence and rewrite the sentence by enclosing each entity using the format [Entity Text | LABEL]. Use only the label tags defined in the Label Set below. |
| Inline XML | Your task is to identify all named entities in the input sentence and rewrite the sentence by enclosing each entity using the format <LABEL>Entity Text</LABEL>. Use only the label tags defined in the Label Set below. |
| Category-grouped JSON | Your task is to identify all named entities in the input sentence and extract them into a JSON object grouped by label. The keys of the JSON object should be the label tags defined in the Label Set below, and the values should be lists of extracted entities. If a label has no corresponding entities, use an empty list. |
| Occurrence-based JSON | Your task is to identify all named entities in the input sentence and extract them into a JSON list. Output a JSON list where each object contains: 1. “text”: the entity string. 2. “label”: the label tags defined in the Label Set below. 3. “occurrence\_index”: a 1-based integer indicating the order of appearance of this text in the sentence (e.g., 1 for the first appearance, 2 for the second). If no entities are found, return an empty list. |
| Offset-based JSON | Your task is to identify all named entities in the input sentence and extract them with precise character offsets. Output a JSON list where each object contains: 1. “text”: the entity string. 2. “label”: the label tags defined in the Label Set below. 3. “start”: the 0-based index of the entity’s first character. 4. “end”: the 0-based index of the first character after the entity(exclusive). |

## B-103be5ca218442

https://arxiv.org/html/2601.17898v1#chars-48793-54113

## Appendix D AI Assistance Statement

We utilized LLMs (e.g., ChatGPT) to assist in polishing the text, refining grammar, and improving the clarity of the manuscript. All content was reviewed and verified by the authors.

As detailed in Appendix [A.3](#A1.SS3 "A.3 Label Definition Schema ‣ Appendix A Full Instructions for Different Datasets ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models"), we employed LLMs to summarize official annotation guidelines for CoNLL2003 dataset and generate standard biomedical definitions for GENIA dataset to construct the label definition schema used in our instruction tuning prompts.

|  |  |
| --- | --- |
| Labels | Definition |
| ORG | A collective entity such as a company, institution, brand, political or governmental body, publication, or any organized group of people acting as a unit. |
| PER | A named individual, including humans, animals, fictional characters, and their aliases. |
| LOC | A geographical or spatial entity, including natural features, built structures, regions, public or commercial places, assorted buildings, and abstract or metaphorical places. |
| MISC | Named entities that are not persons, organizations, or locations, including derived adjectives, religions, ideologies, nationalities, languages, events, programs, wars, titles of works, slogans, eras, and types of objects. |

|  |  |
| --- | --- |
| Labels | Definition |
| PERSON | People, including fictional. |
| NORP | Nationalities or religious or political groups. |
| FAC | Buildings, airports, highways, bridges, etc.. |
| ORG | Companies, agencies, institutions, etc.. |
| GPE | Countries, cities, states. |
| LOC | Non-GPE locations, mountain ranges, bodies of water. |
| PRODUCT | Vehicles, weapons, foods, etc. (Not services). |
| EVENT | Named hurricanes, battles, wars, sports events, etc.. |
| WORK\_OF\_ART | Titles of books, songs, etc.. |
| LAW | Named documents made into laws. |
| LANGUAGE | Any named language. |
| DATE | Absolute or relative dates or periods. |
| TIME | Times smaller than a day. |
| PERCENT | Percentage (including “%”). |
| MONEY | Monetary values, including unit. |
| QUANTITY | Measurements, as of weight or distance. |
| ORDINAL | “first”, “second”. |
| CARDINAL | Numerals that do not fall under another type. |

|  |  |
| --- | --- |
| Labels | Definition |
| DNA | Deoxyribonucleic acid sequences or molecules, including genes, gene fragments, promoters, enhancers, and other genomic regions that encode or regulate biological information. |
| RNA | Ribonucleic acid molecules transcribed from DNA, encompassing messenger RNA, non-coding RNAs, and RNA transcripts involved in gene expression and regulation. |
| Protein | Functional biological macromolecules composed of amino acids, including enzymes, receptors, transcription factors, and protein complexes produced by translation of RNA. |
| Cell\_line | A population of cells derived from a single source and maintained in vitro through continuous culture, often genetically stable and used for experimental research. |
| Cell\_type | A class of cells defined by shared morphological, functional, and molecular characteristics within an organism, such as immune cells, epithelial cells, or neurons. |

|  |  |
| --- | --- |
| Labels | Definition |
| PER | Person entities are limited to humans. A person may be a single individual or a group. |
| ORG | Organization entities are limited to corporations, agencies, and other groups of people defined by an established organizational structure. |
| GPE | GPE entities are geographical regions defined by political and/or social groups. A GPE entity subsumes and does not distinguish between a nation, its region, its government, or its people. |
| LOC | Location entities are limited to geographical entities such as geographical areas and landmasses, bodies of water, and geological formations. |
| FAC | Facility entities are limited to buildings and other permanent man-made structures and real estate improvements. |
| VEH | A vehicle entity is a physical device primarily designed to move an object from one location to another, by (for example) carrying, pulling, or pushing the transported object. Vehicle entities may or may not have their own power source. |
| WEA | Weapon entities are limited to physical devices primarily used as instruments for physically harming or destroying other entities. |

![[LOGO]](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)

## B-1240d80747a8b0

https://arxiv.org/html/2601.17898v1#chars-0-209

##### Report GitHub Issue

Content selection saved. Describe the issue below:

![](/static/base/1.0.1/images/icons/smileybones-small.svg)
![arXiv logo](/static/base/1.0.1/images/arxiv-logo-primary-light.svg)

## B-1d80478aed47c6

https://arxiv.org/html/2601.17898v1#chars-46325-47786

## Appendix B Brief Introduction of Baselines

BERT-Tagger [Devlin et al. (2019)](#bib.bib4) uses BERT model and train classification heads for tagging tokens. GNN-SL [Wang et al. (2023)](#bib.bib18) augments sequence labeling by retrieving nearest neighbor examples and modeling their interactions with the input via GNNs. ACE + Fine-tune [Wang et al. (2021)](#bib.bib19) utilizes a reinforcement learning controller to automatically search for the optimal concatenation of various pre-trained embeddings. For a fair comparison, we adopt its sentence-level variant, achieving SOTA performance on the CoNLL2003 dataset. BERT-MRC+DSC [Li et al. (2020b)](#bib.bib38) addresses data imbalance via Dice loss, achieving SOTA performance on the OntoNotes5.0 dataset. BERT-MRC [Li et al. (2020a)](#bib.bib7) formulates NER as a machine reading comprehension task, achieving SOTA performance on the GENIA dataset. BINDER [Zhang et al. (2023)](#bib.bib21) aligns spans and types in a shared space via a bi-encoder and contrastive learning, distinguishing entities with dynamic thresholding. W2NER [Li et al. (2022)](#bib.bib25) unifies flat, nested, and discontinuous NER by modeling word-word relations on a 2D grid to capture token interactions. Biaffine+CNN [Yan et al. (2023)](#bib.bib24) treats the span feature grid generated by a biaffine decoder as an image, utilizing CNNs to model spatial correlations between neighboring spans for nested entity recognition.

## B-2d3f7a3267b1ec

https://arxiv.org/html/2601.17898v1#chars-41686-41701

## References

## B-2d6981c197cee1

https://arxiv.org/html/2601.17898v1#chars-38471-40183

## 6 Preservation of General Capability

While traditional pre-trained models become single-purpose specialists after task-specific fine-tuning, LLMs retain their inherent multi-task capabilities as general generative models. To examine the impact of generative NER fine-tuning on these general capabilities, we conduct an evaluation across a range of tasks, including reading comprehension (DROP; [Dua et al., 2019](#bib.bib41)), commonsense reasoning (HellaSwag; [Zellers et al., 2019](#bib.bib40)), multitask language understanding (MMLU; [Hendrycks et al., 2021](#bib.bib43)), mathematical reasoning (GSM8K; [Cobbe et al., 2021](#bib.bib39)), and truthfulness (TruthfulQA; [Lin et al., 2022](#bib.bib42)). We use the lm-evaluation-harness framework [Gao et al. (2024)](#bib.bib44) for comparison.

The results are shown in Table [8](#S5.T8 "Table 8 ‣ 5 Error Analysis ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models"). We find that the fine-tuned LLMs performed comparably to the original model across most of the tasks, with only minor fluctuations ranging from a 4.33% decrease to a 3.04% increase. Notably, on the reading comprehension benchmark DROP, the fine-tuned model achieves a substantial performance gain of 25.50 to 45.32 F1 scores. The improvement could be attributed to the fact that DROP answers are often text spans containing named entities (e.g., persons, locations, organizations). Fine-tuning for NER strengthens the model’s ability to detect these entities, leading to more precise answer extraction. Overall, the results suggest that the core capabilities of LLMs remain largely intact after undergoing lightweight fine-tuning for the NER task.

## B-34a55ddb725fc9

https://arxiv.org/html/2601.17898v1#chars-40183-40810

## 7 Conclusion

We present a comprehensive assessment of generative NER using open-source LLMs. Our experiments show that LLMs, when fine-tuned with parameter-efficient methods and appropriate output formats, can match or even exceed the performance of strong traditional NER models, while maintaining robust multi-task capabilities. Furthermore, we find that LLMs keep genuine learning on NER task instead of memorizing entity-label correlations. These confirm the viability of generative NER as a flexible and effective paradigm, highlighting its potential to gradually supplement traditional sequence labeling approaches.

## B-397262305f5f05

https://arxiv.org/html/2601.17898v1#chars-1636-8790

## 1 Introduction

Named entity recognition (NER) is a fundamental task in natural language processing, widely used in downstream applications such as relation extraction, knowledge graph construction, information retrieval, and question answering systems. As a typical sequence labeling task, approaches based on traditional auto-encoding pre-trained models have achieved strong results [Devlin et al. (2019)](#bib.bib4); [Li et al. (2020a)](#bib.bib7); [Lu et al. (2022)](#bib.bib28); [Yan et al. (2023)](#bib.bib24).

![Refer to caption](2601.17898v1/intro.png)

The development of generative pre-trained models [Radford et al. (2019)](#bib.bib36); [Lewis et al. (2020)](#bib.bib5) and large language models (LLMs; [Brown et al., 2020](#bib.bib29); [OpenAI, 2022](#bib.bib31); [OpenAI, 2023](#bib.bib30); [DeepSeek-AI, 2024](#bib.bib32)) is gradually shifting traditional NER task toward a unified generative paradigm. As shown in Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models"), LLMs sequentially generate user-provided sentences along with their corresponding entity labels in textual form. This approach demonstrates strong interactivity, generalization, and user-friendliness. Recent studies have conducted preliminary investigations into NER based on LLMs by crafting specific prompts [Xie et al. (2023)](#bib.bib2); [Wei et al. (2023)](#bib.bib9); [Kim et al. (2024)](#bib.bib8); [Wang et al. (2025a)](#bib.bib1), also achieving promising results.

In this work, we aim to further explore the following research questions: In terms of performance, is generative NER with open-source LLMs a reliable approach compared with advanced pre-trained NER models? Most of the aforementioned studies test the performance of closed-source models like ChatGPT [OpenAI (2022)](#bib.bib31) for zero-shot NER, and there is currently a lack of systematic investigation into the effectiveness of fine-tuned open-source LLMs, such as advanced LLaMA [Grattafiori et al. (2024)](#bib.bib16) and Qwen [Yang et al. (2025)](#bib.bib17) models. Specifically, we seek to examine whether generative LLMs represent a reliable approach and whether there is a performance gap compared to traditional pre-trained model methods on both flat and nested NER tasks.

How do different output formats affect the performance of LLMs in generative NER? The performance of LLMs is highly sensitive to the specific instructions given by users. While recent studies have touched upon format designs [Kim et al. (2024)](#bib.bib8); [Lv et al. (2025)](#bib.bib45), we systematically explore a more diverse set of output templates as a supplement to the aforementioned work and investigate their specific impact on NER performance. Specifically, we design five distinct output formats (Inline Bracketed, Inline XML, Category-grouped JSON, Occurrence-based JSON, and Offset-based JSON) to compare their impact and investigate whether the performance of different models remains consistent across these various formats.

Do LLMs rely on memorization of entity labels to solve NER tasks? Named entities are prevalent in corpora and are incorporated into the training process of LLMs. Moreover, studies indicate that portions of certain datasets have been leaked during LLMs training, casting doubt on the reliability of evaluation results [Sainz et al. (2023)](#bib.bib34); [Dong et al. (2024)](#bib.bib35); [Balloccu et al. (2024)](#bib.bib33). Therefore, we aim to investigate whether the generative NER capability of LLMs stems merely from memorizing entity-label mappings, rather than from genuinely learning the features of entities and accurately identifying and labeling them.

Do LLMs preserve the original capabilities after instruction tuning for NER? One advantage of LLMs is their strong generalization capability, which enables them to perform well across a wide range of tasks. We investigate whether the original abilities of LLMs are affected after instruction tuning on NER tasks. To this end, we compare the performance of the LLM before and after fine-tuning on multiple datasets, including HellaSwag [Zellers et al. (2019)](#bib.bib40), DROP [Dua et al. (2019)](#bib.bib41), GSM8K [Cobbe et al. (2021)](#bib.bib39), MMLU [Hendrycks et al. (2021)](#bib.bib43), and TruthfulQA [Lin et al. (2022)](#bib.bib42).

In this study, we conduct experiments using eight LLMs with varying sizes and
versions of LLaMA [Grattafiori et al. (2024)](#bib.bib16) and Qwen [Yang et al. (2025)](#bib.bib17) across four standard datasets, including two flat NER datasets CoNLL2003 [Tjong Kim Sang and De Meulder (2003)](#bib.bib14) and OntoNotes5.0 [Pradhan et al. (2013)](#bib.bib20), and two nested NER datasets ACE2005 [Walker et al. (2006)](#bib.bib37) and GENIA [Kim et al. (2003)](#bib.bib15). Empirically, the answers for the above questions are as follows:

1) With parameter-efficient fine-tuning and structured output formats like inline bracketed or inline XML, LLMs match the performance of traditional encoder-based NER models and exceed that of closed-source LLMs like GPT-3. They excel particularly in flat NER within general domains, though further progress is needed for nested NER in domains like biomedicine.

2) The strong performance of LLMs in generative NER tasks stems primarily from their powerful instruction-following and text generation capabilities, rather than from merely memorizing entity-label correlations from training corpora. Error analysis indicates that LLMs tend to generate wrong types, which stems from a misalignment between the rich intrinsic knowledge and the detailed annotation guidelines of datasets.

3) LLMs can retain most of their original capabilities under parameter-efficient fine-tuning for NER tasks, with performance on tasks staying stable or slightly decreasing while improving significantly on benchmarks like DROP. Considering their user-friendly natural language interface, which lowers the barrier for non-experts, generative NER systems hold the potential to gradually supplant traditional sequence labeling based NER models.

|  |  |
| --- | --- |
| Types | Examples of Labeled Output |
| Inline Bracketed | This is the first demonstration of a specific interaction with [PU.1 | Protein] |
| on a [myeloid [PU.1 | Protein] binding site | DNA]. |
| Inline XML | This is the first demonstration of a specific interaction with <Protein>PU.1</Protein> |
| on a <DNA>myeloid <Protein>PU.1</Protein> binding site</DNA>. |
| Category-grouped JSON | {“DNA”: [“myeloid PU.1 binding site”], “Protein”: [“PU.1”, “PU.1”], |
| “Cell\_line”: [], “Cell\_type”: [], “RNA”: []} |
| Occurrence-based JSON | [{“text”: “PU.1”, “label”: “Protein”, “occurrence\_index”: 1}, |
| {“text”: “myeloid PU.1 binding site”, “label”: “DNA”, “occurrence\_index”: 1}, |
| {“text”: “PU.1”, “label”: “Protein”, “occurrence\_index”: 2}] |
| Offset-based JSON | [{“text”: “PU.1”, “label”: “Protein”, “start”: 63, “end”: 67}, |
| {“text”: “myeloid PU.1 binding site”, “label”: “DNA”, “start”: 72, “end”: 97}, |
| {“text”: “PU.1”, “label”: “Protein”, “start”: 80, “end”: 84}] |

## B-3f731678be9d44

https://arxiv.org/html/2601.17898v1#chars-8790-19564

## 2 Related Work

NER with Traditional and Pre-trained Models. Traditional NER methods utilize CNN or LSTM approaches for NER [Ma and Hovy (2016)](#bib.bib11); [Yang et al. (2018)](#bib.bib12), where no prior knowledge is used before model training. Subsequently, pre-trained models represented by BERT [Devlin et al. (2019)](#bib.bib4) further enhanced the performance of NER, gradually becoming solid backbone models and reaching state-of-the-art levels [Li et al. (2020a)](#bib.bib7); [Li et al. (2022)](#bib.bib25); [Lu et al. (2022)](#bib.bib28); [Yan et al. (2023)](#bib.bib24). Overall, these methods treat NER as a token-level sequence labeling task, utilizing auto-encoding models for text modeling. [Cui et al. (2021)](#bib.bib6) and [Ma et al. (2022)](#bib.bib3) explore the use of generative BART [Lewis et al. (2020)](#bib.bib5) model for NER, gradually transforming NER from sequence labeling into a sequence-to-sequence generation task, and shifting NER models from auto-encoding representation models to auto-regressive generative models. As a result, the generative NER approach has also demonstrated promising results, while offering good flexibility and generalization.

NER with LLMs and Future Directions. Recent studies employ advanced LLMs for generative NER. [Xie et al. (2023)](#bib.bib2) and [Wei et al. (2023)](#bib.bib9) preliminarily explore the performance of ChatGPT on zero-shot NER. [Kim et al. (2024)](#bib.bib8) test the performance of ChatGPT and LLaMA on nested NER by designing fixed templates. [Zhou et al. (2024)](#bib.bib27) distill knowledge from ChatGPT for NER and [Wang et al. (2025a)](#bib.bib1) investigate the effectiveness of GPT-3 in NER through in-context learning [Brown et al. (2020)](#bib.bib29). These works primarily focus on evaluating zero-shot or few-shot performance of LLMs. We systematically compare the performance of fine-tuned LLMs with traditional state-of-the-art NER models, analyze the impact of different instructions, and explore the memorization and learning capabilities of LLMs for NER tasks, serving as a complement to the aforementioned research efforts.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Datasets | Types | Domain | #Labels | #Train | #Dev | #Test |
| CoNLL2003 | Flat | General | 4 | 14,041 | 3,250 | 3,453 |
| OntoNotes5.0 | Flat | General | 18 | 59,924 | 8,528 | 8,262 |
| ACE2005 | Nested | General | 7 | 7,299 | 971 | 1,060 |
| GENIA | Nested | Biomedical | 5 | 14,835 | 1,854 | 1,854 |

The advancement of LLMs has also given rise to new paradigms for NER. [Huang et al. (2025)](#bib.bib13) employ reinforcement learning to implement NER based on long chain-of-thought reasoning. [Wang et al. (2025b)](#bib.bib10) propose a multi-agent paradigm for zero-shot NER. [Mu et al. (2025)](#bib.bib26) also propose an agent-style framework for multi-domain low-resource NER. These approaches offer new directions for future NER systems.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Models | CoNLL2003 | | | OntoNotes5.0 | | | AvgF1Flat{}^{\text{Flat}}\_{\text{F1}} | ACE2005 | | | GENIA | | | AvgF1Nested{}^{\text{Nested}}\_{\text{F1}} |
| P | R | F1 | P | R | F1 | P | R | F1 | P | R | F1 |
| Pre-Trained NER Models | | | | | | | | | | | | | | |
| BERT-Tagger | 91.20 | 92.30 | 91.70 | 90.01 | 88.35 | 89.16 | 90.43 | - | - | - | - | - | - | - |
| GNN-SL | 93.02 | 93.40 | 93.20 | 91.48 | 91.29 | 91.39 | 92.30 | - | - | - | - | - | - | - |
| ACE + Fine-tune | 93.07 | 94.21 | 93.64 | 91.48 | 91.29 | 91.39 | 92.52 | - | - | - | - | - | - | - |
| BERT-MRC+DSC | 93.41 | 93.25 | 93.33 | 91.59 | 92.56 | 92.07 | 92.70 | - | - | - | - | - | - | - |
| BERT-MRC | 92.33 | 94.61 | 93.04 | 92.98 | 89.95 | 91.11 | 92.08 | 87.16 | 86.59 | 86.88 | 85.18 | 81.12 | 83.75 | 85.32 |
| BINDER | 93.08 | 93.57 | 93.33 | 84.29 | 89.29 | 86.72 | 90.03 | 89.60 | 90.50 | 90.00 | 83.40 | 78.30 | 80.80 | 85.40 |
| W2NER | 92.71 | 93.44 | 93.07 | 90.03 | 90.97 | 90.50 | 91.79 | 85.03 | 88.62 | 86.79 | 81.58 | 79.11 | 80.32 | 83.56 |
| Biaffine+CNN | 92.57 | 93.33 | 92.95 | 90.22 | 90.77 | 90.49 | 91.72 | 86.78 | 87.72 | 87.25 | 81.52 | 79.17 | 80.33 | 83.79 |
| GPT-NER | | | | | | | | | | | | | | |
| GPT-3 (ZS) | 88.54 | 91.40 | 89.97 | 79.17 | 84.29 | 81.73 | 85.85 | 71.72 | 74.20 | 72.96 | 61.38 | 66.74 | 64.06 | 68.51 |
| GPT-3 (ZS w/ Ver.) | 89.47 | 91.77 | 90.62 | 79.64 | 84.52 | 82.08 | 86.35 | 72.63 | 75.39 | 73.46 | 61.77 | 66.81 | 64.29 | 68.88 |
| GPT-3 (FS w/ Ver.) | 89.76 | 92.06 | 90.91 | 79.89 | 84.51 | 82.20 | 86.56 | 72.77 | 75.51 | 73.59 | 61.89 | 66.95 | 64.42 | 69.01 |
| Large Language Models (Inline Bracketed Format) | | | | | | | | | | | | | | |
| LLaMA3.1-8B | 93.50 | 94.21 | 93.85 | 91.23 | 91.32 | 91.28 | 92.57 | 87.16 | 87.85 | 87.51 | 81.93 | 76.62 | 79.18 | 83.35 |
| LLaMA3.2-3B | 92.48 | 93.41 | 92.94 | 89.50 | 89.17 | 89.33 | 91.14 | 80.99 | 82.38 | 81.68 | 79.28 | 70.40 | 74.58 | 78.13 |
| LLaMA3.2-1B | 90.49 | 91.27 | 90.88 | 87.79 | 87.95 | 87.87 | 89.38 | 75.51 | 73.56 | 74.52 | 79.00 | 68.35 | 73.29 | 73.91 |
| Qwen2.5-7B | 93.51 | 93.94 | 93.73 | 90.98 | 90.97 | 90.97 | 92.35 | 86.47 | 86.93 | 86.70 | 81.76 | 75.82 | 78.67 | 82.69 |
| Qwen3-4B | 91.61 | 92.40 | 92.01 | 89.57 | 88.99 | 89.28 | 90.65 | 80.07 | 77.95 | 79.00 | 80.48 | 70.72 | 75.28 | 77.14 |
| Qwen2.5-3B | 91.96 | 92.30 | 92.13 | 89.21 | 88.84 | 89.02 | 90.58 | 78.23 | 73.99 | 76.05 | 80.36 | 68.67 | 74.05 | 75.05 |
| Qwen3-1.7B | 90.52 | 90.62 | 90.57 | 88.39 | 87.44 | 87.91 | 89.24 | 73.57 | 70.73 | 72.12 | 78.58 | 69.45 | 73.73 | 72.93 |
| Qwen2.5-1.5B | 90.79 | 91.27 | 91.03 | 88.36 | 88.15 | 88.26 | 89.65 | 75.21 | 73.80 | 74.50 | 79.81 | 69.97 | 74.57 | 74.54 |
| Average | 91.86 | 92.43 | 92.14 | 89.38 | 89.10 | 89.24 | 90.69 | 79.65 | 78.40 | 79.01 | 80.15 | 71.25 | 75.42 | 77.22 |
| Large Language Models (Inline XML Format) | | | | | | | | | | | | | | |
| LLaMA3.1-8B | 93.57 | 94.09 | 93.83 | 90.84 | 91.05 | 90.94 | 92.39 | 85.30 | 86.98 | 86.13 | 80.78 | 76.18 | 78.41 | 82.27 |
| LLaMA3.2-3B | 90.66 | 91.82 | 91.24 | 89.23 | 88.89 | 89.06 | 90.15 | 79.80 | 81.06 | 80.42 | 78.49 | 71.37 | 74.76 | 77.59 |
| LLaMA3.2-1B | 89.50 | 90.44 | 89.97 | 87.43 | 87.31 | 87.37 | 88.67 | 74.11 | 72.28 | 73.18 | 78.17 | 69.26 | 73.45 | 73.32 |
| Qwen2.5-7B | 93.31 | 93.87 | 93.59 | 90.88 | 90.71 | 90.79 | 92.19 | 85.50 | 86.45 | 85.97 | 81.31 | 77.34 | 79.27 | 82.62 |
| Qwen3-4B | 91.01 | 92.16 | 91.58 | 89.07 | 88.94 | 89.00 | 90.29 | 79.30 | 77.08 | 78.17 | 79.87 | 71.39 | 75.39 | 76.78 |
| Qwen2.5-3B | 90.72 | 91.20 | 90.96 | 88.72 | 88.36 | 88.54 | 89.75 | 76.70 | 74.38 | 75.53 | 79.74 | 69.79 | 74.43 | 74.98 |
| Qwen3-1.7B | 88.57 | 89.16 | 88.87 | 87.00 | 87.33 | 87.17 | 88.02 | 72.93 | 73.17 | 73.05 | 78.27 | 70.24 | 74.04 | 73.55 |
| Qwen2.5-1.5B | 89.60 | 90.78 | 90.18 | 87.92 | 87.89 | 87.90 | 89.04 | 75.11 | 73.63 | 74.36 | 79.58 | 69.20 | 74.03 | 74.20 |
| Average | 90.87 | 91.69 | 91.28 | 88.89 | 88.81 | 88.85 | 90.07 | 78.59 | 78.13 | 78.35 | 79.53 | 71.85 | 75.47 | 76.91 |
| Large Language Models (Category-grouped JSON Format) | | | | | | | | | | | | | | |
| LLaMA3.1-8B | 92.08 | 93.04 | 92.56 | 89.87 | 89.82 | 89.84 | 91.20 | 85.69 | 86.59 | 86.13 | 79.77 | 76.87 | 78.29 | 82.21 |
| LLaMA3.2-3B | 89.24 | 90.49 | 89.86 | 79.71 | 81.45 | 80.57 | 85.22 | 74.90 | 74.16 | 74.53 | 75.53 | 72.49 | 73.98 | 74.26 |
| LLaMA3.2-1B | 88.15 | 88.49 | 88.32 | 79.57 | 77.84 | 78.70 | 83.51 | 69.47 | 68.80 | 69.13 | 73.06 | 69.82 | 71.40 | 70.27 |
| Qwen2.5-7B | 92.44 | 93.04 | 92.74 | 89.49 | 89.46 | 89.48 | 91.11 | 84.79 | 84.88 | 84.84 | 79.37 | 76.97 | 78.15 | 81.50 |
| Qwen3-4B | 89.76 | 90.63 | 90.19 | 79.41 | 81.57 | 80.47 | 85.33 | 77.19 | 76.63 | 76.91 | 76.31 | 74.14 | 75.21 | 76.06 |
| Qwen2.5-3B | 88.26 | 89.98 | 89.11 | 79.10 | 79.26 | 79.18 | 84.15 | 74.45 | 70.71 | 72.53 | 74.21 | 71.11 | 72.63 | 72.58 |
| Qwen3-1.7B | 87.61 | 88.10 | 87.85 | 75.53 | 75.69 | 75.61 | 81.73 | 71.27 | 69.95 | 70.60 | 74.58 | 70.91 | 72.70 | 71.65 |
| Qwen2.5-1.5B | 88.06 | 87.85 | 87.96 | 77.69 | 76.57 | 77.13 | 82.55 | 71.37 | 67.62 | 69.45 | 74.25 | 70.07 | 72.10 | 70.78 |
| Average | 89.45 | 90.20 | 89.82 | 81.30 | 81.46 | 81.37 | 85.60 | 76.14 | 74.92 | 75.52 | 75.89 | 72.80 | 74.31 | 74.92 |
| Large Language Models (Occurrence-based JSON Format) | | | | | | | | | | | | | | |
| LLaMA3.1-8B | 92.89 | 94.19 | 93.54 | 90.27 | 90.76 | 90.52 | 92.03 | 82.78 | 84.06 | 83.41 | 80.07 | 77.30 | 78.66 | 81.04 |
| LLaMA3.2-3B | 91.17 | 92.30 | 91.73 | 82.79 | 82.50 | 82.64 | 87.19 | 71.56 | 68.80 | 70.15 | 74.72 | 72.36 | 73.52 | 71.84 |
| LLaMA3.2-1B | 89.67 | 90.63 | 90.15 | 81.15 | 82.29 | 81.72 | 85.94 | 64.38 | 66.07 | 65.22 | 72.63 | 71.03 | 71.82 | 68.52 |
| Qwen2.5-7B | 93.10 | 93.94 | 93.52 | 89.77 | 90.32 | 90.04 | 91.78 | 81.46 | 81.92 | 81.69 | 78.60 | 76.58 | 77.58 | 79.64 |
| Qwen3-4B | 90.68 | 92.33 | 91.50 | 82.55 | 83.13 | 82.84 | 87.17 | 73.84 | 71.89 | 72.85 | 75.50 | 73.73 | 74.60 | 73.73 |
| Qwen2.5-3B | 90.50 | 91.20 | 90.85 | 81.92 | 80.09 | 81.00 | 85.93 | 70.04 | 66.63 | 68.30 | 74.35 | 70.66 | 72.46 | 70.38 |
| Qwen3-1.7B | 89.03 | 90.28 | 89.65 | 79.03 | 80.31 | 79.67 | 84.66 | 64.63 | 64.69 | 64.66 | 72.86 | 70.38 | 71.60 | 68.13 |
| Qwen2.5-1.5B | 89.61 | 90.24 | 89.93 | 81.16 | 80.70 | 80.93 | 85.43 | 65.71 | 64.56 | 65.13 | 74.84 | 71.58 | 73.17 | 69.15 |
| Average | 90.83 | 91.89 | 91.36 | 83.58 | 83.76 | 83.67 | 87.52 | 71.80 | 71.08 | 71.43 | 75.45 | 72.95 | 74.18 | 72.81 |
| Large Language Models (Offset-based JSON Format) | | | | | | | | | | | | | | |
| LLaMA3.1-8B | 62.91 | 63.53 | 63.22 | 52.99 | 53.63 | 53.31 | 58.27 | 35.53 | 36.17 | 35.85 | 35.16 | 34.09 | 34.62 | 35.24 |
| LLaMA3.2-3B | 38.61 | 39.36 | 38.98 | 16.45 | 16.41 | 16.43 | 27.71 | 12.76 | 12.54 | 12.65 | 8.04 | 7.91 | 7.98 | 10.32 |
| LLaMA3.2-1B | 32.62 | 33.34 | 32.97 | 12.39 | 12.46 | 12.43 | 22.70 | 9.06 | 9.84 | 9.43 | 5.38 | 5.39 | 5.38 | 7.41 |
| Qwen2.5-7B | 60.52 | 61.17 | 60.84 | 50.67 | 51.17 | 50.92 | 55.88 | 32.54 | 32.64 | 32.59 | 32.52 | 31.53 | 32.02 | 32.31 |
| Qwen3-4B | 43.65 | 44.81 | 44.22 | 17.57 | 17.83 | 17.70 | 30.96 | 16.50 | 15.64 | 16.06 | 10.40 | 10.47 | 10.43 | 13.25 |
| Qwen2.5-3B | 16.33 | 16.66 | 16.49 | 5.63 | 5.73 | 5.68 | 11.09 | 6.94 | 6.80 | 6.87 | 3.41 | 3.22 | 3.32 | 5.10 |
| Qwen3-1.7B | 26.34 | 27.32 | 26.82 | 9.88 | 9.97 | 9.92 | 18.37 | 8.82 | 9.21 | 9.01 | 6.05 | 6.17 | 6.11 | 7.56 |
| Qwen2.5-1.5B | 18.82 | 19.07 | 18.94 | 5.63 | 5.53 | 5.58 | 12.26 | 6.35 | 6.07 | 6.21 | 3.57 | 3.57 | 3.57 | 4.89 |
| Average | 37.48 | 38.16 | 37.81 | 21.40 | 21.59 | 21.50 | 29.66 | 16.06 | 16.11 | 16.08 | 13.07 | 12.79 | 12.93 | 14.51 |

## B-412d4c3257b056

https://arxiv.org/html/2601.17898v1#chars-29540-33180

## 4 Entity Recognition or Memorization

LLMs are trained on extensive datasets during the pre-training process. In this section, we investigate whether LLMs genuinely possess entity recognition capabilities or just rely on entity-label memorization when performing generative NER tasks.

Settings. We replace the ground-truth text labels (e.g., LOC, ORG, PER, etc.) with symbols (e.g., A, B, C, etc.) in each sample of CoNLL2003 dataset. We further distinguish two settings based on whether label meaning explanations are provided, as shown in Table [4](#S3.T4 "Table 4 ‣ 3.2 Results ‣ 3 Instructions, Output Format, and Performance of Generative NER ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models"). In the explanation-contained setting, we provide standard entity meaning interpretations for the symbols and denote the transformed dataset as CoNLL2003-SE. In the symbol-only setting, we omit such interpretations, allowing the model to learn the labeling meaning corresponding to each symbol through the training samples during the training process, where the transformed dataset is denoted as CoNLL2003-SO.

|  |  |  |
| --- | --- | --- |
|  | Error Types | Examples of Incorrectly Labeled Output |
| Type | OOD Types | [Inter]ORG{}\_{\textsc{ORG}} will be without suspended [French]MISC{}\_{\textsc{MISC}} defender [Joceyln Angloma]PLAYER{}\_{\textsc{PLAYER}} |
| Wrong Types | [Inter]LOC{}\_{\textsc{LOC}} will be without suspended [French]MISC{}\_{\textsc{MISC}} defender [Joceyln Angloma]PER{}\_{\textsc{PER}} |
| Boundary | Contain Gold | [Inter]ORG{}\_{\textsc{ORG}} will be without suspended [French]MISC{}\_{\textsc{MISC}} [defender Joceyln Angloma]PER{}\_{\textsc{PER}} |
| Contained by Gold | [Inter]ORG{}\_{\textsc{ORG}} will be without suspended [French]MISC{}\_{\textsc{MISC}} defender Joceyln [Angloma]PER{}\_{\textsc{PER}} |
| Overlap with Gold | [Inter]ORG{}\_{\textsc{ORG}} will be without suspended French [defender Joceyln]PER{}\_{\textsc{PER}} Angloma |
| Others | Completely-O | [Inter]ORG{}\_{\textsc{ORG}} will be without [suspended]MISC{}\_{\textsc{MISC}} [French]MISC{}\_{\textsc{MISC}} defender [Joceyln Angloma]PER{}\_{\textsc{PER}} |
| OOD Mentions | [Inter]ORG{}\_{\textsc{ORG}} will be without suspended [French]MISC{}\_{\textsc{MISC}} defender [Joceyln Angloma]PER{}\_{\textsc{PER}} [Milan]ORG{}\_{\textsc{ORG}} |
| Omitted Mentions | [Inter]ORG{}\_{\textsc{ORG}} will be without suspended French defender [Joceyln Angloma]PER{}\_{\textsc{PER}} |

Results. The results with Inline XML format are shown in Table [5](#S3.T5 "Table 5 ‣ 3.2 Results ‣ 3 Instructions, Output Format, and Performance of Generative NER ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models"). We find that: 1) LLMs exhibit a marginal performance drop on datasets with symbol-based labels (by -0.62/-0.42 on CoNLL2003-SE/CoNLL2003-SO, respectively), with the overall change being relatively small; 2) The performance decline on CoNLL2003-SO was smaller, and even LLaMA3.2-3B model shows a slight improvement on CoNLL2003-SO. This may be because the explanations based on symbols introduce additional contextual information that caused some confusion for the model, whereas reasoning solely based on symbolic labels made the model less confused during inference, enabling better symbol-based understanding and reasoning.

Overall, we conclude that LLMs do not rely on strong entity-label memorization in generative NER tasks, but rather demonstrate a considerable capability in entity learning, thereby effectively accomplishing entity recognition tasks.

## B-438038fd5713b6

https://arxiv.org/html/2601.17898v1#chars-47786-48793

## Appendix C Error Type Definitions

Prediction errors are categorized into eight distinct types. The detailed definitions are as follows:

Type Errors. These errors involve correct boundaries but incorrect labeling. OOD Types refer to predicted entity types that do not exist in the provided label set. Wrong Types denote cases where the predicted type is incorrect but belongs to the given label set.

Boundary Errors. These occur when the predicted span is imprecise. Contain Gold describes predicted mentions that enclose the gold mentions. Contained by Gold refers to predicted mentions that are inside the gold mentions. Overlap with Gold covers predictions that overlap with gold mentions but do not fall into the above two cases.

Other Errors. Completely-O represents predicted mentions that have no overlap with any gold mentions. OOD Mentions correspond to hallucinated predictions that do not appear in the input text. Omitted Mentions refer to gold entities that the model fails to identify.

## B-6d7df68138135f

https://arxiv.org/html/2601.17898v1#chars-19633-23660

### 3.1 Settings

Instructions and Output Format. Prompt design is crucial for LLM fine-tuning. It mainly includes the design of instructions primarily used to specify the tasks the model needs to complete, and the output format used for answer generation, extraction, and validation. For the complete instructions, we provide them in Appendix [A](#A1 "Appendix A Full Instructions for Different Datasets ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models") for reproducibility. In this section, we mainly compare five different output formats. Specifically, Inline Bracketed and Inline XML represent an embedded paradigm where entity boundaries and types are inserted directly into the original sentence using brackets or XML tags, yielding natural-language-like outputs. The JSON-based formats treat NER as a structured information extraction task. Category-grouped JSON organizes entities by their label keys, which can only handle the entity-label relationship while ambiguity exists due to the lack of positional information. Occurrence-based JSON records an occurrence order index for each entity, providing a certain level of positional reference, while Offset-based JSON demands precise character-level start and end positions, whose fine-grained positional alignment poses a greater challenge for generative models. We list them in Table [1](#S1.T1 "Table 1 ‣ 1 Introduction ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models").

Datasets. For in-domain evaluation, to fairly compare with pre-trained model based methods, we employ standard datasets and do not use external instruction data such as in UniversalNER [Zhou et al. (2024)](#bib.bib27). For traditional flat NER, we use CoNLL2003 [Tjong Kim Sang and De Meulder (2003)](#bib.bib14) and OntoNotes5.0 [Pradhan et al. (2013)](#bib.bib20) in general domain. For more challenging nested NER, we use ACE200511
1
<https://catalog.ldc.upenn.edu/LDC2006T06> [Walker et al. (2006)](#bib.bib37) in general domain and GENIA [Kim et al. (2003)](#bib.bib15) in molecular biology domain. The statistics of datasets are shown in Table [2](#S2.T2 "Table 2 ‣ 2 Related Work ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models").

Baselines. For pre-trained NER models, we compare BERT-Tagger [Devlin et al. (2019)](#bib.bib4), GNN-SL [Wang et al. (2023)](#bib.bib18), ACE + Fine-tune [Wang et al. (2021)](#bib.bib19), BERT-MRC+DSC [Li et al. (2020b)](#bib.bib38), BERT-MRC [Li et al. (2020a)](#bib.bib7), BINDER [Zhang et al. (2023)](#bib.bib21), W2NER [Li et al. (2022)](#bib.bib25), and Biaffine+CNN [Yan et al. (2023)](#bib.bib24). See Appendix [B](#A2 "Appendix B Brief Introduction of Baselines ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models") for brief introductions of these methods.

We also compare GPT-NER [Wang et al. (2025a)](#bib.bib1), which uses closed-source GPT-3 for generative NER. Three settings are used including zero-shot (ZS), zero-shot with entity verification (ZS w/ Ver.), and few-shot with entity verification (FS w/ Ver.).

Models. We use representative open-source LLaMA [Grattafiori et al. (2024)](#bib.bib16) and Qwen [Yang et al. (2025)](#bib.bib17) models across different versions (LLaMA3.1, LLaMA3.2, Qwen2.5, and Qwen3) with lightweight (1B∼\sim4B) or medium-size (7B∼\sim8B) parameters.

Implementation Details. We fine-tuned all models using the LLaMA-Factory [Zheng et al. (2024)](#bib.bib22) library with LoRA [Hu et al. (2022)](#bib.bib23). Specifically, we set the LoRA rank rr to 256 and the scaling factor α\alpha to 512 inserting adapters on all linear modules. The models were trained with a total batch size of 8 and a learning rate of 2e-5 or 2e-6, utilizing a cosine scheduler and a warmup ratio of 0.01. The maximum length of input is 2048, and the number of training epochs is 2.

We employ Precision (P), Recall (R), and Micro-F1 score (F1) to evaluate NER performance.

## B-8b030965493585

https://arxiv.org/html/2601.17898v1#chars-41701-41846

## Appendix A Full Instructions for Different Datasets

We provide the complete instruction design used for LLMs on generative NER tasks below.

## B-8f3006040e13ba

https://arxiv.org/html/2601.17898v1#chars-33180-38471

## 5 Error Analysis

To understand what types of errors LLMs are prone to make in NER and their specific gaps compared to traditional models, we conduct a statistical analysis of error samples. We follow [Xie et al. (2023)](#bib.bib2) and categorize errors into eight types, as shown in Table [6](#S4.T6 "Table 6 ‣ 4 Entity Recognition or Memorization ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models"). Detailed definitions are in Appendix [C](#A3 "Appendix C Error Type Definitions ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models").

Statistical Results. We present the error distribution statistics for the representative pre-trained model BERT-MRC, and the fine-tuned LLaMA3.1-8B with Inline
Bracketed format in Figure [2](#S4.F2 "Figure 2 ‣ 4 Entity Recognition or Memorization ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models").

Overall, we observe clear differences in error patterns between the two paradigms. BERT-MRC’s errors are dominated by Omitted Mentions(45.5%), indicating a conservative prediction strategy that tends to miss entities.
In contrast, LLaMA3.1-8B exhibits a substantially lower omission rate, reflecting a more aggressive extraction behavior enabled by its extensive pre-training knowledge. However, this higher sensitivity to potential entities leads to a trade-off: the model is prone to over-extraction, resulting in a significantly higher rate of Completely-O errors than BERT-MRC.

The primary error for LLMs is Wrong Types, comprising 38.2% of all errors. This shows while generative models correctly identify entity boundaries, they often misclassify types. This likely arises from a conflict between the model’s strong pre-trained prior knowledge and the specific dataset annotation guidelines. Notably, both models have 0% in OOD Types and OOD Mentions, confirming their adherence to the predefined label set and that all predictions are grounded in the input text.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Errors Types | Input Sentence | Ground Truth | BERT-MRC | LLaMA3.1-8B |
| Omitted Mention | Italy recalled Marcello Cuttitta. | [M. Cuttitta]PER{}\_{\textsc{PER}} | |  | | --- | | O (Missed) | | (45.5%) | | |  | | --- | | [M. Cuttitta]PER{}\_{\textsc{PER}} | | (13.7%) | |
| Wrong Types | In congruence with futures, Permian  cash prices for the weekend fell more… | [Permian]MISC{}\_{\textsc{MISC}} | |  | | --- | | [Permian]MISC{}\_{\textsc{MISC}} | | (29.0%) | | |  | | --- | | [Permian]LOC{}\_{\textsc{LOC}} | | (38.2%) | |
| Completely-O | I’ve also got a contract to play for New  South Wales in the Super 12 next year. | O | |  | | --- | | O | | (11.1%) | | |  | | --- | | [Super 12]MISC{}\_{\textsc{MISC}} | | (25.2%) | |

|  |
| --- |
| O (Missed) |
| (45.5%) |

|  |
| --- |
| [M. Cuttitta]PER{}\_{\textsc{PER}} |
| (13.7%) |

|  |
| --- |
| [Permian]MISC{}\_{\textsc{MISC}} |
| (29.0%) |

|  |
| --- |
| [Permian]LOC{}\_{\textsc{LOC}} |
| (38.2%) |

|  |
| --- |
| O |
| (11.1%) |

|  |
| --- |
| [Super 12]MISC{}\_{\textsc{MISC}} |
| (25.2%) |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Models | TruthfulQA | MMLU | GSM8K | HellaSwag | DROP | Avg. |
| MC1 | Acc | EM | Acc\_norm | F1 |
| LLaMA3.1-8B | 40.15 | 68.76 | 84.69 | 72.53 | 33.20 | 59.87 |
| w/ NER LoRA Fine-tuning (XML) | 36.96 (↓\downarrow3.19) | 67.08 (↓\downarrow1.68) | 80.36 (↓\downarrow4.33) | 70.66 (↓\downarrow1.87) | 58.70 (↑\uparrow25.50) | 62.75 (↑\uparrow2.88) |
| Qwen2.5-7B | 47.49 | 73.42 | 76.57 | 65.43 | 15.74 | 55.73 |
| w/ NER LoRA Fine-tuning (XML) | 45.04 (↓\downarrow2.45) | 72.75 (↓\downarrow0.67) | 79.61 (↑\uparrow3.04) | 68.47 (↑\uparrow3.04) | 61.06 (↑\uparrow45.32) | 65.39 (↑\uparrow9.66) |

Case Study. To intuitively understand the statistical differences discussed above, we provide typical error examples in Table [7](#S5.T7 "Table 7 ‣ 5 Error Analysis ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models").

The first example illustrates a common omission error made by traditional NER models. BERT-MRC omits “Marcello Cuttitta” due to limited pre-training exposure, whereas the LLM correctly extracts it, leveraging extensive world knowledge to recognize unseen entities.

The second example highlights a typical type misclassification made by LLMs. In the phrase “Permian cash price”, the gold standard labels “Permian” as MISC, following the CoNLL2003 guideline that adjectival or derived forms from named entities (e.g., locations, organizations, or persons) should be categorized as miscellaneous. LLaMA3.1-8B predicts “Permian” as LOC, which can be attributed to prior knowledge during large-scale pre-training that associates “Permian” with a geographical region, instead of following the CoNLL2003 annotation guidelines.

The third example demonstrates an over-extraction behavior of LLMs. In this sentence, the gold annotation does not label “Super 12”. However, LLaMA3.1-8B incorrectly labels it as MISC. According to the CoNLL2003 annotation guidelines, the MISC category encompasses a broad and diverse range of entities. This lack of precise semantic boundaries creates ambiguity, making LLMs prone to over-predicting entities.

## B-8f84b6e9be232d

https://arxiv.org/html/2601.17898v1#chars-23660-29540

### 3.2 Results

The results for flat and nested NER are shown in Table [3](#S2.T3 "Table 3 ‣ 2 Related Work ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models"). We conclude the main findings as follows:

The output format has a decisive impact on the performance of generative NER. Among the five designed output formats, the Inline Bracketed and Inline XML formats give the best performance across all LLMs, with average F1 scores (90.69/77.22 and 90.07/76.91) significantly higher than those of the JSON-based formats (85.60/74.92, 87.52/72.81, and 29.66/14.51). This indicates that clear, structured, natural-language-like outputs with inline formats are more conducive to helping LLMs understand and generate accurate entity information, whereas formats requiring concluding the whole information all at once and precise character-offset calculations are poorly suited to the text-generation nature of LLMs, leading to a sharp decline in performance.

Model scale correlates with performance where 1B∼\sim4B models generally lagged behind by up to 10 F1 scores compared to 7B∼\sim8B models. The model size shows a positive correlation with performance. For example, LLaMA3.1-8B and Qwen2.5-7B generally and significantly outperformed their smaller 1B/1.5B/1.7B/3B counterparts across all output formats (e.g., 92.57 vs. 89.38 and 83.35 vs. 73.91 with Inline Bracketed format). These suggest that, under lightweight LoRA fine-tuning, increasing the model size within feasible constraints can improve the performance of NER.

|  |
| --- |
| Instruction I. Symbol-based Label with Explanation (CoNLL2003-SE) |
| Instruction: Your task is to do sequence labeling with labels A, B, C, and D. |
| A: A collective entity such as a company, institution, brand, political or governmental body…(Explanation of ORG) |
| B: A named individual, including humans, animals, fictional characters, and their aliases.  (Explanation of PER) |
| C: A geographical or spatial entity, including natural features, built structures, regions…  (Explanation of LOC) |
| D: Named entities that are not persons, organizations, or locations, including derived…  (Explanation of MISC) |
| Instruction II. Symbol-based Label Only (CoNLL2003-SO) |
| Instruction: Your task is to do sequence labeling with labels A, B, C, and D. |
| Input Sentence and Output with Symbol-based Label Append to the Instructions |
| Input Sentence: Havel praises Czech native Albright as friend. |
| Output: <B>Havel</B> praises <D>Czech</D> native <B>Albright</B> as friend. |

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Models | CoNLL2003 | | | CoNLL2003-SE | | | CoNLL2003-SO | | |
| P | R | F1 | P | R | F1 | P | R | F1 |
| LLaMA3.1-8B | 93.57 | 94.09 | 93.83 | 93.51 | 93.89 | 93.70 (↓\downarrow0.13) | 93.37 | 93.95 | 93.65 (↓\downarrow0.18) |
| LLaMA3.2-3B | 90.66 | 91.82 | 91.24 | 89.87 | 91.15 | 90.51 (↓\downarrow0.73) | 90.98 | 91.75 | 91.36 (↑\uparrow0.12) |
| LLaMA3.2-1B | 89.50 | 90.44 | 89.97 | 88.84 | 89.52 | 89.18 (↓\downarrow0.79) | 89.33 | 90.32 | 89.82 (↓\downarrow0.15) |
| Qwen2.5-7B | 93.31 | 93.87 | 93.59 | 92.95 | 93.43 | 93.19 (↓\downarrow0.40) | 92.79 | 93.41 | 93.10 (↓\downarrow0.49) |
| Qwen3-4B | 91.01 | 92.16 | 91.58 | 90.80 | 91.34 | 91.07 (↓\downarrow0.51) | 90.99 | 91.06 | 91.03 (↓\downarrow0.55) |
| Qwen2.5-3B | 90.72 | 91.20 | 90.96 | 89.72 | 90.97 | 90.34 (↓\downarrow0.62) | 90.41 | 90.83 | 90.62 (↓\downarrow0.34) |
| Qwen3-1.7B | 88.57 | 89.16 | 88.87 | 87.35 | 88.05 | 87.70 (↓\downarrow1.17) | 87.29 | 88.24 | 87.76 (↓\downarrow1.11) |
| Qwen2.5-1.5B | 89.60 | 90.78 | 90.18 | 89.06 | 90.09 | 89.57 (↓\downarrow0.61) | 88.96 | 90.16 | 89.55 (↓\downarrow0.63) |
| Avg. Perf. | 90.87 | 91.69 | 91.28 | 90.26 | 91.05 | 90.66 (↓\downarrow0.62) | 90.52 | 91.22 | 90.86 (↓\downarrow0.42) |

Well-designed output formats enable LLMs to match or surpass some traditional fine-tuning methods and closed-source models. Large models using the inline XML format (e.g., LLaMA3.1-8B) achieved F1 scores (93.85 and 91.28) on datasets like CoNLL2003 and OntoNotes5.0 that are comparable to or even slightly better than many classic fine-tuned pre-trained models (e.g., BERT-MRC with 93.04 and 91.11). The performance is also better than in-context learning results by closed-source GPT-3 models larger than 100B. This demonstrates that with properly constructed prompts, generative NER with open-source LLMs can achieve highly competitive performance, leveraging powerful native language understanding capabilities. Moreover, as shown in Section [6](#S6 "6 Preservation of General Capability ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models"), after instruction tuning on the NER task, the model’s general capability is preserved, with its performance on most tasks remaining unaffected or even improved on some tasks.

Compared with the general domain, LLMs lag behind traditional specialized models in low-resource domains. LLaMA3.1-8B with Inline Bracketed format reaches F1 scores of 93.85, 91.28 and 87.51 on datasets in the general domain, which outperforms specialized models such as BERT-MRC with 93.04, 91.11, and 86.88. However, on GENIA in the biomedical domain, there exists a significant performance gap (79.18 vs. 83.75). This indicates that due to a lack of prior knowledge in low-resource domains, LLMs’ capabilities there are significantly weaker than in the general domains. This highlights the generalization limitations of LLMs in low-resource domains, where their performance is inferior to that in general domains. This gap is again evidenced in NER tasks. Despite LLMs being trained on the same data, their deficiency in low-resource domain knowledge prevents them from surpassing traditional models that have undergone targeted training.

## B-a0e23094f9363f

https://arxiv.org/html/2601.17898v1#chars-209-298

# Assessment of Generative Named Entity Recognition in the Era of Large Language Models

## B-a23a29f73ba935

https://arxiv.org/html/2601.17898v1#chars-298-1636

###### Abstract

Named entity recognition (NER) is evolving from a sequence labeling task into a generative paradigm with the rise of large language models (LLMs). We conduct a systematic evaluation of open-source LLMs on both flat and nested NER tasks. We investigate several research questions including the performance gap between generative NER and traditional NER models, the impact of output formats, whether LLMs rely on memorization, and the preservation of general capabilities after fine-tuning. Through experiments across eight LLMs of varying scales and four standard NER datasets, we find that: (1) With parameter-efficient fine-tuning and structured formats like inline bracketed or XML, open-source LLMs achieve performance competitive with traditional encoder-based models and surpass closed-source LLMs like GPT-3; (2) The NER capability of LLMs stems from instruction-following and generative power, not mere memorization of entity-label pairs; and (3) Applying NER instruction tuning has minimal impact on general capabilities of LLMs, even improving performance on datasets like DROP due to enhanced entity understanding. These findings demonstrate that generative NER with LLMs is a promising, user-friendly alternative to traditional methods. We release the data and code at <https://github.com/szu-tera/LLMs4NER>.

## B-a55160441bc176

https://arxiv.org/html/2601.17898v1#chars-40810-41686

## Limitations

This study primarily focuses on evaluating the NER capabilities of the LLaMA and Qwen model families under instruction tuning. Future improvements could be pursued along two dimensions: First, at the model level, the investigation could be extended to reasoning models with long chain-of-thought output, which offer the advantage of tracing entity labels through the reasoning chain, thereby enhancing interpretability. The current work emphasizes instruction compliance more than the model’s thinking and reasoning abilities. Second, regarding training methodology, reinforcement learning-based approaches such as PPO, DPO, and GRPO have been shown to surpass traditional supervised fine-tuning in terms of eliciting model capability and generalization, yet were not explored in this work. These limitations represent key directions for our future research.

## B-a961e943eddfd0

https://arxiv.org/html/2601.17898v1#chars-41846-42567

### A.1 Instruction Construction Framework

Each instruction follows a unified structural organization. As illustrated in Figure [3](#A1.F3 "Figure 3 ‣ A.1 Instruction Construction Framework ‣ Appendix A Full Instructions for Different Datasets ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models"), the constructed input is composed of three main components: Task Description, which defines the extraction goal and output format; Label Definition Schema, which provides fine-grained semantic constraints for each entity type; Input Sentence, the target text for labeling. These components collectively guide the model to generate the target output according to the specified format.

## B-b8bebfe3afee55

https://arxiv.org/html/2601.17898v1#chars-44833-46325

### A.3 Label Definition Schema

To enhance the semantic understanding of the LLM, particularly for ambiguous or domain-specific entities, we provide explicit definitions for each label in the instructions. These definitions are derived from the official annotation guidelines of each dataset, which serve as the authoritative standard in the dataset’s labeling process. For the CoNLL2003 dataset, the official annotation guidelines contain extensive explanations for the labels, which we have summarized using a large language model to provide concise, standard linguistic definitions. For the GENIA dataset, the official annotation guidelines were not available; therefore, we employed a large language model to generate standard biomedical definitions. The detailed definitions for CoNLL2003, OntoNotes5.0, GENIA, and ACE2005 are provided in Table [10](#A4.T10 "Table 10 ‣ Appendix D AI Assistance Statement ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models"), Table [11](#A4.T11 "Table 11 ‣ Appendix D AI Assistance Statement ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models"), Table [12](#A4.T12 "Table 12 ‣ Appendix D AI Assistance Statement ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models"), and Table [13](#A4.T13 "Table 13 ‣ Appendix D AI Assistance Statement ‣ Assessment of Generative Named Entity Recognition in the Era of Large Language Models"), respectively.

## B-ca3328eb394e7b

https://arxiv.org/html/2601.17898v1#chars-19564-19633

## 3 Instructions, Output Format, and Performance of Generative NER

## B-ef8c7dc9474730

https://arxiv.org/html/2601.17898v1#chars-54113-55452

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

## B-ocr-1a79f5ed684c09

B PDF page 12

Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. 2019. HellaSwag: Can a machine really finish your sentence? In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, pages 4791–4800, Florence, Italy. Association for Computational Linguistics.

Sheng Zhang, Hao Cheng, Jianfeng Gao, and Hoifung Poon. 2023. Optimizing bi-encoder for named entity recognition via contrastive learning. In The Eleventh International Conference on Learning Representations.

Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, and Zheyan Luo. 2024. LlamaFactory: Unified efficient fine-tuning of 100+ language models. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations), pages 400–410, Bangkok, Thailand. Association for Computational Linguistics.

Wenxuan Zhou, Sheng Zhang, Yu Gu, Muhao Chen, and Hoifung Poon. 2024. UniversalNER: Targeted distillation from large language models for open named entity recognition. In The Twelfth International Conference on Learning Representations.

## A Checkpoints of Models

Table 9 lists the checkpoints of the open-source large language models used in our experiments.

[tbl-10.html](tbl-10.html)

Table 9: Checkpoints of open-source models used in our experiments.

## B Full Instructions for Different Datasets

We provide the complete instruction design used for LLMs on generative NER tasks below.

### B.1 Instruction Construction Framework

Each instruction follows a unified structural organization. As illustrated in Figure 4, the constructed input is composed of three main components: Task Description, which defines the extraction goal and

#### Instruction Framework

#### [Task Description]

Your task is to identify all named entities in the input sentence and rewrite the sentence by enclosing each entity using the format <LABEL>Entity Text</LABEL>. Use only the label tags defined in the Label Set below.

#### [Label Definition Schema]

Label Set:

ORG(organization): A collective entity such as a company, institution, brand, political or governmental body, publication, or any organized group of people acting as a unit.

PER(person): A named individual, including humans, animals, fictional characters, and their aliases.

LOC(location): A geographical or spatial entity, including natural features, built structures, regions, public or commercial places, assorted buildings, and abstract or metaphorical places.

MISC(miscellaneous): Named entities that are not persons, organizations, or locations, including derived adjectives, religions, ideologies, nationalities, languages, events, programs, wars, titles of works, slogans, eras, and types of objects.

#### [Input Sentence]

Now process the input sentence:

Figure 4: The template and example of constructing instructions for generative NER.

output format; Label Definition Schema, which provides fine-grained semantic constraints for each entity type; Input Sentence, the target text for labeling. These components collectively guide the model to generate the target output according to the specified format.

### B.2 Task Descriptions for Different Output Formats

We designed five distinct task descriptions corresponding to the output formats. These descriptions explicitly constrain the generation behavior of the LLMs. Table 10 details the specific prompt templates used for each format.

[OCR table id=tbl-10.html; page=12]
<table><tr><td>Model</td><td>Resource Link</td></tr><tr><td></td><td>LLaMA Family</td></tr><tr><td>LLaMA3.1-8B</td><td>meta-llama/Llama-3.1-8B-Instruct</td></tr><tr><td>LLaMA3.2-3B</td><td>meta-llama/Llama-3.2-3B-Instruct</td></tr><tr><td></td><td>Qwen Family</td></tr><tr><td>Qwen2.5-7B</td><td>Qwen/Qwen2.5-7B-Instruct</td></tr><tr><td>Qwen3-4B</td><td>Qwen/Qwen3-4B-Instruct-2507</td></tr><tr><td></td><td>Granite Family</td></tr><tr><td>Granite3.3-8B</td><td>ibm-granite/granite-3.3-8b-instruct</td></tr><tr><td>Granite4-3B</td><td>ibm-granite/granite-4.0-micro</td></tr><tr><td></td><td>Gemma Family</td></tr><tr><td>Gemma2-9B</td><td>google/gemma-2-9b-it</td></tr><tr><td>Gemma3-4B</td><td>google/gemma-3-4b-it</td></tr></table>

## B-ocr-31f00b0a462178

B PDF page 11

Ruotian Ma, Xin Zhou, Tao Gui, Yiding Tan, Linyang Li, Qi Zhang, and Xuanjing Huang. 2022. Template-free prompt tuning for few-shot NER. In Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 5721–5732, Seattle, United States. Association for Computational Linguistics.

Xuezhe Ma and Eduard Hovy. 2016. End-to-end sequence labeling via bi-directional LSTM-CNNs-CRF. In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1064–1074, Berlin, Germany. Association for Computational Linguistics.

Wenxuan Mu, Jinzhong Ning, Di Zhao, and Yijia Zhang. 2026. A multi-agent llm framework for multi-domain low-resource in-context ner via knowledge retrieval, disambiguation and reflective analysis. Proceedings of the AAAI Conference on Artificial Intelligence, 40(38):32528–32536.

OpenAI. 2022. GPT-3.5 turbo model.

OpenAI. 2023. GPT-4 technical report. arXiv preprint arXiv:2303.08774.

Sameer Pradhan, Alessandro Moschitti, Nianwen Xue, Hwee Tou Ng, Anders Björkelund, Olga Uryupina, Yuchen Zhang, and Zhi Zhong. 2013. Towards robust linguistic analysis using OntoNotes. In Proceedings of the Seventeenth Conference on Computational Natural Language Learning, pages 143–152, Sofia, Bulgaria. Association for Computational Linguistics.

Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. 2019. Language models are unsupervised multitask learners. OpenAI blog, 1(8):9.

Susanna Rücker and Alan Akbik. 2023. CleanCoNLL: A nearly noise-free named entity recognition dataset. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 8628–8645, Singapore. Association for Computational Linguistics.

Oscar Sainz, Jon Campos, Iker García-Ferrero, Julen Etxaniz, Oier Lopez de Lacalle, and Eneko Agirre. 2023. NLP evaluation in trouble: On the need to measure LLM data contamination for each benchmark. In Findings of the Association for Computational Linguistics: EMNLP 2023, pages 10776–10787, Singapore. Association for Computational Linguistics.

Erik F. Tjong Kim Sang and Fien De Meulder. 2003. Introduction to the CoNLL-2003 shared task: Language-independent named entity recognition. In Proceedings of the Seventh Conference on Natural Language Learning at HLT-NAACL 2003, pages 142–147.

Christopher Walker, Stephanie Strassel, Julie Medero, and Kazuaki Maeda. 2006. ACE 2005 multilingual training corpus. Linguistic Data Consortium, Philadelphia.

Shuhe Wang, Yuxian Meng, Rongbin Ouyang, Jiwei Li, Tianwei Zhang, Lingjuan Lyu, and Guoyin Wang. 2023. GNN-SL: Sequence labeling based on nearest examples via GNN. In Findings of the Association for Computational Linguistics: ACL 2023, pages 12679–12692, Toronto, Canada. Association for Computational Linguistics.

Shuhe Wang, Xiaofei Sun, Xiaoya Li, Rongbin Ouyang, Fei Wu, Tianwei Zhang, Jiwei Li, Guoyin Wang, and Chen Guo. 2025a. GPT-NER: Named entity recognition via large language models. In Findings of the Association for Computational Linguistics: NAACL 2025, pages 4257–4275, Albuquerque, New Mexico. Association for Computational Linguistics.

Xinyu Wang, Yong Jiang, Nguyen Bach, Tao Wang, Zhongqiang Huang, Fei Huang, and Kewei Tu. 2021. Automated concatenation of embeddings for structured prediction. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pages 2643–2660, Online. Association for Computational Linguistics.

Zihan Wang, Ziqi Zhao, Yougang Lyu, Zhumin Chen, Maarten de Rijke, and Zhaochun Ren. 2025b. A cooperative multi-agent framework for zero-shot named entity recognition. In Proceedings of the ACM on Web Conference 2025, WWW '25, page 4183–4195, New York, NY, USA. Association for Computing Machinery.

Xiang Wei, Xingyu Cui, Ning Cheng, Xiaobin Wang, Xin Zhang, Shen Huang, Pengjun Xie, Jinan Xu, Yufeng Chen, Meishan Zhang, et al. 2023. Zero-shot information extraction via chatting with chatgpt. arXiv preprint arXiv:2302.10205.

Tingyu Xie, Qi Li, Jian Zhang, Yan Zhang, Zuozhu Liu, and Hongwei Wang. 2023. Empirical study of zero-shot NER with ChatGPT. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 7935–7956, Singapore. Association for Computational Linguistics.

Hang Yan, Yu Sun, Xiaonan Li, and Xipeng Qiu. 2023. An embarrassingly easy but strong baseline for nested named entity recognition. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers), pages 1442–1452, Toronto, Canada. Association for Computational Linguistics.

An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. 2025. Qwen3 technical report. arXiv preprint arXiv:2505.09388.

Jie Yang, Shuailong Liang, and Yue Zhang. 2018. Design challenges and misconceptions in neural sequence labeling. In Proceedings of the 27th International Conference on Computational Linguistics, pages 3879–3889, Santa Fe, New Mexico, USA. Association for Computational Linguistics.

## B-ocr-3e26157ed012e2

B PDF page 3

[tbl-0.html](tbl-0.html)

Table 1: Five types of output formats and examples for both flat and nested named entities.

ally becoming solid backbone models and reaching state-of-the-art levels (Li et al., 2020a, 2022; Lu et al., 2022; Yan et al., 2023). Overall, these methods treat NER as a token-level sequence labeling task, utilizing auto-encoding models for text modeling. Cui et al. (2021) and Ma et al. (2022) explore the use of generative BART (Lewis et al., 2020) model for NER, gradually transforming NER from sequence labeling into a sequence-to-sequence generation task, and shifting NER models from auto-encoding representation models to auto-regressive generative models. As a result, the generative NER approach has also demonstrated promising results, while offering good flexibility and generalization.

Generative NER with Large Language Models. Recent studies employ advanced LLMs for generative NER. Xie et al. (2023) and Wei et al. (2023) preliminarily explore the performance of ChatGPT on zero-shot NER. Kim et al. (2024) test the performance of ChatGPT and LLaMA on nested NER by designing fixed templates. Zhou et al. (2024) distill knowledge from ChatGPT for NER and Wang et al. (2025a) investigate the effectiveness of GPT-3 in NER through in-context learning (Brown et al., 2020). These works primarily focus on evaluating zero-shot or few-shot performance of LLMs. However, a comprehensive evaluation and comparison of LLMs for NER tasks remains lacking. We systematically compare the performance of fine-tuned LLMs with traditional state-of-the-art NER models, analyze the impact of different output formats, and explore the memorization and learning capabilities of LLMs for NER tasks, thereby addressing this gap and serving as a complement to the aforementioned research efforts.

[tbl-1.html](tbl-1.html)

Table 2: Statistics of four NER datasets we used.

Recent Exploration on NER. The advancement of LLMs has given rise to new paradigms for NER. Huang et al. (2026) employ reinforcement learning to implement NER based on long chain-of-thought reasoning. Wang et al. (2025b) propose a multi-agent paradigm for zero-shot NER. Mu et al. (2026) also propose an agent-style framework for multidomain low-resource NER. These approaches offer new directions for future NER systems.

## 3 Instructions, Output Format, and Performance of Generative NER

### 3.1 Settings

Instructions and Output Format. Prompt design is crucial for LLM fine-tuning. It mainly includes the design of instructions that specify the tasks the model needs to complete, and the output format used for answer generation, extraction, and validation. The complete instructions are provided in Appendix B for reproducibility.

As listed in Table 1, we compare five different output formats. Inline Bracketed and Inline XML represent an embedded paradigm where entity boundaries and types are inserted directly into the original sentence using brackets or XML tags, yielding natural-language-like outputs that preserve the original text structure. The JSON-based formats treat NER as a structured information extrac-

[OCR table id=tbl-0.html; page=3]
<table><tr><td>Types</td><td>Examples of Labeled Output</td></tr><tr><td>Inline Bracketed</td><td>This is the first demonstration of a specific interaction with [PU.1 | PROTEIN] on a [myeloid [PU.1 | PROTEIN] binding site | DNA].</td></tr><tr><td>Inline XML</td><td>This is the first demonstration of a specific interaction withPU.1on amyeloidPU.1binding site.</td></tr><tr><td>Category-grouped JSON</td><td>{"DNA": ["myeloid PU.1 binding site"], "PROTEIN": ["PU.1", "PU.1"], "CELL_LINE": [], "CELL_TYPE": [], "RNA": []}</td></tr><tr><td>Occurrence-based JSON</td><td>[{"text": "PU.1", "label": "PROTEIN", "occurrence_index": 1}, {"text": "myeloid PU.1 binding site", "label": "DNA", "occurrence_index": 1}, {"text": "PU.1", "label": "PROTEIN", "occurrence_index": 2}]</td></tr><tr><td>Offset-based JSON</td><td>[{"text": "PU.1", "label": "PROTEIN", "start": 63, "end": 67}, {"text": "myeloid PU.1 binding site", "label": "DNA", "start": 73, "end": 98}, {"text": "PU.1", "label": "PROTEIN", "start": 81, "end": 85}]</td></tr></table>

[OCR table id=tbl-1.html; page=3]
<table><tr><td>Datasets</td><td>Types</td><td>Domain</td><td>#Labels</td><td>#Train</td><td>#Dev</td><td>#Test</td></tr><tr><td>CoNLL2003</td><td>Flat</td><td>General</td><td>4</td><td>14,041</td><td>3,250</td><td>3,453</td></tr><tr><td>OntoNotes5.0</td><td>Flat</td><td>General</td><td>18</td><td>59,924</td><td>8,528</td><td>8,262</td></tr><tr><td>ACE2005</td><td>Nested</td><td>General</td><td>7</td><td>7,299</td><td>971</td><td>1,060</td></tr><tr><td>GENIA</td><td>Nested</td><td>Biomedical</td><td>5</td><td>14,835</td><td>1,854</td><td>1,854</td></tr></table>

## B-ocr-498c8f95b7bee0

B PDF page 2

the aforementioned studies test the performance of closed-source models like ChatGPT (OpenAI, 2022) for zero-shot NER, and there is currently a lack of systematic investigation into the effectiveness of fine-tuned open-source LLMs, such as advanced LLaMA (Grattafiori et al., 2024), Qwen (Yang et al., 2025), Granite (IBM Research, 2025) and Gemma (Gemma Team, 2025) models. Specifically, we seek to examine whether generative LLMs represent a reliable approach and whether there is a performance gap compared to traditional pre-trained model methods on both flat and nested NER tasks.

How do different output formats affect the performance of LLMs in generative NER? The performance of LLMs is highly sensitive to the specific instructions given by users. While recent studies have touched upon format designs (Kim et al., 2024; Lv et al., 2025), we systematically explore a more diverse set of output templates as a supplement to the aforementioned work and investigate their specific impact on NER performance. Specifically, we design five distinct output formats (Inline Bracketed, Inline XML, Category-grouped JSON, Occurrence-based JSON, and Offset-based JSON) to compare their impact and investigate whether the performance of different models remains consistent across these various formats.

Do LLMs rely on memorization of entity labels to solve NER tasks? Named entities are prevalent in corpora and are incorporated into the training process of LLMs. Moreover, studies indicate that portions of certain datasets have been leaked during LLM training, casting doubt on the reliability of evaluation results (Sainz et al., 2023; Dong et al., 2024; Balloccu et al., 2024). Therefore, we aim to investigate whether the generative NER capability of LLMs stems merely from memorizing entity-label mappings, rather than from genuinely learning the features of entities and accurately identifying and labeling them. Specifically, we evaluate LLMs under few-shot prompting without fine-tuning and replace standard text labels with arbitrary symbols to test whether models rely on memorized entity-label correlations.

Do LLMs preserve the original capabilities after instruction tuning for NER? One advantage of LLMs is their strong generalization capability, which enables them to perform well across a wide range of tasks. We investigate whether the original abilities of LLMs are affected after instruction tuning on NER tasks. To

this end, we compare the performance of the LLM before and after fine-tuning on multiple datasets, including HellaSwag (Zellers et al., 2019), DROP (Dua et al., 2019), GSM8K (Cobbe et al., 2021), MMLU (Hendrycks et al., 2021), and TruthfulQA (Lin et al., 2022).

In this study, we conduct experiments using eight LLMs with varying sizes and versions of LLaMA, Qwen, Granite, and Gemma across four standard datasets, including two flat NER datasets CoNLL2003 (Tjong Kim Sang and De Meulder, 2003) and OntoNotes5.0 (Pradhan et al., 2013), and two nested NER datasets ACE2005 (Walker et al., 2006) and GENIA (Kim et al., 2003). Empirically, the answers to the above questions are as follows:

1) With parameter-efficient fine-tuning and structured output formats like inline bracketed or inline XML, LLMs match the performance of traditional encoder-based NER models and exceed that of closed-source LLMs like GPT-3. They excel particularly in flat NER within general domains, though further progress is needed for nested NER in domains like biomedicine.

2) The strong performance of LLMs in generative NER tasks stems primarily from their powerful instruction-following and text generation capabilities, rather than from merely memorizing entity-label correlations from training corpora. Error analysis indicates that LLMs tend to generate wrong types, which stems from a misalignment between the rich intrinsic knowledge and the detailed annotation guidelines of datasets.

3) LLMs can retain most of their original capabilities under parameter-efficient fine-tuning for NER tasks, with performance on tasks staying stable or slightly decreasing while improving significantly on benchmarks like DROP (Dua et al., 2019) by 25.50 to 45.32 F1 points. Considering their user-friendly natural language interface, which lowers the barrier for non-experts, generative NER systems hold the potential to gradually supplant traditional sequence labeling based NER models.

## 2 Related Work

NER with Traditional and Pre-trained Models. Traditional NER methods utilize CNN or LSTM approaches for NER (Ma and Hovy, 2016; Yang et al., 2018), where no prior knowledge is used before model training. Subsequently, pre-trained models represented by BERT (Devlin et al., 2019) further enhanced the performance of NER, gradu-

## B-ocr-4a33d4c592441b

B PDF page 8

[tbl-8.html](tbl-8.html)

Table 7: Case study of errors from BERT-MRC and LLaMA3.1-8B. Text in blue indicates incorrect predictions. The number in parentheses indicates the share of each error type among all errors.

[tbl-9.html](tbl-9.html)

Table 8: Performance comparison of LLMs on benchmarks before and after generative NER fine-tuning.

indicating a conservative prediction strategy that tends to miss entities. In contrast, LLaMA3.1-8B exhibits a substantially lower omission rate, reflecting a more aggressive extraction behavior enabled by its extensive pre-training knowledge. However, this higher sensitivity to potential entities leads to a trade-off: the model is prone to over-extraction, resulting in a significantly higher rate of Completely-O errors than BERT-MRC.

The primary error for LLMs is Wrong Types, comprising 38.2% of all errors. This shows that while generative models correctly identify entity boundaries, they often misclassify types. This likely arises from a conflict between the model's strong pre-trained prior knowledge and the specific dataset annotation guidelines. Notably, both models have 0% in OOD Types and OOD Mentions, confirming their adherence to the predefined label set and that all predictions are grounded in the input text.

Case Study. To intuitively understand the statistical differences discussed above, we provide typical error examples in Table 7.

The first example illustrates a common omission error made by traditional NER models. BERT-MRC omits “Marcello Cuttitta” due to limited pre-training exposure, whereas the LLM correctly extracts it, leveraging extensive world knowledge to recognize unseen entities.

The second example highlights a typical type misclassification made by LLMs. In the phrase “Permian cash price”, the gold standard labels

“Permian” as MISC, following the CoNLL2003 guideline that adjectival or derived forms from named entities (e.g., locations, organizations, or persons) should be categorized as miscellaneous. LLaMA3.1-8B predicts “Permian” as LOC, which can be attributed to prior knowledge during large-scale pre-training that associates “Permian” with a geographical region, instead of following the CoNLL2003 annotation guidelines.

The third example demonstrates an over-extraction behavior of LLMs. In this sentence, the gold annotation does not label “Super 12”. However, LLaMA3.1-8B incorrectly labels it as MISC. According to the CoNLL2003 annotation guidelines, the MISC category encompasses a broad and diverse range of entities. This lack of precise semantic boundaries creates ambiguity, making LLMs prone to over-predicting entities.

## 6 Preservation of General Capability

While traditional pre-trained models become single-purpose specialists after task-specific fine-tuning, LLMs retain their inherent multi-task capabilities as general generative models. To examine the impact of generative NER fine-tuning on these general capabilities, we conduct an evaluation across a range of tasks, including reading comprehension (DROP; Dua et al., 2019), commonsense reasoning (HellaSwag; Zellers et al., 2019), multitask language understanding (MMLU; Hendrycks et al., 2021), mathematical reasoning (GSM8K; Cobbe et al., 2021), and truthfulness (TruthfulQA; Lin

[OCR table id=tbl-8.html; page=8]
<table><tr><td>Error Types</td><td>Input Sentence</td><td>Ground Truth</td><td>BERT-MRC</td><td>LLaMA3.1-8B</td></tr><tr><td>Omitted Mentions</td><td>Italy recalledMarcello Cuttitta.</td><td>[M. Cuttitta]PER</td><td>O (Missed)(45.5%)</td><td>[M. Cuttitta]PER(13.7%)</td></tr><tr><td>Wrong Types</td><td>In congruence with futures,Permian cash prices for the weekend fell more...</td><td>[Permian]MISC</td><td>[Permian]MISC(29.0%)</td><td>[Permian]LOC(38.2%)</td></tr><tr><td>Completely-O</td><td>I’ve also got a contract to play for New South Wales in theSuper 12 next year.</td><td>O</td><td>O(11.1%)</td><td>[Super 12]MISC(25.2%)</td></tr></table>

[OCR table id=tbl-9.html; page=8]
<table><tr><td>Models</td><td>TruthfulQA MC1</td><td>MMLU Acc</td><td>GSM8K EM</td><td>HellaSwag Acc_norm</td><td>DROP F1</td><td>Avg.</td></tr><tr><td>LLaMA3.1-8B</td><td>40.15</td><td>68.76</td><td>84.69</td><td>72.53</td><td>33.20</td><td>59.87</td></tr><tr><td>w/ NER LoRA Fine-tuning (XML)</td><td>36.96 (↓3.19)</td><td>67.08 (↓1.68)</td><td>80.36 (↓4.33)</td><td>70.66 (↓1.87)</td><td>58.70 (↑25.50)</td><td>62.75 (↑2.88)</td></tr><tr><td>Qwen2.5-7B</td><td>47.49</td><td>73.42</td><td>76.57</td><td>65.43</td><td>15.74</td><td>55.73</td></tr><tr><td>w/ NER LoRA Fine-tuning (XML)</td><td>45.04 (↓2.45)</td><td>72.75 (↓0.67)</td><td>79.61 (↑3.04)</td><td>68.47 (↑3.04)</td><td>61.06 (↑45.32)</td><td>65.39 (↑9.66)</td></tr></table>

## B-ocr-4e755ed6b769ef

B PDF page 6

Instruction I. Symbol-based Label with Explanations (CoNLL2003-SE)

[tbl-4.html](tbl-4.html)

Instruction II. Symbol-based Label Only (CoNLL2003-SO)

[tbl-5.html](tbl-5.html)

Input Sentence and Output with Symbol-based Labels Appended to the Instructions

[tbl-6.html](tbl-6.html)

Table 5: Examples of two variants of CoNLL2003 with symbol-based labels. The first contains explanations for each symbolic label (CoNLL2003-SE), while the second does not offer explanations in each sample (CoNLL2003-SO).

![img-2.jpeg](img-2.jpeg)

(a)

![img-3.jpeg](img-3.jpeg)

(b)

![img-4.jpeg](img-4.jpeg)

(c)

![img-5.jpeg](img-5.jpeg)

(d)

Figure 2: Investigation of entity-label memorization. (a) and (b) compare few-shot prompting with LoRA SFT on CoNLL2003 (left) and CleanCoNLL (right). (c) and (d) report F1 changes under two variants (SE: with explanations; SO: symbol only) relative to the original dataset.

## 4 Entity Recognition or Memorization?

LLMs are trained on extensive datasets during the pre-training process. In this section, we investigate whether LLMs genuinely possess entity recognition capabilities or just rely on entity-label memorization when performing generative NER tasks.

Settings. We conduct two experiments on both CoNLL2003 and CleanCoNLL (Rücker and Akbik, 2023) with the Inline XML format. CleanCoNLL is a nearly noise-free revision of CoNLL2003 with corrected annotation errors. Because it must be reconstructed locally from the original corpus using the released correction scripts, its fully processed

form is unlikely to have appeared in model pre-training data, making it a more reliable dataset for investigating memorization. Few-shot prompting without fine-tuning: We evaluate all eight LLMs under a 5-shot in-context learning setting. If LLMs had already memorized entity-label mappings during pre-training, they should achieve competitive performance without fine-tuning. Symbol-based label replacement: We replace the ground-truth text labels (e.g., LOC, ORG) with arbitrary symbols (e.g., A, B) in each sample. We further distinguish two settings based on whether label meaning explanations are provided. In the symbolic label with explanations (SE) setting, we pro-

[OCR table id=tbl-4.html; page=6]
<table><tr><td colspan="2">Instruction: Your task is to do sequence labeling with labels A, B, C, and D.</td></tr><tr><td colspan="2">A: A collective entity such as a company, institution, brand, political or governmental body... (Explanation of ORG)</td></tr><tr><td>B: A named individual, including humans, animals, fictional characters, and their aliases.</td><td>(Explanation of PER)</td></tr><tr><td>C: A geographical or spatial entity, including natural features, built structures, regions...</td><td>(Explanation of LOC)</td></tr><tr><td>D: Named entities that are not persons, organizations, or locations, including derived...</td><td>(Explanation of MISC)</td></tr></table>

[OCR table id=tbl-5.html; page=6]
<table><tr><td>Instruction: Your task is to do sequence labeling with labels A, B, C, and D.</td></tr></table>

[OCR table id=tbl-6.html; page=6]
<table><tr><td>Input Sentence: Havel praises Czech native Albright as friend.</td></tr><tr><td>Output: Havel praises Czech native Albright as friend.</td></tr></table>

## B-ocr-6a9010fe0a897a

B PDF page 5

### 3.2 Results

The results for flat and nested NER are shown in Table 3 and Table 4, respectively. We report single-run Micro-F1 scores in the main text and provide the complete Precision, Recall, and F1 results in Appendix H. The main findings are as follows:

The output format has a decisive impact on the performance of generative NER. Among the five output formats, the Inline Bracketed and Inline XML formats achieve the best average performance across all LLMs, with average F1 scores of 91.91/82.85 and 91.71/82.67 on flat and nested NER. Both inline formats consistently outperform the JSON-based formats (90.78/81.69, 91.17/80.07 and 53.91/34.53). These results indicate that clear, structured, natural-language-like inline outputs are more conducive to helping LLMs understand and generate accurate entity information, whereas formats requiring concluding the whole information all at once and precise character-offset calculations are poorly suited to the text-generation nature of LLMs, leading to a sharp decline in performance.

Well-designed output formats enable LLMs to match or surpass some traditional fine-tuning methods and closed-source models. With the Inline Bracketed and XML format, LLaMA3.1-8B achieves 93.85 and 93.83 on CoNLL2003, surpassing all pre-trained NER baselines. On ACE2005, Gemma2-9B achieves 88.02, surpassing BERT-MRC (86.88) and Biaffine+CNN (87.25). Both inline formats also substantially outperform in-context learning by closed-source GPT-3 models. This demonstrates that with properly constructed prompts, generative NER with open-source LLMs can achieve highly competitive performance, leveraging powerful native language understanding capabilities. Moreover, as shown in Section 6, after instruction tuning for NER, the model's general capability is preserved, with performance on some tasks remaining unaffected or even improved.

Compared with the general domain, LLMs lag behind traditional specialized models in low-resource domains. Although LLMs achieve competitive results on general-domain datasets, their performance is less competitive on GENIA in the biomedical domain. The best LLM result is 4.02 F1 points lower than the best specialized model BERT-MRC and falls below other traditional baselines. This indicates that due to a lack of prior knowledge in low-resource domains, LLMs' capabilities there are significantly weaker than in the general

[tbl-3.html](tbl-3.html)

Table 4: Results of pre-trained models, GPT-3, and open-source LLMs on nested NER datasets.

domains. This highlights the generalization limitations of LLMs in low-resource domains, where their performance is inferior to that in general domains. This gap is again evidenced in NER tasks. Despite LLMs being trained on the same data, their deficiency in low-resource domain knowledge prevents them from surpassing traditional models that have undergone targeted training.

[OCR table id=tbl-3.html; page=5]
<table><tr><td>Models</td><td>ACE2005</td><td>GENIA</td><td>Average</td></tr><tr><td colspan="4">Pre-Trained NER Models</td></tr><tr><td>BERT-MRC (Li et al., 2020a)</td><td>86.88</td><td>83.75</td><td>85.32</td></tr><tr><td>BINDER (Zhang et al., 2023)</td><td>90.00</td><td>80.80</td><td>85.40</td></tr><tr><td>W2NER (Li et al., 2022)</td><td>86.79</td><td>80.32</td><td>83.56</td></tr><tr><td>Biaffine+CNN (Yan et al., 2023)</td><td>87.25</td><td>80.33</td><td>83.79</td></tr><tr><td colspan="4">GPT-NER (Wang et al., 2025a)</td></tr><tr><td>GPT-3 (ZS)</td><td>72.96</td><td>64.06</td><td>68.51</td></tr><tr><td>GPT-3 (ZS w/ Ver.)</td><td>73.46</td><td>64.29</td><td>68.88</td></tr><tr><td>GPT-3 (FS w/ Ver.)</td><td>73.59</td><td>64.42</td><td>69.01</td></tr><tr><td colspan="4">Open-Source LLMs (Inline Bracketed)</td></tr><tr><td>LLaMA3.1-8B</td><td>87.51</td><td>79.18</td><td>83.35</td></tr><tr><td>LLaMA3.2-3B</td><td>85.82</td><td>79.15</td><td>82.49</td></tr><tr><td>Qwen2.5-7B</td><td>86.70</td><td>78.67</td><td>82.69</td></tr><tr><td>Qwen3-4B</td><td>86.48</td><td>79.16</td><td>82.82</td></tr><tr><td>Granite3.3-8B</td><td>86.81</td><td>78.87</td><td>82.84</td></tr><tr><td>Granite4-3B</td><td>86.78</td><td>78.42</td><td>82.60</td></tr><tr><td>Gemma2-9B</td><td>87.44</td><td>79.73</td><td>83.59</td></tr><tr><td>Gemma3-4B</td><td>86.20</td><td>78.64</td><td>82.42</td></tr><tr><td>Average</td><td>86.72</td><td>78.98</td><td>82.85</td></tr><tr><td colspan="4">Open-Source LLMs (Inline XML)</td></tr><tr><td>LLaMA3.1-8B</td><td>86.13</td><td>78.41</td><td>82.27</td></tr><tr><td>LLaMA3.2-3B</td><td>86.26</td><td>78.22</td><td>82.24</td></tr><tr><td>Qwen2.5-7B</td><td>85.97</td><td>79.27</td><td>82.62</td></tr><tr><td>Qwen3-4B</td><td>85.66</td><td>79.60</td><td>82.63</td></tr><tr><td>Granite3.3-8B</td><td>87.27</td><td>79.09</td><td>83.18</td></tr><tr><td>Granite4-3B</td><td>86.84</td><td>78.61</td><td>82.73</td></tr><tr><td>Gemma2-9B</td><td>88.02</td><td>79.32</td><td>83.67</td></tr><tr><td>Gemma3-4B</td><td>85.62</td><td>78.46</td><td>82.04</td></tr><tr><td>Average</td><td>86.47</td><td>78.87</td><td>82.67</td></tr><tr><td colspan="4">Open-Source LLMs (Category-grouped JSON)</td></tr><tr><td>LLaMA3.1-8B</td><td>86.13</td><td>78.29</td><td>82.21</td></tr><tr><td>LLaMA3.2-3B</td><td>83.69</td><td>77.99</td><td>80.84</td></tr><tr><td>Qwen2.5-7B</td><td>84.84</td><td>78.15</td><td>81.50</td></tr><tr><td>Qwen3-4B</td><td>84.35</td><td>78.48</td><td>81.42</td></tr><tr><td>Granite3.3-8B</td><td>86.23</td><td>78.47</td><td>82.35</td></tr><tr><td>Granite4-3B</td><td>84.77</td><td>78.38</td><td>81.58</td></tr><tr><td>Gemma2-9B</td><td>86.64</td><td>78.93</td><td>82.79</td></tr><tr><td>Gemma3-4B</td><td>84.51</td><td>77.18</td><td>80.85</td></tr><tr><td>Average</td><td>85.14</td><td>78.23</td><td>81.69</td></tr><tr><td colspan="4">Open-Source LLMs (Occurrence-based JSON)</td></tr><tr><td>LLaMA3.1-8B</td><td>83.41</td><td>78.66</td><td>81.04</td></tr><tr><td>LLaMA3.2-3B</td><td>80.93</td><td>77.41</td><td>79.17</td></tr><tr><td>Qwen2.5-7B</td><td>81.69</td><td>77.58</td><td>79.64</td></tr><tr><td>Qwen3-4B</td><td>81.58</td><td>78.47</td><td>80.03</td></tr><tr><td>Granite3.3-8B</td><td>83.02</td><td>78.27</td><td>80.65</td></tr><tr><td>Granite4-3B</td><td>81.88</td><td>77.25</td><td>79.57</td></tr><tr><td>Gemma2-9B</td><td>84.29</td><td>79.12</td><td>81.71</td></tr><tr><td>Gemma3-4B</td><td>81.58</td><td>76.03</td><td>78.81</td></tr><tr><td>Average</td><td>82.30</td><td>77.85</td><td>80.07</td></tr><tr><td colspan="4">Open-Source LLMs (Offset-based JSON)</td></tr><tr><td>LLaMA3.1-8B</td><td>35.85</td><td>34.62</td><td>35.24</td></tr><tr><td>LLaMA3.2-3B</td><td>27.31</td><td>25.79</td><td>26.55</td></tr><tr><td>Qwen2.5-7B</td><td>32.59</td><td>32.02</td><td>32.31</td></tr><tr><td>Qwen3-4B</td><td>35.41</td><td>36.81</td><td>36.11</td></tr><tr><td>Granite3.3-8B</td><td>36.90</td><td>39.54</td><td>38.22</td></tr><tr><td>Granite4-3B</td><td>33.30</td><td>36.80</td><td>35.05</td></tr><tr><td>Gemma2-9B</td><td>40.80</td><td>41.15</td><td>40.98</td></tr><tr><td>Gemma3-4B</td><td>31.60</td><td>32.00</td><td>31.80</td></tr><tr><td>Average</td><td>34.22</td><td>34.84</td><td>34.53</td></tr></table>

## B-ocr-6f798d0e23e65d

B PDF page 15

[tbl-13.html](tbl-13.html)

Table 12: Impact of character-offset errors on Offset-based JSON performance.  \( F_{1}^{w/o offset} \)  removes the offset-matching requirement, revealing that models identify entities accurately but struggle with precise positional alignment. Green values indicate the absolute F1 improvement from ignoring offsets.

![img-9.jpeg](img-9.jpeg)

Figure 6: Distribution of character-offset errors by boundary displacement d for two representative models across four datasets.

Magnitude of character-offset errors. We further examine predictions whose entity text and label are correct but whose offsets are incorrect. For each prediction, we define the boundary displacement as  \( d = \max(|\hat{s} - s|, |\hat{e} - e|) \) , where  \( (\hat{s}, \hat{e}) \)  and  \( (s, e) \)  are the predicted and gold start and end offsets, respectively. As shown in Figure 6, across all models and datasets, 81–90% of offset errors fall within 3 characters, and large deviations (>10 characters) account for only 1–3%.

Together, these analyses confirm that the low Offset-based JSON scores are caused by character-level offset misalignment, not by failures in entity recognition, and that most errors involve only small boundary deviations. These results indicate that exact character indexing is difficult for autoregressive language models. Clearer instructions and additional examples may reduce some errors, but they are unlikely to remove the problem entirely.

[tbl-14.html](tbl-14.html)

Table 13: Cost-benefit comparison between LLaMA3.1-8B and BERT-MRC on CoNLL2003.

## G Cost-Benefit Analysis

We further conduct a cost-benefit experiment between the best-performing generative NER model, LLaMA3.1-8B with the Inline Bracketed format, and a representative traditional NER model, BERT-MRC, on CoNLL2003. Both models were trained on a single NVIDIA L40 GPU (48GB). The results are shown in Table 13.

While LLaMA3.1-8B requires slightly more resources than BERT-MRC, the gap is modest considering its strong performance (93.85 vs. 93.04). This trade-off demonstrates the viability of generative NER under resource-efficient fine-tuning.

## H Full Precision, Recall, and F1 Results

To provide a complete view of model performance, we report Precision, Recall, and F1 scores for the flat and nested NER experiments in Table 18.

## I Error Type Definitions

Prediction errors are categorized into eight distinct types. The detailed definitions are as follows:

Type Errors. These errors involve correct boundaries but incorrect labeling. OOD Types refer to predicted entity types that do not exist in the pro-

[OCR table id=tbl-13.html; page=15]
<table><tr><td rowspan="2">Model</td><td colspan="2">CoNLL2003</td><td colspan="2">OntoNotes5.0</td><td colspan="2">ACE2005</td><td colspan="2">GENIA</td></tr><tr><td>F1</td><td>\( F_1^{w/o offset} \)</td><td>F1</td><td>\( F_1^{w/o offset} \)</td><td>F1</td><td>\( F_1^{w/o offset} \)</td><td>F1</td><td>\( F_1^{w/o offset} \)</td></tr><tr><td>LLaMA3.1-8B</td><td>63.22</td><td>92.64 (↑29.42)</td><td>53.31</td><td>87.60 (↑34.29)</td><td>35.85</td><td>81.60 (↑45.75)</td><td>34.62</td><td>77.96 (↑43.34)</td></tr><tr><td>LLaMA3.2-3B</td><td>56.13</td><td>91.91 (↑35.78)</td><td>31.20</td><td>84.71 (↑53.51)</td><td>27.31</td><td>79.54 (↑52.23)</td><td>25.79</td><td>76.63 (↑50.84)</td></tr><tr><td>Qwen2.5-7B</td><td>60.84</td><td>92.74 (↑31.90)</td><td>50.92</td><td>87.59 (↑36.67)</td><td>32.59</td><td>80.61 (↑48.02)</td><td>32.02</td><td>76.45 (↑44.43)</td></tr><tr><td>Qwen3-4B</td><td>61.18</td><td>91.97 (↑30.79)</td><td>38.34</td><td>84.76 (↑46.42)</td><td>35.41</td><td>80.07 (↑44.66)</td><td>36.81</td><td>77.33 (↑40.52)</td></tr><tr><td>Granite3.3-8B</td><td>64.79</td><td>92.90 (↑28.11)</td><td>44.08</td><td>87.05 (↑42.97)</td><td>36.90</td><td>81.86 (↑44.96)</td><td>39.54</td><td>77.50 (↑37.96)</td></tr><tr><td>Granite4-3B</td><td>61.40</td><td>92.40 (↑31.00)</td><td>38.91</td><td>86.85 (↑47.94)</td><td>33.30</td><td>80.95 (↑47.65)</td><td>36.80</td><td>77.01 (↑40.21)</td></tr><tr><td>Gemma2-9B</td><td>65.53</td><td>92.47 (↑26.94)</td><td>61.45</td><td>89.35 (↑27.90)</td><td>40.80</td><td>83.30 (↑42.50)</td><td>41.15</td><td>77.93 (↑36.78)</td></tr><tr><td>Gemma3-4B</td><td>59.85</td><td>92.24 (↑32.39)</td><td>51.35</td><td>86.28 (↑34.93)</td><td>31.60</td><td>79.11 (↑47.51)</td><td>32.00</td><td>75.65 (↑43.65)</td></tr><tr><td>Average</td><td>61.62</td><td>92.41 (↑30.79)</td><td>46.20</td><td>86.77 (↑40.58)</td><td>34.22</td><td>80.88 (↑46.66)</td><td>34.84</td><td>77.06 (↑42.22)</td></tr></table>

[OCR table id=tbl-14.html; page=15]
<table><tr><td>Metric</td><td>LLaMA3.1-8B</td><td>BERT-MRC</td></tr><tr><td>Training Time (h)</td><td>2.40</td><td>2.31</td></tr><tr><td>Trainable Parameters (M)</td><td>671</td><td>335</td></tr><tr><td>Peak GPU Memory (GiB)</td><td>27.89</td><td>21.62</td></tr><tr><td>F1</td><td>93.85</td><td>93.04</td></tr></table>

## B-ocr-7a748270f6b518

B PDF page 7

[tbl-7.html](tbl-7.html)

Table 6: Error types based on the sentence: “[Inter] \( _{ORG} \)  will be without suspended [French] \( _{MISC} \)  defender [Joceyln Angloma] \( _{PER} \) .” Underlined entities denote correct predictions, while blue bold spans highlight specific errors.

![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)

Figure 3: Distribution of error types for BERT-MRC and LLaMA3.1-8B on CoNLL2003.

vide standard entity meaning interpretations for the symbols and denote the transformed datasets as CoNLL2003-SE and CleanCoNLL-SE. In the symbol-only (SO) setting, we omit such interpretations, allowing the model to learn the meaning of each symbol solely from the training examples. The transformed datasets are denoted as CoNLL2003-SO and CleanCoNLL-SO.

Results. As shown in Figure 2(a) and (b), all LLMs achieve moderate F1 scores under 5-shot prompting on both CoNLL2003 and CleanCoNLL, far below fine-tuning performance. This large gap indicates that even if LLMs were exposed to the sentences during pre-training, their generative NER ability remains limited. The NER capability is mainly acquired through instruction tuning.

From the symbol-based label experiment in Figure 2(c) and (d), we find that: 1) LLMs exhibit only marginal F1 changes on both datasets (average \(\Delta\)F1 of \(-0.17\) on CoNLL2003-SE and \(+0.01\) on CoNLL2003-SO; \(-0.04\) on CleanCoNLL-SE and \(+0.02\) on CleanCoNLL-SO); 2) The symbol-only setting even yields slight average increases on both datasets. This may be because symbol expla

nations introduce additional context that confuses the model, whereas pure symbolic labels reduce inference-time ambiguity.

Overall, we reach the same conclusion on both datasets: LLMs do not rely on entity-label memorization in generative NER tasks, but rather demonstrate a considerable capability in entity learning, thereby effectively accomplishing entity recognition tasks.

## 5 Error Analysis on Generative NER

To understand what types of errors LLMs are prone to make in NER and their specific gaps compared to traditional models, we conduct a statistical analysis of error samples. We follow Xie et al. (2023) and categorize errors into eight types, as shown in Table 6. Detailed definitions are in Appendix I.

Statistical Results. We present the error distribution statistics for the representative pre-trained model BERT-MRC, and the fine-tuned LLaMA3.1-8B with Inline Bracketed format in Figure 3.

Overall, we observe clear differences in error patterns between the two paradigms. BERT-MRC's errors are dominated by Omitted Mentions (45.5%),

[OCR table id=tbl-7.html; page=7]
<table><tr><td></td><td>Error Types</td><td>Examples of Incorrectly Labeled Output</td></tr><tr><td rowspan="2">Type</td><td>OOD Types</td><td>\( [Inter]_{ORG} \) will be without suspended \( [French]_{MISC} \) defender \( [Joceyln Angloma]_{PLAYER} \)</td></tr><tr><td>Wrong Types</td><td>\( [Inter]_{LOC} \) will be without suspended \( [French]_{MISC} \) defender \( [Joceyln Angloma]_{PER} \)</td></tr><tr><td rowspan="3">Boundary</td><td>Contain Gold</td><td>\( [Inter]_{ORG} \) will be without suspended \( [French]_{MISC} \) [defender Joceyln Angloma]\( _{PER} \)</td></tr><tr><td>Contained by Gold</td><td>\( [Inter]_{ORG} \) will be without suspended \( [French]_{MISC} \) defender Joceyln \( [Angloma]_{PER} \)</td></tr><tr><td>Overlap with Gold</td><td>\( [Inter]_{ORG} \) will be without suspended French \( [defender Joceyln]_{PER} \) Angloma</td></tr><tr><td rowspan="3">Others</td><td>Completely-O</td><td>\( [Inter]_{ORG} \) will be without \( [suspended]_{MISC} \) \( [French]_{MISC} \) defender \( [Joceyln Angloma]_{PER} \)</td></tr><tr><td>OOD Mentions</td><td>\( [Inter]_{ORG} \) will be without suspended \( [French]_{MISC} \) defender \( [Joceyln Angloma]_{PER} \) \( [Milan]_{ORG} \)</td></tr><tr><td>Omitted Mentions</td><td>\( [Inter]_{ORG} \) will be without suspended \( French \) defender \( [Joceyln Angloma]_{PER} \)</td></tr></table>

## B-ocr-86b167ad91f94b

B PDF page 9

et al., 2022). We use the lm-evaluation-harness framework (Gao et al., 2024) for comparison.

The results are shown in Table 8. We find that the fine-tuned LLMs performed comparably to the original model across most of the tasks, with only minor fluctuations ranging from a \(4.33\%\) decrease to a \(3.04\%\) increase. Notably, on the reading comprehension benchmark DROP, the fine-tuned model achieves a substantial performance gain of 25.50 to 45.32 F1 scores. The improvement could be attributed to the fact that DROP answers are often text spans containing named entities (e.g., persons, locations, organizations). Fine-tuning for NER strengthens the model's ability to detect these entities, leading to more precise answer extraction. Overall, the results suggest that the core capabilities of LLMs remain largely intact after undergoing lightweight fine-tuning for the NER task.

## 7 Conclusion

We present a comprehensive assessment of generative NER using open-source LLMs. Our experiments show that LLMs, when fine-tuned with parameter-efficient methods and appropriate output formats, can match or even exceed the performance of strong traditional NER models, while maintaining robust multi-task capabilities. Furthermore, we find that LLMs keep genuine learning on NER task instead of memorizing entity-label correlations. These findings confirm the viability of generative NER as a flexible and effective paradigm, highlighting its potential to gradually supplement traditional sequence labeling approaches.

### Limitations

This study primarily focuses on evaluating the NER capabilities of LLaMA, Qwen, Granite, and Gemma model families under instruction tuning. Future improvements could be pursued along two dimensions: First, at the model level, the investigation could be extended to reasoning models with long chain-of-thought output, which offer the advantage of tracing entity labels through the reasoning chain, thereby enhancing interpretability. The current work emphasizes instruction compliance more than the model's thinking and reasoning abilities. Second, regarding training methodology, reinforcement learning-based approaches such as PPO, DPO, and GRPO have been shown to surpass traditional supervised fine-tuning in terms of eliciting model capability and generalization, yet

were not explored in this work. These limitations represent key directions for our future research.

### Acknowledgments

This work was supported in part by ICFCRT (W2441020), Guangdong Basic and Applied Basic Research Foundation (2026A1515011358), Youth S&T Talent Support Programme of Guangdong Provincial Association for Science and Technology (SKXRC2026862), Shenzhen Natural Science Foundation (JCYJ20250604181610014), Intelligent Computing Center of Shenzhen University, and Scientific Development Fund from Guangdong Provincial Key Laboratory of Visual Media and Multidimensional Intelligence.

## References

Simone Balloccu, Patrícia Schmidtová, Mateusz Lango, and Ondrej Dusek. 2024. Leak, cheat, repeat: Data contamination and evaluation malpractices in closed-source LLMs. In Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), pages 67–93, St. Julian's, Malta. Association for Computational Linguistics.

Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. 2020. Language models are few-shot learners. In Advances in Neural Information Processing Systems, volume 33, pages 1877–1901. Curran Associates, Inc.

Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. 2021. Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168.

Leyang Cui, Yu Wu, Jian Liu, Sen Yang, and Yue Zhang. 2021. Template-based named entity recognition using BART. In Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021, pages 1835–1845, Online. Association for Computational Linguistics.

DeepSeek-AI. 2024. Deepseek-V3 technical report. arXiv preprint arXiv:2412.19437.

Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of

## B-ocr-9a02907be76488

B PDF page 1

arXiv:2601.17898v3 [cs.CL] 9 Oct 2026

# Assessment of Generative Named Entity Recognition in the Era of Large Language Models

Qi Zhan, Yile Wang \( ^{*} \) , Hui Huang

Guangdong Provincial Key Laboratory of Visual Media and Multidimensional Intelligence
CSSE, Shenzhen University

qzhan65@gmail.com, wangyile@szu.edu.cn, hhzhiyan@gmail.com

## Abstract

Named entity recognition (NER) is evolving from a sequence labeling task into a generative paradigm with the rise of large language models (LLMs). We conduct a systematic evaluation of open-source LLMs on both flat and nested NER tasks. We investigate several research questions including the performance gap between generative NER and traditional NER models, the impact of output formats, whether LLMs rely on memorization, and the preservation of general capabilities after fine-tuning. Through experiments across eight LLMs of varying scales and four standard NER datasets, we find that: (1) With parameter-efficient fine-tuning and structured formats like inline bracketed or XML, open-source LLMs achieve performance competitive with traditional encoder-based models and surpass decoder-based LLMs with in-context learning techniques; (2) The NER capability of LLMs stems from instruction-following and generative power, not mere memorization of entity-label pairs; and (3) Applying NER instruction tuning has minimal impact on general capabilities of LLMs, even improving performance on datasets like DROP by 25.50 to 45.32 F1 points due to enhanced entity understanding. These findings demonstrate that generative NER with LLMs is a promising, user-friendly alternative to traditional methods. We release the data and code at https://github.com/szutera/LLMs4NER.

## 1 Introduction

Named entity recognition (NER) is a fundamental task in natural language processing, widely used in downstream applications such as relation extraction, knowledge graph construction, information retrieval, and question answering systems. As a typical sequence labeling task, approaches based on traditional auto-encoding pre-trained models

NER as Sequence Labeling

![img-0.jpeg](img-0.jpeg)

Generative NER

![img-1.jpeg](img-1.jpeg)

Figure 1: Comparison between traditional NER based on pre-trained models (top) and generative NER based on large language models (bottom).

have achieved strong results (Devlin et al., 2019; Li et al., 2020a; Lu et al., 2022; Yan et al., 2023).

The development of generative pre-trained models (Radford et al., 2019; Lewis et al., 2020) and large language models (LLMs; Brown et al., 2020; OpenAI, 2022, 2023; DeepSeek-AI, 2024) is gradually shifting the traditional NER task toward a unified generative paradigm. As shown in Figure 1, LLMs sequentially generate user-provided sentences along with their corresponding entity labels in textual form. This approach demonstrates strong interactivity, generalization, and user-friendliness. Recent studies have conducted preliminary investigations into NER based on LLMs by crafting specific prompts (Xie et al., 2023; Wei et al., 2023; Kim et al., 2024; Wang et al., 2025a), also achieving promising results.

In this work, we aim to further explore the following research questions: In terms of performance, is generative NER with open-source LLMs a reliable approach compared with advanced pre-trained NER models? Most of

## B-ocr-9a738363dfdac6

B PDF page 14

[tbl-12.html](tbl-12.html)

Table 11: Comparison between LoRA fine-tuning and full fine-tuning on CoNLL2003 and GENIA. Numbers in parentheses denote the difference compared with LoRA fine-tuning.

as a machine reading comprehension task, achieving SOTA performance on the GENIA dataset. BINDER (Zhang et al., 2023) aligns spans and types in a shared space via a bi-encoder and contrastive learning, distinguishing entities with dynamic thresholding. W2NER (Li et al., 2022) unifies flat, nested, and discontinuous NER by modeling word-word relations on a 2D grid to capture token interactions. Biaffine+CNN (Yan et al., 2023) treats the span feature grid generated by a biaffine decoder as an image, utilizing CNNs to model spatial correlations between neighboring spans for nested entity recognition.

## D Comparison between LoRA and Full Fine-Tuning

We compare LoRA with full fine-tuning to determine which strategy is more effective for generative NER. The two well-performing models, LLaMA3.1-8B and Qwen2.5-7B, are fine-tuned on the flat NER dataset (CoNLL2003) and the nested NER dataset (GENIA). Both fine-tuning methods use the same training configuration. The F1 results are shown in Table 11.

Across all settings, LoRA fine-tuning obtains slightly higher F1 scores than full fine-tuning. Moreover, because the number of trainable parameters in LoRA is much closer to that of traditional NER models, LoRA also provides a fairer basis for comparing generative and traditional approaches. Therefore, we adopt LoRA as the fine-tuning strategy for all LLMs in our main experiments.

## E Breakdown of Flat and Nested Entity Performance

We further break down performance on the two nested NER datasets, ACE2005 and GENIA, according to the structural relation between entity spans. We define a nested entity as a gold entity whose span strictly contains or is strictly contained by another gold entity in the same sentence. A flat

![img-8.jpeg](img-8.jpeg)

Figure 5: Performance on flat and nested entity mentions in the two nested NER datasets, averaged across eight LLMs for each output format. Downward arrows report the F1 decrease from flat to nested entities.

entity neither contains nor is contained by another gold entity. We compute entity-level Micro-F1 separately for these two disjoint subsets and average the scores across all eight LLMs.

As shown in Figure 5, nested entities consistently achieve lower F1 scores than flat entities across all output formats and on both datasets, indicating that they are more difficult to recognize. Excluding the Offset-based JSON format, whose overall scores are too low for meaningful comparison, the flat-to-nested F1 decrease on GENIA is consistently larger than on ACE2005, suggesting that nested entity recognition is particularly challenging in the biomedical domain.

## F Error Analysis of the Offset-based JSON Format

The Offset-based JSON format yields substantially lower F1 scores than the other formats, as reported in Tables 3 and 4. To further investigate the reasons for the low Offset-based JSON performance, we present two complementary analyses below.

Entity recognition vs. offset generation. We re-evaluate predictions under two criteria. Standard F1 requires an exact match of the entity text, label, and character offsets.  \( F_{1}^{w/o\ offset} \)  matches only the entity text and label. As shown in Table 12, ignoring offsets leads to large improvements across all models and datasets, with performance approaching that of the inline formats. This confirms that the models usually accurately identify entities, while the primary difficulty lies in precise character-level offset alignment.

[OCR table id=tbl-12.html; page=14]
<table><tr><td>Model</td><td>Fine-tuning</td><td>CoNLL2003</td><td>GENIA</td></tr><tr><td>LLaMA3.1-8B</td><td>LoRA</td><td>93.85</td><td>79.18</td></tr><tr><td>LLaMA3.1-8B</td><td>Full</td><td>93.61 (↓0.24)</td><td>78.70 (↓0.48)</td></tr><tr><td>Qwen2.5-7B</td><td>LoRA</td><td>93.73</td><td>78.67</td></tr><tr><td>Qwen2.5-7B</td><td>Full</td><td>93.58 (↓0.15)</td><td>78.53 (↓0.14)</td></tr></table>

## B-ocr-aa81bd82a4d6a0

B PDF page 16

vided label set. Wrong Types denote cases where the predicted type is incorrect but belongs to the given label set.

Boundary Errors. These occur when the predicted span is imprecise. Contain Gold describes predicted mentions that enclose the gold mentions. Contained by Gold refers to predicted mentions that are inside the gold mentions. Overlap with Gold covers predictions that overlap with gold mentions but do not fall into the above two cases.

Other Errors. Completely-O represents predicted mentions that have no overlap with any gold mentions. OOD Mentions correspond to hallucinated predictions that do not appear in the input text. Omitted Mentions refer to gold entities that the model fails to identify.

## J AI Assistance Statement

We utilized LLMs (e.g., ChatGPT) to assist in polishing the text, refining grammar, and improving the clarity of the manuscript. All content was reviewed and verified by the authors.

As detailed in Appendix B.3, we employed LLMs to summarize official annotation guidelines for CoNLL2003 dataset and generate standard biomedical definitions for GENIA dataset to construct the label definition schema used in our instruction tuning prompts.

## B-ocr-ceb2a6218e785f

B PDF page 18

[tbl-17.html](tbl-17.html)

Table 16: Label definitions for GENIA dataset.

[tbl-18.html](tbl-18.html)

Table 17: Label definitions for ACE2005 dataset.

[OCR table id=tbl-17.html; page=18]
<table><tr><td>Labels</td><td>Definition</td></tr><tr><td>DNA</td><td>Deoxyribonucleic acid sequences or molecules, including genes, gene fragments, promoters, enhancers, and other genomic regions that encode or regulate biological information.</td></tr><tr><td>RNA</td><td>Ribonucleic acid molecules transcribed from DNA, encompassing messenger RNA, non-coding RNAs, and RNA transcripts involved in gene expression and regulation.</td></tr><tr><td>PROTEIN</td><td>Functional biological macromolecules composed of amino acids, including enzymes, receptors, transcription factors, and protein complexes produced by translation of RNA.</td></tr><tr><td>CELL_LINE</td><td>A population of cells derived from a single source and maintained in vitro through continuous culture, often genetically stable and used for experimental research.</td></tr><tr><td>CELL_TYPE</td><td>A class of cells defined by shared morphological, functional, and molecular characteristics within an organism, such as immune cells, epithelial cells, or neurons.</td></tr></table>

[OCR table id=tbl-18.html; page=18]
<table><tr><td>Labels</td><td>Definition</td></tr><tr><td>PER</td><td>Person entities are limited to humans. A person may be a single individual or a group.</td></tr><tr><td>ORG</td><td>Organization entities are limited to corporations, agencies, and other groups of people defined by an established organizational structure.</td></tr><tr><td>GPE</td><td>GPE entities are geographical regions defined by political and/or social groups. A GPE entity subsumes and does not distinguish between a nation, its region, its government, or its people.</td></tr><tr><td>LOC</td><td>Location entities are limited to geographical entities such as geographical areas and land-masses, bodies of water, and geological formations.</td></tr><tr><td>FAC</td><td>Facility entities are limited to buildings and other permanent man-made structures and real estate improvements.</td></tr><tr><td>VEH</td><td>A vehicle entity is a physical device primarily designed to move an object from one location to another, by (for example) carrying, pulling, or pushing the transported object. Vehicle entities may or may not have their own power source.</td></tr><tr><td>WEA</td><td>Weapon entities are limited to physical devices primarily used as instruments for physically harming or destroying other entities.</td></tr></table>

## B-ocr-d38b34cebe1a43

B PDF page 4

tion task. Category-grouped JSON organizes entities by their label keys, which can only handle the entity-label relationship while ambiguity exists due to the lack of positional information. Occurrence-based JSON records an occurrence order index for each entity, providing a certain level of positional reference, while Offset-based JSON demands precise character-level start and end positions, whose fine-grained positional alignment poses a greater challenge for generative models.

Datasets. For in-domain evaluation, to fairly compare with pre-trained model based methods, we employ standard datasets and do not use external instruction data such as in UniversalNER (Zhou et al., 2024). For traditional flat NER, we use CoNLL2003 (Tjong Kim Sang and De Meulder, 2003) and OntoNotes5.0 (Pradhan et al., 2013) in general domain. For more challenging nested NER, we use ACE2005 \( ^{1} \) (Walker et al., 2006) in general domain and GENIA (Kim et al., 2003) in molecular biology domain. The statistics of datasets are shown in Table 2.

Baselines. For pre-trained NER models, we compare BERT-Tagger (Devlin et al., 2019), GNN-SL (Wang et al., 2023), ACE + Fine-tune (Wang et al., 2021), BERT-MRC+DSC (Li et al., 2020b), BERT-MRC (Li et al., 2020a), BINDER (Zhang et al., 2023), W2NER (Li et al., 2022), and Biaffine+CNN (Yan et al., 2023). See Appendix C for brief introductions of these methods.

We also compare GPT-NER (Wang et al., 2025a), which uses closed-source GPT-3 for generative NER. Three settings are used including zero-shot (ZS), zero-shot with entity verification (ZS w/ Ver.), and few-shot with entity verification (FS w/ Ver.).

Models. We use representative open-source models from four LLM families: LLaMA (Grattafiori et al., 2024), Qwen (Yang et al., 2025), Granite (IBM Research, 2025), and Gemma (Gemma Team, 2025). Specifically, we evaluate versions including LLaMA3.1, LLaMA3.2, Qwen2.5, Qwen3, Granite3.3, Granite4, Gemma2, and Gemma3, covering lightweight (3B~4B) and medium-sized (7B~9B) parameter scales.

Implementation Details. We fine-tuned all models using the LLaMA-Factory (Zheng et al., 2024) with LoRA (Hu et al., 2022). We compare LoRA and full fine-tuning in Appendix D, showing that LoRA achieves competitive performance with fewer parameters. We set the LoRA rank r to 256 and the

[tbl-2.html](tbl-2.html)

Table 3: Results of pre-trained models, GPT-3, and open-source LLMs on flat NER datasets. The best results are shown in bold and the second-best results are shown in underlined. Averages are highlighted in blue.

scaling factor  \( \alpha \)  to 512, with adapters inserted into all linear modules. The models were trained with a total batch size of 8 and a learning rate of 2e-5, utilizing a cosine scheduler and a warmup ratio of 0.01. The maximum input length was set to 2048, and all models were trained for two epochs.

[OCR table id=tbl-2.html; page=4]
<table><tr><td>Models</td><td>CoNLL2003</td><td>OntoNotes5.0</td><td>Average</td></tr><tr><td colspan="4">Pre-Trained NER Models</td></tr><tr><td>BERT-Tagger (Devlin et al., 2019)</td><td>91.70</td><td>89.16</td><td>90.43</td></tr><tr><td>GNN-SL (Wang et al., 2023)</td><td>93.20</td><td>91.39</td><td>92.30</td></tr><tr><td>ACE + Fine-tune (Wang et al., 2021)</td><td>93.64</td><td>91.39</td><td>92.52</td></tr><tr><td>BERT-MRC+DSC (Li et al., 2020b)</td><td>93.33</td><td>92.07</td><td>92.70</td></tr><tr><td>BERT-MRC (Li et al., 2020a)</td><td>93.04</td><td>91.11</td><td>92.08</td></tr><tr><td colspan="4">GPT-NER (Wang et al., 2025a)</td></tr><tr><td>GPT-3 (ZS)</td><td>89.97</td><td>81.73</td><td>85.85</td></tr><tr><td>GPT-3 (ZS w/ Ver.)</td><td>90.62</td><td>82.08</td><td>86.35</td></tr><tr><td>GPT-3 (FS w/ Ver.)</td><td>90.91</td><td>82.20</td><td>86.56</td></tr><tr><td colspan="4">Open-Source LLMs (Inline Bracketed)</td></tr><tr><td>LLaMA3.1-8B</td><td>93.85</td><td>91.28</td><td>92.57</td></tr><tr><td>LLaMA3.2-3B</td><td>93.54</td><td>89.19</td><td>91.37</td></tr><tr><td>Qwen2.5-7B</td><td>93.73</td><td>90.97</td><td>92.35</td></tr><tr><td>Qwen3-4B</td><td>93.37</td><td>89.30</td><td>91.34</td></tr><tr><td>Granite3.3-8B</td><td>93.76</td><td>90.31</td><td>92.04</td></tr><tr><td>Granite4-3B</td><td>93.15</td><td>89.82</td><td>91.49</td></tr><tr><td>Gemma2-9B</td><td>93.64</td><td>90.91</td><td>92.28</td></tr><tr><td>Gemma3-4B</td><td>93.68</td><td>90.09</td><td>91.89</td></tr><tr><td>Average</td><td>93.59</td><td>90.23</td><td>91.91</td></tr><tr><td colspan="4">Open-Source LLMs (Inline XML)</td></tr><tr><td>LLaMA3.1-8B</td><td>93.83</td><td>90.94</td><td>92.39</td></tr><tr><td>LLaMA3.2-3B</td><td>93.06</td><td>89.30</td><td>91.18</td></tr><tr><td>Qwen2.5-7B</td><td>93.59</td><td>90.79</td><td>92.19</td></tr><tr><td>Qwen3-4B</td><td>93.15</td><td>88.96</td><td>91.06</td></tr><tr><td>Granite3.3-8B</td><td>93.33</td><td>89.95</td><td>91.64</td></tr><tr><td>Granite4-3B</td><td>93.07</td><td>89.46</td><td>91.27</td></tr><tr><td>Gemma2-9B</td><td>93.59</td><td>90.99</td><td>92.29</td></tr><tr><td>Gemma3-4B</td><td>93.22</td><td>90.15</td><td>91.69</td></tr><tr><td>Average</td><td>93.36</td><td>90.07</td><td>91.71</td></tr><tr><td colspan="4">Open-Source LLMs (Category-grouped JSON)</td></tr><tr><td>LLaMA3.1-8B</td><td>92.56</td><td>89.84</td><td>91.20</td></tr><tr><td>LLaMA3.2-3B</td><td>92.41</td><td>87.34</td><td>89.88</td></tr><tr><td>Qwen2.5-7B</td><td>92.74</td><td>89.48</td><td>91.11</td></tr><tr><td>Qwen3-4B</td><td>92.47</td><td>87.67</td><td>90.07</td></tr><tr><td>Granite3.3-8B</td><td>92.97</td><td>88.98</td><td>90.98</td></tr><tr><td>Granite4-3B</td><td>91.78</td><td>88.44</td><td>90.11</td></tr><tr><td>Gemma2-9B</td><td>93.48</td><td>90.54</td><td>92.01</td></tr><tr><td>Gemma3-4B</td><td>92.53</td><td>89.17</td><td>90.85</td></tr><tr><td>Average</td><td>92.62</td><td>88.93</td><td>90.78</td></tr><tr><td colspan="4">Open-Source LLMs (Occurrence-based JSON)</td></tr><tr><td>LLaMA3.1-8B</td><td>93.54</td><td>90.52</td><td>92.03</td></tr><tr><td>LLaMA3.2-3B</td><td>93.58</td><td>87.64</td><td>90.61</td></tr><tr><td>Qwen2.5-7B</td><td>93.52</td><td>90.04</td><td>91.78</td></tr><tr><td>Qwen3-4B</td><td>92.91</td><td>87.98</td><td>90.45</td></tr><tr><td>Granite3.3-8B</td><td>92.94</td><td>89.20</td><td>91.07</td></tr><tr><td>Granite4-3B</td><td>92.76</td><td>88.63</td><td>90.70</td></tr><tr><td>Gemma2-9B</td><td>93.55</td><td>90.29</td><td>91.92</td></tr><tr><td>Gemma3-4B</td><td>93.17</td><td>88.49</td><td>90.83</td></tr><tr><td>Average</td><td>93.25</td><td>89.10</td><td>91.17</td></tr><tr><td colspan="4">Open-Source LLMs (Offset-based JSON)</td></tr><tr><td>LLaMA3.1-8B</td><td>63.22</td><td>53.31</td><td>58.27</td></tr><tr><td>LLaMA3.2-3B</td><td>56.13</td><td>31.20</td><td>43.67</td></tr><tr><td>Qwen2.5-7B</td><td>60.84</td><td>50.92</td><td>55.88</td></tr><tr><td>Qwen3-4B</td><td>61.18</td><td>38.34</td><td>49.76</td></tr><tr><td>Granite3.3-8B</td><td>64.79</td><td>44.08</td><td>54.44</td></tr><tr><td>Granite4-3B</td><td>61.40</td><td>38.91</td><td>50.16</td></tr><tr><td>Gemma2-9B</td><td>65.53</td><td>61.45</td><td>63.49</td></tr><tr><td>Gemma3-4B</td><td>59.85</td><td>51.35</td><td>55.60</td></tr><tr><td>Average</td><td>61.62</td><td>46.20</td><td>53.91</td></tr></table>

## B-ocr-e39215efd2e22f

B PDF page 13

[tbl-11.html](tbl-11.html)

Table 10: Task descriptions for different output formats.

### B.3 Label Definition Schema

To enhance the semantic understanding of the LLM, particularly for ambiguous or domain-specific entities, we provide explicit definitions for each label in the instructions. These definitions are derived from the official annotation guidelines of each dataset, which serve as the authoritative standard in the dataset's labeling process. For the CoNLL2003 dataset, the official annotation guidelines contain extensive explanations for the labels, which we have summarized using a large language model to provide concise, standard linguistic definitions. For the GENIA dataset, the official annotation guidelines were not available; therefore, we employed a large language model to generate standard biomedical definitions. The detailed definitions for CoNLL2003, OntoNotes5.0, GENIA, and ACE2005 are provided in Table 14, Table 15, Ta

ble 16, and Table 17, respectively.

## C Brief Introduction of Baselines

BERT-Tagger (Devlin et al., 2019) uses a BERT model and trains classification heads for tagging tokens. GNN-SL (Wang et al., 2023) augments sequence labeling by retrieving nearest neighbor examples and modeling their interactions with the input via GNNs. ACE + Fine-tune (Wang et al., 2021) utilizes a reinforcement learning controller to automatically search for the optimal concatenation of various pre-trained embeddings. For a fair comparison, we adopt its sentence-level variant, achieving SOTA performance on the CoNLL2003 dataset. BERT-MRC+DSC (Li et al., 2020b) addresses data imbalance via Dice loss, achieving SOTA performance on the OntoNotes5.0 dataset. BERT-MRC (Li et al., 2020a) formulates NER

[OCR table id=tbl-11.html; page=13]
<table><tr><td>Output Format</td><td>Task Description</td></tr><tr><td>Inline Bracketed</td><td>Your task is to identify all named entities in the input sentence and rewrite the sentence by enclosing each entity using the format [Entity Text | LABEL]. Use only the label tags defined in the Label Set below.</td></tr><tr><td>Inline XML</td><td>Your task is to identify all named entities in the input sentence and rewrite the sentence by enclosing each entity using the formatEntity Text. Use only the label tags defined in the Label Set below.</td></tr><tr><td>Category-grouped JSON</td><td>Your task is to identify all named entities in the input sentence and extract them into a JSON object grouped by label. The keys of the JSON object should be the label tags defined in the Label Set below, and the values should be lists of extracted entities. If a label has no corresponding entities, use an empty list.</td></tr><tr><td>Occurrence-based JSON</td><td>Your task is to identify all named entities in the input sentence and extract them into a JSON list. Output a JSON list where each object contains:1. “text”: the entity string.2. “label”: the label tags defined in the Label Set below.3. “occurrence_index”: a 1-based integer indicating the order of appearance of this text in the sentence (e.g., 1 for the first appearance, 2 for the second). If no entities are found, return an empty list.</td></tr><tr><td>Offset-based JSON</td><td>Your task is to identify all named entities in the input sentence and extract them with precise character offsets. Output a JSON list where each object contains:1. “text”: the entity string.2. “label”: the label tags defined in the Label Set below.3. “start”: the 0-based index of the entity’s first character.4. “end”: the 0-based index of the first character after the entity (exclusive).</td></tr></table>

## B-ocr-e55614ac21454d

B PDF page 10

deep bidirectional transformers for language understanding. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pages 4171–4186, Minneapolis, Minnesota. Association for Computational Linguistics.

Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, Bin Gu, Mengfei Yang, and Ge Li. 2024. Generalization or memorization: Data contamination and trustworthy evaluation for large language models. In Findings of the Association for Computational Linguistics: ACL 2024, pages 12039–12050, Bangkok, Thailand. Association for Computational Linguistics.

Dheeru Dua, Yizhong Wang, Pradeep Dasigi, Gabriel Stanovsky, Sameer Singh, and Matt Gardner. 2019. DROP: A reading comprehension benchmark requiring discrete reasoning over paragraphs. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pages 2368–2378, Minneapolis, Minnesota. Association for Computational Linguistics.

Leo Gao, Jonathan Tow, Baber Abbasi, Stella Biderman, Sid Black, Anthony DiPofi, Charles Foster, Laurence Golding, Jeffrey Hsu, Alain Le Noac'h, Haonan Li, Kyle McDonell, Niklas Muennighoff, Chris Ociepa, Jason Phang, Laria Reynolds, Hailey Schoelkopf, Aviya Skowron, Lintang Sutawika, Eric Tang, Anish Thite, Ben Wang, Kevin Wang, and Andy Zou. 2024. The language model evaluation harness.

Gemma Team. 2025. Gemma 3 technical report. arXiv preprint arXiv:2503.19786.

Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. 2024. The llama 3 herd of models. arXiv preprint arXiv:2407.21783.

Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. 2021. Measuring massive multitask language understanding. In International Conference on Learning Representations.

Edward J Hu, yelong shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. 2022. LoRA: Low-rank adaptation of large language models. In International Conference on Learning Representations.

Hui Huang, Yanping Chen, Ruizhang Huang, Chuan Lin, and Yongbin Qin. 2026. A reasoning paradigm for named entity recognition. Proceedings of the AAAI Conference on Artificial Intelligence, 40(37):31140–31148.

IBM Research. 2025. Granite 4.0 language models. https://github.com/ibm-granite/granite-4.0-language-models. Accessed: 2025-10-01.

Hongjin Kim, Jai-Eun Kim, and Harksoo Kim. 2024. Exploring nested named entity recognition with large language models: Methods, challenges, and insights. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 8653–8670, Miami, Florida, USA. Association for Computational Linguistics.

J.-D. Kim, T. Ohta, Y. Tateisi, and J. Tsujii. 2003. Genia corpus—a semantically annotated corpus for biotextmining. Bioinformatics, 19:i180–i182.

Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov, and Luke Zettlemoyer. 2020. BART: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 7871–7880, Online. Association for Computational Linguistics.

Jingye Li, Hao Fei, Jiang Liu, Shengqiong Wu, Meishan Zhang, Chong Teng, Donghong Ji, and Fei Li. 2022. Unified named entity recognition as word-word relation classification. Proceedings of the AAAI Conference on Artificial Intelligence, 36(10):10965–10973.

Xiaoya Li, Jingrong Feng, Yuxian Meng, Qinghong Han, Fei Wu, and Jiwei Li. 2020a. A unified MRC framework for named entity recognition. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 5849–5859, Online. Association for Computational Linguistics.

Xiaoya Li, Xiaofei Sun, Yuxian Meng, Junjun Liang, Fei Wu, and Jiwei Li. 2020b. Dice loss for data-imbalanced NLP tasks. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 465–476, Online. Association for Computational Linguistics.

Stephanie Lin, Jacob Hilton, and Owain Evans. 2022. TruthfulQA: Measuring how models mimic human falsehoods. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 3214–3252, Dublin, Ireland. Association for Computational Linguistics.

Yaojie Lu, Qing Liu, Dai Dai, Xinyan Xiao, Hongyu Lin, Xianpei Han, Le Sun, and Hua Wu. 2022. Unified structure generation for universal information extraction. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 5755–5772, Dublin, Ireland. Association for Computational Linguistics.

Tengxiao Lv, Ling Luo, Juntao Li, Yanhua Wang, Yuchen Pan, Chao Liu, Yanan Wang, Yan Jiang, Huiyi Lv, Yuanyuan Sun, et al. 2025. A unified biomedical named entity recognition framework with large language models. arXiv preprint arXiv:2510.08902.

## B-ocr-f312b0cabf7e2f

B PDF page 19

[tbl-19.html](tbl-19.html)

Table 18: Complete Precision, Recall, and F1 results of pre-trained models, GPT-3, and open-source LLMs on flat and nested NER datasets.

[OCR table id=tbl-19.html; page=19]
<table><tr><td rowspan="2">Models</td><td colspan="3">CoNLL2003</td><td colspan="3">OntoNotes5.0</td><td rowspan="2">\( Avg_{F1}^{The} \)</td><td colspan="3">ACE2005</td><td colspan="3">GENIA</td><td rowspan="2">\( Avg_{F1}^{Named} \)</td></tr><tr><td>P</td><td>R</td><td>F1</td><td>P</td><td>R</td><td>F1</td><td>P</td><td>R</td><td>F1</td><td>P</td><td>R</td><td>F1</td></tr><tr><td colspan="15">Pre-Trained NER Models</td></tr><tr><td>BERT-Tagger</td><td>91.20</td><td>92.30</td><td>91.70</td><td>90.01</td><td>88.35</td><td>89.16</td><td>90.43</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>GNN-SL</td><td>93.02</td><td>93.40</td><td>93.20</td><td>91.48</td><td>91.29</td><td>91.39</td><td>92.30</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>ACE + Fine-tune</td><td>93.07</td><td>94.21</td><td>93.64</td><td>91.48</td><td>91.29</td><td>91.39</td><td>92.52</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>BERT-MRC+DSC</td><td>93.41</td><td>93.25</td><td>93.33</td><td>91.59</td><td>92.56</td><td>92.07</td><td>92.70</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>BERT-MRC</td><td>92.33</td><td>94.61</td><td>93.04</td><td>92.98</td><td>89.95</td><td>91.11</td><td>92.08</td><td>87.16</td><td>86.59</td><td>86.88</td><td>85.18</td><td>81.12</td><td>83.75</td><td>85.32</td></tr><tr><td>BINDER</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>89.60</td><td>90.50</td><td>90.00</td><td>83.40</td><td>78.30</td><td>80.80</td><td>85.40</td></tr><tr><td>W2NER</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>85.03</td><td>88.62</td><td>86.79</td><td>81.58</td><td>79.11</td><td>80.32</td><td>83.56</td></tr><tr><td>Biaffine+CNN</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>86.78</td><td>87.72</td><td>87.25</td><td>81.52</td><td>79.17</td><td>80.33</td><td>83.79</td></tr><tr><td colspan="15">GPT-NER</td></tr><tr><td>GPT-3 (ZS)</td><td>88.54</td><td>91.40</td><td>89.97</td><td>79.17</td><td>84.29</td><td>81.73</td><td>85.85</td><td>71.72</td><td>74.20</td><td>72.96</td><td>61.38</td><td>66.74</td><td>64.06</td><td>68.51</td></tr><tr><td>GPT-3 (ZS w/ Ver.)</td><td>89.47</td><td>91.77</td><td>90.62</td><td>79.64</td><td>84.52</td><td>82.08</td><td>86.35</td><td>72.63</td><td>75.39</td><td>73.46</td><td>61.77</td><td>66.81</td><td>64.29</td><td>68.88</td></tr><tr><td>GPT-3 (FS w/ Ver.)</td><td>89.76</td><td>92.06</td><td>90.91</td><td>79.89</td><td>84.51</td><td>82.20</td><td>86.56</td><td>72.77</td><td>75.51</td><td>73.59</td><td>61.89</td><td>66.95</td><td>64.42</td><td>69.01</td></tr><tr><td colspan="15">Large Language Models (Inline Bracketed Format)</td></tr><tr><td>LLaMA3.1-8B</td><td>93.50</td><td>94.21</td><td>93.85</td><td>91.23</td><td>91.32</td><td>91.28</td><td>92.57</td><td>87.16</td><td>87.85</td><td>87.51</td><td>81.93</td><td>76.62</td><td>79.18</td><td>83.35</td></tr><tr><td>LLaMA3.2-3B</td><td>93.17</td><td>93.91</td><td>93.54</td><td>89.18</td><td>89.21</td><td>89.19</td><td>91.37</td><td>85.18</td><td>86.47</td><td>85.82</td><td>81.77</td><td>76.69</td><td>79.15</td><td>82.49</td></tr><tr><td>Qwen2.5-7B</td><td>93.51</td><td>93.94</td><td>93.73</td><td>90.98</td><td>90.97</td><td>90.97</td><td>92.35</td><td>86.47</td><td>86.93</td><td>86.70</td><td>81.76</td><td>75.82</td><td>78.67</td><td>82.69</td></tr><tr><td>Qwen3-4B</td><td>93.05</td><td>93.68</td><td>93.37</td><td>89.25</td><td>89.35</td><td>89.30</td><td>91.34</td><td>85.56</td><td>87.43</td><td>86.48</td><td>81.94</td><td>76.56</td><td>79.16</td><td>82.82</td></tr><tr><td>Granite3.3-8B</td><td>93.38</td><td>94.14</td><td>93.76</td><td>90.37</td><td>90.26</td><td>90.31</td><td>92.04</td><td>86.08</td><td>87.56</td><td>86.81</td><td>81.24</td><td>76.64</td><td>78.87</td><td>82.84</td></tr><tr><td>Granite4-3B</td><td>92.75</td><td>93.56</td><td>93.15</td><td>89.59</td><td>90.05</td><td>89.82</td><td>91.49</td><td>85.93</td><td>87.66</td><td>86.78</td><td>81.09</td><td>75.91</td><td>78.42</td><td>82.60</td></tr><tr><td>Gemma2-9B</td><td>93.24</td><td>94.03</td><td>93.64</td><td>90.72</td><td>91.11</td><td>90.91</td><td>92.28</td><td>86.55</td><td>88.35</td><td>87.44</td><td>82.41</td><td>77.22</td><td>79.73</td><td>83.59</td></tr><tr><td>Gemma3-4B</td><td>93.32</td><td>94.03</td><td>93.68</td><td>90.01</td><td>90.17</td><td>90.09</td><td>91.89</td><td>85.40</td><td>87.03</td><td>86.20</td><td>81.75</td><td>75.76</td><td>78.64</td><td>82.42</td></tr><tr><td>Average</td><td>93.24</td><td>93.94</td><td>93.59</td><td>90.17</td><td>90.30</td><td>90.23</td><td>91.91</td><td>86.04</td><td>87.41</td><td>86.72</td><td>81.74</td><td>76.40</td><td>78.98</td><td>82.85</td></tr><tr><td colspan="15">Large Language Models (Inline XML Format)</td></tr><tr><td>LLaMA3.1-8B</td><td>93.57</td><td>94.09</td><td>93.83</td><td>90.84</td><td>91.05</td><td>90.94</td><td>92.39</td><td>85.30</td><td>86.98</td><td>86.13</td><td>80.78</td><td>76.18</td><td>78.41</td><td>82.27</td></tr><tr><td>LLaMA3.2-3B</td><td>92.80</td><td>93.33</td><td>93.06</td><td>89.14</td><td>89.46</td><td>89.30</td><td>91.18</td><td>85.31</td><td>87.24</td><td>86.26</td><td>80.21</td><td>76.32</td><td>78.22</td><td>82.24</td></tr><tr><td>Qwen2.5-7B</td><td>93.31</td><td>93.87</td><td>93.59</td><td>90.88</td><td>90.71</td><td>90.79</td><td>92.19</td><td>85.50</td><td>86.45</td><td>85.97</td><td>81.31</td><td>77.34</td><td>79.27</td><td>82.62</td></tr><tr><td>Qwen3-4B</td><td>92.95</td><td>93.36</td><td>93.15</td><td>88.99</td><td>88.93</td><td>88.96</td><td>91.06</td><td>84.89</td><td>86.45</td><td>85.66</td><td>81.39</td><td>77.88</td><td>79.60</td><td>82.63</td></tr><tr><td>Granite3.3-8B</td><td>92.91</td><td>93.75</td><td>93.33</td><td>89.87</td><td>90.04</td><td>89.95</td><td>91.64</td><td>86.87</td><td>87.67</td><td>87.27</td><td>81.42</td><td>76.89</td><td>79.09</td><td>83.18</td></tr><tr><td>Granite4-3B</td><td>92.75</td><td>93.38</td><td>93.07</td><td>89.33</td><td>89.58</td><td>89.46</td><td>91.27</td><td>85.50</td><td>88.23</td><td>86.84</td><td>81.07</td><td>76.30</td><td>78.61</td><td>82.73</td></tr><tr><td>Gemma2-9B</td><td>93.14</td><td>94.03</td><td>93.59</td><td>90.98</td><td>91.01</td><td>90.99</td><td>92.29</td><td>87.24</td><td>88.82</td><td>88.02</td><td>81.93</td><td>76.87</td><td>79.32</td><td>83.67</td></tr><tr><td>Gemma3-4B</td><td>92.73</td><td>93.71</td><td>93.22</td><td>90.08</td><td>90.23</td><td>90.15</td><td>91.69</td><td>85.41</td><td>85.83</td><td>85.62</td><td>81.22</td><td>75.87</td><td>78.46</td><td>82.04</td></tr><tr><td>Average</td><td>93.02</td><td>93.69</td><td>93.36</td><td>90.01</td><td>90.13</td><td>90.07</td><td>91.71</td><td>85.75</td><td>87.21</td><td>86.47</td><td>81.17</td><td>76.71</td><td>78.87</td><td>82.67</td></tr><tr><td colspan="15">Large Language Models (Category-grouped JSON Format)</td></tr><tr><td>LLaMA3.1-8B</td><td>92.08</td><td>93.04</td><td>92.56</td><td>89.87</td><td>89.82</td><td>89.84</td><td>91.20</td><td>85.69</td><td>86.59</td><td>86.13</td><td>79.77</td><td>76.87</td><td>78.29</td><td>82.21</td></tr><tr><td>LLaMA3.2-3B</td><td>92.18</td><td>92.63</td><td>92.41</td><td>87.12</td><td>87.56</td><td>87.34</td><td>89.88</td><td>83.39</td><td>83.99</td><td>83.69</td><td>79.36</td><td>76.68</td><td>77.99</td><td>80.84</td></tr><tr><td>Qwen2.5-7B</td><td>92.44</td><td>93.04</td><td>92.74</td><td>89.49</td><td>89.46</td><td>89.48</td><td>91.11</td><td>84.79</td><td>84.88</td><td>84.84</td><td>79.37</td><td>76.97</td><td>78.15</td><td>81.50</td></tr><tr><td>Qwen3-4B</td><td>92.28</td><td>92.67</td><td>92.47</td><td>87.18</td><td>88.18</td><td>87.67</td><td>90.07</td><td>83.74</td><td>84.98</td><td>84.35</td><td>79.86</td><td>77.14</td><td>78.48</td><td>81.42</td></tr><tr><td>Granite3.3-8B</td><td>92.73</td><td>93.22</td><td>92.97</td><td>88.74</td><td>89.22</td><td>88.98</td><td>90.98</td><td>85.61</td><td>86.85</td><td>86.23</td><td>80.14</td><td>76.87</td><td>78.47</td><td>82.35</td></tr><tr><td>Granite4-3B</td><td>91.48</td><td>92.07</td><td>91.78</td><td>88.51</td><td>88.37</td><td>88.44</td><td>90.11</td><td>84.02</td><td>85.54</td><td>84.77</td><td>79.79</td><td>77.03</td><td>78.38</td><td>81.58</td></tr><tr><td>Gemma2-9B</td><td>93.18</td><td>93.79</td><td>93.48</td><td>90.55</td><td>90.53</td><td>90.54</td><td>92.01</td><td>86.40</td><td>86.88</td><td>86.64</td><td>80.09</td><td>77.81</td><td>78.93</td><td>82.79</td></tr><tr><td>Gemma3-4B</td><td>92.36</td><td>92.71</td><td>92.53</td><td>89.19</td><td>89.16</td><td>89.17</td><td>90.85</td><td>84.54</td><td>84.48</td><td>84.51</td><td>78.83</td><td>75.60</td><td>77.18</td><td>80.85</td></tr><tr><td>Average</td><td>92.34</td><td>92.90</td><td>92.62</td><td>88.83</td><td>89.04</td><td>88.93</td><td>90.78</td><td>84.77</td><td>85.52</td><td>85.14</td><td>79.65</td><td>76.87</td><td>78.23</td><td>81.69</td></tr><tr><td colspan="15">Large Language Models (Occurrence-based JSON Format)</td></tr><tr><td>LLaMA3.1-8B</td><td>92.89</td><td>94.19</td><td>93.54</td><td>90.27</td><td>90.76</td><td>90.52</td><td>92.03</td><td>82.78</td><td>84.06</td><td>83.41</td><td>80.07</td><td>77.30</td><td>78.66</td><td>81.04</td></tr><tr><td>LLaMA3.2-3B</td><td>92.96</td><td>94.21</td><td>93.58</td><td>87.23</td><td>88.05</td><td>87.64</td><td>90.61</td><td>80.27</td><td>81.59</td><td>80.93</td><td>78.68</td><td>76.19</td><td>77.41</td><td>79.17</td></tr><tr><td>Qwen2.5-7B</td><td>93.10</td><td>93.94</td><td>93.52</td><td>89.77</td><td>90.32</td><td>90.04</td><td>91.78</td><td>81.46</td><td>81.92</td><td>81.69</td><td>78.60</td><td>76.58</td><td>77.58</td><td>79.64</td></tr><tr><td>Qwen3-4B</td><td>92.26</td><td>93.56</td><td>92.91</td><td>87.51</td><td>88.45</td><td>87.98</td><td>90.45</td><td>80.85</td><td>82.31</td><td>81.58</td><td>79.32</td><td>77.63</td><td>78.47</td><td>80.03</td></tr><tr><td>Granite3.3-8B</td><td>92.30</td><td>93.59</td><td>92.94</td><td>88.84</td><td>89.57</td><td>89.20</td><td>91.07</td><td>82.08</td><td>83.99</td><td>83.02</td><td>79.67</td><td>76.93</td><td>78.27</td><td>80.65</td></tr><tr><td>Granite4-3B</td><td>92.29</td><td>93.24</td><td>92.76</td><td>88.31</td><td>88.94</td><td>88.63</td><td>90.70</td><td>80.84</td><td>82.94</td><td>81.88</td><td>78.55</td><td>75.99</td><td>77.25</td><td>79.57</td></tr><tr><td>Gemma2-9B</td><td>92.99</td><td>94.12</td><td>93.55</td><td>90.08</td><td>90.50</td><td>90.29</td><td>91.92</td><td>83.49</td><td>85.11</td><td>84.29</td><td>80.30</td><td>77.96</td><td>79.12</td><td>81.71</td></tr><tr><td>Gemma3-4B</td><td>92.74</td><td>93.61</td><td>93.17</td><td>88.60</td><td>88.37</td><td>88.49</td><td>90.83</td><td>81.43</td><td>81.72</td><td>81.58</td><td>79.25</td><td>73.06</td><td>76.03</td><td>78.81</td></tr><tr><td>Average</td><td>92.69</td><td>93.81</td><td>93.25</td><td>88.83</td><td>89.37</td><td>89.10</td><td>91.17</td><td>81.65</td><td>82.95</td><td>82.30</td><td>79.30</td><td>76.45</td><td>77.85</td><td>80.07</td></tr><tr><td colspan="15">Large Language Models (Offset-based JSON Format)</td></tr><tr><td>LLaMA3.1-8B</td><td>62.91</td><td>63.53</td><td>63.22</td><td>52.99</td><td>53.63</td><td>53.31</td><td>58.27</td><td>35.53</td><td>36.17</td><td>35.85</td><td>35.16</td><td>34.09</td><td>34.62</td><td>35.24</td></tr><tr><td>LLaMA3.2-3B</td><td>56.01</td><td>56.25</td><td>56.13</td><td>31.06</td><td>31.34</td><td>31.20</td><td>43.67</td><td>27.03</td><td>27.59</td><td>27.31</td><td>26.17</td><td>25.43</td><td>25.79</td><td>26.55</td></tr><tr><td>Qwen2.5-7B</td><td>60.52</td><td>61.17</td><td>60.84</td><td>50.67</td><td>51.17</td><td>50.92</td><td>55.88</td><td>32.54</td><td>32.64</td><td>32.59</td><td>32.52</td><td>31.53</td><td>32.02</td><td>32.31</td></tr><tr><td>Qwen3-4B</td><td>60.86</td><td>61.51</td><td>61.18</td><td>38.03</td><td>38.66</td><td>38.34</td><td>49.76</td><td>35.06</td><td>35.78</td><td>35.41</td><td>37.51</td><td>36.14</td><td>36.81</td><td>36.11</td></tr><tr><td>Granite3.3-8B</td><td>64.49</td><td>65.09</td><td>64.79</td><td>43.78</td><td>44.38</td><td>44.08</td><td>54.44</td><td>36.48</td><td>37.33</td><td>36.90</td><td>40.06</td><td>39.03</td><td>39.54</td><td>38.22</td></tr><tr><td>Granite4-3B</td><td>60.99</td><td>61.81</td><td>61.40</td><td>38.71</td><td>39.10</td><td>38.91</td><td>50.16</td><td>33.00</td><td>33.60</td><td>33.30</td><td>37.55</td><td>36.08</td><td>36.80</td><td>35.05</td></tr><tr><td>Gemma2-9B</td><td>65.21</td><td>65.86</td><td>65.53</td><td>61.15</td><td>61.75</td><td>61.45</td><td>63.49</td><td>40.45</td><td>41.16</td><td>40.80</td><td>41.75</td><td>40.55</td><td>41.15</td><td>40.98</td></tr><tr><td>Gemma3-4B</td><td>59.67</td><td>60.02</td><td>59.85</td><td>51.50</td><td>51.19</td><td>51.35</td><td>55.60</td><td>31.67</td><td>31.52</td><td>31.60</td><td>33.56</td><td>30.57</td><td>32.00</td><td>31.80</td></tr><tr><td>Average</td><td>61.33</td><td>61.91</td><td>61.62</td><td>45.99</td><td>46.40</td><td>46.20</td><td>53.91</td><td>33.97</td><td>34.47</td><td>34.22</td><td>35.53</td><td>34.18</td><td>34.84</td><td>34.53</td></tr></table>

## B-ocr-f65211fc6798d7

B PDF page 17

[tbl-15.html](tbl-15.html)

Table 14: Label definitions for CoNLL2003 dataset.

[tbl-16.html](tbl-16.html)

Table 15: Label definitions for OntoNotes5.0 dataset.

[OCR table id=tbl-15.html; page=17]
<table><tr><td>Labels</td><td>Definition</td></tr><tr><td>ORG</td><td>A collective entity such as a company, institution, brand, political or governmental body, publication, or any organized group of people acting as a unit.</td></tr><tr><td>PER</td><td>A named individual, including humans, animals, fictional characters, and their aliases.</td></tr><tr><td>LOC</td><td>A geographical or spatial entity, including natural features, built structures, regions, public or commercial places, assorted buildings, and abstract or metaphorical places.</td></tr><tr><td>MISC</td><td>Named entities that are not persons, organizations, or locations, including derived adjectives, religions, ideologies, nationalities, languages, events, programs, wars, titles of works, slogans, eras, and types of objects.</td></tr></table>

[OCR table id=tbl-16.html; page=17]
<table><tr><td>Labels</td><td>Definition</td></tr><tr><td>PERSON</td><td>People, including fictional.</td></tr><tr><td>NORP</td><td>Nationalities or religious or political groups.</td></tr><tr><td>FAC</td><td>Buildings, airports, highways, bridges, etc..</td></tr><tr><td>ORG</td><td>Companies, agencies, institutions, etc..</td></tr><tr><td>GPE</td><td>Countries, cities, states.</td></tr><tr><td>LOC</td><td>Non-GPE locations, mountain ranges, bodies of water.</td></tr><tr><td>PRODUCT</td><td>Vehicles, weapons, foods, etc. (Not services).</td></tr><tr><td>EVENT</td><td>Named hurricanes, battles, wars, sports events, etc..</td></tr><tr><td>WORK_OF_ART</td><td>Titles of books, songs, etc..</td></tr><tr><td>LAW</td><td>Named documents made into laws.</td></tr><tr><td>LANGUAGE</td><td>Any named language.</td></tr><tr><td>DATE</td><td>Absolute or relative dates or periods.</td></tr><tr><td>TIME</td><td>Times smaller than a day.</td></tr><tr><td>PERCENT</td><td>Percentage (including “%”).</td></tr><tr><td>MONEY</td><td>Monetary values, including unit.</td></tr><tr><td>QUANTITY</td><td>Measurements, as of weight or distance.</td></tr><tr><td>ORDINAL</td><td>“first”, “second”.</td></tr><tr><td>CARDINAL</td><td>Numerals that do not fall under another type.</td></tr></table>
