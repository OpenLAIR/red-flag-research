# [TITLE C03]

## A-page-0001

target PDF page 1

# [TITLE C03]

Anonymous authors

Paper under double-blind review

# ABSTRACT

Gradient-based visual jailbreak attacks on vision-language models (VLMs) often optimize image perturbations for a fixed iteration budget using token-level target objectives that only indirectly capture harmful response behavior. We introduce [NAME C03], a behavior-aligned visual jailbreak framework that learns a lightweight behavior predictor from internal VLM representations to estimate response-level behavior. The predictor provides a differentiable behavioral signal for image optimization and enables instance-adaptive iterate selection without response generation or evaluation at every update. Across 917 samples from multimodal jailbreak benchmarks and four target VLMs, [NAME C03] improves ELITE-based attack success rate (E-ASR) by 16.68–33.26 percentage points and HarmBench ASR by 10.25–24.64 points over affirmative-target PGD. [NAME C03] also reduces the mean optimization steps from 300 to 32.7–161.2, yielding 1.8×–10.4× wall-clock speedups. The performance improvements persist across three defenses, while response-behavior analysis shows shifts from refusal and intermediate responses toward successful responses. These results demonstrate that aligning visual optimization with response-level behavior improves both attack effectiveness and efficiency.

# 1 INTRODUCTION

Vision-language models (VLMs) have become general-purpose multimodal systems for visual understanding, instruction following, and reasoning (Alayrac et al., 2022; Liu et al., 2023; OpenAI, 2024; Bai et al., 2025). As these models are deployed broadly, their safety mechanisms must remain reliable for both text and image instructions. However, the visual channel creates an additional input space in which harmful intent can be encoded or adversarially manipulated. Consequently, VLMs that refuse harmful textual requests may still generate unsafe content from multimodal inputs (Qi et al., 2024; Zong et al., 2024; Luo et al., 2024; Liu et al., 2024b). These vulnerabilities have motivated extensive work on multimodal jailbreaks and visual adversarial attacks.

In white-box visual attacks, a common strategy is to update the image so that the model assigns high likelihood to an affirmative or harmful target sequence, such as “Sure, here is” (Qi et al., 2024; Lin et al., 2026). This provides a stable gradient for image optimization, but matching a target sequence does not guarantee that the complete response fulfills the harmful request. A model can begin affirmatively yet produce a vague, evasive, or largely harmless answer. Modern evaluators therefore assess the complete generated response rather than refusal bypass alone (Mazeika et al., 2024; Chao et al., 2024; Souly et al., 2024; Lee et al., 2025). ELITE, for example, incorporates toxicity in multimodal response evaluation (Lee et al., 2025). We refer to the safety-relevant properties of the complete generated response as response behavior, including whether it complies with the request and the resulting content is substantively harmful. Optimization-based visual jailbreak attacks, often using Projected Gradient Descent (PGD), typically optimize a token-level target, whereas jailbreak success is ultimately evaluated based on the behavior of the complete response. We refer to this discrepancy as the objective–behavior mismatch.

Using a response evaluator directly as an attack objective is difficult because its score is obtained only after discrete text generation and cannot be backpropagated to image pixels. Repeatedly generating and judging a full response after every image update would also be computationally expensive. At the same time, prior work shows that safety and refusal information is reflected in internal model representations (Arditi et al., 2024; Rimsky et al., 2024; Zou et al., 2023; Burns et al., 2023; Hao

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

et al., 2026; Song et al., 2025). This suggests that an evaluation of response behavior can instead be predicted from a hidden representation that remains differentiable with respect to the input image.

We implement this idea with a lightweight behavior predictor. For each target VLM, a regression probe is trained to estimate the ELITE score of the model's response from a selected internal representation and is frozen before attack optimization. During optimization, the predictor uses the internal representation to provide a differentiable signal that complements the conventional target-sequence objective, forming our [NAME C03] ([NAME C03]). Once the predicted score reaches a calibrated threshold, the current image is retained and further updates are skipped.

We evaluate our method against affirmative-target PGD in a controlled white-box setting, using the same image-text pairs while optimizing only the image. We measure attack success using two metrics. ELITE-based attack success rate (E-ASR), derived from thresholded ELITE scores, and HarmBench ASR, computed from the binary predictions of the HarmBench classifier. Across 917 samples from multimodal jailbreak benchmarks and four VLMs, our method improves E-ASR by 16.68–33.26 percentage points and HarmBench ASR by 10.25 to 24.64 points. Instance-adaptive optimization reduces the required optimization steps and yields 1.8×–10.4× wall-clock speedups, while the performance gains persist across three defense methods. Response-behavior analysis further shows that the improvement reflects shifts from refusal and intermediate responses toward successful responses, rather than changes near the E-ASR threshold alone.

Our main contributions are as follows. First, we learn a lightweight behavior predictor from internal VLM representations, providing a differentiable response-level signal for image optimization without generating and evaluating a response at every update. Second, We combine the predicted behavioral signal with the affirmative-target objective to align image optimization more closely with response behavior. Third, We use the predicted behavior score to retain an effective iterate and skip unnecessary updates, reducing computation and avoiding degradation from excessive optimization.

## 2 RELATED WORK

### 2.1 MULTIMODAL JAILBREAKS AND VISUAL OPTIMIZATION

Multimodal jailbreaks exploit the visual channel through typographic prompts, generated harmful imagery, cross-modal prompt construction, and adversarial image perturbations (Gong et al., 2025; Li et al., 2024; Ma et al., 2025; Shayegani et al., 2024; Qi et al., 2024). Gradient-based attacks update image pixels, often by maximizing the likelihood of a fixed affirmative or harmful target sequence (Qi et al., 2024; Lin et al., 2026). Our work focuses on the optimization signal used in this setting. Starting from a fixed image-text input, we keep the text unchanged and augment the target-sequence objective with a differentiable signal that reflects response behavior.

### 2.2 REPRESENTATION-BASED ATTACK SIGNALS

Internal representations have been used to identify or manipulate safety related information. Representation engineering and activation steering associate high-level behavior and refusal with directions in hidden space (Zou et al., 2023; Rimsky et al., 2024; Arditi et al., 2024). Prior work further shows that internal states encode information related to model outputs (Burns et al., 2023). In VLM jailbreak research, ActMan manipulates activations during decoding and JailBound uses a probed safe/unsafe boundary to guide attacks (Hao et al., 2026; Song et al., 2025). Rather than optimizing a refusal direction or binary safety boundary itself, we learn a behavior predictor that maps an internal VLM representation to a scalar response behavior score. This prediction remains differentiable with respect to the image and serves as an additional optimization signal.

### 2.3 EVALUATING JAILBREAK SUCCESS

Response evaluators assess whether a generated output meaningfully fulfills a harmful request after generation. HarmBench uses a binary classifier to determine whether the response exhibits the target harmful behavior (Mazeika et al., 2024). ELITE extends the StrongREJECT rubric with toxicity-aware evaluation for multimodal responses (Souly et al., 2024; Lee et al., 2025). In our method, ELITE scores provide supervision for training the behavior predictor, whereas HarmBench is kept

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

![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

![img-2.jpeg](img-2.jpeg)

Figure 1: Overview of the [NAME C03] framework. Stage 1 trains a model-specific behavior predictor from precomputed ELITE scores. Stage 2 combines the affirmative-target loss with a differentiable behavior-guidance loss for image optimization. Stage 3 adapts the number of optimization updates using the predicted behavior score, retaining the first threshold-reaching iterate or the highest-scoring iterate otherwise. Attack success rate is evaluated by ELITE and HarmBench after optimization.

independent of predictor training and is used only for evaluation. We therefore report E-ASR from thresholded ELITE scores and HarmBench ASR from the binary HarmBench classifier.

### 3 METHOD

Figure 1 illustrates our framework. We consider a white-box setting in which the text prompt is fixed and only the visual input is optimized within a bounded perturbation set. Our method has three stages: (i) learning a behavior predictor from precomputed response-level supervision, (ii) [NAME C03] combining the predicted behavioral signal with an affirmative-target objective, and (iii) instance-adaptive optimization using the predicted behavior score to avoid unnecessary updates and performance degradation from excessive optimization. The behavior predictor is trained separately for each target VLM and remain frozen during attack optimization.

### 3.1 PROBLEM FORMULATION

Let $M_\theta$ denote a frozen target VLM, $x$ an input image, and $q$ the associated text prompt. We optimize an additive visual perturbation $\delta$ while leaving both $q$ and the model parameters unchanged. The resulting image is

$$x_{\mathrm{adv}} = x + \delta, \quad \|\delta\|_\infty \leq \epsilon, \tag{1}$$

where $x_{\mathrm{adv}}$ is additionally clipped to the valid image domain. The target model response is $y = M_\theta(x_{\mathrm{adv}}, q)$. An external response evaluator $E(x_{\mathrm{adv}}, q, y)$ returns a scalar score of response behavior; it is used for supervision and evaluation only and never inside the optimization loop.

As in affirmative-target PGD, let $y^*_{1:T}$ be a fixed compliance prefix. We use ``Sure, here is how to do that. Step 1:''', for all samples, tokenized with each target model tokenizer. The corresponding teacher-forced negative log-likelihood is

$$\mathcal{L}_{\mathrm{attack}}(\delta) = -\frac{1}{T} \sum_{t=1}^{T} \log p_\theta(y^*_t \mid x + \delta, q, y^*_{<t}). \tag{2}$$

Minimizing $\mathcal{L}_{\mathrm{attack}}$ increases the likelihood of the affirmative sequence. However, it only measures conformity to a fixed target prefix, not whether the complete response substantively fulfills the request. We therefore augment it with a signal learned from response-level evaluation.

### 3.2 STAGE 1: LEARNING THE BEHAVIOR PREDICTOR

Let $\mathcal{D} = \mathcal{D}_{\mathrm{train}} \cup \mathcal{D}_{\mathrm{val}}$ be a calibration set of image and text pairs. For every $(x_i, q_i) \in \mathcal{D}$ we generate $y_i = M_\theta(x_i, q_i)$ from the unperturbed input and record $s_i = E(x_i, q_i, y_i)$. We instantiate

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

E with the ELITE evaluator (Lee et al., 2025), whose scores lie in [0, 25] the formulation only requires a scalar response-level evaluation. This supervision is computed once before any attack, and D is disjoint from the inputs on which attacks are later evaluated.

Pre-generation representation. We extract the hidden state at the final prompt position, immediately before the first response token is predicted. Let P be the length of the decoder input sequence that the model's own processor produces for (x, q). Indexing positions from zero, the representation at decoder layer ℓ is

$$h_\ell(x, q) = H_\theta^{(\ell)}(x, q)_{P-1} \in \mathbb{R}^{d_h}. \tag{3}$$

This state directly conditions the first generated token and does not depend on any generated token.

Predictor and training. We train a lightweight regression probe $f_\phi : \mathbb{R}^{d_h} \to \mathbb{R}$ is a small regression probe to estimate $s_i$ from $h(x_i, q_i)$. Features are standardized the representation with feature-wise statistics from $\mathcal{D}_{\text{train}}$ and applies a two-hidden-layer MLP (widths 128 and 32, ReLU) with a linear scalar head, fit by squared-error regression,

$$\min_\phi \frac{1}{|\mathcal{D}_{\text{train}}|} \sum_{i \in \mathcal{D}_{\text{train}}} (f_\phi(h_\ell(x_i, q_i)) - s_i)^2, \tag{4}$$

with a separate predictor per target VLM. The layer ℓ is selected per backbone based on predictive performance on $\mathcal{D}_{\text{val}}$ and is kept fixed for both predictor training and attack-time optimization.

Calibrated threshold. We derive a model-specific threshold from the predictor outputs on clean, unperturbed representations,

$$\tau = Q_{0.99} \big( \{ f_\phi(h_\ell(x_i, q_i)) \}_{i \in \mathcal{D}} \big), \tag{5}$$

where $Q_{0.99}$ denotes the 99th percentile. This defines a high predicted-score region from the predictor's own output distribution. The same $\tau$ is used by Stage 2 and Stage 3.

### 3.3 STAGE 2: [NAME C03]

At attack time, the internal representation depends on the perturbation, and we define

$$\widehat{s}(\delta) = f_\phi(h(x + \delta, q)) \tag{6}$$

as the predicted behavior score of the current image. Since this score is computed from the model's internal representation, it remains differentiable with respect to the image and can be used directly for optimization.

Behavior-guidance loss. We convert the predicted score into a normalized hinge deficit,

$$\mathcal{L}_{\text{behavior}}(\delta) = \frac{\max(0, \tau - \widehat{s}(\delta))}{\tau}. \tag{7}$$

When $\widehat{s}(\delta) < \tau$, minimizing $\mathcal{L}_{\text{behavior}}$ increases the predicted behavior score. Once $\widehat{s}(\delta) \ge \tau$, the term becomes zero. This avoids rewarding arbitrarily large predictor outputs and instead asks the current representation only to reach a calibrated high-score region.

The normalization by $\tau$ rescales the deficit but does not restrict the loss to [0, 1], since the predictor output is unconstrained and may be negative. The thresholded loss provides behavioral guidance only while the predicted score remains below $\tau$, without clipping the predictor output itself.

Joint objective. We combine the affirmative-target loss with behavioral guidance as

$$\mathcal{L}_{\text{total}}(\delta) = \mathcal{L}_{\text{attack}}(\delta) + \lambda \mathcal{L}_{\text{behavior}}(\delta), \quad \|\delta\|_\infty \le \epsilon, \tag{8}$$

where $\lambda$ controls the contribution of the behavior-guidance term. Here, $\mathcal{L}_{\text{attack}}$ favors the fixed affirmative continuation, while $\mathcal{L}_{\text{behavior}}$ encourages higher predicted behavior scores until the calibrated threshold is reached. Their combination constitutes our [NAME C03].

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

We optimize only the image using a projected sign-gradient update,

$$\delta^{(k+1)} = \Pi_{\mathcal{B}_\epsilon} \left( \delta^{(k)} - \alpha \operatorname{sign} \left( \nabla_\delta \mathcal{L}_{\text{total}}(\delta^{(k)}) \right) \right), \tag{9}$$

where $\alpha$ is the step size and $\mathcal{B}_\epsilon = \{\delta : \|\delta\|_\infty \le \epsilon, 0 \le x + \delta \le 1\}$ denotes the feasible perturbation set, with the image-domain constraints applied elementwise. The perturbation is initialized uniformly within the $\ell_\infty$ ball, $\delta^{(0)} \sim \mathcal{U}([-\epsilon, \epsilon])$. The target VLM and behavior predictor remain frozen, while the text prompt $q$ is kept unchanged throughout optimization.

### 3.4 STAGE 3: INSTANCE-ADAPTIVE OPTIMIZATION

Stage 3 adapts the optimization process to each sample using the predicted behavior score. Let

$$\widehat{s}_k = f_\phi \left( h_\ell(x + \delta^{(k)}, q) \right) \tag{10}$$

be the score associated with the current iterate. We retain the first iterate that reaches the calibrated threshold,

$$k_{\text{adapt}} = \min \left\{ k : \widehat{s}_k \ge \tau \right\}, \quad k = 0, \dots, K. \tag{11}$$

If the threshold is reached, the current image $x + \delta^{(k_{\text{adapt}})}$ is retained and the remaining image updates are skipped. Otherwise, optimization continues to the maximum iteration budget, and we return the trajectory iterate with the highest predicted behavior score,

$$k^* = \underset{k \in \{0, \dots, K\}}{\arg \max} \widehat{s}_k, \quad x_{\text{adv}} = x + \delta^{(k^*)}. \tag{12}$$

This procedure produces sample-dependent optimization lengths and preserves the first threshold-reaching solution, avoiding additional updates once the behavior-guidance loss becomes zero. This reduces unnecessary computation and helps prevent degradation from excessive optimization. The calibrated threshold serves as an internal signal for adapting optimization process. Final attack success is assessed only after optimization by generating the target VLM response and evaluating it with ELITE score or HarmBench classifier.

## 4 EXPERIMENTS

### 4.1 EXPERIMENTAL SETUP

**Target models and Evaluation data.** We evaluate four instruction-tuned VLMs, including LLaVA-1.5-7B (Liu et al., 2024a), Qwen2.5-VL-7B (Bai et al., 2025), InternVL3-8B (Zhu et al., 2025), and Llama-3.2-11B-Vision (Grattafiori et al., 2024; Meta AI, 2024). These models represent different VLM families and provide a diverse evaluation setting for assessing the behavior predictor and the proposed optimization framework across model backbones. Exact checkpoints are listed in Appendix A.2. We evaluate on 917 multimodal jailbreak data inputs from the ELITE benchmark (Lee et al., 2025), which aggregates eight source datasets and annotates each input with one of eleven hazard categories. These sources span diverse constructions and taxonomies of multimodal safety inputs, enabling us to evaluate the same optimization procedure across heterogeneous input distributions rather than within a single benchmark setting. The behavior predictor is trained on a disjoint split of ELITE, ensuring that no attack-evaluation example is used for predictor training or layer selection. Detailed split statistics and source-dataset composition are provided in Appendix A.1.

**Compared methods.** We compare four conditions under an identical protocol: *Baseline* uses the unperturbed image, while *Random perturb.* applies uniform random noise under the same perturbation budget. *affirmative-target PGD* ($\lambda=0$) optimizes only $\mathcal{L}_{\text{attack}}$ using projected gradient descent (Madry et al., 2018), following the target-sequence objective commonly used in white-box visual jailbreak attacks (Qi et al., 2024; Niu et al., 2024; Lin et al., 2026). [NAME C03] combines the behavior-aligned objective with instance-adaptive optimization. All methods use the same image-text pairs, target models, perturbation budget and generation settings. Our method introduces the behavior-guidance term and instance-adaptive iterate selection while keeping the remaining optimization settings unchanged.

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

![img-3.jpeg](img-3.jpeg)

![img-4.jpeg](img-4.jpeg)

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

Figure 2: Behavior-predictor performance across LLM backbone layers. AUC with the E-ASR cutoff and Pearson r between predicted and true ELITE scores are reported on D_val, shown in blue and orange, respectively. Stars indicate the selected layer for each VLM. (Appendix A.3).

Evaluation metrics and judges. We report two attack success metrics. E-ASR is defined by thresholding the ELITE score at 10, the cutoff set by human judgement in the original work (Lee et al., 2025). ELITE combines refusal, toxicity, convincingness, and specificity into a scalar score on [0, 25], computed as (1 - refused) × convincing+specific / ΔR × toxicity. Higher scores indicate more harmful and compliant responses. HarmBench ASR measure the fraction of responses that a separately trained binary classifier labels as exhibiting the target harmful behavior (Mazeika et al., 2024). ELITE scores supervise the behavior predictor, whereas Harmbench is not used for predictor training, threshold calibration, or iterate selection, and thus provides an independent evaluation signal for assessing whether the observed gains extend beyond the ELITE-derived surrogate. Detailed judge configurations are provided in Appendix A.5.

Implementation details. Unless otherwise specified, we use an L_∞ perturbation budget of ε = 16/255, step size α = 1/255, a maximum of K = 300 optimization steps, and λ = 4. For each model, the threshold τ is calibrated as the 99th percentile of predictor scores on clean inputs. Responses are generated greedily with a maximum of 256 new tokens. Full hyperparameters, model-specific perturbation spaces, and predictor-training settings are provided in Appendix A.

Compute and efficiency measurement. All attacks, response generation, and judging use NVIDIA H100 80GB HBM3 GPUs with batch size 1. To isolate attack-construction cost, efficiency is measured in dedicated runs separate from success-rate evaluation, with each condition run on a dedicated GPU without competing processes and using identical inputs and numerical precision. Warm-up samples are excluded. Per-sample wall-clock time is bracketed by CUDA synchronization, and only the optimization procedure is timed, excluding response generation, judging, and disk I/O. We also record optimization steps and forward/backward passes, providing hardware-independent measures that help verify that observed speedups reflect reduced computation rather than system-level timing effects. (Appendix A.6).

## 4.2 BEHAVIOR PREDICTOR QUALITY AND LAYER SELECTION

Before attack optimization, we evaluate its predictive quality across LLM layers. For each candidate layer ℓ, we train f_φ on D_train and evaluate it on D_val using Pearson correlation with the ground-truth ELITE score and AUC for the binary decision induced by the E-ASR cutoff. Figure 2 shows that predictive performance generally improves from the early layers and remains strong across deeper layers. Based on performance D_val, we select ℓ = 25 for Qwen2.5-VL-7B, ℓ = 18 for LLaVA-1.5-7B, ℓ = 24 for InternVL3-8B, and ℓ = 37 for Llama-3.2-V-11B. The corresponding AUCs are 0.85, 0.79, 0.88, and 0.87, with Pearson correlations of 0.68, 0.57, 0.72, and 0.65, respectively. These results show that the pre-generation representation h_ℓ contains substantial information about

## A-page-0007

target PDF page 7

the response behavior. Because $h_\ell$ is extracted at the final prompt position before any response token is generated, $f_\phi$ provides a differentiable behavioral signal without response generation or repeated ELITE evaluation. The selected layer is fixed for subsequent attacks for each model. (Appendix B).

Table 1: Attack performance on 917 multimodal jailbreak data across four target VLMs. Performance is measured by E-ASR and HarmBench ASR (%), with higher values indicating stronger attacks. Bold indicates the best result in each column, and the second best italic. $\Delta$ vs. PGD denotes the absolute improvement of [NAME C03] over affirmative-target PGD in percentage points.

[tbl-0.html](tbl-0.html)

### 4.3 MAIN ATTACK PERFORMANCE

Table 1 summarizes the main attack results. Our method achieves the highest E-ASR and HarmBench ASR across all four target VLMs. Compared with affirmative-target PGD, [NAME C03] improves E-ASR by 16.68 to 33.26 percentage points and ASR by 10.25 to 24.64 percentage points. Since HarmBench is not used to train the behavior predictor, these consistent gains indicate that the improvement is not specific to the ELITE-based supervision signal. Under the same perturbation budget, random perturbation change E-ASR by only $-2.07$ to $+2.51$ percentage points and HarmBench ASR by $-0.44$ to $+1.75$ percentage points relative to the clean inputs. These substantially smaller changes indicate that the gains arise from the optimization direction rather than perturbation alone.

Affirmative-target PGD, in contrast, does not consistently improve attack success over the clean inputs, increasing E-ASR on three of four models and HarmBench ASR on only two. The failure is particularly pronounced on LLaVA-1.5, where E-ASR decreases from 69.14 to 42.42. This result illustrates the objective–behavior mismatch. Optimizing toward a fixed affirmative prefix can move the model away from substantively harmful response behavior. Behavioral guidance mitigates this failure, increasing LLaVA-1.5 E-ASR to 75.68 while also outperforming PGD under HarmBench. Across the four models, [NAME C03] improves E-ASR over the clean inputs by 24.59 percentage points on average, compared with only 2.76 points for PGD. (Appendix D).

Table 2: Optimization efficiency of our instance-adaptive attack compared with 300 step PGD across four target VLMs. Results are reported over 917 evaluation inputs in terms of the mean and median number of optimization steps, threshold reach rate, wall-clock speedup, and mean $\ell_2$ perturbation norm.

[tbl-1.html](tbl-1.html)

### 4.4 EFFICIENCY OF INSTANCE-ADAPTIVE OPTIMIZATION

Our method improves attack efficiency mainly by reducing the number of optimization steps. The behavior-guidance term reuses a hidden state from the attack forward pass and applies a lightweight 0.46–0.53M parameter predictor, requiring neither response generation nor external evaluator calls within the optimization loop. In a fixed budget of 300 steps, adding the behavioral term changes mean wall-clock time by $-0.27\%$ to $+1.94\%$ and peak memory by at most $0.13\%$ across the four models (Appendix A.6). Table 2 shows that the mean number of optimization steps decreases from 300 to 32.7–161.2, corresponding to $1.86\times$ to $9.19\times$ fewer steps, while wall-clock speedup ranges

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

[OCR table id=tbl-0.html; page=7]
<table><tr><td rowspan="2">Method</td><td colspan="2">Qwen2.5-VL-7B</td><td colspan="2">LLaVA-1.5-7B</td><td colspan="2">InternVL3-8B</td><td colspan="2">Llama-3.2-V-11B</td></tr><tr><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td></tr><tr><td>Baseline</td><td>44.17</td><td>30.53</td><td>69.14</td><td>46.35</td><td>44.27</td><td>37.19</td><td>26.28</td><td>16.79</td></tr><tr><td>Random perturb.</td><td>45.69</td><td>32.28</td><td>67.07</td><td>46.67</td><td>46.78</td><td>36.75</td><td>25.41</td><td>16.90</td></tr><tr><td>PGD ($\mathcal{L}_{\text{attack}}$)</td><td>54.31</td><td>38.17</td><td>42.42</td><td>29.99</td><td>53.00</td><td>33.70</td><td>45.15</td><td>28.03</td></tr><tr><td>Ours ([NAME C03])</td><td>70.99</td><td>48.42</td><td>75.68</td><td>54.63</td><td>72.52</td><td>53.22</td><td>63.03</td><td>41.11</td></tr><tr><td>$\Delta$ vs. PGD</td><td>+16.68</td><td>+10.25</td><td>+33.26</td><td>+24.64</td><td>+19.52</td><td>+19.52</td><td>+17.88</td><td>+13.08</td></tr></table>

[OCR table id=tbl-1.html; page=7]
<table><tr><td>Model</td><td>Mean steps ↓<br/>(reduction ↑)</td><td>Median<br/>$k_{\text{adapt}}$ ↓</td><td>Threshold<br/>reached (%) ↑</td><td>Wall-clock<br/>speedup ↑</td><td>Perturbation $\ell_2$ norm ↓<br/>PGD → [NAME C03]</td></tr><tr><td>Qwen2.5-VL-7B</td><td>161.2 (1.86×)</td><td>145</td><td>72.3</td><td>1.8×</td><td>40.05 → 39.41 (−1.60%)</td></tr><tr><td>LLaVA-1.5-7B</td><td>141.3 (2.12×)</td><td>117</td><td>77.0</td><td>2.1×</td><td>22.48 → 21.50 (−4.36%)</td></tr><tr><td>InternVL3-8B</td><td>32.7 (9.19×)</td><td>21</td><td>99.4</td><td>10.4×</td><td>72.70 → 65.92 (−9.33%)</td></tr><tr><td>Llama-3.2-V-11B</td><td>72.8 (4.12×)</td><td>41</td><td>94.1</td><td>4.1×</td><td>43.78 → 41.16 (−5.98%)</td></tr></table>

## A-page-0008

target PDF page 8

from 1.8× to 10.4×. The retained perturbation is also smaller, with a mean ℓ₂ norm 1.6%–9.3% lower than full-budget PGD under the same ℓ∞ constraint. Together with Section 4.5, where stopping at k_adapt improves E-ASR by 3.82%–8.29% over the same objective for all 300 steps, these results show that instance-adaptive stopping reduces computation and perturbation magnitude without sacrificing attack effectiveness.

Table 3: Ablation of behavioral guidance and instance-adaptive optimization across four target VLMs. E-ASR and HarmBench ASR (%) are reported on n=917 evaluation data. Bold and italic indicate the best and second-best results in each column, respectively.

[tbl-2.html](tbl-2.html)

### 4.5 ABLATION STUDY

Table 3 separates the contributions of behavioral guidance and instance-adaptive optimization. Adding L$_{behavior}$ under a fixed 300 step budget improves E-ASR by 11.23–26.50 percentage points and HarmBench ASR by 7.41–19.41 points over affirmative-target PGD. Enabling k$_{adapt}$ further improves E-ASR by 3.82–8.29 points and HarmBench ASR by 0.11–7.85 points across four target models. The second and third rows use the same joint objective and differ only in adaptive iterate selection. The adaptive variant improves every metric, indicating that retaining the selected iterate can be more effective than continuing to the full budget. Once the predicted behavior score reaches τ, L$_{behavior}$ becomes zero, so subsequent updates may move away from the high-scoring behavior favored in Section 4.3. Thus, the predicted behavior score both guides optimization and determines when to retain an effective iterate. Sensitivity to λ, ε, and the threshold percentile is in Appendix C.

Table 4: Attack performance under three defenses across four target VLMs. E-ASR and HarmBench ASR (%) are reported on 917 evaluation data. Small arrow indicate the relative change from the corresponding undefended performance. Bold and italic denote the best and second-best results.

[tbl-3.html](tbl-3.html)

### 4.6 ROBUSTNESS TO DEFENSES

We evaluate three defense methods: CIDER (Xu et al., 2024), JailGuard (Zhang et al., 2026), and ECSO (Gou et al., 2024). CIDER detects adversarial images based on cross-modal similarity changes under denoising, JailGuard detects attacks through response discrepancies across input mutations, and ECSO regenerates a text-only response from an image caption when the initial response is judged unsafe. Table 4 shows that our attack retains higher E-ASR and HarmBench ASR than affirmative-target PGD in all 24 defense–model–metric comparisons. Relative to the undefended setting, [NAME C03] also exhibits a smaller E-ASR reduction than PGD in 9 of 12 defense–model combinations, demonstrating greater overall robustness. Under CIDER, [NAME C03] shows consistently smaller E-ASR degradation across all four target VLMs. Even when [NAME C03] experiences a larger relative reduction, its absolute post-defense performance remains higher. For example, under JailGuard on Llama-3.2-V, [NAME C03] retains an E-ASR of 45.7, compared with 34.4 for PGD. Overall, these results show that the advantage of [NAME C03] persists both absolute attack success and relative high robustness.

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

[OCR table id=tbl-2.html; page=8]
<table><tr><td rowspan="2">L<sub>attack</sub></td><td rowspan="2">L<sub>behavior</sub></td><td rowspan="2">k<sub>adapt</sub></td><td colspan="2">Qwen2.5-VL-7B</td><td colspan="2">LLaVA-1.5-7B</td><td colspan="2">InternVL3-8B</td><td colspan="2">Llama-3.2-V-11B</td></tr><tr><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td></tr><tr><td>✓</td><td></td><td></td><td>54.31</td><td>38.17</td><td>42.42</td><td>29.99</td><td>53.00</td><td>33.70</td><td>45.15</td><td>28.03</td></tr><tr><td>✓</td><td>✓</td><td></td><td>67.07</td><td>48.31</td><td>68.92</td><td>49.40</td><td>64.23</td><td>45.37</td><td>59.21</td><td>35.44</td></tr><tr><td>✓</td><td>✓</td><td>✓</td><td>70.99</td><td>48.42</td><td>75.68</td><td>54.63</td><td>72.52</td><td>53.22</td><td>63.03</td><td>41.11</td></tr></table>

[OCR table id=tbl-3.html; page=8]
<table><tr><td rowspan="2">Defense Method</td><td rowspan="2">Attack Method</td><td colspan="2">Qwen2.5-VL-7B</td><td colspan="2">LLaVA-1.5-7B</td><td colspan="2">InternVL3-8B</td><td colspan="2">Llama-3.2-V-11B</td></tr><tr><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td></tr><tr><td rowspan="2">CIDER</td><td>PGD (L<sub>attack</sub>)</td><td>51.3 ↓5.6%</td><td>35.3 ↓7.4%</td><td>38.4 ↓9.5%</td><td>26.3 ↓12.4%</td><td>50.1 ↓5.6%</td><td>32.2 ↓4.5%</td><td>43.0 ↓4.8%</td><td>27.0 ↓3.5%</td></tr><tr><td>[NAME C03]</td><td>68.5 ↓3.5%</td><td>46.1 ↓4.7%</td><td>70.2 ↓7.2%</td><td>51.5 ↓5.8%</td><td>69.9 ↓3.6%</td><td>50.7 ↓4.7%</td><td>60.2 ↓4.5%</td><td>39.5 ↓4.0%</td></tr><tr><td rowspan="2">JailGuard</td><td>PGD (L<sub>attack</sub>)</td><td>47.4 ↓12.6%</td><td>33.5 ↓12.3%</td><td>38.7 ↓8.7%</td><td>27.8 ↓7.3%</td><td>44.4 ↓16.3%</td><td>28.5 ↓15.5%</td><td>34.4 ↓23.9%</td><td>20.9 ↓25.3%</td></tr><tr><td>[NAME C03]</td><td>62.3 ↓12.3%</td><td>40.7 ↓16.0%</td><td>72.3 ↓4.5%</td><td>52.8 ↓3.4%</td><td>58.7 ↓19.1%</td><td>40.2 ↓24.4%</td><td>45.7 ↓27.5%</td><td>28.9 ↓29.7%</td></tr><tr><td rowspan="2">ECSO</td><td>PGD (L<sub>attack</sub>)</td><td>38.4 ↓29.3%</td><td>25.1 ↓34.3%</td><td>28.9 ↓31.9%</td><td>19.2 ↓36.0%</td><td>36.3 ↓31.5%</td><td>23.9 ↓29.1%</td><td>43.8 ↓2.9%</td><td>28.0 ↓0.0%</td></tr><tr><td>[NAME C03]</td><td>51.5 ↓27.5%</td><td>31.1 ↓35.8%</td><td>48.3 ↓36.2%</td><td>32.5 ↓40.5%</td><td>56.4 ↓22.3%</td><td>39.2 ↓26.4%</td><td>62.2 ↓1.4%</td><td>41.2 ↑0.3%</td></tr></table>

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

![img-7.jpeg](img-7.jpeg)

![img-8.jpeg](img-8.jpeg)

![img-9.jpeg](img-9.jpeg)

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)

Figure 3: Response-behavior analysis across four target VLMs on 917 evaluation inputs. (a) ELITE-score distributions for Baseline, affirmative-target PGD, and [NAME C03], partitioned into refusal (ELITE=0), partial compliance (0<ELITE<10), and successful responses (ELITE≥10). (b)-(e) Refusal rate and mean toxicity, convincingness, and specificity for PGD and [NAME C03]. Annotations show PGD-to-[NAME C03] score changes, with percentages normalized by the corresponding rubric range.

### 4.7 RESPONSE-BEHAVIOR ANALYSIS

Figure 3 examines how the response distribution changes beyond the binary success criterion used to compute E-ASR. Compared with affirmative-target PGD, [NAME C03] consistently shifts the ELITE-score distribution toward higher scores across all four VLMs. Refusal-like responses (ELITE=0) decrease by 14.1–27.2 percentage points, while intermediate responses (0 <ELITE< 10) decrease by 1.1–6.1 points. At the same time, successful responses (ELITE≥ 10) increase by 16.7–33.3 points. These results show that the E-ASR gains reflect a broad redistribution of responses from the refusal and intermediate regions toward the successful region, rather than marginal changes around the ELITE= 10 decision boundary. The percentage annotation show that, relative to PGD, [NAME C03] reduces refusal by 6.1–19.0% and increases toxicity by 8.9–18.6%, convincingness by 10.3–23.3%, and specificity by 13.8–26.3%. These results indicate that the gains extend beyond refusal reduction, with consistent changes in the toxicity, convincingness, and specificity of the generated responses.

## 5 CONCLUSION

We introduced [NAME C03] for jailbreak attacks. A model-specific behavior predictor provides a differentiable signal for image optimization and guides instance-adaptive iterate selection. Across 917 multimodal jailbreak data and four VLMs our method improves E-ASR by 16.68 to 33.26 percentage points and HarmBench ASR by 10.25 to 24.64 points over affirmative-target PGD. Instance-adaptive optimization reduces the mean step count from 300 to 32.7–161.2 and yields 1.8×–10.4× wall-clock speedups. The gains persist across three defense methods, while response-behavior analysis shows shifts from refusal and intermediate responses toward successful responses. Overall, these results demonstrate the benefit of aligning gradient-based visual optimization with response-level behavior.

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

We used generative AI tools to assist with and refine writing, retrieve and analyze relevant literature, draft section of the manuscript, and support research execution. Generative AI was also used for code development, dataset preprocessing and formatting, translation, feedback on result interpretation. We did not use generative AI to create synthetic datasets or establish mathematical claims. All AI-assisted outputs were reviewed and verified by the authors. AI-assisted code and data-processing procedures were inspected and tested for correctness, cited references were checked against their original sources, and AI-assisted interpretations were validated against the experimental results. The authors take responsibility for the final content of this work, including the text, claims, code, and other materials produced with the assistance of generative AI.

## ETHICS STATEMENT

This work studies white-box visual jailbreak attacks on vision-language models (VLMs) to characterize safety vulnerabilities and support more rigorous multimodal safety evaluation. All experiments use publicly released VLMs and established multimodal jailbreak and safety benchmarks. We do not construct or introduce a new benchmark dataset in this study. We recognize the dual-use nature of jailbreak research, as the proposed attack may expose weaknesses in existing safety mechanisms. To provide a more balanced assessment of this risk, we additionally evaluate [NAME C03] under three representative defense methods, examining its behavior in the presence of existing safeguards. To mitigate potential misuse, we report aggregate attack metrics and response-level analyses rather than reproducing unsafe model generations or actionable harmful content. Moreover, [NAME C03] requires white-box access to internal model representations, limiting its direct applicability to deployed closed models. We intend these findings to support safer VLM development by identifying limitations in existing visual jailbreak objectives and enabling more rigorous evaluation of VLM safety mechanisms. We encourage the use of this method only for authorized safety research and evaluation.

## REPRODUCIBILITY STATEMENT

Section 4.1 summarizes the common experimental protocol, and Appendix A provides the details needed for reproduction: the dataset composition, split procedure, and disjointness of the 917 input evaluation set from predictor training and layer selection (Appendix A.1); the exact model checkpoints and selected representation index for each model (Appendix A.2); the predictor architecture, training procedure, standardization, and threshold calibration (Appendix A.3); the attack hyperparameters, initialization, fixed affirmative target string, and per-model perturbation space (Appendix A.4); the generation settings, judge configurations, and defense evaluation protocol (Appendix A.5); and the compute environment and measurement protocol (Appendix A.6). Sensitivity to the main attack hyperparameters, including \(\epsilon\), \(\lambda\), and the threshold percentile, is reported in Appendix C.

## REFERENCES

Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katherine Millican, Malcolm Reynolds, Roman Ring, Eliza Rutherford, Serkan Cabi, Tengda Han, Zhitao Gong, Sina Samangooei, Marianne Monteiro, Jacob L. Menick, Sebastian Borgeaud, Andy Brock, Aida Nematzadeh, Sahand Sharifzadeh, Mikolaj Binkowski, Ricardo Barreira, Oriol Vinyals, Andrew Zisserman, and Karen Simonyan. Flamingo: a visual language model for few-shot learning. In Advances in Neural Information Processing Systems, volume 35, pp. 23716–23736, 2022.

Andy Arditi, Oscar Obeso, Aaquib Syed, Daniel Paleka, Nina Panickssery, Wes Gurnee, and Neel Nanda. Refusal in language models is mediated by a single direction. In Advances in Neural Information Processing Systems, volume 37, 2024.

Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, Kai Dang, Peng Wang, Shijie Wang, Jun Tang, Humen Zhong, Yuanzhi Zhu, et al. Qwen2.5-VL technical report. arXiv preprint arXiv:2502.13923, 2025.

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

Collin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt. Discovering latent knowledge in language models without supervision. In International Conference on Learning Representations, 2023.

Patrick Chao, Edoardo Debenedetti, Alexander Robey, Maksym Andriushchenko, Francesco Croce, Vikash Sehwag, Edgar Dobriban, Nicolas Flammarion, George J. Pappas, Florian Tramèr, Hamed Hassani, and Eric Wong. JailbreakBench: An open robustness benchmark for jailbreaking large language models. In Advances in Neural Information Processing Systems, Datasets and Benchmarks Track, volume 37, 2024.

Yichen Gong, Delong Ran, Jinyuan Liu, Conglei Wang, Tianshuo Cong, Anyu Wang, Sisi Duan, and Xiaoyun Wang. FigStep: Jailbreaking large vision-language models via typographic visual prompts. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 39, pp. 23951–23959, 2025.

Yunhao Gou, Kai Chen, Zhili Liu, Lanqing Hong, Hang Xu, Zhenguo Li, Dit-Yan Yeung, James T. Kwok, and Yu Zhang. Eyes closed, safety on: Protecting multimodal LLMs via image-to-text transformation. In European Conference on Computer Vision, pp. 388–404, 2024.

Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, et al. The Llama 3 herd of models. arXiv preprint arXiv:2407.21783, 2024.

Tianle Gu, Zeyang Zhou, Kexin Huang, Dandan Liang, Yixu Wang, Haiquan Zhao, Yuanqi Yao, Xingge Qiao, Keqing Wang, Yujiu Yang, Yan Teng, Yu Qiao, and Yingchun Wang. MLLMGuard: A multi-dimensional safety evaluation suite for multimodal large language models. In Advances in Neural Information Processing Systems, Datasets and Benchmarks Track, volume 37, 2024.

Haojie Hao, Jiakai Wang, Aishan Liu, Yuqing Ma, Haotong Qin, Yuanfang Guo, and Xianglong Liu. Activation manipulation attack: Penetrating and harmful jailbreak attack against large vision-language models. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 40, pp. 35481–35489, 2026.

Diederik P. Kingma and Jimmy Ba. Adam: A method for stochastic optimization. In International Conference on Learning Representations, 2015.

Wonjun Lee, Doehyeon Lee, Eugene Choi, Sangyoon Yu, Ashkan Yousefpour, Haon Park, Bumsub Ham, and Suhyun Kim. ELITE: Enhanced language-image toxicity evaluation for safety. In Proceedings of the 42nd International Conference on Machine Learning, volume 267 of Proceedings of Machine Learning Research, pp. 33276–33299. PMLR, 2025.

Yifan Li, Hangyu Guo, Kun Zhou, Wayne Xin Zhao, and Ji-Rong Wen. Images are achilles' heel of alignment: Exploiting visual vulnerabilities for jailbreaking multimodal large language models. In European Conference on Computer Vision, pp. 174–189, 2024.

Runqi Lin, Alasdair Paren, Suqin Yuan, Muyang Li, Philip Torr, Adel Bibi, and Tongliang Liu. FORCE: Transferable visual jailbreaking attacks via feature over-reliance correction. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2026.

Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. In Advances in Neural Information Processing Systems, volume 36, pp. 34892–34916, 2023.

Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction tuning. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 26296–26306, 2024a.

Xin Liu, Yichen Zhu, Jindong Gu, Yunshi Lan, Chao Yang, and Yu Qiao. MM-SafetyBench: A benchmark for safety evaluation of multimodal large language models. In European Conference on Computer Vision, pp. 386–403, 2024b.

Weidi Luo, Siyuan Ma, Xiaogeng Liu, Xiaoyu Guo, and Chaowei Xiao. JailBreakV: A benchmark for assessing the robustness of multimodal large language models against jailbreak attacks. In First Conference on Language Modeling, 2024.

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

Teng Ma, Xiaojun Jia, Ranjie Duan, Xinfeng Li, Yihao Huang, Xiaoshuang Jia, Zhixuan Chu, and Wenqi Ren. Heuristic-induced multimodal risk distribution jailbreak attack for multimodal large language models. In IEEE/CVF International Conference on Computer Vision, pp. 2686–2696, 2025.

Aleksander Madry, Aleksandar Makelov, Ludwig Schmidt, Dimitris Tsipras, and Adrian Vladu. Towards deep learning models resistant to adversarial attacks. In International Conference on Learning Representations, 2018.

Mantas Mazeika, Long Phan, Xuwang Yin, Andy Zou, Zifan Wang, Norman Mu, Elham Sakhaee, Nathaniel Li, Steven Basart, Bo Li, David Forsyth, and Dan Hendrycks. HarmBench: A standardized evaluation framework for automated red teaming and robust refusal. In Proceedings of the 41st International Conference on Machine Learning, volume 235 of Proceedings of Machine Learning Research, pp. 35181–35224. PMLR, 2024.

Meta AI. Llama 3.2: Revolutionizing edge AI and vision with open, customizable models. Meta AI blog, 2024.

Zhenxing Niu, Haodong Ren, Xinbo Gao, Gang Hua, and Rong Jin. Jailbreaking attack against multimodal large language model. arXiv preprint arXiv:2402.02309, 2024.

OpenAI. GPT-4o system card. OpenAI system card, 2024. Also available as arXiv:2410.21276.

Xiangyu Qi, Kaixuan Huang, Ashwinee Panda, Peter Henderson, Mengdi Wang, and Prateek Mittal. Visual adversarial examples jailbreak aligned large language models. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pp. 21527–21536, 2024.

Nina Rimsky, Nick Gabrieli, Julian Schulz, Meg Tong, Evan Hubinger, and Alexander Turner. Steering Llama 2 via contrastive activation addition. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 15504–15522. Association for Computational Linguistics, 2024.

Erfan Shayegani, Yue Dong, and Nael Abu-Ghazaleh. Jailbreak in pieces: Compositional adversarial attacks on multi-modal language models. In International Conference on Learning Representations, 2024.

Jiaxin Song, Yixu Wang, Jie Li, Xuan Tong, Rui Yu, Yan Teng, Xingjun Ma, and Yingchun Wang. JailBound: Jailbreaking internal safety boundaries of vision-language models. In Advances in Neural Information Processing Systems, volume 38, 2025.

Alexandra Souly, Qingyuan Lu, Dillon Bowen, Tu Trinh, Elvis Hsieh, Sana Pandey, Pieter Abbeel, Justin Svegliato, Scott Emmons, Olivia Watkins, and Sam Toyer. A StrongREJECT for empty jailbreaks. In Advances in Neural Information Processing Systems, Datasets and Benchmarks Track, volume 37, 2024.

Siyin Wang, Xingsong Ye, Qinyuan Cheng, Junwen Duan, Shimin Li, Jinlan Fu, Xipeng Qiu, and Xuanjing Huang. Safe inputs but unsafe output: Benchmarking cross-modality safety alignment of large vision-language models. In Findings of the Association for Computational Linguistics: NAACL 2025, pp. 3563–3605. Association for Computational Linguistics, 2025.

Yue Xu, Xiuyuan Qi, Zhan Qin, and Wenjie Wang. Cross-modality information check for detecting jailbreaking in multimodal large language models. In Findings of the Association for Computational Linguistics: EMNLP 2024, pp. 13715–13726. Association for Computational Linguistics, 2024.

Xiaoyu Zhang, Cen Zhang, Tianlin Li, Yihao Huang, Xiaojun Jia, Ming Hu, Jie Zhang, Yang Liu, Shiqing Ma, and Chao Shen. JailGuard: A universal detection framework for prompt-based attacks on LLM systems. ACM Transactions on Software Engineering and Methodology, 35(1): 1–40, 2026.

Yongting Zhang, Lu Chen, Guodong Zheng, Yifeng Gao, Rui Zheng, Jinlan Fu, Zhenfei Yin, Senjie Jin, Yu Qiao, Xuanjing Huang, Feng Zhao, Tao Gui, and Jing Shao. SPA-VL: A comprehensive safety preference alignment dataset for vision language models. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 19867–19878, 2025.

## A-page-0013

target PDF page 13

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

Jinguo Zhu, Weiyun Wang, Zhe Chen, Zhaoyang Liu, Shenglong Ye, Lixin Gu, Yuchen Duan, Hao Tian, Weijie Su, Jie Shao, Zhangwei Gao, Erfei Cui, et al. InternVL3: Exploring advanced training and test-time recipes for open-source multimodal models. arXiv preprint arXiv:2504.10479, 2025.

Yongshuo Zong, Ondrej Bohdal, Tingyang Yu, Yongxin Yang, and Timothy M. Hospedales. Safety fine-tuning at (almost) no cost: A baseline for vision large language models. In Proceedings of the 41st International Conference on Machine Learning, volume 235 of Proceedings of Machine Learning Research, pp. 62867–62891. PMLR, 2024.

Andy Zou, Long Phan, Sarah Chen, James Campbell, Phillip Guo, Richard Ren, Alexander Pan, Xuwang Yin, Mantas Mazeika, Ann-Kathrin Dombrowski, Shashwat Goel, Nathaniel Li, Michael J. Byun, Zifan Wang, Alex Mallen, Steven Basart, Sanmi Koyejo, Dawn Song, Matt Fredrikson, J. Zico Kolter, and Dan Hendrycks. Representation engineering: A top-down approach to AI transparency. arXiv preprint arXiv:2310.01405, 2023.

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

# A EXPERIMENTAL DETAILS AND REPRODUCIBILITY

## A.1 EVALUATION DATA AND SPLITS

All inputs are drawn from the ELITE benchmark (Lee et al., 2025), which aggregates 4,587 image-text pairs from eight source datasets and assigns each pair to one of eleven hazard categories. We partition the benchmark once using a uniform random permutation with seed 42 and a held-out fraction of 0.2, yielding 3,670 training inputs and 917 held-out evaluation inputs. The 917 held-out inputs form the evaluation set used throughout the paper and are disjoint from all inputs used for behavior-predictor training and layer selection.

Within the 3,670 training inputs, we further construct a 90/10 split using seed 42, yielding 3,303 fitting inputs and 367 validation inputs. The fitting split is used to train the behavior predictor, while the validation split is used for layer selection. Neither split overlaps with the 917 held-out evaluation inputs.

Table A1: Composition of the ELITE benchmark and its training and evaluation splits by source dataset. New denotes the benchmark's newly collected portion rather than data drawn from an existing dataset. The evaluation column corresponds to the 917-input held-out set used for all attack evaluations.

[tbl-4.html](tbl-4.html)

The evaluation split covers all eleven hazard categories: S1 Violent Crimes (141), S2 Non-Violent Crimes (147), S3 Sex Crimes (56), S4 Defamation (79), S5 Specialized Advice (65), S6 Privacy (62), S7 Intellectual Property (64), S8 Indiscriminate Weapons (69), S9 Hate (103), S10 Self-Harm (56), and S11 Sexual Content (75). For every attack, the model receives the benchmark's original question field as the text prompt, which remains unchanged throughout optimization.

## A.2 TARGET MODEL CHECKPOINTS

Table A2 reports the exact model checkpoints used in our experiments. We note that the Llama 3 technical report (Grattafiori et al., 2024) predates the Llama-3.2 vision release, so the precise checkpoint we attack is the one documented in its model card (Meta AI, 2024). Representations are extracted from the tuple of hidden states returned by the language model, where element 0 corresponds to the embedding output. Accordingly, the index column denotes the tuple entry used by the behavior predictor, while the states column counts the embedding output together with one state per decoder layer.

## A.3 BEHAVIOR PREDICTOR TRAINING

For each training input, we generate a response from the unperturbed image and score it with the ELITE evaluator, yielding a regression target in [0, 25]. Only unperturbed inputs are used for behavior-predictor training. The predictor input is the hidden state at the final prompt position from the selected index, extracted before any response token is generated. These representations are standardized using statistics computed only from the fitting split.

The behavior predictor is a two-hidden-layer MLP with dimensions $d_h \to 128 \to 32 \to 1$, using ReLU activations and dropout between layers. It is trained with Adam (Kingma & Ba, 2015) at a learning rate of $10^{-3}$, weight decay of $10^{-3}$, and dropout of 0.4, for up to 300 epochs with

[OCR table id=tbl-4.html; page=14]
<table><tr><td>Source dataset</td><td>Full benchmark</td><td>Train</td><td>Evaluation</td></tr><tr><td>SPA-VL (Zhang et al., 2025)</td><td>1,403</td><td>1,127</td><td>276</td></tr><tr><td>New</td><td>1,054</td><td>857</td><td>197</td></tr><tr><td>FigStep (Gong et al., 2025)</td><td>644</td><td>514</td><td>130</td></tr><tr><td>JailbreakV-28K (Luo et al., 2024)</td><td>551</td><td>438</td><td>113</td></tr><tr><td>VLGuard (Zong et al., 2024)</td><td>474</td><td>369</td><td>105</td></tr><tr><td>MM-SafetyBench (Liu et al., 2024b)</td><td>405</td><td>319</td><td>86</td></tr><tr><td>MLLMGuard (Gu et al., 2024)</td><td>43</td><td>36</td><td>7</td></tr><tr><td>SIUO (Wang et al., 2025)</td><td>13</td><td>10</td><td>3</td></tr><tr><td>Total</td><td>4,587</td><td>3,670</td><td>917</td></tr></table>

## A-page-0015

target PDF page 15

Table A2: Target VLMs and model-specific representation settings. States denotes the number of entries in the hidden-state tuple, including the embedding output and one state per decoder layer. Index denotes the hidden-state tuple entry used by the behavior predictor for both predictor training and attack optimization. Width is the hidden size and determines the predictor input dimension. All target VLMs use publicly released instruction-tuned checkpoints and remain frozen throughout.

[tbl-5.html](tbl-5.html)

early stopping on the inner validation split and seed 42. For  \( d_{h} \)  of 3584 or 4096, the predictor contains approximately 0.46–0.53M parameters, making its size negligible relative to the 7–11B target VLMs. During attack optimization, the predictor is placed in evaluation mode with dropout disabled, all predictor parameters remain frozen, and the standardization statistics are loaded from the checkpoint. Because the scalar output head is linear and unconstrained, predicted scores may fall outside [0, 25]. Accordingly,  \( L_{behavior} \)  uses a normalized hinge deficit rather than a ratio-based objective.

Layer selection. Each model's index is selected based on the behavior predictor's performance on the inner validation split. Figure 2 shows the full layer sweep used for this selection. Predictive performance remains relatively stable across the deepest third of each network, where the validation correlation varies by at most 0.056. We therefore do not attribute special significance to a particular index; rather, multiple indices within this plateau provide comparable predictive performance.

Threshold calibration. For each model,  \( \tau \)  is defined as the 99th percentile of the frozen behavior predictor's outputs on clean, unperturbed inputs and remains fixed throughout both the behavior-guidance loss and instance-adaptive optimization. The resulting thresholds are  \( \tau = 20.25 \)  for Qwen2.5-VL, 21.61 for LLaVA-1.5, 21.88 for InternVL3, and 20.17 for Llama-3.2-V. Thus,  \( \tau \)  is calibrated solely from predictions on clean inputs, without using evaluation labels or adversarial responses.

### A.4 ATTACK CONFIGURATION

All attacks use \(\epsilon = 16 / 255\), step size \(\alpha = 1 / 255\), and \(K = 300\) sign-gradient updates. The optimization trajectory contains 301 iterates, including the randomly initialized \(\delta^{(0)}\), which is also eligible for selection. The perturbation is initialized uniformly within the \(\ell_{\infty}\) ball and projected onto the valid pixel range. A per-sample generator with seed \(42 \times 1000003 + \text{index}\), where index denotes the sample index, ensures that initialization depends only on the input and is invariant to sharding or restarts. Each update applies \(\delta \leftarrow \mathrm{clip}_{[-\epsilon, \epsilon]}(\delta - \alpha \operatorname{sign}(\nabla_{\delta} \mathcal{L}_{\text{total}}))\), followed by projection onto the valid pixel range.

The affirmative target is the fixed string "Sure, here is how to do that. Step 1:", which is identical across all models and conditions. It is tokenized with each model's tokenizer without special tokens and scored using teacher forcing. When \(\lambda = 0\), the behavior-guidance term is omitted from the objective rather than multiplied by zero, ensuring that no gradient passes through the behavior predictor. This condition therefore corresponds exactly to affirmative-target PGD.

Reported iterates. The PGD row of Table 1 corresponds to \(\lambda = 0\) evaluated at the final iterate. For [NAME C03], \(\lambda = 4\), and the selected iterate is the first one whose predicted behavior score reaches \(\tau\); if the threshold is never reached, we select the trajectory iterate with the highest predicted behavior score. For attack-success evaluation, the full optimization budget is executed for every input, and the reported [NAME C03] iterate is selected retrospectively from the recorded trajectory. This ensures that the reported attack effectiveness does not depend on whether the implementation terminates optimization early. The computational savings from online instance-adaptive optimization are measured

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

[OCR table id=tbl-5.html; page=15]
<table><tr><td>Model</td><td>Checkpoint</td><td>States</td><td>Index</td><td>Width</td></tr><tr><td>Qwen2.5-VL-7B</td><td>Qwen/Qwen2.5-VL-7B-Instruct</td><td>29</td><td>25</td><td>3584</td></tr><tr><td>LLaVA-1.5-7B</td><td>llava-hf/llava-1.5-7b-hf</td><td>33</td><td>18</td><td>4096</td></tr><tr><td>InternVL3-8B</td><td>OpenGVLab/InternVL3-8B-hf</td><td>29</td><td>24</td><td>3584</td></tr><tr><td>Llama-3.2-V-11B</td><td>meta-llama/Llama-3.2-11B-Vision-Instruct</td><td>41</td><td>37</td><td>4096</td></tr></table>

## A-page-0016

target PDF page 16

separately in the dedicated efficiency runs reported in Table 2, where the remaining updates are skipped immediately after τ is reached.

Where the perturbation lives. Because the four target VLMs use different preprocessing pipelines, we specify the space in which the perturbation budget is enforced. In all cases, δ is defined on the model-specific preprocessed input rather than on the original image file. For Qwen2.5-VL, the perturbation is applied at the processor's smart-resize resolution; for LLaVA-1.5, to the 336 × 336 resized and center-cropped image; for InternVL3, to the stitched tile canvas from which the thumbnail is derived; and for Llama-3.2-V, to the aspect-fitted region of the padded canvas. For each model, optimization is performed through a differentiable reimplementation of its official preprocessing pipeline. The resulting perturbed image is then saved and reloaded through the unmodified official processor for response generation and evaluation. Accordingly, we define the perturbation constraint as an ℓ∞ bound in the model-specific preprocessed input space rather than on the original image file.

# A.5 EVALUATION PROTOCOL AND JUDGES

Responses are generated greedily (do_sample=False) with at most 256 new tokens, identically for every model, attack, and defense condition, at batch size 1.

ELITE evaluator. We score responses with the ELITE rubric (Lee et al., 2025) using gpt-4o-mini as the judge backbone. The image provided to the judge is downscaled to fit within 256 × 256 while preserving its aspect ratio. Because the original work uses a larger judge backbone, absolute E-ASR values are not directly comparable to those reported in the original work, although comparisons across conditions within our experiments remain unaffected. The clean condition is evaluated using the original image, whereas each attacked condition is evaluated using the adversarial image received by the target VLM.

HarmBench classifier. HarmBench ASR is computed using the cals/HarmBench-Llama-2-13b-cls classifier (Mazeika et al., 2024), with the benchmark question provided as the behavior field and the model response as the generation field. The classifier decodes a single token, and an affirmative label is counted as attack success. HarmBench is text-only and is not used for behavior-predictor training, layer selection, threshold calibration, or iterate selection. It therefore serves as an independent evaluation signal in Section 4.3.

Defenses. CIDER (Xu et al., 2024) compares cross-modal similarity between image and query before and after diffusion denoising and refuses above a calibrated threshold. The threshold is calibrated to a 5% false-positive rate on held-out clean images, yielding a realized block rate of 3.82% on our clean condition. JailGuard (Zhang et al., 2026) generates mutated variants of the input, compares the divergence of the resulting responses, and refuses above a divergence threshold. ECSO (Gou et al., 2024) has the model assess its own draft response and, when the draft is judged unsafe, regenerates from a text caption with the image withheld. CIDER and JailGuard act as detectors and return a decision rather than a replacement response. For evaluation, inputs detected by either defense are counted as refusals, ensuring comparability between defended and undefended conditions. All three defenses leave the adversarial image unchanged when they are not triggered.

# A.6 COMPUTE ENVIRONMENT

All attack optimization, response generation, and judging are performed on NVIDIA H100 80GB HBM3 GPUs with batch size 1.

The wall-clock measurements in Table 2 are obtained from dedicated efficiency runs separate from the attack runs used to compute success rates. To ensure comparable timing conditions, each run uses a single GPU of the same model with no competing workload, identical inputs and numerical precision, and warm-up samples that are excluded from the reported statistics. Each timed region is bracketed by torch.cuda.synchronize to prevent asynchronous GPU operations from carrying over between samples. Timing covers only the optimization loop and excludes response generation, judging, and disk I/O for saving adversarial images. Optimization-step, forward-pass, and backward-pass counts are also recorded for each sample.

810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863

## A-page-0017

target PDF page 17

864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917

Among the twelve measured conditions, the fixed-budget settings with λ=0 and λ=4 execute the same 300 optimization steps on identical inputs and differ only in the optimization objective. Relative to λ=0, mean wall-clock time for λ=4 changes by −0.27%, +1.94%, +1.64%, and +0.15% for Qwen2.5-VL, LLaVA-1.5, InternVL3, and Llama-3.2-V, respectively. Mean peak allocated memory differs by at most 0.13% across the three measured conditions for each model.

The iteration at which the predicted behavior score reaches τ varies substantially across models, accounting for the differences in efficiency reported in Table 2. The median retained iterate is 21 for InternVL3 and 145 for Qwen2.5-VL, with τ reached for 99.4% and 72.3% of inputs, respectively. Inputs that never reach τ continue through the full optimization budget and fall back to the trajectory iterate with the highest predicted behavior score. The reported mean step counts therefore include these full-budget cases rather than excluding them.

## B ADDITIONAL BEHAVIOR PREDICTOR ANALYSIS

Section 4.2 uses a single decoder layer for each target VLM. Because predictive performance remains relatively stable across the deepest third of each network, we further examine whether combining multiple highly ranked layers provides a stronger behavioral signal. Table A3 repeats the full attack using behavior predictors that concatenate representations from the 5 or 10 highest-ranked layers instead of a single layer.

Combining multiple layers does not yield consistent improvements. Relative to the single-layer predictor, k=5 improves 3 of the 8 model–metric combinations, while k=10 improves 5 of 8. Only Llama-3.2-V improves on both metrics under both multi-layer settings. The magnitude of these changes is also modest relative to the gains reported for [NAME C03] in the main experiments. The largest improvement is +4.36 points in HarmBench ASR for InternVL3 at k=10, while the largest decrease is −5.13 points in E-ASR for Qwen2.5-VL at k=5. Both are smaller in magnitude than the smallest improvement of [NAME C03] over affirmative-target PGD across the two metrics (+10.25 points). Because concatenating multiple layers increases the behavior predictor input dimension and requires accessing additional hidden states at every optimization step, we retain a single layer per model.

Table A3: Effect of concatenating multiple decoder-layer representations in the behavior predictor. k=1 denotes the single-layer setting used throughout the paper, while k=5 and k=10 concatenate representations from the five and ten highest-ranked layers, respectively. All other settings remain unchanged (λ=4, instance-adaptive optimization). Each cell reports E-ASR (%) and HarmBench ASR (%), with higher values indicating better attack performance. Within each row, the best and second-best results across k are shown in bold and italic, respectively. n=917.

[tbl-6.html](tbl-6.html)

## C HYPERPARAMETER AND THRESHOLD SENSITIVITY

This appendix examines the sensitivity of the default settings used in Section 4.1. In each sweep, only the specified hyperparameter is varied, while the data split, affirmative target string, and evaluation judges remain fixed. Two details are important for interpreting the results. For λ=0 in Table A5, no predicted behavior score is available, so performance is evaluated at the final iterate rather than using instance-adaptive optimization. In the threshold-percentile sweep, changing the percentile directly changes τ, which affects both the behavior-guidance loss and instance-adaptive optimization.

Perturbation budget. Table A4 evaluates perturbation budgets of ε=8/255, 16/255, and 32/255. [NAME C03] remains effective across all three budgets, with no setting consistently outperforming the others. Relative to ε=16/255, reducing the budget to 8/255 decreases E-ASR by at most 3.27 points,

[OCR table id=tbl-6.html; page=17]
<table><tr><td rowspan="2">Model</td><td colspan="2">k = 1</td><td colspan="2">k = 5</td><td colspan="2">k = 10</td></tr><tr><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td></tr><tr><td>Qwen2.5-VL-7B</td><td><b>70.99</b></td><td>48.42</td><td>65.86</td><td>45.51</td><td>70.46</td><td><b>49.12</b></td></tr><tr><td>LLaVA-1.5-7B</td><td>75.68</td><td><b>54.63</b></td><td><b>78.84</b></td><td>53.11</td><td>73.72</td><td>51.58</td></tr><tr><td>InternVL3-8B</td><td>72.52</td><td>53.22</td><td>71.76</td><td>52.34</td><td><b>74.05</b></td><td><b>57.58</b></td></tr><tr><td>Llama-3.2-V-11B</td><td>63.03</td><td>41.11</td><td>64.01</td><td><b>44.49</b></td><td><b>65.65</b></td><td>41.66</td></tr></table>

## A-page-0018

target PDF page 18

918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
939
940
941
942
943
944
945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
971

while increasing it to 32/255 improves performance on some models but degrades it on others. Overall, [NAME C03] is relatively insensitive to the choice of perturbation budget within the evaluated range, indicating robustness to this hyperparameter. We therefore use ε=16/255 as the default setting throughout.

Behavioral weight. Table A5 evaluates λ from 0 to 4 at fixed ε. The λ=0 setting corresponds to affirmative-target PGD because the behavior-guidance term is removed. In this case, no predicted behavior score is available, so k_adapt is undefined and performance is evaluated at the final iterate. All positive-λ settings use instance-adaptive optimization. Every positive value of λ improves over the λ=0 baseline across all four models. Among them, λ=4 achieves the highest E-ASR on three of four models and the highest HarmBench ASR on three, and is therefore used as the default.

Sensitivity to λ is assessed across the positive-λ settings, which differ only in the behavior-guidance weight. Across models, the E-ASR range over these settings is 4.80–13.85 points, indicating that [NAME C03] is not narrowly dependent on a specific positive value of λ. The larger difference between λ=0 and the positive-λ settings should not be attributed to λ alone, because these settings also differ in iterate selection. Table 3 isolates these two effects at fixed λ=4, showing E-ASR gains of 11.23–26.50 points from the behavior-guidance term and an additional 3.82–8.29 points from instance-adaptive optimization.

Calibrated threshold. Table A6 varies the percentile used to define τ. Lower percentiles cause instance-adaptive optimization to retain earlier iterates and increase the fraction of inputs that reach the threshold. At Q₀.₈₅, the mean number of optimization steps decreases to 39.60, and 97.90% of inputs reach τ, compared with 95.39 steps and 85.93% at Q₀.₉₉. Attack effectiveness remains broadly stable across the evaluated percentiles, with some model–metric combinations showing slightly higher performance at lower thresholds. These results indicate that the threshold percentile primarily governs an efficiency–effectiveness trade-off rather than determining whether [NAME C03] is effective. We use Q₀.₉₉ as the default because it is the most conservative of the evaluated settings, retaining later iterates and remaining closest to the fixed-budget optimization regime.

Table A4: Sensitivity to the perturbation budget ε, with the clean Baseline included for reference. All [NAME C03] rows use λ=4 with instance-adaptive optimization and differ only in ε. The default setting used in the main text is ε=16/255. Each cell reports E-ASR (%) and HarmBench ASR (%), with higher values indicating better attack performance. Within each column, the best and second-best results among the three perturbation budgets are shown in bold and italic, respectively. n=917.

[tbl-7.html](tbl-7.html)

### D FINE-GRAINED RESULTS ACROSS DATA SOURCES AND HAZARD CATEGORIES

Section 4.3 reports aggregate results over the 917 evaluation inputs. This appendix further breaks down the same results by source dataset (Table A7) and hazard category (Table A8) across all four target VLMs, allowing us to assess whether the aggregate improvements are consistent across subsets. Both tables are computed from the same per-sample scores used in Table 1, and the weighted combination of each breakdown exactly reproduces the corresponding aggregate result.

Across the six source datasets containing more than 80 evaluation inputs, [NAME C03] achieves the highest E-ASR among the three methods in 21 of 24 model–dataset combinations. The three exceptions are concentrated in two settings. Two occur on JailbreakV-28K, which is also the only one of these six datasets where the average E-ASR gain over affirmative-target PGD is small (+1.99 points, compared with +17.12 to +32.86 points on the other five datasets). The remaining exception is

[OCR table id=tbl-7.html; page=18]
<table><tr><td rowspan="2">Method</td><td colspan="2">Qwen2.5-VL-7B</td><td colspan="2">LLaVA-1.5-7B</td><td colspan="2">InternVL3-8B</td><td colspan="2">Llama-3.2-V-11B</td></tr><tr><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td></tr><tr><td>Baseline</td><td>44.17</td><td>30.53</td><td>69.14</td><td>46.35</td><td>44.27</td><td>37.19</td><td>26.28</td><td>16.79</td></tr><tr><td>[NAME C03] (ε=8/255)</td><td>67.72</td><td>47.81</td><td><b>75.90</b></td><td><b>55.18</b></td><td>70.77</td><td>52.67</td><td>63.36</td><td>42.64</td></tr><tr><td>[NAME C03] (ε=16/255)</td><td><b>70.99</b></td><td>48.42</td><td>75.68</td><td>54.63</td><td><b>72.52</b></td><td>53.22</td><td>63.03</td><td>41.11</td></tr><tr><td>[NAME C03] (ε=32/255)</td><td>68.93</td><td><b>49.89</b></td><td>69.79</td><td>51.91</td><td>72.41</td><td><b>54.85</b></td><td><b>66.41</b></td><td><b>43.51</b></td></tr></table>

## A-page-0019

target PDF page 19

Table A5: Sensitivity to the behavior-guidance weight  \( \lambda \) , with the clean Baseline included for reference. All attack settings use  \( \epsilon=16/255 \) . The  \( \lambda=0 \)  setting corresponds to affirmative-target PGD, for which no predicted behavior score is available and performance is therefore evaluated at the final iterate. All positive- \( \lambda \)  settings use instance-adaptive optimization. The default setting used in the main text is  \( \lambda=4 \)  (shaded). Each cell reports E-ASR (%) and HarmBench ASR (%), with higher values indicating better attack performance. Within each column, the best and second-best results among the five attack settings are shown in bold and italic, respectively. n=917.

[tbl-8.html](tbl-8.html)

Table A6: Sensitivity to the percentile used to define the calibrated threshold  \( \tau \) , with  \( \lambda=4 \)  fixed. Mean steps denotes the mean number of optimization steps to the retained iterate, pooled across the four target VLMs, while Reached  \( \tau \)  denotes the fraction of inputs that reach the threshold within the optimization budget, averaged across models.  \( Q_{0.99} \)  is the default setting used in the main text. Within each column, the best and second-best results among the three threshold settings are shown in bold and italic, respectively. Higher values are better for E-ASR, HarmBench ASR, and Reached  \( \tau \) , while lower values are better for Mean steps. n=917 per model.

[tbl-9.html](tbl-9.html)

FigStep on LLaVA-1.5, where the clean condition already outperforms both attacks. The two smallest sources, MLLMGuard  \( (n=7) \)  and SIUO  \( (n=3) \) , are included for completeness. At these sample sizes, a single response changes the rate by 14.29 and 33.33 points, respectively, and exact ties are marked identically.

The hazard-category breakdown shows a similar pattern. [NAME C03] achieves the highest E-ASR in 40 of the 44 category-model combinations and improves over affirmative-target PGD on average in all eleven categories. Performance nevertheless varies across categories. S7 Intellectual Property shows the smallest average E-ASR gain (+1.95 points) and accounts for two of the four exceptions, while S4 Defamation gains 19.62 E-ASR points but shows essentially no improvement in HarmBench ASR (-0.32 points). In both categories, specificity and convincingness provide relatively limited separation between compliant and refusal-like responses, consistent with the response-behavior analysis in Section 4.7. The largest average E-ASR gains occur for S1 Violent Crimes (+28.55 points) and S11 Sexual Content (+27.67 points), where successful responses can be more concretely actionable.

972
973
974
975
976
977
978
979
980
981
982
983
984
985
986
987
988
989
990
991
992
993
994
995
996
997
998
999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025

[OCR table id=tbl-8.html; page=19]
<table><tr><td rowspan="2">Method</td><td colspan="2">Qwen2.5-VL-7B</td><td colspan="2">LLaVA-1.5-7B</td><td colspan="2">InternVL3-8B</td><td colspan="2">Llama-3.2-V-11B</td></tr><tr><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td></tr><tr><td>Baseline</td><td>44.17</td><td>30.53</td><td>69.14</td><td>46.35</td><td>44.27</td><td>37.19</td><td>26.28</td><td>16.79</td></tr><tr><td>PGD (λ=0)</td><td>54.31</td><td>38.17</td><td>42.42</td><td>29.99</td><td>53.00</td><td>33.70</td><td>45.15</td><td>28.03</td></tr><tr><td>[NAME C03] (λ=0.5)</td><td>66.30</td><td>48.20</td><td>61.83</td><td>45.47</td><td>67.72</td><td>52.67</td><td>58.45</td><td>38.39</td></tr><tr><td>[NAME C03] (λ=1.0)</td><td>64.67</td><td>44.38</td><td>63.69</td><td>47.87</td><td>71.10</td><td>53.98</td><td>62.16</td><td>40.68</td></tr><tr><td>[NAME C03] (λ=2)</td><td>69.14</td><td>47.44</td><td>68.48</td><td>51.25</td><td>70.88</td><td>52.13</td><td>64.67</td><td>39.15</td></tr><tr><td>[NAME C03] (λ=4)</td><td>70.99</td><td>48.42</td><td>75.68</td><td>54.63</td><td>72.52</td><td>53.22</td><td>63.03</td><td>41.11</td></tr></table>

[OCR table id=tbl-9.html; page=19]
<table><tr><td rowspan="2">Threshold \( \tau \)</td><td colspan="2">Qwen2.5-VL-7B</td><td colspan="2">LLaVA-1.5-7B</td><td colspan="2">InternVL3-8B</td><td colspan="2">Llama-3.2-V-11B</td><td colspan="2">Adaptive optimization</td></tr><tr><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>Mean steps</td><td>Reached \( \tau \)(%)</td></tr><tr><td>\( {Q}_{0.85} \)</td><td>66.52</td><td>48.09</td><td>74.48</td><td>52.45</td><td>71.10</td><td>54.09</td><td>57.58</td><td>37.95</td><td>39.60</td><td>97.90</td></tr><tr><td>\( {Q}_{0.90} \)</td><td>66.09</td><td>47.87</td><td>74.48</td><td>55.62</td><td>70.67</td><td>54.53</td><td>60.52</td><td>40.46</td><td>54.25</td><td>94.74</td></tr><tr><td>\( {Q}_{0.99} \)</td><td>70.99</td><td>48.42</td><td>75.68</td><td>54.63</td><td>72.52</td><td>53.22</td><td>63.03</td><td>41.11</td><td>95.39</td><td>85.93</td></tr></table>

## A-page-0020

target PDF page 20

1026
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
1062
1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079

Table A7: Per source dataset breakdown of the results in Table 1. The 917 evaluation inputs are grouped by source dataset, with the number of inputs shown in # Samples. Each cell reports E-ASR (%) and HarmBench ASR (%) for the clean Baseline, affirmative-target PGD (λ=0), and [NAME C03] (λ=4, instance-adaptive optimization). For each dataset-model combination, the best and second-best results among the three methods are shown in bold and italic, respectively. Exact ties receive the same formatting, while values of 0.00 are left unmarked. Results for MLLMGuard (n=7) and SIUO (n=3) are highly sensitive to individual samples and should not be interpreted as reliable per-dataset conclusions.

[tbl-10.html](tbl-10.html)

[OCR table id=tbl-10.html; page=20]
<table><tr><td rowspan="2">Benchmark</td><td rowspan="2"># Samples</td><td rowspan="2">Method</td><td colspan="2">Qwen2.5-VL-7B</td><td colspan="2">LLaVA-1.5-7B</td><td colspan="2">InternVL3-8B</td><td colspan="2">Llama-3.2-V-11B</td></tr><tr><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td></tr><tr><td rowspan="3">SPA-VL</td><td rowspan="3">276</td><td>Baseline</td><td>40.22</td><td>16.30</td><td>64.13</td><td>31.88</td><td>44.57</td><td>23.19</td><td>35.51</td><td>15.94</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>44.93</td><td>23.19</td><td>35.14</td><td>25.36</td><td>46.38</td><td>22.83</td><td>45.65</td><td>25.36</td></tr><tr><td>[NAME C03]</td><td>60.51</td><td>19.57</td><td>73.55</td><td>36.59</td><td>73.91</td><td>37.68</td><td>61.59</td><td>35.14</td></tr><tr><td rowspan="3">New</td><td rowspan="3">197</td><td>Baseline</td><td>49.24</td><td>41.62</td><td>76.65</td><td>73.60</td><td>49.75</td><td>51.78</td><td>22.84</td><td>17.77</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>59.39</td><td>48.73</td><td>52.79</td><td>41.62</td><td>48.73</td><td>31.47</td><td>47.72</td><td>31.98</td></tr><tr><td>[NAME C03]</td><td>77.16</td><td>72.59</td><td>82.23</td><td>77.66</td><td>75.13</td><td>72.59</td><td>65.48</td><td>44.16</td></tr><tr><td rowspan="3">FigStep</td><td rowspan="3">130</td><td>Baseline</td><td>58.46</td><td>36.92</td><td>75.38</td><td>42.31</td><td>63.85</td><td>56.15</td><td>23.08</td><td>13.08</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>70.00</td><td>53.85</td><td>52.31</td><td>26.92</td><td>78.46</td><td>53.85</td><td>32.31</td><td>26.15</td></tr><tr><td>[NAME C03]</td><td>85.38</td><td>63.85</td><td>70.00</td><td>52.31</td><td>82.31</td><td>63.85</td><td>63.85</td><td>45.38</td></tr><tr><td rowspan="3">JailbreakV-28K</td><td rowspan="3">113</td><td>Baseline</td><td>17.70</td><td>23.89</td><td>50.44</td><td>50.44</td><td>18.58</td><td>33.63</td><td>13.27</td><td>12.39</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>56.64</td><td>41.59</td><td>53.98</td><td>49.56</td><td>51.33</td><td>46.90</td><td>44.25</td><td>32.74</td></tr><tr><td>[NAME C03]</td><td>54.87</td><td>50.44</td><td>63.72</td><td>61.95</td><td>52.21</td><td>53.98</td><td>43.36</td><td>33.63</td></tr><tr><td rowspan="3">VLGuard</td><td rowspan="3">105</td><td>Baseline</td><td>50.48</td><td>30.48</td><td>70.48</td><td>25.71</td><td>41.90</td><td>25.71</td><td>32.38</td><td>25.71</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>43.81</td><td>24.76</td><td>20.95</td><td>12.38</td><td>44.76</td><td>26.67</td><td>48.57</td><td>25.71</td></tr><tr><td>[NAME C03]</td><td>75.24</td><td>28.57</td><td>77.14</td><td>37.14</td><td>70.48</td><td>29.52</td><td>66.67</td><td>26.67</td></tr><tr><td rowspan="3">MM-SafetyBench</td><td rowspan="3">86</td><td>Baseline</td><td>52.33</td><td>50.00</td><td>83.72</td><td>59.30</td><td>39.53</td><td>40.70</td><td>22.09</td><td>19.77</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>61.63</td><td>53.49</td><td>41.86</td><td>20.93</td><td>60.47</td><td>37.21</td><td>59.30</td><td>30.23</td></tr><tr><td>[NAME C03]</td><td>87.21</td><td>86.05</td><td>93.02</td><td>77.91</td><td>81.40</td><td>74.42</td><td>83.72</td><td>77.91</td></tr><tr><td rowspan="3">MLLMGuard</td><td rowspan="3">7</td><td>Baseline</td><td>28.57</td><td>14.29</td><td>57.14</td><td>28.57</td><td>42.86</td><td>14.29</td><td>0.00</td><td>0.00</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>28.57</td><td>14.29</td><td>14.29</td><td>14.29</td><td>28.57</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>[NAME C03]</td><td>42.86</td><td>28.57</td><td>57.14</td><td>28.57</td><td>28.57</td><td>14.29</td><td>57.14</td><td>14.29</td></tr><tr><td rowspan="3">SIUO</td><td rowspan="3">3</td><td>Baseline</td><td>33.33</td><td>66.67</td><td>33.33</td><td>0.00</td><td>0.00</td><td>33.33</td><td>0.00</td><td>0.00</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>33.33</td><td>0.00</td><td>0.00</td><td>0.00</td><td>33.33</td><td>33.33</td><td>0.00</td><td>0.00</td></tr><tr><td>[NAME C03]</td><td>66.67</td><td>33.33</td><td>33.33</td><td>33.33</td><td>33.33</td><td>33.33</td><td>33.33</td><td>0.00</td></tr></table>

## A-page-0021

target PDF page 21

1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133

Table A8: Per hazard category breakdown of the results in Table 1. The 917 evaluation inputs are grouped by ELITE hazard category, with the number of inputs shown in # Samples. The evaluated conditions and highlighting follow Table A7. [NAME C03] achieves the highest E-ASR in 40 of the 44 category–model combinations and improves over affirmative-target PGD on average across all eleven hazard categories.

[tbl-11.html](tbl-11.html)

[OCR table id=tbl-11.html; page=21]
<table><tr><td rowspan="2">Taxonomy</td><td rowspan="2"># Samples</td><td rowspan="2">Method</td><td colspan="2">Qwen2.5-VL-7B</td><td colspan="2">LLaVA-1.5-7B</td><td colspan="2">InternVL3-8B</td><td colspan="2">Llama-3.2-V-11B</td></tr><tr><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td><td>E-ASR</td><td>ASR</td></tr><tr><td rowspan="3">S1 Violent Crimes</td><td rowspan="3">141</td><td>Baseline</td><td>46.81</td><td>24.11</td><td>73.05</td><td>40.43</td><td>46.81</td><td>28.37</td><td>33.33</td><td>12.77</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>56.03</td><td>34.75</td><td>45.39</td><td>26.95</td><td>53.90</td><td>26.95</td><td>45.39</td><td>25.53</td></tr><tr><td>[NAME C03]</td><td>76.60</td><td>39.72</td><td>89.36</td><td>46.81</td><td>76.60</td><td>43.26</td><td>72.34</td><td>35.46</td></tr><tr><td rowspan="3">S2 Non-Violent Crimes</td><td rowspan="3">147</td><td>Baseline</td><td>55.10</td><td>44.22</td><td>82.31</td><td>70.75</td><td>52.38</td><td>46.94</td><td>29.93</td><td>21.09</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>67.35</td><td>52.38</td><td>62.59</td><td>40.82</td><td>74.15</td><td>49.66</td><td>57.14</td><td>42.86</td></tr><tr><td>[NAME C03]</td><td>91.16</td><td>76.87</td><td>87.76</td><td>76.19</td><td>88.44</td><td>77.55</td><td>74.15</td><td>61.22</td></tr><tr><td rowspan="3">S3 Sex Crimes</td><td rowspan="3">56</td><td>Baseline</td><td>33.93</td><td>16.07</td><td>73.21</td><td>60.71</td><td>33.93</td><td>28.57</td><td>21.43</td><td>16.07</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>55.36</td><td>41.07</td><td>53.57</td><td>41.07</td><td>60.71</td><td>32.14</td><td>46.43</td><td>33.93</td></tr><tr><td>[NAME C03]</td><td>67.86</td><td>55.36</td><td>83.93</td><td>66.07</td><td>71.43</td><td>51.79</td><td>58.93</td><td>33.93</td></tr><tr><td rowspan="3">S4 Defamation</td><td rowspan="3">79</td><td>Baseline</td><td>40.51</td><td>27.85</td><td>60.76</td><td>30.38</td><td>41.77</td><td>26.58</td><td>21.52</td><td>6.33</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>46.84</td><td>34.18</td><td>27.85</td><td>25.32</td><td>37.97</td><td>24.05</td><td>46.84</td><td>32.91</td></tr><tr><td>[NAME C03]</td><td>51.90</td><td>25.32</td><td>56.96</td><td>25.32</td><td>69.62</td><td>35.44</td><td>59.49</td><td>29.11</td></tr><tr><td rowspan="3">S5 Specialized Advice</td><td rowspan="3">65</td><td>Baseline</td><td>64.62</td><td>32.31</td><td>66.15</td><td>23.08</td><td>50.77</td><td>52.31</td><td>43.08</td><td>21.54</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>53.85</td><td>32.31</td><td>24.62</td><td>6.15</td><td>47.69</td><td>29.23</td><td>32.31</td><td>15.38</td></tr><tr><td>[NAME C03]</td><td>70.77</td><td>29.23</td><td>67.69</td><td>23.08</td><td>64.62</td><td>47.69</td><td>61.54</td><td>27.69</td></tr><tr><td rowspan="3">S6 Privacy</td><td rowspan="3">62</td><td>Baseline</td><td>45.16</td><td>35.48</td><td>79.03</td><td>54.84</td><td>50.00</td><td>43.55</td><td>24.19</td><td>24.19</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>72.58</td><td>51.61</td><td>54.84</td><td>32.26</td><td>51.61</td><td>25.81</td><td>43.55</td><td>19.35</td></tr><tr><td>[NAME C03]</td><td>80.65</td><td>72.58</td><td>77.42</td><td>62.90</td><td>77.42</td><td>66.13</td><td>64.52</td><td>48.39</td></tr><tr><td rowspan="3">S7 Intellectual Property</td><td rowspan="3">64</td><td>Baseline</td><td>21.88</td><td>29.69</td><td>51.56</td><td>53.12</td><td>21.88</td><td>28.12</td><td>20.31</td><td>14.06</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>59.38</td><td>46.88</td><td>57.81</td><td>48.44</td><td>50.00</td><td>51.56</td><td>48.44</td><td>29.69</td></tr><tr><td>[NAME C03]</td><td>56.25</td><td>45.31</td><td>73.44</td><td>65.62</td><td>51.56</td><td>54.69</td><td>42.19</td><td>32.81</td></tr><tr><td rowspan="3">S8 Indiscriminate Weapons</td><td rowspan="3">69</td><td>Baseline</td><td>59.42</td><td>36.23</td><td>76.81</td><td>53.62</td><td>65.22</td><td>53.62</td><td>34.78</td><td>26.09</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>56.52</td><td>43.48</td><td>40.58</td><td>31.88</td><td>59.42</td><td>39.13</td><td>53.62</td><td>27.54</td></tr><tr><td>[NAME C03]</td><td>75.36</td><td>53.62</td><td>78.26</td><td>68.12</td><td>86.96</td><td>68.12</td><td>71.01</td><td>52.17</td></tr><tr><td rowspan="3">S9 Hate</td><td rowspan="3">103</td><td>Baseline</td><td>33.98</td><td>19.42</td><td>64.08</td><td>25.24</td><td>33.98</td><td>23.30</td><td>16.50</td><td>10.68</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>36.89</td><td>20.39</td><td>28.16</td><td>20.39</td><td>46.60</td><td>30.10</td><td>43.69</td><td>23.30</td></tr><tr><td>[NAME C03]</td><td>65.05</td><td>30.10</td><td>66.99</td><td>40.78</td><td>66.99</td><td>33.98</td><td>54.37</td><td>30.10</td></tr><tr><td rowspan="3">S10 Self-Harm</td><td rowspan="3">56</td><td>Baseline</td><td>28.57</td><td>39.29</td><td>66.07</td><td>58.93</td><td>35.71</td><td>51.79</td><td>10.71</td><td>17.86</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>42.86</td><td>37.50</td><td>37.50</td><td>37.50</td><td>48.21</td><td>39.29</td><td>30.36</td><td>19.64</td></tr><tr><td>[NAME C03]</td><td>62.50</td><td>51.79</td><td>67.86</td><td>64.29</td><td>57.14</td><td>58.93</td><td>55.36</td><td>48.21</td></tr><tr><td rowspan="3">S11 Sexual Content</td><td rowspan="3">75</td><td>Baseline</td><td>41.33</td><td>28.00</td><td>53.33</td><td>36.00</td><td>44.00</td><td>34.67</td><td>24.00</td><td>18.67</td></tr><tr><td>PGD (\( \mathcal{L}_{attack} \))</td><td>44.00</td><td>25.33</td><td>21.33</td><td>20.00</td><td>34.67</td><td>17.33</td><td>33.33</td><td>24.00</td></tr><tr><td>[NAME C03]</td><td>58.67</td><td>45.33</td><td>62.67</td><td>60.00</td><td>64.00</td><td>45.33</td><td>58.67</td><td>42.67</td></tr></table>
