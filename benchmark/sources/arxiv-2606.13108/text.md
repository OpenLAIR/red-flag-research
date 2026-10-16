# PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks

## B-01bed14a284907

https://arxiv.org/html/2606.13108v1#chars-45188-48745

## Appendix A Language Support

Table [10](#A1.T10 "Table 10 ‣ Appendix A Language Support ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks") compares language coverage across PP-OCR versions. PP-OCRv3/v4 support only Simplified Chinese and English; PP-OCRv5 adds Traditional Chinese and Japanese; PP-OCRv6 medium/small further incorporate 46 Latin-script languages by adding approximately 200 diacritical characters to the dictionary. The tiny model omits Japanese to avoid the ∼\sim4,000 Kanji/Kana entries that would disproportionately enlarge its 1.1M-parameter output layer.

|  |  |  |
| --- | --- | --- |
| Model | # Lang | Supported Languages |
| PP-OCRv3\_mobile\_rec | 2 | Simplified Chinese, English |
| PP-OCRv4\_mobile\_rec | 2 | Simplified Chinese, English |
| PP-OCRv4\_server\_rec | 2 | Simplified Chinese, English |
| PP-OCRv5\_server\_rec | 4 | Simplified Chinese, Traditional Chinese, English, Japanese |
| PP-OCRv5\_mobile\_rec | 4 | Simplified Chinese, Traditional Chinese, English, Japanese |
| PP-OCRv6\_medium\_rec | 50 | Simplified Chinese, Traditional Chinese, English, Japanese, French, German, Italian, Spanish, Portuguese, Dutch, Polish, Romanian, Czech, Swedish, Norwegian, Danish, Finnish, Hungarian, Turkish, Vietnamese, Indonesian, Malay, Azerbaijani, Afrikaans, Bosnian, Croatian, Welsh, Estonian, Irish, Icelandic, Kurdish, Lithuanian, Latvian, Maltese, Maori, Occitan, Slovak, Slovenian, Albanian, Swahili, Tagalog, Uzbek, Latin, Serbian (Latin), Catalan, Basque, Galician, Luxembourgish, Romansh, Quechua |
| PP-OCRv6\_small\_rec | 50 | Simplified Chinese, Traditional Chinese, English, Japanese, French, German, Italian, Spanish, Portuguese, Dutch, Polish, Romanian, Czech, Swedish, Norwegian, Danish, Finnish, Hungarian, Turkish, Vietnamese, Indonesian, Malay, Azerbaijani, Afrikaans, Bosnian, Croatian, Welsh, Estonian, Irish, Icelandic, Kurdish, Lithuanian, Latvian, Maltese, Maori, Occitan, Slovak, Slovenian, Albanian, Swahili, Tagalog, Uzbek, Latin, Serbian (Latin), Catalan, Basque, Galician, Luxembourgish, Romansh, Quechua |
| PP-OCRv6\_tiny\_rec | 49 | Simplified Chinese, Traditional Chinese, English, French, German, Italian, Spanish, Portuguese, Dutch, Polish, Romanian, Czech, Swedish, Norwegian, Danish, Finnish, Hungarian, Turkish, Vietnamese, Indonesian, Malay, Azerbaijani, Afrikaans, Bosnian, Croatian, Welsh, Estonian, Irish, Icelandic, Kurdish, Lithuanian, Latvian, Maltese, Maori, Occitan, Slovak, Slovenian, Albanian, Swahili, Tagalog, Uzbek, Latin, Serbian (Latin), Catalan, Basque, Galician, Luxembourgish, Romansh, Quechua |

To validate the multilingual capability, we evaluate PP-OCRv6 on dedicated English and Latin-script benchmarks (Table [11](#A1.T11 "Table 11 ‣ Appendix A Language Support ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks")). PP-OCRv6\_medium achieves 88.4% on the English benchmark and 88.0% on the Latin benchmark, outperforming both PP-OCRv5’s language-specific models (en\_PP-OCRv5\_mobile: 86.0%, latin\_PP-OCRv5\_mobile: 81.4%) and the PP-OCRv5 main models (server: 79.5%, mobile: 78.3% on English) while using a single unified model rather than separate per-language models.

|  |  |  |
| --- | --- | --- |
| Model | English (%) | Latin (%) |
| PP-OCRv5\_server | 79.5 | – |
| PP-OCRv5\_mobile | 78.3 | – |
| en\_PP-OCRv5\_mobile | 86.0 | – |
| latin\_PP-OCRv5\_mobile | 77.8 | 81.4 |
| PP-OCRv6\_medium | 88.4 | 88.0 |
| PP-OCRv6\_small | 86.3 | 84.0 |
| PP-OCRv6\_tiny | 77.3 | 63.8 |

## B-18a7463183656d

https://arxiv.org/html/2606.13108v1#chars-1663-6463

## 1 Introduction

The field of computer vision is increasingly dominated by large-scale models, particularly Vision-Language Models (VLMs), which have demonstrated impressive generalist capabilities across a wide range of tasks [[1](#bib.bib2), [2](#bib.bib3)]. This trend of scaling model size has naturally extended to OCR, with modern VLM-based approaches promising an end-to-end solution for extracting text from complex, real-world images. While the performance of these large models is academically remarkable, the prevailing focus on scale often encounters significant practical limitations when deployed in real-world OCR scenarios, which demand not only high recognition accuracy but also precision, reliability, and efficiency.

A primary challenge arises from the ”generalist’s dilemma.” Unified VLM architectures, although designed for diverse tasks, often lack the specialized capabilities needed for high-precision OCR. This manifests in three critical limitations: (1) Imprecise Localization: These models often fail to produce the tight, accurate bounding boxes essential for document analysis. (2) Hallucination: In complex layouts, models can confidently generate plausible yet incorrect text, presenting a critical vulnerability for data-sensitive applications. (3) Computational Inefficiency: Massive parameter counts render these models impractical for deployment in resource-constrained environments or for services demanding high-throughput, low-latency processing.

These challenges naturally steer the focus back towards lightweight, specialized OCR systems. PaddleOCR [[3](#bib.bib11)] has established a strong track record in this direction, evolving through PP-OCRv2 [[4](#bib.bib10)], PP-OCRv3 [[5](#bib.bib12)], PP-OCRv4, and PP-OCRv5 [[6](#bib.bib13)]. The PP-OCR series has explored two complementary directions for improving accuracy. On the architecture side, PP-OCRv3 introduced SVTR-LCNet and LK-PAN, while PP-OCRv4 adopted PPHGNetV2 and LCNetV3 as server and mobile backbones respectively. On the data side, PP-OCRv5 inherited the PP-OCRv4 architecture and focused on systematic data curation along three dimensions: difficulty, accuracy, and diversity. PP-OCRv5 demonstrated that with sufficient high-quality data, the performance ceiling of a 5M-parameter model is far higher than commonly assumed.

In this work, we present PP-OCRv6, which combines both directions. While inheriting PP-OCRv5’s proven data curation methodology, PP-OCRv6 introduces a fundamentally redesigned model architecture. We observe that under the same data regime, the existing backbone designs (HGNetV2 for server, LCNetV3 for mobile) have reached their structural capacity. Specifically, the MobileNet-style DW→\toSE→\toPW block in LCNetV3 does not exploit modern lightweight design principles such as the MetaFormer paradigm [[7](#bib.bib6), [8](#bib.bib7)]; the dense 9×99\times 9 convolutions in LKPAN can be replaced by efficient reparameterizable alternatives with equivalent receptive fields; and the dual-architecture approach (separate backbone families for server and mobile) increases engineering complexity unnecessarily.

Our main contributions are summarized as follows:

Unified and Scalable Model Family: We deliver a comprehensive, three-tier OCR model family spanning 1.5M to 34.5M parameters. The medium-tier model achieves an 86.2% detection H-mean and 83.2% recognition accuracy, serving as a highly efficient, production-ready infrastructure for both industrial deployment and large-scale data pipelines.

Tailored Lightweight Architectural Innovations: We introduce a suite of lightweight architectural components custom-designed for OCR tasks. Specifically, we propose: (i) LCNetV4, a MetaFormer-style lightweight backbone integrated with structural reparameterization; (ii) RepLKFPN(Reparameterizable Large-Kernel Feature Pyramid Network), a detection neck leveraging dilated reparameterizable depthwise convolutions for large-scale receptive fields; and (iii) EncoderWithLightSVTR, a recognition neck powered by local-global attention and additive skip connections.

Extensive Multi-Language and Scenario Generalization: We scale the unified model to support 50 languages and a wide range of challenging industrial scenes (e.g., digital displays, dot-matrix characters, and tire prints). This significantly enhances OCR performance in specialized scenarios that are traditionally underserved by general-purpose visual-language models.

These results provide compelling evidence that lightweight, specialized OCR systems—when equipped with modern architecture designs and high-quality training data—offer a practical and effective alternative for production OCR deployment in the large-model era.

![Refer to caption](2606.13108v1/v6_images_v2/01system.jpg)

## B-1aa9eb2c005815

https://arxiv.org/html/2606.13108v1#chars-28752-28776

### 3.2 Text Detection

## B-27e98ccabcd47a

https://arxiv.org/html/2606.13108v1#chars-27476-27494

## 3 Experiments

## B-33c4ae76756baa

https://arxiv.org/html/2606.13108v1#chars-52696-54517

### C.2 Text Detection

To verify the effectiveness of each proposed strategy, we first conduct ablation experiments on one-fifth of the full detection training data for rapid iteration, starting from the PP-OCRv5\_mobile\_det baseline. After validating the architecture and loss components under this reduced-data setting, we train the final configuration with the full training data. Results are shown in Table [13](#A3.T13 "Table 13 ‣ C.2 Text Detection ‣ Appendix C Ablation Studies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks").

|  |  |  |  |
| --- | --- | --- | --- |
| Configuration | Params | Hmean (%) | Δ\Delta |
| Ablation with 1/5 training data | | | |
| Baseline (PP-OCRv5\_mobile\_det) | 1.19M | 77.84 | – |
| + LCNetV4 Backbone | 2.53M | 79.37 | +1.53 |
| + RepLKFPN | 2.48M | 79.75 | +0.38 |
| + Auxiliary Deep Supervision | – | 80.28 | +0.53 |
| + Focal Loss | – | 81.43 | +1.15 |
| + Full Data Training | – | 84.12 | +2.69 |

As shown in Table [13](#A3.T13 "Table 13 ‣ C.2 Text Detection ‣ Appendix C Ablation Studies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks"), upgrading the backbone from LCNetV3 to LCNetV4 brings a significant improvement of 1.53% Hmean, indicating improved feature extraction capability of the new backbone. Replacing RSEFPN with RepLKFPN further improves Hmean by 0.38% while slightly reducing model parameters from 2.53M to 2.48M, demonstrating the efficiency of the depthwise-separable large-kernel design. Auxiliary deep supervision and Focal Loss contribute complementary gains of 0.53% and 1.15%, respectively. With the full training data, the final model reaches 84.12% Hmean, improving over the reduced-data configuration by 2.69% and over the PP-OCRv5\_mobile\_det baseline by 6.28%.

## B-3964ee999b0431

https://arxiv.org/html/2606.13108v1#chars-28117-28752

##### Data.

PP-OCRv6 inherits the data-centric methodology from PP-OCRv5 [[6](#bib.bib13)], training on the curated large-scale dataset constructed through principled difficulty filtering (confidence 0.95–0.97 sweet spot), accuracy verification, and diversity sampling (1000 K-means clusters). To support the expanded scenario coverage, we further augment the training data with both synthetic generation and real-world collection targeting industrial scenes such as digital displays, dot-matrix characters, tire parameters, and power adapter text. This shared data foundation enables fair ablation of the architecture improvements.

## B-3c5ee77723b9a3

https://arxiv.org/html/2606.13108v1#chars-58427-59611

## Appendix E Hallucination Visualization Comparison with VLMs

Figure [8](#A5.F8 "Figure 8 ‣ Appendix E Hallucination Visualization Comparison with VLMs ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks") presents qualitative examples comparing PP-OCRv6\_medium with several VLMs on our hallucination evaluation set. The key observation is that VLMs tend to “correct” what they perceive as spelling or grammatical errors in the source image, producing text that is linguistically plausible but factually inconsistent with the visual input. In contrast, PP-OCRv6\_medium faithfully reproduces the exact text content—including deliberate misspellings, non-standard character usage, and repeated characters—without injecting linguistic priors.

This behavior reflects a fundamental architectural difference: PP-OCRv6’s CTC+NRTR decoding is grounded in frame-level visual features without auto-regressive language modeling, producing outputs strictly conditioned on the input image. VLMs, by contrast, rely on strong language priors that can override visual evidence when the two conflict.

![Refer to caption](2606.13108v1/v6_images_v2/huanjue.jpg)

## B-52e3387877802a

https://arxiv.org/html/2606.13108v1#chars-16453-17028

### 2.2 Text Detection

In PP-OCRv6, we adopt LCNetV4 as the backbone network for the text detection model. On top of the new backbone, we apply three additional strategies to further improve detection accuracy while maintaining efficiency: (1) RepLKFPN, a lightweight feature pyramid with large receptive field; (2) Auxiliary Deep Supervision for better intermediate feature learning; (3) introducing Focal Loss [[13](#bib.bib14)] combined with Dice Loss [[14](#bib.bib15)] for per-pixel supervision.

![Refer to caption](2606.13108v1/v6_images_v2/ppocrv6_det_pip_ori.png)

## B-55340f63a31c2d

https://arxiv.org/html/2606.13108v1#chars-12265-13705

##### Comparison with LCNetV3.

Table [1](#S2.T1 "Table 1 ‣ Comparison with LCNetV3. ‣ 2.1.1 LCNetV4Block ‣ 2.1 LCNetV4: MetaFormer-Style Lightweight Backbone ‣ 2 Improvement Strategies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks") summarizes the architectural differences. The original MobileNetV3 block in LCNetV3 places the 1×11\times 1 expansion before the DW convolution, coupling token mixing and channel mixing into an inseparable sequence. By contrast, LCNetV4Block moves the DW convolution to the front and applies the 1×11\times 1 expand-compress pair as a standalone residual channel mixer. This enables both the use of structural reparameterization on the DW layer and the BN zero-initialization on the compress layer (which makes each block behave as identity at the start of training, stabilizing convergence for deeper configurations).

|  |  |  |
| --- | --- | --- |
| Design Aspect | LCNetV3 | LCNetV4 (Ours) |
| Architecture Paradigm | MobileNet-style | MetaFormer |
|  | (DW→\toSE→\toPW) | (TokenMixer + ChannelMixer) |
| Channel Interaction | Single 1×\times1 PW Conv | Expand(2×\times)→\toAct→\toCompress |
|  |  | + residual connection |
| Spatial Mixing | Plain DW Conv | RepDWConv (3-branch) |
|  |  | (3×\times3 + 1×\times1 + identity) |
| BN Initialization | Standard | Zero-init on compress BN |
| Scaling Strategy | Uniform scale factor | Per-tier depth/width config |

## B-5675cbc640833f

https://arxiv.org/html/2606.13108v1#chars-25487-27476

#### 2.3.2 Tiny Model: Minimalist Design

The tiny recognition model (1.1M params) forgoes the encoder neck entirely. The backbone output (ℝB×160×1×W\mathbb{R}^{B\times 160\times 1\times W}) is directly reshaped and projected to 80 dimensions via a learned linear layer, then fed into the CTC/NRTR decoder heads. To compensate for the reduced model capacity, we employ knowledge distillation from the medium model. Since the tiny model uses a smaller character dictionary (to reduce output layer size and improve efficiency), we first train a dedicated medium teacher model with the same dictionary as the tiny student, ensuring vocabulary-consistent logit alignment. The teacher is then frozen during distillation. The training objective is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒtiny=ℒCTCGT+ℒNRTRGT+λ⋅ℒKLCTC\mathcal{L}\_{\text{tiny}}=\mathcal{L}\_{\text{CTC}}^{\text{GT}}+\mathcal{L}\_{\text{NRTR}}^{\text{GT}}+\lambda\cdot\mathcal{L}\_{\text{KL}}^{\text{CTC}} |  | (5) |

where ℒCTCGT\mathcal{L}\_{\text{CTC}}^{\text{GT}} and ℒNRTRGT\mathcal{L}\_{\text{NRTR}}^{\text{GT}} are standard ground-truth supervision losses for the CTC and NRTR branches respectively, and ℒKLCTC\mathcal{L}\_{\text{KL}}^{\text{CTC}} is a KL-divergence loss that aligns the student’s CTC output probability distribution with the teacher’s:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒKLCTC=1T∑t=1TDKL(ptteacher∥ptstudent)\mathcal{L}\_{\text{KL}}^{\text{CTC}}=\frac{1}{T}\sum\_{t=1}^{T}D\_{\text{KL}}\big(p\_{t}^{\text{teacher}}\;\|\;p\_{t}^{\text{student}}\big) |  | (6) |

where ptp\_{t} denotes the per-timestep softmax distribution over the vocabulary. Because teacher and student share the identical dictionary, the CTC logits can be directly aligned without any projection or vocabulary mapping. The NRTR branch, supervised only by ground truth with label smoothing, acts as an auxiliary regularizer during training and is discarded at inference. We set λ=1.0\lambda{=}1.0 in all experiments.

## B-5ebe20080eba47

https://arxiv.org/html/2606.13108v1#chars-51129-51161

## Appendix C Ablation Studies

## B-6aa0217d17c913

https://arxiv.org/html/2606.13108v1#chars-56441-58427

## Appendix D Qualitative Analysis of Text Detection

Figure [7](#A4.F7 "Figure 7 ‣ Appendix D Qualitative Analysis of Text Detection ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks") presents qualitative detection results across four representative challenging scenarios. We compare PP-OCRv6\_medium with PP-OCRv5\_server and two state-of-the-art VLMs (Gemini-3.1-Pro and GPT-5.5).

![Refer to caption](2606.13108v1/v6_images_v2/ppocrv6_det_vis.jpg)

The four rows cover curved text on a tire surface, dense small text on an electronic display, artistic/decorative fonts, and business cards, respectively. PP-OCRv6\_medium consistently produces complete and accurate polygon detections across all scenarios. For the curved tire text, PP-OCRv5 misses several text instances, while both VLMs produce overly tight bounding boxes that fail to cover the full text extent. In the electronic display scene, PP-OCRv5 misses some text elements, Gemini-3.1-Pro fails to detect small-sized characters, and GPT-5.5 generates false positives by enclosing non-text regions such as icons and symbols. For the artistic font scene, both PP-OCRv5 and Gemini-3.1-Pro miss text instances. In the business card scene, PP-OCRv5 exhibits missed detections, Gemini-3.1-Pro produces misaligned bounding boxes that do not correspond to the actual text positions, and GPT-5.5 uses axis-aligned boxes that poorly fit the oriented text lines.

These visualizations illustrate the different failure modes of each approach: PP-OCRv5 primarily suffers from missed detections in challenging scenarios, while VLMs exhibit inaccurate localization—either producing overly tight boxes, misaligned regions, or false positives on non-text content. These observations are consistent with the quantitative gaps in Table [4](#S3.T4 "Table 4 ‣ 3.2.1 Main Results ‣ 3.2 Text Detection ‣ 3 Experiments ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks").

## B-6c8fdcc57ffd43

https://arxiv.org/html/2606.13108v1#chars-17028-19224

#### 2.2.1 RepLKFPN: Lightweight Large-Kernel Feature Pyramid

The feature pyramid network (FPN) plays a critical role in fusing multi-scale features for text detection. In PP-OCRv5\_mobile\_det, RSEFPN uses standard 3×\times3 convolutions with Squeeze-and-Excitation (SE) attention [[12](#bib.bib8)] as the output convolution block at each pyramid level. However, these standard convolutions are parameter-heavy, while each block only provides a local 3×\times3 receptive field.

RepLKFPN keeps the overall top-down FPN fusion structure unchanged and replaces only this per-level refinement block with a depthwise-separable design: a DilatedReparamBlock [[15](#bib.bib19)] followed by a 1×\times1 pointwise convolution and SE attention. In our implementation, the DilatedReparamBlock uses a 7×\times7 depthwise convolution as the main branch, plus three parallel dilated depthwise branches (5×\times5 with dilation 1, 3×\times3 with dilation 2, and 3×\times3 with dilation 3). These branches enrich the per-level refinement block with multi-scale spatial patterns during training. At inference, all branches are merged into a single 7×\times7 depthwise convolution via structural reparameterization [[11](#bib.bib18)], incurring no additional branch latency. Table [3](#S2.T3 "Table 3 ‣ 2.2.1 RepLKFPN: Lightweight Large-Kernel Feature Pyramid ‣ 2.2 Text Detection ‣ 2 Improvement Strategies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks") compares the parameter count of the whole FPN neck and the local receptive field of the per-level refinement block.

|  |  |  |  |
| --- | --- | --- | --- |
| Module | Params | Per-level refinement block | Block RF |
| RSEFPN | 172K | 3×\times3 Conv | 3×\times3 |
| RepLKFPN (train) | 140K | DilatedReparamBlock | 7×\times7 |
| RepLKFPN (infer) | 118K | 7×\times7 DWConv | 7×\times7 |

This design reduces the whole FPN neck parameters from 172K to 118K after reparameterization, while increasing the local RF of the per-level refinement block from 3×\times3 to 7×\times7. This provides stronger local context modeling for fused pyramid features and benefits the detection of both large and densely-arranged text.

## B-6e351af8809a15

https://arxiv.org/html/2606.13108v1#chars-45160-45175

## References

## B-72c977863385df

https://arxiv.org/html/2606.13108v1#chars-214-356

# PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks

![[Uncaptioned image]](2606.13108v1/logo/pp_logo.png)

## B-747d3462b58324

https://arxiv.org/html/2606.13108v1#chars-48745-51129

## Appendix B Speed Comparison of Text Detection Models

We further evaluate the inference speed of PP-OCRv6 and PP-OCRv5 text detection models using the PaddleX Inference Benchmark platform. The benchmark is conducted on a server equipped with Intel Xeon Gold 6271C CPUs and NVIDIA Tesla V100-SXM2-32GB GPUs. GPU latency is measured with the Paddle inference backend, while CPU ONNX latency is measured with the PaddleX ONNX Runtime backend.

For each exported detection model, the platform runs batch-size-one inference on square inputs from 512 to 2048 pixels. All latency numbers are averaged over 30 measured iterations after 15 warm-up iterations. Since the benchmark records latency only, this section analyzes inference speed rather than accuracy.

As shown in Figure [6](#A2.F6 "Figure 6 ‣ Appendix B Speed Comparison of Text Detection Models ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks"), PP-OCRv6\_medium is consistently faster than PP-OCRv5\_server under both backends. At the 2048 input resolution, PP-OCRv6\_medium takes 106.89 ms on GPU compared with 253.52 ms for PP-OCRv5\_server, corresponding to a 2.37×\times speedup. Under CPU ONNX inference, PP-OCRv6\_medium takes 2327.23 ms compared with 3034.93 ms for PP-OCRv5\_server, yielding a 1.30×\times speedup.

The lighter PP-OCRv6 tiers provide different speed-capacity trade-offs. PP-OCRv6\_small is close to PP-OCRv5\_mobile in GPU latency at 2048 resolution (42.70 ms vs. 37.36 ms) and is slightly faster under CPU ONNX inference (654.25 ms vs. 687.98 ms). PP-OCRv6\_tiny achieves the lowest CPU ONNX latency among all compared models, reaching 317.06 ms at 2048 resolution. On GPU, however, the tiny model is not always faster than the small model; for example, at 1024 resolution PP-OCRv6\_small takes 12.48 ms while PP-OCRv6\_tiny takes 12.83 ms. This indicates that practical GPU latency is affected not only by model size, but also by operator fusion, parallelism, kernel scheduling, and hardware utilization.

Across both backends, increasing the input resolution from 512 to 2048 leads to a monotonic increase in latency for all models, and the gap between model tiers becomes more pronounced at high resolution. The PP-OCRv5\_server model shows the steepest growth, while the PP-OCRv6 family maintains a more favorable speed-capacity balance across resolutions.

## B-7a4ec5573cfdcc

https://arxiv.org/html/2606.13108v1#chars-34980-35006

### 3.3 Text Recognition

## B-7cfce34685735d

https://arxiv.org/html/2606.13108v1#chars-61619-62958

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

## B-7f87f29c4e66a4

https://arxiv.org/html/2606.13108v1#chars-54517-56441

### C.3 Text Recognition

We evaluate the recognition-specific design choices (neck and decoder) on the final LCNetV4 backbone. All experiments use the same training subset and schedule as the backbone ablation above.

|  |  |  |
| --- | --- | --- |
| Configuration | Acc. (%) | Δ\Delta |
| Neck design | | |
| EncoderWithSVTR (PP-OCRv5, concat skip) | 79.35 | – |
| EncoderWithLightSVTR (additive skip only) | 79.77 | +0.42 |
| EncoderWithLightSVTR (+ DWConv 1×71{\times}7) | 80.24 | +0.89 |
| No neck (reshape + FC, tiny reference) | 74.52 | −-4.83 |
| Decoder configuration (with LightSVTR neck) | | |
| CTC only | 79.08 | – |
| CTC + NRTR-384 (multi-head) | 80.24 | +1.16 |
| CTC + NRTR-512 (medium only) | 80.61 | +1.53 |
| Knowledge distillation (tiny model, no neck) | | |
| Tiny without distillation | 71.83 | – |
| Tiny + CTC KL distillation (λ=1.0\lambda{=}1.0) | 74.52 | +2.69 |

Replacing the concatenation-based skip in EncoderWithSVTR with a lightweight additive connection improves accuracy by +0.42% while reducing neck parameters. Adding the DWConv 1×71{\times}7 local context layer before global attention provides a further +0.47%, confirming that explicit local horizontal modeling is complementary to global self-attention for sequential text features. Removing the neck entirely causes a 4.83% drop, indicating that sequence modeling in the neck is essential for medium/small capacity models.

For the decoder, the multi-head CTC+NRTR design outperforms CTC-only by +1.16%, as the NRTR branch acts as an implicit language model that regularizes the shared encoder during training without adding inference cost. Increasing the NRTR dimension from 384 to 512 for the medium model yields an additional +0.37%.

For the tiny model, CTC logit distillation from the vocabulary-matched medium teacher provides +2.69% accuracy, effectively recovering much of the capacity gap introduced by removing the neck.

## B-81c0ac61beba3a

https://arxiv.org/html/2606.13108v1#chars-19224-20303

#### 2.2.2 Auxiliary Deep Supervision

In PP-OCRv5\_mobile\_det, supervision is only applied to the final fused feature map, which means gradient signals must propagate through the entire FPN before reaching the backbone. This can lead to insufficient learning of intermediate features, particularly at deeper scales.

We introduce auxiliary prediction heads [[16](#bib.bib17)] at three FPN levels (P2, P3, P4). Each auxiliary head independently predicts the shrink map, threshold map, and binary map using the same head architecture as the main branch. During training, the auxiliary outputs are supervised with the same loss formulation as the main branch (Dice+Focal loss on the shrink map and binary map, L1 loss on the threshold map), weighted by per-scale coefficients (λP2=0.4\lambda\_{\text{P2}}=0.4, λP3=0.3\lambda\_{\text{P3}}=0.3, λP4=0.2\lambda\_{\text{P4}}=0.2). This deep supervision provides stronger gradient signals to intermediate features and acts as a regularizer. At inference, the auxiliary heads are removed, so the model size and speed remain unchanged.

## B-8417768abd2c3c

https://arxiv.org/html/2606.13108v1#chars-27522-28117

##### Training Configuration.

All models are implemented in PaddlePaddle and trained with Adam optimizer (β1=0.9\beta\_{1}=0.9, β2=0.999\beta\_{2}=0.999) using cosine learning rate schedule with linear warmup. Recognition models are trained for 100 epochs with L2 regularization (3×10−53\times 10^{-5}). Detection models are trained for 500 epochs with L2 regularization (1×10−61\times 10^{-6}). Multi-scale training with input sizes [320×32,320×48,320×64][320\times 32,320\times 48,320\times 64] is used for recognition. Detection uses 640×640640\times 640 input with CopyPaste augmentation.

## B-881f59f63ecc6f

https://arxiv.org/html/2606.13108v1#chars-8994-10658

#### 2.1.1 LCNetV4Block

Following the MetaFormer paradigm, the LCNetV4Block (Figure [3](#S2.F3 "Figure 3 ‣ 2.1 LCNetV4: MetaFormer-Style Lightweight Backbone ‣ 2 Improvement Strategies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks")) decomposes each layer into a token mixer followed by a channel mixer. Let 𝐱∈ℝC×H×W\mathbf{x}\in\mathbb{R}^{C\times H\times W} denote the input feature. The block computes:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐱^\displaystyle\hat{\mathbf{x}} | =SE​(DW​(𝐱))+𝐱\displaystyle=\text{SE}\big(\text{DW}(\mathbf{x})\big)+\mathbf{x} |  | (1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐲\displaystyle\mathbf{y} | =W2​σ​(W1​𝐱^)+𝐱^\displaystyle=W\_{2}\,\sigma(W\_{1}\,\hat{\mathbf{x}})+\hat{\mathbf{x}} |  | (2) |

where DW​(⋅)\text{DW}(\cdot) is a 3×33\times 3 depthwise convolution (the token mixer), SE is an optional squeeze-and-excitation [[12](#bib.bib8)] module, W1∈ℝ2​C×CW\_{1}\in\mathbb{R}^{2C\times C} and W2∈ℝC×2​CW\_{2}\in\mathbb{R}^{C\times 2C} are 1×11\times 1 pointwise convolutions forming the channel mixer with expansion ratio 2, and σ\sigma is GELU. Both stages employ identity shortcuts when the spatial resolution and channel dimension remain unchanged.

This separation has two practical advantages. First, it provides independent design knobs: the token mixer controls the spatial receptive field while the channel mixer controls the per-position representational capacity, and the two can be tuned without mutual interference. Second, it enables targeted application of structural reparameterization to the token mixer alone, as discussed below.

## B-89a44193261116

https://arxiv.org/html/2606.13108v1#chars-39746-41496

#### 3.3.3 Robustness to Crop Margin Variation

In practical OCR pipelines, the text detection module produces bounding boxes with varying margins around the actual text content. Depending on the detection model’s behavior and post-processing parameters, the cropped text image may be tightly clipped to the character boundaries or include substantial background padding. A robust recognition model should produce consistent predictions regardless of how much margin surrounds the text. To evaluate this, we measure recognition consistency across different crop margins: for each test sample, we generate multiple crops with progressively looser boundaries and report the percentage of samples that yield identical predictions across all margin settings (Table [8](#S3.T8 "Table 8 ‣ 3.3.3 Robustness to Crop Margin Variation ‣ 3.3 Text Recognition ‣ 3 Experiments ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks")).

|  |  |  |
| --- | --- | --- |
| Model | Consistency (%) | Δ\Delta vs. v5 |
| PP-OCRv3\_mobile | 31.05 | – |
| PP-OCRv4\_server | 45.69 | – |
| PP-OCRv4\_mobile | 43.41 | – |
| PP-OCRv5\_server | 54.82 | – |
| PP-OCRv5\_mobile | 57.74 | – |
| PP-OCRv6\_medium | 75.32 | +20.5 |
| PP-OCRv6\_small | 67.80 | +10.1 |
| PP-OCRv6\_tiny | 44.80 | – |

PP-OCRv6\_medium achieves 75.32% consistency, a +20.5% improvement over PP-OCRv5\_server (54.82%). This improvement suggests that LCNetV4’s MetaFormer architecture and LightSVTR’s local-global attention mechanism produce feature representations that are less sensitive to input crop variations. The trend is consistent across the series: v3 (31.05%) →\to v4 (45.69%) →\to v5 (54.82%) →\to v6 (75.32%), showing steady progress with each generation.

## B-90f81c768d1d48

https://arxiv.org/html/2606.13108v1#chars-13705-16453

#### 2.1.2 Network Architecture and Scaling

LCNetV4 is designed to serve both text detection and text recognition within a single codebase, differentiated only by stride configuration and output interface. Unlike LCNetV3, which applies a uniform scale factor to resize all channels simultaneously, LCNetV4 adopts explicit per-tier configurations with independently tuned depth and width at each stage (Table [2](#S2.T2 "Table 2 ‣ 2.1.2 Network Architecture and Scaling ‣ 2.1 LCNetV4: MetaFormer-Style Lightweight Backbone ‣ 2 Improvement Strategies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks")).

The two task modes differ in their spatial processing strategy. In detection mode, each stage transition applies standard stride-2 downsampling, producing multi-scale feature maps at strides 4, 8, 16, and 32 for FPN-based processing. In recognition mode, the width dimension must be preserved for sequential CTC/NRTR decoding. We address this by applying asymmetric stride (2,1)(2,1) at the Stage 3 and Stage 4 transitions, which halves the height at each step while leaving the width intact. After Stage 4, average pooling along the height axis produces a 1-D feature sequence of shape [B,C,1,W][B,C,1,W]. This asymmetric stride mechanism is what allows a single backbone to output both 2-D spatial pyramids (for detection) and 1-D sequential features (for recognition). Table [2](#S2.T2 "Table 2 ‣ 2.1.2 Network Architecture and Scaling ‣ 2.1 LCNetV4: MetaFormer-Style Lightweight Backbone ‣ 2 Improvement Strategies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks") summarizes the per-tier configurations for both tasks; Figure [3](#S2.F3 "Figure 3 ‣ 2.1 LCNetV4: MetaFormer-Style Lightweight Backbone ‣ 2 Improvement Strategies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks") illustrates both modes.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Task | Tier | Stem | Stage 1 | Stage 2 | Stage 3 | Stage 4 |
| Det | Tiny | Branch(16) | 2×\times16 | 3×\times32 | 5×\times64 | 3×\times160 |
| Small | Branch(48) | 2×\times48 | 3×\times96 | 5×\times192 | 3×\times384 |
| Medium | Branch(128) | 2×\times128 | 3×\times256 | 5×\times512 | 3×\times896 |
| Rec | Tiny | Simple(48) | 1×\times48 | 1×\times48 | 3×\times96 | 4×\times160 |
| Small | Branch(96) | 1×\times96 | 2×\times96 | 7×\times192 | 3×\times384 |
| Medium | Branch(128) | 1×\times128 | 3×\times256 | 7×\times512 | 3×\times768 |
| Full model parameters (Det / Rec) | | | | | | |
| Tiny | | 0.43M / 1.1M  (end-to-end: 1.5M) | | | | |
| Small | | 2.48M / 5.2M  (end-to-end: 7.7M) | | | | |
| Medium | | 15.5M / 19M  (end-to-end: 34.5M) | | | | |

## B-9510b9c1151e17

https://arxiv.org/html/2606.13108v1#chars-35006-38460

#### 3.3.1 Main Results

Table [6](#S3.T6 "Table 6 ‣ 3.3.1 Main Results ‣ 3.3 Text Recognition ‣ 3 Experiments ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks") compares recognition accuracy on our in-house benchmark (15 categories) across PP-OCRv6, PP-OCRv5, and state-of-the-art VLMs.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | W-Avg | Scenario-specific Accuracy (%) | | | | | | | | | | | | | | |
| Handwritten | | Printed | | TC | Anc. | JP | Conf. | Spec. | Gen. | Pin. | Art. | Indus. | Screen | Card |
| CN | EN | CN | EN |
| Vision-Language Models | | | | | | | | | | | | | | | | |
| GPT-5.5 | 64.2 | 19.2 | 56.9 | 75.7 | 82.2 | 57.5 | 63.7 | 58.6 | 49.1 | 48.3 | 67.7 | 50.4 | 53.0 | 62.4 | 67.7 | 71.1 |
| Qwen3-VL-235B | 74.9 | 49.7 | 73.2 | 82.3 | 86.2 | 76.4 | 33.6 | 66.2 | 56.1 | 49.0 | 82.5 | 76.5 | 69.6 | 74.7 | 73.8 | 78.7 |
| Kimi-K2.6 | 62.9 | 31.0 | 58.4 | 76.8 | 80.9 | 62.7 | 16.5 | 54.1 | 43.5 | 38.0 | 68.0 | 45.2 | 59.9 | 57.1 | 58.4 | 68.4 |
| MiniMax-M3 | 54.1 | 15.5 | 60.3 | 63.5 | 81.5 | 53.2 | 2.2 | 43.7 | 42.2 | 42.8 | 53.8 | 50.3 | 44.3 | 44.1 | 56.6 | 67.0 |
| Gemini-3.1-Pro | 71.4 | 46.4 | 73.0 | 80.0 | 90.5 | 69.5 | 18.0 | 67.2 | 54.4 | 50.3 | 74.6 | 75.9 | 63.1 | 69.1 | 73.2 | 75.9 |
| PP-OCRv5 Series | | | | | | | | | | | | | | | | |
| PP-OCRv5\_server | 78.1 | 58.0 | 59.6 | 90.1 | 85.1 | 74.7 | 60.4 | 73.7 | 59.4 | 56.8 | 86.5 | 74.4 | 64.0 | 70.2 | 68.1 | 87.6 |
| PP-OCRv5\_mobile | 73.7 | 41.7 | 50.9 | 86.0 | 86.0 | 72.0 | 57.8 | 75.8 | 55.7 | 54.8 | 80.7 | 72.5 | 54.0 | 59.3 | 57.6 | 81.7 |
| PP-OCRv6 (Ours) | | | | | | | | | | | | | | | | |
| PP-OCRv6\_medium | 83.2 | 62.1 | 67.8 | 91.5 | 94.1 | 78.6 | 72.4 | 90.5 | 64.9 | 61.7 | 87.5 | 78.1 | 71.2 | 77.4 | 82.5 | 88.1 |
| PP-OCRv6\_small | 81.3 | 57.6 | 61.1 | 90.5 | 93.3 | 77.0 | 71.1 | 88.2 | 64.1 | 60.2 | 85.7 | 75.9 | 68.4 | 76.4 | 79.7 | 86.9 |
| PP-OCRv6\_tiny | 73.5 | 40.1 | 39.3 | 86.7 | 88.4 | 65.0 | 68.4 | 89.8 | 52.3 | 57.1 | 78.0 | 65.4 | 54.7 | 62.1 | 71.2 | 80.5 |

Abbreviations: CN: Chinese, EN: English, TC: Traditional Chinese, Anc.: Ancient Text, JP: Japanese, Conf.: Confusable Characters, Spec.: Special Characters, Gen.: General Scenes, Pin.: Pinyin, Art.: Artistic Text, Indus.: Industrial Characters, Screen: Screen Displays, Card: Physical Card Surfaces.

PP-OCRv6\_medium achieves 83.2% weighted average, outperforming PP-OCRv5\_server by +5.1% absolute with fewer parameters. The gains are particularly pronounced on categories requiring strong multilingual and contextual understanding: Japanese (+16.8%), Ancient text (+12.0%), and Screen displays (+14.4%). PP-OCRv6\_small (5.2M) surpasses PP-OCRv5\_server (21M) by +3.2% with 4×\times fewer parameters, demonstrating the architectural efficiency of LCNetV4.

Compared to VLMs, the performance gap is substantial. The best-performing VLM (Qwen3-VL-235B, 74.9%) trails PP-OCRv6\_medium by 8.3%, despite having approximately 6800×\times more parameters. Even PP-OCRv6\_tiny (1.1M) exceeds four of the five VLMs in weighted average, trailing only Qwen3-VL-235B by 1.4%. VLMs exhibit particularly poor performance on low-resource categories such as Ancient text (Gemini: 18.0%, MiniMax: 2.2%) and Handwritten Chinese (GPT-5.5: 19.2%), indicating that these categories require specialized supervision.

## B-9d2be2866f13b3

https://arxiv.org/html/2606.13108v1#chars-7189-8994

### 2.1 LCNetV4: MetaFormer-Style Lightweight Backbone

PP-OCRv5 employs two separate backbone families: PPHGNetV2 for the server model and LCNetV3 [[9](#bib.bib4)] for the mobile model. This dual-architecture design increases engineering complexity in training, deployment, and maintenance. LCNetV3 follows the MobileNet-style [[10](#bib.bib5)] convention in which depthwise convolution, squeeze-and-excitation, and pointwise convolution are stacked sequentially without explicit functional decomposition. This design conflates spatial aggregation and cross-channel interaction into a single monolithic block, limiting the flexibility to optimize each operation independently.

The MetaFormer [[7](#bib.bib6)] framework offers an alternative perspective: an effective architecture can be decomposed into a token mixer for spatial feature aggregation and a channel mixer for per-position feature transformation. RepViT [[8](#bib.bib7)] validated this decomposition on lightweight CNNs, showing consistent accuracy gains over MobileNet-style baselines at comparable computational budgets.

Building on these findings, we design LCNetV4 around an explicit token mixer / channel mixer decomposition, augmented with structural reparameterization [[11](#bib.bib18)] to enrich the training-time representational capacity without increasing inference cost. A single LCNetV4 implementation serves both text detection and text recognition through task-specific stride configurations (Figure [3](#S2.F3 "Figure 3 ‣ 2.1 LCNetV4: MetaFormer-Style Lightweight Backbone ‣ 2 Improvement Strategies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks")), unifying the previously separate backbone families into one codebase.

![Refer to caption](2606.13108v1/v6_images_v2/backbone.png)

## B-a1b287901c9a93

https://arxiv.org/html/2606.13108v1#chars-28776-32601

#### 3.2.1 Main Results

Table [4](#S3.T4 "Table 4 ‣ 3.2.1 Main Results ‣ 3.2 Text Detection ‣ 3 Experiments ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks") compares detection Hmean on our in-house benchmark covering 16 categories across PP-OCRv6, PP-OCRv5, and state-of-the-art VLMs. Detailed ablation studies validating each individual strategy are provided in Appendix [C.2](#A3.SS2 "C.2 Text Detection ‣ Appendix C Ablation Studies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks").

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | AVG | Scenario-specific Hmean (%) | | | | | | | | | | | | | | | |
| Handwritten | | Printed | | TC | Anc. | JP | Blur | Emo. | Warp | Pin. | Art. | Tab. | Rot. | Indus. | Gen. |
| CN | EN | CN | EN |
| Vision-Language Models | | | | | | | | | | | | | | | | | |
| Gemini-3.1-Pro | 46.8 | 53.4 | 56.5 | 47.3 | 47.6 | 39.0 | 45.8 | 38.2 | 50.0 | 68.1 | 44.6 | 40.6 | 65.2 | 26.9 | 22.1 | 52.5 | 50.2 |
| GPT-5.5 | 45.6 | 42.4 | 58.5 | 50.2 | 51.9 | 35.0 | 26.7 | 42.0 | 49.1 | 97.5 | 37.7 | 36.3 | 52.0 | 71.0 | 10.0 | 36.2 | 32.6 |
| Qwen3-VL-235B | 38.3 | 56.5 | 66.0 | 41.7 | 37.0 | 19.3 | 13.1 | 27.0 | 38.5 | 81.2 | 28.5 | 33.0 | 68.3 | 19.6 | 2.1 | 48.4 | 32.3 |
| Kimi-K2.6 | 12.8 | 12.5 | 25.5 | 10.1 | 18.5 | 8.2 | 7.5 | 11.2 | 16.9 | 28.9 | 13.9 | 6.8 | 16.1 | 10.9 | 0.8 | 6.3 | 10.9 |
| MiniMax-M3 | 12.0 | 13.7 | 19.3 | 9.8 | 14.1 | 7.7 | 11.1 | 10.6 | 16.1 | 32.8 | 12.8 | 8.5 | 16.6 | 5.5 | 0.1 | 6.4 | 6.4 |
| PP-OCRv5 | | | | | | | | | | | | | | | | | |
| PP-OCRv5\_server | 81.6 | 80.3 | 84.1 | 94.5 | 91.7 | 81.5 | 67.6 | 77.2 | 90.1 | 96.2 | 87.6 | 67.1 | 67.3 | 97.1 | 80.0 | 64.3 | 79.7 |
| PP-OCRv5\_mobile | 75.2 | 74.4 | 77.7 | 90.5 | 91.0 | 82.3 | 58.1 | 72.7 | 87.4 | 93.6 | 82.7 | 57.5 | 52.5 | 92.8 | 64.7 | 52.8 | 72.1 |
| PP-OCRv6 (Ours) | | | | | | | | | | | | | | | | | |
| PP-OCRv6\_medium | 86.2 | 83.7 | 84.0 | 95.1 | 93.7 | 86.3 | 80.2 | 84.3 | 94.1 | 99.6 | 88.6 | 74.0 | 69.0 | 96.8 | 93.8 | 73.3 | 82.8 |
| PP-OCRv6\_small | 84.1 | 80.5 | 87.1 | 94.2 | 93.6 | 85.7 | 72.6 | 82.3 | 92.6 | 99.7 | 87.6 | 69.6 | 65.3 | 95.6 | 93.7 | 67.6 | 78.2 |
| PP-OCRv6\_tiny | 80.6 | 79.4 | 85.9 | 93.1 | 92.3 | 83.7 | 63.0 | 76.6 | 89.3 | 99.8 | 86.1 | 59.0 | 60.1 | 94.7 | 91.0 | 62.0 | 73.8 |

Abbreviations: CN: Chinese, EN: English, TC: Traditional Chinese, Anc.: Ancient Text, JP: Japanese, Emo.: Emoji, Pin.: Pinyin, Art.: Artistic Text, Tab.: Table OCR, Rot.: Rotate, Indus.: Industrial Characters, Gen.: General Scenes.

PP-OCRv6 consistently improves text detection accuracy over previous PP-OCR models. PP-OCRv6\_medium achieves the best average Hmean of 86.2%, outperforming PP-OCRv5\_server by 4.6 percentage points, with notable gains on Japanese, ancient text, rotated text, and industrial-character scenarios. PP-OCRv6\_small further reaches 84.1% average Hmean and also surpasses PP-OCRv5\_server, while PP-OCRv6\_tiny obtains 80.6% average Hmean, approaching the server baseline and clearly outperforming PP-OCRv5\_mobile.

Compared with VLMs, the PP-OCRv6 detection models show a substantial advantage in precise text localization. PP-OCRv6\_medium exceeds the best VLM result, Gemini-3.1-Pro, by 39.4 percentage points (86.2% vs. 46.8%), and even PP-OCRv6\_tiny outperforms it by 33.8 percentage points (80.6% vs. 46.8%). Qwen3-VL-235B, Kimi-K2.6, and MiniMax-M3 achieve average Hmean scores of only 38.3%, 12.8%, and 12.0%, respectively. The consistent gap across all evaluated VLMs suggests that accurate text localization remains challenging for current general-purpose VLMs and continues to benefit from specialized OCR architectures.

## B-a8de81e0454780

https://arxiv.org/html/2606.13108v1#chars-41496-44083

### 3.4 End-to-End System Inference Speed

We benchmark the end-to-end OCR pipeline (detection + recognition) on 200 images comprising both general scene and document images. The measurement includes image I/O from disk, pre-processing, model inference, and post-processing. The software environment is PaddlePaddle 3.2.1, ONNX Runtime 1.23.2 (CUDA 12.6), OpenVINO 2025.0, and TensorRT 8.6.1 (CUDA 11.8, paddle2onnx 2.0.2rc3). Results are summarized in Table [9](#S3.T9 "Table 9 ‣ 3.4 End-to-End System Inference Speed ‣ 3 Experiments ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks").

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hardware | Backend | PP-OCRv6\_medium | PP-OCRv6\_small | PP-OCRv6\_tiny | PP-OCRv5\_server | PP-OCRv5\_mobile | PP-OCRv4\_mobile |
| NVIDIA A100 | PaddlePaddle | 0.29 | 0.25 | 0.13 | 0.32 | 0.25 | 0.14 |
| TensorRT | – | 0.32 | 0.16 | – | 0.33 | 0.16 |
| NVIDIA V100 | PaddlePaddle | 0.72 | 0.49 | 0.21 | 0.66 | 0.50 | 0.25 |
| ONNX Runtime | 0.67 | 0.53 | 0.29 | 0.77 | 0.46 | 0.27 |
| TensorRT | 0.77 | 0.60 | 0.23 | 0.73 | 0.59 | 0.27 |
| Intel Xeon 8350C | PaddlePaddle | 2.05 | 0.79 | 0.32 | 2.04 | 0.80 | 0.62 |
| OpenVINO | 1.40 | 0.59 | 0.20 | 7.30 | 0.78 | 0.60 |
| ONNX Runtime | 3.31 | 0.61 | 0.22 | 6.36 | 0.61 | 0.49 |
| Apple M4 | PaddlePaddle | 8.82 | 3.07 | 0.96 | >>10 | 5.82 | 5.65 |
| ONNX Runtime | 5.55 | 1.29 | 0.35 | 7.20 | 1.10 | 1.02 |

Table [9](#S3.T9 "Table 9 ‣ 3.4 End-to-End System Inference Speed ‣ 3 Experiments ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks") reveals several trends. First, PP-OCRv6\_medium consistently matches or outperforms PP-OCRv5\_server across all tested configurations: 1.1×\times faster on A100 (0.29s vs. 0.32s), 1.15×\times on V100 ONNX Runtime (0.67s vs. 0.77s), and 5.2×\times on Intel Xeon OpenVINO (1.40s vs. 7.30s). Second, PP-OCRv6\_small matches PP-OCRv5\_mobile in latency on most platforms while delivering higher accuracy; it is 1.9×\times faster on Apple M4 PaddlePaddle (3.07s vs. 5.82s) and 1.3×\times on Intel Xeon OpenVINO (0.59s vs. 0.78s). Third, PP-OCRv6\_tiny is the fastest model across all platforms, achieving 6.1×\times speedup over PP-OCRv5\_mobile on Apple M4 PaddlePaddle (0.96s vs. 5.82s), 3.9×\times on Intel Xeon OpenVINO (0.20s vs. 0.78s), and reaching 0.13s on A100. Overall, the depthwise-separable architecture of LCNetV4 translates into favorable latency characteristics particularly on CPU and under optimized inference backends such as OpenVINO.

## B-a98ba993d23546

https://arxiv.org/html/2606.13108v1#chars-21810-22881

### 2.3 Text Recognition

The PP-OCRv6 recognition system (Figure [5](#S2.F5 "Figure 5 ‣ 2.3.1 EncoderWithLightSVTR ‣ 2.3 Text Recognition ‣ 2 Improvement Strategies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks")) adopts a Backbone–Neck–Head pipeline. The LCNetV4 backbone encodes the input text line image (3×48×W3\times 48\times W) into a compact feature map 𝐅∈ℝB×C×1×W\mathbf{F}\in\mathbb{R}^{B\times C\times 1\times W}, where the height has been collapsed to 1 by the asymmetric stride design described above. This feature map is then passed to the EncoderWithLightSVTR neck (for medium/small models) or directly reshaped (for tiny), before being decoded by a multi-head architecture combining CTC [[18](#bib.bib1)] and NRTR [[19](#bib.bib9)]. At inference, only the CTC branch is evaluated for parallel decoding; the NRTR branch participates only during training, functioning as an implicit language model that regularizes the shared encoder representations through auxiliary cross-entropy supervision with label smoothing.

## B-b03f7cf098b896

https://arxiv.org/html/2606.13108v1#chars-45175-45188

## Appendix

## B-b09096a9b7c69e

https://arxiv.org/html/2606.13108v1#chars-10658-12265

##### Reparameterization of the token mixer.

The token mixer in Eq. ([1](#S2.E1 "In 2.1.1 LCNetV4Block ‣ 2.1 LCNetV4: MetaFormer-Style Lightweight Backbone ‣ 2 Improvement Strategies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks")) performs depthwise convolution followed by a residual addition. As shown by RepVGG [[11](#bib.bib18)], any convolution with an identity shortcut can be augmented with additional parallel branches during training and then merged into a single convolution at inference via algebraic equivalence. We apply this insight to the depthwise layer: during training, we maintain a 3×33\times 3 DW branch, a 1×11\times 1 DW branch, and a batch-normalized identity branch, all summed before a shared BN layer. At inference, the three branches are fused into one 3×33\times 3 DW convolution by zero-padding the 1×11\times 1 kernel and the identity to 3×33\times 3, then summing the weight tensors. This introduces zero additional inference cost while providing a richer optimization landscape during training through the implicit ensemble of different-scale receptive fields.

We do not apply reparameterization to the channel mixer because 1×11\times 1 convolutions already operate with maximal parameter efficiency per FLOP (every parameter contributes a unique cross-channel interaction) and lack spatial extent, so multi-branch augmentation offers negligible benefit. This asymmetric use of reparameterization, applying it to the spatial DW layer but not the 1×11\times 1 layers, follows the same design principle as RepViT [[8](#bib.bib7)].

## B-b34880eff4aec1

https://arxiv.org/html/2606.13108v1#chars-6463-7189

## 2 Improvement Strategies

This section presents the key technical improvements in PP-OCRv6. We first describe LCNetV4, the unified backbone (Section [2.1](#S2.SS1 "2.1 LCNetV4: MetaFormer-Style Lightweight Backbone ‣ 2 Improvement Strategies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks")), then detail detection-specific (Section [2.2](#S2.SS2 "2.2 Text Detection ‣ 2 Improvement Strategies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks")) and recognition-specific (Section [2.3](#S2.SS3 "2.3 Text Recognition ‣ 2 Improvement Strategies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks")) improvements.

## B-b6cd890619fc59

https://arxiv.org/html/2606.13108v1#chars-0-214

##### Report GitHub Issue

Content selection saved. Describe the issue below:

![](/static/base/1.0.1/images/icons/smileybones-small.svg)
![arXiv logo](/static/base/1.0.1/images/arxiv-logo-primary-light.svg)

001

## B-ba2eb27fd05462

https://arxiv.org/html/2606.13108v1#chars-27494-27522

### 3.1 Experimental Setup

## B-bcb6b1f0fba365

https://arxiv.org/html/2606.13108v1#chars-356-1663

###### Abstract

Vision-Language Models (VLMs) have achieved impressive results on general vision-language tasks, yet they suffer from hallucination, imprecise localization, and prohibitive computational cost when applied to dedicated OCR scenarios. This paper presents PP-OCRv6, a lightweight OCR system that combines architectural innovation with data-centric optimization. PP-OCRv6 redesigns the backbone, detection neck, and recognition neck around a unified MetaFormer-style building block with structural reparameterization, decoupling spatial token mixing from channel mixing and supporting both tasks through task-specific stride configurations. Three model tiers (medium, small, tiny) share the same block primitives, covering deployment scenarios from server to edge. On our in-house benchmarks, PP-OCRv6\_medium achieves 83.2% recognition accuracy and 86.2% detection Hmean, outperforming PP-OCRv5\_server by +5.1% and +4.6% respectively while surpassing Qwen3-VL-235B, GPT-5.5, and Gemini-3.1-Pro with orders of magnitude fewer parameters. The tiny tier achieves 3.9×\times faster inference than PP-OCRv5\_mobile on Intel Xeon CPU while maintaining comparable accuracy.

![Refer to caption](2606.13108v1/v6_images_v2/v6acc_opt.png)

![Refer to caption](2606.13108v1/v6_images_v2/v6acc_opt.png)

## B-bf4dc3a2d1aeca

https://arxiv.org/html/2606.13108v1#chars-20303-21810

#### 2.2.3 Focal Loss for Per-Pixel Supervision

PP-OCRv5\_mobile\_det uses only DiceLoss [[14](#bib.bib15)] for the probability map supervision. DiceLoss is a set-level metric that computes a single scalar measuring the global overlap between prediction and ground truth—it provides less explicit pixel-wise discrimination between easy and hard samples. Although OHEM [[17](#bib.bib16)] is applied, it relies on per-pixel loss ranking to select hard negatives, which may limit the effectiveness of hard-sample mining because the optimization objective is dominated by global region overlap..

To address this, we introduce Focal Loss [[13](#bib.bib14)] as an explicit per-pixel supervision signal and combine it with DiceLoss:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒshrink=λdice⋅ℒDice+λfocal⋅ℒFocal\mathcal{L}\_{\text{shrink}}=\lambda\_{\text{dice}}\cdot\mathcal{L}\_{\text{Dice}}+\lambda\_{\text{focal}}\cdot\mathcal{L}\_{\text{Focal}} |  | (3) |

where λdice=λfocal=1.0\lambda\_{\text{dice}}=\lambda\_{\text{focal}}=1.0. Focal Loss computes an independent loss value for each pixel via −αt​(1−pt)γ​log⁡(pt)-\alpha\_{t}(1-p\_{t})^{\gamma}\log(p\_{t}), providing true per-pixel supervision that DiceLoss alone cannot offer. We set α=0.25\alpha=0.25 and γ=2.5\gamma=2.5. The two losses are complementary: DiceLoss optimizes global region overlap, while Focal Loss provides fine-grained per-pixel gradients that adaptively emphasize hard examples, enabling more precise learning at the pixel level.

## B-c31f5e39362734

https://arxiv.org/html/2606.13108v1#chars-22881-25487

#### 2.3.1 EncoderWithLightSVTR

The recognition neck in PP-OCRv5 (EncoderWithSVTR) applies global self-attention to the feature sequence and then fuses the result with the input via concatenation along the channel axis, followed by a 1×11\times 1 projection from 2​C2C back to CC. This concatenation-based skip demands a 2​C×C2C\times C projection matrix, which is parameter-heavy (e.g., 2×120×120=28,8002\times 120\times 120=28{,}800 parameters for the mobile model) and provides limited inductive bias about the local structure of text.

We propose EncoderWithLightSVTR (Figure [5](#S2.F5 "Figure 5 ‣ 2.3.1 EncoderWithLightSVTR ‣ 2.3 Text Recognition ‣ 2 Improvement Strategies ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks")) to address both issues simultaneously. The design rests on two observations: (1) text is inherently sequential, so local context along the horizontal axis is complementary to global attention; (2) additive skip connections are sufficient for feature fusion when dimensions match, avoiding the doubled channel width.

Concretely, the input feature map 𝐅\mathbf{F} is first projected by a 1×11\times 1 convolution to reduce the channel dimension from CC to a smaller DD (e.g., D=192D{=}192 for medium). A depthwise convolution with kernel 1×71\times 7 is then applied along the width axis, injecting local positional awareness of neighboring characters before any global interaction occurs. This local-context-first design is motivated by the observation that character boundaries and inter-character spacing are highly informative for recognition, yet purely global attention treats all positions equally. The locally-primed features then pass through LL stacked Transformer blocks (MHSA + FFN). Finally, the output is added element-wise to a lightweight 1×11\times 1 skip projection of the original input:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐲=TransformerBlockL​(DWConv1×7​(Conv1×1​(𝐱)))⏟local-global path+Conv1×1skip​(𝐱)⏟skip path\mathbf{y}=\underbrace{\text{TransformerBlock}^{L}\!\big(\text{DWConv}\_{1\times 7}(\text{Conv}\_{1\times 1}(\mathbf{x}))\big)}\_{\text{local-global path}}+\underbrace{\text{Conv}\_{1\times 1}^{\text{skip}}(\mathbf{x})}\_{\text{skip path}} |  | (4) |

The additive fusion costs only C×DC\times D parameters (vs. 2​C22C^{2} for concatenation), and the DWConv adds merely D×7D\times 7 depthwise parameters—negligible overhead. For the medium model we set D=192D{=}192, L=2L{=}2, MLP ratio 4.0; for small, D=120D{=}120, L=2L{=}2, ratio 2.0.

![Refer to caption](2606.13108v1/v6_images_v2/rec.png)

## B-ce66a7ba1adf7c

https://arxiv.org/html/2606.13108v1#chars-44083-45160

## 4 Conclusion

We present PP-OCRv6, a lightweight OCR system that advances accuracy through the combination of architectural innovation and data-centric optimization. Experiments demonstrate that PP-OCRv6\_medium achieves 83.2% recognition accuracy (+5.1% over PP-OCRv5\_server) and 86.2% detection Hmean (+4.6% over PP-OCRv5\_server), while PP-OCRv6\_tiny (0.43M detection, 1.1M recognition) approaches PP-OCRv5\_server in detection and remains competitive for recognition with an order of magnitude fewer parameters. Compared to VLMs, PP-OCRv6 achieves higher accuracy with 6800×\times fewer parameters and produces substantially lower hallucination rates (93.2% vs. 80.6% for Qwen3-VL-235B). These results confirm that lightweight specialized OCR systems, when equipped with modern architecture designs and curated training data, remain the practical choice for production deployment in the large-model era.

In future work, we plan to release a PP-OCRv6\_large model with greater capacity, higher accuracy, and broader language coverage beyond the current 50 languages.

## B-dadea74893eb58

https://arxiv.org/html/2606.13108v1#chars-59611-61619

## Appendix F Qualitative Comparison with PP-OCRv5

Figures [9](#A6.F9 "Figure 9 ‣ Appendix F Qualitative Comparison with PP-OCRv5 ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks")–[14](#A6.F14 "Figure 14 ‣ Appendix F Qualitative Comparison with PP-OCRv5 ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks") present side-by-side end-to-end OCR results comparing PP-OCRv6\_medium and PP-OCRv5\_server across diverse real-world scenarios, covering Chinese, English, Japanese, artistic fonts, industrial characters, rotated text, pinyin, dot-matrix characters, special characters, and general scenes. Each figure shows the input image alongside the detection and recognition outputs of both systems.

![Refer to caption](2606.13108v1/v6_images_v2/case1.jpg)
![Refer to caption](2606.13108v1/v6_images_v2/case2.jpg)
![Refer to caption](2606.13108v1/v6_images_v2/case3.jpg)
![Refer to caption](2606.13108v1/v6_images_v2/case4.jpg)
![Refer to caption](2606.13108v1/v6_images_v2/case5.jpg)
![Refer to caption](2606.13108v1/v6_images_v2/case6.jpg)
![[LOGO]](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)

## B-dce52acf09890b

https://arxiv.org/html/2606.13108v1#chars-32601-34980

#### 3.2.2 Robustness to Input Resolution Variation

To evaluate detection robustness under input-resolution perturbations, we construct a scaled validation benchmark by randomly sampling 600 images from the detection validation set and resizing each image using seven scale factors ranging from 0.35× to 2.83×. The scales form a symmetric geometric progression around the original resolution, with a ratio of 2\sqrt{2} between adjacent levels, providing approximately uniform sampling in scale space while covering both moderate and substantial resolution variations. Polygon annotations are scaled by the same factor as the image and validated before evaluation. We report Hmean at each tested scale, together with the mean Hmean, standard deviation, and coefficient of variation (CV) across all scales.

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | 0.35×\times | 0.50×\times | 0.71×\times | 1.00×\times | 1.41×\times | 2.00×\times | 2.83×\times | Mean ↑\uparrow | Std. ↓\downarrow | CV ↓\downarrow (%) |
| PP-OCRv4\_server | 55.76 | 69.75 | 71.32 | 73.30 | 73.42 | 68.39 | 57.09 | 67.00 | 6.91 | 10.31 |
| PP-OCRv4\_mobile | 48.53 | 65.51 | 68.38 | 68.56 | 69.73 | 68.56 | 64.65 | 64.84 | 6.87 | 10.60 |
| PP-OCRv5\_server | 74.70 | 82.37 | 86.30 | 85.88 | 84.17 | 79.13 | 67.28 | 79.98 | 6.41 | 8.02 |
| PP-OCRv5\_mobile | 66.94 | 73.59 | 79.20 | 81.50 | 80.77 | 75.39 | 65.81 | 74.74 | 5.91 | 7.90 |
| PP-OCRv6\_medium | 76.29 | 85.00 | 89.04 | 89.72 | 89.69 | 89.04 | 87.94 | 86.67 | 4.50 | 5.19 |
| PP-OCRv6\_small | 71.86 | 81.12 | 86.35 | 88.52 | 88.65 | 87.75 | 86.52 | 84.40 | 5.64 | 6.68 |
| PP-OCRv6\_tiny | 69.21 | 78.12 | 83.64 | 84.74 | 84.92 | 84.24 | 81.81 | 80.95 | 5.27 | 6.52 |

Table [5](#S3.T5 "Table 5 ‣ 3.2.2 Robustness to Input Resolution Variation ‣ 3.2 Text Detection ‣ 3 Experiments ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks") shows that PP-OCRv6 is consistently more robust to resolution variation. PP-OCRv6\_medium obtains both the highest mean Hmean (86.67%) and the lowest CV (5.19%), while PP-OCRv6\_small and PP-OCRv6\_tiny also achieve lower CV than the PP-OCRv5 baselines. At the extreme 2.83×\times scale, all PP-OCRv6 models retain over 81% Hmean, clearly outperforming PP-OCRv5\_server (67.28%) and PP-OCRv5\_mobile (65.81%).

## B-e75ac22b82a6ff

https://arxiv.org/html/2606.13108v1#chars-38460-39746

#### 3.3.2 Hallucination Evaluation

A critical advantage of specialized OCR models over VLMs is the absence of text hallucination—generating text not present in the input image. Table [7](#S3.T7 "Table 7 ‣ 3.3.2 Hallucination Evaluation ‣ 3.3 Text Recognition ‣ 3 Experiments ‣ PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks") evaluates this on our curated hallucination benchmark, where accuracy measures the rate of correct outputs without hallucinated content.

|  |  |  |
| --- | --- | --- |
| Type | Model | Accuracy (%) |
| VLMs | Qwen3-VL-235B | 80.56 |
| GPT-5.5 | 78.00 |
| Kimi-K2.6 | 85.00 |
| MiniMax-M3 | 72.60 |
| PP-OCRv6 | PP-OCRv6\_medium | 93.20 |
| PP-OCRv6\_small | 88.20 |
| PP-OCRv6\_tiny | 86.80 |

PP-OCRv6\_medium achieves 93.2% accuracy on the hallucination benchmark, compared to 85.0% for Kimi-K2.6, 80.6% for Qwen3-VL-235B, and 72.6% for MiniMax-M3. This gap reflects a structural difference: PP-OCRv6’s CTC+NRTR decoding architecture produces outputs grounded in visual features, whereas VLMs’ auto-regressive generation may produce plausible but non-existent text. This characteristic is particularly important for data-sensitive applications such as financial documents, medical records, and legal text extraction.

## B-f490e329fda1cf

https://arxiv.org/html/2606.13108v1#chars-51161-52696

### C.1 LCNetV4 Backbone

We isolate the contribution of each backbone design choice by progressively upgrading from PP-OCRv5\_mobile (LCNetV3, scale=0.95) to the final LCNetV4. All models use the same EncoderWithSVTR neck and are trained on a representative subset (approximately 20% of the full training data) for 50 epochs to enable rapid iteration. Recognition accuracy is measured on the in-house benchmark subset.

|  |  |  |
| --- | --- | --- |
| Configuration | Acc. (%) | Δ\Delta |
| LCNetV3 (PP-OCRv5\_mobile baseline) | 76.01 | – |
| + MetaFormer-style block (Token/Channel Mixer separation) | 78.24 | +2.23 |
| + RepDWConv in token mixer | 78.30 | +0.06 |
| + Multi-branch StemBlock | 78.96 | +0.66 |
| + Per-tier depth/width configuration | 79.21 | +0.25 |
| + BN zero-init on channel mixer compress | 79.35 | +0.14 |

The MetaFormer-style decomposition contributes the largest single gain (+2.23%), confirming that separating spatial aggregation from channel interaction yields substantially better representations under the same parameter budget. The multi-branch StemBlock adds +0.66% by providing richer low-level features through parallel MaxPool and convolution paths. RepDWConv contributes a modest +0.06% in accuracy; its primary value is zero-cost inference regularization through the implicit multi-scale ensemble during training. The explicit per-tier depth/width design (+0.25%) and BN zero-init (+0.14%) provide cumulative gains that reflect improved training dynamics for the deeper LCNetV4 configurations.

## B-ocr-0ccbbe2bfbdf2d

B PDF page 11

[tbl-3.html](tbl-3.html)

Table 4 | Text detection Hmean (%) on our in-house benchmark (16 categories). Red and blue cells indicate the best and second-best results per column, respectively.

by 4.6 percentage points, with notable gains on Japanese, ancient text, rotated text, and industrial-character scenarios. PP-OCRv6_small further reaches 84.1% average Hmean and also surpasses PP-OCRv5_server, while PP-OCRv6_tiny obtains 80.6% average Hmean, approaching the server baseline and clearly outperforming PP-OCRv5_mobile.

Compared with VLMs, the PP-OCRv6 detection models show a substantial advantage in precise text localization. PP-OCRv6_medium exceeds the best VLM result, Gemini-3.1-Pro, by 39.4 percentage points (86.2% vs. 46.8%), and even PP-OCRv6_tiny outperforms it by 33.8 percentage points (80.6% vs. 46.8%). Qwen3-VL-235B, Kimi-K2.6, and MiniMax-M3 achieve average Hmean scores of only 38.3%, 12.8%, and 12.0%, respectively. The consistent gap across all evaluated VLMs suggests that accurate text localization remains challenging for current general-purpose VLMs and continues to benefit from specialized OCR architectures.

#### 3.2.2. Robustness to Input Resolution Variation

To evaluate detection robustness under input-resolution perturbations, we construct a scaled validation benchmark by randomly sampling 600 images from the detection validation set and resizing each image using seven scale factors ranging from  \( 0.35\times \)  to  \( 2.83\times \) . The scales form a symmetric geometric progression around the original resolution, with a ratio of  \( \sqrt{2} \)  between adjacent levels, providing approximately uniform sampling in scale space while covering both moderate and substantial resolution variations. Polygon annotations are scaled by the same factor as the image and validated before evaluation. We report Hmean at each tested scale, together with the mean Hmean, standard deviation, and coefficient of variation (CV) across all scales.

Table 5 shows that PP-OCRv6 is consistently more robust to resolution variation. PP-OCRv6_medium obtains both the highest mean Hmean (86.67%) and the lowest CV (5.19%), while PP-OCRv6_small and PP-OCRv6_tiny also achieve lower CV than the PP-OCRv5 baselines. At the extreme 2.83× scale, all PP-OCRv6 models retain over 81% Hmean, clearly outperforming PP-OCRv5_server (67.28%) and PP-OCRv5_mobile (65.81%).

[OCR table id=tbl-3.html; page=11]
<table><tr><td rowspan="3">Model</td><td rowspan="3">AVG</td><td colspan="16">Scenario-specific Hmean (%)</td></tr><tr><td colspan="2">Handwritten</td><td colspan="2">Printed</td><td rowspan="2">TC</td><td rowspan="2">Anc.</td><td rowspan="2">JP</td><td rowspan="2">Blur</td><td rowspan="2">Emo.</td><td rowspan="2">Warp</td><td rowspan="2">Pin.</td><td rowspan="2">Art.</td><td rowspan="2">Tab.</td><td rowspan="2">Rot.</td><td rowspan="2">Indus.</td><td rowspan="2">Gen.</td></tr><tr><td>CN</td><td>EN</td><td>CN</td><td>EN</td></tr><tr><td colspan="18">Vision-Language Models</td></tr><tr><td>Gemini-3.1-Pro</td><td>46.8</td><td>53.4</td><td>56.5</td><td>47.3</td><td>47.6</td><td>39.0</td><td>45.8</td><td>38.2</td><td>50.0</td><td>68.1</td><td>44.6</td><td>40.6</td><td>65.2</td><td>26.9</td><td>22.1</td><td>52.5</td><td>50.2</td></tr><tr><td>GPT-5.5</td><td>45.6</td><td>42.4</td><td>58.5</td><td>50.2</td><td>51.9</td><td>35.0</td><td>26.7</td><td>42.0</td><td>49.1</td><td>97.5</td><td>37.7</td><td>36.3</td><td>52.0</td><td>71.0</td><td>10.0</td><td>36.2</td><td>32.6</td></tr><tr><td>Qwen3-VL-235B</td><td>38.3</td><td>56.5</td><td>66.0</td><td>41.7</td><td>37.0</td><td>19.3</td><td>13.1</td><td>27.0</td><td>38.5</td><td>81.2</td><td>28.5</td><td>33.0</td><td>68.3</td><td>19.6</td><td>2.1</td><td>48.4</td><td>32.3</td></tr><tr><td>Kimi-K2.6</td><td>12.8</td><td>12.5</td><td>25.5</td><td>10.1</td><td>18.5</td><td>8.2</td><td>7.5</td><td>11.2</td><td>16.9</td><td>28.9</td><td>13.9</td><td>6.8</td><td>16.1</td><td>10.9</td><td>0.8</td><td>6.3</td><td>10.9</td></tr><tr><td>MiniMax-M3</td><td>12.0</td><td>13.7</td><td>19.3</td><td>9.8</td><td>14.1</td><td>7.7</td><td>11.1</td><td>10.6</td><td>16.1</td><td>32.8</td><td>12.8</td><td>8.5</td><td>16.6</td><td>5.5</td><td>0.1</td><td>6.4</td><td>6.4</td></tr><tr><td colspan="18">PP-OCRv5</td></tr><tr><td>PP-OCRv5_server</td><td>81.6</td><td>80.3</td><td>84.1</td><td>94.5</td><td>91.7</td><td>81.5</td><td>67.6</td><td>77.2</td><td>90.1</td><td>96.2</td><td>87.6</td><td>67.1</td><td>67.3</td><td>97.1</td><td>80.0</td><td>64.3</td><td>79.7</td></tr><tr><td>PP-OCRv5_mobile</td><td>75.2</td><td>74.4</td><td>77.7</td><td>90.5</td><td>91.0</td><td>82.3</td><td>58.1</td><td>72.7</td><td>87.4</td><td>93.6</td><td>82.7</td><td>57.5</td><td>52.5</td><td>92.8</td><td>64.7</td><td>52.8</td><td>72.1</td></tr><tr><td colspan="18">PP-OCRv6 (Ours)</td></tr><tr><td>PP-OCRv6_medium</td><td>86.2</td><td>83.7</td><td>84.0</td><td>95.1</td><td>93.7</td><td>86.3</td><td>80.2</td><td>84.3</td><td>94.1</td><td>99.6</td><td>88.6</td><td>74.0</td><td>69.0</td><td>96.8</td><td>93.8</td><td>73.3</td><td>82.8</td></tr><tr><td>PP-OCRv6_small</td><td>84.1</td><td>80.5</td><td>87.1</td><td>94.2</td><td>93.6</td><td>85.7</td><td>72.6</td><td>82.3</td><td>92.6</td><td>99.7</td><td>87.6</td><td>69.6</td><td>65.3</td><td>95.6</td><td>93.7</td><td>67.6</td><td>78.2</td></tr><tr><td>PP-OCRv6_tiny</td><td>80.6</td><td>79.4</td><td>85.9</td><td>93.1</td><td>92.3</td><td>83.7</td><td>63.0</td><td>76.6</td><td>89.3</td><td>99.8</td><td>86.1</td><td>59.0</td><td>60.1</td><td>94.7</td><td>91.0</td><td>62.0</td><td>73.8</td></tr></table>

## B-ocr-1ab5e923c9189f

B PDF page 7

![img-3.jpeg](img-3.jpeg)

Figure 4 | PP-OCRv6 text detection architecture. Top: overall pipeline with LCNetV4 backbone, RepLKFPN neck, DB head, and training-only auxiliary DB heads. Bottom: RepLKFPN performs top-down multi-scale fusion and large-kernel per-level refinement before aggregating outputs at 1/4 resolution.

training. At inference, all branches are merged into a single  \( 7 \times 7 \)  depthwise convolution via structural reparameterization [11], incurring no additional branch latency. Table 3 compares the parameter count of the whole FPN neck and the local receptive field of the per-level refinement block.

[tbl-2.html](tbl-2.html)

Table 3 | Parameter comparison of the whole FPN neck (out_channels=96). The RF column denotes the local receptive field of the per-level refinement block.

This design reduces the whole FPN neck parameters from 172K to 118K after reparameterization, while increasing the local RF of the per-level refinement block from  \( 3 \times 3 \)  to  \( 7 \times 7 \) . This provides stronger local context modeling for fused pyramid features and benefits the detection of both large and densely-arranged text.

[OCR table id=tbl-2.html; page=7]
<table><tr><td>Module</td><td>Params</td><td>Per-level refinement block</td><td>Block RF</td></tr><tr><td>RSEFPN</td><td>172K</td><td>3×3 Conv</td><td>3×3</td></tr><tr><td>RepLKFPN (train)</td><td>140K</td><td>DilatedReparamBlock</td><td>7×7</td></tr><tr><td>RepLKFPN (infer)</td><td>118K</td><td>7×7 DWConv</td><td>7×7</td></tr></table>

## B-ocr-2a9281962713e4

B PDF page 20

## C. Ablation Studies

### C.1. LCNetV4 Backbone

We isolate the contribution of each backbone design choice by progressively upgrading from PP-OCRv5_mobile (LCNetV3, scale=0.95) to the final LCNetV4. All models use the same EncoderWithSVTR neck and are trained on a representative subset (approximately 20% of the full training data) for 50 epochs to enable rapid iteration. Recognition accuracy is measured on the in-house benchmark subset.

[tbl-11.html](tbl-11.html)

Table 12 | Backbone ablation on the recognition task. Each row adds one design change to the previous configuration. The neck (EncoderWithSVTR) and decoder are held constant throughout.

The MetaFormer-style decomposition contributes the largest single gain (+2.23%), confirming that separating spatial aggregation from channel interaction yields substantially better representations under the same parameter budget. The multi-branch StemBlock adds +0.66% by providing richer low-level features through parallel MaxPool and convolution paths. RepDWConv contributes a modest +0.06% in accuracy; its primary value is zero-cost inference regularization through the implicit multi-scale ensemble during training. The explicit per-tier depth/width design (+0.25%) and BN zero-init (+0.14%) provide cumulative gains that reflect improved training dynamics for the deeper LCNetV4 configurations.

### C.2. Text Detection

To verify the effectiveness of each proposed strategy, we first conduct ablation experiments on one-fifth of the full detection training data for rapid iteration, starting from the PP-OCRv5_mobile_det baseline. After validating the architecture and loss components under this reduced-data setting, we train the final configuration with the full training data. Results are shown in Table 13.

[tbl-12.html](tbl-12.html)

Table 13 | Ablation study for PP-OCRv6_small text detection. Each row adds one strategy on top of the previous configuration.

As shown in Table 13, upgrading the backbone from LCNetV3 to LCNetV4 brings a signifi-

[OCR table id=tbl-11.html; page=20]
<table><tr><td>Configuration</td><td>Acc. (%)</td><td>\( \Delta \)</td></tr><tr><td>LCNetV3 (PP-OCRv5_mobile baseline)</td><td>76.01</td><td>-</td></tr><tr><td>+ MetaFormer-style block (Token/Channel Mixer separation)</td><td>78.24</td><td>+2.23</td></tr><tr><td>+ RepDWConv in token mixer</td><td>78.30</td><td>+0.06</td></tr><tr><td>+ Multi-branch StemBlock</td><td>78.96</td><td>+0.66</td></tr><tr><td>+ Per-tier depth/width configuration</td><td>79.21</td><td>+0.25</td></tr><tr><td>+ BN zero-init on channel mixer compress</td><td>79.35</td><td>+0.14</td></tr></table>

[OCR table id=tbl-12.html; page=20]
<table><tr><td>Configuration</td><td>Params</td><td>Hmean (%)</td><td>\( \Delta \)</td></tr><tr><td colspan="4">Ablation with 1/5 training data</td></tr><tr><td>Baseline (PP-OCRv5_mobile_det)</td><td>1.19M</td><td>77.84</td><td>-</td></tr><tr><td>+ LCNetV4 Backbone</td><td>2.53M</td><td>79.37</td><td>+1.53</td></tr><tr><td>+ RepLKFPN</td><td>2.48M</td><td>79.75</td><td>+0.38</td></tr><tr><td>+ Auxiliary Deep Supervision</td><td>-</td><td>80.28</td><td>+0.53</td></tr><tr><td>+ Focal Loss</td><td>-</td><td>81.43</td><td>+1.15</td></tr><tr><td>+ Full Data Training</td><td>-</td><td>84.12</td><td>+2.69</td></tr></table>

## B-ocr-2b557c00874b32

B PDF page 23

## E. Hallucination Visualization Comparison with VLMs

Figure 8 presents qualitative examples comparing PP-OCRv6_medium with several VLMs on our hallucination evaluation set. The key observation is that VLMs tend to “correct” what they perceive as spelling or grammatical errors in the source image, producing text that is linguistically plausible but factually inconsistent with the visual input. In contrast, PP-OCRv6_medium faithfully reproduces the exact text content—including deliberate misspellings, non-standard character usage, and repeated characters—without injecting linguistic priors.

This behavior reflects a fundamental architectural difference: PP-OCRv6's CTC+NRTR decoding is grounded in frame-level visual features without auto-regressive language modeling, producing outputs strictly conditioned on the input image. VLMs, by contrast, rely on strong language priors that can override visual evidence when the two conflict.

![img-8.jpeg](img-8.jpeg)

Figure 8 | Hallucination comparison between PP-OCRv6_medium and VLMs. For each example, the input image (left) contains text with non-standard spelling or repeated characters. PP-OCRv6_medium faithfully reproduces the exact visual content (√), while VLMs (MiniMax-M3, GPT-5.5, Qwen3-VL-235B, Kimi-K2.6) modify the text based on linguistic priors (✗), introducing hallucinated corrections not present in the image. Red characters highlight discrepancies from the ground truth.

## B-ocr-33586c8b234a59

B PDF page 9

![img-4.jpeg](img-4.jpeg)

Figure 5 | PP-OCRv6 text recognition architecture. Top: overall recognition pipeline where input passes through LCNetV4 backbone, then LightSVTR neck (medium/small) or Reshape+FC (tiny), feeding into CTC Head for inference and NRTR Head for training. Bottom: comparison between EncoderWithLightSVTR and EncoderWithSVTR.

\( 2C \times C \) projection matrix, which is parameter-heavy (e.g., \( 2 \times 120 \times 120 = 28,800 \) parameters for the mobile model) and provides limited inductive bias about the local structure of text.

We propose EncoderWithLightSVTR (Figure 5) to address both issues simultaneously. The design rests on two observations: (1) text is inherently sequential, so local context along the horizontal axis is complementary to global attention; (2) additive skip connections are sufficient for feature fusion when dimensions match, avoiding the doubled channel width.

Concretely, the input feature map F is first projected by a  \( 1 \times 1 \)  convolution to reduce the channel dimension from C to a smaller D (e.g., D=192 for medium). A depthwise convolution with kernel  \( 1 \times 7 \)  is then applied along the width axis, injecting local positional awareness of neighboring characters before any global interaction occurs. This local-context-first design is motivated by the observation that character boundaries and inter-character spacing are highly informative for recognition, yet purely global attention treats all positions equally. The locally-primed features then pass through L stacked Transformer blocks (MHSA + FFN). Finally, the output is added element-wise to a lightweight  \( 1 \times 1 \)  skip projection of the original input:

\[
\mathbf {y} = \underbrace {\text { TransformerBlock } ^ {L} \left(\mathrm{DWConv} _ {1 \times 7} \left(\operatorname{Conv} _ {1 \times 1} (\mathbf {x})\right)\right)} _ {\text { local   -   global   path }} + \underbrace {\operatorname{Conv} _ {1 \times 1} ^ {\text { skip }} (\mathbf {x})} _ {\text { skip   path }} \tag {4}
\]

The additive fusion costs only  \( C \times D \)  parameters (vs.  \( 2C^{2} \)  for concatenation), and the DWConv adds merely  \( D \times 7 \)  depthwise parameters—negligible overhead. For the medium model we set D=192, L=2, MLP ratio 4.0; for small, D=120, L=2, ratio 2.0.

#### 2.3.2. Tiny Model: Minimalist Design

The tiny recognition model (1.1M params) forgoes the encoder neck entirely. The backbone output  \( (\mathbb{R}^{B\times160\times1\times W}) \)  is directly reshaped and projected to 80 dimensions via a learned linear layer, then fed into the CTC/NRTR decoder heads. To compensate for the reduced model

## B-ocr-3453dd3bf378fc

B PDF page 13

#### 3.3.2. Hallucination Evaluation

A critical advantage of specialized OCR models over VLMs is the absence of text hallucination—generating text not present in the input image. Table 7 evaluates this on our curated hallucination benchmark, where accuracy measures the rate of correct outputs without hallucinated content.

[tbl-6.html](tbl-6.html)

Table 7 | Hallucination evaluation. Higher accuracy indicates less hallucination.

PP-OCRv6_medium achieves 93.2% accuracy on the hallucination benchmark, compared to 85.0% for Kimi-K2.6, 80.6% for Qwen3-VL-235B, and 72.6% for MiniMax-M3. This gap reflects a structural difference: PP-OCRv6's CTC+NRTR decoding architecture produces outputs grounded in visual features, whereas VLMs' auto-regressive generation may produce plausible but non-existent text. This characteristic is particularly important for data-sensitive applications such as financial documents, medical records, and legal text extraction.

#### 3.3.3. Robustness to Crop Margin Variation

In practical OCR pipelines, the text detection module produces bounding boxes with varying margins around the actual text content. Depending on the detection model's behavior and post-processing parameters, the cropped text image may be tightly clipped to the character boundaries or include substantial background padding. A robust recognition model should produce consistent predictions regardless of how much margin surrounds the text. To evaluate this, we measure recognition consistency across different crop margins: for each test sample, we generate multiple crops with progressively looser boundaries and report the percentage of samples that yield identical predictions across all margin settings (Table 8).

[tbl-7.html](tbl-7.html)

Table 8 | Crop margin robustness (%). Higher is better. Measures the percentage of samples with consistent recognition results across varying crop boundaries. PP-OCRv6 demonstrates substantially improved robustness to bounding box variations.

PP-OCRv6_medium achieves 75.32% consistency, a +20.5% improvement over PP-OCRv5_server (54.82%). This improvement suggests that LCNetV4's MetaFormer architecture and LightSVTR's

[OCR table id=tbl-6.html; page=13]
<table><tr><td>Type</td><td>Model</td><td>Accuracy (%)</td></tr><tr><td rowspan="4">VLMs</td><td>Qwen3-VL-235B</td><td>80.56</td></tr><tr><td>GPT-5.5</td><td>78.00</td></tr><tr><td>Kimi-K2.6</td><td>85.00</td></tr><tr><td>MiniMax-M3</td><td>72.60</td></tr><tr><td rowspan="3">PP-OCRv6</td><td>PP-OCRv6_medium</td><td>93.20</td></tr><tr><td>PP-OCRv6_small</td><td>88.20</td></tr><tr><td>PP-OCRv6_tiny</td><td>86.80</td></tr></table>

[OCR table id=tbl-7.html; page=13]
<table><tr><td>Model</td><td>Consistency (%)</td><td>Δ vs. v5</td></tr><tr><td>PP-OCRv3_mobile</td><td>31.05</td><td>-</td></tr><tr><td>PP-OCRv4_server</td><td>45.69</td><td>-</td></tr><tr><td>PP-OCRv4_mobile</td><td>43.41</td><td>-</td></tr><tr><td>PP-OCRv5_server</td><td>54.82</td><td>-</td></tr><tr><td>PP-OCRv5_mobile</td><td>57.74</td><td>-</td></tr><tr><td>PP-OCRv6_medium</td><td>75.32</td><td>+20.5</td></tr><tr><td>PP-OCRv6_small</td><td>67.80</td><td>+10.1</td></tr><tr><td>PP-OCRv6_tiny</td><td>44.80</td><td>-</td></tr></table>

## B-ocr-3d6f7dc4fad57b

B PDF page 21

cant improvement of 1.53% Hmean, indicating improved feature extraction capability of the new backbone. Replacing RSEFPN with RepLKFPN further improves Hmean by 0.38% while slightly reducing model parameters from 2.53M to 2.48M, demonstrating the efficiency of the depthwise-separable large-kernel design. Auxiliary deep supervision and Focal Loss contribute complementary gains of 0.53% and 1.15%, respectively. With the full training data, the final model reaches 84.12% Hmean, improving over the reduced-data configuration by 2.69% and over the PP-OCRv5_mobile_det baseline by 6.28%.

### C.3. Text Recognition

We evaluate the recognition-specific design choices (neck and decoder) on the final LCNetV4 backbone. All experiments use the same training subset and schedule as the backbone ablation above.

[tbl-13.html](tbl-13.html)

Table 14 | Recognition neck and decoder ablation. The backbone (LCNetV4-small) is fixed. Each section varies one component while holding others constant.

Replacing the concatenation-based skip in EncoderWithSVTR with a lightweight additive connection improves accuracy by +0.42% while reducing neck parameters. Adding the DWConv 1×7 local context layer before global attention provides a further +0.47%, confirming that explicit local horizontal modeling is complementary to global self-attention for sequential text features. Removing the neck entirely causes a 4.83% drop, indicating that sequence modeling in the neck is essential for medium/small capacity models.

For the decoder, the multi-head CTC+NRTR design outperforms CTC-only by +1.16%, as the NRTR branch acts as an implicit language model that regularizes the shared encoder during training without adding inference cost. Increasing the NRTR dimension from 384 to 512 for the medium model yields an additional +0.37%.

For the tiny model, CTC logit distillation from the vocabulary-matched medium teacher provides +2.69% accuracy, effectively recovering much of the capacity gap introduced by removing the neck.

[OCR table id=tbl-13.html; page=21]
<table><tr><td>Configuration</td><td>Acc. (%)</td><td>\( \Delta \)</td></tr><tr><td colspan="3">Neck design</td></tr><tr><td>EncoderWithSVTR (PP-OCRv5, concat skip)</td><td>79.35</td><td>-</td></tr><tr><td>EncoderWithLightSVTR (additive skip only)</td><td>79.77</td><td>+0.42</td></tr><tr><td>EncoderWithLightSVTR (+ DWConv 1×7)</td><td>80.24</td><td>+0.89</td></tr><tr><td>No neck (reshape + FC, tiny reference)</td><td>74.52</td><td>-4.83</td></tr><tr><td colspan="3">Decoder configuration (with LightSVTR neck)</td></tr><tr><td>CTC only</td><td>79.08</td><td>-</td></tr><tr><td>CTC + NRTR-384 (multi-head)</td><td>80.24</td><td>+1.16</td></tr><tr><td>CTC + NRTR-512 (medium only)</td><td>80.61</td><td>+1.53</td></tr><tr><td colspan="3">Knowledge distillation (tiny model, no neck)</td></tr><tr><td>Tiny without distillation</td><td>71.83</td><td>-</td></tr><tr><td>Tiny + CTC KL distillation (\( \lambda=1.0 \))</td><td>74.52</td><td>+2.69</td></tr></table>

## B-ocr-67e5044d2ed1a4

B PDF page 15

## References

[1] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. arXiv preprint arXiv:2303.08774, 2023.

[2] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388, 2025.

[3] Yuning Du, Chenxia Li, Ruoyu Guo, Xiaoting Yin, Weiwei Liu, Jun Zhou, Yifan Bai, Zilin Yu, Yehua Yang, Qingqing Dang, et al. Pp-ocr: A practical ultra lightweight ocr system. arXiv preprint arXiv:2009.09941, 2020.

[4] Yuning Du, Chenxia Li, Ruoyu Guo, Cheng Cui, Weiwei Liu, Jun Zhou, Bin Lu, Yehua Yang, Qiwen Liu, Xiaoguang Hu, et al. Pp-ocrv2: Bag of tricks for ultra lightweight ocr system. arXiv preprint arXiv:2109.03144, 2021.

[5] Chenxia Li, Weiwei Liu, Ruoyu Guo, Xiaoting Yin, Kaitao Jiang, Yongkun Du, Yuning Du, Lingfeng Zhu, Baohua Lai, Xiaoguang Hu, et al. Pp-ocrv3: More attempts for the improvement of ultra lightweight ocr system. arXiv preprint arXiv:2206.03001, 2022.

[6] Cheng Cui, Yubo Zhang, Ting Sun, Xueqing Wang, Hongen Liu, Manhui Lin, Yue Zhang, Tingquan Gao, Changda Zhou, Jiaxuan Liu, et al. Pp-ocrv5: A specialized 5m-parameter model rivaling billion-parameter vision-language models on ocr tasks. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 2467–2476, 2026.

[7] Weihao Yu, Mi Luo, Pan Zhou, Chenyang Si, Yichen Zhou, Xinchao Wang, Jiashi Feng, and Shuicheng Yan. Metaformer is actually what you need for vision. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 10819–10829, 2022.

[8] Ao Wang, Hui Chen, Zijia Lin, Jungong Han, and Guiguang Ding. Repvit: Revisiting mobile cnn from vit perspective. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 15909–15920, 2024.

[9] Cheng Cui, Tingquan Gao, Shengyu Wei, Yuning Du, Ruoyu Guo, Shuilong Dong, Bin Lu, Ying Zhou, Xueying Lv, Qiwen Liu, et al. Pp-lcnet: A lightweight cpu convolutional neural network. arXiv preprint arXiv:2109.15099, 2021.

[10] Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zhmoginov, and Liang-Chieh Chen. Mobilenetv2: Inverted residuals and linear bottlenecks. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 4510–4520, 2018.

[11] Xiaohan Ding, Xiangyu Zhang, Ningning Ma, Jungong Han, Guiguang Ding, and Jian Sun. Repvgg: Making vgg-style convnets great again. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 13733–13742, 2021.

[12] Jie Hu, Li Shen, and Gang Sun. Squeeze-and-excitation networks. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 7132–7141, 2018.

[13] Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He, and Piotr Dollár. Focal loss for dense object detection. In Proceedings of the IEEE international conference on computer vision, pages 2980–2988, 2017.

[14] Fausto Milletari, Nassir Navab, and Seyed-Ahmad Ahmadi. V-net: Fully convolutional neural networks for volumetric medical image segmentation. In 2016 fourth international conference on 3D vision (3DV), pages 565–571. Ieee, 2016.

[15] Xiaohan Ding, Yiyuan Zhang, Yixiao Ge, Sijie Zhao, Lin Song, Xiangyu Yue, and Ying Shan. Unireplknet: A universal perception large-kernel convnet for audio video point cloud time-series and image recognition. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 5513–5524, 2024.

## B-ocr-72c354075689a6

B PDF page 28

![img-38.jpeg](img-38.jpeg)

Figure 13 | Qualitative comparison between PP-OCRv6 and PP-OCRv5 (e).

## B-ocr-759242b7ce3742

B PDF page 8

#### 2.2.2. Auxiliary Deep Supervision

In PP-OCRv5_mobile_det, supervision is only applied to the final fused feature map, which means gradient signals must propagate through the entire FPN before reaching the backbone. This can lead to insufficient learning of intermediate features, particularly at deeper scales.

We introduce auxiliary prediction heads  \( [16] \)  at three FPN levels (P2, P3, P4). Each auxiliary head independently predicts the shrink map, threshold map, and binary map using the same head architecture as the main branch. During training, the auxiliary outputs are supervised with the same loss formulation as the main branch (Dice+Focal loss on the shrink map and binary map, L1 loss on the threshold map), weighted by per-scale coefficients ( \( \lambda_{P2} = 0.4 \) ,  \( \lambda_{P3} = 0.3 \) ,  \( \lambda_{P4} = 0.2 \) ). This deep supervision provides stronger gradient signals to intermediate features and acts as a regularizer. At inference, the auxiliary heads are removed, so the model size and speed remain unchanged.

#### 2.2.3. Focal Loss for Per-Pixel Supervision

PP-OCRv5_mobile_det uses only DiceLoss  \( [14] \)  for the probability map supervision. DiceLoss is a set-level metric that computes a single scalar measuring the global overlap between prediction and ground truth—it provides less explicit pixel-wise discrimination between easy and hard samples. Although OHEM  \( [17] \)  is applied, it relies on per-pixel loss ranking to select hard negatives, which may limit the effectiveness of hard-sample mining because the optimization objective is dominated by global region overlap..

To address this, we introduce Focal Loss  \( [13] \)  as an explicit per-pixel supervision signal and combine it with DiceLoss:

\[
\mathcal {L} _ {\text { shrink }} = \lambda_ {\text { dice }} \cdot \mathcal {L} _ {\text { Dice }} + \lambda_ {\text { focal }} \cdot \mathcal {L} _ {\text { Focal }} \tag {3}
\]

where  \( \lambda_{dice} = \lambda_{focal} = 1.0 \) . Focal Loss computes an independent loss value for each pixel via  \( -\alpha_{t}(1 - p_{t})^{\gamma} \log(p_{t}) \) , providing true per-pixel supervision that DiceLoss alone cannot offer. We set  \( \alpha = 0.25 \)  and  \( \gamma = 2.5 \) . The two losses are complementary: DiceLoss optimizes global region overlap, while Focal Loss provides fine-grained per-pixel gradients that adaptively emphasize hard examples, enabling more precise learning at the pixel level.

### 2.3. Text Recognition

The PP-OCRv6 recognition system (Figure 5) adopts a Backbone–Neck–Head pipeline. The LCNetV4 backbone encodes the input text line image  \( (3 \times 48 \times W) \)  into a compact feature map  \( F \in R^{B \times C \times 1 \times W} \) , where the height has been collapsed to 1 by the asymmetric stride design described above. This feature map is then passed to the EncoderWithLightSVTR neck (for medium/small models) or directly reshaped (for tiny), before being decoded by a multi-head architecture combining CTC [18] and NRTR [19]. At inference, only the CTC branch is evaluated for parallel decoding; the NRTR branch participates only during training, functioning as an implicit language model that regularizes the shared encoder representations through auxiliary cross-entropy supervision with label smoothing.

#### 2.3.1. EncoderWithLightSVTR

The recognition neck in PP-OCRv5 (EncoderWithSVTR) applies global self-attention to the feature sequence and then fuses the result with the input via concatenation along the channel axis, followed by a  \( 1 \times 1 \)  projection from 2C back to C. This concatenation-based skip demands a

## B-ocr-79fad21474d61f

B PDF page 4

![img-2.jpeg](img-2.jpeg)

Figure 3 | LCNetV4 backbone architecture. Left: block comparison between LCNetV3Block and LCNetV4Block, along with RepDWConv detail. Right: LCNetV4 in recognition mode and detection mode.

training-time representational capacity without increasing inference cost. A single LCNetV4 implementation serves both text detection and text recognition through task-specific stride configurations (Figure 3), unifying the previously separate backbone families into one codebase.

#### 2.1.1. LCNetV4Block

Following the MetaFormer paradigm, the LCNetV4Block (Figure 3) decomposes each layer into a token mixer followed by a channel mixer. Let  \( x \in R^{C \times H \times W} \)  denote the input feature. The block computes:

\[
\hat {\mathbf {x}} = \operatorname{SE} (\mathrm{DW} (\mathbf {x})) + \mathbf {x} \tag {1}
\]

\[
\mathbf {y} = W _ {2} \sigma (W _ {1} \hat {\mathbf {x}}) + \hat {\mathbf {x}} \tag {2}
\]

where  \( DW(\cdot) \)  is a  \( 3 \times 3 \)  depthwise convolution (the token mixer), SE is an optional squeeze-and-excitation [12] module,  \( W_{1} \in R^{2C \times C} \)  and  \( W_{2} \in R^{C \times 2C} \)  are  \( 1 \times 1 \)  pointwise convolutions forming the channel mixer with expansion ratio 2, and  \( \sigma \)  is GELU. Both stages employ identity shortcuts when the spatial resolution and channel dimension remain unchanged.

This separation has two practical advantages. First, it provides independent design knobs: the token mixer controls the spatial receptive field while the channel mixer controls the per-

## B-ocr-7bc0f3da2cda71

B PDF page 6

[tbl-1.html](tbl-1.html)

Table 2 | LCNetV4 network configurations for detection and recognition. Depth: number of LCNetV4Blocks per stage. Width: channel dimension. Recognition mode uses asymmetric stride (2, 1) in Stage 3–4 to preserve width. Params denotes full model parameters (backbone + neck + head).

stage transition applies standard stride-2 downsampling, producing multi-scale feature maps at strides 4, 8, 16, and 32 for FPN-based processing. In recognition mode, the width dimension must be preserved for sequential CTC/NRTR decoding. We address this by applying asymmetric stride (2, 1) at the Stage 3 and Stage 4 transitions, which halves the height at each step while leaving the width intact. After Stage 4, average pooling along the height axis produces a 1-D feature sequence of shape  \( [B, C, 1, W] \) . This asymmetric stride mechanism is what allows a single backbone to output both 2-D spatial pyramids (for detection) and 1-D sequential features (for recognition). Table 2 summarizes the per-tier configurations for both tasks; Figure 3 illustrates both modes.

### 2.2. Text Detection

In PP-OCRv6, we adopt LCNetV4 as the backbone network for the text detection model. On top of the new backbone, we apply three additional strategies to further improve detection accuracy while maintaining efficiency: (1) RepLKFPN, a lightweight feature pyramid with large receptive field; (2) Auxiliary Deep Supervision for better intermediate feature learning; (3) introducing Focal Loss  \( [13] \)  combined with Dice Loss  \( [14] \)  for per-pixel supervision.

#### 2.2.1. RepLKFPN: Lightweight Large-Kernel Feature Pyramid

The feature pyramid network (FPN) plays a critical role in fusing multi-scale features for text detection. In PP-OCRv5_mobile_det, RSEFPN uses standard 3×3 convolutions with Squeeze-and-Excitation (SE) attention [12] as the output convolution block at each pyramid level. However, these standard convolutions are parameter-heavy, while each block only provides a local 3×3 receptive field.

RepLKFPN keeps the overall top-down FPN fusion structure unchanged and replaces only this per-level refinement block with a depthwise-separable design: a DilatedReparamBlock  \( [15] \)  followed by a  \( 1\times1 \)  pointwise convolution and SE attention. In our implementation, the DilatedReparamBlock uses a  \( 7\times7 \)  depthwise convolution as the main branch, plus three parallel dilated depthwise branches ( \( 5\times5 \)  with dilation 1,  \( 3\times3 \)  with dilation 2, and  \( 3\times3 \)  with dilation 3). These branches enrich the per-level refinement block with multi-scale spatial patterns during

[OCR table id=tbl-1.html; page=6]
<table><tr><td>Task</td><td>Tier</td><td>Stem</td><td>Stage 1</td><td>Stage 2</td><td>Stage 3</td><td>Stage 4</td></tr><tr><td rowspan="3">Det</td><td>Tiny</td><td>Branch(16)</td><td>\( 2 \times 16 \)</td><td>\( 3 \times 32 \)</td><td>\( 5 \times 64 \)</td><td>\( 3 \times 160 \)</td></tr><tr><td>Small</td><td>Branch(48)</td><td>\( 2 \times 48 \)</td><td>\( 3 \times 96 \)</td><td>\( 5 \times 192 \)</td><td>\( 3 \times 384 \)</td></tr><tr><td>Medium</td><td>Branch(128)</td><td>\( 2 \times 128 \)</td><td>\( 3 \times 256 \)</td><td>\( 5 \times 512 \)</td><td>\( 3 \times 896 \)</td></tr><tr><td rowspan="3">Rec</td><td>Tiny</td><td>Simple(48)</td><td>\( 1 \times 48 \)</td><td>\( 1 \times 48 \)</td><td>\( 3 \times 96 \)</td><td>\( 4 \times 160 \)</td></tr><tr><td>Small</td><td>Branch(96)</td><td>\( 1 \times 96 \)</td><td>\( 2 \times 96 \)</td><td>\( 7 \times 192 \)</td><td>\( 3 \times 384 \)</td></tr><tr><td>Medium</td><td>Branch(128)</td><td>\( 1 \times 128 \)</td><td>\( 3 \times 256 \)</td><td>\( 7 \times 512 \)</td><td>\( 3 \times 768 \)</td></tr><tr><td colspan="7">Full model parameters (Det / Rec)</td></tr><tr><td colspan="2">Tiny</td><td>0.43M / 1.1M</td><td colspan="4">(end-to-end: 1.5M)</td></tr><tr><td colspan="2">Small</td><td>2.48M / 5.2M</td><td colspan="4">(end-to-end: 7.7M)</td></tr><tr><td colspan="2">Medium</td><td>15.5M / 19M</td><td colspan="4">(end-to-end: 34.5M)</td></tr></table>

## B-ocr-7c289fe9a5fe5d

B PDF page 10

capacity, we employ knowledge distillation from the medium model. Since the tiny model uses a smaller character dictionary (to reduce output layer size and improve efficiency), we first train a dedicated medium teacher model with the same dictionary as the tiny student, ensuring vocabulary-consistent logit alignment. The teacher is then frozen during distillation. The training objective is:

\[
\mathcal {L} _ {\text {tiny}} = \mathcal {L} _ {\mathrm{CTC}} ^ {\mathrm{GT}} + \mathcal {L} _ {\mathrm{NRTR}} ^ {\mathrm{GT}} + \lambda \cdot \mathcal {L} _ {\mathrm{KL}} ^ {\mathrm{CTC}} \tag {5}
\]

where \(\mathcal{L}_{\mathrm{CTC}}^{\mathrm{GT}}\) and \(\mathcal{L}_{\mathrm{NRTR}}^{\mathrm{GT}}\) are standard ground-truth supervision losses for the CTC and NRTR branches respectively, and \(\mathcal{L}_{\mathrm{KL}}^{\mathrm{CTC}}\) is a KL-divergence loss that aligns the student's CTC output probability distribution with the teacher's:

\[
\mathcal {L} _ {\mathrm{KL}} ^ {\mathrm{CTC}} = \frac {1}{T} \sum_ {t = 1} ^ {T} D _ {\mathrm{KL}} \left(p _ {t} ^ {\text { teacher }} \| p _ {t} ^ {\text { student }}\right) \tag {6}
\]

where  \( p_{t} \)  denotes the per-timestep softmax distribution over the vocabulary. Because teacher and student share the identical dictionary, the CTC logits can be directly aligned without any projection or vocabulary mapping. The NRTR branch, supervised only by ground truth with label smoothing, acts as an auxiliary regularizer during training and is discarded at inference. We set  \( \lambda=1.0 \)  in all experiments.

## 3. Experiments

### 3.1. Experimental Setup

Training Configuration. All models are implemented in PaddlePaddle and trained with Adam optimizer ( \( \beta_{1}=0.9 \) ,  \( \beta_{2}=0.999 \) ) using cosine learning rate schedule with linear warmup. Recognition models are trained for 100 epochs with L2 regularization ( \( 3\times10^{-5} \) ). Detection models are trained for 500 epochs with L2 regularization ( \( 1\times10^{-6} \) ). Multi-scale training with input sizes [320×32, 320×48, 320×64] is used for recognition. Detection uses 640×640 input with CopyPaste augmentation.

Data. PP-OCRv6 inherits the data-centric methodology from PP-OCRv5 [6], training on the curated large-scale dataset constructed through principled difficulty filtering (confidence 0.95–0.97 sweet spot), accuracy verification, and diversity sampling (1000 K-means clusters). To support the expanded scenario coverage, we further augment the training data with both synthetic generation and real-world collection targeting industrial scenes such as digital displays, dot-matrix characters, tire parameters, and power adapter text. This shared data foundation enables fair ablation of the architecture improvements.

### 3.2. Text Detection

#### 3.2.1. Main Results

Table 4 compares detection Hmean on our in-house benchmark covering 16 categories across PP-OCRv6, PP-OCRv5, and state-of-the-art VLMs. Detailed ablation studies validating each individual strategy are provided in Appendix C.2.

PP-OCRv6 consistently improves text detection accuracy over previous PP-OCR models. PP-OCRv6_medium achieves the best average Hmean of 86.2%, outperforming PP-OCRv5_server

## B-ocr-7e503734e8c8e0

B PDF page 14

local-global attention mechanism produce feature representations that are less sensitive to input crop variations. The trend is consistent across the series: v3 (31.05%) → v4 (45.69%) → v5 (54.82%) → v6 (75.32%), showing steady progress with each generation.

### 3.4. End-to-End System Inference Speed

We benchmark the end-to-end OCR pipeline (detection + recognition) on 200 images comprising both general scene and document images. The measurement includes image I/O from disk, preprocessing, model inference, and post-processing. The software environment is PaddlePaddle 3.2.1, ONNX Runtime 1.23.2 (CUDA 12.6), OpenVINO 2025.0, and TensorRT 8.6.1 (CUDA 11.8, paddle2onnx 2.0.2rc3). Results are summarized in Table 9.

[tbl-8.html](tbl-8.html)

Table 9 | End-to-end OCR pipeline inference speed (s/image).

Table 9 reveals several trends. First, PP-OCRv6_medium consistently matches or outperforms PP-OCRv5_server across all tested configurations: 1.1× faster on A100 (0.29s vs. 0.32s), 1.15× on V100 ONNX Runtime (0.67s vs. 0.77s), and 5.2× on Intel Xeon OpenVINO (1.40s vs. 7.30s). Second, PP-OCRv6_small matches PP-OCRv5_mobile in latency on most platforms while delivering higher accuracy; it is 1.9× faster on Apple M4 PaddlePaddle (3.07s vs. 5.82s) and 1.3× on Intel Xeon OpenVINO (0.59s vs. 0.78s). Third, PP-OCRv6_tiny is the fastest model across all platforms, achieving 6.1× speedup over PP-OCRv5_mobile on Apple M4 PaddlePaddle (0.96s vs. 5.82s), 3.9× on Intel Xeon OpenVINO (0.20s vs. 0.78s), and reaching 0.13s on A100. Overall, the depthwise-separable architecture of LCNetV4 translates into favorable latency characteristics particularly on CPU and under optimized inference backends such as OpenVINO.

## 4. Conclusion

We present PP-OCRv6, a lightweight OCR system that advances accuracy through the combination of architectural innovation and data-centric optimization. Experiments demonstrate that PP-OCRv6_medium achieves 83.2% recognition accuracy (+5.1% over PP-OCRv5_server) and 86.2% detection Hmean (+4.6% over PP-OCRv5_server), while PP-OCRv6_tiny (0.43M detection, 1.1M recognition) approaches PP-OCRv5_server in detection and remains competitive for recognition with an order of magnitude fewer parameters. Compared to VLMs, PP-OCRv6 achieves higher accuracy with 6800× fewer parameters and produces substantially lower hallucination rates (93.2% vs. 80.6% for Qwen3-VL-235B). These results confirm that lightweight specialized OCR systems, when equipped with modern architecture designs and curated training data, remain the practical choice for production deployment in the large-model era.

In future work, we plan to release a PP-OCRv6_large model with greater capacity, higher accuracy, and broader language coverage beyond the current 50 languages.

[OCR table id=tbl-8.html; page=14]
<table><tr><td>Hardware</td><td>Backend</td><td>PP-OCRv6_medium</td><td>PP-OCRv6_small</td><td>PP-OCRv6_tiny</td><td>PP-OCRv5_server</td><td>PP-OCRv5_mobile</td><td>PP-OCRv4_mobile</td></tr><tr><td rowspan="2">NVIDIA A100</td><td>PaddlePaddle</td><td>0.29</td><td>0.25</td><td>0.13</td><td>0.32</td><td>0.25</td><td>0.14</td></tr><tr><td>TensorRT</td><td>-</td><td>0.32</td><td>0.16</td><td>-</td><td>0.33</td><td>0.16</td></tr><tr><td rowspan="3">NVIDIA V100</td><td>PaddlePaddle</td><td>0.72</td><td>0.49</td><td>0.21</td><td>0.66</td><td>0.50</td><td>0.25</td></tr><tr><td>ONNX Runtime</td><td>0.67</td><td>0.53</td><td>0.29</td><td>0.77</td><td>0.46</td><td>0.27</td></tr><tr><td>TensorRT</td><td>0.77</td><td>0.60</td><td>0.23</td><td>0.73</td><td>0.59</td><td>0.27</td></tr><tr><td rowspan="3">Intel Xeon 8350C</td><td>PaddlePaddle</td><td>2.05</td><td>0.79</td><td>0.32</td><td>2.04</td><td>0.80</td><td>0.62</td></tr><tr><td>OpenVINO</td><td>1.40</td><td>0.59</td><td>0.20</td><td>7.30</td><td>0.78</td><td>0.60</td></tr><tr><td>ONNX Runtime</td><td>3.31</td><td>0.61</td><td>0.22</td><td>6.36</td><td>0.61</td><td>0.49</td></tr><tr><td rowspan="2">Apple M4</td><td>PaddlePaddle</td><td>8.82</td><td>3.07</td><td>0.96</td><td>&gt;10</td><td>5.82</td><td>5.65</td></tr><tr><td>ONNX Runtime</td><td>5.55</td><td>1.29</td><td>0.35</td><td>7.20</td><td>1.10</td><td>1.02</td></tr></table>

## B-ocr-86ffc8d9746c4f

B PDF page 29

![img-39.jpeg](img-39.jpeg)

![img-40.jpeg](img-40.jpeg)

![img-41.jpeg](img-41.jpeg)

![img-42.jpeg](img-42.jpeg)

![img-43.jpeg](img-43.jpeg)

![img-44.jpeg](img-44.jpeg)

![img-45.jpeg](img-45.jpeg)

![img-46.jpeg](img-46.jpeg)

![img-47.jpeg](img-47.jpeg)

![img-48.jpeg](img-48.jpeg)

![img-49.jpeg](img-49.jpeg)

![img-50.jpeg](img-50.jpeg)

Figure 14 | Qualitative comparison between PP-OCRv6 and PP-OCRv5 (f).

## B-ocr-8bcb37e2436066

B PDF page 1

# PP-OCRv6: From 1.5M to 34.5M Parameters, Surpassing Billion-Scale VLMs on OCR Tasks

Yubo Zhang, Xueqing Wang, Manhui Lin, Yue Zhang, Penglongyi Deng, Ting Sun, Tingquan Gao, Zelun Zhang, Jiaxuan Liu, Changda Zhou, Hongen Liu, Suyin Liang, Cheng Cui \( ^{†} \) , Yi Liu, Dianhai Yu, Yanjun Ma

PaddlePaddle Team, Baidu Inc.

\( ^{\dagger} \) Project Leader

paddleocr@baidu.com

Official Website: https://www.paddleocr.com

Source Code: https://github.com/PaddlePaddle/PaddleOCR

Models: https://huggingface.co/PaddlePaddle

## Abstract

Vision-Language Models (VLMs) have achieved impressive results on general vision-language tasks, yet they suffer from hallucination, imprecise localization, and prohibitive computational cost when applied to dedicated OCR scenarios. This paper presents PP-OCRv6, a lightweight OCR system that combines architectural innovation with data-centric optimization. PP-OCRv6 redesigns the backbone, detection neck, and recognition neck around a unified MetaFormer-style building block with structural reparameterization, decoupling spatial token mixing from channel mixing and supporting both tasks through task-specific stride configurations. Three model tiers (medium, small, tiny) share the same block primitives, covering deployment scenarios from server to edge. On our in-house benchmarks, PP-OCRv6_medium achieves 83.2% recognition accuracy and 86.2% detection Hmean, outperforming PP-OCRv5_server by +5.1% and +4.6% respectively while surpassing Qwen3-VL-235B, GPT-5.5, and Gemini-3.1-Pro with orders of magnitude fewer parameters. The tiny tier achieves 3.9× faster inference than PP-OCRv5_mobile on Intel Xeon CPU while maintaining comparable accuracy.

![img-0.jpeg](img-0.jpeg)

Figure 1 | Performance comparison between PP-OCRv6, PP-OCRv5, and Vision-Language Models. Left: text detection average Hmean (%) on our in-house benchmark. Right: text recognition weighted average accuracy (%) on the recognition benchmark.

arXiv:2606.13108v1 [cs.CV] 11 Jun 2026

## B-ocr-974fecff8e41e3

B PDF page 27

![img-37.jpeg](img-37.jpeg)

Figure 12 | Qualitative comparison between PP-OCRv6 and PP-OCRv5 (d).

## B-ocr-9ab2c9aadf4951

B PDF page 25

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)

![img-12.jpeg](img-12.jpeg)

![img-13.jpeg](img-13.jpeg)

![img-14.jpeg](img-14.jpeg)

![img-15.jpeg](img-15.jpeg)

![img-16.jpeg](img-16.jpeg)

![img-17.jpeg](img-17.jpeg)

![img-18.jpeg](img-18.jpeg)

![img-19.jpeg](img-19.jpeg)

![img-20.jpeg](img-20.jpeg)

![img-21.jpeg](img-21.jpeg)

![img-22.jpeg](img-22.jpeg)

![img-23.jpeg](img-23.jpeg)

![img-24.jpeg](img-24.jpeg)

Figure 10 | Qualitative comparison between PP-OCRv6 and PP-OCRv5 (b).

## B-ocr-a1cfe373c4f8e0

B PDF page 16

[16] Chen-Yu Lee, Saining Xie, Patrick Gallagher, Zhengyou Zhang, and Zhuowen Tu. Deeply-supervised nets. In Artificial intelligence and statistics, pages 562–570. Pmlr, 2015.

[17] Abhinav Shrivastava, Abhinav Gupta, and Ross Girshick. Training region-based object detectors with online hard example mining. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 761–769, 2016.

[18] Wenyang Hu, Xiaocong Cai, Jun Hou, Shuai Yi, and Zhiping Lin. Gtc: Guided training of ctc towards efficient and accurate scene text recognition. In Proceedings of the AAAI conference on artificial intelligence, volume 34, pages 11005–11012, 2020.

[19] Fenfen Sheng, Zhineng Chen, and Bo Xu. Nrtr: A no-recurrence sequence-to-sequence model for scene text recognition. In 2019 International conference on document analysis and recognition (ICDAR), pages 781–786. IEEE, 2019.

## B-ocr-a26e73c72a193e

B PDF page 3

![img-1.jpeg](img-1.jpeg)

Figure 2 | Overview of the PP-OCRv6 system. The pipeline consists of text detection and text recognition, both built on the unified LCNetV4 backbone. Three model variants (medium, small, tiny) share the same block primitives with different depth/width configurations.

and (iii) EncoderWithLightSVTR, a recognition neck powered by local-global attention and additive skip connections.

3. Extensive Multi-Language and Scenario Generalization: We scale the unified model to support 50 languages and a wide range of challenging industrial scenes (e.g., digital displays, dot-matrix characters, and tire prints). This significantly enhances OCR performance in specialized scenarios that are traditionally underserved by general-purpose visual-language models.

These results provide compelling evidence that lightweight, specialized OCR systems—when equipped with modern architecture designs and high-quality training data—offer a practical and effective alternative for production OCR deployment in the large-model era.

## 2. Improvement Strategies

This section presents the key technical improvements in PP-OCRv6. We first describe LCNetV4, the unified backbone (Section 2.1), then detail detection-specific (Section 2.2) and recognition-specific (Section 2.3) improvements.

### 2.1. LCNetV4: MetaFormer-Style Lightweight Backbone

PP-OCRv5 employs two separate backbone families: PPHGNetV2 for the server model and LCNetV3  \( [9] \)  for the mobile model. This dual-architecture design increases engineering complexity in training, deployment, and maintenance. LCNetV3 follows the MobileNet-style  \( [10] \)  convention in which depthwise convolution, squeeze-and-excitation, and pointwise convolution are stacked sequentially without explicit functional decomposition. This design conflates spatial aggregation and cross-channel interaction into a single monolithic block, limiting the flexibility to optimize each operation independently.

The MetaFormer  \( [7] \)  framework offers an alternative perspective: an effective architecture can be decomposed into a token mixer for spatial feature aggregation and a channel mixer for per-position feature transformation. RepViT  \( [8] \)  validated this decomposition on lightweight CNNs, showing consistent accuracy gains over MobileNet-style baselines at comparable computational budgets.

Building on these findings, we design LCNetV4 around an explicit token mixer / channel mixer decomposition, augmented with structural reparameterization  \( [11] \)  to enrich the

## B-ocr-b0136516de9800

B PDF page 22

### D. Qualitative Analysis of Text Detection

Figure 7 presents qualitative detection results across four representative challenging scenarios. We compare PP-OCRv6_medium with PP-OCRv5_server and two state-of-the-art VLMs (Gemini-3.1-Pro and GPT-5.5).

![img-7.jpeg](img-7.jpeg)

Figure 7 | Qualitative comparison of text detection results. Columns from left to right: PP-OCRv6_medium, PP-OCRv5_server, Gemini-3.1-Pro, and GPT-5.5. Colored polygons indicate detected text regions.

The four rows cover curved text on a tire surface, dense small text on an electronic display, artistic/decorative fonts, and business cards, respectively. PP-OCRv6_medium consistently produces complete and accurate polygon detections across all scenarios. For the curved tire text, PP-OCRv5 misses several text instances, while both VLMs produce overly tight bounding boxes that fail to cover the full text extent. In the electronic display scene, PP-OCRv5 misses some text elements, Gemini-3.1-Pro fails to detect small-sized characters, and GPT-5.5 generates false positives by enclosing non-text regions such as icons and symbols. For the artistic font scene, both PP-OCRv5 and Gemini-3.1-Pro miss text instances. In the business card scene, PP-OCRv5 exhibits missed detections, Gemini-3.1-Pro produces misaligned bounding boxes that do not correspond to the actual text positions, and GPT-5.5 uses axis-aligned boxes that poorly fit the oriented text lines.

These visualizations illustrate the different failure modes of each approach: PP-OCRv5 primarily suffers from missed detections in challenging scenarios, while VLMs exhibit inaccurate localization—either producing overly tight boxes, misaligned regions, or false positives on non-text content. These observations are consistent with the quantitative gaps in Table 4.

## B-ocr-b2eceee161ae2e

B PDF page 19

## B. Speed Comparison of Text Detection Models

We further evaluate the inference speed of PP-OCRv6 and PP-OCRv5 text detection models using the PaddleX Inference Benchmark platform. The benchmark is conducted on a server equipped with Intel Xeon Gold 6271C CPUs and NVIDIA Tesla V100-SXM2-32GB GPUs. GPU latency is measured with the Paddle inference backend, while CPU ONNX latency is measured with the PaddleX ONNX Runtime backend.

For each exported detection model, the platform runs batch-size-one inference on square inputs from 512 to 2048 pixels. All latency numbers are averaged over 30 measured iterations after 15 warm-up iterations. Since the benchmark records latency only, this section analyzes inference speed rather than accuracy.

![img-5.jpeg](img-5.jpeg)

(a) GPU inference.

![img-6.jpeg](img-6.jpeg)

(b) CPU ONNX inference.

Figure 6 | Inference time comparison of PP-OCRv6 and PP-OCRv5 text detection models under different input resolutions.

As shown in Figure 6, PP-OCRv6_medium is consistently faster than PP-OCRv5_server under both backends. At the 2048 input resolution, PP-OCRv6_medium takes 106.89 ms on GPU compared with 253.52 ms for PP-OCRv5_server, corresponding to a 2.37× speedup. Under CPU ONNX inference, PP-OCRv6_medium takes 2327.23 ms compared with 3034.93 ms for PP-OCRv5_server, yielding a 1.30× speedup.

The lighter PP-OCRv6 tiers provide different speed-capacity trade-offs. PP-OCRv6_small is close to PP-OCRv5_mobile in GPU latency at 2048 resolution (42.70 ms vs. 37.36 ms) and is slightly faster under CPU ONNX inference (654.25 ms vs. 687.98 ms). PP-OCRv6_tiny achieves the lowest CPU ONNX latency among all compared models, reaching 317.06 ms at 2048 resolution. On GPU, however, the tiny model is not always faster than the small model; for example, at 1024 resolution PP-OCRv6_small takes 12.48 ms while PP-OCRv6_tiny takes 12.83 ms. This indicates that practical GPU latency is affected not only by model size, but also by operator fusion, parallelism, kernel scheduling, and hardware utilization.

Across both backends, increasing the input resolution from 512 to 2048 leads to a monotonic increase in latency for all models, and the gap between model tiers becomes more pronounced at high resolution. The PP-OCRv5_server model shows the steepest growth, while the PP-OCRv6 family maintains a more favorable speed-capacity balance across resolutions.

## B-ocr-b585fc35e99ae2

B PDF page 2

## 1. Introduction

The field of computer vision is increasingly dominated by large-scale models, particularly Vision-Language Models (VLMs), which have demonstrated impressive generalist capabilities across a wide range of tasks  \( [1, 2] \) . This trend of scaling model size has naturally extended to OCR, with modern VLM-based approaches promising an end-to-end solution for extracting text from complex, real-world images. While the performance of these large models is academically remarkable, the prevailing focus on scale often encounters significant practical limitations when deployed in real-world OCR scenarios, which demand not only high recognition accuracy but also precision, reliability, and efficiency.

A primary challenge arises from the “generalist’s dilemma.” Unified VLM architectures, although designed for diverse tasks, often lack the specialized capabilities needed for high-precision OCR. This manifests in three critical limitations: (1) Imprecise Localization: These models often fail to produce the tight, accurate bounding boxes essential for document analysis. (2) Hallucination: In complex layouts, models can confidently generate plausible yet incorrect text, presenting a critical vulnerability for data-sensitive applications. (3) Computational Inefficiency: Massive parameter counts render these models impractical for deployment in resource-constrained environments or for services demanding high-throughput, low-latency processing.

These challenges naturally steer the focus back towards lightweight, specialized OCR systems. PaddleOCR  \( [3] \)  has established a strong track record in this direction, evolving through PP-OCRv2  \( [4] \) , PP-OCRv3  \( [5] \) , PP-OCRv4, and PP-OCRv5  \( [6] \) . The PP-OCR series has explored two complementary directions for improving accuracy. On the architecture side, PP-OCRv3 introduced SVTR-LCNet and LK-PAN, while PP-OCRv4 adopted PPHGNetV2 and LCNetV3 as server and mobile backbones respectively. On the data side, PP-OCRv5 inherited the PP-OCRv4 architecture and focused on systematic data curation along three dimensions: difficulty, accuracy, and diversity. PP-OCRv5 demonstrated that with sufficient high-quality data, the performance ceiling of a 5M-parameter model is far higher than commonly assumed.

In this work, we present PP-OCRv6, which combines both directions. While inheriting PP-OCRv5's proven data curation methodology, PP-OCRv6 introduces a fundamentally redesigned model architecture. We observe that under the same data regime, the existing backbone designs (HGNetV2 for server, LCNetV3 for mobile) have reached their structural capacity. Specifically, the MobileNet-style DW→SE→PW block in LCNetV3 does not exploit modern lightweight design principles such as the MetaFormer paradigm  \( [7, 8] \) ; the dense  \( 9 \times 9 \)  convolutions in LKPAN can be replaced by efficient reparameterizable alternatives with equivalent receptive fields; and the dual-architecture approach (separate backbone families for server and mobile) increases engineering complexity unnecessarily.

Our main contributions are summarized as follows:

1. Unified and Scalable Model Family: We deliver a comprehensive, three-tier OCR model family spanning 1.5M to 34.5M parameters. The medium-tier model achieves an 86.2% detection H-mean and 83.2% recognition accuracy, serving as a highly efficient, production-ready infrastructure for both industrial deployment and large-scale data pipelines.
2. Tailored Lightweight Architectural Innovations: We introduce a suite of lightweight architectural components custom-designed for OCR tasks. Specifically, we propose: (i) LCNetV4, a MetaFormer-style lightweight backbone integrated with structural reparameterization; (ii) RepLKFPN(Reparameterizable Large-Kernel Feature Pyramid Network), a detection neck leveraging dilated reparameterizable depthwise convolutions for large-scale receptive fields;

## B-ocr-cb570a3ffe4e25

B PDF page 18

Latin-script benchmarks (Table 11). PP-OCRv6_medium achieves 88.4% on the English benchmark and 88.0% on the Latin benchmark, outperforming both PP-OCRv5's language-specific models (en_PP-OCRv5_mobile: 86.0%, latin_PP-OCRv5_mobile: 81.4%) and the PP-OCRv5 main models (server: 79.5%, mobile: 78.3% on English) while using a single unified model rather than separate per-language models.

[tbl-10.html](tbl-10.html)

Table 11 | Recognition accuracy (%) on English and Latin-script evaluation benchmarks. PP-OCRv6 uses a single unified model for all languages, while PP-OCRv5 requires separate language-specific models for optimal English/Latin performance.

[OCR table id=tbl-10.html; page=18]
<table><tr><td>Model</td><td>English (%)</td><td>Latin (%)</td></tr><tr><td>PP-OCRv5_server</td><td>79.5</td><td>-</td></tr><tr><td>PP-OCRv5_mobile</td><td>78.3</td><td>-</td></tr><tr><td>en_PP-OCRv5_mobile</td><td>86.0</td><td>-</td></tr><tr><td>latin_PP-OCRv5_mobile</td><td>77.8</td><td>81.4</td></tr><tr><td>PP-OCRv6_medium</td><td>88.4</td><td>88.0</td></tr><tr><td>PP-OCRv6_small</td><td>86.3</td><td>84.0</td></tr><tr><td>PP-OCRv6_tiny</td><td>77.3</td><td>63.8</td></tr></table>

## B-ocr-d024aa5d34eb20

B PDF page 24

## F. Qualitative Comparison with PP-OCRv5

Figures 9–14 present side-by-side end-to-end OCR results comparing PP-OCRv6_medium and PP-OCRv5_server across diverse real-world scenarios, covering Chinese, English, Japanese, artistic fonts, industrial characters, rotated text, pinyin, dot-matrix characters, special characters, and general scenes. Each figure shows the input image alongside the detection and recognition outputs of both systems.

![img-9.jpeg](img-9.jpeg)

Figure 9 | Qualitative comparison between PP-OCRv6 and PP-OCRv5 (a).

## B-ocr-d41684a0e20db0

B PDF page 26

![img-25.jpeg](img-25.jpeg)

![img-26.jpeg](img-26.jpeg)

![img-27.jpeg](img-27.jpeg)

![img-28.jpeg](img-28.jpeg)

![img-29.jpeg](img-29.jpeg)

![img-30.jpeg](img-30.jpeg)

![img-31.jpeg](img-31.jpeg)

![img-32.jpeg](img-32.jpeg)

![img-33.jpeg](img-33.jpeg)

![img-34.jpeg](img-34.jpeg)

![img-35.jpeg](img-35.jpeg)

![img-36.jpeg](img-36.jpeg)

Figure 11 | Qualitative comparison between PP-OCRv6 and PP-OCRv5 (c).

## B-ocr-e680e7358441c1

B PDF page 17

## Appendix

### A. Language Support

Table 10 compares language coverage across PP-OCR versions. PP-OCRv3/v4 support only Simplified Chinese and English; PP-OCRv5 adds Traditional Chinese and Japanese; PP-OCRv6 medium/small further incorporate 46 Latin-script languages by adding approximately 200 diacritical characters to the dictionary. The tiny model omits Japanese to avoid the ~4,000 Kanji/Kana entries that would disproportionately enlarge its 1.1M-parameter output layer.

[tbl-9.html](tbl-9.html)

Table 10 | Language support comparison across PP-OCR recognition models. “# Lang” indicates the total number of languages supported by a single unified model.

To validate the multilingual capability, we evaluate PP-OCRv6 on dedicated English and

[OCR table id=tbl-9.html; page=17]
<table><tr><td>Model</td><td># Lang</td><td>Supported Languages</td></tr><tr><td>PP-OCRv3_mobile_rec</td><td>2</td><td>Simplified Chinese, English</td></tr><tr><td>PP-OCRv4_mobile_rec</td><td>2</td><td>Simplified Chinese, English</td></tr><tr><td>PP-OCRv4_server_rec</td><td>2</td><td>Simplified Chinese, English</td></tr><tr><td>PP-OCRv5_server_rec</td><td>4</td><td>Simplified Chinese, Traditional Chinese, English, Japanese</td></tr><tr><td>PP-OCRv5_mobile_rec</td><td>4</td><td>Simplified Chinese, Traditional Chinese, English, Japanese</td></tr><tr><td>PP-OCRv6_medium_rec</td><td>50</td><td>Simplified Chinese, Traditional Chinese, English, Japanese, French, German, Italian, Spanish, Portuguese, Dutch, Polish, Romanian, Czech, Swedish, Norwegian, Danish, Finnish, Hungarian, Turkish, Vietnamese, Indonesian, Malay, Azerbaijani, Afrikaans, Bosnian, Croatian, Welsh, Estonian, Irish, Icelandic, Kurdish, Lithuanian, Latvian, Maltese, Maori, Occitan, Slovak, Slovenian, Albanian, Swahili, Tagalog, Uzbek, Latin, Serbian (Latin), Catalan, Basque, Galician, Luxembourgish, Romansh, Quechua</td></tr><tr><td>PP-OCRv6_small_rec</td><td>50</td><td>Simplified Chinese, Traditional Chinese, English, Japanese, French, German, Italian, Spanish, Portuguese, Dutch, Polish, Romanian, Czech, Swedish, Norwegian, Danish, Finnish, Hungarian, Turkish, Vietnamese, Indonesian, Malay, Azerbaijani, Afrikaans, Bosnian, Croatian, Welsh, Estonian, Irish, Icelandic, Kurdish, Lithuanian, Latvian, Maltese, Maori, Occitan, Slovak, Slovenian, Albanian, Swahili, Tagalog, Uzbek, Latin, Serbian (Latin), Catalan, Basque, Galician, Luxembourgish, Romansh, Quechua</td></tr><tr><td>PP-OCRv6_tiny_rec</td><td>49</td><td>Simplified Chinese, Traditional Chinese, English, French, German, Italian, Spanish, Portuguese, Dutch, Polish, Romanian, Czech, Swedish, Norwegian, Danish, Finnish, Hungarian, Turkish, Vietnamese, Indonesian, Malay, Azerbaijani, Afrikaans, Bosnian, Croatian, Welsh, Estonian, Irish, Icelandic, Kurdish, Lithuanian, Latvian, Maltese, Maori, Occitan, Slovak, Slovenian, Albanian, Swahili, Tagalog, Uzbek, Latin, Serbian (Latin), Catalan, Basque, Galician, Luxembourgish, Romansh, Quechua</td></tr></table>

## B-ocr-ee69501f60dded

B PDF page 5

[tbl-0.html](tbl-0.html)

Table 1 | Block design comparison between LCNetV3 and LCNetV4.

position representational capacity, and the two can be tuned without mutual interference. Second, it enables targeted application of structural reparameterization to the token mixer alone, as discussed below.

Reparameterization of the token mixer. The token mixer in Eq. (1) performs depthwise convolution followed by a residual addition. As shown by RepVGG [11], any convolution with an identity shortcut can be augmented with additional parallel branches during training and then merged into a single convolution at inference via algebraic equivalence. We apply this insight to the depthwise layer: during training, we maintain a  \( 3 \times 3 \)  DW branch, a  \( 1 \times 1 \)  DW branch, and a batch-normalized identity branch, all summed before a shared BN layer. At inference, the three branches are fused into one  \( 3 \times 3 \)  DW convolution by zero-padding the  \( 1 \times 1 \)  kernel and the identity to  \( 3 \times 3 \), then summing the weight tensors. This introduces zero additional inference cost while providing a richer optimization landscape during training through the implicit ensemble of different-scale receptive fields.

We do not apply reparameterization to the channel mixer because  \( 1 \times 1 \)  convolutions already operate with maximal parameter efficiency per FLOP (every parameter contributes a unique cross-channel interaction) and lack spatial extent, so multi-branch augmentation offers negligible benefit. This asymmetric use of reparameterization, applying it to the spatial DW layer but not the  \( 1 \times 1 \)  layers, follows the same design principle as RepViT [8].

Comparison with LCNetV3. Table 1 summarizes the architectural differences. The original MobileNetV3 block in LCNetV3 places the  \( 1 \times 1 \)  expansion before the DW convolution, coupling token mixing and channel mixing into an inseparable sequence. By contrast, LCNetV4Block moves the DW convolution to the front and applies the  \( 1 \times 1 \)  expand-compress pair as a standalone residual channel mixer. This enables both the use of structural reparameterization on the DW layer and the BN zero-initialization on the compress layer (which makes each block behave as identity at the start of training, stabilizing convergence for deeper configurations).

#### 2.1.2. Network Architecture and Scaling

LCNetV4 is designed to serve both text detection and text recognition within a single codebase, differentiated only by stride configuration and output interface. Unlike LCNetV3, which applies a uniform scale factor to resize all channels simultaneously, LCNetV4 adopts explicit per-tier configurations with independently tuned depth and width at each stage (Table 2).

The two task modes differ in their spatial processing strategy. In detection mode, each

[OCR table id=tbl-0.html; page=5]
<table><tr><td>Design Aspect</td><td>LCNetV3</td><td>LCNetV4 (Ours)</td></tr><tr><td>Architecture Paradigm</td><td>MobileNet-style (DW→SE→PW)</td><td>MetaFormer (TokenMixer + ChannelMixer)</td></tr><tr><td>Channel Interaction</td><td>Single 1×1 PW Conv</td><td>Expand(2×)→Act→Compress + residual connection</td></tr><tr><td>Spatial Mixing</td><td>Plain DW Conv</td><td>RepDWConv (3-branch) (3×3 + 1×1 + identity)</td></tr><tr><td>BN Initialization</td><td>Standard</td><td>Zero-init on compress BN</td></tr><tr><td>Scaling Strategy</td><td>Uniform scale factor</td><td>Per-tier depth/width config</td></tr></table>

## B-ocr-f628c1854e11c9

B PDF page 12

[tbl-4.html](tbl-4.html)

Table 5 | Resolution robustness of text detection models. Hmean and Mean are higher-is-better, while Std. ↓ and CV ↓ are lower-is-better. Red and blue cells indicate the best and second-best results per column, respectively.

### 3.3. Text Recognition

#### 3.3.1. Main Results

Table 6 compares recognition accuracy on our in-house benchmark (15 categories) across PP-OCRv6, PP-OCRv5, and state-of-the-art VLMs.

[tbl-5.html](tbl-5.html)

Table 6 | Text recognition accuracy (%) on our in-house benchmark (15 categories). Red and blue cells indicate the best and second-best results per column, respectively.

Abbreviations: CN: Chinese, EN: English, TC: Traditional Chinese, Anc.: Ancient Text, JP: Japanese, Conf.: Confusable Characters, Spec.: Special Characters, Gen.: General Scenes, Pin.: Pinyin, Art.: Artistic Text, Indus.: Industrial Characters, Screen: Screen Displays, Card: Physical Card Surfaces.

PP-OCRv6_medium achieves 83.2% weighted average, outperforming PP-OCRv5_server by +5.1% absolute with fewer parameters. The gains are particularly pronounced on categories requiring strong multilingual and contextual understanding: Japanese (+16.8%), Ancient text (+12.0%), and Screen displays (+14.4%). PP-OCRv6_small (5.2M) surpasses PP-OCRv5_server (21M) by +3.2% with 4× fewer parameters, demonstrating the architectural efficiency of LC-NetV4.

Compared to VLMs, the performance gap is substantial. The best-performing VLM (Qwen3-VL-235B, 74.9%) trails PP-OCRv6_medium by 8.3%, despite having approximately 6800× more parameters. Even PP-OCRv6_tiny (1.1M) exceeds four of the five VLMs in weighted average, trailing only Qwen3-VL-235B by 1.4%. VLMs exhibit particularly poor performance on low-resource categories such as Ancient text (Gemini: 18.0%, MiniMax: 2.2%) and Handwritten Chinese (GPT-5.5: 19.2%), indicating that these categories require specialized supervision.

[OCR table id=tbl-4.html; page=12]
<table><tr><td>Model</td><td>0.35×</td><td>0.50×</td><td>0.71×</td><td>1.00×</td><td>1.41×</td><td>2.00×</td><td>2.83×</td><td>Mean ↑</td><td>Std. ↓</td><td>CV ↓ (%)</td></tr><tr><td>PP-OCRv4_server</td><td>55.76</td><td>69.75</td><td>71.32</td><td>73.30</td><td>73.42</td><td>68.39</td><td>57.09</td><td>67.00</td><td>6.91</td><td>10.31</td></tr><tr><td>PP-OCRv4_mobile</td><td>48.53</td><td>65.51</td><td>68.38</td><td>68.56</td><td>69.73</td><td>68.56</td><td>64.65</td><td>64.84</td><td>6.87</td><td>10.60</td></tr><tr><td>PP-OCRv5_server</td><td>74.70</td><td>82.37</td><td>86.30</td><td>85.88</td><td>84.17</td><td>79.13</td><td>67.28</td><td>79.98</td><td>6.41</td><td>8.02</td></tr><tr><td>PP-OCRv5_mobile</td><td>66.94</td><td>73.59</td><td>79.20</td><td>81.50</td><td>80.77</td><td>75.39</td><td>65.81</td><td>74.74</td><td>5.91</td><td>7.90</td></tr><tr><td>PP-OCRv6_medium</td><td>76.29</td><td>85.00</td><td>89.04</td><td>89.72</td><td>89.69</td><td>89.04</td><td>87.94</td><td>86.67</td><td>4.50</td><td>5.19</td></tr><tr><td>PP-OCRv6_small</td><td>71.86</td><td>81.12</td><td>86.35</td><td>88.52</td><td>88.65</td><td>87.75</td><td>86.52</td><td>84.40</td><td>5.64</td><td>6.68</td></tr><tr><td>PP-OCRv6_tiny</td><td>69.21</td><td>78.12</td><td>83.64</td><td>84.74</td><td>84.92</td><td>84.24</td><td>81.81</td><td>80.95</td><td>5.27</td><td>6.52</td></tr></table>

[OCR table id=tbl-5.html; page=12]
<table><tr><td rowspan="3">Model</td><td rowspan="3">W-Avg</td><td colspan="15">Scenario-specific Accuracy (%)</td></tr><tr><td colspan="2">Handwritten</td><td colspan="2">Printed</td><td rowspan="2">TC</td><td rowspan="2">Anc.</td><td rowspan="2">JP</td><td rowspan="2">Conf.</td><td rowspan="2">Spec.</td><td rowspan="2">Gen.</td><td rowspan="2">Pin.</td><td rowspan="2">Art.</td><td rowspan="2">Indus.</td><td rowspan="2">Screen</td><td rowspan="2">Card</td></tr><tr><td>CN</td><td>EN</td><td>CN</td><td>EN</td></tr><tr><td colspan="17">Vision-Language Models</td></tr><tr><td>GPT-5.5</td><td>64.2</td><td>19.2</td><td>56.9</td><td>75.7</td><td>82.2</td><td>57.5</td><td>63.7</td><td>58.6</td><td>49.1</td><td>48.3</td><td>67.7</td><td>50.4</td><td>53.0</td><td>62.4</td><td>67.7</td><td>71.1</td></tr><tr><td>Qwen3-VL-235B</td><td>74.9</td><td>49.7</td><td>73.2</td><td>82.3</td><td>86.2</td><td>76.4</td><td>33.6</td><td>66.2</td><td>56.1</td><td>49.0</td><td>82.5</td><td>76.5</td><td>69.6</td><td>74.7</td><td>73.8</td><td>78.7</td></tr><tr><td>Kimi-K2.6</td><td>62.9</td><td>31.0</td><td>58.4</td><td>76.8</td><td>80.9</td><td>62.7</td><td>16.5</td><td>54.1</td><td>43.5</td><td>38.0</td><td>68.0</td><td>45.2</td><td>59.9</td><td>57.1</td><td>58.4</td><td>68.4</td></tr><tr><td>MiniMax-M3</td><td>54.1</td><td>15.5</td><td>60.3</td><td>63.5</td><td>81.5</td><td>53.2</td><td>2.2</td><td>43.7</td><td>42.2</td><td>42.8</td><td>53.8</td><td>50.3</td><td>44.3</td><td>44.1</td><td>56.6</td><td>67.0</td></tr><tr><td>Gemini-3.1-Pro</td><td>71.4</td><td>46.4</td><td>73.0</td><td>80.0</td><td>90.5</td><td>69.5</td><td>18.0</td><td>67.2</td><td>54.4</td><td>50.3</td><td>74.6</td><td>75.9</td><td>63.1</td><td>69.1</td><td>73.2</td><td>75.9</td></tr><tr><td colspan="17">PP-OCRv5 Series</td></tr><tr><td>PP-OCRv5_server</td><td>78.1</td><td>58.0</td><td>59.6</td><td>90.1</td><td>85.1</td><td>74.7</td><td>60.4</td><td>73.7</td><td>59.4</td><td>56.8</td><td>86.5</td><td>74.4</td><td>64.0</td><td>70.2</td><td>68.1</td><td>87.6</td></tr><tr><td>PP-OCRv5_mobile</td><td>73.7</td><td>41.7</td><td>50.9</td><td>86.0</td><td>86.0</td><td>72.0</td><td>57.8</td><td>75.8</td><td>55.7</td><td>54.8</td><td>80.7</td><td>72.5</td><td>54.0</td><td>59.3</td><td>57.6</td><td>81.7</td></tr><tr><td colspan="17">PP-OCRv6 (Ours)</td></tr><tr><td>PP-OCRv6_medium</td><td>83.2</td><td>62.1</td><td>67.8</td><td>91.5</td><td>94.1</td><td>78.6</td><td>72.4</td><td>90.5</td><td>64.9</td><td>61.7</td><td>87.5</td><td>78.1</td><td>71.2</td><td>77.4</td><td>82.5</td><td>88.1</td></tr><tr><td>PP-OCRv6_small</td><td>81.3</td><td>57.6</td><td>61.1</td><td>90.5</td><td>93.3</td><td>77.0</td><td>71.1</td><td>88.2</td><td>64.1</td><td>60.2</td><td>85.7</td><td>75.9</td><td>68.4</td><td>76.4</td><td>79.7</td><td>86.9</td></tr><tr><td>PP-OCRv6_tiny</td><td>73.5</td><td>40.1</td><td>39.3</td><td>86.7</td><td>88.4</td><td>65.0</td><td>68.4</td><td>89.8</td><td>52.3</td><td>57.1</td><td>78.0</td><td>65.4</td><td>54.7</td><td>62.1</td><td>71.2</td><td>80.5</td></tr></table>
