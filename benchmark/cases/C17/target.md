# [TITLE C17]

## A-page-0001

target PDF page 1

# [TITLE C17]

Anonymous authors

Paper under double-blind review

# ABSTRACT

Text image restoration requires preserving character identity and stroke geometry. Recognition-guided methods exploit character priors but are limited by vocabulary coverage. However, visible stroke patterns can guide reconstruction even for out-of-vocabulary characters, while reliable priors can complement visual evidence under severe degradation. Motivated by this complementarity, we propose [NAME C17] (Glyph Reconstruction via Adaptive Selection of Paths), a framework for legibility-guided selection between visual reconstruction and character-prior completion. A geometry-aware extractor aligns character features in a shared glyph space, where a visual path reconstructs observed structures and a prior path generates character-conditioned glyphs with input-dependent style modulation. A selector uses visual evidence and recognition confidence to choose complete glyphs, with visual fallback for predictions labeled as unknown. The selected glyphs form a structure mask for full-image restoration. We develop a synthetic training pipeline spanning 900 fonts and introduce [NAME C17], a multilingual real-world benchmark. Experiments demonstrate the effectiveness of [NAME C17] across character subsets and degradation levels, including languages absent from full-image restoration training.

![img-0.jpeg](img-0.jpeg)

Figure 1: Motivation for [NAME C17]. Light degradation (a,b) calls for preserving visible strokes. Heavy degradation (c,d) benefits from reliable priors for known characters and visual recovery for unknowns. [NAME C17] selects these paths per character. We compare with DiffTSR (Zhang et al., 2024), MARCONet++ (Li et al., 2025), and TiGeSR (Luo et al., 2026). Known/Unknown denotes characters inside/outside the recognition vocabulary.

# 1 INTRODUCTION

Text image restoration aims to recover both textual content and visual appearance from degraded observations. This task is particularly challenging because character identity depends on highly structured stroke patterns. Even minor deviations in stroke topology or geometry can change one character into another. Although general restoration models (Yu et al., 2024; Lin et al., 2024; 2025; Wu et al., 2024a;b) leverage powerful diffusion priors to recover realistic visual details, these models may synthesize plausible strokes that fail to preserve the original character identity.

## A-page-0002

target PDF page 2

054
055
056
057
058
059
060
061
062
063
064
065
066
067
068
069
070
071
072
073
074
075
076
077
078
079
080
081
082
083
084
085
086
087
088
089
090
091
092
093
094
095
096
097
098
099
100
101
102
103
104
105
106
107

To improve textual fidelity, existing methods introduce recognition constrained supervision (Wang et al., 2019; Chen et al., 2021; Shi et al., 2023; Qin & Wang, 2024) or explicit recognition and generative priors (Ma et al., 2023; Zhao et al., 2022; Zhang et al., 2024; Min et al., 2026; Kim et al., 2025; Li et al., 2023; Luo et al., 2026). However, recognition losses constrain stroke geometry indirectly, making the restoration insufficient under severe degradation. Furthermore, explicit priors can provide structural guidance, but vocabulary-bound priors cannot provide identity-specific representations for out-of-vocabulary characters. Unfamiliar fonts also cause structural mismatches even for supported characters. These limitations are particularly relevant to text restoration in the wild, where multilingual content, complex typeface structure, and scenes containing misspellings are common. Such factors frequently introduce character identities and glyph appearances that are beyond the coverage of the training data. As shown in Fig. 1, mismatched priors can override visible stroke patterns and produce incorrect glyph structures.

Our key observation is that visible stroke patterns can guide the restoration of characters outside the recognition vocabulary. Characters across writing systems often share local stroke patterns, such as line segments, curves, and junctions. These shared patterns provide a basis for reconstructing out-of-vocabulary glyphs from visual evidence without assigning them to a known character category. With mild degradation, stroke layout and connectivity usually remain, so restoration can preserve the original structure, even for out-of-vocabulary characters and complex typefaces. With severe degradation, restoration should clarify recoverable strokes using shared visual patterns and remaining structural evidence. For supported characters, reliable OCR can reduce ambiguity and guide completion of missing strokes. However, conflicts exist between preserving visual fidelity and reconstructing characters using learned priors because of complex degradation. Coupling these two capabilities during training creates a trade-off: greater reliance on learned priors risks distorting out-of-vocabulary characters, while stronger dependence on visual evidence limits restoration under severe degradation.

Motivated by these observations, we introduce [NAME C17] (Glyph Reconstruction via Adaptive Selection of Paths), a framework for legibility-guided selection between visual recovery and character-prior completion. [NAME C17] decouples these two capabilities through a visual branch and a prior branch operating in a  \( 128 \times 128 \)  character space, and adaptively selects their reconstructions at the character level. A Geometry-Aware Character Feature Extractor constructs this shared space through two modules. An Attention-based Character Geometry Predictor estimates character transforms from multi-scale cross-attention maps. An Adaptive Affine RoI Extractor normalizes the corresponding features into a shared space for both reconstruction branches. The visual branch combines attention to stroke regions with multi-scale residual connections to preserve fine details. The prior branch generates glyph structures from predicted token embeddings, incorporating font style and affine geometry through adaptive instance normalization. Local and whole-character discriminators reinforce their respective specialization in stroke detail and global structure. Our [NAME C17] Module uses recoverable visual structure and recognition reliability as complementary cues. It chooses between candidate glyphs using aligned visual features and OCR confidence, supervised by an oracle comparing structure and character identity. Selection operates at the character level, avoiding the pixel-wise stroke inconsistencies. For characters predicted as unknown, [NAME C17] falls back to the visual branch, preserving recovery beyond the recognition vocabulary.

Following TiGeSR (Luo et al., 2026), the selected glyphs form a spatial mask for full-image restoration. However, visual plausibility alone does not ensure textual fidelity. A generative restoration model may replace the reconstructed strokes with plausible alternatives. We apply layout augmentation that introduces discrepancies between the low-quality input and the mutually aligned ground-truth image and mask, encouraging the restored text to follow the mask.

To train [NAME C17], we develop a synthetic training pipeline with 900 fonts and introduce [NAME C17], a multilingual real-world benchmark covering diverse typography and degradations. We evaluate glyph and full-image restoration on unfamiliar glyphs with recoverable strokes and severely degraded characters requiring reliable priors. Trained only on Chinese characters, English letters, and digits, the full-image restoration network is further evaluated on multilingual text with different degradations.

Our contributions are summarized as follows:

- We propose [NAME C17], a geometry-aware glyph reconstruction framework that decouples visual recovery from character-prior completion in a shared character space, preserving a visual recovery path for characters beyond the recognition vocabulary.

## A-page-0003

target PDF page 3

108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161

![img-1.jpeg](img-1.jpeg)

Figure 2: Overview of [NAME C17]. Left: Geometry-aware extraction aligns character features in a shared glyph space. Middle: Complementary visual and prior branches reconstruct glyphs, followed by legibility-guided character-level selection. Right: Selected glyphs form a full-image structure mask that guides RGB restoration together with the low-quality input.

- We introduce legibility-guided character-level selection that uses glyph structure, aligned visual features, and OCR confidence to choose between complementary reconstruction paths. Whole-glyph selection preserves structural coherence, with an explicit visual fallback for characters predicted as unknown.
- We develop a synthetic training pipeline spanning 900 fonts and introduce [NAME C17], a multilingual real-world benchmark covering diverse character sets, typography, and degradations, supporting evaluation within and beyond the recognition vocabulary.

## 2 RELATED WORK

### 2.1 REAL WORLD IMAGE RESTORATION

Real-world image restoration recovers high-quality images from low-quality images affected by complex and often unknown degradations. CNN-based approaches learn mappings from degraded inputs to clean targets, with methods such as RealSR (Cai et al., 2019). GAN-based approaches Zhang et al. (2021); Wang et al. (2021) introduce adversarial supervision to recover perceptually realistic details. More recently, diffusion-based methods have advanced real-world image restoration. StableSR (Wang et al., 2024) adapts pretrained diffusion priors to super-resolution, PASD (Yang et al., 2024) introduces pixel-aware guidance, SeeSR (Wu et al., 2024b) incorporates semantic-aware guidance, DiffBIR (Lin et al., 2024) separates degradation removal from detail generation, and SUPIR (Yu et al., 2024) scales up diffusion-based restoration. OSEDiff (Wu et al., 2024a) enables efficient one-step restoration, while HYPIR (Lin et al., 2025) combines pretrained diffusion priors with adversarial fine-tuning to achieve high-quality restoration in a single forward pass. DiT-SR (Cheng et al., 2025) and DiT4SR (Duan et al., 2025) explore diffusion Transformer architectures for super-resolution. Despite their success in recovering natural image details, these methods do not explicitly enforce character identity or stroke fidelity. This discrepancy motivates text-specific restoration methods that account for both visual appearance and textual content.

### 2.2 TEXT IMAGE RESTORATION

Scene Text Image Restoration. Methods for cropped words and text lines improve readability through recognition supervision (Wang et al., 2019; Chen et al., 2021), gradient profile losses (Wang et al., 2020), or recognition-derived priors (Ma et al., 2023; 2022). Beyond recognition features, MARCONet (Li et al., 2023) and MARCONet++ (Li et al., 2025) introduce generative structure priors to provide character-specific shape and appearance information. DiffTSR (Zhang et al., 2024) couples textual and visual diffusion to improve blind text super-resolution. Such priors help resolve missing content, but their usefulness depends on their compatibility with the observed glyph; an incorrect character prediction or a mismatched shape prior can instead bias the reconstruction.

Text-Aware Full-Image Restoration. Recent approaches extend text restoration to full scene images. TeReDiff (Min et al., 2026) jointly learns image restoration and text spotting, using intermediate

## A-page-0004

target PDF page 4

162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215

recognition predictions to guide diffusion denoising. UniT (Kim et al., 2025) further integrates a vision-language model to iteratively refine textual guidance. Such semantic guidance depends on recognition reliability and may introduce incorrect character priors when unfamiliar text is incorrectly recognized. TiGeSR (Luo et al., 2026) adopts a text-first, image-later pipeline, with a text structure reconstruction module similar to DiffTSR (Zhang et al., 2024). Although it performs well on many images, its own ablation experiments indicate limited reliance on OCR guidance. Its apparent preference for visual features over character priors limits restoration under severe degradation. Together, these approaches motivate adapting the use of character priors to recoverable visual evidence and recognition reliability.

### 3 METHODOLOGY

### 3.1 GEOMETRY-AWARE CHARACTER EXTRACTION

To better disentangle visual evidence and character priors for individual glyphs, [NAME C17] reformulates text reconstruction in a character space, where each character is represented by a 128 × 128 output. This formulation requires accurately extracting individual character features from a text line and mapping the reconstructed glyphs back to their original positions. Therefore, we introduce a Geometry-Aware Character Extractor that localizes each character from its cross-attention response and maps the corresponding multi-scale features into a shared space.

Attention-Based Character Geometry Prediction As shown in Fig. 2, the visual encoder extracts multi-scale features {F^l}_{l=1}^S from I_LQ^T. Multi-scale recognition decoders produce character visual features {h_i^l}_{l=1}^S and character-specific cross-attention maps {A_i^l}_{l=1}^S, which provide localization cues without an additional character detector. For each character, we summarize the highest-resolution attention map by its normalized centroid and spatial extent, m_i = [μ_i^x, μ_i^y, σ_i^x, σ_i^y], and aggregate multi-scale visual features into v_i using attention-weighted pooling. A residual MLP predicts character scales and translation offsets:

$$[s_i^x, s_i^y, \Delta t_i^x, \Delta t_i^y] = \mathcal{P}_{\text{geo}}([\mathbf{m}_i; \mathbf{v}_i; \mathbf{p}_i]), \tag{1}$$

where p_i encodes the character index.

Rather than predicting character locations from scratch, we construct a translation prior t̄_i that centers a character patch of predefined initial scale at the attention centroid. The predicted offsets refine this prior, yielding the character-to-line scale-and-translation transform

$$\mathbf{T}_i = \begin{bmatrix} s_i^x & 0 & W(\bar{t}_i^x + \Delta t_i^x) \\ 0 & s_i^y & H(\bar{t}_i^y + \Delta t_i^y) \end{bmatrix}, \tag{2}$$

where H and W denote the text-line height and width. This parameterization combines attention-based localization with learned geometric refinement. Attention construction, feature aggregation, and the translation prior are detailed in Supp. Sec. A.

Adaptive Affine RoI Extraction Using T_i, we map a regular character grid G to the text line and extract aligned features through differentiable bilinear sampling:

$$\widetilde{\mathbf{F}}_i^l = \text{GridSample}(\mathbf{F}^l, \mathbf{T}_i(\mathcal{G})), \tag{3}$$

with sampling coordinates converted to the convention of each feature map. The shared transform adapts the sampling location and extent to each character while preserving correspondence across scales. The extracted features are aligned with the 128 × 128 character space and supplied to both glyph reconstruction paths. We retain T_i to place the selected glyph back into the text line.

### 3.2 DUAL-BRANCH GLYPH RECONSTRUCTION

The visual and prior paths reconstruct glyphs from perception and character conditioning, respectively:

$$\hat{\mathbf{G}}_i^v = \mathcal{R}_v(\mathbf{v}_i, \{\widetilde{\mathbf{F}}_i^l\}_{l=1}^S), \quad \hat{\mathbf{G}}_i^p = \mathcal{R}_p(z_i, \{\widetilde{\mathbf{F}}_i^l\}_{l=1}^S). \tag{4}$$

The recognition classifier and prior embeddings share vocabulary V, excluding special tokens. During prior training, z_i uses ground-truth identities, mapping out-of-vocabulary labels to ⟨unk⟩; selector training and inference use OCR predictions.

## A-page-0005

target PDF page 5

**Visual-Evidence Reconstruction Path** A projection of $\mathbf{v}_i$ initializes an upsampling decoder without character-class embeddings. Aligned spatial features preserve stroke details through

$$\mathbf{X}_i^{v,l} = \mathcal{B}_l^v([\mathrm{Up}(\mathbf{X}_i^{v,l-1}); \mathcal{C}_l^v(\tilde{\mathbf{F}}_i^l)]), \tag{5}$$

where $\mathcal{C}_l^v$ projects features and $\mathcal{B}_l^v$ is a residual block at scale $l$. All valid characters, including unknowns, use the ground-truth glyph $\mathbf{G}_i^{\mathrm{GT}}$ as the reconstruction target.

**Character-Prior Reconstruction Path** A jointly learned embedding indexed by $z_i$ initializes the prior decoder. Pooled aligned features predict stage-specific style parameters for channel-wise modulation:

$$\tilde{\mathbf{X}}_i^{p,l} = (1 + \boldsymbol{\gamma}_i^l) \odot \mathrm{IN}(\mathbf{X}_i^{p,l}) + \boldsymbol{\beta}_i^l, \tag{6}$$

where IN is instance normalization. Thus, visual conditioning uses modulation rather than spatial concatenation. The prior target is $\mathbf{G}_i^{p,\mathrm{tgt}} = \mathbf{G}_i^{\mathrm{GT}}$ for $y_i \in \mathcal{V}$ and $\mathbf{0}$ otherwise.

**Reconstruction objectives.** For $b \in \{v, p\}$, $\mathcal{L}_{\mathrm{rec}}^b$ combines pixel, perceptual, foreground segmentation, and structural similarity terms. Local and whole-character discriminators $D_v, D_p$ encourage stroke detail and global structure, respectively, with generator loss $\mathcal{L}_{\mathrm{adv}}^b = -\mathbb{E}_{i \in \Omega_b}[D_b(\hat{\mathbf{G}}_i^b)]$. Each path uses $\mathcal{L}_b = \mathcal{L}_{\mathrm{rec}}^b + \lambda_{\mathrm{adv}}^b \mathcal{L}_{\mathrm{adv}}^b$, giving $\mathcal{L}_{\mathrm{glyph}} = \mathcal{L}_v + \mathcal{L}_p$. More details appear in Supp. Sec. B.

### 3.3 [NAME C17]

Visual features and recognition confidence provide complementary legibility cues. The selector predicts the probability of choosing the visual path:

$$p_i^v = \mathcal{S}_{\mathrm{sel}}(\hat{\mathbf{G}}_i^v, \hat{\mathbf{G}}_i^p, \mathbf{V}_i, c_i), \tag{7}$$

where $\mathbf{V}_i$ aggregates aligned multi-scale features and $c_i$ is the maximum recognition probability.

**Quality-based supervision.** An oracle compares both candidates against the original ground-truth glyph using pixel and foreground segmentation errors together with an identity loss from a frozen OCR recognizer $\mathcal{O}$:

$$E_i^b = \lambda_{\mathrm{pix}} E_{\mathrm{pix},i}^b + \lambda_{\mathrm{seg}} E_{\mathrm{seg},i}^b + \lambda_{\mathrm{ocr}} E_{\mathrm{ocr},i}^b, \quad b \in \{v, p\}, \tag{8}$$

where $E_{\mathrm{ocr},i}^b = \ell_{\mathrm{ocr}}(\mathcal{O}(\hat{\mathbf{G}}_i^b), y_i)$ for $y_i \in \mathcal{V}$ and zero otherwise. The detached soft target is

$$o_i = \mathrm{sg}\left[\mathrm{Sigmoid}\left(\frac{E_i^p - E_i^v}{\tau}\right)\right], \tag{9}$$

where $\tau > 0$ controls sharpness, larger $o_i$ favors the visual path, and sg stops gradients. Detached weights $\rho_i$ downweight candidates of similar quality. We optimize

$$\mathcal{L}_{\mathrm{sel}} = \frac{\sum_{i \in \Omega_{\mathrm{sel}}} \rho_i \mathrm{BCE}(p_i^v, o_i)}{\sum_{i \in \Omega_{\mathrm{sel}}} \rho_i + \epsilon} + \frac{\lambda_{\mathrm{bin}}}{|\Omega_{\mathrm{sel}}|} \sum_{i \in \Omega_{\mathrm{sel}}} p_i^v (1 - p_i^v), \tag{10}$$

where $\Omega_{\mathrm{sel}}$ includes all valid characters, including unknowns, and $\epsilon > 0$ stabilizes normalization. The second term encourages decisive selection.

**Inference.** We select the complete visual glyph when OCR predicts $\langle \mathrm{unk} \rangle$ or $p_i^v \ge 0.5$, and the prior glyph otherwise. Selector and oracle details appear in Supp. Sec. C.

### 3.4 TRAINING OBJECTIVES

**Stage I: Visual and geometry learning.** We jointly train the encoder, recognition module, geometry predictor, visual path, and its discriminator on all valid characters. Recognition and geometry use token cross-entropy $\mathcal{L}_{\mathrm{text}}$ and Smooth L1 loss $\mathcal{L}_{\mathrm{geo}}$. Visual glyphs form a differentiable line mask $\hat{\mathbf{M}}^{\mathrm{T}} = \mathrm{Compose}(\{(\hat{\mathbf{G}}_i^v, \mathbf{T}_i)\}_{i=1}^L)$. Against the ground-truth mask, $\mathcal{L}_{\mathrm{paste}}$ combines BCE, Dice, and $\ell_1$ terms to supervise reconstruction and placement:

$$\mathcal{L}_{\mathrm{stage1}} = \lambda_{\mathrm{text}} \mathcal{L}_{\mathrm{text}} + \lambda_{\mathrm{geo}} \mathcal{L}_{\mathrm{geo}} + \lambda_{\mathrm{paste}} \mathcal{L}_{\mathrm{paste}} + \mathcal{L}_v. \tag{11}$$

**Stage II: Prior learning.** We freeze Stage I modules and optimize the prior decoder, embeddings, and discriminator with $\mathcal{L}_p$, using ground-truth identities and the targets in Section 3.2.

216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269

## A-page-0006

target PDF page 6

270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323

![img-2.jpeg](img-2.jpeg)

Figure 3: Qualitative comparison on synthetic degradations under light and heavy degradation settings, with known and unknown text categories. Each setting contains two examples.

Stage III: Selector learning. We freeze all preceding modules and train only the selector with $\mathcal{L}_{\text{sel}}$. OCR-conditioned prior candidates expose it to inference-time recognition errors. Loss and discriminator details appear in Supp. Sec. D.

### 3.5 LAYOUT AUGMENTATION FOR FULL-IMAGE RESTORATION

Selected glyphs form a spatial mask that guides restoration alongside the low-quality input. During restoration training, layout augmentation keeps the ground-truth image and its mask aligned while introducing slight text-placement discrepancies with the low-quality input. Supervision against the corresponding ground-truth image encourages the network to follow the mask-specified layout, strengthening mask control over restored text.

## 4 EXPERIMENTS

Training Data. We synthesize paired images and text masks by rendering text with randomized typography and geometry using 900 fonts on patches from DF2K, comprising DIV2K (Agustsson & Timofte, 2017) and Flickr2K (Timofte et al., 2017). Degraded inputs are generated online using the two-stage Real-ESRGAN pipeline (Wang et al., 2021). Recognition and prior modules share a vocabulary of simplified Chinese characters, English letters, and digits; traditional Chinese characters outside this vocabulary are used as unknown-class examples for glyph reconstruction. Thus, out-of-vocabulary indicates vocabulary exclusion, not necessarily absence from reconstruction training. Additional Japanese and Korean samples, labeled ⟨unk⟩, train only the recognition classifier with both encoder and decoder features detached. They do not expand the vocabulary for train glyph reconstruction or full-image restoration.

Synthetic Test Data. Our paired synthetic benchmark, SynData, comprises 600 clean images with 1,440 text lines, split equally into Known (724 lines with simplified Chinese, English, and digits) and Unknown (716 lines with Japanese, Korean, French, Greek, and Thai) subsets. In Unknown, 72% of characters fall outside the shared recognition and prior vocabulary; thus, this designation applies to the subset rather than every character. This mixture better reflects real-world scenarios. Text is placed using SynthText's segmentation and depth guidance (Gupta et al., 2016) or randomly on high-quality background crops. We apply light and heavy degradations from the training degradation family to the same clean images for controlled comparisons.

Real-World Test Data. We further evaluate on [NAME C17], a curated real-world test set containing 500 low-quality scene-text images, each with a long side of 1,024 pixels and corresponding ground-truth text annotations. The set is balanced across four subsets: known/light, known/heavy, unknown/light, and unknown/heavy with 125 images each and 236, 660, 453, and 788 annotated text lines, respectively. This yields 250 light samples with 689 text lines and 250 heavy samples with 1,448 text lines. [NAME C17] is constructed from ReCTS Liu et al. (2019), ICDAR2015 Karatzas et al. (2015), and MLT2019 Nayef et al. (2019), contributing 67, 62, and 371 images, respectively. At the image-stratum level, it contains 90 Chinese, 160 English-or-digit, 40 Arabic, 37 Bangla, 34 Hindi, 48 Japanese, and 91 Korean samples. In total, the dataset contains 2,137 annotated text lines, including 848 Latin, 406 Chinese, 255 Korean, 224 Arabic, 134 Bangla, 131 Hindi, 111 Japanese, 24 symbol,

## A-page-0007

target PDF page 7

324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377

![img-3.jpeg](img-3.jpeg)

Figure 4: Qualitative comparison on the real-world [NAME C17] dataset under light and heavy degradations, with Known and Unknown subsets shown separately. Each setting contains two examples.

and 4 mixed-script lines. We report OCR-A and FID; the FID reference set contains 984 collected high-quality scene-text images with 6,508 text lines, covering the same languages as [NAME C17].

Implementation Details. We implement [NAME C17] in PyTorch using 1024 × 1024 training images, 512 × 128 normalized text lines, and 128 × 128 glyphs. Text-line outputs are mapped back via projective transformations to preserve spatial layout. Across training stages, all components use AdamW with a learning rate of 5 × 10⁻⁵, 1,000 warm-up iterations, cosine decay, and a per-GPU batch size of 4. We adopt the TiGeSR (Luo et al., 2026) restoration architecture, trained with paired supervision on 512 × 512 crops and layout augmentation (Section 3.5) to align outputs with text masks. Further details are provided in Supp. Sec. E.

### 4.1 COMPARISON WITH OTHER METHODS

We compare [NAME C17] with ten restoration methods from three groups: (i) GAN-based general image restoration methods, including BSRGAN (Zhang et al., 2021) and Real-ESRGAN (Wang et al., 2021); (ii) general image restoration methods that exploit pretrained diffusion priors, including DiffBIR (Lin et al., 2024), SUPIR (Yu et al., 2024), SeeSR (Wu et al., 2024b), and HYPIR (Lin et al., 2025); and (iii) methods designed specifically for text restoration, including MARCONet++ (Li et al., 2025), DiffTSR (Zhang et al., 2024), TeReDiff (Min et al., 2026), and TiGeSR (Luo et al., 2026).

Quantitative Comparison. We evaluate restoration using six complementary metrics: PSNR and SSIM (Wang et al., 2004) measure reconstruction fidelity; LPIPS (Zhang et al., 2018) and DISTS (Ding et al., 2022) assess perceptual similarity; FID (Heusel et al., 2017) measures distributional image quality; and OCR recognition accuracy (OCR-A) (Luo et al., 2026), evaluated with PP-OCRv6 (Zhang et al., 2026), measures textual correctness. Tables 1 and 2 report results under light and heavy degradations, respectively, with Known and Unknown evaluated separately for both SynData and [NAME C17]. SynData is evaluated using all six metrics, while [NAME C17] is evaluated using FID and OCR-A. All metrics are computed on text-line crops extracted from full-image restoration outputs; full-image metrics are provided in the supplementary material. To control for differences in text detection, all methods use the same bounding boxes for text-line extraction and pasting.

Under light degradation on SynData, [NAME C17] achieves the best LPIPS, DISTS, and FID on both subsets. It also ranks first in OCR-A on Known and PSNR on Unknown, second in PSNR on Known and OCR-A on Unknown, and third in SSIM on both subsets. These results demonstrate strong perceptual restoration alongside competitive reconstruction fidelity and textual correctness. BSRGAN and Real-ESRGAN also achieve competitive OCR-A. This is consistent with the importance of preserving observable character structures when degradation is mild. The lower OCR-A of several generative and text-specific baselines suggests that strong restoration priors do not necessarily improve readability when sufficient visual evidence remains. Under heavy degradation on SynData, [NAME C17] ranks first in PSNR, SSIM, LPIPS, DISTS, and OCR-A on both subsets. In particular, it achieves OCR-A scores of 69.88% on Known and 69.87% on Unknown, exceeding the strongest competing methods by 7.35 and 2.60 percentage points, respectively. These results are consistent with the benefits of combining learned character priors with transferable stroke-level cues when the observed glyph structure is incomplete or ambiguous.

## A-page-0008

target PDF page 8

Table 1: Evaluation on SynData and [NAME C17] with light degradation. Metrics are computed on text-line crops extracted from full-image restoration outputs. Full-image metrics are provided in the supplementary material. OCR-A is reported in %. Best and second-best results are shown in bold and underlined, respectively.

[tbl-0.html](tbl-0.html)

Table 2: Evaluation on SynData and [NAME C17] with heavy degradation. Settings follow Table 1.

[tbl-1.html](tbl-1.html)

On [NAME C17], [NAME C17] achieves the highest OCR-A across all four subset-degradation combinations. Under light degradation, it obtains 97.05% on Known and 86.15% on Unknown; under heavy degradation, it achieves 90.78% and 60.31%, respectively. The improvements over the strongest competing methods are particularly pronounced on Unknown, reaching 2.62 percentage points under light degradation and 5.36 percentage points under heavy degradation. [NAME C17] also ranks second in FID in all four settings. Together, these results demonstrate consistent gains in textual correctness on real-world images while maintaining competitive distributional image quality.

Qualitative Comparison. Figure 3 and Figure 4 compare [NAME C17] with other methods across both degradation levels and character subsets. In the lightly degraded examples, [NAME C17] preserves distinctive glyph styles and visible stroke layouts, whereas competing outputs sometimes regularize these details or introduce structural changes. Under heavy degradation, [NAME C17] produces more coherent stroke patterns in the illustrated Unknown example, while some competing outputs contain incomplete glyphs or substantially altered character shapes. These examples illustrate differences in structural preservation and readability that complement the quantitative evaluation.

### 4.2 ABLATION STUDIES

Tables 3 and 4 examine the roles of the reconstruction branches, adaptive selector, text masks, and restoration model. Unless explicitly stated otherwise, all ablations use the same trained [NAME C17] model and the same fixed full-image restorer, changing only the specified inference configuration. In the Prior Branch Only ablation, characters predicted as  \( \langle unk\rangle \)  contribute empty glyph masks, without falling back to the visual branch. The full model instead selects the visual reconstruction for these predictions. Both GT OCR variants replace predicted character labels with ground-truth labels; Full w/ GT OCR retains the learned selector and fixes recognition confidence at 0.95.

Complementarity of reconstruction branches. The single-branch ablations reveal complementary strengths of visual evidence and character priors. Under light degradation, visual-only outperforms both prior-only variants across all reported metrics on both subsets, even when the prior branch receives ground-truth character labels. Under heavy degradation, prior-only achieves higher OCR-A

378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431

[OCR table id=tbl-0.html; page=8]
<table><tr><td rowspan="3">Method</td><td colspan="11">SynData</td><td colspan="4">[NAME C17]</td></tr><tr><td colspan="5">Known</td><td colspan="6">Unknown</td><td colspan="2">Known</td><td colspan="2">Unknown</td></tr><tr><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>DISTS↓</td><td>FID↓</td><td>OCR-A↑</td><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>DISTS↓</td><td>FID↓</td><td>OCR-A↑</td><td>FID↓</td><td>OCR-A↑</td><td>FID↓</td></tr><tr><td>BSRGAN</td><td>21.72</td><td>.7503</td><td>.2533</td><td>.1829</td><td>51.67</td><td>80.05</td><td>22.54</td><td>.7523</td><td>.2502</td><td>.1838</td><td>55.18</td><td>77.17</td><td>78.58</td><td>96.11</td><td>54.68</td></tr><tr><td>Real-ESRGAN</td><td>21.12</td><td>.7486</td><td>.2473</td><td>.1826</td><td>49.13</td><td>80.60</td><td>21.78</td><td>.7506</td><td>.2415</td><td>.1813</td><td>51.87</td><td>76.80</td><td>78.94</td><td>96.04</td><td>54.72</td></tr><tr><td>DiffBIR</td><td>18.13</td><td>.5467</td><td>.3322</td><td>.2073</td><td>53.30</td><td>68.89</td><td>19.74</td><td>.5979</td><td>.2954</td><td>.1926</td><td>50.50</td><td>69.66</td><td>79.46</td><td>92.38</td><td>54.61</td></tr><tr><td>SUPIR</td><td>16.43</td><td>.5019</td><td>.3736</td><td>.2292</td><td>51.08</td><td>66.53</td><td>18.05</td><td>.5481</td><td>.3432</td><td>.2187</td><td>54.02</td><td>65.34</td><td>79.32</td><td>95.37</td><td>54.98</td></tr><tr><td>SeeSR</td><td>17.36</td><td>.5044</td><td>.3793</td><td>.2320</td><td>58.97</td><td>60.74</td><td>18.91</td><td>.5609</td><td>.3382</td><td>.2151</td><td>55.02</td><td>64.00</td><td>78.59</td><td>94.62</td><td>54.57</td></tr><tr><td>HYPIR</td><td>14.94</td><td>.4167</td><td>.4013</td><td>.2516</td><td>62.84</td><td>64.71</td><td>16.22</td><td>.4550</td><td>.3692</td><td>.2389</td><td>58.75</td><td>64.98</td><td>79.45</td><td>94.72</td><td>55.00</td></tr><tr><td>MARCONet++</td><td>20.15</td><td>.6473</td><td>.3275</td><td>.2091</td><td>62.41</td><td>73.67</td><td>21.70</td><td>.6615</td><td>.3272</td><td>.2141</td><td>75.41</td><td>74.66</td><td>77.32</td><td>95.33</td><td>53.90</td></tr><tr><td>DiffTSR</td><td>18.43</td><td>.5928</td><td>.3389</td><td>.2084</td><td>66.03</td><td>71.46</td><td>19.97</td><td>.6162</td><td>.3367</td><td>.2126</td><td>63.97</td><td>68.98</td><td>77.80</td><td>95.98</td><td>54.34</td></tr><tr><td>TeReDiff</td><td>16.25</td><td>.4099</td><td>.4450</td><td>.2661</td><td>69.68</td><td>51.08</td><td>17.62</td><td>.4626</td><td>.4102</td><td>.2485</td><td>66.55</td><td>57.88</td><td>81.01</td><td>83.49</td><td>55.10</td></tr><tr><td>TiGeSR</td><td>20.38</td><td>.6615</td><td>.3085</td><td>.2045</td><td>54.30</td><td>76.58</td><td>21.79</td><td>.6782</td><td>.2961</td><td>.2020</td><td>54.95</td><td>75.73</td><td>79.80</td><td>95.88</td><td>54.71</td></tr><tr><td>Ours</td><td>21.70</td><td>.7405</td><td>.2413</td><td>.1618</td><td>42.41</td><td>81.10</td><td>22.96</td><td>.7481</td><td>.2273</td><td>.1569</td><td>41.58</td><td>76.87</td><td>77.38</td><td>97.05</td><td>54.24</td></tr></table>

[OCR table id=tbl-1.html; page=8]
<table><tr><td rowspan="3">Method</td><td colspan="11">SynData</td><td colspan="4">[NAME C17]</td></tr><tr><td colspan="5">Known</td><td colspan="6">Unknown</td><td colspan="2">Known</td><td colspan="2">Unknown</td></tr><tr><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>DISTS↓</td><td>FID↓</td><td>OCR-A↑</td><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>DISTS↓</td><td>FID↓</td><td>OCR-A↑</td><td>FID↓</td><td>OCR-A↑</td><td>FID↓</td></tr><tr><td>BSRGAN</td><td>17.85</td><td>.5136</td><td>.4347</td><td>.2845</td><td>95.57</td><td>60.47</td><td>18.64</td><td>.5479</td><td>.4175</td><td>.2760</td><td>92.47</td><td>65.49</td><td>42.20</td><td>89.77</td><td>35.96</td></tr><tr><td>Real-ESRGAN</td><td>17.74</td><td>.5221</td><td>.4250</td><td>.2764</td><td>86.76</td><td>62.35</td><td>18.50</td><td>.5547</td><td>.4066</td><td>.2691</td><td>85.75</td><td>67.27</td><td>42.83</td><td>89.96</td><td>36.23</td></tr><tr><td>DiffBIR</td><td>16.64</td><td>.4432</td><td>.4208</td><td>.2538</td><td>64.99</td><td>57.35</td><td>17.66</td><td>.4894</td><td>.3895</td><td>.2407</td><td>61.96</td><td>63.52</td><td>42.58</td><td>60.03</td><td>36.32</td></tr><tr><td>SUPIR</td><td>15.19</td><td>.3936</td><td>.4423</td><td>.2608</td><td>60.52</td><td>56.10</td><td>16.61</td><td>.4487</td><td>.4093</td><td>.2473</td><td>62.06</td><td>60.42</td><td>43.49</td><td>72.68</td><td>36.42</td></tr><tr><td>SeeSR</td><td>16.45</td><td>.4389</td><td>.4257</td><td>.2539</td><td>64.43</td><td>54.90</td><td>17.61</td><td>.4895</td><td>.3877</td><td>.2382</td><td>60.60</td><td>61.68</td><td>42.30</td><td>71.06</td><td>35.75</td></tr><tr><td>HYPIR</td><td>14.72</td><td>.3896</td><td>.4302</td><td>.2569</td><td>61.56</td><td>57.64</td><td>15.83</td><td>.4313</td><td>.3947</td><td>.2422</td><td>57.22</td><td>61.61</td><td>42.64</td><td>75.79</td><td>36.67</td></tr><tr><td>MARCONet++</td><td>17.65</td><td>.4929</td><td>.4403</td><td>.2686</td><td>80.65</td><td>60.45</td><td>18.83</td><td>.5308</td><td>.4268</td><td>.2658</td><td>91.55</td><td>64.41</td><td>42.19</td><td>89.95</td><td>36.35</td></tr><tr><td>DiffTSR</td><td>16.10</td><td>.4510</td><td>.4245</td><td>.2468</td><td>66.91</td><td>61.57</td><td>17.30</td><td>.4851</td><td>.4215</td><td>.2500</td><td>74.34</td><td>58.59</td><td>42.03</td><td>89.54</td><td>36.11</td></tr><tr><td>TeReDiff</td><td>15.71</td><td>.3799</td><td>.4575</td><td>.2706</td><td>71.29</td><td>50.49</td><td>16.78</td><td>.4282</td><td>.4243</td><td>.2526</td><td>65.61</td><td>56.65</td><td>45.09</td><td>38.52</td><td>37.69</td></tr><tr><td>TiGeSR</td><td>17.61</td><td>.4748</td><td>.4226</td><td>.2667</td><td>73.43</td><td>62.53</td><td>18.83</td><td>.5140</td><td>.4001</td><td>.2594</td><td>73.01</td><td>66.19</td><td>43.12</td><td>88.45</td><td>36.72</td></tr><tr><td>Ours</td><td>17.92</td><td>.5311</td><td>.3715</td><td>.2305</td><td>61.45</td><td>69.88</td><td>19.37</td><td>.5717</td><td>.3474</td><td>.2248</td><td>59.50</td><td>69.87</td><td>42.07</td><td>90.78</td><td>35.96</td></tr></table>

## A-page-0009

target PDF page 9

Table 3: Ablations on SynData with light degradation. Known and Unknown are evaluated on text-line crops. Overall OCR-A uses weights 724 : 716. OCR-A is in %. Rankings use displayed values within each block. The upper block marks best/second-best in bold/underlined, and the lower block marks only best in bold. The lower block uses the same fixed TiGeSR restoration model (T-R) with TiGeSR and [NAME C17] masks, respectively.

[tbl-2.html](tbl-2.html)

Table 4: Ablations on SynData with heavy degradation. Settings follow Table 3.

[tbl-3.html](tbl-3.html)

on Known, whereas visual-only performs better on Unknown, with the same pattern holding after correcting the prior branch's character labels. These results support complementary strengths across degradation levels and character subsets.

Effectiveness of [NAME C17]. With predicted OCR, adaptive selection outperforms both fixed branches in OCR-A on Known and Unknown under heavy degradation, but falls below visual-only under light degradation. With ground-truth labels and confidence fixed at 0.95, selection surpasses visual-only on both light-degradation subsets, achieving 79.24% overall OCR-A versus 79.17%. In contrast, prior-only with ground-truth labels reaches only 78.88%. Thus, improved prior reconstructions alone do not explain the gain; the results support the selector's ability to exploit complementary candidates under reliable recognition conditioning. The contrast with predicted-OCR selection suggests that recognition conditioning limits its benefits under light degradation.

Transferability of reconstructed text masks. Keeping the TiGeSR restoration weights fixed, substituting [NAME C17] masks improves overall recognition at both degradation levels, with gains on both subsets. These results show that our masks provide more useful recognition cues. However, these gains do not consistently extend to image-quality metrics, suggesting that more informative text masks without a matched restoration do not guarantee better restoration across all metrics.

## 5 CONCLUSION

We presented [NAME C17], a framework that combines geometry-aligned visual reconstruction and character-prior completion through legibility-guided selection to guide full-image text restoration. Experiments on SynData and [NAME C17] demonstrate strong textual fidelity across character subsets and degradation levels. Ablations show that visual reconstruction is more effective on Unknown under both degradation levels and on Known under light degradation, while character priors improve recognition on Known under heavy degradation. Adaptive selection improves overall OCR accuracy over either path under heavy degradation, but does not consistently surpass visual-only reconstruction under light degradation because of OCR accuracy. Future work will improve selection under uncertain recognition and geometry handling for complex scripts.

432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485

[OCR table id=tbl-2.html; page=9]
<table><tr><td rowspan="2">Setting</td><td colspan="6">Known</td><td colspan="6">Unknown</td><td>Overall</td></tr><tr><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>DISTS↓</td><td>FID↓</td><td>OCR-A↑</td><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>DISTS↓</td><td>FID↓</td><td>OCR-A↑</td><td>OCR-A↑</td></tr><tr><td>Full ([NAME C17])</td><td>21.70</td><td>.7405</td><td>.2413</td><td>.1618</td><td>42.41</td><td>81.10</td><td>22.96</td><td>.7481</td><td>.2273</td><td>.1569</td><td>41.58</td><td>76.87</td><td>79.00</td></tr><tr><td>Visual Branch Only</td><td>21.85</td><td>.7445</td><td>.2384</td><td>.1611</td><td>42.18</td><td>81.33</td><td>23.02</td><td>.7495</td><td>.2260</td><td>.1564</td><td>41.38</td><td>76.99</td><td>79.17</td></tr><tr><td>Prior Branch Only</td><td>21.41</td><td>.7341</td><td>.2467</td><td>.1649</td><td>44.08</td><td>81.27</td><td>22.88</td><td>.7450</td><td>.2361</td><td>.1643</td><td>43.81</td><td>76.43</td><td>78.86</td></tr><tr><td>Prior Only w/ GT OCR</td><td>21.40</td><td>.7338</td><td>.2469</td><td>.1649</td><td>44.16</td><td>81.29</td><td>22.90</td><td>.7449</td><td>.2366</td><td>.1649</td><td>44.02</td><td>76.45</td><td>78.88</td></tr><tr><td>Full w/ GT OCR</td><td>21.70</td><td>.7403</td><td>.2414</td><td>.1618</td><td>42.45</td><td>81.38</td><td>22.97</td><td>.7481</td><td>.2273</td><td>.1568</td><td>41.54</td><td>77.08</td><td>79.24</td></tr><tr><td>TiGeSR</td><td>20.38</td><td>.6615</td><td>.3085</td><td>.2045</td><td>54.30</td><td>76.58</td><td>21.79</td><td>.6782</td><td>.2961</td><td>.2020</td><td>54.95</td><td>75.73</td><td>76.16</td></tr><tr><td>w/ T-R</td><td>19.21</td><td>.6185</td><td>.3174</td><td>.2070</td><td>54.70</td><td>79.69</td><td>20.77</td><td>.6520</td><td>.2990</td><td>.2026</td><td>53.82</td><td>75.84</td><td>77.78</td></tr></table>

[OCR table id=tbl-3.html; page=9]
<table><tr><td rowspan="2">Setting</td><td colspan="6">Known</td><td colspan="6">Unknown</td><td>Overall</td></tr><tr><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>DISTS↓</td><td>FID↓</td><td>OCR-A↑</td><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>DISTS↓</td><td>FID↓</td><td>OCR-A↑</td><td>OCR-A↑</td></tr><tr><td>Full ([NAME C17])</td><td>17.92</td><td>.5311</td><td>.3715</td><td>.2305</td><td>61.45</td><td>69.88</td><td>19.37</td><td>.5717</td><td>.3474</td><td>.2248</td><td>59.50</td><td>69.87</td><td>69.88</td></tr><tr><td>Visual Branch Only</td><td>18.24</td><td>.5421</td><td>.3700</td><td>.2322</td><td>63.06</td><td>68.59</td><td>19.45</td><td>.5744</td><td>.3459</td><td>.2247</td><td>59.49</td><td>69.74</td><td>69.16</td></tr><tr><td>Prior Branch Only</td><td>17.77</td><td>.5270</td><td>.3728</td><td>.2317</td><td>61.98</td><td>69.78</td><td>19.46</td><td>.5741</td><td>.3578</td><td>.2362</td><td>62.33</td><td>67.21</td><td>68.50</td></tr><tr><td>Prior Only w/ GT OCR</td><td>17.76</td><td>.5268</td><td>.3727</td><td>.2315</td><td>61.95</td><td>69.91</td><td>19.49</td><td>.5742</td><td>.3589</td><td>.2373</td><td>62.63</td><td>68.28</td><td>69.10</td></tr><tr><td>Full w/ GT OCR</td><td>17.92</td><td>.5310</td><td>.3713</td><td>.2305</td><td>61.31</td><td>70.05</td><td>19.38</td><td>.5720</td><td>.3473</td><td>.2248</td><td>59.52</td><td>70.11</td><td>70.08</td></tr><tr><td>TiGeSR</td><td>17.61</td><td>.4748</td><td>.4226</td><td>.2667</td><td>73.43</td><td>62.53</td><td>18.83</td><td>.5140</td><td>.4001</td><td>.2594</td><td>73.01</td><td>66.19</td><td>64.35</td></tr><tr><td>w/ T-R</td><td>16.61</td><td>.4282</td><td>.4336</td><td>.2684</td><td>76.40</td><td>68.54</td><td>18.22</td><td>.4951</td><td>.4058</td><td>.2643</td><td>74.91</td><td>67.28</td><td>67.91</td></tr></table>

## A-page-0010

target PDF page 10

486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539

## AI USE STATEMENT

We used AI-assisted tools to help identify and fix bugs in our implementation, organize intermediate files generated during experiments, and polish the language and clarity of the manuscript. The authors take full responsibility for the correctness of the implementation, the accuracy of the reported results, and the final content of the paper.

## REFERENCES

Eirikur Agustsson and Radu Timofte. NTIRE 2017 challenge on single image super-resolution: Dataset and study. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition Workshops, pp. 126–135, 2017.

Jianrui Cai, Hui Zeng, Hongwei Yong, Zisheng Cao, and Lei Zhang. Toward real-world single image super-resolution: A new benchmark and a new model. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 3086–3095, 2019.

Jingye Chen, Bin Li, and Xiangyang Xue. Scene text telescope: Text-focused scene image super-resolution. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 12026–12035, 2021.

Kun Cheng, Lei Yu, Zhijun Tu, Xiao He, Liyu Chen, Yong Guo, Mingrui Zhu, Nannan Wang, Xinbo Gao, and Jie Hu. Effective diffusion transformer architecture for image super-resolution. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 39, pp. 2455–2463, 2025. doi: 10.1609/aaai.v39i3.32247.

Keyan Ding, Kede Ma, Shiqi Wang, and Eero P. Simoncelli. Image quality assessment: Unifying structure and texture similarity. IEEE Transactions on Pattern Analysis and Machine Intelligence, 44(5):2567–2581, 2022. doi: 10.1109/TPAMI.2020.3045810.

Zheng-Peng Duan, Jiawei Zhang, Xin Jin, Ziheng Zhang, Zheng Xiong, Dongqing Zou, Jimmy S. Ren, Chunle Guo, and Chongyi Li. DiT4SR: Taming diffusion transformer for real-world image super-resolution. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 18948–18958, 2025.

Ankush Gupta, Andrea Vedaldi, and Andrew Zisserman. Synthetic data for text localisation in natural images. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 2315–2324, 2016.

Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter. GANs trained by a two time-scale update rule converge to a local Nash equilibrium. In Advances in Neural Information Processing Systems, volume 30, 2017.

Dimosthenis Karatzas, Lluis Gomez-Bigorda, Anguelos Nicolaou, Suman Ghosh, Andrew Bagdanov, Masakazu Iwamura, Jiri Matas, Lukas Neumann, Vijay R. Chandrasekhar, Shijian Lu, Faisal Shafait, Seiichi Uchida, and Ernest Valveny. ICDAR 2015 competition on robust reading. In International Conference on Document Analysis and Recognition, pp. 1156–1160, 2015. doi: 10.1109/ICDAR.2015.7333942.

Jin Hyeon Kim, Paul Hyunbin Cho, Claire Kim, Jaewon Min, Jaeun Lee, Jihye Park, Yeji Choi, and Seungryong Kim. Unified diffusion transformer for high-fidelity text-aware image restoration. arXiv preprint arXiv:2512.08922, 2025.

Xiaoming Li, Wangmeng Zuo, and Chen Change Loy. Learning generative structure prior for blind text image super-resolution. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 10103–10113, 2023.

Xiaoming Li, Wangmeng Zuo, and Chen Change Loy. Enhanced generative structure prior for chinese text image super-resolution. IEEE Transactions on Pattern Analysis and Machine Intelligence, 47(12):11366–11381, 2025. doi: 10.1109/TPAMI.2025.3596329.

## A-page-0011

target PDF page 11

540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593

Xinqi Lin, Jingwen He, Ziyan Chen, Zhaoyang Lyu, Bo Dai, Fanghua Yu, Yu Qiao, Wanli Ouyang, and Chao Dong. DiffBIR: Toward blind image restoration with generative diffusion prior. In Proceedings of the European Conference on Computer Vision, pp. 430–448, 2024.

Xinqi Lin, Fanghua Yu, Jinfan Hu, Zhiyuan You, Wu Shi, Jimmy S. Ren, Jinjin Gu, and Chao Dong. Harnessing diffusion-yielded score priors for image restoration. ACM Transactions on Graphics, 44(6):1–21, 2025. doi: 10.1145/3763346.

Xi Liu, Rui Zhang, Yongsheng Zhou, Qianyi Jiang, Qi Song, Nan Li, Kai Zhou, Lei Wang, Dong Wang, Minghui Liao, Mingkun Yang, Xiang Bai, Baoguang Shi, Dimosthenis Karatzas, Shijian Lu, and C. V. Jawahar. ICDAR 2019 robust reading challenge on reading Chinese text on signboard. In International Conference on Document Analysis and Recognition, pp. 1577–1581, 2019. doi: 10.1109/ICDAR.2019.00253.

Minxing Luo, Linlong Fan, Qiushi Wang, Ge Wu, Yiyan Luo, Yuhang Yu, Jinwei Chen, Yaxing Wang, Qingnan Fan, and Jian Yang. Restore text first, enhance image later: Two-stage scene text image super-resolution with glyph structure guidance. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 30553–30563, 2026.

Jianqi Ma, Zhetong Liang, and Lei Zhang. A text attention network for spatial deformation robust scene text image super-resolution. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 5911–5920, 2022.

Jianqi Ma, Shi Guo, and Lei Zhang. Text prior guided scene text image super-resolution. IEEE Transactions on Image Processing, 32:1341–1353, 2023. doi: 10.1109/TIP.2023.3237002.

Jaewon Min, Jin Hyeon Kim, Paul Hyunbin Cho, Jaeeun Lee, Jihye Park, Minkyu Park, Sangpil Kim, Hyunhee Park, and Seungryong Kim. Text-aware image restoration with diffusion models. In Proceedings of the International Conference on Learning Representations, 2026.

Nibal Nayef, Yash Patel, Michal Busta, Pinaki Nath Chowdhury, Dimosthenis Karatzas, Wafa Khlif, Jiri Matas, Umapada Pal, Jean-Christophe Burie, Cheng-Lin Liu, and Jean-Marc Ogier. ICDAR2019 robust reading challenge on multi-lingual scene text detection and recognition—RRC-MLT-2019. In International Conference on Document Analysis and Recognition, pp. 1582–1587, 2019. doi: 10.1109/ICDAR.2019.00254.

Rui Qin and Bin Wang. Scene text image super-resolution via content perceptual loss and criss-cross transformer blocks. In Proceedings of the International Joint Conference on Neural Networks, pp. 1–10, 2024. doi: 10.1109/IJCNN60899.2024.10650570.

Qin Shi, Yu Zhu, Chuantao Fang, and Dawei Yang. TLWSR: Weakly supervised real-world scene text image super-resolution using text label. IET Image Processing, 17(9):2780–2790, 2023. doi: 10.1049/ipr2.12827.

Radu Timofte, Eirikur Agustsson, Luc Van Gool, Ming-Hsuan Yang, and Lei Zhang. NTIRE 2017 challenge on single image super-resolution: Methods and results. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition Workshops, pp. 114–125, 2017.

Jianyi Wang, Zongsheng Yue, Shangchen Zhou, Kelvin C. K. Chan, and Chen Change Loy. Exploiting diffusion prior for real-world image super-resolution. International Journal of Computer Vision, 132(12):5929–5949, 2024. doi: 10.1007/s11263-024-02168-7.

Wenjia Wang, Enze Xie, Peize Sun, Wenhai Wang, Lixun Tian, Chunhua Shen, and Ping Luo. TextSR: Content-aware text super-resolution guided by recognition. arXiv preprint arXiv:1909.07113, 2019.

Wenjia Wang, Enze Xie, Xuebo Liu, Wenhai Wang, Ding Liang, Chunhua Shen, and Xiang Bai. Scene text image super-resolution in the wild. In Proceedings of the European Conference on Computer Vision, pp. 650–666. Springer, 2020. doi: 10.1007/978-3-030-58607-2_38.

Xintao Wang, Liangbin Xie, Chao Dong, and Ying Shan. Real-ESRGAN: Training real-world blind super-resolution with pure synthetic data. In Proceedings of the IEEE/CVF International Conference on Computer Vision Workshops, pp. 1905–1914, 2021.

## A-page-0012

target PDF page 12

594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647

Zhou Wang, Alan C. Bovik, Hamid R. Sheikh, and Eero P. Simoncelli. Image quality assessment: From error visibility to structural similarity. IEEE Transactions on Image Processing, 13(4): 600–612, 2004. doi: 10.1109/TIP.2003.819861.

Rongyuan Wu, Lingchen Sun, Zhiyuan Ma, and Lei Zhang. One-step effective diffusion network for real-world image super-resolution. In Advances in Neural Information Processing Systems, volume 37, 2024a. doi: 10.52202/079017-2938.

Rongyuan Wu, Tao Yang, Lingchen Sun, Zhengqiang Zhang, Shuai Li, and Lei Zhang. SeeSR: Towards semantics-aware real-world image super-resolution. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 25456–25467, 2024b.

Tao Yang, Rongyuan Wu, Peiran Ren, Xuansong Xie, and Lei Zhang. Pixel-aware stable diffusion for realistic image super-resolution and personalized stylization. In Proceedings of the European Conference on Computer Vision, pp. 74–91. Springer, 2024. doi: 10.1007/978-3-031-73247-8_5.

Fanghua Yu, Jinjin Gu, Zheyuan Li, Jinfan Hu, Xiangtao Kong, Xintao Wang, Jingwen He, Yu Qiao, and Chao Dong. Scaling up to excellence: Practicing model scaling for photo-realistic image restoration in the wild. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 25669–25680, 2024.

Kai Zhang, Jingyun Liang, Luc Van Gool, and Radu Timofte. Designing a practical degradation model for deep blind image super-resolution. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 4791–4800, 2021.

Richard Zhang, Phillip Isola, Alexei A. Efros, Eli Shechtman, and Oliver Wang. The unreasonable effectiveness of deep features as a perceptual metric. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 586–595, 2018.

Yubo Zhang, Xueqing Wang, Manhui Lin, Yue Zhang, Penglongyi Deng, Ting Sun, Tingquan Gao, Zelun Zhang, Jiaxuan Liu, Changda Zhou, Hongen Liu, Suyin Liang, Cheng Cui, Yi Liu, Dianhai Yu, and Yanjun Ma. PP-OCRv6: From 1.5M to 34.5M parameters, surpassing billion-scale VLMs on OCR tasks, 2026.

Yuzhe Zhang, Jiawei Zhang, Hao Li, Zhouxia Wang, Luwei Hou, Dongqing Zou, and Liheng Bian. Diffusion-based blind text image super-resolution. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 25827–25836, 2024.

Minyi Zhao, Miao Wang, Fan Bai, Bingjia Li, Jie Wang, and Shuigeng Zhou. C3-STISR: Scene text image super-resolution with triple clues. In Proceedings of the International Joint Conference on Artificial Intelligence, pp. 1707–1713, 2022. doi: 10.24963/ijcai.2022/238.
