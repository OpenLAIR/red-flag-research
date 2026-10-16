# Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling

## B-012c1ebce39eb7

https://arxiv.org/html/2511.16301v1#chars-17682-18256

#### Why it generalizes.

Unlike feed-forward upsamplers that require dataset-level training [[6](#bib.bib20), [22](#bib.bib21), [10](#bib.bib22), [3](#bib.bib23), [23](#bib.bib24)],
Upsample Anything learns only per-image, pixel-wise mixing weights from the HR guidance through a test-time optimization process, and reuses these weights to splat Fl​rF\_{lr} into Fh​rF\_{hr}.
Because the mechanism is based on edge- and range-aware interpolation rather than value synthesis,
Upsample Anything is inherently *resolution-free, model-agnostic*, and robust to unseen domains.

## B-079c8749fe3f85

https://arxiv.org/html/2511.16301v1#chars-56369-57051

#### Implementation note.

In practice we adopt ([12](#S13.E12 "Equation 12 ‣ Theorem 2 (Specialization of GSJBU to JBU (isotropic limit)). ‣ Connection to standard 2D GS. ‣ 13 Formal Relation Between Joint Bilateral Upsampling and Gaussian Splatting ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")) with test-time optimization of (Σq,σr​(q))(\Sigma\_{q},\sigma\_{r}(q)).
For stability, Σq≻0\Sigma\_{q}\succ 0 is parameterized via R⁡(θq)​diag​(σx2​(q),σy2​(q))​R​(θq)⊤R(\theta\_{q})\mathrm{diag}(\sigma\_{x}^{2}(q),\sigma\_{y}^{2}(q))R(\theta\_{q})^{\!\top} with σx,σy>0\sigma\_{x},\sigma\_{y}{>}0.

![Refer to caption](2511.16301v1/vis_noise.png)

## B-085785f827c108

https://arxiv.org/html/2511.16301v1#chars-32514-34643

#### Why Upsample Anything: Design Motivation and Comparative Analysis

In our architecture search, we aimed to achieve accurate upsampling within one second while maintaining generalization across domains.
 [Tab. 5](#S5.T5 "In Why Upsample Anything: Design Motivation and Comparative Analysis ‣ 5.5 Ablation Study ‣ 5 Experiments ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling") compares different upsampling strategies on PASCAL-VOC and NYUv2 benchmarks. Guided Linear Upsampling (GLU) [[21](#bib.bib32)] represents a strong bilateral-filter-based baseline but exhibits unstable optimization due to its unconstrained formulation.
We also implemented a 2D Gaussian Splatting (2DGS) [[9](#bib.bib28)] baseline by directly optimizing Gaussian kernels for low-to-high feature interpolation without hierarchical fitting.
Although 2DGS can model local structures continuously, its dense Gaussian representation and lack of spatial–range constraints make it computationally heavy and prone to over-smoothing during test-time optimization.
In contrast, Upsample Anything inherits the spatial–range constraint of classical JBU while leveraging the continuous Gaussian formulation for differentiable optimization.
As shown in  [Tab. 5](#S5.T5 "In Why Upsample Anything: Design Motivation and Comparative Analysis ‣ 5.5 Ablation Study ‣ 5 Experiments ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling") Upsample Anything achieves the best balance between speed, convergence, and accuracy, demonstrating that the JBU constraint synergizes effectively with Gaussian optimization for fast and stable test-time refinement.

| Method | Time (s) | PASCAL-VOC (Segmentation) | | NYUv2 (Depth Estimation) | |
| --- | --- | --- | --- | --- | --- |
| mIoU (↑) | Acc. (↑) | RMSE (↓) | δ1\delta\_{1} (↑) |
| Bilinear | 0.00009 | 81.27 | 95.96 | 0.545 | 0.804 |
| Guided Linear Upsample | 0.00303 | 80.12 | 94.73 | 0.598 | 0.773 |
| JBU | 0.00600 | 81.65 | 96.21 | 0.531 | 0.812 |
| LIG | 481.526 | 78.54 | 93.02 | 0.642 | 0.741 |
| GSJBU (Ours) | 0.4197 | 82.22 | 96.90 | 0.498 | 0.829 |

## B-0b2f8a235f3a93

https://arxiv.org/html/2511.16301v1#chars-7345-8997

### 2.1 Joint Bilateral Upsampling

Joint Bilateral Upsampling (JBU), first introduced by [[14](#bib.bib26)], is a classic non-learning, edge-preserving upsampling technique designed to transfer structural details from a high-resolution guidance image to a low-resolution signal such as a depth map or label map.
Formally, JBU computes each high-resolution output pixel F^​h​r​[p]\hat{F}{hr}[p] as a weighted average of nearby low-resolution pixels F​l​r​[q]F{lr}[q], as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^h​r​[p]=1Zp​∑q∈Ω⁡(p)Fl​r​[q]​exp⁡(−‖p−q‖22​σs2)​exp⁡(−‖I⁡[p]−I⁡[q]‖22​σr2),\hat{F}\_{hr}[p]=\frac{1}{Z\_{p}}\sum\_{q\in\Omega(p)}F\_{lr}[q]\exp\!\left(-\frac{\|p-q\|^{2}}{2\sigma\_{s}^{2}}\right)\exp\!\left(-\frac{\|I[p]-I[q]\|^{2}}{2\sigma\_{r}^{2}}\right), |  | (1) |

where II denotes the high-resolution guidance image, and σs\sigma\_{s}, σr\sigma\_{r} control the spatial and range sensitivity, respectively.
Here, ZpZ\_{p} is a normalization factor ensuring that all weights sum to one, and Ω⁡(p)\Omega(p) denotes the spatial neighborhood around pixel pp in the low-resolution domain.
By coupling spatial proximity and color similarity, JBU preserves edges and fine details while interpolating missing information, enabling high-quality restoration of dense signals without any additional learning.
This formulation has inspired numerous modern variants and learnable extensions that generalize bilateral filtering [[6](#bib.bib20)] to feature space and neural representations.
Although JBU performs upsampling without any training, the resulting quality remains limited due to its fixed, hand-crafted kernel design.

## B-0f5dc469d3023a

https://arxiv.org/html/2511.16301v1#chars-34643-35847

#### Impact of Test-Time Optimization Steps

We conducted experiments to investigate the trade-off between the number of TTO iterations, inference time, and performance.
Table [6](#S5.T6 "Table 6 ‣ Impact of Test-Time Optimization Steps ‣ 5.5 Ablation Study ‣ 5 Experiments ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling") summarizes the results.
We measured PSNR between Il​rI\_{lr} and I^h​r\hat{I}\_{hr}, along with downstream segmentation performance on PASCAL-VOC.
As shown, PSNR quickly converges to 35.60 after about 500 iterations, indicating that Upsample Anything reaches its optimum very early.
Interestingly, the best segmentation accuracy is achieved at only 50 iterations, which also provides the fastest inference time (0.419s).
Based on this observation, we adopt 50 iterations as the default setting throughout all experiments.

| Iteration | PSNR (↑) | PASCAL-VOC (Segmentation) | | Time (s) |
| --- | --- | --- | --- | --- |
| mIoU (↑) | Acc. (↑) |
| 50 | 35.33 | 82.22 | 96.90 | 0.041 |
| 300 | 35.59 | 82.10 | 96.84 | 3.397 |
| 500 | 35.60 | 82.15 | 96.88 | 6.161 |
| 1000 | 35.60 | 82.10 | 96.82 | 12.294 |
| 5000 | 35.60 | 82.17 | 96.80 | 61.458 |

## B-20cb25d1704c81

https://arxiv.org/html/2511.16301v1#chars-20801-22141

### 5.2 Implementation Details

Our Upsample Anything is implemented purely in PyTorch without any chunked or patch-wise processing.
All computations are performed in a fully parallel manner over the entire high-resolution grid.
Gaussian parameters are initialized as σx=σy=16.0\sigma\_{x}=\sigma\_{y}=16.0, σr=0.12\sigma\_{r}=0.12, and θ=0\theta=0,
and are optimized per-pixel using the Adam optimizer with a learning rate of 1×10−31\times 10^{-3}.
The model performs test-time optimization for only 50 iterations in total, without any batching or data augmentation.
Please refer to the supplementary material for additional implementation details, hyperparameter choices, and ablations.

| Method | COCO | | PASCAL-VOC | | ADE20k | |
| --- | --- | --- | --- | --- | --- | --- |
| mIoU (↑\uparrow) | Acc. (↑\uparrow) | mIoU (↑\uparrow) | Acc. (↑\uparrow) | mIoU (↑\uparrow) | Acc. (↑\uparrow) |
| Bilinear | 60.43 | 80.18 | 81.27 | 95.96 | 41.48 | 74.95 |
| FeatUp | 60.96 | 80.65 | 81.91 | 96.27 | 41.92 | 75.41 |
| LoftUp | 61.08 | 80.72 | 81.84 | 96.33 | 41.83 | 75.36 |
| JAFAR | 60.87 | 80.51 | 82.05 | 96.21 | 41.74 | 75.22 |
| AnyUp | 61.25 | 80.89 | 82.18 | 96.39 | 42.02 | 75.63 |
| Upsample Anything | 61.41 | 81.34 | 82.22 | 96.90 | 42.95 | 76.52 |
| Upsample Anything (prob.) | 63.40 | 83.73 | 84.57 | 97.42 | 44.29 | 78.58 |

## B-2a87860db24977

https://arxiv.org/html/2511.16301v1#chars-10467-10487

## 3 Preliminaries

## B-306e0f5716a999

https://arxiv.org/html/2511.16301v1#chars-38620-39531

## 8 Details of Probabilistic Map Upsampling in Table 1.

Figure [8](#S8.F8 "Figure 8 ‣ 8 Details of Probabilistic Map Upsampling in Table 1. ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")-(c) corresponds to the Upsample Anything (prob.) configuration reported in Table 1.
In this setting, the segmentation map is predicted from downsampled features using a lightweight 1×1 convolution, followed by our probabilistic upsampling to reconstruct high-resolution outputs.
This simple setup already shows strong performance.
Because the computation is performed on a small feature map, heavier or more complex decoders are expected to be feasible without large computational overhead.
This suggests that the proposed segmentation pipeline has further potential, although designing such decoders is beyond the scope of this work.

![Refer to caption](2511.16301v1/seg_pipeline.png)

## B-4cf90167e61113

https://arxiv.org/html/2511.16301v1#chars-0-209

##### Report GitHub Issue

Content selection saved. Describe the issue below:

![](/static/base/1.0.1/images/icons/smileybones-small.svg)
![arXiv logo](/static/base/1.0.1/images/arxiv-logo-primary-light.svg)

## B-4e22ff6995e2ee

https://arxiv.org/html/2511.16301v1#chars-54877-56369

#### Consequences.

(i) *Equivalence in the joint domain* (Thm. [1](#Thmtheorem1 "Theorem 1 (JBU as a normalized Gaussian mixture in the joint domain). ‣ Notation. ‣ 13 Formal Relation Between Joint Bilateral Upsampling and Gaussian Splatting ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")) shows that JBU is a GS evaluation on (x,I⁡(x))(x,I(x)) with block-diagonal covariance.
(ii) *Anisotropic generalization* ([12](#S13.E12 "Equation 12 ‣ Theorem 2 (Specialization of GSJBU to JBU (isotropic limit)). ‣ Connection to standard 2D GS. ‣ 13 Formal Relation Between Joint Bilateral Upsampling and Gaussian Splatting ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")) recovers JBU in the isotropic limit (Thm. [2](#Thmtheorem2 "Theorem 2 (Specialization of GSJBU to JBU (isotropic limit)). ‣ Connection to standard 2D GS. ‣ 13 Formal Relation Between Joint Bilateral Upsampling and Gaussian Splatting ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")), and enables per-center covariance learning (our GSJBU).
(iii) *Discrete-to-continuous consistency* (Prop. [1](#Thmproposition1 "Proposition 1 (Discrete-to-continuous convergence). ‣ Connection to standard 2D GS. ‣ 13 Formal Relation Between Joint Bilateral Upsampling and Gaussian Splatting ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")) justifies replacing sums by integrals when refining the sampling grid.

## B-4ebfaac4742137

https://arxiv.org/html/2511.16301v1#chars-289-1559

###### Abstract

We present Upsample Anything, a lightweight test-time optimization (TTO) framework that restores low-resolution features to high-resolution, pixel-wise outputs without any training.
Although Vision Foundation Models demonstrate strong generalization across diverse downstream tasks, their representations are typically downsampled by 14×/16× (e.g., ViT), which limits their direct use in pixel-level applications.
Existing feature upsampling approaches depend on dataset-specific retraining or heavy implicit optimization, restricting scalability and generalization.
Upsample Anything addresses these issues through a simple per-image optimization that learns an anisotropic Gaussian kernel combining spatial and range cues, effectively bridging Gaussian Splatting and Joint Bilateral Upsampling.
The learned kernel acts as a universal, edge-aware operator that transfers seamlessly across architectures and modalities, enabling precise high-resolution reconstruction of features, depth, or probability maps.
It runs in only ≈0.419​s\approx 0.419\text{s} per 224×224 image and achieves state-of-the-art performance on semantic segmentation, depth estimation, and both depth and probability map upsampling.

![Refer to caption](2511.16301v1/teaser.png)

## B-51dc990108307f

https://arxiv.org/html/2511.16301v1#chars-44190-44906

## 13 Formal Relation Between Joint Bilateral Upsampling and Gaussian Splatting

The purpose of this section is not to claim that Joint Bilateral Upsampling (JBU) and Gaussian Splatting (GS) are mathematically equivalent.
Instead, we aim to show why the GS framework provides a useful foundation for our formulation.
By reinterpreting JBU through the perspective of GS, we reveal a common idea based on continuous and differentiable Gaussian kernels, which motivates our use of GS-style parameter learning in the Upsample Anything (GSJBU) framework.
In short, this section clarifies the conceptual link between the two views and explains why GS-based test-time optimization naturally applies to feature upsampling.

## B-526c2dc096ca4a

https://arxiv.org/html/2511.16301v1#chars-29277-30422

#### Feature Similarity Analysis.

[Fig. 7](#S5.F7 "In Feature Similarity Analysis. ‣ 5.4 Qualitative results ‣ 5 Experiments ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling") visualizes the feature similarity between two different images that share the same object category.
This setting is often adopted in few-shot segmentation tasks to assess the consistency of feature representations.
As shown in the figure, both AnyUp and Upsample Anything produce visually plausible feature upsampling results; however, when measuring cosine similarity, AnyUp tends to yield uniformly high similarity across the entire image, indicating a lack of spatial discrimination.
In contrast, our Upsample Anything produces sharper and more localized similarity maps,
where object boundaries are clearly preserved and distinct regions are well separated.
We believe that such discriminative feature behavior suggests the potential of our method for downstream tasks such as few-shot segmentation and category-level feature matching.

![Refer to caption](2511.16301v1/vis_backbone.png)
![Refer to caption](2511.16301v1/cossim.png)

## B-579a10402978ee

https://arxiv.org/html/2511.16301v1#chars-53157-53757

###### Proof.

Substitute Σq=σs2​I2\Sigma\_{q}=\sigma\_{s}^{2}I\_{2} and σr​(q)=σr\sigma\_{r}(q)=\sigma\_{r} into ([12](#S13.E12 "Equation 12 ‣ Theorem 2 (Specialization of GSJBU to JBU (isotropic limit)). ‣ Connection to standard 2D GS. ‣ 13 Formal Relation Between Joint Bilateral Upsampling and Gaussian Splatting ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")) to recover the numerator/denominator of ([1](#S2.E1 "Equation 1 ‣ 2.1 Joint Bilateral Upsampling ‣ 2 Related Works ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")).
∎

## B-5b314f97815dba

https://arxiv.org/html/2511.16301v1#chars-17152-17682

#### Feature rendering (no value synthesis).

Given low-resolution features Fl​r∈ℝC×Hl×WlF\_{lr}\in\mathbb{R}^{C\times H\_{l}\times W\_{l}} and scale ss, we render the HR feature Fh​r∈ℝC×(s​Hl)×(s​Wl)F\_{hr}\in\mathbb{R}^{C\times(sH\_{l})\times(sW\_{l})} by *pure mixing*:

|  |  |  |
| --- | --- | --- |
|  | Fh​r​(p)=∑q∈Ω⁡(p)wp←q​Fl​r​(q).F\_{hr}(p)\;=\;\sum\_{q\in\Omega(p)}w\_{p\leftarrow q}\;F\_{lr}(q). |  |

This strictly reweights existing LR features (no content generation), hence transfers across backbones and tasks.

## B-5ce47559a2e15d

https://arxiv.org/html/2511.16301v1#chars-14746-15391

### 4.2 Algorithm Design

Our design is inspired by classical Joint Bilateral Upsampling (JBU) [[14](#bib.bib26)].
The key merit of JBU is *transferability*: it does not hallucinate new values but instead *learns mixing weights* that decide how much to blend neighboring samples, which makes it naturally model-/task-agnostic.
However, standard JBU in  [Eq. 1](#S2.E1 "In 2.1 Joint Bilateral Upsampling ‣ 2 Related Works ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling") is limited by *global* (σs,σr)(\sigma\_{s},\sigma\_{r}) and *isotropic* range/spatial kernels, reducing expressivity near complex structures.

## B-65f7d37018c8fc

https://arxiv.org/html/2511.16301v1#chars-42152-43219

## 11 Gaussian Blob Visualization

To better understand what our learned anisotropic kernels capture, we visualized the Gaussian blobs of our model, as shown in Fig. [10](#S10.F10 "Figure 10 ‣ 10 From 2D Low-Resolution Feature Maps to 3D High-Resolution Feature Volumes ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling").
(a) shows the original high-resolution RGB image, and (b) overlays the learned Gaussian blobs on the corresponding low-resolution image.
Although the visualization can be difficult to interpret directly, certain spatial regions such as the eyes, nose, and corners exhibit overlapping or consistently oriented blobs, which suggests that nearby kernels capture semantically similar local structures.
This indicates that the learned kernels adaptively encode meaningful directional features rather than behaving randomly.
However, similar to other methods that rely on Gaussian Splatting or 2DGS, not every blob is fully interpretable, and some visual noise appears due to overparameterization and kernel redundancy.

## B-66305e777fa252

https://arxiv.org/html/2511.16301v1#chars-1559-7325

## 1 Introduction

![Refer to caption](2511.16301v1/teaser2.png)

Modern computer vision systems for pixel-level prediction tasks such as semantic, instance, and panoptic segmentation [[5](#bib.bib1), [15](#bib.bib3), [2](#bib.bib2), [30](#bib.bib4)] or depth estimation [[20](#bib.bib5), [26](#bib.bib6), [11](#bib.bib7)] often use an encoder–decoder paradigm.
The encoder extracts hierarchical features that capture semantic abstraction from the input image, and the decoder reconstructs dense, task-specific predictions such as class maps, depth, or optical flow at the original spatial resolution.

Recent advances in large-scale self-supervised learning [[1](#bib.bib8), [17](#bib.bib9), [7](#bib.bib10), [31](#bib.bib11), [18](#bib.bib12), [27](#bib.bib13)] introduce general-purpose encoders called Vision Foundation Models (VFMs) that can serve as universal backbones across diverse downstream tasks.
This paradigm shift has led to the emergence of Vision Foundation Models (VFMs) such as DINO [[17](#bib.bib9)], CLIP [[18](#bib.bib12)], SigLIP [[27](#bib.bib13)], and MAE [[7](#bib.bib10)], which provide transferable and semantically rich features with minimal task-specific fine-tuning.

By decoupling the encoder from the downstream task, these foundation models dramatically reduce the data and training costs needed for adaptation while maintaining strong generalization across domains.
However, despite these advantages, high-performing pixel-level systems still require large and complex decoders such as DPT [[19](#bib.bib14)], UPerNet [[24](#bib.bib15)], or SegFormer [[25](#bib.bib16)] to recover spatial details from low-resolution features.
Foundation features are typically downsampled by a factor of 14-16 in Vision Transformer [[4](#bib.bib17)] architectures or equivalently through multiple pooling stages in CNN-based backbones [[16](#bib.bib18), [8](#bib.bib19)].
As a result, they lack fine-grained spatial information, forcing decoders to rely on heavy upsampling networks that are computationally expensive, memory-intensive, and often difficult to generalize to new architectures or resolutions.

To address this resolution gap, a growing line of research has explored feature upsampling methods [[6](#bib.bib20), [22](#bib.bib21), [10](#bib.bib22), [3](#bib.bib23), [23](#bib.bib24)] to restore spatial details in pretrained representations without modifying the encoder.
These methods learn an upsampling operator that maps low-resolution foundation features to higher resolutions, effectively bridging the semantic–spatial gap before the downstream decoder.
In doing so, they can achieve strong performance across diverse pixel-level tasks even with a single 1×1 convolutional decoder.

Feature upsampling approaches can be broadly categorized into two paradigms depending on how the upsampler is optimized: (a) dataset-level training [[6](#bib.bib20), [22](#bib.bib21), [10](#bib.bib22), [3](#bib.bib23), [23](#bib.bib24)] and (b) test-time optimization (TTO) [[6](#bib.bib20)], as illustrated in  [Fig. 2](#S1.F2 "In 1 Introduction ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling").
In the dataset-level training paradigm, the feature upsampler is trained on a target dataset either by generating pseudo-labels using methods such as SAM [[13](#bib.bib25)] for zero-shot supervision [[10](#bib.bib22)] or by adopting multi-view training objectives [[6](#bib.bib20), [22](#bib.bib21), [3](#bib.bib23), [23](#bib.bib24)].

While this approach can generalize to certain unseen data, it still requires dataset-level training, meaning that the upsampler must be retrained whenever the backbone architecture or target dataset changes.
Moreover, due to heavy memory usage, most trained upsamplers can only operate up to 112–224 pixels in resolution.
The test-time optimization paradigm, exemplified by methods such as FeatUp (Implicit), avoids dataset-level training by optimizing the feature upsampler directly at inference time for each test image.
Although this removes the need for offline training, the per-image optimization is computationally expensive, taking an average of 49 seconds to converge for a 224-sized image.

We propose Upsample Anything, a test-time optimization (TTO) framework for feature upsampling, as illustrated in [Fig. 2](#S1.F2 "In 1 Introduction ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")-(b).
Unlike previous methods requiring dataset-level training, it performs lightweight per-image optimization and processes a 224-sized image in only ≈\approx 0.419 s.
Given an input image, Upsample Anything resizes the RGB guidance to match the low-resolution (LR) feature-map size, reconstructs the high-resolution (HR) color image through optimization, and learns pixelwise anisotropic Gaussian parameters—(σx,σy,θ,σr)(\sigma\_{x},\sigma\_{y},\theta,\sigma\_{r})—that define a continuous spatial–range splatting kernel.
These optimized kernels are then applied to the LR feature maps from a foundation encoder to produce HR feature maps aligned with the original image grid.
Although the optimization is guided only by color reconstruction, the learned kernels implicitly capture geometry and semantics.
As a result, Upsample Anything not only enhances 2D feature resolution but also generalizes to other pixel- or voxel-level signals (e.g., depth, segmentation, or even 3D representations) without retraining.
This property highlights its potential as a unified, lightweight, and resolution-free upsampling operator across 2D and 3D domains.
Despite requiring no dataset-level training, it consistently achieves state-of-the-art or near-SOTA performance on multiple pixel-level benchmarks, including semantic segmentation and depth estimation.

## B-6fe9fd22cabcd7

https://arxiv.org/html/2511.16301v1#chars-22141-22171

### 5.3 quantitative results

## B-70948f5069e277

https://arxiv.org/html/2511.16301v1#chars-50429-53157

###### Theorem 2 (Specialization of GSJBU to JBU (isotropic limit)).

Consider the anisotropic per-center model:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | F⁡(p)\displaystyle F(p) | =∑qfq​exp⁡(−12​(p−q)⊤​Σq−1​(p−q))​βq​(p)∑qexp⁡(−12​(p−q)⊤​Σq−1​(p−q))​βq​(p),\displaystyle=\frac{\sum\limits\_{q}f\_{q}\,\exp\!\big(-\tfrac{1}{2}(p-q)^{\!\top}\Sigma\_{q}^{-1}(p-q)\big)\,\beta\_{q}(p)}{\sum\limits\_{q}\exp\!\big(-\tfrac{1}{2}(p-q)^{\!\top}\Sigma\_{q}^{-1}(p-q)\big)\,\beta\_{q}(p)}, |  | (12) |
|  | βq​(p)\displaystyle\beta\_{q}(p) | :=exp⁡(−‖I⁡(p)−I⁡(q)‖22​σr2​(q)).\displaystyle:=\exp\!\big(-\tfrac{\|I(p)-I(q)\|^{2}}{2\sigma\_{r}^{2}(q)}\big). |  |

If Σq→σs2​I2\Sigma\_{q}\to\sigma\_{s}^{2}I\_{2} and σr​(q)→σr\sigma\_{r}(q)\to\sigma\_{r} for all qq, then ([12](#S13.E12 "Equation 12 ‣ Theorem 2 (Specialization of GSJBU to JBU (isotropic limit)). ‣ Connection to standard 2D GS. ‣ 13 Formal Relation Between Joint Bilateral Upsampling and Gaussian Splatting ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")) reduces exactly to JBU ([1](#S2.E1 "Equation 1 ‣ 2.1 Joint Bilateral Upsampling ‣ 2 Related Works ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Parameter | Symbol | Default | Role | Rationale |
| Spatial sigma (x) | σx\sigma\_{x} | init=scale\text{init}=\text{scale} (e.g., 16) | Controls major-axis smoothing; receptive-field size | Initialized proportional to upsampling factor to provide a wide prior; refined by TTO. |
| Spatial sigma (y) | σy\sigma\_{y} | Same as σx\sigma\_{x} | Controls minor-axis smoothing | Same reasoning as σx\sigma\_{x}; enables anisotropy to emerge during TTO. |
| Orientation | θ\theta | 00 | Rotation of the anisotropic Gaussian | Zero-init avoids directional bias; TTO discovers optimal orientation. |
| Range sigma | σr\sigma\_{r} | 0.120.12 | Sensitivity to appearance/color similarity | Moderate color differences (Δ​I≈0.2∼0.3\Delta I\approx 0.2\sim 0.3) are significantly downweighted; acts as soft bilateral prior. |
| Support radius (max) | RmaxR\_{\max} | 4​–​84\text{--}8 | Upper bound on spatial Gaussian support | Balances context capture and cost (𝒪⁡((2​Rmax+1)2)\mathcal{O}((2R\_{\max}+1)^{2})); too small truncates optimal kernels. |
| Dynamic multiplier | αdyn\alpha\_{\mathrm{dyn}} | 2.02.0 | Converts σeff\sigma\_{\mathrm{eff}} to effective support radius | Ensures coverage of ∼95%\sim 95\% Gaussian mass (2​σ2\sigma rule); prevents under-coverage early in TTO. |
| Center mode | – | nearest | Determines LR anchor for each HR pixel | Nearest-center alignment improves stability and avoids aliasing for large upsampling factors. |

## B-75ab03311369c6

https://arxiv.org/html/2511.16301v1#chars-48214-49185

###### Corollary 1 (Discrete GS view in the joint domain).

Let μq:=ϕ⁡(q)\mu\_{q}:=\phi(q) and fq:=Flr​(q)f\_{q}:=F\_{\mathrm{lr}}(q).
Then Theorem [1](#Thmtheorem1 "Theorem 1 (JBU as a normalized Gaussian mixture in the joint domain). ‣ Notation. ‣ 13 Formal Relation Between Joint Bilateral Upsampling and Gaussian Splatting ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling") states that JBU equals

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^hr​(p)=∑qfq​exp⁡(−12​(ϕ⁡(p)−μq)⊤​Λ−1​(ϕ⁡(p)−μq))∑qexp⁡(−12​(ϕ⁡(p)−μq)⊤​Λ−1​(ϕ⁡(p)−μq)),\small\hat{F}\_{\mathrm{hr}}(p)=\frac{\sum\limits\_{q}f\_{q}\,\exp\!\big(-\tfrac{1}{2}(\phi(p)-\mu\_{q})^{\!\top}\Lambda^{-1}(\phi(p)-\mu\_{q})\big)}{\sum\limits\_{q}\exp\!\big(-\tfrac{1}{2}(\phi(p)-\mu\_{q})^{\!\top}\Lambda^{-1}(\phi(p)-\mu\_{q})\big)}, |  | (10) |

i.e., a *Gaussian Splatting* evaluation in ℝ2+d\mathbb{R}^{2+d} with fixed block-diagonal covariance and centers on the lifted LR grid.

## B-7b59eff887b5b6

https://arxiv.org/html/2511.16301v1#chars-22171-24662

#### Semantic Segmentation.

For a fair comparison, we adopt the conventional linear-probe protocol in which prior work fine-tunes only a 1×11{\times}1 convolutional head for 10 epochs. However, we found that this shallow schedule often under-trains the head. We therefore extend training to 100 epochs and apply a cosine learning-rate schedule to gradually decay the head’s learning rate. Under this setting, our results in Table [1](#S5.T1 "Table 1 ‣ 5.2 Implementation Details ‣ 5 Experiments ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling") show a trend that differs from previous reports [[6](#bib.bib20), [22](#bib.bib21), [10](#bib.bib22), [3](#bib.bib23), [23](#bib.bib24)]: although all methods converge quickly, their eventual gains over simple bilinear upsampling are modest when the backbone representation is strong.
This raises the question of how much feature upsampling helps semantic segmentation under high-capacity backbones.
Nevertheless, our proposed Upsample Anything attains the best accuracy across COCO, PASCAL-VOC, and ADE20K, with AnyUp consistently second.

Upsample Anything (prob.). In addition to upsampling feature maps, we evaluate a low-compute variant that *predicts the segmentation at the feature resolution* (no feature upsampling), produces a probabilistic map, and then upsamples *probabilities* to the original image size using our method.
Because the logits/probabilities live on a much smaller spatial grid, this pipeline achieves the lowest computational cost yet delivers the highest accuracy in Table [1](#S5.T1 "Table 1 ‣ 5.2 Implementation Details ‣ 5 Experiments ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling").
This suggests a promising paradigm for segmentation: upsample task probabilities rather than intermediate features.

| Method | Depth Estimation | | Surface Normal Estimation | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RMSE (↓) | δ1\delta\_{1} (↑) | Mean (↓) | Median (↓) | <11.25∘<\!11.25^{\circ} (↑) | <22.5∘<\!22.5^{\circ} (↑) | <30∘<\!30^{\circ} (↑) |
| Bilinear | 0.545 | 0.804 | 23.8 | 19.5 | 33.0 | 70.0 | 81.0 |
| FeatUp | 0.523 | 0.810 | 22.7 | 18.6 | 35.5 | 72.3 | 83.0 |
| LoftUp | 0.796 | 0.789 | 28.9 | 24.1 | 25.0 | 58.0 | 71.0 |
| JAFAR | 0.521 | 0.807 | 23.2 | 19.0 | 34.0 | 70.8 | 82.0 |
| AnyUp | 0.513 | 0.817 | 22.2 | 18.1 | 36.8 | 73.5 | 84.1 |
| Upsample Anything (Ours) | 0.498 | 0.829 | 21.5 | 17.4 | 38.1 | 75.2 | 85.8 |

## B-849e88970919e6

https://arxiv.org/html/2511.16301v1#chars-28221-29277

#### Across Different Backbones.

We compare the visual quality of upsampled features produced by AnyUP and our Upsample Anything across various backbone architectures.
Given the 224×224 input image, the spatial resolutions of the extracted feature maps differ by model: 7×7 for ConvNeXt, 14×14 for CLIP and DINOv1, and 16×16 for DINOv2 and DINOv3.
In this example, I^H​R\hat{I}\_{HR} denotes the reconstructed high-resolution image obtained from a 7×7 low-resolution IL​RI\_{LR} using Upsample Anything.
As shown in  [Fig. 6](#S5.F6 "In Feature Similarity Analysis. ‣ 5.4 Qualitative results ‣ 5 Experiments ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling"), Upsample Anything consistently produces sharper boundaries, finer local structures, and more coherent feature clustering than AnyUP across all backbones.
We attribute this advantage to Upsample Anything’s test-time optimization, which adaptively fits Gaussian parameters to each input image, yielding features that align more precisely with image-level semantics.

## B-8c9a19422acec0

https://arxiv.org/html/2511.16301v1#chars-7325-7345

## 2 Related Works

## B-91084d84f65247

https://arxiv.org/html/2511.16301v1#chars-27517-28221

#### Across Different Resolutions.

Figure [5](#S5.F5 "Figure 5 ‣ Depth Map Upsampling ‣ 5.3 quantitative results ‣ 5 Experiments ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling") compares AnyUp (previous SOTA) and our Upsample Anything across different input resolutions.
As shown, AnyUp performs reasonably well at higher resolutions (e.g., 32×3232{\times}32 and 16×1616{\times}16) but tends to produce over-smoothed regions, as highlighted by the red boxes.
In contrast, Upsample Anything maintains sharp boundaries and fine structures even at extremely low resolutions (e.g., 7×77{\times}7 and 4×44{\times}4), demonstrating stronger robustness to spatial degradation.

## B-929306efade115

https://arxiv.org/html/2511.16301v1#chars-24662-25664

#### Depth Estimation

We evaluate our method on the NYUv2 dataset using a frozen DINOv2 backbone.
Following prior works (AnyUp, LoftUp), we adopt a lightweight DPT-style decoder head for dense prediction (details in Appendix).
Unlike the original DPT, our Upsample Anything removes the internal interpolation layers, as the feature maps are already upsampled to high resolution.
As shown in Table [2](#S5.T2 "Table 2 ‣ Semantic Segmentation. ‣ 5.3 quantitative results ‣ 5 Experiments ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling"), Upsample Anything achieves the best performance on both depth and surface normal estimation
(RMSE 0.498, δ1\delta\_{1} 0.829, mean 21.5°),
indicating that precise feature upsampling is particularly beneficial for geometry-oriented tasks,
while LoftUp suffers from domain gaps and fails to generalize.
It appears that feature upsampling plays a more critical role in depth and surface normal estimation than in semantic segmentation.

## B-9612544197c049

https://arxiv.org/html/2511.16301v1#chars-35847-36931

## 6 Conclusion

We introduced Upsample Anything, a unified framework that connects Joint Bilateral Upsampling (JBU) and Gaussian Splatting (GS) under a continuous formulation.
It performs lightweight test-time optimization without pre-training or architectural constraints, achieving efficient and robust upsampling across diverse resolutions and domains.
It optimizes a 224×224 image in 0.419 seconds while producing significant gains in both feature and depth upsampling.
Extensive experiments show that Upsample Anything achieves state-of-the-art performance without any learnable module, serving as a universal, plug-and-play framework that combines the simplicity of JBU with the expressive power of Gaussian representation.
Limitation.
Despite its generality, Upsample Anything may face challenges under severe occlusions or low-SNR guidance, where optimization becomes unstable.
Future work will focus on enhancing the robustness and adaptability of the framework across diverse domains, aiming to make it more resilient under challenging conditions.

Supplementary Material

## B-983109aa286bfc

https://arxiv.org/html/2511.16301v1#chars-47263-48214

###### Proof.

By construction,
‖ϕ⁡(p)−ϕ⁡(q)‖Λ−12=(p−q)⊤​(σs−2​I2)​(p−q)+(I⁡(p)−I⁡(q))⊤​(σr−2​Id)​(I⁡(p)−I⁡(q)).\|\phi(p)-\phi(q)\|\_{\Lambda^{-1}}^{2}=(p-q)^{\!\top}(\sigma\_{s}^{-2}I\_{2})(p-q)+(I(p)-I(q))^{\!\top}(\sigma\_{r}^{-2}I\_{d})(I(p)-I(q)).
Thus
𝒢Λ​(ϕ⁡(p),ϕ⁡(q))=exp⁡(−‖p−q‖22​σs2)​exp⁡(−‖I⁡(p)−I⁡(q)‖22​σr2),\mathcal{G}\_{\Lambda}(\phi(p),\phi(q))=\exp\!\big(-\tfrac{\|p-q\|^{2}}{2\sigma\_{s}^{2}}\big)\,\exp\!\big(-\tfrac{\|I(p)-I(q)\|^{2}}{2\sigma\_{r}^{2}}\big),
and substituting this identity in ([1](#S2.E1 "Equation 1 ‣ 2.1 Joint Bilateral Upsampling ‣ 2 Related Works ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")) yields ([9](#S13.E9 "Equation 9 ‣ Theorem 1 (JBU as a normalized Gaussian mixture in the joint domain). ‣ Notation. ‣ 13 Formal Relation Between Joint Bilateral Upsampling and Gaussian Splatting ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")).
∎

## B-9e3a95b4317381

https://arxiv.org/html/2511.16301v1#chars-39531-40085

## 9 Details of Depth Estimation in Table 2.

We followed the DPT-based depth estimation setup used in prior works [[10](#bib.bib22), [23](#bib.bib24)].
Although DPT includes an internal upsampling, its exact implementation details are not provided in the paper or codebase.
Therefore, we reimplemented the head as described in Algorithm [1](#alg1 "Algorithm 1 ‣ 9 Details of Depth Estimation in Table 2. ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling") and used it consistently for all our depth estimation experiments.

## B-9eaca53efa2036

https://arxiv.org/html/2511.16301v1#chars-40085-42152

## 10 From 2D Low-Resolution Feature Maps to 3D High-Resolution Feature Volumes

![Refer to caption](2511.16301v1/3df.png)

We extend our test-time optimization (TTO) framework to reconstruct dense 3D feature volumes directly from low-resolution 2D feature maps.
Starting with an RGB–Depth (RGB-D) pair, we first downsample the RGB image by a factor of ss to simulate a low-resolution feature space.
The corresponding high-resolution RGB-D map is used as the guide signal for optimization.
During TTO stage, we train only the pixel-wise anisotropic Gaussian kernel parameters (σx,σy,σz,θ,σr)(\sigma\_{x},\sigma\_{y},\sigma\_{z},\theta,\sigma\_{r}) so that the 3D Upsample Anyting can accurately project the low-resolution RGB features to their high-resolution RGB-D counterparts.
Once optimized, these learned kernels are frozen and reused in upsample stage to upsample semantic features extracted from 2D LR feature into full 3D feature volumes.
This process allows each low-resolution feature token to be expanded not only spatially along the xx–yy plane, but also along the depth axis zz, guided by the HR depth map.
The resulting tensor 𝐅3​D∈ℝDh×C×Hh×Wh\mathbf{F}\_{3D}\in\mathbb{R}^{D\_{h}\times C\times H\_{h}\times W\_{h}} captures the local geometric and appearance-aware structure of the scene.
We visualize these 3D feature maps using PCA on each depth slice, revealing how distinct depth layers retain meaningful semantic separation while smoothly transitioning across depth.
Figure [9](#S10.F9 "Figure 9 ‣ 10 From 2D Low-Resolution Feature Maps to 3D High-Resolution Feature Volumes ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling") shows that even without explicit 3D supervision, our Full3DJBU reconstructs volumetric features that align with depth continuity, edges, and object boundaries—demonstrating that our framework can generalize from 2D low-resolution feature inputs to 3D high-resolution representations at test time.

![Refer to caption](2511.16301v1/gs_vis.png)
![Refer to caption](2511.16301v1/seg_vis2.png)

## B-a075ece671dcdb

https://arxiv.org/html/2511.16301v1#chars-19802-19820

## 5 Experiments

## B-aa7d70af9f3cb8

https://arxiv.org/html/2511.16301v1#chars-57965-59909

## 15 Limitation under Low-SNR or Corrupted Inputs

Although our method performs robustly across diverse datasets and even under moderate perturbations such as those in ImageNet-C, it exhibits a clear limitation when applied to images with extremely low signal-to-noise ratios or severe corruption.

Because our framework performs test-time optimization (TTO) by reconstructing the input image itself, the optimization process inherently assumes that the image contains a clean and reliable signal. When the input is degraded by noise—such as salt-and-pepper artifacts or heavy sensor perturbations—the model tends to overfit to these corruptions rather than recovering the underlying structure. Figure [12](#S13.F12 "Figure 12 ‣ Implementation note. ‣ 13 Formal Relation Between Joint Bilateral Upsampling and Gaussian Splatting ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling") illustrates this effect: the first row shows results on a clean image, while the second and third rows demonstrate increasing corruption levels of 10% and 20%, respectively.

Despite the noise, pretrained Vision Foundation Models still produce reasonable feature embeddings, and AnyUp remains stable by directly upsampling feature maps. In contrast, our TTO-based Upsample Anything reconstructs the noisy signal faithfully, which unintentionally amplifies noise in both the reconstructed RGB and upsampled feature domains.

This limitation is not unique to our method but is common across all TTO-based image restoration approaches that optimize directly on corrupted inputs.
While one could incorporate a denoising stage before optimization to alleviate this issue, we consider it outside the current scope.
In summary, AnyUp demonstrates higher robustness under corrupted or low-SNR conditions, whereas our Upsample Anything excels when inputs are visually clean or when handling multi-modal signals such as RGB-D or 3D features.

## B-b4502b05011d92

https://arxiv.org/html/2511.16301v1#chars-60819-62158

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

## B-b96eb29b874b3a

https://arxiv.org/html/2511.16301v1#chars-18256-19802

### 4.3 Test-Time Optimization

After defining the Upsample Anything formulation in [Sec. 4.2](#S4.SS2 "4.2 Algorithm Design ‣ 4 Methods ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling"), the next step is to optimize its per-pixel parameters
{σx,σy,θ,σr}\{\sigma\_{x},\sigma\_{y},\theta,\sigma\_{r}\}.
Our key idea is inspired by the patchified processing of modern Vision Foundation Models (VFMs):
since VFMs downsample images by a fixed stride to extract low-resolution features,
we emulate this process during optimization.

Specifically, the high-resolution image Ih​rI\_{hr} is downsampled to Il​rI\_{lr} by bilinear interpolation with a stride ss,
and the GSJBU parameters are optimized under a reconstruction objective from Il​rI\_{lr} back to Ih​rI\_{hr}:

|  |  |  |
| --- | --- | --- |
|  | ℒTTO=‖GSJBU⁡(Il​r)−Ih​r‖1.\mathcal{L}\_{\text{TTO}}=\big\|\mathrm{GSJBU}(I\_{lr})-I\_{hr}\big\|\_{1}. |  |

This test-time optimization finds image-specific, pixel-wise kernels that best reconstruct the guidance signal.

After the TTO process, the learned kernels are reused to render the high-resolution feature map:

|  |  |  |
| --- | --- | --- |
|  | Fh​r=GSJBU⁡(Fl​r,σ^x,σ^y,θ^,σ^r),F\_{hr}=\mathrm{GSJBU}(F\_{lr};\,\hat{\sigma}\_{x},\hat{\sigma}\_{y},\hat{\theta},\hat{\sigma}\_{r}), |  |

where the optimized parameters {σ^x,σ^y,θ^,σ^r}\{\hat{\sigma}\_{x},\hat{\sigma}\_{y},\hat{\theta},\hat{\sigma}\_{r}\}
are directly transferred to the foundation feature space to upsample Fl​rF\_{lr} into Fh​rF\_{hr}.

## B-bb500db3d94781

https://arxiv.org/html/2511.16301v1#chars-209-289

# Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling

## B-bd5cc707e57c7d

https://arxiv.org/html/2511.16301v1#chars-13276-14746

### 4.1 Overview

As illustrated in [Fig. 3](#S2.F3 "In 2.2 Feature Upsampling ‣ 2 Related Works ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling"), our method, Upsample Anything, consists of two stages:
(i) test-time optimization (TTO) and
(ii) feature rendering.
In the TTO stage, Upsample Anything learns per-pixel anisotropic Gaussian parameters
{σx,σy,θ,σr}\{\sigma\_{x},\sigma\_{y},\theta,\sigma\_{r}\}
by reconstructing the high-resolution image Ih​rI\_{hr} from its patch-wise downsampled version Il​rI\_{lr}.
This process enables each pixel to learn how spatially and photometrically similar neighbors should be blended-effectively discovering local mixing weights that generalize beyond the image domain.
Once optimized, these Gaussian kernels are directly transferred to the foundation feature space,
where the low-resolution feature map Fl​r∈ℝC×H/s×W/sF\_{lr}\!\in\!\mathbb{R}^{C\times H/s\times W/s}
is splatted to produce the high-resolution feature Fh​r∈ℝC×H×WF\_{hr}\!\in\!\mathbb{R}^{C\times H\times W}
using the same learned anisotropic weighting mechanism.
Because the splatting weights depend only on spatial–range similarity,
this transfer is naturally domain-agnostic, allowing the learned kernels to act as universal upsampling operators.
Excluding the feature extraction time of the Vision Foundation Model (VFM),
the entire optimization and inference for a 224×224224{\times}224 image takes ≈0.419\approx 0.419 s.

## B-c58490b950d385

https://arxiv.org/html/2511.16301v1#chars-25664-27488

#### Depth Map Upsampling

Unlike feature upsampling tasks, our Upsample Anything can also be applied to *other modalities* such as raw depth maps.
In Table [3](#S5.T3 "Table 3 ‣ Depth Map Upsampling ‣ 5.3 quantitative results ‣ 5 Experiments ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling"), we evaluate Upsample Anything by downsampling high-resolution depth maps to 32×3232{\times}32 and restoring them to 512×512512{\times}512 resolution.
This setup shares the same bilateral upsampling pipeline as our feature experiments, except that the low-resolution input is a depth map itself.
We compare against the state-of-the-art guided interpolation method (GLU) [[21](#bib.bib32)] and the bilinear baseline.
As shown in Figure [4](#S5.F4 "Figure 4 ‣ Depth Map Upsampling ‣ 5.3 quantitative results ‣ 5 Experiments ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling"), Upsample Anything achieves the best performance on the Middlebury dataset, producing sharper and more consistent structures.
In contrast, on the NYUv2 dataset, the bilinear method yields a slightly lower RMSE (0.159 vs. 0.237), likely because the ground-truth depth maps are blurred and contain smoother structures.
Nevertheless, the qualitative results suggest that Upsample Anything preserves geometry more effectively, especially for high-frequency and edge-dominant regions.

| Method | NYUv2 (Depth Up.) | | Middlebury (Depth Up.) | |
| --- | --- | --- | --- | --- |
| RMSE (↓) | δ1\delta\_{1} (↑) | RMSE (↓) | δ1\delta\_{1} (↑) |
| Bilinear | 0.167 | 0.983 | 0.231 | 0.962 |
| GLU (Guided Linear Upsample) | 0.372 | 0.841 | 0.491 | 0.825 |
| Upsample Anything (Ours) | 0.214 | 0.976 | 0.209 | 0.967 |

![Refer to caption](2511.16301v1/depth.png)
![Refer to caption](2511.16301v1/size.png)

## B-c73598c1664869

https://arxiv.org/html/2511.16301v1#chars-8997-10467

### 2.2 Feature Upsampling

A pioneering work in feature upsampling is FeatUp [[6](#bib.bib20)], which proposed two model-agnostic modules: FeatUp (JBU) and FeatUp (Implicit).
The former generalizes Joint Bilateral Upsampling (JBU) [[14](#bib.bib26)] to high-dimensional feature space by replacing the fixed Gaussian range kernel with a learnable MLP, while the latter parameterizes high-resolution features as an implicit function Fh​r=MLP​(x,I⁡(x))F\_{hr}=\text{MLP}(x,I(x)) optimized per image.
While FeatUp effectively restores spatial detail from foundation features, it either requires dataset-level training or incurs long per-image optimization.

Several follow-up studies further improved spatial fidelity through learnable upsamplers.
LiFT [[22](#bib.bib21)] employed a lightweight U-Net-like upsampler with reconstruction loss,
LoftUp [[10](#bib.bib22)] integrated RGB coordinates via cross-attention with pseudo-groundtruth supervision,
and JAFAR [[3](#bib.bib23)] introduced joint-attention filtering for semantic–structural alignment.
AnyUp [[23](#bib.bib24)] proposed resolution-conditioned kernels for scalable upsampling.
Despite their strong performance, these methods rely on dataset-level training, which makes them less adaptive to unseen domains.
They often generalize reasonably well but still exhibit suboptimal performance when facing novel architectures, resolutions, or out-of-distribution data.

![Refer to caption](2511.16301v1/method.png)

## B-d28add6b2cca41

https://arxiv.org/html/2511.16301v1#chars-43219-44190

## 12 Segment-then-Upsample Pipeline Visualization Results

This section presents the visualization results of our segment-then-upsample pipeline, corresponding to the method in Fig. [8](#S8.F8 "Figure 8 ‣ 8 Details of Probabilistic Map Upsampling in Table 1. ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")-(c).
In this configuration, we perform semantic segmentation on the low-resolution feature maps first and subsequently upsample the segmentation logits by a factor of 16×16\times.
Despite the large upsampling ratio, our Upsample Anything produces visually sharp and semantically consistent results, as illustrated in Fig. [11](#S10.F11 "Figure 11 ‣ 10 From 2D Low-Resolution Feature Maps to 3D High-Resolution Feature Volumes ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling").
Compared to conventional bilinear interpolation, the recovered boundaries and fine structures are significantly clearer.

## B-dc403241c0ffb1

https://arxiv.org/html/2511.16301v1#chars-57051-57965

## 14 Hyperparameter Table

The hyperparameters in Table [8](#S13.T8 "Table 8 ‣ Connection to standard 2D GS. ‣ 13 Formal Relation Between Joint Bilateral Upsampling and Gaussian Splatting ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling") function primarily as soft priors for test-time optimization.
Since all spatial and range parameters are refined during the 50 optimization steps, the final performance depends only weakly on their initial values.
A well-chosen initialization simply accelerates convergence, whereas suboptimal values are eventually corrected by the optimization itself.
The table therefore summarizes practical initialization rules rather than strict hyperparameter requirements.
These rules are based on the expected receptive-field size, the dynamic range of the guidance image, and the desired locality prior, and they lead to stable and fast convergence.

## B-de1b388295b99e

https://arxiv.org/html/2511.16301v1#chars-53757-54482

###### Proposition 1 (Discrete-to-continuous convergence).

Assume FlrF\_{\mathrm{lr}} admits a bandlimited (or Lipschitz-continuous) interpolation F~:Ω→ℝC\tilde{F}:\Omega\to\mathbb{R}^{C},
and let the LR grid spacing be Δ​x\Delta x.
Then as Δ​x→0\Delta x\to 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑qF~​(q)​𝒢Λ​(ϕ⁡(p),ϕ⁡(q))​(Δ​x)2⟶∫ΩF~​(x)​𝒢Λ​(ϕ⁡(p),ϕ⁡(x))​𝑑x,\small\sum\nolimits\_{q}\tilde{F}(q)\,\mathcal{G}\_{\Lambda}\!\big(\phi(p),\phi(q)\big)\,(\Delta x)^{2}\ \longrightarrow\ \int\_{\Omega}\tilde{F}(x)\,\mathcal{G}\_{\Lambda}\!\big(\phi(p),\phi(x)\big)\,dx, |  | (13) |

and the corresponding normalized ratios converge as well. Hence, discrete JBU converges to its continuous lifted-domain GS counterpart.

## B-de958af3e490ef

https://arxiv.org/html/2511.16301v1#chars-30422-30446

### 5.5 Ablation Study

## B-e01d5f9e5d8f47

https://arxiv.org/html/2511.16301v1#chars-59909-60819

## References

![[LOGO]](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)

## B-e0ff3d8f9e6dc8

https://arxiv.org/html/2511.16301v1#chars-49185-50429

#### Connection to standard 2D GS.

Standard (2D) GS writes, for p∈ℝ2p\in\mathbb{R}^{2},

|  |  |  |  |
| --- | --- | --- | --- |
|  | F⁡(p)=∑iαi​exp⁡(−12​(p−μ~i)⊤​Σ~i−1​(p−μ~i))​f~i∑jαj​exp⁡(−12​(p−μ~j)⊤​Σ~j−1​(p−μ~j)).\small F(p)=\frac{\sum\limits\_{i}\alpha\_{i}\,\exp\!\big(-\tfrac{1}{2}(p-\tilde{\mu}\_{i})^{\!\top}\tilde{\Sigma}\_{i}^{-1}(p-\tilde{\mu}\_{i})\big)\,\tilde{f}\_{i}}{\sum\limits\_{j}\alpha\_{j}\,\exp\!\big(-\tfrac{1}{2}(p-\tilde{\mu}\_{j})^{\!\top}\tilde{\Sigma}\_{j}^{-1}(p-\tilde{\mu}\_{j})\big)}. |  | (11) |

The range term in JBU can be *absorbed* by lifting to the joint domain (Theorem [1](#Thmtheorem1 "Theorem 1 (JBU as a normalized Gaussian mixture in the joint domain). ‣ Notation. ‣ 13 Formal Relation Between Joint Bilateral Upsampling and Gaussian Splatting ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")), or, equivalently, by keeping the domain 2D and letting the amplitude be query-dependent,
αi​(p)=exp⁡(−‖I⁡(p)−I⁡(μ~i)‖22​σr2).\alpha\_{i}(p)=\exp\!\big(-\tfrac{\|I(p)-I(\tilde{\mu}\_{i})\|^{2}}{2\sigma\_{r}^{2}}\big).
The former is strictly *query-independent* and thus mathematically cleaner; the latter matches common GS implementations with view-dependent weights.

## B-e9190e35433dae

https://arxiv.org/html/2511.16301v1#chars-15391-17152

#### Per-pixel anisotropic kernels.

To overcome these limits, Upsample Anything assigns a *per-LR-pixel* anisotropic Gaussian with parameters
{σx​(q),σy​(q),θ⁡(q),σr​(q)}\{\sigma\_{x}(q),\,\sigma\_{y}(q),\,\theta(q),\,\sigma\_{r}(q)\} for each low-resolution location qq.
Let the spatial covariance be

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σq=R⁡(θq)​[σx2​(q)00σy2​(q)]​R⊤​(θq);R⁡(θq)=[cos⁡θq−sin⁡θqsin⁡θqcos⁡θq].\Sigma\_{q}=R(\theta\_{q})\begin{bmatrix}\sigma\_{x}^{2}(q)&0\\[3.0pt] 0&\sigma\_{y}^{2}(q)\end{bmatrix}R^{\top}(\theta\_{q});\hskip 8.50012ptR(\theta\_{q})=\begin{bmatrix}\cos\theta\_{q}&-\sin\theta\_{q}\\[3.0pt] \sin\theta\_{q}&\cos\theta\_{q}\end{bmatrix}. |  | (4) |

For an HR coordinate pp, the *unnormalized* spatial weight and range (guidance) weight are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | log⁡wp←qs\displaystyle\small\log w^{\text{s}}\_{p\leftarrow q} | =−12​(p−μq)⊤​Σq−1​(p−μq),\displaystyle=-\tfrac{1}{2}\,(p-\mu\_{q})^{\top}\Sigma\_{q}^{-1}(p-\mu\_{q}), |  | (5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | log⁡wp←qr\displaystyle\log w^{\text{r}}\_{p\leftarrow q} | =−‖I⁡(p)−I⁡(q)‖22​σr2​(q).\displaystyle=-\frac{\|I(p)-I(q)\|^{2}}{2\,\sigma\_{r}^{2}(q)}. |  | (6) |

where μq\mu\_{q} is the LR center projected to HR coordinates and I⁡(⋅)I(\cdot) is the HR guidance image.
The final normalized mixing weight is

|  |  |  |  |
| --- | --- | --- | --- |
|  | wp←q=exp⁡(log⁡wp←qs+log⁡wp←qr)∑q′∈Ω⁡(p)exp⁡(log⁡wp←q′s+log⁡wp←q′r).w\_{p\leftarrow q}\;=\;\frac{\exp\!\big(\log w^{\text{s}}\_{p\leftarrow q}+\log w^{\text{r}}\_{p\leftarrow q}\big)}{\sum\limits\_{q^{\prime}\in\Omega(p)}\exp\!\big(\log w^{\text{s}}\_{p\leftarrow q^{\prime}}+\log w^{\text{r}}\_{p\leftarrow q^{\prime}}\big)}. |  | (7) |

## B-e95c6056ec4f2f

https://arxiv.org/html/2511.16301v1#chars-13262-13276

## 4 Methods

## B-eb858d4fb83fdb

https://arxiv.org/html/2511.16301v1#chars-27488-27517

### 5.4 Qualitative results

## B-ef5fd7d536509a

https://arxiv.org/html/2511.16301v1#chars-19820-20801

### 5.1 Experimental Setting

Following prior feature-upscaling works [[6](#bib.bib20), [22](#bib.bib21), [10](#bib.bib22), [3](#bib.bib23), [23](#bib.bib24)], we evaluate Upsample Anything on semantic segmentation (COCO, PASCAL-VOC, ADE20K) and depth estimation (NYUv2). For segmentation, we use a single 1×11\times 1 convolution head (linear probe), identical to prior settings.
For depth, we adopt a DPT-style decoder head, consistent with [[10](#bib.bib22), [23](#bib.bib24)]. To compare backbones, we consider DINOv1, DINOv2, DINOv3, CLIP, and ConvNeXt, covering both transformer and convolutional families; unless otherwise specified, the default backbone is DINOv2-S.

Unlike prior approaches restricted to feature maps, Upsample Anything applies to general bilateral upsampling. Accordingly, we further evaluate (i) depth-map upsampling on NYUv2 and Middlebury, and (ii) probability-map upsampling on Cityscapes—each guided by the corresponding high-resolution RGB image.

## B-f3793c84811ad8

https://arxiv.org/html/2511.16301v1#chars-30446-32514

#### Resolution–Efficiency Tradeoff

We analyze the computational efficiency of our Upsample Anything compared with AnyUp [[23](#bib.bib24)] across multiple output resolutions, as summarized in Table [4](#S5.T4 "Table 4 ‣ Resolution–Efficiency Tradeoff ‣ 5.5 Ablation Study ‣ 5 Experiments ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling").
AnyUp employs a feature-agnostic layer and local window attention that allow flexible inference across arbitrary encoders and resolutions.
While this design yields fast performance at lower resolutions (<256×256<\!256\times 256), the window-based attention and dense similarity computation introduce quadratic growth in both memory and time complexity as the spatial size increases.
Consequently, AnyUp suffers from significant GPU memory overhead and fails with out-of-memory (OOM) errors beyond 512×512512\times 512, exposing a scalability bottleneck in its dense attention formulation.

In contrast, our Upsample Anything performs fully parallel anisotropic Gaussian splatting without building dense pairwise affinity maps, resulting in linear memory growth with respect to the output size.
As shown in Table [4](#S5.T4 "Table 4 ‣ Resolution–Efficiency Tradeoff ‣ 5.5 Ablation Study ‣ 5 Experiments ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling"), Upsample Anything maintains stable runtime and controlled memory even at 1024×10241024\times 1024 resolution—where AnyUp cannot execute—demonstrating its robustness for large-scale feature upsampling.

|  |  |  |
| --- | --- | --- |
| Resolution (H×W) | AnyUp (trained) / | AnyUp (trained) / |
|  | Ours (TTA) Time (s) | Ours (TTA) Peak Mem (MB) |
| 64×64 | 0.0025 / 0.0055 | 53.8 / 358.5 |
| 128×128 | 0.0034 / 0.0150 | 121.9 / 1320.5 |
| 224×224 | 0.0137 / 0.0419 | 531.0 / 3969.7 |
| 448×448 | 0.0583 / 0.2398 | 6184.2 / 15774.8 |
| 512×512 | 0.0893 / 0.3211 | 10283.8 / 20590.4 |
| 896×896 | 0.5875 / 1.2789 | 91250.9 / 62985.2 |
| 1024×1024 | OOM / 1.8083 | — / 82255.5 |
| 2048×2048 | OOM / OOM | — / — |

## B-f4253e0c31cb28

https://arxiv.org/html/2511.16301v1#chars-11879-13262

#### Relation to Joint Bilateral Upsampling (JBU).

JBU [[14](#bib.bib26)] computes each high-resolution (HR) output Fhr​(p)F\_{\mathrm{hr}}(p) as a normalized weighted average of low-resolution (LR) samples Flr​(q)F\_{\mathrm{lr}}(q), where the weights depend on both spatial proximity and guidance-image similarity (see Eq. [1](#S2.E1 "Equation 1 ‣ 2.1 Joint Bilateral Upsampling ‣ 2 Related Works ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling")).
Viewed geometrically, each LR sample qq can be regarded as a Gaussian centered at μq=q\mu\_{q}{=}q with an *isotropic* covariance Σq=σs2​I\Sigma\_{q}{=}\sigma\_{s}^{2}I.
Under this view, JBU corresponds to a discrete and isotropic instance of a guidance-modulated 2D Gaussian Splatting (2DGS) process, where the range term is provided by the HR guidance image.
In contrast, Upsample Anything assigns per-pixel anisotropic covariances Σp\Sigma\_{p} and range scales σr,p\sigma\_{r,p} through test-time optimization, enabling adaptive fusion across space and range.
This pixel-level Gaussian parameterization captures locally varying orientations and scales, making Upsample Anything a continuous, edge-preserving extension of JBU within the 2DGS framework.
For the exact derivation and a more formal discussion of how this formulation differs from a simple combination, please refer to Appendix §12.

## B-f4970bcb0fe40d

https://arxiv.org/html/2511.16301v1#chars-36931-38620

## 7 Semantic Segmentation on Cityscapes

We evaluated feature upsampling and probability-map upsampling on Cityscapes using the official LoftUp segmentation codebase with a stronger training setup that includes 448×448 input resolution, 100 epochs, and a learning-rate scheduler.
Under this configuration, all methods, including LoftUp and ours, produced almost the same mIoU as bilinear interpolation, which differs from the improvements reported in the LoftUp paper.

To ensure correctness, we carefully re-examined our implementation through an automated code audit with ChatGPT and a manual review by multiple authors. We found no inconsistencies or bugs.

The quantitative results are summarized in Table [7](#S7.T7 "Table 7 ‣ 7 Semantic Segmentation on Cityscapes ‣ Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling").
Across all methods, including feature-level and probability-level upsampling, the differences remain within a very narrow range.
Cityscapes primarily contains large and regular structures, and its annotations are relatively coarse.
With a sufficiently trained segmentation head, bilinear interpolation already performs near optimally, leaving little room for additional gains.
In contrast, datasets such as COCO, PASCAL-VOC, and ADE20K include many small objects and complex boundaries, where upsampling delivers clear benefits.

| Method | Cityscapes | |
| --- | --- | --- |
| mIoU (↑\uparrow) | Acc. (↑\uparrow) |
| Bilinear | 57.90 | 90.59 |
| FeatUp | 57.92 | 90.61 |
| LoftUp | 57.89 | 90.60 |
| JAFAR | 57.91 | 90.58 |
| AnyUp | 57.93 | 90.62 |
| Upsample Anything | 57.92 | 90.63 |
| Upsample Anything (prob.) | 56.36 | 90.05 |

## B-f6073c0a3e305d

https://arxiv.org/html/2511.16301v1#chars-46468-47263

###### Theorem 1 (JBU as a normalized Gaussian mixture in the joint domain).

Fix σs>0,σr>0\sigma\_{s}{>}0,\ \sigma\_{r}{>}0 and let Λ=Λ⁡(σs,σr)\Lambda=\Lambda(\sigma\_{s},\sigma\_{r}).
Then for any p∈Ωp\in\Omega,

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^hr​(p)=∑q∈Ω⁡(p)Flr​(q)​𝒢Λ​(ϕ⁡(p),ϕ⁡(q))∑q∈Ω⁡(p)𝒢Λ​(ϕ⁡(p),ϕ⁡(q)).\small\hat{F}\_{\mathrm{hr}}(p)=\frac{\sum\limits\_{q\in\Omega(p)}F\_{\mathrm{lr}}(q)\,\mathcal{G}\_{\Lambda}\!\big(\phi(p),\,\phi(q)\big)}{\sum\limits\_{q\in\Omega(p)}\mathcal{G}\_{\Lambda}\!\big(\phi(p),\,\phi(q)\big)}. |  | (9) |

In particular, JBU coincides with evaluating a *normalized* Gaussian mixture in the lifted space ℝ2+d\mathbb{R}^{2+d} whose centers are {ϕ⁡(q)}q∈Ω⁡(p)\{\phi(q)\}\_{q\in\Omega(p)} and whose (isotropic-by-block) covariance is Λ\Lambda.

## B-f66a9c1725fa4b

https://arxiv.org/html/2511.16301v1#chars-10487-11879

#### 2D Gaussian Splatting (2DGS).

Recent works extend 3D Gaussian Splatting (3DGS) [[12](#bib.bib27)] from volumetric radiance fields to 2D image representations [[28](#bib.bib29), [29](#bib.bib30), [32](#bib.bib31)].
In the image–plane setting, a pixel or small region is represented by a Gaussian kernel

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gi​(x)=exp⁡(−12​(x−μi)⊤​Σi−1​(x−μi)),G\_{i}(x)=\exp\!\Big(-\tfrac{1}{2}(x-\mu\_{i})^{\top}\Sigma\_{i}^{-1}(x-\mu\_{i})\Big), |  | (2) |

where μi∈ℝ2\mu\_{i}\in\mathbb{R}^{2} is the center, Σi∈ℝ2×2\Sigma\_{i}\in\mathbb{R}^{2\times 2} is a positive–definite covariance (encoding scale and orientation), and αi\alpha\_{i} is a per–kernel weight.
The rendered image (or feature map) is obtained by normalized alpha blending:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I⁡(x)=∑iwi,ci,wi=αi​Gi​(x)∑jαj​Gj​(x),I(x)=\sum\_{i}w\_{i},c\_{i},\qquad w\_{i}=\frac{\alpha\_{i}G\_{i}(x)}{\sum\_{j}\alpha\_{j}G\_{j}(x)}, |  | (3) |

with cic\_{i} the color or feature associated with kernel ii.
Because all kernels lie on a single 2D plane, rendering reduces to a normalized weighted summation without depth sorting. This process is often described as rasterization/alpha blending and can also be interpreted as a spatially varying anisotropic convolution.
This property enables real-time, pose-free optimization directly in 2D image/feature domains.

## B-f6897e6517c752

https://arxiv.org/html/2511.16301v1#chars-44906-46468

#### Notation.

Let Flr:𝒬→ℝCF\_{\mathrm{lr}}:\mathcal{Q}\!\to\!\mathbb{R}^{C} be a low-resolution feature map on a discrete grid 𝒬⊂ℤ2\mathcal{Q}\subset\mathbb{Z}^{2},
and let I:Ω→ℝdI:\Omega\!\to\!\mathbb{R}^{d} be an HR guidance signal (d=1d{=}1 for grayscale, d=3d{=}3 for RGB, etc.).
For p∈Ω⊂ℝ2p\in\Omega\subset\mathbb{R}^{2}, classical JBU is

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^hr​(p)=∑q∈Ω⁡(p)Flr​(q)​exp⁡(−‖p−q‖22​σs2)​exp⁡(−‖I⁡(p)−I⁡(q)‖22​σr2)∑q∈Ω⁡(p)exp⁡(−‖p−q‖22​σs2)​exp⁡(−‖I⁡(p)−I⁡(q)‖22​σr2).\small\hat{F}\_{\mathrm{hr}}(p)=\frac{\sum\limits\_{q\in\Omega(p)}F\_{\mathrm{lr}}(q)\,\exp\!\big(-\tfrac{\|p-q\|^{2}}{2\sigma\_{s}^{2}}\big)\,\exp\!\big(-\tfrac{\|I(p)-I(q)\|^{2}}{2\sigma\_{r}^{2}}\big)}{\sum\limits\_{q\in\Omega(p)}\exp\!\big(-\tfrac{\|p-q\|^{2}}{2\sigma\_{s}^{2}}\big)\,\exp\!\big(-\tfrac{\|I(p)-I(q)\|^{2}}{2\sigma\_{r}^{2}}\big)}. |  | (8) |

Joint spatial–range lifting.
Define the lifted embedding

|  |  |  |
| --- | --- | --- |
|  | ϕ:Ω→ℝ2+d,ϕ⁡(x):=[xI⁡(x)],\phi:\Omega\to\mathbb{R}^{2+d},\qquad\phi(x):=\begin{bmatrix}x\\ I(x)\end{bmatrix}, |  |

and the block-diagonal covariance

|  |  |  |
| --- | --- | --- |
|  | Λ⁡(σs,σr):=diag⁡(σs2​I2,σr2​Id)∈ℝ(2+d)×(2+d).\Lambda(\sigma\_{s},\sigma\_{r}):=\mathrm{diag}\!\big(\sigma\_{s}^{2}I\_{2},\ \sigma\_{r}^{2}I\_{d}\big)\in\mathbb{R}^{(2+d)\times(2+d)}. |  |

For u,v∈ℝ2+du,v\in\mathbb{R}^{2+d}, let

|  |  |  |
| --- | --- | --- |
|  | 𝒢Λ​(u,v):=exp⁡(−12​(u−v)⊤​Λ−1​(u−v)).\mathcal{G}\_{\Lambda}(u,v):=\exp\!\Big(-\tfrac{1}{2}\,(u-v)^{\!\top}\Lambda^{-1}(u-v)\Big). |  |

## B-fbe8742fc00852

https://arxiv.org/html/2511.16301v1#chars-54482-54877

###### Sketch.

𝒢Λ​(ϕ⁡(p),ϕ⁡(⋅))\mathcal{G}\_{\Lambda}(\phi(p),\phi(\cdot)) is bounded and continuous for fixed pp.
Under the stated regularity, Riemann sums converge to the integral and the denominators stay strictly positive (finite kernel mass). The ratio convergence follows by standard arguments (e.g., dominated convergence and continuity of division on ℝ∖{0}\mathbb{R}\setminus\{0\}).
∎

## B-ocr-20bfda98b190b1

B PDF page 10

Algorithm 1 Depth estimation setting used in Table 2.

Require: Input image x
Ensure: Predicted depth map D
1: Extract multi-scale features F using a pretrained Vision Foundation Model encoder (e.g., DINOv2)
2: Pass F through the DPT head:
3:  \( F_{1} \leftarrow \text{Conv}(F, k=3, c \rightarrow c/2) \) 
4:  \( F_{2} \leftarrow \text{Conv}(F_{1}, k=3, c/2 \rightarrow 32) \) 
5:  \( F_{3} \leftarrow \text{ReLU}(F_{2}) \) 
6:  \( D_{inv} \leftarrow \text{Conv}(F_{3}, k=1, 32 \rightarrow 1) \) 
7:  \( D_{inv} \leftarrow \text{ReLU}(D_{inv}) \)  (if non-negative)
8: if invert is True then
9:  \( D \leftarrow \frac{1}{\text{clip}(s \cdot D_{inv} + t, 1e-8, \infty)} \) 
10: else
11:  \( D \leftarrow D_{inv} \) 
12: end if
13: Output the final depth prediction D

sampling, its exact implementation details are not provided in the paper or codebase. Therefore, we reimplemented the head as described in Algorithm 1 and used it consistently for all our depth estimation experiments.

## 10. From 2D Low-Resolution Feature Maps to 3D High-Resolution Feature Volumes

We extend our test-time optimization (TTO) framework to reconstruct dense 3D feature volumes directly from low-resolution 2D feature maps. Starting with an RGB–Depth (RGB-D) pair, we first downsample the RGB image by a factor of s to simulate a low-resolution feature space. The corresponding high-resolution RGB-D map is used as the guide signal for optimization. During TTO stage, we train only the pixel-wise anisotropic Gaussian kernel parameters  \( (\sigma_{x}, \sigma_{y}, \sigma_{z}, \theta, \sigma_{r}) \)  so that the 3D Upsample Anything can accurately project the low-resolution RGB features to their high-resolution RGB-D counterparts. Once optimized, these learned kernels are frozen and reused in upsample stage to upsample semantic features extracted from 2D LR feature into full 3D feature volumes. This process allows each low-resolution feature token to be expanded not only spatially along the x-y plane, but also along the depth axis z, guided by the HR depth map. The resulting tensor  \( F_{3D} \in R^{D_{h} \times C \times H_{h} \times W_{h}} \)  captures the local geometric and appearance-aware structure of the scene. We visualize these 3D feature maps using PCA on each depth slice, revealing how distinct depth layers retain meaningful semantic separation while smoothly transitioning across depth. Figure 9 shows that even without explicit 3D supervision, our Full3DJBU reconstructs volumetric features that align with depth continuity, edges, and object boundaries—demonstrating that our framework can generalize

from 2D low-resolution feature inputs to 3D high-resolution representations at test time.

## 11. Gaussian Blob Visualization

To better understand what our learned anisotropic kernels capture, we visualized the Gaussian blobs of our model, as shown in Fig. 10. (a) shows the original high-resolution RGB image, and (b) overlays the learned Gaussian blobs on the corresponding low-resolution image. Although the visualization can be difficult to interpret directly, certain spatial regions such as the eyes, nose, and corners exhibit overlapping or consistently oriented blobs, which suggests that nearby kernels capture semantically similar local structures. This indicates that the learned kernels adaptively encode meaningful directional features rather than behaving randomly. However, similar to other methods that rely on Gaussian Splatting or 2DGS, not every blob is fully interpretable, and some visual noise appears due to overparameterization and kernel redundancy.

## 12. Segment-then-Upsample Pipeline Visualization Results

This section presents the visualization results of our segment-then-upsample pipeline, corresponding to the method in Fig. 8-(c). In this configuration, we perform semantic segmentation on the low-resolution feature maps first and subsequently upsample the segmentation logits by a factor of \(16\times\). Despite the large upsampling ratio, our Upsample Anything produces visually sharp and semantically consistent results, as illustrated in Fig. 11. Compared to conventional bilinear interpolation, the recovered boundaries and fine structures are significantly clearer.

## 13. Formal Relation Between Joint Bilateral Upsampling and Gaussian Splatting

The purpose of this section is not to claim that Joint Bilateral Upsampling (JBU) and Gaussian Splatting (GS) are mathematically equivalent. Instead, we aim to show why the GS framework provides a useful foundation for our formulation. By reinterpreting JBU through the perspective of GS, we reveal a common idea based on continuous and differentiable Gaussian kernels, which motivates our use of GS-style parameter learning in the Upsample Anything (GSJBU) framework. In short, this section clarifies the conceptual link between the two views and explains why GS-based test-time optimization naturally applies to feature upsampling.

Notation. Let \( F_{\mathrm{lr}}: \mathcal{Q} \to \mathbb{R}^C \) be a low-resolution feature map on a discrete grid \( \mathcal{Q} \subset \mathbb{Z}^2 \), and let \( I: \Omega \to \mathbb{R}^d \) be an HR guidance signal (\( d = 1 \) for grayscale, \( d = 3 \) for RGB,

## B-ocr-45970be21539f6

B PDF page 1

arXiv:2511.16301v2 [cs.CV] 24 Nov 2025

# Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling

Minseok Seo \( ^{1} \)  Mark Hamilton \( ^{2,3} \)  Changick Kim \( ^{1} \)

\( ^{1} \) KAIST  \( ^{2} \) MIT  \( ^{3} \) Microsoft

minseok.seo@kaist.ac.kr

![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

![img-2.jpeg](img-2.jpeg)

![img-3.jpeg](img-3.jpeg)

## Upsample Anything

A universal, training-free upsampler via lightweight test-time optimization

![img-4.jpeg](img-4.jpeg)

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)

Figure 1. Our method performs lightweight test-time optimization ( \( \approx0.419 \)  s/image) without requiring any dataset-level training. It generalizes seamlessly across domains while maintaining consistent reconstruction quality for every image. (All examples are randomly selected, without cherry-picking.)

## Abstract

We present Upsample Anything, a lightweight test-time optimization (TTO) framework that restores low-resolution features to high-resolution, pixel-wise outputs without any training. Although Vision Foundation Models demonstrate strong generalization across diverse downstream tasks, their representations are typically downsampled by  \( 14\times/16\times \)  (e.g., ViT), which limits their direct use in pixel-level applications. Existing feature upsampling approaches depend on dataset-specific retraining or heavy implicit optimization, restricting scalability and generalization. Upsample Anything addresses these issues through a simple per-image optimization that learns an anisotropic Gaussian kernel combining spatial and range cues, effectively bridging Gaussian Splatting and Joint Bilateral Upsampling.

The learned kernel acts as a universal, edge-aware operator that transfers seamlessly across architectures and modalities, enabling precise high-resolution reconstruction of features, depth, or probability maps. It runs in only  \( \approx 0.419s \)  per  \( 224\times224 \)  image and achieves state-of-the-art performance on semantic segmentation, depth estimation, and both depth and probability map upsampling. Project page: https://seominseok0429.github.io/Upsample-Anything/

## 1. Introduction

Modern computer vision systems for pixel-level prediction tasks such as semantic, instance, and panoptic segmentation [2, 5, 15, 30] or depth estimation [11, 20, 26] often use an encoder-decoder paradigm. The encoder extracts hi-

## B-ocr-51e1128921dca4

B PDF page 15

efficient design for semantic segmentation with transformers. Advances in neural information processing systems, 34:12077–12090, 2021. 2

[26] Lihe Yang, Bingyi Kang, Zilong Huang, Zhen Zhao, Xiaogang Xu, Jiashi Feng, and Hengshuang Zhao. Depth anything v2. Advances in Neural Information Processing Systems, 37:21875–21911, 2024. 1

[27] Xiaohua Zhai, Basil Mustafa, Alexander Kolesnikov, and Lucas Beyer. Sigmoid loss for language image pre-training. In Proceedings of the IEEE/CVF international conference on computer vision, pages 11975–11986, 2023. 2

[28] Xinjie Zhang, Xingtong Ge, Tongda Xu, Dailan He, Yan Wang, Hongwei Qin, Guo Lu, Jing Geng, and Jun Zhang. Gaussianimage: 1000 fps image representation and compression by 2d gaussian splatting. In European Conference on Computer Vision, pages 327–345. Springer, 2024. 3

[29] Yunxiang Zhang, Bingxuan Li, Alexandr Kuznetsov, Akshay Jindal, Stavros Diolatzis, Kenneth Chen, Anton Sochenov, Anton Kaplanyan, and Qi Sun. Image-gs: Content-adaptive image representation via 2d gaussians. In Proceedings of the Special Interest Group on Computer Graphics and Interactive Techniques Conference Conference Papers, pages 1–11, 2025. 3

[30] Bolei Zhou, Hang Zhao, Xavier Puig, Tete Xiao, Sanja Fidler, Adela Barriuso, and Antonio Torralba. Semantic understanding of scenes through the ade20k dataset. International Journal of Computer Vision, 127(3):302–321, 2019. 1

[31] Jinghao Zhou, Chen Wei, Huiyu Wang, Wei Shen, Cihang Xie, Alan Yuille, and Tao Kong. ibot: Image bert pre-training with online tokenizer. arXiv preprint arXiv:2111.07832, 2021. 2

[32] Lingting Zhu, Guying Lin, Jinnan Chen, Xinjie Zhang, Zhenchao Jin, Zhao Wang, and Lequan Yu. Large images are gaussians: High-quality large image representation with levels of 2d gaussian splatting. In Proceedings of the AAAI Conference on Artificial Intelligence, pages 10977–10985, 2025. 3

## B-ocr-6580ba2a20a7fd

B PDF page 13

[tbl-7.html](tbl-7.html)

Table 8. Hyperparameter settings for Upsample Anything. All parameters act as soft priors; the effective kernel shape is governed by test-time optimization of pixelwise anisotropic Gaussians.

![img-52.jpeg](img-52.jpeg)

Figure 12. Qualitative comparison under low-SNR and noise corruption. From left to right: RGB input, low-resolution feature, upsampled feature by AnyUp, and ours (Upsample Anything). From top to bottom: clean image, 10% noise, and 20% noise. AnyUp remains stable under noise, while our TTO-based method overfits to noisy pixels, revealing its limitation when directly optimizing on corrupted inputs.

and the denominators stay strictly positive (finite kernel mass). The ratio convergence follows by standard arguments (e.g., dominated convergence and continuity of division on \(\mathbb{R} \setminus \{0\}\)).

Consequences. (i) Equivalence in the joint domain (Thm. 1) shows that JBU is a GS evaluation on \((x, I(x))\) with block-diagonal covariance. (ii) Anisotropic generalization (12) recovers JBU in the isotropic limit (Thm. 2), and enables per-center covariance learning (our GSJBU). (iii) Discrete-to-continuous consistency (Prop. 1) justifies replacing sums by integrals when refining the sampling grid.

Implementation note. In practice we adopt (12) with test-time optimization of  \( (\Sigma_{q}, \sigma_{r}(q)) \) . For stability,  \( \Sigma_{q} \succ 0 \)  is parameterized via  \( R(\theta_{q})\mathrm{diag}(\sigma_{x}^{2}(q), \sigma_{y}^{2}(q))R(\theta_{q})^{\top} \)  with  \( \sigma_{x}, \sigma_{y} > 0 \) .

## 14. Hyperparameter Table

The hyperparameters in Table 8 function primarily as soft priors for test-time optimization. Since all spatial and range parameters are refined during the 50 optimization steps, the final performance depends only weakly on their initial values. A well-chosen initialization simply accelerates convergence, whereas suboptimal values are eventually corrected by the optimization itself. The table therefore summarizes practical initialization rules rather than strict hyperparameter requirements. These rules are based on the expected receptive-field size, the dynamic range of the guidance image, and the desired locality prior, and they lead to stable and fast convergence.

## 15. Limitation under Low-SNR or Corrupted Inputs

Although our method performs robustly across diverse datasets and even under moderate perturbations such as those in ImageNet-C, it exhibits a clear limitation when applied to images with extremely low signal-to-noise ratios or severe corruption.

Because our framework performs test-time optimization (TTO) by reconstructing the input image itself, the optimization process inherently assumes that the image contains a clean and reliable signal. When the input is degraded by noise—such as salt-and-pepper artifacts or heavy sensor perturbations—the model tends to overfit to these corruptions rather than recovering the underlying structure. Figure 12 illustrates this effect: the first row shows results on a clean image, while the second and third rows demonstrate increasing corruption levels of 10% and 20%, respectively.

Despite the noise, pretrained Vision Foundation Models still produce reasonable feature embeddings, and AnyUp remains stable by directly upsampling feature maps. In contrast, our TTO-based Upsample Anything reconstructs the noisy signal faithfully, which unintentionally amplifies noise in both the reconstructed RGB and upsampled feature domains.

This limitation is not unique to our method but is common across all TTO-based image restoration approaches that optimize directly on corrupted inputs. While one could incorporate a denoising stage before optimization to alleviate this issue, we consider it outside the current scope.

[OCR table id=tbl-7.html; page=13]
<table><tr><td>Parameter</td><td>Symbol</td><td>Default</td><td>Role</td><td>Rationale</td></tr><tr><td>Spatial sigma (s)</td><td>\( \sigma_s \)</td><td>init = scale (e.g., 16)</td><td>Controls major-axis smoothing; receptive-field size</td><td>Initialized proportional to upsampling factor to provide a wide prior; refined by TTO.</td></tr><tr><td>Spatial sigma (y)</td><td>\( \sigma_y \)</td><td>Same as \( \sigma_x \)</td><td>Controls minor-axis smoothing</td><td>Same reasoning as \( \sigma_x \); enables anisotropy to emerge during TTO.</td></tr><tr><td>Orientation</td><td>\( \theta \)</td><td>0</td><td>Rotation of the anisotropic Gaussian</td><td>Zero-init avoids directional bias, TTO discovers optimal orientation.</td></tr><tr><td>Range sigma</td><td>\( \sigma_r \)</td><td>0.12</td><td>Sensitivity to appearance/color similarity</td><td>Moderate color differences (\( \Delta I \approx 0.2 \sim 0.3 \)) are significantly downweighted; acts as soft bilateral prior.</td></tr><tr><td>Support radius (max)</td><td>\( R_{\text{max}} \)</td><td>6–8</td><td>Upper bound on spatial Gaussian support</td><td>Balances context capture and cost (\( \mathcal{O}(2R_{\text{max}} + 1)^2 \)); too small truncates optimal kernels.</td></tr><tr><td>Dynamic multiplier</td><td>\( \sigma_{\text{dyn}} \)</td><td>2.0</td><td>Converts \( \sigma_{\text{all}} \) to effective support radius</td><td>Ensures coverage of \( \sim 95\% \) Gaussian mass (2σ rule); prevents under-coverage early in TTO.</td></tr><tr><td>Center mode</td><td>—</td><td>nearest</td><td>Determines LR anchor for each HR pixel</td><td>Nearest-center alignment improves stability and avoids aliasing for large upsampling factors.</td></tr></table>

## B-ocr-66608eecedf406

B PDF page 11

![img-31.jpeg](img-31.jpeg)

Image

![img-32.jpeg](img-32.jpeg)

Depth

![img-33.jpeg](img-33.jpeg)

Slices 1

![img-34.jpeg](img-34.jpeg)

Slices 3

![img-35.jpeg](img-35.jpeg)

Slices 5

![img-36.jpeg](img-36.jpeg)

Slices 7

![img-37.jpeg](img-37.jpeg)

Slices 9

![img-38.jpeg](img-38.jpeg)

Slices 11

![img-39.jpeg](img-39.jpeg)

Slices 13

![img-40.jpeg](img-40.jpeg)

Slices 15

![img-41.jpeg](img-41.jpeg)

Slices 17

![img-42.jpeg](img-42.jpeg)

Slices 19

![img-43.jpeg](img-43.jpeg)

Slices 21

![img-44.jpeg](img-44.jpeg)

Slices 23

![img-45.jpeg](img-45.jpeg)

Slices 25

![img-46.jpeg](img-46.jpeg)

Slices 27

![img-47.jpeg](img-47.jpeg)

Slices 29

![img-48.jpeg](img-48.jpeg)

Slices 31

Figure 9. Visualization of our 3D feature upsampling results. The first two columns show the RGB image and its corresponding depth map. The remaining panels depict representative depth slices from the reconstructed 3D high-resolution feature volume obtained using our Upsample Anything. Each slice is visualized via PCA projection into RGB space. Notice that the recovered 3D feature layers exhibit smooth transitions along the depth axis while preserving fine object boundaries and geometric continuity.

![img-49.jpeg](img-49.jpeg)

(a) Image

![img-50.jpeg](img-50.jpeg)

(b) Gaussian Blob

Figure 10. Visualization of learned Gaussian blobs. (a) shows the original image and (b) displays the Gaussian blobs overlaid on the low-resolution input. The blobs reveal locally coherent directions and magnitudes, indicating that the learned kernels adapt to the underlying structure of the scene.

etc.). For \(p \in \Omega \subset \mathbb{R}^2\), classical JBU is

\[
\hat {F} _ {\mathrm{lr}} (p) = \frac {\sum_ {q \in \Omega (p)} F _ {\mathrm{lr}} (q) \exp \left(- \frac {\| p - q \| ^ {2}}{2 \sigma_ {r} ^ {2}}\right) \exp \left(- \frac {\| I (p) - I (q) \| ^ {2}}{2 \sigma_ {r} ^ {2}}\right)}{\sum_ {q \in \Omega (p)} \exp \left(- \frac {\| p - q \| ^ {2}}{2 \sigma_ {r} ^ {2}}\right) \exp \left(- \frac {\| I (p) - I (q) \| ^ {2}}{2 \sigma_ {r} ^ {2}}\right)}. \tag {8}
\]

Joint spatial–range lifting. Define the lifted embedding

\[
\phi : \Omega \to \mathbb {R} ^ {2 + d}, \qquad \phi (x) := \left[ \begin{array}{c} x \\ I (x) \end{array} \right],
\]

and the block-diagonal covariance

\[
\Lambda \left(\sigma_ {s}, \sigma_ {r}\right) := \operatorname{diag} \left(\sigma_ {s} ^ {2} I _ {2}, \sigma_ {r} ^ {2} I _ {d}\right) \in \mathbb {R} ^ {(2 + d) \times (2 + d)}.
\]

For \(u, v \in \mathbb{R}^{2 + d}\), let

\[
\mathcal {G} _ {\Lambda} (u, v) := \exp \left(- \frac {1}{2} (u - v) ^ {\top} \Lambda^ {- 1} (u - v)\right).
\]

Theorem 1 (JBU as a normalized Gaussian mixture in the joint domain). Fix \(\sigma_s > 0\), \(\sigma_r > 0\) and let \(\Lambda = \Lambda(\sigma_s, \sigma_r)\). Then for any \(p \in \Omega\),

\[
\hat {F} _ {\mathrm{lr}} (p) = \frac {\sum_ {q \in \Omega (p)} F _ {\mathrm{lr}} (q) \mathcal {G} _ {\Lambda} (\phi (p) , \phi (q))}{\sum_ {q \in \Omega (p)} \mathcal {G} _ {\Lambda} (\phi (p) , \phi (q))}. \tag {9}
\]

In particular, JBU coincides with evaluating a normalized Gaussian mixture in the lifted space  \( R^{2+d} \)  whose centers are  \( \{\phi(q)\}_{q\in\Omega(p)} \)  and whose (isotropic-by-block) covariance is  \( \Lambda \) .

Proof. By construction,  \( \|\phi(p)-\phi(q)\|_{\Lambda^{-1}}^{2}=(p-q)^{\top}(\sigma_{s}^{-2}I_{2})(p-q)+(I(p)-I(q))^{\top}(\sigma_{r}^{-2}I_{d})(I(p)-I(q)) \) . Thus  \( \mathcal{G}_{\Lambda}(\phi(p),\phi(q))=\exp\left(-\frac{\|p-q\|^{2}}{2\sigma_{r}^{2}}\right)\exp\left(-\frac{\|I(p)-I(q)\|^{2}}{2\sigma_{r}^{2}}\right) \) , and substituting this identity in (1) yields (9).

## B-ocr-67209ad4a41b6c

B PDF page 8

![img-26.jpeg](img-26.jpeg)

Figure 6. Visual comparison across different backbones. Given the same  \( 224 \times 224 \)  input, feature maps have varying spatial resolutions ( \( 7 \times 7 \)  for ConvNeXt,  \( 14 \times 14 \)  for CLIP and DINOv1,  \( 16 \times 16 \)  for DINOv2/v3). Upsample Anything produces sharper edges, richer textures, and more distinct feature clustering than AnyUP across all backbones, demonstrating its strong adaptability through test-time optimization.

![img-27.jpeg](img-27.jpeg)

Figure 7. Visualization of feature similarity between a reference and a target image. The feature vector is obtained by averaging the reference features within the reference mask, and cosine similarity is then computed against all feature locations in the target image.

[tbl-4.html](tbl-4.html)

Table 5. Comparison of inference time, segmentation, and depth estimation performance across different upsampling methods. GSJBU achieves the best balance between accuracy and scalability.

over-smoothing during test-time optimization. In contrast, Upsample Anything inherits the spatial-range constraint of classical JBU while leveraging the continuous Gaussian formulation for differentiable optimization. As shown in Tab. 5 Upsample Anything achieves the best balance between speed, convergence, and accuracy, demonstrating that the JBU constraint synergizes effectively with Gaussian optimization for fast and stable test-time refinement.

Impact of Test-Time Optimization Steps We conducted experiments to investigate the trade-off between the number of TTO iterations, inference time, and performance. Table 6 summarizes the results. We measured PSNR between \( I_{lr} \) and \( \hat{I}_{hr} \), along with downstream segmentation perfor-

[tbl-5.html](tbl-5.html)

Table 6. Ablation on the number of optimization iterations.

mance on PASCAL-VOC. As shown, PSNR quickly converges to 35.60 after about 500 iterations, indicating that Upsample Anything reaches its optimum very early. Interestingly, the best segmentation accuracy is achieved at only 50 iterations, which also provides the fastest inference time (0.419s). Based on this observation, we adopt 50 iterations as the default setting throughout all experiments.

## 6. Conclusion

We introduced Upsample Anything, a unified framework that connects Joint Bilateral Upsampling (JBU) and Gaussian Splatting (GS) under a continuous formulation. It performs lightweight test-time optimization without pretraining or architectural constraints, achieving efficient and robust upsampling across diverse resolutions and domains. It optimizes a  \( 224 \times 224 \)  image in 0.419 seconds while producing significant gains in both feature and depth upsampling. Extensive experiments show that Upsample Anything achieves state-of-the-art performance without any learnable module, serving as a universal, plug-and-play framework that combines the simplicity of JBU with the expressive power of Gaussian representation. Limitation. Despite its generality, Upsample Anything may face challenges under severe occlusions or low-SNR guidance, where optimization becomes unstable. Future work will focus on enhancing the robustness and adaptability of the framework across diverse domains, aiming to make it more resilient under challenging conditions.

[OCR table id=tbl-4.html; page=8]
<table><tr><td rowspan="2">Method</td><td rowspan="2">Time (s)</td><td colspan="2">PASCAL-VOC (Segmentation)</td><td colspan="2">NYUv2 (Depth Estimation)</td></tr><tr><td>mIoU (↑)</td><td>Acc. (↑)</td><td>RMSE (↓)</td><td>\( \lambda_1 \)(↑)</td></tr><tr><td>Bilinear</td><td>0.00009</td><td>81.27</td><td>95.96</td><td>0.545</td><td>0.804</td></tr><tr><td>Guided Linear Upsample</td><td>0.00303</td><td>80.12</td><td>94.73</td><td>0.598</td><td>0.773</td></tr><tr><td>JBU</td><td>0.00600</td><td>81.65</td><td>96.21</td><td>0.531</td><td>0.812</td></tr><tr><td>LIG</td><td>481.526</td><td>78.54</td><td>93.02</td><td>0.642</td><td>0.741</td></tr><tr><td>GSJBU (Ours)</td><td>0.4197</td><td>82.22</td><td>96.90</td><td>0.498</td><td>0.829</td></tr></table>

[OCR table id=tbl-5.html; page=8]
<table><tr><td rowspan="2">Iteration</td><td rowspan="2">PSNR (↑)</td><td colspan="2">PASCAL-VOC (Segmentation)</td><td rowspan="2">Time (s)</td></tr><tr><td>mIoU (↑)</td><td>Acc. (↑)</td></tr><tr><td>50</td><td>35.33</td><td>82.22</td><td>96.90</td><td>0.041</td></tr><tr><td>300</td><td>35.59</td><td>82.10</td><td>96.84</td><td>3.397</td></tr><tr><td>500</td><td>35.60</td><td>82.15</td><td>96.88</td><td>6.161</td></tr><tr><td>1000</td><td>35.60</td><td>82.10</td><td>96.82</td><td>12.294</td></tr><tr><td>5000</td><td>35.60</td><td>82.17</td><td>96.80</td><td>61.458</td></tr></table>

## B-ocr-6c72a532da401d

B PDF page 14

In summary, AnyUp demonstrates higher robustness under corrupted or low-SNR conditions, whereas our Upsample Anything excels when inputs are visually clean or when handling multi-modal signals such as RGB-D or 3D features.

## References

[1] Mathilde Caron, Hugo Touvron, Ishan Misra, Hervé Jégou, Julien Mairal, Piotr Bojanowski, and Armand Joulin. Emerging properties in self-supervised vision transformers. In Proceedings of the IEEE/CVF international conference on computer vision, pages 9650–9660, 2021. 2

[2] Marius Cordts, Mohamed Omran, Sebastian Ramos, Timo Rehfeld, Markus Enzweiler, Rodrigo Benenson, Uwe Franke, Stefan Roth, and Bernt Schiele. The cityscapes dataset for semantic urban scene understanding. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 3213–3223, 2016. 1

[3] Paul Couairon, Loick Chambon, Louis Serrano, Jean-Emmanuel Haugeard, Matthieu Cord, and Nicolas Thome. Jafar: Jack up any feature at any resolution. arXiv preprint arXiv:2506.11136, 2025. 2, 3, 5

[4] Alexey Dosovitskiy. An image is worth 16x16 words: Transformers for image recognition at scale. arXiv preprint arXiv:2010.11929, 2020. 2

[5] Mark Everingham, Luc Van Gool, Christopher KI Williams, John Winn, and Andrew Zisserman. The pascal visual object classes (voc) challenge. International journal of computer vision, 88(2):303–338, 2010. 1

[6] Stephanie Fu, Mark Hamilton, Laura E. Brandt, Axel Feldmann, Zhoutong Zhang, and William T. Freeman. Featup: A model-agnostic framework for features at any resolution. In The Twelfth International Conference on Learning Representations, 2024. 2, 3, 5

[7] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 770–778, 2016. 2

[8] Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, and Ross Girshick. Masked autoencoders are scalable vision learners. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 16000-16009, 2022. 2

[9] Binbin Huang, Zehao Yu, Anpei Chen, Andreas Geiger, and Shenghua Gao. 2d gaussian splatting for geometrically accurate radiance fields. In ACM SIGGRAPH 2024 conference papers, pages 1–11, 2024. 7

[10] Haiwen Huang, Anpei Chen, Volodymyr Havrylov, Andreas Geiger, and Dan Zhang. Loftup: Learning a coordinate-based feature upsampler for vision foundation models, 2025. 2, 3, 5, 1

[11] Bingxin Ke, Anton Obukhov, Shengyu Huang, Nando Metzger, Rodrigo Caye Daudt, and Konrad Schindler. Repurposing diffusion-based image generators for monocular depth estimation. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 9492–9502, 2024. 1

[12] Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, and George Drettakis. 3d gaussian splatting for real-time radiance field rendering. ACM Trans. Graph., 42(4):139–1, 2023. 3

[13] Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi Mao, Chloe Rolland, Laura Gustafson, Tete Xiao, Spencer Whitehead, Alexander C Berg, Wan-Yen Lo, et al. Segment anything. In Proceedings of the IEEE/CVF international conference on computer vision, pages 4015–4026, 2023. 2

[14] Johannes Kopf, Michael F Cohen, Dani Lischinski, and Matt Uyttendaele. Joint bilateral upsampling. ACM Transactions on Graphics (ToG), 26(3):96–es, 2007. 3, 4

[15] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, and C Lawrence Zitnick. Microsoft coco: Common objects in context. In European conference on computer vision, pages 740–755. Springer, 2014. 1

[16] Zhuang Liu, Hanzi Mao, Chao-Yuan Wu, Christoph Feichtenhofer, Trevor Darrell, and Saining Xie. A convnet for the 2020s. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 11976–11986, 2022. 2

[17] Maxime Oquab, Timothée Darcet, Théo Moutakanni, Huy Vo, Marc Szafraniec, Vasil Khalidov, Pierre Fernandez, Daniel Haziza, Francisco Massa, Alaaeldin El-Nouby, et al. Dinov2: Learning robust visual features without supervision. arXiv preprint arXiv:2304.07193, 2023. 2

[18] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual models from natural language supervision. In International conference on machine learning, pages 8748–8763. PmLR, 2021. 2

[19] René Ranftl, Alexey Bochkovskiy, and Vladlen Koltun. Vision transformers for dense prediction. In Proceedings of the IEEE/CVF international conference on computer vision, pages 12179–12188, 2021. 2

[20] Nathan Silberman, Derek Hoiem, Pushmeet Kohli, and Rob Fergus. Indoor segmentation and support inference from rgbd images. In European conference on computer vision, pages 746–760. Springer, 2012. 1

[21] Shuangbing Song, Fan Zhong, Tianju Wang, Xueying Qin, and Changhe Tu. Guided linear upsampling. ACM Transactions on Graphics (TOG), 42(4):1–12, 2023. 6, 7

[22] Saksham Suri, Matthew Walmer, Kamal Gupta, and Abhinav Shrivastava. Lift: A surprisingly simple lightweight feature transform for dense vit descriptors. In European Conference on Computer Vision, pages 110–128. Springer, 2024. 2, 3, 5

[23] Thomas Wimmer, Prune Truong, Marie-Julie Rakotosaona, Michael Oechsle, Federico Tombari, Bernt Schiele, and Jan Eric Lenssen. Anyup: Universal feature upsampling. arXiv preprint arXiv:2510.12764, 2025. 2, 3, 5, 7, 1

[24] Tete Xiao, Yingcheng Liu, Bolei Zhou, Yuning Jiang, and Jian Sun. Unified perceptual parsing for scene understanding. In Proceedings of the European conference on computer vision (ECCV), pages 418–434, 2018. 2

[25] Enze Xie, Wenhai Wang, Zhiding Yu, Anima Anandkumar, Jose M Alvarez, and Ping Luo. Segformer: Simple and

## B-ocr-8d78315f9c0b3b

B PDF page 6

[tbl-1.html](tbl-1.html)

Table 2. Comparison of depth and surface normal estimation on the NYUv2 dataset.

samples probabilities to the original image size using our method. Because the logits/probabilities live on a much smaller spatial grid, this pipeline achieves the lowest computational cost yet delivers the highest accuracy in Table 1. This suggests a promising paradigm for segmentation: upsample task probabilities rather than intermediate features.

Depth Estimation We evaluate our method on the NYUv2 dataset using a frozen DINOv2 backbone. Following prior works (AnyUp, LoftUp), we adopt a lightweight DPT-style decoder head for dense prediction (details in Appendix). Unlike the original DPT, our Upsample Anything removes the internal interpolation layers, as the feature maps are already upsampled to high resolution. As shown in Table 2, Upsample Anything achieves the best performance on both depth and surface normal estimation (RMSE 0.498, δ₁ 0.829, mean 21.5°), indicating that precise feature upsampling is particularly beneficial for geometry-oriented tasks, while LoftUp suffers from domain gaps and fails to generalize. It appears that feature upsampling plays a more critical role in depth and surface normal estimation than in semantic segmentation.

Depth Map Upsampling Unlike feature upsampling tasks, our Upsample Anything can also be applied to other modalities such as raw depth maps. In Table 3, we evaluate Upsample Anything by downsampling high-resolution depth maps to 32×32 and restoring them to 512×512 resolution. This setup shares the same bilateral upsampling pipeline as our feature experiments, except that the low-resolution input is a depth map itself. We compare against the state-of-the-art guided interpolation method (GLU) [21] and the bilinear baseline. As shown in Figure 4, Upsample Anything achieves the best performance on the Middlebury dataset, producing sharper and more consistent structures. In contrast, on the NYUv2 dataset, the bilinear method yields a slightly lower RMSE (0.159 vs. 0.237), likely because the ground-truth depth maps are blurred and contain smoother structures. Nevertheless, the qualitative results suggest that Upsample Anything preserves geometry more effectively, especially for high-frequency and edge-dominant regions.

[tbl-2.html](tbl-2.html)

Table 3. Comparison on NYUv2 and Middlebury depth upsampling.

![img-12.jpeg](img-12.jpeg)

Figure 4. Depth upsampling results on Middlebury (top) and NYUv2 (bottom). 32×32 low-resolution depth maps were upsampled to high resolution using different methods. While Upsample Anything produces sharper and more detailed edges, it still achieves lower RMSE (0.237) than bilinear (0.159) on low-resolution maps. However, in high-resolution depth prediction, Upsample Anything outperforms both qualitatively and quantitatively.

### 5.4. Qualitative results

Across Different Resolutions. Figure 5 compares AnyUp (previous SOTA) and our Upsample Anything across different input resolutions. As shown, AnyUp performs reasonably well at higher resolutions (e.g., 32×32 and 16×16) but tends to produce over-smoothed regions, as highlighted by the red boxes. In contrast, Upsample Anything maintains sharp boundaries and fine structures even at extremely low resolutions (e.g., 7×7 and 4×4), demonstrating stronger robustness to spatial degradation.

Across Different Backbones. We compare the visual quality of upsampled features produced by AnyUP and our Upsample Anything across various backbone architectures. Given the 224×224 input image, the spatial resolutions of the extracted feature maps differ by model: 7×7 for ConvNeXt, 14×14 for CLIP and DINOv1, and 16×16 for DINOv2 and DINOv3. In this example, I_HR denotes the reconstructed high-resolution image obtained from a 7×7 low-resolution I_LR using Upsample Anything. As shown in Fig. 6, Upsample Anything consistently produces sharper boundaries, finer local structures, and more coherent feature clustering than AnyUP across all backbones. We attribute this advantage to Upsample Anything's test-time optimization, which adaptively fits Gaussian parameters to each in-

[OCR table id=tbl-1.html; page=6]
<table><tr><td rowspan="2">Method</td><td colspan="2">Depth Estimation</td><td colspan="5">Surface Normal Estimation</td></tr><tr><td>RMSE (↓)</td><td>δ₁ (↑)</td><td>Mean (↓)</td><td>Median (↓)</td><td>&lt;11.25° (↑)</td><td>&lt;22.5° (↑)</td><td>&lt;30° (↑)</td></tr><tr><td>Bilinear</td><td>0.545</td><td>0.804</td><td>23.8</td><td>19.5</td><td>33.0</td><td>70.0</td><td>81.0</td></tr><tr><td>FeatUp</td><td>0.523</td><td>0.810</td><td>22.7</td><td>18.6</td><td>35.5</td><td>72.3</td><td>83.0</td></tr><tr><td>LoftUp</td><td>0.796</td><td>0.789</td><td>28.9</td><td>24.1</td><td>25.0</td><td>58.0</td><td>71.0</td></tr><tr><td>JAFAR</td><td>0.521</td><td>0.807</td><td>25.2</td><td>19.0</td><td>34.0</td><td>70.8</td><td>82.0</td></tr><tr><td>AnyUp</td><td>0.513</td><td>0.817</td><td>22.2</td><td>18.1</td><td>36.8</td><td>75.5</td><td>84.1</td></tr><tr><td>Upsample Anything (Ours)</td><td>0.498</td><td>0.829</td><td>21.5</td><td>17.4</td><td>38.1</td><td>75.2</td><td>85.8</td></tr></table>

[OCR table id=tbl-2.html; page=6]
<table><tr><td rowspan="2">Method</td><td colspan="2">NYUv2 (Depth Up.)</td><td colspan="2">Middlebury (Depth Up.)</td></tr><tr><td>RMSE (↓)</td><td>δ₁ (↑)</td><td>RMSE (↓)</td><td>δ₁ (↑)</td></tr><tr><td>Bilinear</td><td>0.167</td><td>0.983</td><td>0.231</td><td>0.962</td></tr><tr><td>GLU (Guided Linear Upsample)</td><td>0.372</td><td>0.841</td><td>0.491</td><td>0.825</td></tr><tr><td>Upsample Anything (Ours)</td><td>0.214</td><td>0.976</td><td>0.209</td><td>0.967</td></tr></table>

## B-ocr-adf71609ec0a4c

B PDF page 3

Gaussian parameters—$(\sigma_x, \sigma_y, \theta, \sigma_r)$—that define a continuous spatial-range splatting kernel. These optimized kernels are then applied to the LR feature maps from a foundation encoder to produce HR feature maps aligned with the original image grid. Although the optimization is guided only by color reconstruction, the learned kernels implicitly capture geometry and semantics. As a result, Upsample Anything not only enhances 2D feature resolution but also generalizes to other pixel- or voxel-level signals (e.g., depth, segmentation, or even 3D representations) without retraining. This property highlights its potential as a unified, lightweight, and resolution-free upsampling operator across 2D and 3D domains. Despite requiring no dataset-level training, it consistently achieves state-of-the-art or near-SOTA performance on multiple pixel-level benchmarks, including semantic segmentation and depth estimation.

## 2. Related Works

### 2.1. Joint Bilateral Upsampling

Joint Bilateral Upsampling (JBU), first introduced by [14], is a classic non-learning, edge-preserving upsampling technique designed to transfer structural details from a high-resolution guidance image to a low-resolution signal such as a depth map or label map. Formally, JBU computes each high-resolution output pixel $\hat{F}hr[p]$ as a weighted average of nearby low-resolution pixels $Flr[q]$, as follows:

$$\hat{F}_{hr}[p] = \frac{1}{Z_p} \sum_{q \in \Omega(p)} F_{lr}[q] \exp\left(-\frac{\|p-q\|^2}{2\sigma_s^2}\right) \exp\left(-\frac{\|I[p]-I[q]\|^2}{2\sigma_r^2}\right), \tag{1}$$

where $I$ denotes the high-resolution guidance image, and $\sigma_s, \sigma_r$ control the spatial and range sensitivity, respectively. Here, $Z_p$ is a normalization factor ensuring that all weights sum to one, and $\Omega(p)$ denotes the spatial neighborhood around pixel $p$ in the low-resolution domain. By coupling spatial proximity and color similarity, JBU preserves edges and fine details while interpolating missing information, enabling high-quality restoration of dense signals without any additional learning. This formulation has inspired numerous modern variants and learnable extensions that generalize bilateral filtering [6] to feature space and neural representations. Although JBU performs upsampling without any training, the resulting quality remains limited due to its fixed, hand-crafted kernel design.

### 2.2. Feature Upsampling

A pioneering work in feature upsampling is FeatUp [6], which proposed two model-agnostic modules: FeatUp (JBU) and FeatUp (Implicit). The former generalizes Joint Bilateral Upsampling (JBU) [14] to high-dimensional feature space by replacing the fixed Gaussian range kernel with a learnable MLP, while the latter parameterizes high-resolution features as an implicit function $F_{hr} = \text{MLP}(x, I(x))$ optimized per image. While FeatUp effec-

tively restores spatial detail from foundation features, it either requires dataset-level training or incurs long per-image optimization.

Several follow-up studies further improved spatial fidelity through learnable upsamplers. LiFT [22] employed a lightweight U-Net-like upsampler with reconstruction loss, LoftUp [10] integrated RGB coordinates via cross-attention with pseudo-groundtruth supervision, and JAFAR [3] introduced joint-attention filtering for semantic-structural alignment. AnyUp [23] proposed resolution-conditioned kernels for scalable upsampling. Despite their strong performance, these methods rely on dataset-level training, which makes them less adaptive to unseen domains. They often generalize reasonably well but still exhibit suboptimal performance when facing novel architectures, resolutions, or out-of-distribution data.

## 3. Preliminaries

2D Gaussian Splatting (2DGS). Recent works extend 3D Gaussian Splatting (3DGS) [12] from volumetric radiance fields to 2D image representations [28, 29, 32]. In the image-plane setting, a pixel or small region is represented by a Gaussian kernel

$$G_i(x) = \exp\left(-\frac{1}{2}(x - \mu_i)^\top \Sigma_i^{-1}(x - \mu_i)\right), \tag{2}$$

where $\mu_i \in \mathbb{R}^2$ is the center, $\Sigma_i \in \mathbb{R}^{2 \times 2}$ is a positive-definite covariance (encoding scale and orientation), and $\alpha_i$ is a per-kernel weight. The rendered image (or feature map) is obtained by normalized alpha blending:

$$I(x) = \sum_i w_i, c_i, \quad w_i = \frac{\alpha_i G_i(x)}{\sum_j \alpha_j G_j(x)}, \tag{3}$$

with $c_i$ the color or feature associated with kernel $i$. Because all kernels lie on a single 2D plane, rendering reduces to a normalized weighted summation without depth sorting. This process is often described as rasterization/alpha blending and can also be interpreted as a spatially varying anisotropic convolution. This property enables real-time, pose-free optimization directly in 2D image/feature domains.

Relation to Joint Bilateral Upsampling (JBU). JBU [14] computes each high-resolution (HR) output $F_{hr}(p)$ as a normalized weighted average of low-resolution (LR) samples $F_{lr}(q)$, where the weights depend on both spatial proximity and guidance-image similarity (see Eq. 1). Viewed geometrically, each LR sample $q$ can be regarded as a Gaussian centered at $\mu_q = q$ with an isotropic covariance $\Sigma_q = \sigma_s^2 I$. Under this view, JBU corresponds to a discrete and isotropic instance of a guidance-modulated 2D Gaussian Splatting (2DGS) process, where the range

## B-ocr-c1c5112406d944

B PDF page 2

Step1. Training Upsampler

![img-8.jpeg](img-8.jpeg)

Step2. Inference (Task-specific inference only)

![img-9.jpeg](img-9.jpeg)

(a) Dataset-Level Training Method

Step1. Test-time Optimization & Inference

![img-10.jpeg](img-10.jpeg)

(b) Upsample Anything (Ours)

Figure 2. Comparison of dataset-level training and our test-time optimization (TTO). (a) Dataset-level methods (FeatUp, LoftUp, JAFAR, AnyUp) require paired training data and handle only 2D feature maps. (b) Our Upsample Anything performs TTO using only one HR image and generalizes to feature, depth, segmentation, and even 3D features.

erarchical features that capture semantic abstraction from the input image, and the decoder reconstructs dense, task-specific predictions such as class maps, depth, or optical flow at the original spatial resolution.

Recent advances in large-scale self-supervised learning [1, 8, 17, 18, 27, 31] introduce general-purpose encoders called Vision Foundation Models (VFMs) that can serve as universal backbones across diverse downstream tasks. This paradigm shift has led to the emergence of Vision Foundation Models (VFMs) such as DINO [17], CLIP [18], SigLIP [27], and MAE [8], which provide transferable and semantically rich features with minimal task-specific fine-tuning.

By decoupling the encoder from the downstream task, these foundation models dramatically reduce the data and training costs needed for adaptation while maintaining strong generalization across domains. However, despite these advantages, high-performing pixel-level systems still require large and complex decoders such as DPT [19], UPerNet [24], or SegFormer [25] to recover spatial details from low-resolution features. Foundation features are typically downsampled by a factor of 14-16 in Vision Transformer [4] architectures or equivalently through multiple pooling stages in CNN-based backbones [7, 16]. As a result, they lack fine-grained spatial information, forcing decoders to rely on heavy upsampling networks that are computationally expensive, memory-intensive, and often difficult to generalize to new architectures or resolutions.

To address this resolution gap, a growing line of research has explored feature upsampling methods [3, 6, 10, 22, 23] to restore spatial details in pretrained representations without modifying the encoder. These methods learn an upsampling operator that maps low-resolution foundation features to higher resolutions, effectively bridging the seman-

tic–spatial gap before the downstream decoder. In doing so, they can achieve strong performance across diverse pixel-level tasks even with a single 1×1 convolutional decoder.

Feature upsampling approaches can be broadly categorized into two paradigms depending on how the upsampler is optimized: (a) dataset-level training [3, 6, 10, 22, 23] and (b) test-time optimization (TTO) [6], as illustrated in Fig. 2. In the dataset-level training paradigm, the feature upsampler is trained on a target dataset either by generating pseudo-labels using methods such as SAM [13] for zero-shot supervision [10] or by adopting multi-view training objectives [3, 6, 22, 23].

While this approach can generalize to certain unseen data, it still requires dataset-level training, meaning that the upsampler must be retrained whenever the backbone architecture or target dataset changes. Moreover, due to heavy memory usage, most trained upsamplers can only operate up to 112–224 pixels in resolution. The test-time optimization paradigm, exemplified by methods such as FeatUp (Implicit), avoids dataset-level training by optimizing the feature upsampler directly at inference time for each test image. Although this removes the need for offline training, the per-image optimization is computationally expensive, taking an average of 49 seconds to converge for a 224-sized image.

We propose Upsample Anything, a test-time optimization (TTO) framework for feature upsampling, as illustrated in Fig. 2-(b). Unlike previous methods requiring dataset-level training, it performs lightweight per-image optimization and processes a 224-sized image in only ≈ 0.419 s. Given an input image, Upsample Anything resizes the RGB guidance to match the low-resolution (LR) feature-map size, reconstructs the high-resolution (HR) color image through optimization, and learns pixelwise anisotropic

## B-ocr-c66111fe2bac0e

B PDF page 12

![img-51.jpeg](img-51.jpeg)

Figure 11. Visualization of the segment-then-upsample pipeline. The segmentation logits are first generated at low resolution and then upsampled by  \( 16\times \)  using our method. The results exhibit remarkably sharp object boundaries and preserve semantic coherence, highlighting the effectiveness of our upsampling approach.

Corollary 1 (Discrete GS view in the joint domain). Let \(\mu_q := \phi(q)\) and \(f_q := F_{\mathrm{lr}}(q)\). Then Theorem 1 states that JBU equals

\[
\hat {F} _ {\mathrm{lr}} (p) = \frac {\sum_ {q} f _ {q} \exp \left(- \frac {1}{2} (\phi (p) - \mu_ {q}) ^ {\top} \Lambda^ {- 1} (\phi (p) - \mu_ {q})\right)}{\sum_ {q} \exp \left(- \frac {1}{2} (\phi (p) - \mu_ {q}) ^ {\top} \Lambda^ {- 1} (\phi (p) - \mu_ {q})\right)}, \tag {10}
\]

i.e., a Gaussian Splatting evaluation in  \( R^{2+d} \)  with fixed block-diagonal covariance and centers on the lifted LR grid.

Connection to standard 2D GS. Standard (2D) GS writes, for  \( p \in R^{2} \) ,

\[
F (p) = \frac {\sum_ {i} \alpha_ {i} \exp \left(- \frac {1}{2} (p - \tilde {\mu} _ {i}) ^ {\top} \hat {\Sigma} _ {i} ^ {- 1} (p - \tilde {\mu} _ {i})\right) \tilde {f} _ {i}}{\sum_ {j} \alpha_ {j} \exp \left(- \frac {1}{2} (p - \tilde {\mu} _ {j}) ^ {\top} \hat {\Sigma} _ {j} ^ {- 1} (p - \tilde {\mu} _ {j})\right)}. \tag {11}
\]

The range term in JBU can be absorbed by lifting to the joint domain (Theorem 1), or, equivalently, by keeping the domain 2D and letting the amplitude be query-dependent, \(\alpha_{i}(p) = \exp \left(-\frac{\|I(p) - I(\tilde{\mu}_{i})\|^{2}}{2\sigma_{r}^{2}}\right)\). The former is strictly query-independent and thus mathematically cleaner; the latter matches common GS implementations with view-dependent weights.

Theorem 2 (Specialization of GSJBU to JBU (isotropic limit)). Consider the anisotropic per-center model:

\[
F (p) = \frac {\sum_ {q} f _ {q} \exp \left(- \frac {1}{2} (p - q) ^ {\top} \Sigma_ {q} ^ {- 1} (p - q)\right) \beta_ {q} (p)}{\sum_ {q} \exp \left(- \frac {1}{2} (p - q) ^ {\top} \Sigma_ {q} ^ {- 1} (p - q)\right) \beta_ {q} (p)}, \tag {12}
\]

\[
\beta_ {q} (p) := \exp \big (- \frac {\| I (p) - I (q) \| ^ {2}}{2 \sigma_ {r} ^ {2} (q)} \big).
\]

If \(\Sigma_q \to \sigma_s^2 I_2\) and \(\sigma_r(q) \to \sigma_r\) for all \(q\), then (12) reduces exactly to JBU (1).

Proof. Substitute  \( \Sigma_{q} = \sigma_{s}^{2}I_{2} \)  and  \( \sigma_{r}(q) = \sigma_{r} \)  into (12) to recover the numerator/denominator of (1). ☐

Proposition 1 (Discrete-to-continuous convergence). Assume \( F_{\mathrm{lr}} \) admits a bandlimited (or Lipschitz-continuous) interpolation \( \hat{F} : \Omega \to \mathbb{R}^C \), and let the LR grid spacing be \( \Delta x \). Then as \( \Delta x \to 0 \),

\[
\sum_ {q} \hat {F} (q) \mathcal {G} _ {\Lambda} (\phi (p), \phi (q)) (\Delta x) ^ {2} \longrightarrow \int_ {\Omega} \hat {F} (x) \mathcal {G} _ {\Lambda} (\phi (p), \phi (x)) d x, \tag {13}
\]

and the corresponding normalized ratios converge as well. Hence, discrete JBU converges to its continuous lifted-domain GS counterpart.

Sketch.  \( \mathcal{G}_{\Lambda}(\phi(p),\phi(\cdot)) \)  is bounded and continuous for fixed p. Under the stated regularity, Riemann sums converge to the integral

## B-ocr-c68a74efbe4c08

B PDF page 7

![img-13.jpeg](img-13.jpeg)

\(I_{\mathrm{AM}}(512\times 512)\)

![img-14.jpeg](img-14.jpeg)

\(F_{LR}(32\times 32)\)

![img-15.jpeg](img-15.jpeg)

AnyUP

![img-16.jpeg](img-16.jpeg)

Ours

![img-17.jpeg](img-17.jpeg)

\(F_{LR}(16\times 16)\)

![img-18.jpeg](img-18.jpeg)

AnyUP

![img-19.jpeg](img-19.jpeg)

Ours

![img-20.jpeg](img-20.jpeg)

\(F_{LR}(7\times 7)\)

![img-21.jpeg](img-21.jpeg)

AnyUP

![img-22.jpeg](img-22.jpeg)

Ours

![img-23.jpeg](img-23.jpeg)

\(F_{LR}(4\times 4)\)

![img-24.jpeg](img-24.jpeg)

AnyUP

![img-25.jpeg](img-25.jpeg)

Ours

Figure 5. Comparison across different resolutions. Qualitative results of AnyUp (previous SOTA) and our Upsample Anything on varying input resolutions.

put image, yielding features that align more precisely with image-level semantics.

Feature Similarity Analysis. Fig. 7 visualizes the feature similarity between two different images that share the same object category. This setting is often adopted in few-shot segmentation tasks to assess the consistency of feature representations. As shown in the figure, both AnyUp and Upsample Anything produce visually plausible feature upsampling results; however, when measuring cosine similarity, AnyUp tends to yield uniformly high similarity across the entire image, indicating a lack of spatial discrimination. In contrast, our Upsample Anything produces sharper and more localized similarity maps, where object boundaries are clearly preserved and distinct regions are well separated. We believe that such discriminative feature behavior suggests the potential of our method for downstream tasks such as few-shot segmentation and category-level feature matching.

### 5.5. Ablation Study

Resolution–Efficiency Tradeoff We analyze the computational efficiency of our Upsample Anything compared with AnyUp [23] across multiple output resolutions, as summarized in Table 4. AnyUp employs a feature-agnostic layer and local window attention that allow flexible inference across arbitrary encoders and resolutions. While this design yields fast performance at lower resolutions (<256 × 256), the window-based attention and dense similarity computation introduce quadratic growth in both memory and time complexity as the spatial size increases. Consequently, AnyUp suffers from significant GPU memory overhead and fails with out-of-memory (OOM) errors beyond 512 × 512, exposing a scalability bottleneck in its dense attention formulation.

In contrast, our Upsample Anything performs fully parallel anisotropic Gaussian splatting without building dense

[tbl-3.html](tbl-3.html)

Table 4. comparison of inference time and GPU memory usage between AnyUp and Upsample Anything under varying input resolutions. Both methods operate without training, but Upsample Anything performs per-image test-time optimization (TTO), which results in slightly higher computational cost but significantly improved generalization.

pairwise affinity maps, resulting in linear memory growth with respect to the output size. As shown in Table 4, Upsample Anything maintains stable runtime and controlled memory even at  \( 1024 \times 1024 \)  resolution—where AnyUp cannot execute—demonstrating its robustness for large-scale feature upsampling.

Why Upsample Anything: Design Motivation and Comparative Analysis In our architecture search, we aimed to achieve accurate upsampling within one second while maintaining generalization across domains. Tab. 5 compares different upsampling strategies on PASCAL-VOC and NYUv2 benchmarks. Guided Linear Upsampling (GLU) [21] represents a strong bilateral-filter-based baseline but exhibits unstable optimization due to its unconstrained formulation. We also implemented a 2D Gaussian Splatting (2DGS) [9] baseline by directly optimizing Gaussian kernels for low-to-high feature interpolation without hierarchical fitting. Although 2DGS can model local structures continuously, its dense Gaussian representation and lack of spatial-range constraints make it computationally heavy and prone to

[OCR table id=tbl-3.html; page=7]
<table><tr><td>Resolution (H×W)</td><td>AnyUp (trained) / Ours (TTA) Time (s)</td><td>AnyUp (trained) / Ours (TTA) Peak Mem (MB)</td></tr><tr><td>64×64</td><td>0.0025 / 0.0055</td><td>53.8 / 358.5</td></tr><tr><td>128×128</td><td>0.0034 / 0.0150</td><td>121.9 / 1320.5</td></tr><tr><td>224×224</td><td>0.0137 / 0.0419</td><td>531.0 / 3969.7</td></tr><tr><td>448×448</td><td>0.0583 / 0.2398</td><td>6184.2 / 15774.8</td></tr><tr><td>512×512</td><td>0.0893 / 0.3211</td><td>10283.8 / 20590.4</td></tr><tr><td>896×896</td><td>0.5875 / 1.2789</td><td>91250.9 / 62985.2</td></tr><tr><td>1024×1024</td><td>OOM / 1.8083</td><td>— / 82255.5</td></tr><tr><td>2048×2048</td><td>OOM / OOM</td><td>— / —</td></tr></table>

## B-ocr-d3dc77f3923e2c

B PDF page 9

# Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling

Supplementary Material

## 7. Semantic Segmentation on Cityscapes

We evaluated feature upsampling and probability-map upsampling on Cityscapes using the official LoftUp segmentation codebase with a stronger training setup that includes 448×448 input resolution, 100 epochs, and a learning-rate scheduler. Under this configuration, all methods, including LoftUp and ours, produced almost the same mIoU as bilinear interpolation, which differs from the improvements reported in the LoftUp paper.

To ensure correctness, we carefully re-examined our implementation through an automated code audit with ChatGPT and a manual review by multiple authors. We found no inconsistencies or bugs.

The quantitative results are summarized in Table 7. Across all methods, including feature-level and probability-level upsampling, the differences remain within a very narrow range. Cityscapes primarily contains large and regular structures, and its annotations are relatively coarse. With a sufficiently trained segmentation head, bilinear interpolation already performs near optimally, leaving little room for additional gains. In contrast, datasets such as COCO, PASCAL-VOC, and ADE20K include many small objects and complex boundaries, where upsampling delivers clear benefits.

[tbl-6.html](tbl-6.html)

Table 7. Segmentation performance on the Cityscapes dataset using the official LoftUp evaluation pipeline.

## 8. Details of Probabilistic Map Upsampling in Table 1.

Figure 8-(c) corresponds to the Upsample Anything (prob.) configuration reported in Table 1. In this setting, the segmentation map is predicted from downsampled features using a lightweight 1×1 convolution, followed by our prob-

![img-28.jpeg](img-28.jpeg)

(a) Conventional Segmentation pipeline

![img-29.jpeg](img-29.jpeg)

(b) Feature Upsampling for Segmentation Pipeline

![img-30.jpeg](img-30.jpeg)

(c) Upsample Anything Segmentation Pipeline

Figure 8. Comparison of segmentation pipelines. (a) Conventional segmentation pipeline with a Vision Foundation Model encoder and task-specific decoders such as DPT, UPerNet, SegFormer, or Mask2Former. (b) Feature upsampling pipeline using pretrained upsamplers such as FeatUP, LoftUP, JAFAR, or AnyUp, operating on feature maps. (c) Our proposed Upsample Anything, which performs test-time optimization and handles both feature and segmentation upsampling without additional training.

abilistic upsampling to reconstruct high-resolution outputs. This simple setup already shows strong performance. Because the computation is performed on a small feature map, heavier or more complex decoders are expected to be feasible without large computational overhead. This suggests that the proposed segmentation pipeline has further potential, although designing such decoders is beyond the scope of this work.

## 9. Details of Depth Estimation in Table 2.

We followed the DPT-based depth estimation setup used in prior works [10, 23]. Although DPT includes an internal up-

[OCR table id=tbl-6.html; page=9]
<table><tr><td rowspan="2">Method</td><td colspan="2">Cityscapes</td></tr><tr><td>mIoU (↑)</td><td>Acc. (↑)</td></tr><tr><td>Bilinear</td><td>57.90</td><td>90.59</td></tr><tr><td>FeatUp</td><td>57.92</td><td>90.61</td></tr><tr><td>LoftUp</td><td>57.89</td><td>90.60</td></tr><tr><td>JAFAR</td><td>57.91</td><td>90.58</td></tr><tr><td>AnyUp</td><td>57.93</td><td>90.62</td></tr><tr><td>Upsample Anything</td><td>57.92</td><td>90.63</td></tr><tr><td>Upsample Anything (prob.)</td><td>56.36</td><td>90.05</td></tr></table>

## B-ocr-dfa0937c25962c

B PDF page 4

![img-11.jpeg](img-11.jpeg)

Figure 3. Overview of Upsample Anything. Given a high-resolution image \( I_{hr} \), we downsample it to \( I_{lr} \) and optimize GSJBU to reconstruct \( I_{hr} \), learning per-pixel anisotropic kernels \( \{\sigma_x, \sigma_y, \theta, \sigma_r\} \) via test-time optimization (TTO). The learned kernels are then applied to foundation features \( F_{lr} \) for rendering the high-resolution features \( F_{hr} \), achieving pixel-wise anisotropic joint bilateral upsampling.

term is provided by the HR guidance image. In contrast, Upsample Anything assigns per-pixel anisotropic covariances  \( \Sigma_{p} \)  and range scales  \( \sigma_{r,p} \)  through test-time optimization, enabling adaptive fusion across space and range. This pixel-level Gaussian parameterization captures locally varying orientations and scales, making Upsample Anything a continuous, edge-preserving extension of JBU within the 2DGS framework. For the exact derivation and a more formal discussion of how this formulation differs from a simple combination, please refer to Appendix §12.

## 4. Methods

### 4.1. Overview

As illustrated in Fig. 3, our method, Upsample Anything, consists of two stages: (i) test-time optimization (TTO) and (ii) feature rendering. In the TTO stage, Upsample Anything learns per-pixel anisotropic Gaussian parameters \(\{\sigma_x,\sigma_y,\theta ,\sigma_r\}\) by reconstructing the high-resolution image \(I_{hr}\) from its patch-wise downsampled version \(I_{lr}\). This process enables each pixel to learn how spatially and photometrically similar neighbors should be blended-effectively discovering local mixing weights that generalize beyond the image domain. Once optimized, these Gaussian kernels are directly transferred to the foundation feature space, where the low-resolution feature map \(F_{lr}\in \mathbb{R}^{C\times H / s\times W / s}\) is splatted to produce the high-resolution feature \(F_{hr}\in \mathbb{R}^{C\times H\times W}\) using the same learned anisotropic weighting mechanism. Because the splatting weights depend only on spatial-range similarity, this transfer is naturally domain-agnostic, allowing the learned kernels to act as universal upsampling operators. Excluding the feature extraction time of the Vision Foundation Model (VFM), the entire optimization and inference for a \(224\times 224\) image takes \(\approx 0.419\) s.

### 4.2. Algorithm Design

Our design is inspired by classical Joint Bilateral Upsampling (JBU) [14]. The key merit of JBU is transferability: it does not hallucinate new values but instead learns mixing weights that decide how much to blend neighboring samples, which makes it naturally model-/task-agnostic. However, standard JBU in Eq. (1) is limited by global \((\sigma_s,\sigma_r)\) and isotropic range/spatial kernels, reducing expressivity near complex structures.

Per-pixel anisotropic kernels. To overcome these limits, Upsample Anything assigns a per-LR-pixel anisotropic Gaussian with parameters  \( \{\sigma_{x}(q), \sigma_{y}(q), \theta(q), \sigma_{r}(q)\} \)  for each low-resolution location q. Let the spatial covariance be

\[
\Sigma_ {q} = R (\theta_ {q}) \left[ \begin{array}{c c} \sigma_ {x} ^ {2} (q) & 0 \\ 0 & \sigma_ {y} ^ {2} (q) \end{array} \right] R ^ {\top} (\theta_ {q}); \quad R (\theta_ {q}) = \left[ \begin{array}{c c} \cos \theta_ {q} & - \sin \theta_ {q} \\ \sin \theta_ {q} & \cos \theta_ {q} \end{array} \right]. \tag {4}
\]

For an HR coordinate p, the unnormalized spatial weight and range (guidance) weight are

\[
\log w _ {p \leftarrow q} ^ {s} = - \frac {1}{2} (p - \mu_ {q}) ^ {\top} \Sigma_ {q} ^ {- 1} (p - \mu_ {q}), \tag {5}
\]

\[
\log w _ {p \leftarrow q} ^ {s} = - \frac {\| I (p) - I (q) \| ^ {2}}{2 \sigma_ {r} ^ {2} (q)}. \tag {6}
\]

where  \( \mu_{q} \)  is the LR center projected to HR coordinates and  \( I(\cdot) \)  is the HR guidance image. The final normalized mixing weight is

\[
w _ {p \leftarrow q} = \frac {\exp \left(\log w _ {p \leftarrow q} ^ {s} + \log w _ {p \leftarrow q} ^ {s}\right)}{\sum_ {q ^ {\prime} \in \Omega (p)} \exp \left(\log w _ {p \leftarrow q ^ {\prime}} ^ {s} + \log w _ {p \leftarrow q ^ {\prime}} ^ {s}\right)}. \tag {7}
\]

Feature rendering (no value synthesis). Given low-resolution features  \( F_{lr} \in R^{C \times H_{l} \times W_{l}} \)  and scale s, we render

## B-ocr-f6c569976570d6

B PDF page 5

the HR feature $F_{hr} \in \mathbb{R}^{C \times (sH_1) \times (sW_1)}$ by pure mixing:

$$F_{hr}(p) = \sum_{q \in \Omega(p)} w_{p \leftarrow q} F_{lr}(q).$$

This strictly reweights existing LR features (no content generation), hence transfers across backbones and tasks.

**Why it generalizes.** Unlike feed-forward upsamplers that require dataset-level training [3, 6, 10, 22, 23], Upsample Anything learns only per-image, pixel-wise mixing weights from the HR guidance through a test-time optimization process, and reuses these weights to splat $F_{lr}$ into $F_{hr}$. Because the mechanism is based on edge- and range-aware interpolation rather than value synthesis, Upsample Anything is inherently *resolution-free, model-agnostic*, and robust to unseen domains.

### 4.3. Test-Time Optimization

After defining the Upsample Anything formulation in Sec. 4.2, the next step is to optimize its per-pixel parameters $\{\sigma_x, \sigma_y, \theta, \sigma_r\}$. Our key idea is inspired by the patchified processing of modern Vision Foundation Models (VFMs): since VFMs downsample images by a fixed stride to extract low-resolution features, we emulate this process during optimization.

Specifically, the high-resolution image $I_{hr}$ is downsampled to $I_{lr}$ by bilinear interpolation with a stride $s$, and the GSJBU parameters are optimized under a reconstruction objective from $I_{lr}$ back to $I_{hr}$:

$$\mathcal{L}_{\text{TTO}} = \|\text{GSJBU}(I_{lr}) - I_{hr}\|_1.$$

This test-time optimization finds image-specific, pixel-wise kernels that best reconstruct the guidance signal.

After the TTO process, the learned kernels are reused to render the high-resolution feature map:

$$F_{hr} = \text{GSJBU}(F_{lr}; \hat{\sigma}_x, \hat{\sigma}_y, \hat{\theta}, \hat{\sigma}_r),$$

where the optimized parameters $\{\hat{\sigma}_x, \hat{\sigma}_y, \hat{\theta}, \hat{\sigma}_r\}$ are directly transferred to the foundation feature space to upsample $F_{lr}$ into $F_{hr}$.

## 5. Experiments

### 5.1. Experimental Setting

Following prior feature-upscaling works [3, 6, 10, 22, 23], we evaluate Upsample Anything on semantic segmentation (COCO, PASCAL-VOC, ADE20K) and depth estimation (NYUv2). For segmentation, we use a single $1 \times 1$ convolution head (linear probe), identical to prior settings. For depth, we adopt a DPT-style decoder head, consistent with [10, 23]. To compare backbones, we consider DINOv1, DINOv2, DINOv3, CLIP, and ConvNeXt, covering

[tbl-0.html](tbl-0.html)

Table 1. Comparison of different upsampling methods on COCO, PASCAL-VOC, and ADE20k datasets.

both transformer and convolutional families; unless otherwise specified, the default backbone is DINOv2-S.

Unlike prior approaches restricted to feature maps, Upsample Anything applies to general bilateral upsampling. Accordingly, we further evaluate (i) depth-map upsampling on NYUv2 and Middlebury, and (ii) probability-map upsampling on Cityscapes—each guided by the corresponding high-resolution RGB image.

### 5.2. Implementation Details

Our Upsample Anything is implemented purely in PyTorch without any chunked or patch-wise processing. All computations are performed in a fully parallel manner over the entire high-resolution grid. Gaussian parameters are initialized as $\sigma_x = \sigma_y = 16.0$, $\sigma_r = 0.12$, and $\theta = 0$, and are optimized per-pixel using the Adam optimizer with a learning rate of $1 \times 10^{-3}$. The model performs test-time optimization for only 50 iterations in total, without any batching or data augmentation. Please refer to the supplementary material for additional implementation details, hyperparameter choices, and ablations.

### 5.3. quantitative results

**Semantic Segmentation.** For a fair comparison, we adopt the conventional linear-probe protocol in which prior work fine-tunes only a $1 \times 1$ convolutional head for 10 epochs. However, we found that this shallow schedule often undertrains the head. We therefore extend training to 100 epochs and apply a cosine learning-rate schedule to gradually decay the head's learning rate. Under this setting, our results in Table 1 show a trend that differs from previous reports [3, 6, 10, 22, 23]: although all methods converge quickly, their eventual gains over simple bilinear upsampling are modest when the backbone representation is strong. This raises the question of how much feature upsampling helps semantic segmentation under high-capacity backbones. Nevertheless, our proposed Upsample Anything attains the best accuracy across COCO, PASCAL-VOC, and ADE20K, with AnyUp consistently second.

*Upsample Anything (prob.).* In addition to upsampling feature maps, we evaluate a low-compute variant that predicts the segmentation at the feature resolution (no feature upsampling), produces a probabilistic map, and then up-

[OCR table id=tbl-0.html; page=5]
<table><tr><td rowspan="2">Method</td><td colspan="2">COCO</td><td colspan="2">PASCAL-VOC</td><td colspan="2">ADE20k</td></tr><tr><td>mIoU (↑)</td><td>Acc. (↑)</td><td>mIoU (↑)</td><td>Acc. (↑)</td><td>mIoU (↑)</td><td>Acc. (↑)</td></tr><tr><td>Bilinear</td><td>60.43</td><td>80.18</td><td>81.27</td><td>95.96</td><td>41.48</td><td>74.95</td></tr><tr><td>FeatUp</td><td>60.96</td><td>80.65</td><td>81.91</td><td>96.27</td><td>41.92</td><td>75.41</td></tr><tr><td>LoiUp</td><td>61.08</td><td>80.72</td><td>81.84</td><td>96.33</td><td>41.83</td><td>75.36</td></tr><tr><td>JAFAR</td><td>60.87</td><td>80.51</td><td>82.05</td><td>96.21</td><td>41.74</td><td>75.22</td></tr><tr><td>AnyUp</td><td>61.25</td><td>80.89</td><td>82.18</td><td>96.39</td><td>42.02</td><td>75.63</td></tr><tr><td>Upsample Anything</td><td>61.41</td><td>81.34</td><td>82.22</td><td>96.90</td><td>42.95</td><td>76.52</td></tr><tr><td>Upsample Anything (prob.)</td><td>63.40</td><td>83.73</td><td>84.57</td><td>97.42</td><td>44.29</td><td>78.58</td></tr></table>
