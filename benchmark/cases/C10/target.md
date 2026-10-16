# [TITLE C10]

## A-page-0001

target PDF page 1

# [TITLE C10]

Anonymous authors

Paper under double-blind review

# ABSTRACT

Vision-language models (VLMs) suffer from visual hallucination, such as saying an object that is not present in an image. We ask a more fundamental question: whether a VLM is even aware of where it is looking before understanding the semantic meaning in the image. We formulate this question as a [NAME C10] task: identifying which parts of its visual input were available to the model. We construct the task in a self-supervised way without manually labeling the available region to the model. Our experiments show that existing VLMs fail to localize the visible region. We further show that fine-tuning VLMs on the proposed [NAME C10] task improves a model's awareness of visual input.

# 1 INTRODUCTION

Vision-language models (VLMs) can describe images fluently while referring to objects that are not actually present. This failure mode, commonly termed visual hallucination, has been widely evidenced (Rohrbach et al., 2018; Li et al., 2023; Chen et al., 2024b) and persists even in frontier models. For example, Asadi et al. (2026) show that Gemini-3-Pro, Gemini-2.5-Pro, Claude-Opus-4.5, and GPT-5.1 can readily produce detailed image descriptions and elaborate reasoning traces even when no image is provided. This observation suggests that visual hallucination can arise prior to visual misinterpretation: the model may fail to reliably distinguish between the presence and absence of visual input. In this sense, current VLMs lack a basic form of visual-input awareness, the ability to recognize whether they are receiving visual information at all. This stands in sharp contrast to human visual perception, where an observer is inherently aware of whether visual input is available, for example, whether their eyes are open or closed.

However, existing efforts to address visual hallucination are limited at the level of semantics. They curate instruction data with negative and counterfactual examples (Liu et al., 2024a), align outputs with factual or human preferences (Sun et al., 2024), or intervene during decoding to suppress content the image does not support (Leng et al., 2024; Huang et al., 2024). Despite their differences, these methods address essentially the same question: whether the model's claims about the visual

![img-0.jpeg](img-0.jpeg)

Figure 1: Hierarchy of visual understanding: [NAME C10] → Perceive → Understand. We introduce a hierarchical visual grounding structure and argue that visual hallucination can arise from any level. This work focuses on the fundamental Look level.

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

scene are semantically correct. We instead ask a more fundamental question that precedes semantic interpretation: Is a VLM aware of where it is looking in the first place before reasoning about what the visual input means?

To this end, we argue that general visual grounding can be organized into a three-level hierarchy as shown in Fig. 1: Look identifies where the model is looking, Perceive determines what is present there, and Understand uses this evidence to answer a question or draw an inference. We hypothesize that visual hallucination may arise as early as the first level, Look, a capability that remains largely untested by existing benchmarks. A model should ground its claims in available visual input when asserting that it sees something and, more fundamentally, should be aware of whether visual input is available at all.

We therefore propose [NAME C10], a task designed to probe a VLM's awareness of the visual input available to it. Specifically, the model is given an image crop and must localize the visible region as a bounding box in the coordinate frame of the original image. We encode only the crop pixels, while assigning each crop patch the same positional embedding it would have received in the full image. Thus, although the excluded scene content is unavailable, the model retains all geometric information required to localize the crop. Intuitively, this is analogous to covering one of a person's eyes and asking them to identify which eye is covered. [NAME C10] probes a model's awareness of the visual input available to it, rather than the semantic content of what it sees.

Our experiments primarily use Qwen3-VL, which preserves absolute positional information for image patches, whereas many other VLMs rely only on relative positional embeddings and therefore lack the spatial cues required for the [NAME C10] task. We first show that pretrained VLMs fail to reliably localize the visual input available to them. We then fine-tune Qwen3-VL on automatically constructed [NAME C10] data and find that the model can learn the task and generalize well to unseen examples. To evaluate whether [NAME C10] improves a VLM's awareness of visual input more broadly, we further introduce the [NAME C10] ([NAME C10]). In [NAME C10], visual tokens are replaced with null <image_pad> tokens, and the model is asked whether a target object is present in the image. Models fine-tuned on [NAME C10] substantially outperform the corresponding baselines, suggesting that [TITLE C10] enhances a model's awareness of available visual evidence and naturally helps mitigate visual hallucination.</image_pad>

Our contributions are threefold:

(i) We introduce a three-level hierarchy of visual grounding. The hierarchy decomposes visual grounding into Look, Perceive, and Understand, providing a framework for studying visual hallucination at a more fundamental level.
(ii) We propose the [NAME C10] task for improving visual awareness through self-supervision. [NAME C10] training data can be generated from arbitrary image datasets by cropping images, with the crop region itself providing bounding-box supervision and requiring no semantic annotation.
(iii) We introduce [NAME C10] to evaluate a VLM's awareness of visual input. We show that pretrained VLMs can hallucinate object presence even when visual evidence is absent, while fine-tuning on [NAME C10] substantially improves visual awareness and reduces such hallucinations.

## 2 HIERARCHY OF VISUAL UNDERSTANDING

Visual understanding is commonly evaluated by the success rate on visual question answering (VQA) tasks. However, when a model produces an incorrect answer, it is often difficult to determine where the failure originates. We argue that visual understanding involves multiple stages, and that visual hallucination can arise at any of them. Effectively mitigating visual hallucination therefore requires identifying the stage at which the failure occurs and addressing its underlying cause.

To this end, we propose a three-level hierarchy of visual understanding as shown in Fig. 1. Let I denote an image, w a region of it, I_w the pixels inside w, and P_w the positions those pixels occupy in I. The three levels answer three different questions about the given image input:

$$\underbrace{\hat{w} = L(I_w, P_w)}_{\text{Look: did I see and where is it?}}, \quad \underbrace{\hat{z} = P(I_w)}_{\text{Perceive: what is in it?}}, \quad \underbrace{\hat{a} = U(\hat{z}, q)}_{\text{Understand: what follows?}}, \tag{1}$$

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

![img-2.jpeg](img-2.jpeg)

![img-3.jpeg](img-3.jpeg)

Figure 2: Where does a hallucination originate? In this example, we ask what animal is grazing in a photograph of a dog on grassland, a model answers “a sheep”. The same wrong answer can arise at two levels of the hierarchy. At the Perceive level, the model uses the image but misrecognizes the dog. At the Look level, the model does not rely on the image at all, and “sheep” follows from the textual context.

where  \( \hat{z} \)  denotes observations and q a question. Particularly, the ordering of the hierarchy expresses the dependence of evidence to conclude the final visual understanding: a claim about what the image contains  \( (P) \)  or implies  \( (U) \)  should presuppose some account of what input was available  \( (L) \) . Consider the limiting case where an input that carries no visual content at all. In this case, the correct output of L is that nothing is visible, and every positive claim of P is a hallucination without grounding (Asadi et al., 2026).

Source of visual hallucination. While existing work largely focuses on semantic-level visual perception and reasoning, our hierarchy highlights the more fundamental role of Look in visual grounding. Before interpreting visual content, a model should first be aware of the visual input available to it and distinguish visual evidence from textual context. For example (Fig. 2), if a model hallucinates a sheep in an image of grassland containing a dog, the failure may arise because it misperceives the dog as a sheep, corresponding to a failure at the Perceive level. More fundamentally, however, the model may fail to rely on the image at all and instead generate sheep from textual associations with the surrounding context, corresponding to a failure at the Look level. Distinguishing these failure modes is essential for identifying where visual hallucination originates and how it should be addressed.

## 3 THE [NAME C10] TASK

Motivated by the proposed hierarchy and the goal of improving visual grounding at the fundamental Look level, we design the [NAME C10] task to quantify a VLM's awareness of its available visual input. We further use the task as a self-supervised training objective to enhance this awareness. A central challenge, however, is to disentangle visual-input awareness from semantic shortcuts that could allow the model to solve the task without actually identifying where it is looking.

### 3.1 CONSTRUCTING A [NAME C10] EXAMPLE

Just as a person knows which part of their surroundings falls within their view, a model should know which part of an image it receives. In the [NAME C10] task, the full image plays the role of the environment and a crop plays the role of the available view (Fig. 3). We sample a rectangular window aligned with the model's visual-token grid, encode only the pixels inside it, and ask the model for the bounding box of the window in the coordinate frame of the full image. Because we sample the window ourselves, the label can be automatically obtained and any image can be used as [NAME C10] examples.

However, a crop encoded on its own carries no trace of where it came from. The same pixels could occur anywhere in a larger image, and a model could only guess from semantic cues, such as sky suggesting the top of a scene. We therefore assign each crop token the positional information it would have received in the full image. We implement [NAME C10] on Qwen3-VL (Qwen Team, 2025),

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

![img-4.jpeg](img-4.jpeg)

Figure 3: Constructing a [NAME C10] example. We select a merge-block-aligned viewport and encode only its pixels for the VLM. Importantly, we restore positional metadata from the full canvas without encoding the excluded image content. The crop's coordinates provide the target automatically. Changed blocks indicate places where token positions are added.

which preserves absolute positional information for image patches and thus provides the spatial cues needed to identify the available region. Specifically, as illustrated in Fig. 3, we preserve the crop's original full-image positions at two points in the architecture: the vision encoder's absolute positional embeddings ① and the language model's multimodal rotary positional embeddings (MRoPE) ②. In this way, the geometric information required for localization is explicitly available, allowing the model to identify its available visual region without relying on semantic cues to infer its location. The [NAME C10] task therefore directly probes whether the model can recognize where its visual input comes from. Implementation details are provided in App. B.

### 3.2 TRAINING WITH [NAME C10] DATA

Visual perception verbs as the interface between language and vision. To improve a model's visual awareness, we encourage it to be sensitive when generating expressions that explicitly invoke visual perception, such as I see and I observe. We view such expressions as a linguistic interface between the language and visual modalities: when a model claims to see something, that claim should be grounded in the visual input available to it. Accordingly, we equip each [NAME C10] example with diverse localization prompts that invoke such visual-perception expressions, as listed in App. E.

Concretely, each [NAME C10] example pairs a localization prompt $q_{\text{look}}$ with the bounding box $y(w)$ of the sampled window, represented in the model's coordinate format as defined in Eq. (4). Given an existing instruction-tuning mixture dataset $D_{\text{inst}}$ and the generated [NAME C10] dataset $D_{\text{look}}$, we train on their union using the standard autoregressive cross-entropy objective:

$$\mathcal{L}(\theta) = - \frac{1}{\sum_{(x,q,r) \in D} |r|} \sum_{(x,q,r) \in D} \sum_{t=1}^{|r|} \log p_{\theta}(r_t \mid x, q, r_{<t}), \quad D = D_{\text{inst}} \cup D_{\text{look}}, \tag{2}$$

where $r$ is the target response of an example and $|r|$ its length in tokens, so the loss is averaged over all response tokens. For [NAME C10] examples, $r$ is the serialized box $y(w)$ and $x = (I_w, P_w)$ denotes the cropped visual input and its positional information, while ordinary instruction examples retain their original image inputs and responses.

## 4 [NAME C10]: EVALUATING VLMs' ILLUSION

The [NAME C10] task examines where the available visual input lies within a scene. Its limiting case concerns whether any visual input is available at all. A model that is aware of its visual input should recognize when none is present, rather than describe content it has never received, the illusion failure shown in Asadi et al. (2026). To evaluate VLMs' illusion, we introduce the [NAME C10] ([NAME C10]).

Benchmark construction. [NAME C10] uses all 10,752 referring expressions from the RefCOCO testA and testB splits (Yu et al., 2016), spanning 1,500 COCO images (Lin et al., 2014). For each expression, we ask the model: "Does this image contain: {expression}? Answer with Yes or No." We evaluate three input conditions, illustrated in Fig. 4:

## A-page-0005

target PDF page 5

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

![img-5.jpeg](img-5.jpeg)

(i) Real image

![img-6.jpeg](img-6.jpeg)

(ii) No image

![img-7.jpeg](img-7.jpeg)

(iii) Wrong image

Figure 4: Illustration of [NAME C10] construction. All conditions use the same prompt, “Does this image contain: dog? Answer with Yes or No.”, with the only difference being the visual input. The grounded answer is Yes in (i) and No in (ii) and (iii).

(i) Real image. The expression is paired with its original image, which contains the referred object; the correct answer is therefore Yes.
(ii) No image. We bypass the vision encoder while retaining the \(<|\text{image\_pad}|>\) placeholder embedding at each visual-token position. This preserves the sequence length, token positions, and attention mask of the corresponding real-image input while removing all visual content. The correct answer is therefore No.
(iii) Wrong image. Each image is paired with the expression of a different item, for which the expected answer is No.

We use the same 10,752 items, the same set of images and referring expressions throughout for the three conditions. The no-image condition serves as our primary test of visual awareness.

Metrics. We score the model from the logits  \( \ell \)  at the first answer position instead of parsing generated text, since free-form responses can vary substantially. Answers such as “Yes.”, “yes, it does”, or a longer sentence that never clearly commits to either answer make string-based evaluation brittle and discard information about confidence. We therefore compute

\[
p (\text { Yes }) = \sigma \left(\log \sum_ {t \in \mathcal {Y}} e ^ {\ell_ {t}} - \log \sum_ {t \in \mathcal {N}} e ^ {\ell_ {t}}\right), \tag {3}
\]

where  \( \sigma \)  is the logistic function and Y and N contain every vocabulary token whose surface form, ignoring case and surrounding whitespace, is Yes and No, respectively. We classify an answer as Yes when  \( p(\text{Yes}) > 0.5 \) . This readout requires only a single forward pass, avoids parsing failures, and provides a continuous confidence score.

We report the following metrics for each of the three input conditions:

(1) Yes rate: the fraction of examples for which the model answers Yes. In the no-image condition it is our primary metric ( \( \downarrow \) ), corresponding to false claims that the referred object is visually present. In the real-image condition ( \( \uparrow \) ) it controls for whether the model still recognizes the referred object when the correct image is provided; a model that always answers No would score perfectly on the no-image Yes rate but fail here. In the wrong-image condition ( \( \downarrow \) ) it gives a coarse measure of whether the model checks the referring expression against the actual image content.
(2) Mean \( p(\text{Yes}) \): the average probability assigned to Yes, with the same direction as the Yes rate in each condition. It captures the model's confidence even when this remains below the decision threshold.
(3) \( Gap(\uparrow) \): the difference between the real-image and no-image Yes rates, summarizing the model's sensitivity to the presence of visual evidence.

## A-page-0006

target PDF page 6

Table 1: Compare different probe methods for visual awareness. We report IoU of the pretrained Qwen3-VL when asked for the visible region over 1,000 views. IoU counts answers without a valid box as zero. Methods operating on pixels or patch embeddings fail to probe visual awareness because the model can exploit semantic shortcuts, often predicting the bounding box of the dominant object rather than the available visual region.

[tbl-0.html](tbl-0.html)

(i) Full image

![img-8.jpeg](img-8.jpeg)

IoU 0.47

(ii) Pixel greyed

![img-9.jpeg](img-9.jpeg)

IoU 0.64

(iii) Embedding zeroed

![img-10.jpeg](img-10.jpeg)

IoU 0.57

(iv) [NAME C10]

![img-11.jpeg](img-11.jpeg)

IoU 0.20

Figure 5: Four ways to probe visual awareness. The green box shows the available visual region while the red dashed box shows the prediction. (i) We input the full image, but the model boxes the dominant person rather than the whole canvas. (ii, iii) When the context pixels are greyed out or its embeddings are zeroed, the model still locates the dominant person, likely using semantic shortcuts. (iv) In [NAME C10], the model answers with the whole canvas.

## 5 EXPERIMENTS

We design experiments to answer four questions: (i) whether [NAME C10] measures visual awareness without semantic shortcuts, (ii) whether the [NAME C10] task is learnable, (iii) whether [NAME C10] fine-tuning improves [NAME C10] performance, and (iv) whether [NAME C10] fine-tuning preserves the model's general visual perception capabilities.

### 5.1 SETUP

Training dataset. To improve visual awareness while preserving the VLM's general capabilities, we train on a mixture of replay data and the proposed [NAME C10] data. (i) Replay mixture dataset. We use 46,000 instruction-tuning examples drawn from eight public datasets as detailed in App. A. (ii) [NAME C10] dataset. We construct the [NAME C10] data from the same replay images by sampling one window per image as described in Sec. 3 and pairing each crop with one of the 36 localization prompts listed in App. E. To study the effect of [NAME C10] supervision, we combine the full replay mixture with \(10\%\), \(20\%\), and \(100\%\) of the [NAME C10] dataset, denoted as [NAME C10]-to-replay ratios of 1:10, 2:10, and 10:10.

Model training and baselines. We experiment with Qwen3-VL-8B-Instruct (Qwen Team, 2025) since it uses absolute positional embeddings for image patches. We fine-tune the model with LoRA (Hu et al., 2022) of rank 16 and scale 32 on all linear layers, keeping the vision encoder and the projector frozen, and train for two epochs with a learning rate of \(10^{-4}\), an effective batch size of 32, and a maximum sequence length of 4096, using the objective in Eq. (2). Training is implemented with ms-swift (Zhao et al., 2025) on four H200 GPUs. We compare three configurations. (i) The SFT baseline is trained on the replay instruction mixture alone. (ii) Ours is trained on the mixture together with [NAME C10] data at the three ratios above. (iii) LocPos is an ablation that uses the same [NAME C10] data as Ours (10:10) but disables the positional restoration of Sec. 3.1 during training, so that each crop carries crop-local positions. This ablation separates the contribution of global positional information from that of the crop data and the answer format.

### 5.2 HOW TO MEASURE VISUAL AWARENESS WITHOUT SEMANTIC SHORTCUTS?

We aim to measure a VLM's awareness of its available visual input while preventing it from exploiting semantic shortcuts. We compare four families of probes as illustrated in Fig. 5. (i) Full image.

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

[OCR table id=tbl-0.html; page=6]
<table><tr><td rowspan="2">Probe methods</td><td rowspan="2">Full image</td><td colspan="2">Pixel operation</td><td colspan="2">Patch embedding</td><td colspan="2">Crop</td></tr><tr><td>Black</td><td>Grey</td><td>Zero</td><td>Mean</td><td>Local pos.</td><td>Global pos. ([NAME C10])</td></tr><tr><td>IoU ↓</td><td>0.52</td><td>0.75</td><td>0.77</td><td>0.58</td><td>0.76</td><td>0.18</td><td>0.18</td></tr></table>

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

Table 2: Performance on [NAME C10] task. Results are tested on the same 1,000 views of Table 1. Success@0.5 is the fraction of views with an IoU of at least 0.5.

[tbl-1.html](tbl-1.html)

![img-12.jpeg](img-12.jpeg)

Figure 7: Permutation test. The grey bars mean IoU after re-pairing each prediction with the window of another image while the color lines show the IoU on the given image. The pretrained and SFT models show no positive dependence on the view.

We input the full image and ask the model about its visible region. (ii) Pixel operations. We paint the hidden region black or gray. (iii) Patch-embedding operations. We set the embeddings of the hidden patches to zero or to their mean. (iv) Crop based. We encode only the visible region, with either local or global positions used to compute the absolute positional embeddings in Qwen3-VL.

We evaluate each probe on the pretrained model using 1,000 views sampled from the RefCOCO validation images (Yu et al., 2016; Lin et al., 2014). As shown in Table 1, pixel- and patch-embedding-based probes achieve higher IoU, but this performance is largely driven by semantic shortcuts. The model often predicts the extent of dominant objects rather than the available visual region, a behavior also evident in the full-image setting. We therefore adopt cropping with global positional information for the [NAME C10] task, as it removes the hidden content while preserving the geometric information required for localization.

### 5.3 [TITLE C10]

In this section, we examine whether the [NAME C10] task is learnable. Following the training setup in Sec. 5.1, we compare model performance on the [NAME C10] task. As the results shown in Table 2 and the learning dynamics in Fig. 6, combining replay instruction data with [NAME C10] data substantially improves localization performance. In contrast, LocPos fails to learn the task because it lacks the global positional information used by our method. Notably, even a 1:10 ratio of [NAME C10] data to replay data yields a substantial improvement.

Do predictions depend on the given view? To further assess if the model is truly aware of its visual input, we perform a permutation test by pairing each prediction

with the target window from another image. As shown in Fig. 7, the Base and SFT models achieve even higher IoU under permutation (grey bars), indicating that their predictions are poorly grounded in the actual visual input.

![img-13.jpeg](img-13.jpeg)

Figure 6: [TITLE C10] dynamics.

[OCR table id=tbl-1.html; page=7]
<table><tr><td rowspan="2">Method</td><td rowspan="2">Base</td><td rowspan="2">SFT</td><td rowspan="2">LocPos</td><td colspan="3">Ours</td></tr><tr><td>1:10</td><td>2:10</td><td>10:10</td></tr><tr><td>IoU ↑</td><td>0.181</td><td>0.111</td><td>0.371</td><td>0.609</td><td>0.665</td><td>0.742</td></tr><tr><td>Success@0.5 ↑</td><td>0.025</td><td>0.012</td><td>0.322</td><td>0.734</td><td>0.808</td><td>0.844</td></tr></table>

## A-page-0008

target PDF page 8

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

Table 3: [NAME C10]. All 10,752 items, identical for every model. No image: features withheld, correct answer No. Real image: the expression's own image, correct answer Yes. Wrong image: the image of a different item, approximately No. For each condition we report the Yes rate in percent and the mean p(Yes). Gap is the real-image minus the no-image Yes rate. The bottom rows are other pretrained VLMs (Bai et al., 2025; Liu et al., 2024b; Gemma Team, 2026). †The image placeholder embedding of this model is untrained, so it answers neither Yes nor No without an image and the no-image results are not reported.

[tbl-2.html](tbl-2.html)

Table 4: [NAME C10] maintains general capabilities. We report accuracy (%) on MMStar, MMMU and MMMU-Pro and F1 score on POPE. We evaluate 500 items per benchmark.

[tbl-3.html](tbl-3.html)

### 5.4 DOES [NAME C10] FINE-TUNING IMPROVE [NAME C10]?

We next evaluate whether training on [NAME C10] improves visual awareness as measured by [NAME C10]. As shown in Table 3, [NAME C10] fine-tuning consistently improves performance. In particular, Ours (10:10) reduces the no-image Yes rate to 0.8%, compared with 2.5% for the pretrained model and 31.2% for standard SFT, while maintaining a comparable real-image Yes rate. It also achieves the largest real-to-no-image gap of 93.2. These results indicate that [NAME C10] improves the model's awareness of whether visual input is actually available without compromising its ability to recognize objects when an image is present. We note that this failure is also not specific to Qwen3-VL. For example, Gemma-4-12B (Gemma Team, 2026) answers Yes on 42.9% of no-image items.

### 5.5 DOES [NAME C10] FINE-TUNING PRESERVE GENERAL CAPABILITIES?

Finally, we examine whether [NAME C10] training affects the model's general capabilities. As shown in Table 4, on MMStar (Chen et al., 2024a), POPE (Li et al., 2023), MMMU (Yue et al., 2024), and MMMU-Pro (Yue et al., 2025), all of our models remain within 2.5 points of the SFT baseline. In particular, Ours (1:10), which uses the smallest amount of [NAME C10] data while already substantially reducing hallucination in the absence of visual input, performs on par with or better than SFT across all four benchmarks. We hypothesize that the transfer of visual awareness learned by [NAME C10] to the general VLM benchmarks needs more careful datasets and training design. Also note that the visual hallucination can arise from the semantic perception and understanding levels which need extra techniques to address in addition to the [NAME C10]. We leave this to the future work.

[OCR table id=tbl-2.html; page=8]
<table><tr><td rowspan="2"></td><td colspan="2">No image</td><td colspan="2">Real image</td><td colspan="2">Wrong image</td><td rowspan="2">Gap ↑</td></tr><tr><td>Yes (%) ↓</td><td>p(Yes) ↓</td><td>Yes (%) ↑</td><td>p(Yes) ↑</td><td>Yes (%) ↓</td><td>p(Yes) ↓</td></tr><tr><td>Base</td><td>2.5</td><td>0.041</td><td>93.3</td><td>0.927</td><td>15.6</td><td>0.158</td><td>90.7</td></tr><tr><td>SFT</td><td>31.2</td><td>0.409</td><td>94.9</td><td>0.915</td><td>17.0</td><td>0.196</td><td>63.7</td></tr><tr><td>LocPos</td><td>5.7</td><td>0.272</td><td>92.6</td><td>0.890</td><td>15.0</td><td>0.170</td><td>86.9</td></tr><tr><td>Ours (1:10)</td><td>2.3</td><td>0.202</td><td>94.1</td><td>0.910</td><td>15.7</td><td>0.183</td><td>91.8</td></tr><tr><td>Ours (2:10)</td><td>4.9</td><td>0.241</td><td>93.9</td><td>0.911</td><td>16.0</td><td>0.188</td><td>89.0</td></tr><tr><td>Ours (10:10)</td><td>0.8</td><td>0.101</td><td>94.1</td><td>0.909</td><td>15.1</td><td>0.175</td><td>93.2</td></tr><tr><td>Qwen2.5-VL-7B†</td><td>-</td><td>-</td><td>90.0</td><td>0.868</td><td>12.5</td><td>0.129</td><td>-</td></tr><tr><td>LLaVA-1.5-7B†</td><td>-</td><td>-</td><td>95.3</td><td>0.775</td><td>30.2</td><td>0.355</td><td>-</td></tr><tr><td>Gemma-4-12B</td><td>42.9</td><td>0.434</td><td>88.2</td><td>0.880</td><td>12.2</td><td>0.123</td><td>45.4</td></tr></table>

[OCR table id=tbl-3.html; page=8]
<table><tr><td></td><td>MMStar</td><td>POPE</td><td>MMMU</td><td>MMMU-Pro</td></tr><tr><td>Base</td><td>66.4</td><td>88.0</td><td>55.1</td><td>39.4</td></tr><tr><td>SFT</td><td>63.6</td><td>88.5</td><td>56.5</td><td>40.8</td></tr><tr><td>LocPos</td><td>64.4</td><td>87.2</td><td>54.4</td><td>41.0</td></tr><tr><td>Ours (1:10)</td><td>65.4</td><td>88.6</td><td>56.0</td><td>41.0</td></tr><tr><td>Ours (2:10)</td><td>65.0</td><td>89.3</td><td>54.1</td><td>38.6</td></tr><tr><td>Ours (10:10)</td><td>63.8</td><td>88.5</td><td>56.2</td><td>39.2</td></tr></table>

## A-page-0009

target PDF page 9

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

## 6 RELATED WORK

Visual hallucination. Existing benchmarks such as CHAIR (Rohrbach et al., 2018), POPE (Li et al., 2023), ROPE (Chen et al., 2024b), and HallusionBench (Guan et al., 2024) measure different forms of mismatch between visual evidence and generated claims, and methods address such errors through instruction data (Liu et al., 2024a), preference alignment (Sun et al., 2024), or decoding (Leng et al., 2024; Huang et al., 2024). Other studies expose limits of visual representations (Tong et al., 2024), elementary perception (Rahmanzadehgervi et al., 2024), and spatial relations (Kamath et al., 2023). Recently, Asadi et al. (2026) show the illusion even in frontier models where models describe images they were never given. [NAME C10] turns this observation into a quantitative measure, while [NAME C10] targets the underlying capability: knowing what visual input is available before reasoning about what it contains.

Self-supervised methods to mitigate hallucination. Context prediction (Doersch et al., 2015), jigsaw puzzles (Noroozi & Favaro, 2016), rotation prediction (Gidaris et al., 2018), and masked reconstruction (He et al., 2022) derive supervision from transformations of the input image. Recent multimodal post-training methods, such as Visual Jigsaw (Wu et al., 2026) and SSL-R1 (Xie et al., 2026), extend this paradigm to language-model outputs and verifiable rewards. [NAME C10] shares their annotation-free construction, but differs in asking the model to localize its available visual input within the coordinate frame of the original image. As a result, the task is solved through positional information rather than semantic cues from the image content.

## 7 LIMITATIONS

Our work has several limitations. First, our study focuses primarily on a single model family. The current implementation of [NAME C10] requires a variable visual-token grid and access to absolute positional information, so architectures that encode geometry differently may require alternative task designs. Second, [NAME C10] replaces visual features with a constant embedding, which is far from the distribution of natural images. As a result, awareness of missing visual input does not necessarily imply faithful grounding on challenging real images. Finally, visual hallucination may arise at the Look, Perceive, and Understand levels, and developing methods that jointly address failures across all three levels remains an open problem.

## 8 CONCLUSION

We study visual hallucination from a more fundamental perspective by asking whether a VLM is aware of the visual input available to it before reasoning about what that input contains. To structure this question, we introduce a three-level hierarchy of visual grounding—Look, Perceive, and Understand—and focus on the first level, which remains largely untested by existing benchmarks. We propose the self-supervised [NAME C10] task, where a model must localize its available visual region using positional information while the excluded image content is never encoded. Our experiments show that pretrained VLMs struggle with this task, whereas fine-tuning on automatically generated [NAME C10] data substantially improves visual awareness with little effect on general VLM performance. We further introduce [NAME C10] to test whether a model recognizes when visual evidence is absent. On [NAME C10], standard instruction tuning increases the no-image false-Yes rate to 31.2%, while [NAME C10] fine-tuning reduces it to 0.8% without degrading real-image performance. These results suggest that visual hallucination can arise as early as the Look level and that explicitly training visual-input awareness provides a simple, annotation-free way to improve visual grounding before semantic perception and reasoning begin.

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

## REPRODUCIBILITY STATEMENT

Sec. 3 specifies the [NAME C10] construction and the positional restoration, Sec. 4 the [NAME C10] construction and scoring, and Sec. 5.1 the training and evaluation protocol. App. A gives the instruction mixture and training recipe, App. E the prompts, and App. F the implementation checks. Accompanying scripts rebuild every table and figure from saved predictions without model inference and record hashes of their inputs.

## ETHICS STATEMENT

The study uses existing research datasets and collects no new human-subject data. Images may depict identifiable people; any release must respect the source datasets' access and licensing terms. Improved awareness of visual input does not guarantee factual or safe outputs, and the models should not be described as having human-like awareness.

## AI ASSISTANCE DISCLOSURE

AI tools assisted with manuscript editing, analysis-code preparation, and figure layout.

## REFERENCES

Mohammad Asadi, Jack W. O'Sullivan, Fang Cao, Tahoura Nedaee, Kamyar Rajabalifardi, Fei-Fei Li, Ehsan Adeli, and Euan Ashley. MIRAGE: The illusion of visual understanding. arXiv preprint arXiv:2603.21687, 2026.

Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, et al. Qwen2.5-VL technical report. arXiv preprint arXiv:2502.13923, 2025.

Lin Chen, Jinsong Li, Xiaoyi Dong, Pan Zhang, Yuhang Zang, Zehui Chen, Haodong Duan, Jiaqi Wang, Yu Qiao, Dahua Lin, and Feng Zhao. Are we on the right way for evaluating large vision-language models? In Advances in Neural Information Processing Systems, volume 37, 2024a.

Xuweiyi Chen, Ziqiao Ma, Xuejun Zhang, Sihan Xu, Shengyi Qian, Jianing Yang, David F. Fouhey, and Joyce Y. Chai. Multi-object hallucination in vision language models. In Advances in Neural Information Processing Systems, volume 37, 2024b.

Carl Doersch, Abhinav Gupta, and Alexei A. Efros. Unsupervised visual representation learning by context prediction. In Proceedings of the IEEE International Conference on Computer Vision, pp. 1422–1430, 2015.

Haodong Duan, Junming Yang, Yuxuan Qiao, Xinyu Fang, Lin Chen, Yuan Liu, Xiaoyi Dong, Yuhang Zang, Pan Zhang, Jiaqi Wang, Dahua Lin, and Kai Chen. VLMEvalKit: An open-source toolkit for evaluating large multi-modality models. In Proceedings of the 32nd ACM International Conference on Multimedia, pp. 11198–11201, 2024.

Gemma Team. Gemma 4 technical report. arXiv preprint arXiv:2607.02770, 2026.

Spyros Gidaris, Praveer Singh, and Nikos Komodakis. Unsupervised representation learning by predicting image rotations. In International Conference on Learning Representations, 2018.

Yash Goyal, Tejas Khot, Douglas Summers-Stay, Dhruv Batra, and Devi Parikh. Making the V in VQA matter: Elevating the role of image understanding in visual question answering. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 6904–6913, 2017.

Tianrui Guan, Fuxiao Liu, Xiyang Wu, Ruiqi Xian, Zongxia Li, Xiaoyu Liu, Xijun Wang, Lichang Chen, Furong Huang, Yaser Yacoob, Dinesh Manocha, and Tianyi Zhou. HallusionBench: An advanced diagnostic suite for entangled language hallucination and visual illusion in large vision-language models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 14375–14385, 2024.

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

Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, and Ross Girshick. Masked autoencoders are scalable vision learners. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 16000–16009, 2022.

Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. LoRA: Low-rank adaptation of large language models. In International Conference on Learning Representations, 2022.

Qidong Huang, Xiaoyi Dong, Pan Zhang, Bin Wang, Conghui He, Jiaqi Wang, Dahua Lin, Weiming Zhang, and Nenghai Yu. OPERA: Alleviating hallucination in multi-modal large language models via over-trust penalty and retrospection-allocation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 13418–13427, 2024.

Amita Kamath, Jack Hessel, and Kai-Wei Chang. What's "up" with vision-language models? investigating their struggle with spatial reasoning. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pp. 9161–9175, 2023.

Mehran Kazemi, Hamidreza Alvari, Ankit Anand, Jialin Wu, Xi Chen, and Radu Soricut. GeomVerse: A systematic evaluation of large models for geometric reasoning. arXiv preprint arXiv:2312.12241, 2023.

Sicong Leng, Hang Zhang, Guanzheng Chen, Xin Li, Shijian Lu, Chunyan Miao, and Lidong Bing. Mitigating object hallucinations in large vision-language models through visual contrastive decoding. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 13872–13882, 2024.

Yifan Li, Yifan Du, Kun Zhou, Jinpeng Wang, Wayne Xin Zhao, and Ji-Rong Wen. Evaluating object hallucination in large vision-language models. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pp. 292–305, 2023.

Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, and C. Lawrence Zitnick. Microsoft COCO: Common objects in context. In European Conference on Computer Vision, pp. 740–755, 2014.

Fuxiao Liu, Kevin Lin, Linjie Li, Jianfeng Wang, Yaser Yacoob, and Lijuan Wang. Mitigating hallucination in large multi-modal models via robust instruction tuning. In International Conference on Learning Representations, 2024a.

Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction tuning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2024b.

Pan Lu, Swaroop Mishra, Tanglin Xia, Liang Qiu, Kai-Wei Chang, Song-Chun Zhu, Oyvind Tafjord, Peter Clark, and Ashwin Kalyan. Learn to explain: Multimodal reasoning via thought chains for science question answering. In Advances in Neural Information Processing Systems, volume 35, pp. 2507–2521, 2022.

Ahmed Masry, Do Xuan Long, Jia Qing Tan, Shafiq Joty, and Enamul Hoque. ChartQA: A benchmark for question answering about charts with visual and logical reasoning. In Findings of the Association for Computational Linguistics: ACL 2022, pp. 2263–2279, 2022.

Mehdi Noroozi and Paolo Favaro. Unsupervised learning of visual representations by solving jigsaw puzzles. In European Conference on Computer Vision, pp. 69–84, 2016.

Qwen Team. Qwen3-VL technical report. arXiv preprint arXiv:2511.21631, 2025.

Pooyan Rahmanzadehgervi, Logan Bolton, Mohammad Reza Taesiri, and Anh Totti Nguyen. Vision language models are blind. In Proceedings of the Asian Conference on Computer Vision, pp. 18–34, 2024.

Anna Rohrbach, Lisa Anne Hendricks, Kaylee Burns, Trevor Darrell, and Kate Saenko. Object hallucination in image captioning. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, pp. 4035–4045, 2018.

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

Dustin Schwenk, Apoorv Khandelwal, Christopher Clark, Kenneth Marino, and Roozbeh Mottaghi. A-OKVQA: A benchmark for visual question answering using world knowledge. In European Conference on Computer Vision, pp. 146–162, 2022.

Oleksii Sidorov, Ronghang Hu, Marcus Rohrbach, and Amanpreet Singh. TextCaps: A dataset for image captioning with reading comprehension. In European Conference on Computer Vision, pp. 742–758, 2020.

Amanpreet Singh, Vivek Natarajan, Meet Shah, Yu Jiang, Xinlei Chen, Dhruv Batra, Devi Parikh, and Marcus Rohrbach. Towards VQA models that can read. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 8317–8326, 2019.

Jianlin Su, Murtadha Ahmed, Yu Lu, Shengfeng Pan, Wen Bo, and Yunfeng Liu. RoFormer: Enhanced transformer with rotary position embedding. Neurocomputing, 568:127063, 2024.

Zhiqing Sun, Sheng Shen, Shengcao Cao, Haotian Liu, Chunyuan Li, Yikang Shen, Chuang Gan, Liang-Yan Gui, Yu-Xiong Wang, Yiming Yang, Kurt Keutzer, and Trevor Darrell. Aligning large multimodal models with factually augmented RLHF. In Findings of the Association for Computational Linguistics: ACL 2024, pp. 13088–13110, 2024.

Shengbang Tong, Zhuang Liu, Yuexiang Zhai, Yi Ma, Yann LeCun, and Saining Xie. Eyes wide shut? exploring the visual shortcomings of multimodal LLMs. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 9568–9578, 2024.

Penghao Wu, Yushan Zhang, Haiwen Diao, Bo Li, Lewei Lu, and Ziwei Liu. Visual jigsaw post-training improves mllms. In International Conference on Learning Representations, 2026.

Jiahao Xie, Alessio Tonioni, Nathalie Rauschmayr, Federico Tombari, and Bernt Schiele. SSL-R1: Self-supervised visual reinforcement post-training for multimodal large language models. arXiv preprint arXiv:2604.20705, 2026.

Licheng Yu, Patrick Poirson, Shan Yang, Alexander C. Berg, and Tamara L. Berg. Modeling context in referring expressions. In European Conference on Computer Vision, pp. 69–85, 2016.

Xiang Yue, Yuansheng Ni, Kai Zhang, Tianyu Zheng, Ruoqi Liu, Ge Zhang, Samuel Stevens, Dongfu Jiang, Weiming Ren, Yuxuan Sun, et al. MMMU: A massive multi-discipline multimodal understanding and reasoning benchmark for expert AGI. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 9556–9567, 2024.

Xiang Yue, Tianyu Zheng, Yuansheng Ni, Yubo Wang, Kai Zhang, Shengbang Tong, Yuxuan Sun, Botao Yu, Ge Zhang, Huan Sun, Yu Su, Wenhu Chen, and Graham Neubig. MMMU-Pro: A more robust multi-discipline multimodal understanding benchmark. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 2025.

Yuze Zhao, Jintao Huang, Jinghan Hu, Xingjun Wang, Yunlin Mao, Daoze Zhang, Zeyinzi Jiang, Zhikai Wu, Baole Ai, Ang Wang, Wenmeng Zhou, and Yingda Chen. SWIFT: A scalable lightweight infrastructure for fine-tuning. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 39, pp. 29733–29735, 2025.

Yuke Zhu, Oliver Groth, Michael Bernstein, and Li Fei-Fei. Visual7W: Grounded question answering in images. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 4995–5004, 2016.

## A-page-0013

target PDF page 13

# A TRAINING DATA AND IMPLEMENTATION DETAILS

Table A1: The instruction mixture replay datasets. [NAME C10] examples reuse its image pool.

[tbl-4.html](tbl-4.html)

We train in bfloat16 using scaled dot-product attention and apply LoRA to all linear layers with rank 16 and α = 32, while keeping the vision encoder and projector frozen. We use a per-device batch size of 1 with 8 gradient-accumulation steps across four GPUs, giving an effective batch size of 32. Training runs for two epochs with a learning rate of 10⁻⁴, a warmup ratio of 0.05, a maximum sequence length of 4096, and a maximum image area of 1,003,520 pixels. We reserve 1% of the combined training examples for validation.

# B IMPLEMENTATION OF THE [NAME C10] TASK

Sampling the window. The processor resizes image I to a canonical canvas of R_w × R_h pixels. For patch size p and spatial merge factor m, each visual token corresponds to a merge block of side c = pm, so the canvas contains B_w = R_w/c by B_h = R_h/c blocks. We sample a rectangle w = (b_x₀, b_y₀, b_x₁, b_y₁) on this block grid, with sides between 15% and 80% of the canvas, and serialize the target in the integer coordinate convention of Qwen3-VL:

$$y(w) = 1000 \left( \frac{b_{x_0}}{B_w}, \frac{b_{y_0}}{B_h}, \frac{b_{x_1}}{B_w}, \frac{b_{y_1}}{B_h} \right). \tag{4}$$

Because each window is aligned with the visual-token grid, every token lies entirely inside or outside the selected region, making the target box exact up to coordinate rounding. We resize the full image before cropping and disable any subsequent resizing, so each crop patch is pixel-identical to the corresponding patch in the full image. The resulting crop features nevertheless differ from their full-image counterparts because the excluded patches do not participate in vision-encoder attention. We discard crops smaller than four merge blocks, which would otherwise be upsampled by the image loader. This removes 264 of the 46,000 generated training examples.

Restoring global positions. We override the three positional pathways through input arguments and forward hooks, without introducing new parameters or modifying the attention computation.

(1) Vision absolute positions. Qwen3-VL interpolates a learned positional table to the current patch grid. We compute the interpolation indices and weights on the full-image grid and then select the entries corresponding to the crop patches.
(2) Vision rotary positions. We offset the crop's two-dimensional patch indices by (mb_y₀, mb_x₀). Because a shared translation cancels in the rotary query-key inner product (Su et al., 2024), this pathway does not by itself encode absolute location. We nevertheless restore it for consistency.
(3) Language-model positions. We shift the height and width components of the image tokens' multimodal rotary positions by (b_y₀, b_x₀), thereby preserving their spatial placement relative to the text tokens.

In a controlled comparison, overriding the vision absolute positions changes the vision-encoder output by a relative L₂ distance of 0.676, compared with only 0.033 for the rotary-position override. On Qwen2.5-VL (Bai et al., 2025), whose vision encoder uses only rotary positional encoding, restoring the crop positions leaves the output unchanged. This further motivates our requirement for an absolute positional signal in the [NAME C10] task.

648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701

[OCR table id=tbl-4.html; page=13]
<table><tr><td>Dataset</td><td>Rows</td><td>Task</td></tr><tr><td>VQAv2 (Goyal et al., 2017)</td><td>12,000</td><td>Visual question answering</td></tr><tr><td>TextVQA (Singh et al., 2019)</td><td>6,000</td><td>Text reading and question answering</td></tr><tr><td>Visual7W (Zhu et al., 2016)</td><td>6,000</td><td>Grounded question answering</td></tr><tr><td>A-OKVQA (Schwenk et al., 2022)</td><td>5,000</td><td>Knowledge-based question answering</td></tr><tr><td>ChartQA (Masry et al., 2022)</td><td>5,000</td><td>Chart reasoning</td></tr><tr><td>TextCaps (Sidorov et al., 2020)</td><td>4,000</td><td>Captioning with text</td></tr><tr><td>ScienceQA (Lu et al., 2022)</td><td>4,000</td><td>Science question answering</td></tr><tr><td>GeomVerse (Kazemi et al., 2023)</td><td>4,000</td><td>Geometric reasoning</td></tr><tr><td>Total</td><td>46,000</td><td></td></tr></table>

## A-page-0014

target PDF page 14

702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755

## C [NAME C10] DETAILS

We use the prompt “Does this image contain: {expression}? Answer with Yes or No.”, inserting the raw RefCOCO expression. Images are resized to the model’s canonical geometry, consistent with our other evaluations. In the no-image condition, the image is still loaded so that the number of visual tokens matches the real-image input, but the vision encoder is bypassed. The feature function instead returns the \(<|image\_pad|>\) embedding at every visual-token position together with all-zero DeepStack features. For the wrong-image condition, we sort items by image and pair each item with the expression from the item halfway around the list, skipping pairs that originate from the same image. The sets \(\mathcal{Y}\) and \(\mathcal{N}\) include all vocabulary tokens whose decoded surface forms, after removing surrounding whitespace and ignoring case, are “yes” and “no”, respectively. The two sets are disjoint by construction. Each model is evaluated with one forward pass per item and condition, for a total of 32,256 forward passes per model.

## D EVALUATION DETAILS

Protocol. MMStar (Chen et al., 2024a), POPE (Li et al., 2023), and MMMU-Pro (Yue et al., 2025) are capped at 500 items; MMMU (Yue et al., 2024) reports the 425 validation items within its cap. The harness is VLMEvalKit (Duan et al., 2024), and POPE reports F1.

Answer extraction. Without an LLM judge, the evaluation harness marks a multiple-choice response as incorrect whenever its answer-extraction rule fails, which disproportionately penalizes verbose outputs. Under the default extraction, the pretrained model obtains an MMMU score of only 0.089, largely because its chain-of-thought responses are not successfully parsed. We therefore re-score all saved outputs using the same fixed sequence of extraction rules for every model: the last explicit answer phrase, a bolded option letter, the harness's option rule applied to the final non-empty line, and a unique match to an option string within the final 300 characters. Responses that remain unresolved are counted as incorrect. For open-ended questions, we match the normalized final answer exactly or as a substring, using a \(1\%\) relative tolerance for numerical answers. With this corrected scoring procedure, the pretrained model's MMMU score increases to 0.551. This change reflects improved answer extraction rather than any modification to the model or its outputs.

## E PROMPT INVENTORY

The evaluation cycles through 11 groups and samples one prompt within each group. Every prompt contains a format cue and asks for the visible region, not a description of its content. The inventory below is copied from the evaluation code.

[tbl-5.html](tbl-5.html)

[OCR table id=tbl-5.html; page=14]
<table><tr><td>Group</td><td>Prompt</td></tr><tr><td>see</td><td>Which region of the full image can you see? Answer with a bounding box.What part of the image is visible to you? Give a bounding box.Identify the area you are able to see; respond with a bounding box.Report the visible region as a bounding box.</td></tr><tr><td>look</td><td>Where in the full image are you looking? Answer with a bounding box.Which region are you looking at? Reply with box coordinates.Point out the region you are looking at, as a bounding box.Give the bounding box of the area you are currently looking at.</td></tr><tr><td>observe</td><td>Which part of the image are you observing? Answer with a bounding box.Mark the region you can observe; return a bounding box.What area is under your observation? Provide a bounding box.</td></tr><tr><td>perceive</td><td>Which region of the scene do you perceive? Answer with a bounding box.Delimit the portion of the image you perceive, in bounding-box form.</td></tr></table>

## A-page-0015

target PDF page 15

756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809

[tbl-6.html](tbl-6.html)

## F VERIFYING THE POSITIONAL RESTORATION

We validate positional restoration independently of downstream performance. Translating the crop patch indices by the grid offset must exactly reproduce the corresponding rows of the full-image position indices. The same row mapping is used to select the absolute interpolation entries, so any indexing error affects both pathways and is detected by this check. We additionally use a painted-patch test to verify the processor's merge-block-major flattening order. After canonical resizing, cropping must leave the retained patch inputs unchanged, and the loader must not upsample the crop. During training, crop offsets must also survive the full dataset-loading pipeline. We therefore log the first active positional-override calls to detect any silent loss of these offsets.

The output parser supports both plain-text bounding boxes and the model's special-token box format. For all model comparisons, we verify that images, prompts, and target windows are identical, recompute IoU directly from the predicted coordinates, and record SHA-256 hashes for every input file. All permutation tests use fixed random seeds.

[OCR table id=tbl-6.html; page=15]
<table><tr><td>Group</td><td>Prompt</td></tr><tr><td rowspan="4">view</td><td>State, as a bounding box, the region you can perceive.</td></tr><tr><td>What is your field of view within the full image? Answer with a bounding box.</td></tr><tr><td>Which region falls inside your view? Express it as a bounding box.</td></tr><tr><td>Give the bounding box of your viewport.</td></tr><tr><td rowspan="3">examine</td><td>Which rectangle of the original image are you viewing? Answer with its bounding box.</td></tr><tr><td>Which region are you able to examine? Answer with a bounding box.</td></tr><tr><td>Give the bounding box of the area you can inspect.</td></tr><tr><td rowspan="3">discern</td><td>Which part of the image can you discern? Answer with a bounding box.</td></tr><tr><td>What region can you make out? Give its bounding box.</td></tr><tr><td>Which area do you notice? Answer with a bounding box.</td></tr><tr><td rowspan="3">access</td><td>Which portion of the image can you glimpse? Provide a bounding box.</td></tr><tr><td>Which region of the image is accessible to you? Answer with a bounding box.</td></tr><tr><td>What portion of the image is available to you? Give a bounding box.</td></tr><tr><td rowspan="4">origin</td><td>This is part of a larger image. Where does it come from? Answer with a bounding box.</td></tr><tr><td>Locate this view within the full image; return a bounding box.</td></tr><tr><td>Where is this region situated in the original image? Answer with box coordinates.</td></tr><tr><td>Return the bounding box of this view in the full image.</td></tr><tr><td rowspan="2">occlusion</td><td>Everything outside one rectangle is hidden from you. Which rectangle is not? Answer with a bounding box.</td></tr><tr><td>Only one region of the image reaches you. Which one? Give its bounding box.</td></tr><tr><td rowspan="4">terse</td><td>Visible region (bounding box):</td></tr><tr><td>Your viewport, as a bounding box.</td></tr><tr><td>Looking at (bounding box):</td></tr><tr><td>Seen region, as a box:</td></tr></table>
