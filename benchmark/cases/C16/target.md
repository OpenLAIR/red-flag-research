# [TITLE C16]

## A-page-0001

target PDF page 1

# [TITLE C16]

## Anonymous authors

Paper under double-blind review

![img-0.jpeg](img-0.jpeg)

Figure 1: [NAME C16] is a real-time interactive world model enabling versatile controls with long-horizon consistency. Top: It supports flexible interactions, including navigation controls and complex semantic events. Middle: It executes multi-turn interactions to achieve coherent storytelling. Bottom: It maintains long-horizon consistency under complex navigation controls.

## ABSTRACT

Interactive world models require responding in real time to versatile controls and maintaining long-horizon consistency. However, modeling heterogeneous controls remains difficult, while explosive contexts and unstable distillation impede achieving both long-horizon consistency and real-time responsiveness. In this paper, we present [NAME C16], an interactive world model that couples a factorized hybrid control interface with a co-design of compressed memory and stable distillation. 1) Our factorized hybrid control interface integrates frame-aligned action control with structured semantic control that explicitly disentangles scene appearance, character identity, and dynamic semantic events, thereby facilitating effective control learning. 2) To achieve efficient long-horizon modeling, we compress historical contexts into compact memory tokens shared by the autoregressive student and the bidirectional teacher. This design enables clip-wise, memory-conditioned score evaluation instead of jointly processing an entire long rollout, substantially reducing distillation overhead. 3) We further propose Stable Forcing, which initializes the autoregressive student via a few-step strategy and leverages full-rollout replay to preserve the quality of long-horizon rollouts, ensuring robust and stable distillation. Extensive experiments demonstrate the strong generalizability of our model and its superior performance compared to existing methods.

Reviewers: please read the Reviewer Guidelines (cit: cc:Conferences/2027/ReviewerGuidelines) and the AI Policy for Reviewers (cit: cc:Conferences/2027/AIPolicyForReviewers). If you used AI to expand, edit, or polish your review, please provide the input text to the LLM. Better still, consider skipping the LLM and submitting your original text; we, and the authors, are much more interested in your unedited thoughts than in what an LLM has to say. AI-assisted or not, you are putting your name and reputation behind your review: LLM-generated falsehoods, hallucinations or misrepresentations are subject to disciplinary action, which may include desk-rejecting all papers you have authored.

000
001
002
003
004
005
006
007
008
009
010
011
012
013
014
015
016
017
018
019
020
021
022
023
024
025
026
027
028
029
030
031
032
033
034
035
036
037
038
039
040
041
042
043
044
045
046
047
048
049
050
051
052
053

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

# 1 INTRODUCTION

Interactive world models (Parker-Holder et al., 2025; Sun et al., 2026; He et al., 2025; Team et al., 2026d; Alibaba, 2026; Hong et al., 2025; Xu et al., 2026; Jiang et al., 2026; Zhu et al., 2026a) are beginning to transform video generators (Wan et al., 2025; Wu et al., 2025; Deepmind, 2025) from passive content-creation systems into interactive environments that evolve in response to user input. Such models have the potential to serve as general-purpose simulators (Agarwal et al., 2026; Brooks et al., 2024), allowing users to explore, interact with, and reshape the generated environments while providing scalable data generators and policy evaluators for embodied agents (Wiedemer et al., 2025; Team et al., 2025). Realizing these applications requires world models to support versatile controls, preserve coherent world states over long horizons, and operate in real time.

Controllability represents a primary challenge for world models. Early efforts (Sun et al., 2026; He et al., 2025; Team et al., 2026d) focused on navigation-oriented controls, lacking richer mechanisms for interacting with the environment. Although recent works (Team et al., 2026a; Gao et al., 2026) attempt to accommodate increasingly diverse interactive events, effectively integrating these heterogeneous inputs remains challenging because these control signals inherently operate across disparate semantic granularities and temporal horizons. Specifically, camera motion and character locomotion demand precise, frame-aligned control, whereas complex interactive events are more naturally expressed via high-level semantic commands spanning longer temporal horizons. Moreover, control signals must be disentangled from content factors such as scene appearance and character identity. Otherwise, the model may conflate visual appearance, spatial movement, and occurring events, leading to ambiguous supervision and unreliable responses.

The second challenge lies in co-designing memory and distillation. Existing methods (Team et al., 2026d; Hong et al., 2025; Xu et al., 2026; Zhu et al., 2026a) often rely on full-context bidirectional models as teachers. However, computational costs scale quadratically with video length, which not only hinders long-horizon modeling but, more crucially, makes score evaluation during distillation prohibitively expensive. Moreover, preserving long-horizon consistency during distillation presents additional challenges. This process typically requires the student model to autoregressively generate long video sequences (Hong et al., 2025; Sun et al., 2026; Xu et al., 2026; Team et al., 2026d), but due to error accumulation and few-step sampling, the student's generation distribution diverges significantly from that of the teacher, thereby rendering distillation unstable and severely degrading generation quality. Therefore, world models require a co-design in which memory is sufficiently compact to enable efficient long-horizon modeling and distillation is sufficiently stable to preserve long-horizon consistency.

In this paper, we introduce [NAME C16], a real-time interactive world model that combines factorized hybrid control interface, distillation-oriented compressed memory, and stable long-horizon distillation. Specifically, we propose a factorized hybrid control interface that explicitly disentangles low-level movements, high-level semantic interactions, and visual content factors. Low-level movements, e.g., camera motion and third-person character locomotion, are precisely modulated via frame-aligned action control. Concurrently, to govern high-level semantic interactions and content factors, we design a structured semantic control that partitions signals into three decoupled fields, i.e., scene, character, and event, where each field governs a distinct concept within the world. By disentangling these signals, the model learns reusable combinations across the heterogeneous controls while retaining the precise responsiveness required for world models.

Then, we co-design the memory and distillation. For the memory mechanism, we compress the generated history into compact memory tokens, substantially reducing the computational cost for long-horizon modeling. Crucially, this design bypasses score evaluations across the full-resolution rollouts during distillation. By partitioning long-horizon rollouts into local temporal clips conditioned on compact memory tokens, we can compute scores independently per clip, ensuring scalable and computationally tractable distillation. For distillation, we propose Stable Forcing, a stable framework tailored for long-horizon distillation. We first warm-start the autoregressive student via a few-step initialization scheme inspired by PDD (Shaul et al., 2026), yielding a well-behaved few-step student. This initialization ensures that the student's rollout distribution closely aligns with that of the teacher over long horizons, thereby stabilizing subsequent distribution distillation. Building on this starting point, we perform distribution-matching distillation to enhance long-horizon consistency and mitigate exposure bias. In this stage, we introduce full-rollout replay to decouple

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

long-horizon rollouts from gradient backpropagation. During the forward rollout phase, each chunk undergoes full few-step sampling to maintain fidelity and bolster stability. Meanwhile, a random intermediate step is recorded and replayed with gradients during the backward pass. Combining our initialization with full-rollout replay preserves rollout quality over long horizons, thereby achieving stable and robust distillation.

Taken together, our model demonstrates remarkable generalization across different scenes and characters. As shown in Fig. 1, it not only supports versatile, multi-turn interactive controls, but also preserves geometric consistency over long horizons. Moreover, extensive quantitative and qualitative experiments validate the effectiveness of our methods, demonstrating superior performance compared to existing methods.

## 2 RELATED WORK

Interactive World Models. Interactive world models generate future visual frames conditioned on previous observations and current actions, enabling users or embodied agents to interact with the environment. Recent world models have substantially expanded environmental diversity (Zhang et al., 2025; He et al., 2025; Li et al., 2025; Team et al., 2026b; Mao et al., 2025; Jiang et al., 2026; Team, 2025; 2026), long-horizon consistency (Sun et al., 2026; Hong et al., 2025; Xu et al., 2026; Team et al., 2026d; Wang et al., 2026c; Team et al., 2026c), and the range of supported controls (Parker-Holder et al., 2025; Gao et al., 2026; Team et al., 2026a; Mao et al., 2026; Alibaba, 2026; Tang et al., 2025). WorldPlay (Sun et al., 2026), Lingbot-World (Team et al., 2026d), and Wonder (Xu et al., 2026) utilize camera poses, discrete keyboard inputs, or pixel-space coordinate field as control signals to govern viewpoint transformation and character movement. Lingbot-World-V2 (Gao et al., 2026) and AlayaWorld (Team et al., 2026a) introduce language-driven events to further enable richer interactive controls. However, these control signals are inherently heterogeneous, making unified and effective representation particularly challenging. Moreover, existing methods model long-horizon consistency via retrieval (Yu et al., 2025; Xiao et al., 2026), sparse attention (Xu et al., 2026), or explicit 3D representations (Team et al., 2026c;a), while treating distillation as an isolated module. In contrast, our method co-designs the memory mechanism and distillation, improving both training efficiency and distillation stability.

Distillation. Distillation accelerates diffusion models by reducing the number of function evaluations. One representative line of studies aggregates multi-step instantaneous velocity into single-step average velocity. For instance, MeanFlow (Geng et al., 2026) derives the relationship between instantaneous and average velocities, whereas rCM (Zheng et al., 2026b), AnyFlow (Gu et al., 2026), and TiM (Wang et al., 2026b) implement a parallelism-compatible JVP kernel or differential derivation to scale this approach to large-scale models. PiFlow (Chen et al., 2026) and PDD (Shaul et al., 2026) further optimize trajectory learning to estimate average velocities more efficiently, achieving strong performance in bidirectional model distillation. Another major paradigm performs distribution matching distillation (Yin et al., 2024b;a; 2025; Zheng et al., 2026a; Zhu et al., 2026b; Huang et al., 2026), aligning the generation distribution of a few-step student with that of a multi-step teacher. This paradigm is widely adopted for interactive world models because it accelerates sampling, mitigates exposure bias, and inherits desirable properties from the teacher, such as long-horizon consistency. However, when the student performs few-step long-horizon rollouts, its generation distribution diverges significantly from that of the teacher, making distillation highly unstable.

## 3 METHOD

Our goal is to construct a real-time interactive world model $N_{\theta}(x_t|x_{<t}, A_{\le t})$ parameterized by $\theta$ that supports versatile controls while maintaining long-horizon consistency. The model generates next chunk $x_t \in \mathbb{R}^{T \times H \times W}$ based on past observations $x_{<t} = \{x_{t-1}, ..., x_0\}$, controls $A_{<t} = \{A_{t-1}, ..., A_0\}$, and current control signal $A_t$. We first introduce our factorized hybrid control interface in Sec. 3.1, which disentangles heterogeneous inputs to support diverse interactions. In Sec. 3.2, we present our distillation-oriented compressed memory mechanism, enabling efficient long-horizon modeling and teacher supervision. Finally, we detail Stable Forcing in Sec. 3.3, a stable long-horizon distillation framework that distills a many-step autoregressive model into a few-step model while preserving long-horizon consistency. Fig. 2 illustrates the overview of our model.

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

![img-1.jpeg](img-1.jpeg)

Figure 2: Overview of [NAME C16]. We employ factorized hybrid control interface to decouple heterogeneous inputs into frame-aligned action control and structured semantic control, ensuring accurate interactive responses. Concurrently, a history compressor abstracts past contexts into compact memory tokens to achieve efficient long-horizon inference.

### 3.1 FACTORIZED HYBRID CONTROL INTERFACE

Interactive world models require versatile responsiveness to heterogeneous controls, which often exhibit varying levels of abstraction. Camera motion and character locomotion demand precise, frame-aligned signals, whereas complex interactions and content factors are more naturally expressed via high-level semantic instructions. Therefore, we propose a factorized hybrid control interface that disentangles low-level movements, high-level semantic interactions, and visual content factors. Specifically, each control signal is represented as $A_t = \{a_t, d_t\}$, where $a_t$ denotes frame-aligned action control and $d_t$ denotes structured semantic control.

Frame-aligned Action Control. Our low-level movements $a_t$ consist of continuous camera pitch and yaw angles, discrete longitudinal and lateral movements, the camera perspective, and a special action (i.e., jumping). We separately embed the continuous and discrete components and combine them into a unified action representation,

$$e_t = E(\text{continuous}) + \mathbf{e}[\text{discrete}], \tag{1}$$

where $E$ is an MLP for continuous signals and $\mathbf{e}$ denotes the learnable embeddings for the discrete signals. The resulting action representation is aligned with the corresponding visual tokens and injected before the feed-forward network (FFN) in each Transformer block,

$$\bar{h}_t = h_t + F([h_t \oplus e_t]), \tag{2}$$

where $F$ is an auxiliary MLP, $h_t$ denotes the hidden states, and $\oplus$ means channel concatenation.

Structured Semantic Control. High-level semantic control involves diverse interactions and visual content factors that often span longer temporal horizons, making it challenging to represent with low-dimensional vectors. Therefore, we utilize structured caption $d_t$ as the semantic control signals. Specifically, $d_t$ encapsulates visual content factors (i.e., scene and character identity) as well as dynamic semantic events,

$$d_t = (d_{\text{scene}}, d_{\text{character}}, d_{\text{event}}). \tag{3}$$

Here, the scene field $d_{\text{scene}}$ describes the environmental content, including spatial layout, objects, illumination, and visual style. $d_{\text{character}}$ specifies the persistent identity and appearance of the controlled entity. $d_{\text{event}}$ describes the semantic change associated with the current event, such as object manipulation, environmental changes, and object appearance.

### 3.2 DISTILLATION-ORIENTED COMPRESSED MEMORY

Long-horizon world modeling requires access to historical information beyond a limited local context. A straightforward approach is to retain the entire full-resolution contexts (Team et al., 2026d;

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

Hong et al., 2025). However, this causes context length to scale linearly during autoregressive rollout, rapidly increasing inference latency and complicating long-horizon modeling. Moreover, this computational burden is further amplified during distillation, where the full-context bidirectional teacher is used to evaluate long student rollouts to provide supervision. To this end, we design a compressed memory mechanism inspired by Zhang et al. (2026a), shared across long-horizon modeling and distillation. This enables efficient context conditioning while keeping teacher evaluation during distillation computationally tractable.

Instead of conditioning the model directly on the full-resolution contexts, we employ a learnable history compressor $\mathcal{C}_{\phi}$ to encode the history context into a compact sequence of memory tokens:

$$m_{<t} = [x_{\text{sink}}; x_{\text{cmp}} = \mathcal{C}_{\phi}(x_{<t}, x_{<t}^{\text{lr}}); x_{\text{tmp}}], \tag{4}$$

where $[; ;]$ denotes sequence concatenation, $x_{\text{sink}}$ denotes sink tokens providing a stable reference, $x_{\text{tmp}}$ represents adjacent temporal tokens that enforce temporal consistency, and $x_{<t}^{\text{lr}} \in \mathbb{R}^{\frac{T}{t} \times \frac{H}{t} \times \frac{W}{t}}$ denotes the low-resolution, low-frame-rate video latent encoded by the VAE, with $l = 2$ and $s = 4$ representing the temporal and spatial down-sampling factors, respectively. For the history compressor $\mathcal{C}_{\phi}$, we adopt a dual-branch design (Zhang et al., 2026a). Specifically, the coarse branch processes $x_{<t}^{\text{lr}}$ through the DiT's patchifier to produce coarse features, while the fine branch passes $x_{<t}$ through a downsample module to yield residual fine features. This dual-branch representation provides both high-level semantic information and fine-grained visual details for subsequent generation. Compared to full-resolution contexts, our memory compression mechanism reduces the sequence length by a factor of approximately $l \cdot s^2 = 32$, significantly reducing computational overhead.

![img-2.jpeg](img-2.jpeg)

Figure 3: Causal attention mask for compressed memory training.

Given a long training video, we partition it into a compressed historical context and a target clip $x_{[t:t+L]}$. For the causal autoregressive student $N_{\theta}$, we employ teacher forcing with a causal attention mask (illustrated in Fig. 3) to maintain temporal causality and follow the flow matching objective (Lipman et al., 2023),

$$\mathcal{L}_{\text{student}} = \mathbb{E}_{x, \epsilon, \sigma} \left\| N_{\theta} \left( x_{[t:t+L]}^{\sigma}, \sigma, m_{<t+L}, A_{\le t+L} \right) - (\epsilon - x_{[t:t+L]}) \right\|^2, \tag{5}$$

where $\epsilon \sim \mathcal{N}(0, \mathbf{I})$ denotes Gaussian noise and $\sigma$ represents the diffusion noise level. Concurrently, the bidirectional teacher model is trained without the causal attention mask. By applying our proposed memory mechanism to both student and teacher models, we can efficiently model long-horizon consistency. Moreover, it enables long student rollouts to be partitioned into smaller clips for individual teacher evaluation, significantly reducing computational overhead during distillation.

### 3.3 STABLE FORCING

Self Forcing (Huang et al., 2026) has emerged as an effective approach for distilling autoregressive video diffusion models, as it simultaneously reduces sampling steps and mitigates error accumulation. However, extending it to long-horizon rollout introduces new challenges. Performing long-horizon student rollouts with few sampling steps causes errors to compound rapidly across chunks, driving the student's generation distribution away from the teacher's and leading to unstable training. Additionally, evaluating scores over long rollouts using full-context teacher models demands substantial computational resources and GPU memory. To address these challenges, we introduce Stable Forcing as shown in Fig. 4, a long-horizon distillation framework designed to achieve stable training via few-step initialization, full-rollout replay, and efficient score evaluation.

Few-step Initialization. Stable long-horizon distillation requires the student to produce meaningful rollouts under few-step sampling. To establish a reliable few-step initialization, we extend PDD (Shaul et al., 2026) to our memory-augmented autoregressive student model. Specifically, PDD discretizes the diffusion noise schedule into $K$ blocks, where each block $i$ contains $C$ sub-intervals $\{\sigma_0^i, \ldots, \sigma_{C-1}^i\}$. A parallel decoder then predicts the mean velocities $u_0, \ldots, u_{C-1}$ across

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

Figure 4: Overview of Stable Forcing. It integrates few-step initialization, full-rollout replay, and efficient score evaluation to achieve efficient and stable long-horizon distillation.

adjacent intervals within a block in a single forward pass. The training objective is,

$$\mathcal{L}_{\mathrm{PDD}} = \mathbb{E}_{k \in [0, C-1]} \left\| u_k - \mathrm{sg}(N_\theta(x_t^{\sigma_k^i}, \sigma_k^i, m_{<t}, A_{\le t})) \right\|^2, \tag{6}$$

where $x_t^{\sigma_k^i}$ is computed via parallel decoding sampling and $\mathrm{sg}(\cdot)$ denotes the stop-gradient operator. By predicting multiple consecutive denoising intervals in parallel, it reduces the number of network evaluations and provides a reliable few-step initialization to stabilize subsequent long-horizon distribution matching distillation.

**Full-rollout Replay.** To further enhance the stability of distribution matching distillation, we decouple the rollout phase from gradient backpropagation. Specifically, during the rollout phase, each chunk performs full few-step sampling, and only its final prediction is incorporated into subsequent chunk generation and score evaluation. Simultaneously, we cache a randomly selected intermediate denoising timestep for each chunk and replay it with gradients after computing the score. This strategy not only improves rollout quality but also ensures supervision across denoising timesteps.

**Efficient Score Evaluation.** After the student model generates a long rollout $x_{[0:BL]}$, we perform an efficient score evaluation to obtain the distribution-matching signal. Specifically, the rollout is partitioned into $B$ clips. For each clip $x_{[iL:(i+1)L]}$, the preceding chunks are encoded into compact memory tokens $m_{<iL}$ and the real and fake scores are evaluated using the teacher model $v$ as follows,

$$s_{\mathrm{fake/real}} = v(x_{[iL:(i+1)L]}^\sigma, \sigma, m_{<iL}, A_{\le(i+1)L}). \tag{7}$$

In this manner, we preserve long-horizon supervision while reducing the sequence length processed by the score model, thereby achieving more efficient score evaluation.

## 4 EXPERIMENTS

**Dataset.** Our training corpus comprises two distinct subsets: a spatial navigation dataset and an interactive event dataset. Our navigation dataset aggregates various sources, including SpatialVID (Wang et al., 2026a), Sekai (Li et al., 2026), ABot-World (Jiang et al., 2026), internal gameplay recordings, and Unreal Engine (UE) rendering sequences, totaling 700K video clips (lasting 30s to 60s). To endow the model with flexible interactive capabilities, we construct an interactive event dataset comprising 10K clips (lasting 10s to 30s). This subset covers three categories, i.e., environmental transition, object addition/removal, and complex interaction. Although the interactive event dataset is relatively small, the pretrained model inherently exhibits strong instruction-following capability. Therefore, it suffices to unlock this capability. Details are provided in the Appendix.

**Implementation Details.** Our training follows a multi-stage curriculum. Specifically, the base video diffusion model is first trained for navigation controls on our spatial navigation dataset. Subsequently, utilizing the full dataset, we integrate the memory compressor following the two-stage training regime of Zhang et al. (2026a) to improve long-horizon geometric consistency. Next, the bidirectional model is adapted into a chunk-wise autoregressive model via teacher forcing, initialized for few-step generation via PDD (Shaul et al., 2026). Finally, we leverage distribution matching distillation to obtain the target world model. Furthermore, we deploy inference optimizations covering computation graph fusion, low-bit quantization, KV caching, and a lightweight VAE to achieve real-time generation at 16 FPS on 8 H20 GPUs. See Appendix for more details.

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

Table 1: Quantitative comparisons. We benchmark our approach against recent interactive world models on both WBench and [NAME C16] to systematically evaluate controllability, long-horizon consistency, and visual fidelity. Abbreviations: Avg: Average, Qua: Quality, Set: Setting, Int: Interaction, Con: Consistency, Phy: Physical.

[tbl-0.html](tbl-0.html)

![img-4.jpeg](img-4.jpeg)

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)

![img-8.jpeg](img-8.jpeg)

![img-9.jpeg](img-9.jpeg)

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)

![img-12.jpeg](img-12.jpeg)

![img-13.jpeg](img-13.jpeg)

![img-14.jpeg](img-14.jpeg)

![img-15.jpeg](img-15.jpeg)

![img-16.jpeg](img-16.jpeg)

![img-17.jpeg](img-17.jpeg)

![img-18.jpeg](img-18.jpeg)

Figure 5: Qualitative comparisons with existing methods. [NAME C16] supports versatile interactive events while demonstrating superior generalization across diverse characters and maintaining long-horizon geometric consistency.

Evaluation Details. To assess controllability, consistency, and visual fidelity, we benchmark all models on WBench (Ying et al., 2026). To systematically assess long-horizon geometric consistency, we introduce [NAME C16], an evaluation benchmark comprising 200 revisit trajectories following the protocol in Sun et al. (2026), which are curated from WBench and our self-collected validation sets. We quantify 2D visual consistency via LPIPS, PSNR, and SSIM, as well as 3D spatial consistency via MEt3R (Asim et al., 2025). Additionally, we curate 145 samples from WBench

[OCR table id=tbl-0.html; page=7]
<table><tr><td rowspan="2"></td><td colspan="6">WBench</td><td colspan="4">[NAME C16]</td></tr><tr><td>Avg. ↑</td><td>Qua. ↑</td><td>Set. ↑</td><td>Int. ↑</td><td>Con. ↑</td><td>Phy. ↑</td><td>PSNR ↑</td><td>SSIM ↑</td><td>LPIPS ↓</td><td>MEt3R ↓</td></tr><tr><td>WorldPlay (Sun et al., 2026)</td><td>78.1</td><td>78.1</td><td>72.2</td><td>86.8</td><td>86.9</td><td>66.3</td><td>17.05</td><td>0.553</td><td>0.416</td><td>0.179</td></tr><tr><td>AlayaWorld (Team et al., 2026a)</td><td>76.3</td><td>79.3</td><td>69.7</td><td>80.0</td><td>89.5</td><td>63.1</td><td>13.61</td><td>0.399</td><td>0.569</td><td>0.244</td></tr><tr><td>Lingbot-World-V2 (Gao et al., 2026)</td><td>79.4</td><td>81.8</td><td>76.8</td><td>82.8</td><td>86.5</td><td>69.1</td><td>14.46</td><td>0.469</td><td>0.506</td><td>0.301</td></tr><tr><td>EchoWM (Zhang et al., 2026b)</td><td>81.0</td><td>81.1</td><td>77.5</td><td>87.9</td><td>88.3</td><td>70.1</td><td>14.83</td><td>0.513</td><td>0.477</td><td>0.283</td></tr><tr><td>Alaya-Evoke-Turbo (Yin et al., 2026)</td><td>82.0</td><td>81.9</td><td>82.1</td><td>83.9</td><td>88.1</td><td>74.0</td><td>16.33</td><td>0.501</td><td>0.412</td><td>0.236</td></tr><tr><td>Ours (w/o Stable Forcing)</td><td>79.0</td><td>79.1</td><td>77.8</td><td>82.4</td><td>87.4</td><td>68.2</td><td>16.52</td><td>0.535</td><td>0.439</td><td>0.215</td></tr><tr><td>Ours (full)</td><td>83.1</td><td>81.8</td><td>81.5</td><td>88.3</td><td>90.0</td><td>74.0</td><td>19.71</td><td>0.613</td><td>0.318</td><td>0.105</td></tr></table>

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

and our interactive event dataset as test cases, which are held out from training, to evaluate model responsiveness to diverse interactive events. We deploy a vision-language model (VLM) (Seed, 2025) as an automated evaluator to score instruction adherence and execution accuracy. We compare our approach against five interactive world models: WorldPlay (Sun et al., 2026), AlayaWorld (Team et al., 2026a), Lingbot-World-V2 (Gao et al., 2026), EchoWM (Zhang et al., 2026b), and Alaya-Evoke-Turbo (Yin et al., 2026).

### 4.1 COMPARISONS WITH EXISTING METHODS

Quantitative Results. Tab. 1 compares our method with five representative interactive world models on the navigation split of WBench and [NAME C16]. [NAME C16] achieves the highest overall average score of 83.1, surpassing the previous state-of-the-art baseline, Alaya-Evoke-Turbo (Yin et al., 2026), by 1.1 points. Notably, [NAME C16] demonstrates a pronounced advantage in Interaction and Consistency. This empirically validates that our factorized hybrid control interface, coupled with the co-design of memory and distillation, significantly enhances long-horizon consistency while maintaining precise navigation controllability. [NAME C16] further evaluates long-horizon geometric consistency under loop-closure trajectories. Constrained by fixed context window lengths, Lingbot-World-V2 (Gao et al., 2026) and EchoWM (Zhang et al., 2026b) suffer from memory degradation, failing to preserve geometric consistency. Although WorldPlay (Sun et al., 2026) incorporates camera poses for historical context retrieval, it is inherently susceptible to compounding camera pose drift as rollouts progress, making it challenging to retrieve accurate context. AlayaWorld (Team et al., 2026a) and Alaya-Evoke-Turbo (Yin et al., 2026) rely on explicit 3D representations to maintain memory, but suffer from metric scale ambiguities across different chunks. Such scale discrepancies severely impede fine-grained control and inevitably induce geometric inconsistencies. In contrast, [NAME C16] maintains robust long-horizon geometric consistency without relying on error-prone retrieval or sensitive explicit 3D representations. Furthermore, as evidenced by the results, Stable Forcing substantially improves performance, directly demonstrating its effectiveness.

As shown in Tab. 2, we evaluate responsiveness across diverse interactive events. Although Lingbot-World-V2(Gao et al., 2026) and AlayaWorld (Team et al., 2026a) leverage chunk-wise captions to accommodate diverse controls, they fail to disentangle underlying world states. This entangles content factors with interactive events, making it challenging for them to capture precise correspondences between textual descriptions and visual dy-

namics, particularly in complex interactions. In contrast, our model explicitly factorizes the world state via the factorized hybrid control interface, yielding superior interactive fidelity.

Qualitative Results. Fig. 5 presents the qualitative comparisons with baselines. Due to the scarcity of interactive event datasets and reliance on entangled control conditioning, WorldPlay (Sun et al., 2026) and AlayaWorld (Team et al., 2026a) fail to respond accurately to diverse interactive commands. Meanwhile, Lingbot-World-V2 (Gao et al., 2026) and EchoWM (Zhang et al., 2026b) struggle to maintain long-horizon geometric consistency as a consequence of memory decay inherent in their sliding-window designs. Furthermore, their lack of factorized representations between background scenes and foreground characters impedes precise and smooth locomotion, such as airplane turning and entity centering. Although Alaya-Evoke-Turbo (Yin et al., 2026) can generate long sequences, its dependence on explicit 3D representations often introduces severe temporal flickering and visual artifacts, such as ghosting and duplicate entity appearances. In contrast, our approach reliably executes diverse interaction events, enables fine-grained and fluid control over different characters, and preserves long-horizon consistency, highlighting the efficacy and superiority of our method. Please refer to the supplementary videos for comprehensive visualizations.

### 4.2 ABLATION STUDIES

Controllability. Fig. 6(a) presents the ablation study on controllability. When trained without the interactive event dataset, the model's interactive capabilities are constrained, failing to respond to

Table 2: Quantitative comparison on responsiveness to interactive events. Abbreviations: EO: Environment and Object change, CI: Complex Interaction.

[tbl-1.html](tbl-1.html)

[OCR table id=tbl-1.html; page=8]
<table><tr><td>Method</td><td>Avg. ↑</td><td>EO. ↑</td><td>CI. ↑</td></tr><tr><td>WorldPlay (Sun et al., 2026)</td><td>43.3</td><td>47.9</td><td>38.7</td></tr><tr><td>AlayaWorld (Team et al., 2026a)</td><td>39.4</td><td>48.3</td><td>30.5</td></tr><tr><td>Lingbot-World-V2 (Gao et al., 2026)</td><td>52.5</td><td>61.5</td><td>43.4</td></tr><tr><td>EchoWM (Zhang et al., 2026b)</td><td>43.8</td><td>56.3</td><td>31.2</td></tr><tr><td>Alaya-Evoke-Turbo (Yin et al., 2026)</td><td>40.7</td><td>45.7</td><td>35.7</td></tr><tr><td>Ours</td><td>74.7</td><td>79.2</td><td>70.1</td></tr></table>

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

![img-19.jpeg](img-19.jpeg)

Figure 6: (a) Ablation on controllability: We verify the impact of interactive data scaling and structured semantic control. (b) Ablation on memory: We compare the GPU memory footprint and training time with the full-context baseline. For our method, we partition long sequences into multiple clips and compute sequentially within a single iteration. (c) Ablation on distillation: We analyze the components of Stable Forcing. Zoom in for details.

semantic events. Incorporating even a small fraction of interactive data unlocks these capabilities, enabling coherent interactions spanning dynamic semantic events and navigation controls. Furthermore, omitting our structured semantic control causes the model to conflate intricate foreground characters with background scenes, compromising precise navigation controllability.

Memory. To validate the efficiency of our compressed memory, we compare its GPU memory footprint and training time with the full-context baseline across various video lengths, as summarized in Fig. 6(b). At the same sequence lengths, compressed memory substantially reduces both memory consumption and iteration time, enabling scalable training and distillation on longer sequences. As shown in Fig. 6(b), our compressed memory achieves comparable long-horizon geometric consistency to its full-context counterpart when trained on 96 latents, demonstrating its effectiveness.

Distillation. Fig. 6(c) demonstrates the stability and efficacy of Stable Forcing. We first ablate the full-rollout replay, omitting it leads to progressive quality degradation during long-horizon generation and eventually triggers mode collapse, as evidenced by the ground artifacts. Furthermore, we evaluate the impact of the PDD initialization. Employing PDD initialization effectively mitigates blurry outputs and grid-like artifacts, confirming the robustness of our method. Additionally, while distilling with the full-context teacher achieves competitive performance, it demands substantially longer training wall-clock time (261s vs. 167s per iteration). Furthermore, extending the full-context teacher to longer horizon distillation (e.g., 320 latents) triggers out-of-memory issues, whereas our method scales with superior efficiency.

## 5 CONCLUSION AND LIMITATIONS

We present [NAME C16], an interactive world model that achieves real-time responsiveness, versatile control, and long-horizon consistency. It significantly expands the interactive capabilities of world models, faithfully executing both navigation-oriented controls and semantic interactive events while maintaining geometric consistency over long horizons. Crucially, [NAME C16] is designed with scalability at its core, which scales efficiently and stably as compute budgets and data volume expand. We hope [NAME C16] serves as a crucial step toward advancements in embodied intelligence, spatial computing, and interactive entertainment.

Limitations. Despite the promising capabilities demonstrated by [NAME C16], several challenges need further investigation. First, characters are still prone to gradual visual and semantic drift, occasionally failing to preserve strict identity consistency during long rollouts. Second, scaling our framework to infinite-horizon generation remains an open challenge. Maintaining both infinite rollout stability and long-term geometric consistency without error accumulation represents one of the most fundamental yet demanding frontiers in interactive world modeling.

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

In this work, we used generative AI tools for generating synthetic datasets, implementing methods, assisting with translation, cleaning and reformatting dataset, supporting qualitative and thematic data analysis, and interpreting results. We have not used generative AI tools for designing or providing feedback on research methodology or experiments. The rest of the required disclosure tasks are not applicable to this work. Additionally, we used generative AI tools for creating or editing software code and editing the paper to improve readability. We have reviewed all AI-assisted work. Specifically, both the synthesized datasets and the LLM-generated code were verified and tested to guarantee data fidelity and execution correctness. We take responsibility for the final content of this work, including text, claims, or artifacts produced with the aid of generative AI.

## REPRODUCIBILITY STATEMENT

We have taken care to ensure that our results can be reproduced. The full model formulation and training objectives are presented in the main paper. Moreover, the complete training, evaluation details, and the composition and processing of our training dataset are provided in the Appendix.

## REFERENCES

Niket Agarwal, Arslan Ali, Jon Allen, Martin Antolini, Adeline Aubame, Alisson Azzolini, Junjie Bai, Maciej Bala, Yogesh Balaji, Josh Bapst, et al. Cosmos 3: Omnimodal world models for physical ai. arXiv preprint arXiv:2606.02800, 2026.

Alibaba. HappyOyster, 2026. [URL REDACTED]

Mohammad Asim, Christopher Wewer, Thomas Wimmer, Bernt Schiele, and Jan Eric Lenssen. MEt3R: Measuring multi-view consistency in generated images. In CVPR, pp. 6034–6044, 2025.

Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen, Xionghui Chen, Zesen Cheng, Lianghao Deng, Wei Ding, Chang Gao, Chunjiang Ge, et al. Qwen3-VL technical report. arXiv preprint arXiv:2511.21631, 2025.

Ollin Boer Bohan. TAEHV: Tiny autoencoder for hunyuan video. [URL REDACTED] 2025.

Tim Brooks, Bill Peebles, Connor Holmes, Will DePue, Yufei Guo, Leo Jing, David Schnurr, Joe Taylor, Troy Luhman, Eric Luhman, et al. Video generation models as world simulators. OpenAI Blog, 1(8):1, 2024.

Hansheng Chen, Kai Zhang, Hao Tan, Leonidas Guibas, Gordon Wetzstein, and Sai Bi. Pi-Flow: Policy-based few-step generation via imitation distillation. In ICLR, pp. 151521–151547, 2026.

Google Deepmind. Veo3 video model, 2025. [URL REDACTED]

Juechu Dong, Boyuan Feng, Driss Guessous, Yanbo Liang, and Horace He. Flex Attention: A programming model for generating optimized attention kernels. arXiv preprint arXiv:2412.05496, 2(3):4, 2024.

Zelin Gao, Qiuyu Wang, Jiapeng Zhu, Jingye Chen, Zichen Liu, Qingyan Bai, Jiahao Wang, Yufeng Yuan, Hanlin Wang, Yichong Lu, et al. Infinite worlds with versatile interactions. arXiv preprint arXiv:2607.07534, 2026.

Zhengyang Geng, Mingyang Deng, Xingjian Bai, Zico Kolter, and Kaiming He. Mean flows for one-step generative modeling. NeurIPS, 38:75460–75482, 2026.

Yuchao Gu, Guian Fang, Yuxin Jiang, Weijia Mao, Song Han, Han Cai, and Mike Zheng Shou. AnyFlow: Any-step video diffusion model with on-policy flow map distillation. arXiv preprint arXiv:2605.13724, 2026.

Xianglong He, Chunli Peng, Zexiang Liu, Boyang Wang, Yifan Zhang, Qi Cui, Fei Kang, Biao Jiang, Mengyin An, Yangyang Ren, et al. Matrix-Game 2.0: An open-source real-time and streaming interactive world model. arXiv preprint arXiv:2508.13009, 2025.

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

Yicong Hong, Yiqun Mei, Chongjian Ge, Yiran Xu, Yang Zhou, Sai Bi, Yannick Hold-Geoffroy, Mike Roberts, Matthew Fisher, Eli Shechtman, et al. RELIC: Interactive video world model with long-horizon memory. arXiv preprint arXiv:2512.04040, 2025.

Jiahui Huang, Qunjie Zhou, Hesam Rabeti, Aleksandr Korovko, Huan Ling, Xuanchi Ren, Tianchang Shen, Jun Gao, Dmitry Slepichev, Chen-Hsuan Lin, et al. ViPE: Video pose engine for 3d geometric perception. arXiv preprint arXiv:2508.10934, 2025.

Xun Huang, Zhengqi Li, Guande He, Mingyuan Zhou, and Eli Shechtman. Self Forcing: Bridging the train-test gap in autoregressive video diffusion. NeurIPS, 38:167283–167308, 2026.

Fan Jiang, Zhaoxu Sun, Mengchao Wang, Ziyu Zhu, Chiyu Wang, Yunpeng Zhang, Wenlin Liu, Yun Wang, Xue Zheng, Rui Sun, et al. ABot-World-0: Infinite interactive world rollout on a single desktop gpu. arXiv preprint arXiv:2607.19191, 2026.

Jiaqi Li, Junshu Tang, Zhiyong Xu, Longhuang Wu, Yuan Zhou, Shuai Shao, Tianbao Yu, Zhiguo Cao, and Qinglin Lu. Hunyuan-GameCraft: High-dynamic interactive game video generation with hybrid history condition. arXiv preprint arXiv:2506.17201, 2(3):6, 2025.

Zhen Li, Chuanhao Li, Xiaofeng Mao, Shaoheng Lin, Ming Li, Shitian Zhao, Zhaopan Xu, Xinyue Li, Yukang Feng, Jianwen Sun, et al. Sekai: A video dataset towards world exploration. NeurIPS, 38, 2026.

Yaron Lipman, Ricky TQ Chen, Heli Ben-Hamu, Maximilian Nickel, and Matt Le. Flow matching for generative modeling. In ICLR, 2023.

Xiaofeng Mao, Shaoheng Lin, Zhen Li, Chuanhao Li, Wenshuo Peng, Tong He, Jiangmiao Pang, Mingmin Chi, Yu Qiao, and Kaipeng Zhang. Yume: An interactive world generation model. arXiv preprint arXiv:2507.17744, 2025.

Xiaofeng Mao, Zhen Li, Chuanhao Li, Xiaojie Xu, Kaining Ying, and Kaipeng Zhang. Yume1.5: A text-controlled interactive world generation model. In CVPR, pp. 7752–7761, 2026.

OpenAI. Gpt 6 astra, 2026. [URL REDACTED]

Jack Parker-Holder, Shlomi Fruchter, et al. Genie 3: A new frontier for world models. Google DeepMind Blog, 2025.

ByteDance Seed. Seed 2.1, 2025. [URL REDACTED]

Neta Shaul, Chao Liu, Arash Vahdat, and Julius Berner. Parallel decoding distillation for fast image and video generation. arXiv preprint arXiv:2607.26004, 2026.

Wenqiang Sun, Haiyu Zhang, Haoyuan Wang, Junta Wu, Zehan Wang, Zhenwei Wang, Yunhong Wang, Jun Zhang, Tengfei Wang, and Chunchao Guo. WorldPlay: Towards long-term geometric consistency for real-time interactive world modeling. In ICML, 2026.

Junshu Tang, Jiacheng Liu, Jiaqi Li, Longhuang Wu, Haoyu Yang, Penghao Zhao, Siruis Gong, Xiang Yuan, Shuai Shao, Linfeng Zhang, et al. Hunyuan-GameCraft-2: Instruction-following interactive game world model. arXiv preprint arXiv:2511.23429, 2025.

AlayaWorld Team, Kaipeng Zhang, Chuanhao Li, Yifan Zhan, Yongtao Ge, Yuanyang Yin, Jiaming Tan, Kang He, Liaoyuan Fan, Mingliang Zhai, et al. AlayaWorld: Interactive long-horizon world modeling–full technical report. arXiv preprint arXiv:2607.18367, 2026a.

DreamX Team, Yancheng Bai, Rui Chen, Xiangxiang Chu, Rujing Dang, Hao Dou, Bingjie Gao, Qiwen Gu, Siyu Hong, Jiachen Lei, et al. DreamX-World 1.0: A general-purpose interactive world model. arXiv preprint arXiv:2606.16993, 2026b.

Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, Katie Millican, et al. Gemini: a family of highly capable multimodal models. arXiv preprint arXiv:2312.11805, 2023.

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

Gemini Robotics Team, Krzysztof Choromanski, Coline Devin, Yilun Du, Debidatta Dwibedi, Ruiqi Gao, Abhishek Jindal, Thomas Kipf, Sean Kirmani, Isabel Leal, et al. Evaluating gemini robotics policies in a veo world simulator. arXiv preprint arXiv:2512.10675, 2025.

InSpatio Team, Donghui Shen, Guofeng Zhang, Haomin Liu, Haoyu Ji, Hujun Bao, Hongjia Zhai, Jialin Liu, Jing Guo, Nan Wang, et al. Inspatio-world: A real-time 4d world simulator via spatiotemporal autoregressive modeling. arXiv preprint arXiv:2604.07209, 2026c.

Robbyant Team, Zelin Gao, Qiuyu Wang, Yanhong Zeng, Jiapeng Zhu, Ka Leong Cheng, Yixuan Li, Hanlin Wang, Yinghao Xu, Shuailei Ma, et al. Advancing open-source world models. arXiv preprint arXiv:2601.20540, 2026d.

Tencent HY World Team. HunyuanWorld 1.0: Generating immersive, explorable, and interactive 3d worlds from words or pixels. arXiv preprint arXiv:2507.21809, 2025.

Tencent HY World Team. HY-World 2.0: A multi-modal world model for reconstructing, generating, and simulating 3d worlds. arXiv preprint arXiv:2604.14268, 2026.

Team Wan, Ang Wang, Baole Ai, Bin Wen, Chaojie Mao, Chen-Wei Xie, Di Chen, Feiwu Yu, Haiming Zhao, Jianxiao Yang, et al. Wan: Open and advanced large-scale video generative models. arXiv preprint arXiv:2503.20314, 2025.

Jiahao Wang, Yufeng Yuan, Rujie Zheng, Youtian Lin, Jian Gao, Lin-Zhuo Chen, Yajie Bao, Chang Zeng, Yanxi Zhou, Xiao-Xiao Long, et al. SpatialVID: A large-scale video dataset with spatial annotations. In CVPR, pp. 42592–42603, 2026a.

Zidong Wang, Yiyuan Zhang, Xiaoyu Yue, Xiangyu Yue, Yangguang Li, Wanli Ouyang, and Lei Bai. Transition models: Rethinking the generative learning objective. In CVPR, pp. 29178–29189, 2026b.

Zile Wang, Zexiang Liu, Jiaxing Li, Kaichen Huang, Baixin Xu, Fei Kang, Mengyin An, Peiyu Wang, Biao Jiang, Yichen Wei, et al. Matrix-Game 3.0: Real-time and streaming interactive world model with long-horizon memory. arXiv preprint arXiv:2604.08995, 2026c.

Thaddäus Wiedemer, Yuxuan Li, Paul Vicol, Shixiang Shane Gu, Nick Matarese, Kevin Swersky, Been Kim, Priyank Jaini, and Robert Geirhos. Video models are zero-shot learners and reasoners. arXiv preprint arXiv:2509.20328, 2025.

Bing Wu, Chang Zou, Changlin Li, Duojun Huang, Fang Yang, Hao Tan, Jack Peng, Jianbing Wu, Jiangfeng Xiong, Jie Jiang, et al. Hunyuanvideo 1.5 technical report. arXiv preprint arXiv:2511.18870, 2025.

Zeqi Xiao, Yushi Lan, Yifan Zhou, Wenqi Ouyang, Shuai Yang, Yanhong Zeng, and Xingang Pan. WorldMem: Long-term consistent world simulation with memory. NeurIPS, 38:49632–49652, 2026.

Jiacong Xu, Hanwen Jiang, Zhixin Shu, Kalyan Sunkavalli, Vishal M Patel, and Yiqun Mei. Wonder: Video world model done better. arXiv preprint arXiv:2607.26037, 2026.

Tianwei Yin, Michaël Gharbi, Taesung Park, Richard Zhang, Eli Shechtman, Fredo Durand, and William T Freeman. Improved distribution matching distillation for fast image synthesis. NeurIPS, 37:47455–47487, 2024a.

Tianwei Yin, Michaël Gharbi, Richard Zhang, Eli Shechtman, Fredo Durand, William T Freeman, and Taesung Park. One-step diffusion with distribution matching distillation. In CVPR, pp. 6613–6623, 2024b.

Tianwei Yin, Qiang Zhang, Richard Zhang, William T Freeman, Fredo Durand, Eli Shechtman, and Xun Huang. From slow bidirectional to fast autoregressive video diffusion models. In CVPR, pp. 22963–22974, 2025.

Yuanyang Yin, Gongxuan Wang, Yifan Zhan, Chuanhao Li, Kaipeng Zhang, and Feng Zhao. Alaya-EVOKE: From linear-scaling supervision to endless world. arXiv preprint arXiv:2608.13546, 2026.

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

Kaining Ying, Hengrui Hu, Siyu Ren, Jiamu Li, Fengjiao Chen, Ziwen Wang, Xuezhi Cao, Xunliang Cai, and Henghui Ding. WBench: A comprehensive multi-turn benchmark for interactive video world model evaluation. arXiv preprint arXiv:2605.25874, 2026.

Jiwen Yu, Jianhong Bai, Yiran Qin, Quande Liu, Xintao Wang, Pengfei Wan, Di Zhang, and Xihui Liu. Context as memory: Scene-consistent interactive long video generation with memory retrieval. In SIGGRAPH Asia, pp. 1–11, 2025.

Jintao Zhang, Haofeng Huang, Pengle Zhang, Jia Wei, Jun Zhu, and Jianfei Chen. SageAttention2: Efficient attention with thorough outlier smoothing and per-thread int4 quantization. arXiv preprint arXiv:2411.10958, 2024.

Lvmin Zhang, Shengqu Cai, Muyang Li, Chong Zeng, Beijia Lu, Anyi Rao, Song Han, Gordon Wetzstein, and Maneesh Agrawala. TinyHistory: Lightweight video history embeddings via two-stage context learning. In ECCV, 2026a.

Songchun Zhang, Yaowei Li, Junhao Zhuang, Weiyang Jin, Haoyu Wang, Xin Lu, Yilang Sun, Shiyi Zhang, Haoran Li, Xiaoxiao Ma, et al. EchoWM: Open and enterable omnimodal world models. arXiv preprint arXiv:2608.23189, 2026b.

Yifan Zhang, Chunli Peng, Boyang Wang, Puyi Wang, Qingcheng Zhu, Fei Kang, Biao Jiang, Zedong Gao, Eric Li, Yang Liu, et al. Matrix-Game: Interactive world foundation model. arXiv preprint arXiv:2506.18701, 2025.

Kaiwen Zheng, Guande He, Min Zhao, Jintao Zhang, Huayu Chen, Jianfei Chen, Chen-Hsuan Lin, Ming-Yu Liu, Jun Zhu, and Qianli Ma. Causal-rCM: A unified teacher-forcing and self-forcing open recipe for autoregressive diffusion distillation in streaming video generation and interactive world models. arXiv preprint arXiv:2606.25473, 2026a.

Kaiwen Zheng, Yuji Wang, Qianli Ma, Huayu Chen, Jintao Zhang, Yogesh Balaji, Jianfei Chen, Ming-Yu Liu, Jun Zhu, and Qinsheng Zhang. Large scale diffusion distillation via score-regularized continuous-time consistency. In ICLR, pp. 2582–2603, 2026b.

Haoyi Zhu, Haozhe Liu, Yuyang Zhao, Tian Ye, Junsong Chen, Jincheng Yu, Tong He, Song Han, and Enze Xie. SANA-WM: Efficient minute-scale world modeling with hybrid linear diffusion transformer. arXiv preprint arXiv:2605.15178, 2026a.

Hongzhou Zhu, Min Zhao, Guande He, Hang Su, Chongxuan Li, and Jun Zhu. Causal Forcing: Autoregressive diffusion distillation done right for high-quality real-time interactive video generation. In ICML, 2026b.

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

## APPENDIX

### A DISCUSSION

A predominant paradigm among concurrent interactive world models (Gao et al., 2026; Jiang et al., 2026) relies on sliding-window mechanisms to facilitate autoregressive rollout over extended temporal horizons. While computationally tractable, this formulation fundamentally enforces a local assumption: the model's predictive distribution is heavily conditioned on adjacent frames, inherently ignoring distant observations. Consequently, such architectures struggle with long-horizon geometric consistency. In contrast, our framework departs from local receptive fields by designing an efficient memory mechanism with a stable distillation. This enables our model to anchor spatiotemporal invariants across long rollouts, maintaining high-fidelity geometric and semantic consistency. Despite these gains, we candidly acknowledge the boundaries of our approach. Scaling our framework to unbounded, infinite-horizon generation remains an open challenge. We posit that achieving both infinite-horizon rollout and long-term geometric persistence represents one of the most fundamental frontiers in interactive world modeling. Furthermore, recent coding agents (OpenAI, 2026) have demonstrated a remarkable ability to synthesize spatially coherent 3D environments via programmatic generation. This milestone signals a profound paradigm shift, transitioning agents from static textual domains to dynamic embodied multi-modal domains. We believe that integrating such intelligence into generative world models represents an exceptionally promising frontier.

### B DATASET

#### B.1 SPATIAL NAVIGATION DATASET

As detailed in Tab. 3, our spatial navigation dataset comprises three complementary categories. First, to capture real-world physical dynamics and complex photorealistic textures, we curate high-quality subsets from SpatialVID (Wang et al., 2026a) and Sekai (Li et al., 2026). Specifically, we curate videos captured in open unobstructed environments with smooth navigation trajectories. Second, to reinforce long-term geometric consistency under complex camera trajectories, we design a dedicated loop-closure rendering pipeline in UE. The synthesized camera trajectories are strictly self-symmetric, i.e., the second half of the sequence precisely reverses the camera path of the first half. During the first half exploration phase, multiple navigation actions are executed with randomized durations ranging from 1s to 5s. Finally, to broaden trajectory diversity and improve generalization, we incorporate open-source gameplay datasets (Jiang et al., 2026) and scale the simulation recording dataset. This substantially enriches the coverage of game genres, dynamic environments, and third-person characters.

#### B.2 INTERACTIVE EVENT DATASET

Our interactive event dataset comprises three categories: complex interaction, environmental transition, and object addition/removal, as detailed in Tab. 3 and Fig. 7. For complex interaction, we aim to jointly capture intricate behavioral interactions alongside spatial navigation, spanning 13 distinct action categories across both first-person and third-person perspectives. For environmental transition, we collect diverse videos capturing dynamic weather shifts (e.g., clear skies transitioning to heavy rain, fog, or snow), seasonal evolutions (e.g., summer lushness shifting to autumnal foliage or winter snowscapes), and holistic stylistic variations (e.g., day-to-night lighting and artistic rendering styles). For object addition and removal, our dataset encompasses the emergence and disappearance of dynamic agents such as animals, flying crafts (e.g., drones and aircraft), vehicles, tools, boxes, and handheld items.

#### B.3 DATA PROCESSING

Our data processing pipeline consists of three stages: structured semantic captioning, spatial navigation action extraction, and quality filtering.

## A-page-0015

target PDF page 15

Structured Semantic Captioning. In alignment with our structured semantic control, each video clip requires a disentangled textual description. To this end, we utilize VLMs (Team et al., 2023; Bai et al., 2025) to parse the visual information into structured captions using the following template.

#### Structured Semantic Captioning Template

Role: You are a professional video annotator specializing in interactive world models.

Core Task: You will be given a video. Your task is to describe it and output a single JSON object. Follow these rules exactly.

Important: This video has been pre-labeled as: PERSPECTIVE. Trust this label and follow the corresponding perspective handling rule below.

##### — Rules —

Language: Write all field values in English.

Output: Return ONLY one valid JSON object with exactly four keys: scene, character, UI, dynamic_interactions. No extra text, no markdown code fences, no commentary. Do not describe camera motion, camera rotation, camera shake, zooming, viewpoint movement, gameplay controls. Be specific, concrete, and visually grounded. Do not invent details that cannot be seen.

Perspective handling (affects the character field only): TPS: Describe the visual appearance of any visible player-controlled subject (humanoid, vehicle, or creature) under character. FPS: Set character to "None".

Scene: A unified descriptor encompassing visible terrain/objects, the environmental setting (e.g., forest, urban, room), and aesthetic styles (e.g., lighting, rendering scheme). Dynamic actions and transient events are prohibited.

Character: An appearance-only descriptor of the controlled agent, strictly omitting transient poses, gestures, or kinetic activities. It details four morphological dimensions: agent taxonomy & build, surface styling, equipped accessories, and active mounts.

UI: A unified spatial layout descriptor of all visible on-screen interface elements—including HUD components, status meters, minimaps, crosshairs, and text overlays—along with their designated screen positions, defaulting to "None" when no graphical interface is present.

dynamic_interactions: A chronological array of 5s intervals (start_time, end_time, event) cataloging visually grounded causal dynamics. It prioritizes salient physical engagements, hand gestures, contact transitions (approach, manipulation, release), and resulting state changes. Camera motions, static descriptions, and speculative actions are strictly excluded; inactive segments default to "None".

##### — Output Format —

{
    "scene": "...",
    "character": "...",
    "UI": "...",
    "dynamic_interactions": [
    {
    "start_time": 0,
    "end_time": 5,
    "event": "..."
    },
    {
    "start_time": 5,
    "end_time": 10,
    "event": "..."
    }
    ]
}

Spatial Navigation Action Extraction. We observe that directly applying ViPE (Huang et al., 2025) to long-horizon video clips frequently suffers from severe trajectory drift and scale collapse. To mitigate this degradation, we partition each long video into overlapping clips of 150 frames with a 10-frame temporal overlap. Camera poses are estimated independently for each sub-clip and

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

## A-page-0016

target PDF page 16

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

Table 3: Data organization. We detail the data type, category, data source, clip counts, and their corresponding proportions in the training corpus.

[tbl-2.html](tbl-2.html)

![img-20.jpeg](img-20.jpeg)

Figure 7: Overview of our interactive event dataset. The dataset encompasses three categories, including complex interaction, environmental transition, and object addition/removal. Left: The composition of the dataset. Right: Representative visual examples for each category.

subsequently stitched together by aligning metric scales using the overlapping windows. From the reconstructed camera poses, we derive frame-aligned action controls by decomposing the motion into discrete longitudinal and lateral translations alongside continuous pitch and yaw angles. Our internal gameplay recordings are captured under constant angular velocities per game. Leveraging this property, we compute the directional angular velocities offline for each game and adopt their empirical medians as the calibrated rotation rates along the corresponding axes.

Quality Filtering. Our quality filtering pipeline operates along two distinct dimensions: visual fidelity and action precision. Following Wu et al. (2025), we employ a comprehensive visual quality assessment model coupled with an aesthetic scoring operator to evaluate video clips across five perceptual dimensions, i.e., sharpness, fine-detail retention, noise and compression artifacts, dynamic range, and aesthetic appeal, systematically filtering out low-quality candidates. Then, we evaluate the temporal smoothness and physical plausibility of the estimated camera poses for each video clip, filtering out abrupt camera jitter to ensure accurate action labels.

## C MORE IMPLEMENTATION DETAILS

### C.1 ARCHITECTURE DETAILS

Frame-aligned Action Module. Since our frame-aligned actions contain both continuous camera rotations and discrete controls, we devise tailored encoding pathways as shown in Fig. 8. For continuous camera rotations, we employ an MLP to model varying angular velocities. For discrete controls, we adopt learnable embeddings to effectively capture concrete patterns. The two action embeddings are

![img-21.jpeg](img-21.jpeg)

Figure 8: Illustration of our action module.

[OCR table id=tbl-2.html; page=16]
<table><tr><td>Data Type</td><td>Category</td><td>Data Source</td><td>Quantity</td><td>Ratio</td></tr><tr><td rowspan="5">Spatial Navigation</td><td rowspan="2">Real-World Dynamics</td><td>SpatialVID (Wang et al., 2026a)</td><td>30K</td><td>4.22%</td></tr><tr><td>Sekai (Li et al., 2026)</td><td>20K</td><td>2.81%</td></tr><tr><td>Synthetic 4D Scenes</td><td>UE Rendering</td><td>50K</td><td>7.04%</td></tr><tr><td rowspan="2">Simulation Dynamics</td><td>ABot-World (Jiang et al., 2026)</td><td>30K</td><td>4.22%</td></tr><tr><td>Gameplay Recording</td><td>570K</td><td>80.28%</td></tr><tr><td rowspan="3">Interactive Event</td><td>Complex Interaction</td><td></td><td>5K</td><td>0.70%</td></tr><tr><td>Environmental Transition</td><td>Internal Dataset</td><td>3K</td><td>0.42%</td></tr><tr><td>Object Addition/Removal</td><td></td><td>2K</td><td>0.28%</td></tr></table>

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

![img-22.jpeg](img-22.jpeg)

Figure 9: Overview of our multi-stage training pipeline. The bidirectional base model is progressively adapted into a streaming autoregressive model via action conditioning (AC), memory integration, and distillation.

Algorithm 1 Stable Forcing (Full-rollout Replay and Efficient Score Evaluation)

Require: Initialized student  \( N_{\theta} \) ; real and fake score models  \( v_{real} \) ,  \( v_{fake} \) ; the number of rollout chunks M; denoising schedule  \( \{\sigma_{d}\}_{d=0}^{D} \) ;
Output: Few-step autoregressive student.
1:  \( H \leftarrow \emptyset \) ;  \( X \leftarrow \emptyset \) 
2: Stage 1: Full-rollout without gradients
3: for  \( i = 1, \ldots, M \)  do
4:  \( m_{<i} \leftarrow \text{CompressedMemory}(\mathcal{H}) \) 
5:  \( z_{i} \sim \mathcal{N}(0, I) \) ;  \( d_{i} \sim \text{Uniform}(\{0, \ldots, D-1\}) \) 
6: for  \( d = 0, \ldots, D-1 \)  do
7: if  \( d = d_{i} \)  then
8:  \( R_{i} \leftarrow \text{Snapshot}(z_{i}, \sigma_{d}, m_{<i}, A_{\leq i}) \) 
9: end if
10:  \( z_{i} \leftarrow \text{Denoise}(z_{i}, N_{\theta}(z_{i}, \sigma_{d}, m_{<i}, A_{\leq i})) \) 
11: end for
12: Append  \( \text{sg}(z_{i}) \)  to X and H
13: end for
14: Stage 2: Efficient score evaluation without gradients
15: Partition X into B consecutive clips  \( \{x_{b}\}_{b=1}^{B} \) 
16: for  \( b = 1, \ldots, B \)  do
17: Sample score timestep  \( \sigma \)  and noise  \( \epsilon \) 
18:  \( x_{b}^{\sigma} \leftarrow \text{AddNoise}(x_{b}, \sigma, \epsilon) \) 
19:  \( g_{b} \leftarrow [v_{\text{fake}}(x_{b}^{\sigma}, \sigma, m_{<b}, A_{\leq b}) - v_{\text{real}}(x_{b}^{\sigma}, \sigma, m_{<b}, A_{\leq b})] \) 
20: end for
21: Stage 3: Gradient replay with gradients
22: for  \( i = 1, \ldots, M \)  do
23:  \( \widetilde{z}_{i} \leftarrow \text{CleanPrediction}(z_{i}, \sigma_{d_{i}}, N_{\theta}(\mathcal{R}_{i})) \) 
24:  \( L_{i} \leftarrow \text{MSE}(\widetilde{z}_{i}, \text{sg}(\widetilde{z}_{i} - g_{i})) \) 
25: Backpropagate  \( L_{i} \) 
26: end for
27: Update  \( \theta \)  once using the accumulated gradients
28: Update  \( v_{fake} \)  following DMD2 (Yin et al., 2024a)

then added and injected before the FFN in each Transformer block. Interestingly, we observe that omitting explicit camera poses incurs no visible degradation in navigation control. Moreover, enforcing rigid camera trajectories makes it difficult to simulate character-centric rotations. In contrast, our design unleashes smoother, more fluid third-person character locomotion and delivers stronger generalization across diverse characters.

History Compressor. Our history compressor builds upon the design paradigm of TinyHistory (Zhang et al., 2026a), combining 3D convolutions to compress spatiotemporal history with attention modules to enhance expressiveness. We further replace standard 3D convolutions with causal 3D convolutions. This design strictly prevents future information leakage, thereby adhering to the temporal causality of autoregressive generation.

### C.2 TRAINING DETAILS

Our multi-stage training pipeline is summarized in Fig. 9. For the bidirectional model, each training sequence comprises 32 target latents with the associated memory context. For the AR model, the

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

Table 4: Inference speed improvements from system optimizations. Latency is benchmarked as the average time per chunk across multiple generated chunks. Latency reductions are reported relative to the baseline.

[tbl-3.html](tbl-3.html)

training sequence is formulated over 16 target latents, i.e., 4 chunks, along with their corresponding memory context. To optimize AR training throughput, we pad the variable-length memory contexts to a uniform sequence length, which enables efficient kernel execution via FlexAttention (Dong et al., 2024). Furthermore, both bidirectional and AR models are trained using a progressive curriculum, increasing the maximum data length to facilitate smooth convergence. During Stable Forcing, we leverage the AR model as the student, distilling it into 4 steps under the supervision of the bidirectional teacher model. Specifically, the student model performs self-rollout over a horizon of 320 latents, which the teacher partitions into 10 clips to efficiently compute scores. To compute backward passes over these long-horizon sequences, we adopt a gradient replay strategy analogous to RELIC (Hong et al., 2025), effectively reducing peak GPU memory footprints during backpropagation. Alg. 1 outlines the pseudocode of Stable Forcing.

### C.3 INFERENCE DETAILS

Complementing our algorithmic acceleration, we implement end-to-end systems optimizations across the entire inference pipeline, ultimately achieving a real-time streaming throughput of 16 FPS on 8 NVIDIA H20 GPUs as shown in Tab. 4. These optimizations include three complementary dimensions, i.e., computational graph fusion, quantization coupled with caching reuse, and lightweight VAE.

Computational Graph Fusion. We fuse the rotary position embeddings with the query-key linear projections (QKRoPE), combine query-key-value linear projections into a single linear projection (QKVFusion), and apply block-level compilation to the feed-forward networks (FFNCompile).

Quantization Coupled with Caching Reuse. We incorporate FP8 quantization (FP8 Quantization) alongside SageAttention (Zhang et al., 2024) to further compress execution latency and peak memory footprints. Moreover, we cache the text embeddings (Text Cache), which bypasses redundant text encoding passes. Finally, we disable Fully Sharded Data Parallel (FSDP) during inference, thereby eliminating cross-device collective communication overheads.

Lightweight VAE. To overcome the severe latency bottleneck inherent in video VAE, we redesign and retrain a lightweight VAE grounded on TAE (Boer Bohan, 2025).

### C.4 EVALUATION DETAILS

To systematically evaluate long-horizon geometric consistency, we construct [NAME C16], comprising 50 10s and 150 30s test cases with loop-closure trajectories. Specifically, for each test case, we first randomly sample discrete movement and continuous rotation to generate the trajectory for the first half of the sequence. For the remaining duration, we invert the preceding action sequence, making the model revisit its original path. These rigorous loop-closure cases reliably evaluate the geometric consistency of world models.

As described in the main paper, to evaluate the responsiveness to diverse interactive events, we leverage the VLM as an automated evaluator to quantitatively verify instruction adherence and execution

[OCR table id=tbl-3.html; page=18]
<table><tr><td>Optimization</td><td>Latency (s)</td><td>Speedup</td><td>Reduction</td></tr><tr><td>Baseline</td><td>4.138</td><td>1.00×</td><td>-</td></tr><tr><td>+ QKRoPE</td><td>4.103</td><td>1.01×</td><td>0.85%</td></tr><tr><td>+ QKVFusion</td><td>4.077</td><td>1.01×</td><td>1.47%</td></tr><tr><td>+ FFNCompile</td><td>4.074</td><td>1.02×</td><td>1.55%</td></tr><tr><td>+ Text Cache</td><td>3.955</td><td>1.05×</td><td>4.42%</td></tr><tr><td>+ FP8 Quantization</td><td>3.805</td><td>1.09×</td><td>8.05%</td></tr><tr><td>- FSDP</td><td>3.562</td><td>1.16×</td><td>13.92%</td></tr><tr><td>+ SageAttention (Zhang et al., 2024)</td><td>3.432</td><td>1.21×</td><td>17.06%</td></tr><tr><td>+ LightVAE (Final)</td><td>0.998</td><td>4.15×</td><td>75.88%</td></tr></table>

## A-page-0019

target PDF page 19

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

accuracy. Specifically, regarding environment and object change, we assess whether the expected state transitions faithfully occur and reach completion, as well as whether these visual transformations semantically correspond to the given interactive controls. For complex interactions, we further examine whether the fine-grained interactive details strictly align with the user-specified control inputs. We employ the following prompt template.

#### Interactive Evaluation Template

Role: You are an impartial evaluator of interactive world models. Evaluate how faithfully the video responds to the provided interactive control instructions, using only visual observations.

Inputs: Video: <video>; Interaction category: <eo ci="" or="">; Control instructions: <instructions>; Instruction timing: <frame ranges="">;</frame></instructions></eo></video>

#### Evaluate the following dimensions:

A. Instruction Adherence. Assess whether the observed response matches the requested action, target, and attributes, without incorrect targets, reversed actions, or unintended substitutions. Assess whether the action or state transition reaches its intended endpoint. Distinguish completion from attempts or partial execution.

B. Execution Accuracy. Assess whether the requested action is visibly executed correctly. For EO, verify that the intended state transition occurs with the specified direction and attributes. For CI, verify the interaction and relevant details, including contact location, motion direction, manipulation, and the resulting relationship. Do not impose requirements beyond the instruction.

#### — Scoring —

Assign an integer from 0 to 4 to each dimension:

- 0: No fulfillment, or clear contradiction of the requirement.
- 1: Minimal fulfillment, with major errors or only a weak attempt.
- 2: Partial fulfillment, with substantial omissions or errors.
- 3: Mostly fulfilled, with minor errors or limited incompleteness.
- 4: Fully fulfilled, supported by clear visual evidence.

#### — Output Format —

{
    "category": "EO or CI",
    "evaluations": [
    {
    "instruction_id": 1,
    "instruction": "...",
    "scores": {
    "instruction_adherence": "3",
    "execution_accuracy": "4",
    },
    "reasoning": "Provide the evidence."
    }
    ]
}

## D MORE RESULTS

### D.1 MORE VISUALIZATIONS

Fig. 10, Fig. 11, and Fig. 12 illustrate the comprehensive qualitative performance of [NAME C16] across diverse environments, different characters, and versatile controls. [NAME C16] not only accommodates intricate semantic interactions (e.g., dexterous grasping and box opening) alongside macro-level environmental transitions (e.g., weather shift and explosion), but also exhibits exceptional third-person character controllability. Specifically, it faithfully synthesizes smooth character motions that adhere strictly to the physical and kinematic constraints of diverse entities. Furthermore, it sustains robust geometric consistency and structural fidelity even under compound, multi-stage interactive controls.

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

Table 5: Quantitative comparison on interactive event dataset.

[tbl-4.html](tbl-4.html)

Table 7: Quantitative comparison on memory. For fair comparisons, both variants utilize a bidirectional backbone and train under 96 latents.

[tbl-5.html](tbl-5.html)

Table 6: Quantitative comparison on structured semantic control.

[tbl-6.html](tbl-6.html)

Table 8: Quantitative comparison on distillation.

[tbl-7.html](tbl-7.html)

### D.2 QUANTITATIVE ABLATIONS

Controllability. To validate the factorized hybrid control interface, we perform ablations on our bidirectional teacher model. As presented in Tab. 5, we first probe the role of the interactive event dataset on semantic responsiveness. We observe that even in the absence of the interactive event data, the model already exhibits moderate responsiveness. Consequently, introducing a small fraction of interactive data is highly sample-efficient, yielding substantial gains in semantic interactivity. Moreover, we assess navigation performance regarding structured semantic control as in Tab. 6. Ablating this module causes navigation conditioning to couple with other world states, inducing semantic entanglement that degrades navigation accuracy.

Memory. As reported in Tab. 7, we evaluate long-horizon geometric consistency on revisit trajectories, comparing our compressed memory against the full-context baseline, where both variants are trained on 96 latents. While retaining uncompressed, full-resolution history endows high expressive capacity, training this model incurs prohibitive computational overhead and training time. In contrast, our compressed memory mechanism models long-horizon information in a resource-efficient manner, achieving highly competitive geometric consistency while drastically alleviating the training burden.

Distillation. To validate our distillation, we quantitatively benchmark different variants on WBench, as summarized in Tab. 8. Without few-step initialization and full-rollout replay, the student model suffers from severe mode collapse, leading to degraded visual quality (as shown in Quality dimension). While incorporating full-rollout replay partially mitigates training divergence, it remains visibly inferior to Stable Forcing across the metrics. Although distilling with the full-context teacher obtains competitive performance, scaling it to longer horizons suffers from prohibitive computational overhead, hindering efficient training. In contrast, our method achieves efficient distillation while maintaining generation quality, highlighting the effectiveness of Stable Forcing.

[OCR table id=tbl-4.html; page=20]
<table><tr><td>Method</td><td>Avg. ↑</td><td>EO. ↑</td><td>CI. ↑</td></tr><tr><td>w/o interactive event dataset</td><td>46.7</td><td>57.5</td><td>35.8</td></tr><tr><td>Ours (Bidirectional)</td><td>84.0</td><td>86.8</td><td>81.2</td></tr></table>

[OCR table id=tbl-5.html; page=20]
<table><tr><td>Method</td><td>PSNR ↑</td><td>SSIM ↑</td><td>LPIPS ↓</td><td>MEt3R ↓</td></tr><tr><td>Full-context</td><td>18.47</td><td>0.688</td><td>0.406</td><td>0.133</td></tr><tr><td>Ours</td><td>18.80</td><td>0.653</td><td>0.414</td><td>0.128</td></tr></table>

[OCR table id=tbl-6.html; page=20]
<table><tr><td>Method</td><td>Rot. Err. ↓</td><td>Trans. Acc. ↑</td></tr><tr><td>w/o structured semantic control</td><td>0.478</td><td>88.9</td></tr><tr><td>Ours (Bidirectional)</td><td>0.168</td><td>98.3</td></tr></table>

[OCR table id=tbl-7.html; page=20]
<table><tr><td rowspan="2">Method</td><td colspan="6">WBench</td></tr><tr><td>Avg. ↑</td><td>Qua. ↑</td><td>Set. ↑</td><td>Int. ↑</td><td>Con. ↑</td><td>Phy. ↑</td></tr><tr><td>w/o init &amp; full-rollout</td><td>73.9</td><td>74.4</td><td>64.6</td><td>81.9</td><td>82.6</td><td>65.8</td></tr><tr><td>w/o init</td><td>75.2</td><td>76.2</td><td>68.0</td><td>82.6</td><td>83.3</td><td>65.9</td></tr><tr><td>Full-context Teacher</td><td>82.3</td><td>81.6</td><td>79.5</td><td>88.1</td><td>89.4</td><td>72.9</td></tr><tr><td>Ours</td><td>83.1</td><td>81.8</td><td>81.5</td><td>88.3</td><td>90.0</td><td>74.0</td></tr></table>

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

![img-23.jpeg](img-23.jpeg)

Figure 10: Qualitative visualizations on versatile controls. [NAME C16] supports a broad range of open-ended interactions, such as fine-grained hand-object manipulations (dexterous grasping and box opening), dynamic environmental transitions and anomaly events (weather shifts and explosion), and complex full-body interactions (getting in vehicles and riding animals).

## A-page-0022

target PDF page 22

1134
1135
1136
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187

![img-24.jpeg](img-24.jpeg)

![img-25.jpeg](img-25.jpeg)

![img-26.jpeg](img-26.jpeg)

Figure 11: Qualitative visualizations on long-horizon consistency. [NAME C16] generalizes robustly across different characters. Crucially, it can execute intricate interactions seamlessly alongside navigation controls (first case), while faithfully preserving spatiotemporal consistency over long horizons.

## A-page-0023

target PDF page 23

1188
1189
1190
1191
1192
1193
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
1213
1214
1215
1216
1217
1218
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
1241

![img-27.jpeg](img-27.jpeg)

![img-28.jpeg](img-28.jpeg)

![img-29.jpeg](img-29.jpeg)

Figure 12: Qualitative visualizations on long-horizon consistency. Top: [NAME C16] maintains geometric consistency under compound navigation controls. Middle: It generates structurally plausible scene layouts and preserves spatial coherence over long horizons. Bottom: It preserves geometric consistency under 360° camera rotations.
