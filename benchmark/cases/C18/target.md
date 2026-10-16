# [TITLE C18]?

## A-page-0001

target PDF page 1

# [TITLE C18]?

Anonymous authors

Paper under double-blind review

# ABSTRACT

Large language models (LLMs) based on the Transformer have demonstrated strong performance across diverse tasks. However, current models still exhibit limitations in out-of-distribution (OOD) generalization compared with humans. We investigate this gap through periodicity, one of the basic OOD scenarios. Periodicity captures invariance amid variation. Periodicity generalization represents a model's ability to extract periodic patterns from training data and generalize to OOD scenarios. We introduce a unified interpretation of periodicity from the perspective of abstract algebra and reasoning, including both single and composite periodicity, to analyze why Transformers struggle to generalize periodicity. Then we construct **Coper** about composite periodicity, a controllable generative dataset with two OOD settings, **Hollow** and **Extrapolation**. Experiments reveal that periodicity generalization in Transformers is limited, where models can memorize periodic data during training, but cannot generalize to unseen composite periodicity. We release the source code to support future research (Repository, 2026).

# 1 INTRODUCTION

In recent years, large language models (LLMs) based on the Transformer architecture (Vaswani et al., 2017) have achieved milestone progress in natural language processing (OpenAI, 2023; Google, 2025) and reasoning (DeepSeek-AI et al., 2025; El-Kishky et al., 2025; Chen et al., 2021). Recent studies show that LLMs can even discover new physical laws (Fang et al., 2025) and mathematical theorems (Liu et al., 2025). These achievements lead many researchers to believe that LLMs may eventually reach artificial general intelligence (AGI) (Bubeck et al., 2023).

However, some researchers remain skeptical about the path from LLMs to AGI (Perrigo, 2024). Compared with humans, who can learn complex patterns from limited data with low energy consumption (Sutskever, 2025; Feng et al., 2024), current models still exhibit significant gaps in learning efficiency and out-of-distribution (OOD) generalization (Bender et al., 2021; Song et al., 2025; Wu et al., 2025; Kordi et al., 2025; Hu et al., 2024).

To understand this gap, periodicity provides a key entry point. Periodicity is an essential characteristic that appears widely in nature, mathematics, and human cognition (Buzsáki, 2006; Shapley et al., 1985). It reflects invariance amid variation, from nature (Zalta et al., 2020) to abstract algebra (Dummit & Foote, 2004), and from signal processing (Orfanidis, 1995) to reasoning (Lake et al., 2017; Dong et al., 2025b). Periodicity generalization is the ability to extract periodic patterns from observed data and generalize to unseen scenarios. For humans, it reflects the ability to perform abstract inference from known to unknown. For models, it reflects the ability to generalize learned periodic patterns from training data to OOD scenarios.

Periodicity can be expressed using abstract algebra (Dummit & Foote, 2004; Brin & Stuck, 2002). The essence of periodicity is invariance under specific transformations. When inputs or rules recur in temporal, spatial, or abstract forms, new instances can be inferred based on previously observed periodic patterns, which is a core feature of reasoning (Dong et al., 2025a).

To this end, we introduce a unified interpretation of periodicity from the perspective of abstract algebra and reasoning, describing periodicity in time-series and reasoning. Our interpretation explains why Transformers struggle to generalize periodicity. From this, we further introduce the concept of **composite periodicity**, which describes the interaction and composition of multiple periodicities.

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

Then we construct **Coper**, a dataset to characterize **Combinations** and transformations of different **periodicities**, including training and test sets. The test set contains two challenging OOD settings: **① Hollow**: the periods of the test samples remain within the training distribution, but certain period composition is deliberately removed from the training set, to evaluate the model's **interpolation ability**; **② Extrapolation**: the periods of the test samples lie beyond the training distribution, to evaluate the model's **extrapolation ability**.

As shown in Figure 1, experiments show that the Transformers can memorize seen composite periods during training, but struggle in OOD settings. Other model architectures (*e.g.*, Mamba,

RWKV) and existing periodicity modeling works (*e.g.*, FANformer) exhibit similar failures. We further discover three interesting findings: 1) Transformers with RoPE struggle to generalize single periodicity under non-invariant transformations. 2) Transformers struggle to generalize composite periodicity, even when the underlying single periods are seen during training. 3) Increasing data density or model scale improves performance in the Hollow setting, but only by a margin in Extrapolation.

Our contributions are summarized as follows:

1. **A group-theoretic view of periodicity**: proposing a unified interpretation of periodicity, and deriving the boundary of periodicity modeling in Transformers with RoPE under shift-group relative-position invariance.
2. **A dataset for composite periodicity**: constructing a controllable, generative **Coper** dataset with Hollow and Extrapolation scenarios to evaluate models' periodicity generalization ability;
3. **Limits of periodicity generalization**: experiments demonstrate that existing models can memorize seen periods, but struggle to generalize periodicity.

## 2 RELATED WORK

### 2.1 OUT-OF-DISTRIBUTION GENERALIZATION

Out-of-distribution (OOD) generalization studies how models generalize learned patterns when the test distribution differs from the training distribution (Shen et al., 2021; Yu et al., 2024). Several works (Wu et al., 2025; Gagnon-Audet et al., 2023) analyze OOD generalization of neural networks in time series and real-world settings, showing that performance can drop sharply under distribution shifts, even when in-distribution accuracy is high. Other works (Nam et al., 2022; Ouellette et al., 2023; de Luca et al., 2024; Huang et al., 2025; Altabaa et al., 2025; Hu et al., 2025; Chang & Bisk, 2025) investigate OOD generalization on logic and reasoning tasks, finding that standard Transformers can fit the training distribution but often fail on variations of the same underlying rules or on much longer inputs.

However, most existing works focus on a single task or a single rule. Generalization across composition of multiple tasks or rules, where models need to compose learned patterns, receives little study (Sinha et al., 2024). Learning by Analogy (Kong et al., 2025) introduces a causal framework for compositional generalization in visual reasoning. Our work treats periodicity as a basic OOD scenario and provides a unified interpretation that links periodic patterns with rule composition.

### 2.2 PERIODICITY MODELING

Periodicity is a basic pattern that naturally appears in physical and biological processes. Several works (Wu et al., 2021; Zhou et al., 2022; Woo et al., 2022; Liang et al., 2024; Kui et al., 2025) explicitly model periodicity in time-series forecasting to capture seasonal patterns and long-term dependencies. Autoformer (Wu et al., 2021) decomposes a time series into trend and seasonal components and uses an auto-correlation mechanism to capture periodicity for long-horizon forecasting.

![img-0.jpeg](img-0.jpeg)

Figure 1: Accuracy heatmaps of Transformer and FANformer on composite periodicity tasks in **Coper**. Models perform well on seen composite periods, but accuracy drops in Hollow and Extrapolation OOD settings, showing limits in periodicity generalization. The full results are shown in Figure 3.

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

FEDformer (Zhou et al., 2022) introduces a frequency-enhanced Transformer that replaces standard attention with Fourier and wavelet blocks to improve long-horizon forecasting.

However, the above approaches only study periodicity in in-distribution settings and do not consider OOD scenarios. FAN (Dong et al., 2025b) extends periodicity modeling to OOD scenarios using a Fourier-based module. FANformer (Dong et al., 2025a) further connects periodicity with reasoning, and scales the FAN model to 1B parameters. Through large-scale pretraining of a 1B-parameter model, FANformer (Dong et al., 2025a) integrates FAN into the Transformer architecture, demonstrating that periodicity modeling influences both language modeling and reasoning performance. However, both still struggle with composite periodicity.

### 3 UNIFIED INTERPRETATION OF PERIODICITY VIA GROUP THEORY

In this section, we present our unified interpretation of periodicity via group theory. Section 3.1 formalizes the group-theoretic definition of periodicity. Section 3.2 then generalizes the above definition to rule periodicity, grounded in concrete reasoning examples. Section 3.3 explains the limitations of Transformers in generalizing rule periodicity. Finally, Section 3.4 introduces composite periodicity, extending this limitation to composed periodic rules.

### 3.1 GROUP-THEORETIC DEFINITION OF PERIODICITY

Let $X$ be the value space (for example $X = \mathbb{R}$). Consider a discrete sequence defined as a function $f : \mathbb{Z} \to X$. Suppose that there exists $T \in \mathbb{N}^+$ such that

$$f(t + T) = f(t), \quad \forall t \in \mathbb{Z},$$

then we say $f$ admits the sequence period $T$. Since $T \in \mathbb{N}^+$, we can assume that $T$ is the minimal positive period among all periods without loss of generality. This description shows the periodicity in the temporal dimension.

From the perspective of abstract algebra, the essence of periodicity is to remain invariant under transformation (Dummit & Foote, 2004; Brin & Stuck, 2002). Let $X$ be an object space (for example, functions, numbers, or positions), and a group $G$ acts on $X$. Suppose that there exists a non-identity element $g \in G$ and a minimal integer $n \in \mathbb{N}^+$ such that

$$g^n \cdot x = x, \tag{1}$$

then we say that the element $x \in X$ is periodic under the left $g$-action. The minimal positive period is defined as

$$T(x \mid g) := \min \left\{ n \in \mathbb{N}^+ \mid g^n \cdot x = x \right\}. \tag{2}$$

The above definition naturally describes the invariance of periodic functions under group actions. For instance, consider a periodic sequence

$$f : \mathbb{Z} \to \mathbb{R}, \quad f(t + T) = f(t), \forall t \in \mathbb{Z},$$

the corresponding shift group is $G = \langle g \rangle$, and the left group action is defined to be$^1$

$$g \cdot f := \phi_g(f) : t \mapsto f(g^{-1} \cdot t) = f(t - 1).$$

Hence, the generator $g$ acts on functions repetitively:

$$g^n \cdot f(t) = g^{n-1} \cdot \phi_g(f)(t) = g^{n-1} \cdot f(t - 1) = \dots = f(t - n).$$

Therefore, the minimal positive period under the group action on $f$ is

$$\begin{array}{l} T(f \mid g) := \min\{n \in \mathbb{N}^+ \mid g^n \cdot f = f\} \\ = \min\{n \in \mathbb{N}^+ \mid f(t - n) = f(t), \forall t \in \mathbb{Z}\} = T. \end{array}$$

We call this sequence periodicity, the repetitive pattern of the input sequence itself.

$^1$Here we use the inverse to ensure the associativity in the induced action. Otherwise, if $g \cdot f(t) := f(g \cdot t)$, then $g_1 \cdot (g_2 \cdot f(t)) = g_1 \cdot \phi_{g_2}(f)(t) = \phi_{g_2}(f)(g_1 \cdot t) = f(g_2 \cdot (g_1 \cdot t)) \neq f((g_1 \cdot g_2) \cdot t) = (g_1 \cdot g_2) \cdot f(t)$. The equation does not hold when the group is not abelian. Inverse solves this problem due to $(g_1 \cdot g_2)^{-1} = g_2^{-1} \cdot g_1^{-1}$.

## A-page-0004

target PDF page 4

Our group-theoretic definition applies not only to sequence periodicity, but also rule periodicity (discussed in Section 3.2). When the mapping relationship is preserved for inputs or rules under transformations, it can also be viewed as invariance under the action of the corresponding transformation group.

### 3.2 RULE PERIODICITY IN REASONING

Reasoning tasks often exhibit rule periodicity, referring to the repetition of the same rule. We still use the group action interpretation in Section 3.1. Let the rule set be $\mathcal{R} = \{R_k\}_{k \in I}$, the index set be $I = \mathbb{Z}$, and the value space be $V = \{0, \ldots, p - 1\}$, and we introduce two types of group:

- Shift group $G_\tau = \langle \tau \rangle \simeq \mathbb{Z}$: the generator $\tau$ acts as $\tau \cdot k = k + 1$.
- Modulo group $G_\sigma = \langle \sigma \rangle \simeq \mathbb{Z}_p$: the generator $\sigma$ acts as $\sigma \cdot x = x + 1 \pmod p$.

Now we define two primitive reasoning rules as mappings (with position parameter $k$):

① Digit-wise addition without carry:

$$R_k : \mathbb{Z} \times \mathbb{Z} \to \mathbb{Z}, \qquad (x_k, y_k) \mapsto x_k + y_k.$$

The shift group $G_\tau = \langle \tau \rangle$ acts on the index set $I$ as $\tau \cdot k = k + 1$, and the induced action on the rule set $\mathcal{R}$ is

$$\tau \cdot R_k = R_{\tau^{-1} \cdot k} = R_{k-1}, \quad \tau^n \cdot R_k = R_{k-n}.$$

If there exists $T \in \mathbb{N}^+$ such that

$$\tau^T \cdot R_k = R_k, \quad \forall k \in \mathbb{Z},$$

then the rule $R_k$ is said to admit a period of length $T$ along the positional dimension. For digit-wise addition without carry$^2$, the same rule is applied identically at adjacent positions. Therefore, $R_k$ satisfies $T = 1$.

The shift group $G_\tau$ acts on the rule set $\mathcal{R}$, rather than on a specific input sequence, which induces a group action over the entire function space. As a concrete example, consider the computation of $342 + 117$, units: $2 + 7 = 9$; tens: $4 + 1 = 5$; hundreds: $3 + 1 = 4$, resulting in the sequence 459, where the digit-wise addition rule is applied repeatedly at each position.

② Single-position modulo:

$$M_k : \mathbb{Z} \to \mathbb{Z}_p, \qquad x_k \mapsto x_k \pmod p.$$

The modulo group $G_\sigma = \langle \sigma \rangle$ acts on the value space $V$ as $\sigma \cdot x = x + 1 \pmod p$. Under this action, the modulo mapping satisfies

$$M_k(\sigma^{T_2} \cdot x_k) = (x_k + T_2) \pmod p = x_k \pmod p = M_k(x_k),$$

so the modulo operation has the period length $T_2 = p$ on the value space.

From the perspective of function space, the modulo operation can be viewed as the result of shift group acting on rule set $\mathcal{R} = \{M_k : \mathbb{Z} \to \mathbb{Z}_p\}$, i.e., the same modulo rule being applied on different position $k$. This shows the same rule periodicity as in the addition rules. Here the period length for $M_k$ is $T_2' = 1$ on the index set.

In summary, digit-wise addition and single-position modulo operation can be seen as periodically invariant mapping, respectively under the action of shift group and modulo group. This structural repetition shows the rule periodicity in reasoning: the same rule being repeated in position or value space. Rule periodicity reflects the model's capability of reuse and generalization.

### 3.3 LIMITATION OF TRANSFORMERS IN PERIODICITY GENERALIZATION

#### 3.3.1 SHIFT EQUIVARIANCE PRESERVED BY TRANSFORMER WITH ROPE

$^2$ Digit-wise addition with carry can be expressed as a combination of the modulo group and the shift group; see Section 3.4 for details on composite periodicity.

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

We first clarify what kinds of periodicity Transformers with RoPE are able to generalize. Let $f : \mathbb{Z} \to X$ be an input sequence, and let $G = \langle g \rangle$ be a shift group.

**Proposition.** If $f$ satisfies the sequence periodicity $g^T \cdot f = f$, then a Transformer with RoPE preserves the shift equivariance:

$$\mathcal{T}(g^T \cdot f) = g^T \cdot \mathcal{T}(f). \tag{3}$$

The proof follows from the equivariance of position-wise operations (i.e., MLP, activation function, layer normalization, and residual connection), self-attention with RoPE relative positions, and layer composition. Full proof is provided in Appendix B.1.

In particular, when the input sequence satisfies the sequence periodicity $g^T \cdot f = f$, i.e., $f(t) = f(t + T), \forall t \in \mathbb{Z}$, Transformer with RoPE preserves the

equivariant structure induced by the corresponding shift-group invariance as characterized in Eq. 3. From the proof, sequence periodicity further implies relative position invariance: for all $i, j$, we have

$$f(i) - f(j) = f(i + T) - f(j + T). \tag{4}$$

As a result, Transformers with RoPE can capture sequence periodicity satisfying Eq. 4. Without RoPE (e.g., using absolute positional encodings), the periodicity generalization ability of Transformers is substantially weaker. Experimental evidence supporting our proof is provided in the top of Figure 2 (see Appendix B.2 and B.3 for details).

### 3.3.2 LIMITATION IN CAPTURING RULE PERIODICITY

In reasoning tasks, **rule periodicity** is more crucial, i.e., repeating and reusing the same rule on different structures. Rule periodicity satisfies $R_{k+T} = R_k$, which is different from sequence periodicity: a rule $R$ is applied to sequence $f$ and obtains $R_k(f(k))$, and it repeats on every position **without relying on relative position difference** of the sequence. Now we present a concise proof that Transformers struggle to generalize rule periodicity.

**Proof.** Assume $R_i$ possesses a period that is different from $T$, which is the period of $f$. On one hand, $f$ satisfies $g^T \cdot f = f$, where $\langle g \rangle$ is the shift group acting on the function space. On the other hand, $R_i$ does not exhibit the same shift invariance. In general, the two group actions do not commute with $R_i$, i.e.,

$$\tau^T \cdot R_i \neq R_i \circ g^{-T}. \tag{5}$$

If Eq. 5 does not hold, we would have

$$\begin{array}{l} R_{i+T}(f(i + T)) - R_{j+T}(f(j + T)) \\ = R_{i+T}(g^{-T} \cdot f(i)) - R_{j+T}(g^{-T} \cdot f(j)) \\ = \tau^T \cdot R_{i+T}(f(i)) - \tau^T \cdot R_{j+T}(f(j)) \\ = R_i(f(i)) - R_j(f(j)). \end{array}$$

Unfortunately, Eq. 5 holds in general. So for all $i, j \in \mathbb{Z}$, we generally have

$$R_i(f(i)) - R_j(f(j)) \neq R_{i+T}(f(i + T)) - R_{j+T}(f(j + T)), \tag{6}$$

which means that rule periodicity does not satisfy shift invariance in general.

Hence, by Eq. 4, Transformers with RoPE preserve shift equivariance and can generalize **sequence periodicity**. However, Transformers with RoPE struggle to generalize rule periodicity according to Eq. 6. Experimental evidence supporting our proof is provided in the bottom of Figure 2 (see Appendix B.4 for details).

![img-1.jpeg](img-1.jpeg)

Figure 2: Top: Transformer with RoPE generalizes well for under invariance transformation ($f(t + T) = f(t)$). Bottom: Single-period sequences under a non-invariant transformation ($f(t + T) = 2 \cdot f(t)$), showing the generalization failure.

## A-page-0006

target PDF page 6

### 3.4 COMPOSITE PERIODICITY

To further explore the limitation of Transformer architecture, we introduce the formal definition of composite periodicity. Assume there are two periodic sequences: $f_1 : X_1 \to Y_1$, $f_2 : X_2 \to Y_2$, and define composite operation:

$$C(f_1(t), f_2(t)) := (M \circ R)(f_1(t), f_2(t)), \tag{7}$$

for example modular addition:

$$C(f_1(t), f_2(t)) = (f_1(t) + f_2(t)) \pmod{p}.$$

We further define the group structure of basic reasoning modulo rule. Let $G_R = G_\tau = \langle \tau \rangle$ be the shift group acting on addition rules in position space, and $G_M = G_\sigma = \langle \sigma \rangle$ be the modulo group acting on the modulo operation rules. In the perspective of group theory, the composite group acting on reasoning modulo rules can be presented by direct product:

$$G = G_R \times G_M = \langle \tau \rangle \times \langle \sigma \rangle, \tag{8}$$

and the induced action is

$$(\tau^i, \sigma^j) \cdot (R_k, M_k) = (R_{\tau^{-i} \cdot k}, M_k \circ \sigma^j) = (R_{k-i}, M_k(\cdot + j)). \tag{9}$$

If the composite group $G$ defined by Eq. 8 is non-invariant according to Eq. 6, Transformers cannot generalize such composite periodicity. We summarize the types of periodicity and their corresponding group-theoretic formulation in Table 4 in Appendix B.

Next, Section 4 constructs datasets based on our interpretation, and Section 5 evaluates the performance of multiple models on various composite periodicity tasks as support.

## 4 DATASET

![img-2.jpeg](img-2.jpeg)

Figure 3: Full accuracy heatmaps across all baseline models on composite periodicity tasks, corresponding to the final models trained as in Figure 5. Notably, even when trained for 1000 epochs, RWKV and Mamba still fail to fit.

To investigate the generalization ability of existing model architectures in composite periodicity scenarios, we construct Coper, a fully controllable and generative dataset for composite periodicity. Coper contains 50k training samples and 3k test samples. Using our data construction script (see supplementary material), Coper can be easily scaled to construct more samples. Moreover, by modifying our script, new composite periodicity tasks (e.g., the convolution) can be constructed.

We compose the rules $R_k$ and $M_k$ introduced in Section 3.4, and define a modulo addition operator $C$, which is explicitly unfolded along the time dimension as

$$\begin{array}{l} C(f_1(t), f_2(t)) = (M \circ R)(f_1(t), f_2(t)) \\ = (f_1(t \bmod P_1) + f_2(t \bmod P_2)) \bmod P. \end{array}$$

If the periodicity conditions in Eqs. 1 & 2 are satisfied, such periodicity compositions can also be interpreted under our proposed unified interpretation (e.g., convolution tasks; see Section 5.4 for experiments).

We set the training period range as $L \le P_1, P_2 \le U$, where $L$ and $U$ denote the lower and upper bounds of the training range, respectively. The training set contains the combinations $\mathcal{P}_{train} = \{(P_1, P_2) \mid P_1, P_2 \in [L, U], (P_1, P_2) \notin \mathcal{P}_{test}^{hollow}\}$.

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

During dataset construction, we deliberately introduce two types of OOD settings, Hollow and Extrapolation, to analyze two types of model generalization: interpolation and extrapolation. Each OOD setting contains 1k test samples, in addition to 1k in-distribution test samples. More hyperparameters are listed in Appendix A.

(1) Hollow We define the deliberately held-out hollow combinations within the training range as

$$\mathcal{P}_{test}^{hollow} = \{H_1, H_2, \dots, H_m\} \subset [L, U]^2,$$

These hollows are located inside the training range $[L, U]$, adjacent to trained combinations; however, they are not included in training. Hollow evaluates the model's interpolation ability to infer unseen composite periodic rules from adjacent, in-distribution combinations.

(2) Extrapolation We define the new combinations outside the training range as

$$\mathcal{P}_{test}^{extra} = \{(P_1, P_2) \mid P_1 \notin [L, U] \text{ or } P_2 \notin [L, U]\}.$$

Extrapolation evaluates the model's extrapolation ability to infer OOD composite periodic rules from the training distribution.

## 5 EXPERIMENTS

![img-3.jpeg](img-3.jpeg)

Figure 4: Accuracy of different models on composite periodicity tasks in Coper across different OOD settings.

![img-4.jpeg](img-4.jpeg)

Figure 5: Loss curves on ID and OOD testsets during training.

### 5.1 FAILURE OF PERIODICITY GENERALIZATION ACROSS DIFFERENT ARCHITECTURES

In the first experiment, we evaluate the fitting and generalization abilities of different model architectures about composite periodicity. In addition to the Transformer, we include representative architectures for periodicity including FANFormer (Dong et al., 2025a), as well as recently discussed architectures, Mamba and RWKV as baselines. And different models' loss curves on in-distribution and OOD test sets during training are shown in Figure 5. Unless otherwise speci-

Table 1: Performance comparison across different model architectures on composite periodicity tasks. ID denotes in-distribution.

[tbl-0.html](tbl-0.html)

fied, all models are trained and evaluated using the same random seeds and hyperparameter settings (provided in Appendix A). For evaluation metrics, we report the final test loss on the in-distribution and OOD splits, test accuracy on the in-distribution, Hollow, and Extrapolation splits, together with the overall average. The results are reported in Table 1, Figure 3 and Figure 4.

The results show that the Transformer struggles to generalize composite periodicity in OOD scenarios. Although the Transformer fits the training distribution well, with 99.8% in-distribution accuracy, its accuracy on unseen combinations is low, with only 36.4% on Hollow and 24.4% on Extrapolation. Architectures designed for periodicity modeling do not resolve this limitation. FANFormer also achieves high in-distribution accuracy at 89.5%, while performance on Hollow and Extrapolation remains low at 41.7% and 19.4%. In contrast, state-based models show much weaker fitting under the

[OCR table id=tbl-0.html; page=7]
<table><tr><td rowspan="2">Model</td><td colspan="2">Testset Loss ↓</td><td rowspan="2">ID</td><td rowspan="2">Hollow</td><td rowspan="2">Extrapolation</td><td rowspan="2">Avg.</td></tr><tr><td>ID</td><td>OOD</td></tr><tr><td>Transformer</td><td>0.05</td><td>3.89</td><td>99.8</td><td>36.4</td><td>24.4</td><td>53.5</td></tr><tr><td>Fanformer</td><td>0.47</td><td>3.15</td><td>89.5</td><td>41.7</td><td>19.4</td><td>50.2</td></tr><tr><td>Mamba</td><td>1.33</td><td>1.48</td><td>49.5</td><td>43.1</td><td>45.3</td><td>46.0</td></tr><tr><td>RWKV</td><td>0.95</td><td>1.09</td><td>64.4</td><td>62.6</td><td>60.4</td><td>62.5</td></tr></table>

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

same training budget. Importantly, OOD generalization can only be interpreted when in-distribution fitting is sufficient. RWKV reaches 62.6% on Hollow and 60.4% on Extrapolation, but in-distribution accuracy is only 64.4%, far below the Transformer. Overall, existing architectures struggle to support both accurate in-distribution fitting and OOD generalization simultaneously, and none truly learn the composite periodicity R.

## 5.2 EFFECT OF DATA DENSITY OOD GENERALIZATION

In the second experiment, we further investigate the effect of training data density on OOD generalization. Intuitively, the Hollow lies within the training distribution, and the neighboring period combinations of the Hollow are all observed during training. A natural question is whether reducing the hollow size, i.e., making the training data denser, enables models to fill the missing combinations via interpolation. To this end, while keeping the number of training samples fixed, we shrink the period range from [2, 16] to a denser range of [2, 11] to explicitly control the hollow size, retaining only a hollow combination H = (6, 7) ∪ (7, 7).

![img-5.jpeg](img-5.jpeg)

Figure 6: Accuracy heatmaps with increased training data density.

The results are shown in Figure 6 and Figure 12. Increasing training data density improves interpolation in the Hollow setting. For example, the Transformer achieves 56.5% on Hollow, compared with 29.8% reported in Table 1, indicating an increase of +26.7% through denser training data. However, performance on Extrapolation remains largely unchanged (22.7% vs 22.6%). FANFormer exhibits similar trends: higher accuracy in Hollow but minimal margin in Extrapolation. These findings indicate that denser training data improves performance in the Hollow, but has minimal margin on Extrapolation, showing that models do not learn the composite periodicity R. More details are shown in Appendix D.

## 5.3 SCALING MODEL AND DATA SIZE FOR GENERALIZATION

In the third experiment, we study the effect of model scale on generalization of composite periodicity. The previous experiments show that, under a fixed model scale, both different architectures and different data densities suffer from clear generalization failures in the Hollow and Extrapolation settings. A natural question is whether these failures are caused by insufficient model capacity. We gradually increase the number of layers to scale model parameters and evaluate the generalization performance in the Hollow and Extrapolation settings. All models are trained for the same number of epochs on identical training data.

The results of scaling model parameters are reported in Table 5. Increasing the number of layers consistently improves generalization in both Hollow and Extrapolation settings. For instance, the Transformer improves from 29.8% to 57.2% on Hollow and from 22.6% to 32.7% on Extrapolation when scaling from 3 to 7 layers. FANFormer shows similar trends, with OOD loss decreasing from 3.21 to 2.09. These results show that larger models improve OOD generalization for composite periodicity. However, Extrapolation performance remains below in-distribution accuracy, and such improvement comes at the cost of computational overhead, which will be discussed in Section 6. More details are shown in Appendix E.

## 5.4 FAILURE UNDER OTHER COMPOSITE PERIODICITY

Previous experiments analyzed the failure of generalization for composite periodicity from the perspectives of model architecture, data density, and model scale. However, they are based on the same composite periodicity. A key question is whether the observed failure depends on the specific rule periodicity or represents a more general phenomenon, as suggested in Section 3.3. Prior work conducted experiments on carry-addition tasks (Hu et al., 2024). In our final experiment, we use the circular convolution task as a new composite periodicity rule to further evaluate OOD generalization. The group-theoretic interpretation of circular convolution is provided in Appendix C.

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

![img-6.jpeg](img-6.jpeg)

Figure 7: Although Transformer fits the ID training data $y = \sin(x)$ within the range $[-6\pi, +6\pi]$ well, it struggles to preserve the same periodicity when extrapolating, where $x$ is a token sequence.

The results are reported in Table 2. Under circular convolution, models exhibit the same generalization failure observed in previous experiments. The Transformer achieves 80.6% in-distribution accuracy but performs poorly on Hollow and Extrapolation, with accuracies of 15.9% and 17.8%, respectively. State-based models like Mamba and RWKV struggle to fit the training distribution within the same training budget, re-

flecting low learning efficiency. Overall, the generalization failure persists across more composite periodicity scenarios, rather than being specific to a unique case. More details are shown in Appendix F and Appendix G.

Table 2: Performance comparison across different model architectures on circular convolution.

[tbl-1.html](tbl-1.html)

## 6 DISCUSSION

### 6.1 MORE TYPES OF PERIODICITY

Beyond sequence and rule periodicity, there exist hidden periodicity patterns, where individual samples do not show obvious repetition, and the periodicity only appears at the level of the full data distribution. An example is the sine function. Rather than being contained in one piece of data (e.g., 12341234 ···), the periodic patterns in the sine function can be learned only after seeing many $(x, y)$ data points across the distribution. We conduct an experiment to train a Transformer to fit $y = \sin(x)$. Consistent with Coper, we divide the data into in-distribution $[-6\pi, +6\pi]$ for training and OOD beyond this range. As shown in Figure 7, the Transformer fails to generalize such periodicity. More experimental details are provided in Appendix H. In real-world tasks, periodicity appears as combinations of different types.

### 6.2 HOLLOW, DATA DENSITY, AND SCALING BEHAVIOR

OOD performance is influenced by data density and model size, which helps explain “grokking” behavior observed during scaling (Power et al., 2022). Larger models and denser data enable stronger generalization beyond the training distribution. However, our group-theoretic interpretation and experiments show that increasing data density or model size does not enable rule generalization. Even with minimal Hollow size, missing periodic combinations remain unresolved. As large-scale pretraining data approaches saturation, further improvements require exponentially higher training cost or model parameters. Progress beyond Hollow and Extrapolation therefore requires model architectures to have at least the ability to represent reasonable OOD generalization, like periodicity.

## 7 CONCLUSION AND FUTURE WORK

Our work proposes a unified interpretation of periodicity and reasoning through group theory to explain why Transformers struggle to generalize periodicity. Based on this, we further propose the composite periodicity dataset Coper to enable controlled evaluation of periodicity generalization. Experiments show that current models fail in Hollow and Extrapolation scenarios, revealing the limitations of current architectures in periodicity generalization.

Our limitations include 1) not studying external reasoning mechanisms such as chain-of-thought (CoT) or memory, and 2) applying our interpretation only to Transformer with RoPE, without more models like Mamba. Future works include 1) extending the group-theoretic interpretation to more reasoning scenarios and 2) designing architectures that can model composite periodicity.

[OCR table id=tbl-1.html; page=9]
<table><tr><td rowspan="2">Model</td><td colspan="2">Testset Loss ↓</td><td rowspan="2">ID</td><td rowspan="2">Hollow</td><td rowspan="2">Extrapolation</td><td rowspan="2">Avg.</td></tr><tr><td>ID</td><td>OOD</td></tr><tr><td>Transformer</td><td>0.42</td><td>3.16</td><td>80.6</td><td>15.9</td><td>17.8</td><td>38.1</td></tr><tr><td>Fanformer</td><td>1.24</td><td>1.66</td><td>47.4</td><td>34.6</td><td>24.9</td><td>35.6</td></tr><tr><td>Mamba</td><td>1.99</td><td>2.05</td><td>17.7</td><td>15.4</td><td>17.2</td><td>16.8</td></tr><tr><td>RWKV</td><td>2.11</td><td>2.15</td><td>14.2</td><td>11.9</td><td>12.1</td><td>12.7</td></tr></table>

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

In preparing this manuscript, we use LLMs to assist with writing and coding. Specifically, LLMs improve clarity, grammar, and phrasing, ensuring the text is concise and readable. The use of LLMs does not influence the technical contributions or the interpretation of experimental findings. All content edited by LLMs was carefully checked by at least two authors.

## REFERENCES

Awni Altabaa, Siyu Chen, John Lafferty, and Zhuoran Yang. Unlocking out-of-distribution generalization in transformers via recursive latent space reasoning. CoRR, abs/2510.14095, 2025.

Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. On the dangers of stochastic parrots: Can language models be too big? In FAccT, pp. 610–623. ACM, 2021.

Michael Brin and Garrett Stuck. Introduction to dynamical systems. Cambridge university press, 2002.

Sébastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar, Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott M. Lundberg, Harsha Nori, Hamid Palangi, Marco Túlio Ribeiro, and Yi Zhang. Sparks of artificial general intelligence: Early experiments with GPT-4. CoRR, abs/2303.12712, 2023.

György Buzsáki. Rhythms of the Brain. Oxford university press, 2006.

Yingshan Chang and Yonatan Bisk. Language models need inductive biases to count inductively. In ICLR. OpenReview.net, 2025.

Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pondé de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, Alethea Power, Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe Tillet, Felipe Petroski Such, Dave Cummings, Matthias Plappert, Fotios Chantzis, Elizabeth Barnes, Ariel Herbert-Voss, William Hebgen Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain, William Saunders, Christopher Hesse, Andrew N. Carr, Jan Leike, Joshua Achiam, Vedant Misra, Evan Morikawa, Alec Radford, Matthew Knight, Miles Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario Amodei, Sam McCandlish, Ilya Sutskever, and Wojciech Zaremba. Evaluating large language models trained on code. CoRR, abs/2107.03374, 2021.

Artur Back de Luca, George Giapitzakis, Shenghao Yang, Petar Velickovic, and Kimon Fountoulakis. Positional attention: Out-of-distribution generalization and expressivity for neural algorithmic reasoning. CoRR, abs/2410.01686, 2024.

DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J. L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R. J. Chen, R. L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shutting Pan, and S. S. Li. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. CoRR, abs/2501.12948, 2025.

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

Yihong Dong, Ge Li, Xue Jiang, Yongding Tao, Kechi Zhang, Lecheng Wang, Hao Zhu, Huanyu Liu, jiazheng ding, Jia Li, Jinliang Deng, and Hong Mei. Reasoning is periodicity? improving large language models through effective periodicity modeling. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025a.

Yihong Dong, Ge Li, Yongding Tao, Xue Jiang, Kechi Zhang, Jia Li, Jinliang Deng, Jing Su, Jun Zhang, and Jingjing Xu. Fourier analysis network. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025b.

David S Dummit and Richard M Foote. Abstract algebra. john wile & sons. Inc., Hoboken, NJ, 2004.

Ahmed El-Kishky, Alexander Wei, Andre Saraiva, Borys Minaiev, Daniel Selsam, David Dohan, Francis Song, Hunter Lightman, Ignasi Clavera Gilaberte, Jakub Pachocki, Jerry Tworek, Lorenz Kuhn, Lukasz Kaiser, Mark Chen, Max Schwarzer, Mostafa Rohaninejad, Nat McAleese, o3 contributors, Oleg Mürk, Rhythm Garg, Rui Shu, Szymon Sidor, Vineet Kosaraju, and Wenda Zhou. Competitive programming with large reasoning models. CoRR, abs/2502.06807, 2025.

You-Le Fang, Dong-Shan Jian, Xiang Li, and Yan-Qing Ma. AI-newton: A concept-driven physical law discovery system without prior physical knowledge. CoRR, abs/2504.01538, 2025.

Tao Feng, Chuanyang Jin, Jingyu Liu, Kunlun Zhu, Haoqin Tu, Zirui Cheng, Guanyu Lin, and Jiaxuan You. How far are we from AGI: are llms all we need? Trans. Mach. Learn. Res., 2024, 2024.

Jean-Christophe Gagnon-Audet, Kartik Ahuja, Mohammad-Javad Darvishi Bayazi, Pooneh Mousavi, Guillaume Dumas, and Irina Rish. WOODS: benchmarks for out-of-distribution generalization in time series. Trans. Mach. Learn. Res., 2023, 2023.

Team Google. Gemma 3 technical report. CoRR, abs/2503.19786, 2025.

Yi Hu, Xiaojuan Tang, Haotong Yang, and Muhan Zhang. Case-based or rule-based: How do transformers do the math? In ICML. OpenReview.net, 2024.

Yi Hu, Shijia Kang, Haotong Yang, Haotian Xu, and Muhan Zhang. Beyond single-task: Robust multi-task length generalization for llms, 2025. URL https://arxiv.org/abs/2502.11525.

Xinting Huang, Andy Yang, Satwik Bhattamishra, Yash Raj Sarrof, Andreas Krebs, Hattie Zhou, Preetum Nakkiran, and Michael Hahn. A formal framework for understanding length generalization in transformers. In ICLR. OpenReview.net, 2025.

Lingjing Kong, Shaoan Xie, Yang Jiao, Yetian Chen, Yanhui Guo, Simone Shao, Yan Gao, Guangyi Chen, and Kun Zhang. Learning by analogy: A causal framework for composition generalization, 2025. URL https://arxiv.org/abs/2512.10669.

Yeganeh Kordi, Nihal V. Nayak, Max Zuo, Ilana Nguyen, and Stephen H. Bach. Revisiting generalization across difficulty levels: It's not so easy, 2025. URL https://arxiv.org/abs/2511.21692.

Xiaoyan Kui, Canwei Liu, Qinsong Li, Zhipeng Hu, Yangyang Shi, Weixin Si, and Beiji Zou. TFKAN: time-frequency KAN for long-term time series forecasting. CoRR, abs/2506.12696, 2025.

Brenden M Lake, Tomer D Ullman, Joshua B Tenenbaum, and Samuel J Gershman. Building machines that learn and think like people. Behavioral and brain sciences, 40:e253, 2017.

Daojun Liang, Haixia Zhang, Dongfeng Yuan, and Minggao Zhang. Periodformer: An efficient long-term time series forecasting method based on periodic attention. Knowl. Based Syst., 304:112556, 2024.

Yuanhang Liu, Yanxing Huang, Yanqiao Wang, Peng Li, and Yang Liu. AI mathematician: Towards fully automated frontier mathematical research. CoRR, abs/2505.22451, 2025.

Ziming Liu, Yixuan Wang, Sachin Vaidya, Fabian Ruehle, James Halverson, Marin Soljacic, Thomas Y. Hou, and Max Tegmark. KAN: kolmogorov-arnold networks. CoRR, abs/2404.19756, 2024.

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

Andrew J. Nam, Mustafa Abdool, Trevor Maxfield, and James L. McClelland. Achieving and understanding out-of-distribution generalization in systematic reasoning in small-scale transformers, 2022. URL https://arxiv.org/abs/2210.03275.

OpenAI. GPT-4 technical report. CoRR, abs/2303.08774, 2023.

Sophocles J Orfanidis. Introduction to signal processing. Prentice-Hall, Inc., 1995.

Simon Ouellette, Rolf Pfister, and Hansueli Jud. Counting and algorithmic generalization with transformers. CoRR, abs/2310.08661, 2023.

Billy Perrigo. Meta's chief ai scientist yann lecun on agi, open-source, and ai risk. TIME, February 2024. URL [URL REDACTED]

Alethea Power, Yuri Burda, Harri Edwards, Igor Babuschkin, and Vedant Misra. Grokking: Generalization beyond overfitting on small algorithmic datasets. CoRR, abs/2201.02177, 2022.

Anonymous Repository. Periodicity generalization project repository. [URL REDACTED] 2026.

Robert Shapley, Peter Lennie, et al. Spatial frequency analysis in the visual system. Annual review of neuroscience, 8(1):547–581, 1985.

Zheyan Shen, Jiashuo Liu, Yue He, Xingxuan Zhang, Renzhe Xu, Han Yu, and Peng Cui. Towards out-of-distribution generalization: A survey. CoRR, abs/2108.13624, 2021.

Sania Sinha, Tanawan Premsri, and Parisa Kordjamshidi. A survey on compositional learning of AI models: Theoretical and experimental practices. Trans. Mach. Learn. Res., 2024, 2024.

Peiyang Song, Pengrui Han, and Noah Goodman. A survey on large language model reasoning failures. In 2nd AI for Math Workshop@ ICML 2025, 2025.

Ilya Sutskever. We're moving from the age of scaling to the age of research. YouTube video, November 2025. URL [URL REDACTED] Uploaded by Dwarkesh Patel.

Ryotaro Takehara. Comparative evaluation of novel neural network architectures. PhD thesis, The University of Texas at Austin, 2025.

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In NIPS, pp. 5998–6008, 2017.

Gerald Woo, Chenghao Liu, Doyen Sahoo, Akshat Kumar, and Steven C. H. Hoi. Etsformer: Exponential smoothing transformers for time-series forecasting. CoRR, abs/2202.01381, 2022.

Haixu Wu, Jiehui Xu, Jianmin Wang, and Mingsheng Long. Autoformer: Decomposition transformers with auto-correlation for long-term series forecasting. In NeurIPS, pp. 22419–22430, 2021.

Xin Wu, Fei Teng, Xingwang Li, Ji Zhang, Tianrui Li, and Qiang Duan. Out-of-distribution generalization in time series: A survey. CoRR, abs/2503.13868, 2025.

Han Yu, Jiashuo Liu, Xingxuan Zhang, Jiayun Wu, and Peng Cui. A survey on evaluation of out-of-distribution generalization. CoRR, abs/2403.01874, 2024.

Arnaud Zalta, Spase Petkoski, and Benjamin Morillon. Natural rhythms of periodic temporal attention. Nature communications, 11(1):1051, 2020.

Tian Zhou, Ziqing Ma, Qingsong Wen, Xue Wang, Liang Sun, and Rong Jin. Fedformer: Frequency enhanced decomposed transformer for long-term series forecasting. In ICML, volume 162 of Proceedings of Machine Learning Research, pp. 27268–27286. PMLR, 2022.

## A-page-0013

target PDF page 13

# A EXPERIMENTAL DETAILS OF TRAINING AND DATASET

Table 3: Training hyperparameters and dataset parameters.

[tbl-2.html](tbl-2.html)

Dataset Construction. Training sequences are sampled such that

$$(P_1, P_2) \in [4, 14]^2 \setminus \text{Hollow},$$

where Hollow defines a held-out region within the training range for interpolation evaluation.

The test set contains two types of OOD scenarios:

- Hollow: combinations within \([4, 14]^2\) but excluded from training, i.e., \(P_1, P_2 \in [8, 11]\).
- Extrapolation: combinations where \( P_{1} \) or \( P_{2} \) is outside the training range [4, 14], e.g., (1, 16), (2, 15), to evaluate extrapolation ability.

Each sequence is generated by sampling two sequences of length P$_{1}$ and P$_{2}$, repeating them to the least common multiple length, summing element-wise modulo 10, and concatenating as sequence1 + '+' + sequence2 + '='. The next-token prediction task is then defined over this sequence.

For example, let f$_{1}$(t) = (1, 2, 3) with period P$_{1}$ = 3 and f$_{2}$(t) = (1, 2) with period P$_{2}$ = 2. Then, their composition via Eq. 7 produces

$$\begin{array}{l} C(f_1(t), f_2(t)) \\ = (f_1(t \bmod 3) + f_2(t \bmod 2)) \bmod 10 \\ = (2, 4, 4, 3, 3, 5, \dots). \end{array}$$

We choose to use the pretrained Qwen2.5 tokenizer and embedding and keep them fixed during training to avoid introducing spurious numeric priors. Our prior experiments show that training embeddings from scratch on numeric tasks inadvertently allows the model to capture numeric magnitude information directly, which can lead to shortcut solutions and hack the intended evaluation of reasoning capability. By using fixed pretrained embeddings, we ensure that models rely on learned reasoning rather than trivial numeric cues, enabling a fair comparison across all models. All experiments are conducted on 8×A100 (40GB) GPUs for about few hours.

We train the model three times using fixed random seeds, evaluate each run separately, and report the averaged results. And for each model, we compute accuracy by performing token-wise comparisons between the model's predicted sequence and the ground-truth sequence, and averaging the correctness over all positions and all samples in the dataset.

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

[OCR table id=tbl-2.html; page=13]
<table><tr><th colspan="2">Training Hyperparameters</th></tr><tr><td>Batch size</td><td>32</td></tr><tr><td>Number of epochs</td><td>450</td></tr><tr><td>Learning rate</td><td>1 × 10<sup>-5</sup></td></tr><tr><td>Weight decay</td><td>0.01</td></tr><tr><td>Hidden state size</td><td>896</td></tr><tr><td>Model Layers</td><td>3 ~ 7</td></tr><tr><th colspan="2">Dataset Parameters</th></tr><tr><td>Number of training samples</td><td>50,000</td></tr><tr><td>Number of test samples</td><td>3,000</td></tr><tr><td>Sequence period range (train)</td><td>[4, 14]</td></tr><tr><td>Total range</td><td>[2, 16]</td></tr><tr><td>In-distribution pairs</td><td>(P<sub>1</sub>, P<sub>2</sub>) ∈ [4, 14]<sup>2</sup> \ Hollow</td></tr><tr><td>Hollow test pairs</td><td>P<sub>1</sub>, P<sub>2</sub> ∈ [8, 11]</td></tr><tr><td>Extrapolation test pairs</td><td>(P<sub>1</sub> or P<sub>2</sub> ∉ [4, 14])</td></tr><tr><td>Output token</td><td>0 ~ 9</td></tr></table>

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

## B FURTHER ANALYSIS: CAPACITY AND LIMITATIONS OF TRANSFORMER WITH ROPE IN PERIODICITY GENERALIZATION

[tbl-3.html](tbl-3.html)

Table 4: Types of periodicity and OOD generalization.

### B.1 EQUIVARIANCE OF LAYER NORMALIZATION, RESIDUAL CONNECTIONS, AND LAYER COMPOSITION

This appendix provides the detailed proof of Proposition 3 by showing that all core Transformer components preserve shift equivariance under the shift-group action. The proof consists of two parts. First, position-wise operations, including MLP, Layer Normalization, and residual connections, preserve shift equivariance since the same parameters are shared across all token positions. Second, self-attention preserves shift equivariance under the sequence periodicity condition $$g^T \cdot f = f$$ together with the relative position invariance introduced by RoPE.

**Proof.**

**① Position-wise operations.** MLP, activation, normalization, and residual connection are all position-wise (or token-wise) operations in Transformer, *i.e.*, they are independently applied to each position while sharing the same parameters across all positions. For example, the MLP satisfies

$$\text{MLP}(f(i)) = \text{Act}(f(i)W_1 + b_1)W_2 + b_2.$$

Under the shift group action in Section 3.1,

$$\begin{aligned} & \text{MLP}((g^T \cdot f)(i)) \\ &= \text{Act}(f(i - T)W_1 + b_1)W_2 + b_2 \\ &= \text{MLP}(f(i - T)) \\ &= (g^T \cdot \text{MLP}(f))(i). \end{aligned}$$

Therefore, position-wise operations preserve the same shift equivariance property. Since activation functions, normalization layers, and residual connections are also independently applied to each token and do not depend on the position index, the same shift equivariance property holds.

**② Residual Connection.** For a residual block,

$$\text{Res}(f)(i) = f(i) + F(f)(i),$$

where $$F$$ denotes a Transformer sublayer (e.g., MLP or self-attention).

Assume $$F$$ is shift equivariant, i.e.,

$$F(g^T \cdot f) = g^T \cdot F(f).$$

Then,

$$\begin{aligned} \text{Res}(g^T \cdot f)(i) &= (g^T \cdot f)(i) + F(g^T \cdot f)(i) \\ &= f(i - T) + F(f)(i - T) \\ &= \text{Res}(f)(i - T) \\ &= (g^T \cdot \text{Res}(f))(i). \end{aligned}$$

[OCR table id=tbl-3.html; page=14]
<table><tr><th>Periodicity Type</th><th>Group-theoretic Formulation</th><th>OOD Generalization</th></tr><tr><td>Shift-equivariant sequence periodicity</td><td>$$g^T \circ f = f$$, e.g., $$f(t + T) = f(t)$$</td><td>✓ Yes</td></tr><tr><td>Non-equivariant sequence periodicity</td><td>$$g^T \circ f \neq f$$, e.g., $$f(t + T) = 2f(t)$$</td><td>✗ No</td></tr><tr><td>Rule periodicity</td><td>$$R(g \circ f) = g \circ R(f)$$</td><td>✗ No</td></tr><tr><td>Composite periodicity</td><td>$$G = G_R \times G_M$$, $$(T^i, \sigma^j) \circ (R_k, M_k) = (R_{k-i}, M_k(\cdot + j))$$</td><td>✗ No</td></tr></table>

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

Thus,

$$\operatorname{Res}(g^T \cdot f) = g^T \cdot \operatorname{Res}(f).$$

**③ Layer Normalization.** Layer Normalization is applied independently to each token:

$$\operatorname{LN}(f(i)) = \gamma \frac{f(i) - \mu(f(i))}{\sigma(f(i))} + \beta,$$

where $\mu(\cdot)$ and $\sigma(\cdot)$ are computed over feature dimensions and are independent of the position index $i$.

Under the shift group action,

$$(g^T \cdot f)(i) = f(i - T),$$

we have

$$\mu((g^T \cdot f)(i)) = \mu(f(i - T)),$$

$$\sigma((g^T \cdot f)(i)) = \sigma(f(i - T)).$$

Therefore,

$$\begin{array}{l} \operatorname{LN}((g^T \cdot f)(i)) \\ = \gamma \frac{f(i - T) - \mu(f(i - T))}{\sigma(f(i - T))} + \beta \\ = \operatorname{LN}(f(i - T)) \\ = (g^T \cdot \operatorname{LN}(f))(i). \end{array}$$

Hence,

$$\operatorname{LN}(g^T \cdot f) = g^T \cdot \operatorname{LN}(f).$$

**④ Self-attention.** Let $Q_i = f(i) \cdot W_Q, K_i = f(i) \cdot W_K, V_i = f(i) \cdot W_V$. Since the linear projections are independently applied to each token,

$$Q_{i-T} = (g^T \cdot f)(i)W_Q = (g^T \cdot Q)(i).$$

and similarly for $K_i$ and $V_i$.

Consider two positions $(i, j)$ and their translated positions $(i + T, j + T)$. Under RoPE, the attention score depends on both token content and relative positional encoding,

$$s_{i,j} = \frac{Q_i K_j^\top}{\sqrt{d}} = h(f(i), f(j), \operatorname{RoPE}(i, j)).$$

Since $(i + T) - (j + T) = i - j$, the relative positional encoding remains unchanged:

$$\operatorname{RoPE}(i + T, j + T) = \operatorname{RoPE}(i, j).$$

We obtain

$$\begin{array}{l} s_{i,j} = h(f(i), f(j), \operatorname{RoPE}(i, j)) \\ = h(f(i + T), f(j + T), \operatorname{RoPE}(i + T, j + T)) \\ = s_{i+T, j+T}. \end{array}$$

The attention weight is

$$\alpha_{i,j} = \frac{\exp(s_{i,j})}{\sum_k \exp(s_{i,k})} = \alpha_{i+T, j+T}.$$

The attention output is

$$\operatorname{Attn}(f)(i) = \sum_j \alpha_{i,j} V_j.$$

Then,

$$\begin{array}{l} \operatorname{Attn}(g^T \cdot f)(i) = \sum_j \alpha_{i-T, j-T} V_{j-T} \\ = \sum_k \alpha_{i-T, k} V_k = \operatorname{Attn}(f)(i - T) \\ = (g^T \cdot \operatorname{Attn}(f))(i). \end{array}$$

## A-page-0016

target PDF page 16

⑤ Composition of Layers. A Transformer is a composition of layers:

$$\mathcal{T} = F_L \circ \dots \circ F_1.$$

We prove by induction that each composition preserves shift equivariance.

Base case. For $F_1$,

$$F_1(g^T \cdot f) = g^T \cdot F_1(f).$$

Inductive step. Assume

$$F_{k-1} \circ \dots \circ F_1(g^T \cdot f) = g^T \cdot (F_{k-1} \circ \dots \circ F_1)(f).$$

Then,

$$\begin{array}{l} F_k \circ \dots \circ F_1(g^T \cdot f) \\ = F_k \big(g^T \cdot (F_{k-1} \circ \dots \circ F_1)(f)\big) \\ = g^T \cdot F_k \big((F_{k-1} \circ \dots \circ F_1)(f)\big) \\ = g^T \cdot (F_k \circ \dots \circ F_1)(f). \end{array}$$

Thus,

$$\mathcal{T}(g^T \cdot f) = g^T \cdot \mathcal{T}(f).$$

Therefore, the complete Transformer preserves shift equivariance.

### B.2 FORMAL ILLUSTRATION OF ROPE AND SINGLE PERIOD SHIFT INVARIANCE

In Section 3.3, we dive into sequence periodicity and rule periodicity. Here we analyze how Transformer models simple sequence periodicity satisfying Eq. 4 through RoPE, for example the time shift invariance of a single periodic sequence $f(t) = f(t + T)$.

The core idea of RoPE is to map time step $t$ onto the phase rotation in the complex plane:

$$\text{RoPE}(x_t) = x_t e^{i\theta t}, \quad \theta = \frac{2\pi}{T},$$

where $T$ is the implicit period length. When a time shift $\Delta t$ occurs on the input sequence, we have

$$\begin{array}{l} \frac{\text{RoPE}(x_{t+\Delta t})}{\text{RoPE}(x_t)} = \frac{x_{t+\Delta t} \cdot e^{i\theta(t+\Delta t)}}{x_t \cdot e^{i\theta t}} \\ = \frac{x_{t+\Delta t}}{x_t} \cdot e^{i\theta \Delta t}, \end{array}$$

and if the periodicity ensures $x_{t+\Delta t} = x_t$, then

$$\text{RoPE}(x_{t+\Delta t}) = e^{i\theta \Delta t} \cdot \text{RoPE}(x_t),$$

hence shift equivariance remains in the self-attention computation:

$$\begin{array}{l} \langle \text{RoPE}(x_{t+\Delta t}), \text{RoPE}(x_{s+\Delta t}) \rangle \\ = \langle \text{RoPE}(x_t), \text{RoPE}(x_s) \rangle. \end{array}$$

This means that RoPE can realize the sequence shift invariance under single period $T$, therefore captures the simple sequence periodic pattern of the input sequence. We conduct an experiment to compare the ability of modeling single periodicity between RoPE and traditional absolute positional encoding (i.e., Sinusoidal Positional Encoding, SinPE) in Appendix B.3.

### B.3 EXPERIMENTAL VALIDATION OF ROPE MODELING SINGLE PERIODICITY

In Appendix B.2, we analyze how Transformer models simple sequence periodicity through RoPE. To prove that RoPE contributes to this, we conduct an experiment to compare RoPE with absolute positional encoding on the task of generalizing single periodicity.

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

![img-7.jpeg](img-7.jpeg)

![img-8.jpeg](img-8.jpeg)

Figure 8: Comparison of periodicity generalization between RoPE and absolute positional encoding.
In-distribution vs Out-of-distribution Test Set Loss Curves

![img-9.jpeg](img-9.jpeg)

Figure 9: Loss curves for models with RoPE and absolute positional encoding on single-periodicity generalization tasks. The SinPE means Sinusoidal Positional Encoding, which is an absolute positional encoding in the original Transformer.

We construct a periodic sequence continuation task. Given a periodic numerical sequence with more than two cycles, the model is required to predict the subsequent tokens. For example, here is an example for T = 6, where a single cycle is 955884:

Input: 9558849558849

Target output: 55884955884

The datasets are constructed as follows:

- Training Set (In-distribution): Sequences with periods T ∈ {4, 5, 6, 8, 9, 10}, totaling 10,000 samples.
- Test Set (OOD): Totaling 3,000 samples.
  - Hollow: Sequences with periods T = 7.
  - Extrapolation: Sequences with periods T ∈ {2, 3, 11, 12}.

We compare two transformer architectures: one with RoPE and another with absolute positional encoding. Both models are trained until convergence (100 epochs). The accuracy we use to measure

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

the performance is at the token level, which is the ratio of correctly predicted tokens across all predicted ones.

The result is shown in Fig. 8, where the two graphs represent the performance of two positional encoding, and the two colors stand for in-distribution and OOD generalization ability. Fig. 11 reports loss of both positional encodings on in-distribution and OOD datasets during training. We draw the following conclusions:

In the in-distribution scenario ($T \in \{4, 5, 6, 8,$

$9, 10\}$), RoPE and absolute positional encoding both achieve near 1.00 accuracy, indicating their common ability to memorize the seen periodic patterns. In the case of hollow interpolation ($T = 7$), RoPE remains a high accuracy, but the performance of absolute positional encoding drops significantly. In extrapolation cases ($T \in \{2, 3, 11, 12\}$), the accuracy of RoPE declines at a certain degree. On the contrast, the accuracy of absolute positional encoding is far less than RoPE's. The failure of absolute positional encoding on generalizing OOD cases proves its incompetence in modeling single periodicity. Notably, when $T = 2$, absolute positional encoding gains accuracy $\approx 0.80$, which is due to the features of absolute positional encoding. It captures low-range parity information, and gains advantages through even period lengths in training sets, which is not an evidence to the extrapolation ability of absolute positional encoding.

The result confirms the theoretical conclusion in Appendix B.2. By utilizing relative positional invariance compared to absolute positional encoding, RoPE has the ability to model single periodic patterns and make effective generalization. However, although RoPE performs well in generalizing single periodicity, it fails to generalize when facing composite periodicity as in Section 3.3.2.

### B.4 THE FAILURE OF ROPE MODELING SINGLE PERIODICITY UNDER NON-INVARIANT TRANSFORMATION

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)

Figure 10: Prediction accuracy on single-period sequences under a non-invariant transformation ($f(t + T) = 2 \cdot f(t)$) showing Transformer's failure with RoPE.

This appendix presents a counterexample showing that RoPE fails to model single periodicity when the underlying transformation violates relative positional invariance.

Consider a single-period sequence continuation task with period length $T$. The periodic transformation is defined as

$$f(t + T) = 2 \cdot f(t),$$

which induces a scale change across periods. Under this transformation, the relative positional relation is no longer preserved Eq.6. Therefore, the core assumption required for RoPE-based periodic modeling does not hold.

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

![img-12.jpeg](img-12.jpeg)

Figure 11: Loss curves for Transformer and FANformer with RoPE on single-period sequences under non-invariant transformations.

We train a Transformer equipped with RoPE on this task using the same training protocol as in the successful single-periodicity experiment in Appendix B.3. The model fails to learn the periodic continuation rule. As shown in Fig. 10, the prediction accuracy remains low across all evaluation settings. The training loss curve in Fig. 11 further indicates that the model does not converge to a stable solution.

These results demonstrate that RoPE cannot model single periodicity when the periodic structure involves non-invariant transformations. RoPE relies on relative positional consistency across cycles. When such consistency is violated, RoPE fails to support effective learning and generalization, even in the single-period setting.

This counterexample provides further verification of Eq. 6. Regardless of how the equation becomes invalid, whether by adding a composite periodicity as in Section 3.3.2 or by scaling the original periodic sequence, the model consistently fails to generalize the periodicity. Hence, the relative position invariance instilled by RoPE is crucial for periodicity generalization.

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

### C GROUP-THEORETIC INTERPRETATION OF CIRCULAR CONVOLUTION

In Section 5.4, we conduct an experiment utilizing circular convolution as another example of composite periodicity. Here we provide a theoretic explanation, demonstrating how circular convolution effectively represents composite periodicity.

Let $f_1, f_2 : \mathbb{Z}_N \to \mathbb{R}$ be two input sequences with period $P_1, P_2$, where $N$ is a common multiple of $P_1$ and $P_2$, usually $N = \text{lcm}(P_1, P_2)$. The circular convolution of $f_1, f_2$ is defined as

$$(f_1 * f_2)(t) := \sum_{n=0}^{N-1} f_1(n) \cdot f_2(t - n), \tag{10}$$

where $n$ and $t - n$ are calculated under modulo $P_1$ and $P_2$ respectively.

Now we use the group $G = \langle g \rangle \simeq \mathbb{Z}_N$ to induce an action on the sequence space $\mathcal{F} = \{f \mid f : \mathbb{Z}_N \to \mathbb{R}\}$. The group action is defined as

$$g \cdot t = t + 1 \pmod{N}.$$

The induced action is$^3$

$$g \cdot f(t) = f(g^{-1} \cdot t) = f(t - 1 \bmod N) = f(t - 1).$$

Hence, $g^n \cdot f(t) = f(g^{-n} \cdot t) = f(t - n)$.

For $i = 1, 2$, assume $\mathcal{G}_{P_i} := \langle g^{P_i} \rangle$, since $f_i$ has a period of $P_i$, for all $\gamma \in \mathcal{G}_{P_i}$ we have $\gamma \cdot f_i = f_i$, which implies the sequence periodicity. Because $P_i \mid N$, we have $g^n \cdot f_i(t) = f_i(t - n) = f_i(t - n \bmod P_i)$.

Therefore, we can reform Eq. 10 as:

$$f_1 * f_2 = \sum_{n \in \mathbb{Z}_N} f_1(n) \cdot (g^n \cdot f_2).$$

Next we prove that $g^k \cdot (f_1 * f_2) = (g^k \cdot f_1) * f_2$. On one hand,

$$(g^k \cdot (f_1 * f_2))(t) = (f_1 * f_2)(t - k) = \sum_{n \in \mathbb{Z}_N} f_1(n) \cdot f_2(t - k - n).$$

On the other hand,

$$((g^k \cdot f_1) * f_2)(t) = \sum_{n \in \mathbb{Z}_N} (g^k \cdot f_1)(n) \cdot f_2(t - n) = \sum_{n \in \mathbb{Z}_N} f_1(n - k) \cdot f_2(t - n).$$

Replace $n - k$ with $m$, then $n = k + m$, and as $n$ ranges over $\mathbb{Z}_N$, so does $m$. We have

$$((g^k \cdot f_1) * f_2)(t) = \sum_{m \in \mathbb{Z}_N} f_1(m) \cdot f_2(t - k - m).$$

This is the same formula as above, hence we have proved the equation.

Let $P = \text{lcm}(P_1, P_2)$, then $g^P \cdot f_1 = f_1$, and $g^P \cdot f_2 = f_2$. From this we know that the circular convolution $f_1 * f_2$ has a period of $P$:

$$g^P \cdot (f_1 * f_2) = (g^P \cdot f_1) * f_2 = f_1 * f_2, \quad i.e. (f_1 * f_2)(t - P) = (f_1 * f_2)(t).$$

This is exactly the composite periodicity of two independent sequence periods.

### D COMPLETE RESULTS FOR EFFECT OF TRAINING DATA DENSITY ON OOD GENERALIZATION (EXPERIMENT 2)

The full category accuracy bar and the loss curves after increasing data density are shown in Fig. 12 and Fig. 13. TFKAN (Kui et al., 2025) employs a dual time–frequency KAN (Liu et al., 2024) architecture that models nonlinear relationships and periodicity in time and frequency domains. In the following appendix, we include TFKAN as a baseline. The experimental results of KAN (or TFKAN) are similar to those reported in prior work (Takehara, 2025).

$^3$Here we use the inverse to ensure the associativity in the induced action. See footnote 1.

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

![img-13.jpeg](img-13.jpeg)

Figure 12: Category accuracy heatmap across models after increasing data density.

![img-14.jpeg](img-14.jpeg)

Figure 13: Loss curves on ID and OOD test sets after increasing data density.

### E COMPLETE EXPERIMENTAL RESULTS FOR SCALING MODEL PARAMETERS (EXPERIMENT 3)

The full results for different model and different parameter scales are shown in Table 5.

### F COMPLETE EXPERIMENTAL RESULTS FOR THE CIRCULAR CONVOLUTION TASK (EXPERIMENT 4)

The full accuracy heatmap, the category accuracy bar, and the loss curves for the circular convolution task are shown in Fig. 14, Fig. 15, and Fig. 16, respectively.

![img-15.jpeg](img-15.jpeg)

Figure 14: Heatmaps of model performance (450 training epochs) on the circular convolution task across different period lengths.

### G COMPLETE EXPERIMENTAL RESULTS FOR MORE COMPOSITE PERIODICITY

In Section 5, our main experiment evaluates models' ability to generalize composite periodicity using the Coper dataset introduced in Section 4. We utilize two rules: addition and modulo operation, which are both invariant, i.e., both with period T = 1. In this appendix, we further test models on additional composite periodicity to extend the concept of rule periodicity. We replace the addition rule with a periodic operation: applying addition and subtraction alternately. The composite operation can be formalized as

$$\begin{array}{l} C ^ {\prime} (f _ {1} (t), f _ {2} (t)) = (M \circ R ^ {\prime}) (f _ {1} (t), f _ {2} (t)) \\ = \left\{ \begin{array}{l} \left(f _ {1} (t \bmod P _ {1}) + f _ {2} (t \bmod P _ {2})\right) \bmod P, \quad 2 \mid t \\ \left(f _ {1} (t \bmod P _ {1}) - f _ {2} (t \bmod P _ {2})\right) \bmod P, \quad 2 \nmid t \end{array} \right. \\ = \left(f _ {1} (t \bmod P _ {1}) + (- 1) ^ {t} f _ {2} (t \bmod P _ {2})\right) \bmod P. \\ \end{array}$$

Consequently, the period of rule $R'$ becomes $T = 2$, and $R'_{t+2} = R'_t$.

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

![img-16.jpeg](img-16.jpeg)

Figure 15: Accuracy by category of different models on the circular convolution task on various OOD settings.

![img-17.jpeg](img-17.jpeg)

Figure 16: Loss curves on ID and OOD test sets during training on circular convolution tasks.

Table 5: Effect of model scaling on composite periodicity generalization. Importantly, OOD generalization can only be interpreted when in-distribution fitting is sufficient. With different ID performance and loss, OOD loss and OOD accuracy are not strictly positively correlated.

[tbl-4.html](tbl-4.html)

For example, let \( f_{1}(t) = (1,2,3) \) with period \( P_{1} = 3 \) and \( f_{2}(t) = (1,2) \) with period \( P_{2} = 2 \). Then, their composition produces

\[
\begin{array}{l} C ^ {\prime} (f _ {1} (t), f _ {2} (t)) \\ = \left(f _ {1} (t \bmod 3) + (- 1) ^ {t} f _ {2} (t \bmod 2)\right) \bmod P \\ = (2, 0, 4, 9, 3, 1, \dots). \\ \end{array}
\]

Fig. 17, Fig. 18, and Fig. 19 show the results of the experiment. Just like what happens in Section 5, the models fail to generalize the periodic patterns, whether in the hollow or in the extrapolation area. This experiment provides an additional verification of the conclusion in Section 3.3.2: when it fails to retain relative position difference, Transformer with RoPE fails to represent such periodicity.

## H FURTHER ANALYSIS OF HIDDEN PERIODICITY

This Appendix evaluates the generalization ability of the Transformer and other periodicity modeling works, such as FANFormer, on hidden periodicity. The experiment trains models to fit  \( y = \sin(x) \) . The training data is divided into in-distribution  \( [-6\pi, +6\pi] \)  for training and OOD beyond this interval.

To enable the Transformer's self-attention mechanism, \( x \) is tokenized into a fixed 10-digit sequence (e.g., +3.1415926), including the sign (+ or -), the decimal point, and digits 0–9. The model output

[OCR table id=tbl-4.html; page=22]
<table><tr><td rowspan="2">Model</td><td rowspan="2">Layers</td><td colspan="2">Testset Loss ↓</td><td rowspan="2">ID</td><td rowspan="2">Hollow</td><td rowspan="2">Extrapolation</td><td rowspan="2">Avg.</td></tr><tr><td>ID</td><td>OOD</td></tr><tr><td>Transformer</td><td>3</td><td>0.34</td><td>3.63</td><td>94.7</td><td>29.8</td><td>22.6</td><td>49.0</td></tr><tr><td>Transformer</td><td>5</td><td>0.05</td><td>3.89</td><td>99.8</td><td>36.4</td><td>24.4</td><td>53.5</td></tr><tr><td>Transformer</td><td>7</td><td>0.02</td><td>2.88</td><td>99.9</td><td>57.2</td><td>32.7</td><td>63.3</td></tr><tr><td>FANFormer</td><td>3</td><td>0.91</td><td>3.21</td><td>71.0</td><td>36.1</td><td>21.4</td><td>48.8</td></tr><tr><td>FANFormer</td><td>5</td><td>0.47</td><td>3.15</td><td>89.5</td><td>41.7</td><td>19.4</td><td>50.2</td></tr><tr><td>FANFormer</td><td>7</td><td>0.61</td><td>2.09</td><td>83.1</td><td>47.5</td><td>25.2</td><td>51.9</td></tr><tr><td>TFKAN</td><td>3</td><td>0.45</td><td>3.73</td><td>91.5</td><td>31.7</td><td>20.9</td><td>48.0</td></tr><tr><td>TFKAN</td><td>5</td><td>0.17</td><td>2.38</td><td>98.1</td><td>50.5</td><td>27.6</td><td>58.7</td></tr><tr><td>TFKAN</td><td>7</td><td>0.21</td><td>2.14</td><td>97.4</td><td>52.4</td><td>35.4</td><td>61.7</td></tr><tr><td>Mamba</td><td>3</td><td>1.36</td><td>1.42</td><td>49.4</td><td>48.4</td><td>46.7</td><td>48.2</td></tr><tr><td>Mamba</td><td>5</td><td>1.33</td><td>1.48</td><td>49.5</td><td>43.1</td><td>45.3</td><td>46.0</td></tr><tr><td>Mamba</td><td>7</td><td>1.47</td><td>1.63</td><td>45.6</td><td>42.0</td><td>36.0</td><td>41.2</td></tr><tr><td>RWKV</td><td>3</td><td>1.08</td><td>1.14</td><td>60.5</td><td>57.9</td><td>59.5</td><td>59.3</td></tr><tr><td>RWKV</td><td>5</td><td>0.95</td><td>1.09</td><td>64.4</td><td>62.6</td><td>60.4</td><td>62.5</td></tr><tr><td>RWKV</td><td>7</td><td>0.96</td><td>1.03</td><td>65.3</td><td>65.0</td><td>62.1</td><td>64.1</td></tr></table>

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

![img-18.jpeg](img-18.jpeg)

Figure 17: Heatmaps of model performance (450 training epochs) on the add–subtract alternating task across different period lengths.

![img-19.jpeg](img-19.jpeg)

Figure 18: Accuracy by category of different models on the add-subtract alternating task under various OOD settings.

![img-20.jpeg](img-20.jpeg)

Figure 19: Training loss curves of different models on the add-subtract alternating task.

is decoded back to numerical values using the same digit alignment. The Qwen2.5 tokenizer and embedding are frozen during training.

Beyond sequence and rule periodicity, we further define hidden periodicity, where individual samples do not exhibit explicit repetitive patterns, and the periodic structure only emerges at the level of the full data distribution. Formally, let the input be represented as a token sequence  \( (x_{1}, x_{2}, x_{3}, \ldots) \) . Hidden periodicity exists if there is a non-zero shift vector  \( (T_{1}, T_{2}, T_{3}, \ldots) \)  such that

\[
f (x _ {1}, x _ {2}, x _ {3}, \dots) = f (x _ {1} + T _ {1}, x _ {2} + T _ {2}, x _ {3} + T _ {3}, \dots).
\]

An example is the sine function. Although  \( \sin(x) \)  satisfies  \( \sin(x)=\sin(x+2\pi) \) , this periodicity cannot be directly observed from a single sample. Instead, after tokenization, adding one period changes multiple digit positions simultaneously due to carry operations. For example,

\[
\sin (+ 3. 1 4 1 5 9 2 6) = \sin (+ 6. 2 8 3 1 8 5 2),
\]

which corresponds to a coordinated token-level transformation such as

\[
f (x _ {1}, x _ {2}, x _ {3}, \dots) = f (x _ {1} + 3, x _ {2} + 1, x _ {3} + 4, \dots).
\]

Therefore, the periodicity can only be inferred after observing many \((x,y)\) pairs across the full data distribution.

As shown in Figure 20, FANFormer also fails to generalize hidden periodicity, similar to the Transformer.

![img-21.jpeg](img-21.jpeg)

Figure 20: FANformer fails to generalize  \( y = \sin(x) \) , where x is a token sequence
