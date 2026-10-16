# [TITLE C19]

## A-page-0001

target PDF page 1

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

# [TITLE C19]

Anonymous authors

Paper under double-blind review

# ABSTRACT

Controlling importance ratios in reinforcement learning with verifiable rewards requires retaining useful learning signals while limiting the influence of extreme policy deviations. Hard clipping can eliminate direct gradients for informative tokens, while unbounded ratio weighting can overemphasize outliers. We propose [NAME C19] ([NAME C19]), which separates these concerns through its gradient multipliers. A Log-Fidelity Modulator (LFM) preserves local ratio fidelity and supplies a smooth, positive, globally bounded multiplier. A Decoupled Hazard Penalty (DHP) uses established cumulative hazard functions to attenuate ratio expansions and contractions separately, without reversing their direct gradient contributions. Under an explicit assumption on the joint moment of advantages and score norms, we derive a local bound on the second moment of the gradient. We also explain how repeated ratio contractions accumulate along autoregressive prefixes. Component ablations, token masking, and diagnostics of directional tails connect these design choices to retained learning signals and reduced prefix contraction. Among the evaluated baselines, [NAME C19] achieves the best average across benchmarks on both Qwen3-4B-Base and Qwen3-30B-A3B-Base. Further evaluations on instruction-tuned and multimodal models support transfer across the tested settings.

# 1 INTRODUCTION

Reinforcement learning (RL) has become a central paradigm for the post-training of foundation models and unlocks extended chain-of-thought reasoning on complex mathematical and logical problems (Ouyang et al., 2022; OpenAI, 2024; Guo et al., 2025). Methods based on Group Relative Policy Optimization (GRPO) (Shao et al., 2024; Guo et al., 2025) have been scaled from small dense backbones to large Mixture-of-Experts (MoE) models, and are increasingly used as the default recipe for closing the gap between base models and the strongest reasoning-tuned counterparts. A parallel line of work has also extended GRPO beyond text, to vision-language models (Shen et al., 2025; Zhan et al., 2025; Yang et al., 2025b), which we cover in the appendix.

Despite these advances, ratio control presents a basic trade-off. In PPO/GRPO (Schulman et al., 2017; Shao et al., 2024), clipping removes the direct surrogate gradient when a token has already moved sufficiently far in its advantage-favored direction. This limits aggressive updates, but also discards potentially useful tail signals. Removing clipping restores those signals while exposing the update to large ratio-induced weights. DAPO (Yu et al., 2025), SAPO (Gao et al., 2025), CISPO (Chen et al., 2025), and MASPO (Fu et al., 2026) address this trade-off through different clipping or reweighting designs. Our question is how to retain a nonzero, advantage-aligned direct contribution while bounding its ratio-induced amplification and independently controlling directional attenuation.

Ratio direction adds a distinct consideration. We call $r_t > 1$ a ratio expansion and $r_t < 1$ a ratio contraction, both measured relative to the fixed behavior policy. These terms describe an existing probability displacement, not the advantage sign or the direction of the next update. Expanding a narrow set of tokens can concentrate learning. Contracting a useful token reduces the probability of every continuation sharing that prefix, holding the remaining conditional probabilities fixed. For autoregressive policies, the prefix likelihood ratio is $\exp(\sum_{j<t} \log r_j)$, so repeated contractions can

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

![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

![img-2.jpeg](img-2.jpeg)

![img-3.jpeg](img-3.jpeg)

![img-4.jpeg](img-4.jpeg)

![img-5.jpeg](img-5.jpeg)

Figure 1: Overview of [NAME C19]. (1–4) Ratio control proceeds from token importance ratios through log-space modulation and directional hazard attenuation to bounded gradient weighting. (5) Gains over Qwen3-4B-Base (Avg@32, percentage points) across five benchmarks. (6) Directional regulation and per-sample effective gradient shifts. Positive and negative shifts denote ratio expansion and contraction relative to the behavior policy. Sections 3 and 4.3 give the operator definitions and mechanism diagnostics.

compound even when each token-level change is modest. This multiplicative structure motivates separate control of expansion and contraction.

We propose [NAME C19] ([NAME C19]) to separate signal retention from directional damping (Fig. 1). The Log-Fidelity Modulator (LFM) maps log ratios through a scaled tanh, preserving the unclipped multiplier near the behavior-policy anchor while smoothly limiting outlier influence. The Decoupled Hazard Penalty (DHP) applies a detached survival weight from the established Weibull cumulative-hazard family (Cox & Oakes, 1984; Kalbfleisch & Prentice, 2002). Its positive weight attenuates each LFM contribution while preserving its direction. Separate branches allow stronger damping on the contraction side. Our contribution combines these operators and analyzes their gradient and prefix effects in policy optimization.

Our contributions are threefold. First, LFM and DHP provide positive bounded influence with separately configurable directional attenuation. Second, we derive a global-in-ratio multiplier bound and a local gradient moment certificate under a product-moment condition, together with the prefix identity that motivates contraction control. Third, evaluations and mechanism diagnostics connect the design to retained clipped-tail signals, reduced tail severity, and improved checkpoint retention. Appendix C gives the diagnostic definitions and derivations.

## 2 RELATED WORK

Ratio-control methods for GRPO. PPO (Schulman et al., 2017) and GRPO (Shao et al., 2024) motivate many recent RLVR objectives. DAPO (Yu et al., 2025) changes clipping boundaries, SAPO (Gao et al., 2025) uses soft gating, and GSPO (Zheng et al., 2025) uses sequence-level ratios. CISPO (Chen et al., 2025) clips detached importance weights rather than dropping the direct learning signal outside a clip boundary. GMPO (Zhao et al., 2025) changes arithmetic aggregation to a geometric mean. MASPO (Fu et al., 2026) combines Gaussian soft gating, a probability-mass-adaptive limiter, and an asymmetric risk controller. [NAME C19] shares the goal of retaining useful gradients with these methods. Its specific design combines a locally faithful log-ratio map with detached directional attenuation and a closed-form bound on their composite score multiplier.

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

Directional asymmetry. A complementary line distinguishes advantage polarities. SAPO (Gao et al., 2025) selects its sigmoid-gate temperature by advantage sign. [NAME C19] instead separates a log-ratio modulator with a closed-form multiplier bound from detached attenuation conditioned on ratio direction. ASPO (Wang et al., 2026) modifies importance weighting asymmetrically across positive- and negative-advantage samples. Advantage-level approaches (Tang et al., 2025; Nan et al., 2025) reshape the learning signal itself. Ratio direction and advantage polarity are distinct: a token with negative advantage may still have r > 1 and require a corrective probability decrease.

Trust-region methods. TRPO's KL constraint (Schulman et al., 2015) and PPO's clipped surrogate (Schulman et al., 2017) are established approaches to controlling local policy changes. DPPO (Qi et al., 2026) uses distributional divergence to assess proximity, while LPO (Qu et al., 2026) formulates group-based RLVR as target projection on a response simplex. [NAME C19] acts directly on sampled-token gradient multipliers, providing a complementary form of local update control. We compare against CISPO and MASPO in the same experimental framework.

### 3 METHODOLOGY

We first derive the GRPO gradient to identify the signal-retention problem, then introduce LFM and DHP, and finally connect their local update properties to autoregressive prefixes and the moment bound.

### 3.1 PRELIMINARIES OF GRPO

Let $$\pi_\theta$$ denote an autoregressive language model parameterized by $$\theta$$. Given a query $$p$$ from the query set $$\mathcal{D}$$, GRPO (Shao et al., 2024) samples a group of $$K$$ responses $$\{q^1, \ldots, q^K\}$$ from the reference policy $$\pi_{\theta_{\mathrm{old}}}$$. The likelihood of each response $$q^i$$ is factorized as $$\pi_{\theta_{\mathrm{old}}}(q^i \mid p) = \prod_{t=1}^{T_i} \pi_{\theta_{\mathrm{old}}}(q_t^i \mid p, q_{<t}^i)$$, where $$T_i$$ denotes the sequence length. Each response $$q^i$$ is then evaluated by a reward model or a verifiable rule to obtain a scalar reward $$R^i$$.

Following (Shao et al., 2024), the GRPO training objective is defined at the token level as:

$$\mathcal{L}_{\mathrm{GRPO}}(\theta) = -\mathbb{E}_{\substack{p \sim \mathcal{D}, \\ \{q^i\}_{i=1}^K \sim \pi_{\theta_{\mathrm{old}}}(\cdot \mid p)}} \left[ \frac{1}{K} \sum_{i=1}^K \frac{1}{T_i} \sum_{t=1}^{T_i} \min\left(r_t^i(\theta) \hat{A}_t^i, \operatorname{clip}(r_t^i(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t^i\right) \right], \tag{1}$$

where

$$r_t^i(\theta) = \frac{\pi_\theta(q_t^i \mid p, q_{<t}^i)}{\pi_{\theta_{\mathrm{old}}}(q_t^i \mid p, q_{<t}^i)}, \quad \hat{A}_t^i = \hat{A}^i = \frac{R^{(i)} - mean(\{R^1, \ldots, R^K\})}{std(\{R^1, \ldots, R^K\})}, \quad \epsilon > 0. \tag{2}$$

Here $$\pi_{\theta_{\mathrm{old}}}$$ is the fixed behavior policy, not an optional KL-reference model. The group-standardized advantage $$\hat{A}^i$$ is shared across tokens of response $$i$$, not across different responses. We isolate the policy-surrogate term and omit any separate KL regularizer.

From the clipped objective to its gradient. Let $$z_t = \log r_t$$ and $$s_t = \nabla_\theta \log \pi_\theta(q_t \mid p, q_{<t})$$. Since the behavior policy is fixed, $$\nabla_\theta r_t = r_t s_t$$. Away from the clip boundaries, differentiating the per-token maximization objective gives

$$\nabla_\theta J_{\mathrm{GRPO}, t} = \hat{A}_t \mathcal{M}_{\mathrm{GRPO}, t} s_t, \tag{3}$$

$$\mathcal{M}_{\mathrm{GRPO}, t} = r_t \mathbf{1}[(\hat{A}_t > 0 \land r_t < 1+\epsilon) \lor (\hat{A}_t < 0 \land r_t > 1-\epsilon)].$$

Thus the GRPO-dead set is $$D_t = \mathbf{1}[(\hat{A}_t > 0, r_t > 1+\epsilon) \lor (\hat{A}_t < 0, r_t < 1-\epsilon)]$$. "Dead" means zero direct surrogate contribution, not a frozen token probability under shared parameters. For example, $$r_t > 1$$ with $$\hat{A}_t < 0$$ remains active and encourages a corrective decrease. Ratio direction and advantage sign must therefore be distinguished.

### 3.2 THE [NAME C19] OBJECTIVE

We propose the [NAME C19] objective, which is designed to enhance training stability and provide fine-grained control over gradient updates. The model parameters $$\theta$$ are optimized by minimizing the

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

![img-6.jpeg](img-6.jpeg)

(a) LFM Operator $\psi(r_t^i(\theta))$

![img-7.jpeg](img-7.jpeg)

(b) LFM Derivative (Gradient Modulation)

Figure 2: Characteristics of the Log-Fidelity Modulator (LFM). (a) The LFM operator $\psi(r_t^i(\theta))$ with different values of $c$. The transformation exhibits reciprocal antisymmetry ($\psi(1/r_t^i(\theta)) = -\psi(r_t^i(\theta))$) around the on-policy anchor ($r_t^i(\theta) = 1$) and smoothly bounds the output within the interval $[-c, c]$. The marked points at $r_t^i(\theta) = \frac{1}{2}$ and $r_t^i(\theta) = 2$ (for $c = 1.0$) confirm $\psi(\frac{1}{2}) = -\psi(2)$. (b) The derivative of the LFM map, with $d\psi/dr = 1$ at the anchor. The parameter-gradient multiplier includes the additional factor $re^{\psi(r)}$ in Eq. (7).

following objective function:

$$\mathcal{L}_{\text{[NAME C19]}}(\theta) = -\mathbb{E}_{p \sim \mathcal{D}, \{q^i\}_{i=1}^K \sim \pi_{\theta_{\text{old}}}(\cdot|p)} \left[ \frac{1}{K} \sum_{i=1}^K \frac{1}{T_i} \sum_{t=1}^{T_i} \exp\left(\psi(r_t^i(\theta)) - \text{sg}\left(\zeta(r_t^i(\theta))\right)\right) \hat{A}_t^i \right], \tag{4}$$

where the transformation functions $\psi(\cdot)$ and $\zeta(\cdot)$ are defined as:

$$\psi(\cdot) = c \tanh \frac{\log(\cdot)}{c}, \quad \zeta(\cdot) = \left(\frac{s(\psi(\cdot))}{\lambda_+}\right)^{k_+} + \left(\frac{s(-\psi(\cdot))}{\lambda_-}\right)^{k_-}. \tag{5}$$

Here $\text{sg}(\cdot)$ is stop-gradient, $s(x) = \log(1 + e^x)$ is standard softplus (fixed smoothing $\beta = 1$), and $c, k_+, k_-, \lambda_+, \lambda_- > 0$ are the five configurable scalars. The implemented objective differentiates through LFM while detaching DHP. LFM acts on the ratio, not the reward. Its domain is $r > 0$, as softmax probabilities are positive for finite logits. We compute $z = \log \pi_\theta - \log \pi_{\theta_{\text{old}}}$ directly to avoid forming an underflowed ratio. We next elaborate on the two principal components of this objective, namely the Log-Fidelity Modulator and the Decoupled Hazard Penalty.

### 3.2.1 THE LOG-FIDELITY MODULATOR

The Log-Fidelity Modulator (LFM) is defined as $\psi(\cdot) = c \tanh(\log(\cdot)/c)$. It projects the importance ratio $r_t^i(\theta)$ into log-space and bounds its contribution to the objective within $[-c, c]$. In contrast to the hard clipping used in standard GRPO, which produces gradient discontinuities and vanishing regions at the trust-region boundary, the LFM applies a smooth saturation that preserves differentiability across the entire domain, as shown in Figure 2(a). The derivative of the LFM operator is

$$\frac{d\psi}{dr_t^i(\theta)} = \frac{1}{r_t^i(\theta)} \text{sech}^2 \left(\frac{\log r_t^i(\theta)}{c}\right), \tag{6}$$

The relevant quantity for the parameter gradient also includes $\nabla_\theta r = r s_t$. Writing $u(z) = c \tanh(z/c)$, its multiplier is

$$\nabla_\theta J_{\text{LFM},t} = \hat{A}_t \mathcal{M}_{\text{LFM}}(z_t) s_t, \quad \mathcal{M}_{\text{LFM}}(z) = e^{u(z)} u'(z) = e^{c \tanh(z/c)} \text{sech}^2(z/c) > 0. \tag{7}$$

The $1/r$ factor cancels in this chain rule. Tail control concerns $\mathcal{M}_{\text{LFM}}$, not $d\psi/dr$ in isolation. The map $u(z)$ is strictly increasing, with $u''(z) = -(2/c)\text{sech}^2(z/c) \tanh(z/c)$. Its curvature changes sign at zero, so it is neither globally convex nor globally concave.

Local fidelity. As $z \to 0$, $u(z) = z + O(z^3)$ and $\mathcal{M}_{\text{LFM}}(z) = e^z(1 + O(z^2))$, recovering the unclipped ratio multiplier locally. Bounded tail influence. The multiplier is positive at every finite $z$, tends to zero in both tails, and has the finite supremum in Theorem 1. Unlike clipping, it has no finite dead interval. The token-masking results in Section 4.3 show the utility of the retained clipped-tail contributions. Smoothness. LFM is $C^\infty$ on $r > 0$, removing clip-boundary discontinuities.

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

(a) Separate cumulative hazards

![img-8.jpeg](img-8.jpeg)

(b) Positive attenuation weight

![img-9.jpeg](img-9.jpeg)

Figure 3: DHP with the default asymmetric parameters. (a) The separate cumulative hazards and their sum, with $(k_+, \lambda_+, k_-, \lambda_-) = (1.5, 1.0, 2.0, 0.8)$. (b) The corresponding weight $w = e^{-\Omega} \in (0, 1]$. Both panels use $c = 1.5$ and fixed $\beta = 1$. DHP attenuates more strongly on the contraction side for these settings.

### 3.2.2 THE DECOUPLED HAZARD PENALTY

LFM bounds ratio-induced amplification. DHP adds directional control through a positive weight that preserves each direct contribution's direction and regulates expansion and contraction with separate hazard branches (Fig. 3):

$$\zeta(\cdot) = \left(\frac{s(\psi(\cdot))}{\lambda_+}\right)^{k_+} + \left(\frac{s(-\psi(\cdot))}{\lambda_-}\right)^{k_-}, \tag{8}$$

where the subscripts + and - refer to the signs of the modulated log ratio, not of $\hat{A}_t$. The softplus branches overlap near zero. In particular, $\zeta(1) > 0$, so DHP introduces baseline attenuation at the anchor rather than leaving it exactly unchanged.

**Why cumulative hazards?** In survival analysis, a survival function $S(x)$ and its cumulative hazard satisfy $H(x) = -\log S(x)$ (Cox & Oakes, 1984; Kalbfleisch & Prentice, 2002). The established Weibull family gives

$$H(x) = \left(\frac{x}{\lambda}\right)^k. \tag{9}$$

Thus $e^{-H(x)} \in (0, 1]$ is naturally an attenuation factor, $\lambda$ sets the order-one scale, and $k > 1$ makes $H(x)/x$ increase with $x$. We use this family as a deterministic shaping operator. Since $u(z)$ is bounded, the composed magnitudes are also bounded. Increasing $k$ strengthens attenuation where $x/\lambda > 1$ and weakens it where $x/\lambda < 1$, controlling the contrast between central and tail magnitudes.

**How attenuation relates to prefix contraction.** Write $\Omega(z) = \zeta(e^z)$ and $w(z) = e^{-\Omega(z)}$. For an isolated token, one SGD ascent step from the same $\theta$, with the same advantage, score vector, and step size $\eta$, satisfies

$$\delta\theta_{\mathrm{LFM}} = \eta\hat{A}_t\mathcal{M}_{\mathrm{LFM}}(z_t)s_t, \quad \delta\theta_{\mathrm{[NAME C19]}} = w(z_t)\delta\theta_{\mathrm{LFM}}. \tag{10}$$

Consequently, for $\Delta z_X = z_t(\theta + \delta\theta_X) - z_t(\theta)$, local smoothness gives $\Delta z_{\mathrm{[NAME C19]}} = w(z_t)\Delta z_{\mathrm{LFM}} + O(\eta^2)$. When the direct update further contracts the token, DHP reduces that contraction to first order. For a fixed prefix,

$$C_t = \log \frac{\pi_\theta(q_{\le t} \mid p)}{\pi_{\theta_{\mathrm{old}}}(q_{\le t} \mid p)} = \sum_{j \le t} z_j, \quad R_t = e^{C_t}. \tag{11}$$

Repeated negative terms therefore multiply their effects on prefix likelihood. This motivates stronger contraction-side damping: reducing direct contributions that reinforce contraction addresses a token-level source of cumulative prefix suppression.

With shared parameters, one mini-batch SGD step gives the evaluated token $j$

$$\Delta z_j = \eta \sum_t \alpha_t \hat{A}_t \mathcal{M}_{\mathrm{LFM}}(z_t) w(z_t) s_j^\top s_t + O(\eta^2), \tag{12}$$

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

Algorithm 1 [NAME C19] Training

Require: Policy  \( \pi_{\theta} \) , dataset D, LFM bound c, DHP parameters  \( (k_{+}, \lambda_{+}, k_{-}, \lambda_{-}) \) 

1: for each iteration do

2: Freeze  \( \theta_{old} \leftarrow \theta \) ; sample prompts and K responses per prompt using  \( \pi_{\theta_{old}} \) 

3: Compute group-normalized advantages  \( \hat{A}_{t}^{i} \) 

4: for each actor mini-batch update on this rollout do

5: for each response  \( q^{i} \) , each token t do

6:  \( z_{t}^{i} \leftarrow \log \pi_{\theta}(q_{t}^{i} \mid p, q_{<t}^{i}) - \log \pi_{\theta_{old}}(q_{t}^{i} \mid p, q_{<t}^{i}) \) 

7:  \( \psi_{t} \leftarrow c \tanh(z_{t}^{i}/c) \)  // LFM, computed directly in log space

8:  \( \zeta_{t} \leftarrow (s(\text{sg}(\psi_{t}))/\lambda_{+})^{k_{+}} + (s(-\text{sg}(\psi_{t}))/\lambda_{-})^{k_{-}} \)  // DHP

9: end for

10: Average  \( -\exp(\psi_{t} - \zeta_{t})\hat{A}_{t}^{i} \)  with the weights in Eq. (4); update  \( \theta \) 

11: end for

12: end for

where  \( \alpha_{t} \)  are normalized batch weights. The inner products  \( s_{j}^{\top}s_{t} \)  couple token updates, and DHP weights each contribution separately. This connects directional attenuation to realized probability changes through shared representations. Section 4.3 measures the resulting tail and prefix effects, including a uniform attenuation control. Appendix C.2 gives the derivation.

### 3.3 STABILITY ANALYSIS OF [NAME C19]

The stop-gradient in Eq. (4) is essential to the direction-preserving design. Full differentiation would instead yield \( e^{u - \Omega}(u' - \Omega') \), whose sign can reverse for some parameter settings. Detaching the hazard gives a positive multiplier with bounded ratio-induced amplification.

The token-level [NAME C19] objective is

\[
J _ {\mathrm{[NAME C19]}} (r _ {t} ^ {i} (\theta)) = \exp \big (\psi (r _ {t} ^ {i} (\theta)) - \mathrm{sg} \big (\zeta (r _ {t} ^ {i} (\theta)) \big) \big) \hat {A} _ {t} ^ {i}, \tag {13}
\]

where \(\mathrm{sg}(\cdot)\) denotes the stop-gradient operator. Applying the chain rule (Appendix B.3) yields

\[
\nabla_ {\theta} J _ {\mathrm{[NAME C19]}} (r _ {t} ^ {i} (\theta)) = \underbrace {\exp \big (\psi (r _ {t} ^ {i} (\theta)) - \zeta (r _ {t} ^ {i} (\theta)) \big) \operatorname{sech} ^ {2} \Big (\frac {\log r _ {t} ^ {i} (\theta)}{c} \Big)} _ {\mathcal {M} (r _ {t} ^ {i} (\theta))} \nabla_ {\theta} \log \pi_ {\theta} (q _ {t} ^ {i} \mid p, q _ {<   t} ^ {i})   \hat {A} _ {t} ^ {i}, \tag {14}
\]

where \(\mathcal{M}(r)\) is the gradient multiplier that smoothly rescales the per-token gradient. For compactness, \(\zeta (\cdot)\) denotes \(\mathrm{sg}(\zeta (\cdot))\) in the equation above.

The certificate propagates a pointwise multiplier bound to a normalized mini-batch gradient under an explicit local moment assumption. It requires neither token independence nor a factorization of advantage and score moments.

Theorem 1 ([NAME C19] multiplier-to-moment stability certificate). Consider the normalized mini-batch semi-gradient \( g(\theta) = K^{-1}\sum_{i=1}^{K}T_i^{-1}\sum_{t=1}^{T_i}\mathcal{M}(r_t^i (\theta))\nabla_\theta \log \pi_\theta (q_t^i\mid p,q_{< t}^i)\hat{A}_t^i \). At the current parameter value, write \( s_t^i = \nabla_\theta \log \pi_\theta (q_t^i\mid p,q_{< t}^i) \) and assume \( \mathbb{E}_{\mu}[K^{-1}\sum_iT_i^{-1}\sum_t(\hat{A}_t^i)^2\| s_t^i\|^2 ]\leq C \). Define the exact LFM multiplier certificate \( M_{\psi}(c) = \frac{2}{1 + \sqrt{1 + c^2}}\exp \left(\frac{c^2}{1 + \sqrt{1 + c^2}}\right) \). Then, for all \( r > 0 \) and \( \tau >0 \),

\[
0 \leq \mathcal {M} (r) \leq M _ {\psi} (c),
\]

\[
\mathbb {E} _ {\mu} \left[ \| g (\theta) \| ^ {2} \right] \leq C M _ {\psi} (c) ^ {2}, \quad \operatorname * {P r} _ {\mu} (\| g (\theta) \| \geq \tau) \leq \frac {C M _ {\psi} (c) ^ {2}}{\tau^ {2}}. \tag {15}
\]

Proof sketch. Since \(0 < w \leq 1\), \(\mathcal{M} \leq e^u u' \leq M_\psi(c)\). Convexity gives \(\|g\|^2 \leq K^{-1} \sum_i T_i^{-1} \sum_t \mathcal{M}_t^2 (\hat{A}_t^i)^2 \|s_t^i\|^2\). Taking expectations and applying Markov's inequality proves the result. The multiplier bound is global in ratio, and the gradient moment bound applies at the current parameter value under the stated condition on \(C\). DHP shapes directional influence while preserving the \(c\)-only multiplier bound. Full proofs appear in Appendix B.

## A-page-0007

target PDF page 7

Table 1: Main results on the Qwen3-4B-Base foundation model without instruction tuning. We report Avg@32 (%) for the best checkpoint. Avg. denotes the macro-average across benchmarks.

[tbl-0.html](tbl-0.html)

## 4 EXPERIMENTS

We evaluate Qwen3-4B-Base and Qwen3-30B-A3B-Base, with ablations and mechanism diagnostics on Qwen3-4B. Section 4.4 evaluates a smaller distilled reasoning model. Table 5(A–C) reports general-purpose, math-specialized, and vision-language instruction-tuned backbones.

### 4.1 EXPERIMENTAL SETUP

Models and datasets. The main results are reported on two foundation models of different scales and architectures, namely the dense Qwen3-4B-Base (Yang et al., 2025a) and the Mixture-of-Experts Qwen3-30B-A3B-Base (Yang et al., 2025a), both without prior instruction tuning. The policy is optimized on DAPO-Math-17k-Processed (Yu et al., 2025) with verifiable outcome-based rewards, and zero-shot generalization is evaluated on AIME 2024/2025 (Mathematical Association of America, 2025a), AMC 2023 (Mathematical Association of America, 2025b), HMMT25 (HMMT Organization, 2025), and MATH-500 (Hendrycks et al., 2021). The ablation studies in Section 4.3 are conducted on Qwen3-4B-Base under the same training and evaluation protocol. Additional instruction-tuned and vision-language results appear in Appendix D.

Baselines and metrics. We compare against GRPO, GSPO, DAPO, SAPO, CISPO, and MASPO. Avg@32 is the mean correctness of 32 sampled responses per prompt, averaged across prompts. It estimates single-sample pass@1, not the probability of at least one success in 32 attempts. Repeated-sample averaging is also used in DeepSeek-R1 and DAPO (Guo et al., 2025; Yu et al., 2025). Under independent samples with correctness probability p, the conditional sampling variance is  \( p(1-p)/32 \) . Appendix A gives the formula. “Avg.” in tables is the unweighted mean across the displayed tasks.

Configuration and cost. We use  \( (k_{+}, \lambda_{+}, k_{-}, \lambda_{-}) = (1.5, 1.0, 2.0, 0.8) \) , with c = 1.5 for the evaluated dense models and c = 4.0 for Qwen3-MoE. On the H20 training platform, the additional work consists of  \( O(BT) \)  token-wise scalar operations for B responses of length T, with no extra rollout, model forward pass, or trainable module. Appendix A gives implementation details.

### 4.2 MAIN RESULTS

Tables 1 and 2 show the best macro-average for [NAME C19] at both scales. On Qwen3-4B, [NAME C19] reaches \(52.9\%\), exceeding CISPO by 4.4 points and MASPO by 5.3 points. It leads on all five tasks. Among baselines, DAPO is best on HMMT25 \((14.9\%)\), while MASPO is best on AIME25 \((34.5\%)\). [NAME C19]'s gains over these task-specific baselines are 4.5 and 6.9 points. On Qwen3-MoE, [NAME C19] reaches \(54.7\%\) versus CISPO's \(54.0\%\) and MASPO's \(49.7\%\). CISPO remains higher on HMMT25 \((37.8\%\) versus \(37.3\%)\), and [NAME C19] leads on the other four tasks.

### 4.3 ABLATION STUDIES

We study component utility, parameter sensitivity, and mechanism diagnostics on Qwen3-4B-Base. Component ablations establish which parts help performance, while the diagnostics test the specific signal-retention and directional-contraction explanations.

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
<table><tr><td>Method</td><td>MATH500</td><td>HMMT25</td><td>AMC23</td><td>AIME25</td><td>AIME24</td><td>Avg.</td></tr><tr><td>Baseline</td><td>57.2 (+0.0)</td><td>3.8 (+0.0)</td><td>41.3 (+0.0)</td><td>5.7 (+0.0)</td><td>8.8 (+0.0)</td><td>23.4 (+0.0)</td></tr><tr><td>GRPO</td><td>64.8 (+7.6)</td><td>11.1 (+7.3)</td><td>81.3 (+40.0)</td><td>30.8 (+25.1)</td><td>40.4 (+31.6)</td><td>45.7 (+22.3)</td></tr><tr><td>GSPO</td><td>66.2 (+9.0)</td><td>12.4 (+8.6)</td><td>83.5 (+42.2)</td><td>34.0 (+28.3)</td><td>39.7 (+30.9)</td><td>47.2 (+23.8)</td></tr><tr><td>DAPO</td><td>64.0 (+6.8)</td><td>14.9 (+11.1)</td><td>75.8 (+34.5)</td><td>29.2 (+23.5)</td><td>34.2 (+25.4)</td><td>43.6 (+20.2)</td></tr><tr><td>SAPO</td><td>66.4 (+9.2)</td><td>11.5 (+7.7)</td><td>81.4 (+40.1)</td><td>32.9 (+27.2)</td><td>39.6 (+30.8)</td><td>46.4 (+23.0)</td></tr><tr><td>CISPO</td><td>69.0 (+11.8)</td><td>11.0 (+7.2)</td><td>85.3 (+44.0)</td><td>33.5 (+27.8)</td><td>43.7 (+34.9)</td><td>48.5 (+25.1)</td></tr><tr><td>MASPO</td><td>67.5 (+10.3)</td><td>12.8 (+9.0)</td><td>82.6 (+41.3)</td><td>34.5 (+28.8)</td><td>40.8 (+32.0)</td><td>47.6 (+24.2)</td></tr><tr><td>[NAME C19] (Ours)</td><td>70.9 (+13.7)</td><td>19.4 (+15.6)</td><td>88.2 (+46.9)</td><td>41.4 (+35.7)</td><td>44.7 (+35.9)</td><td>52.9 (+29.5)</td></tr></table>

## A-page-0008

target PDF page 8

Table 2: Main results on the Qwen3-30B-A3B-Base foundation model without instruction tuning. We report Avg@32 (%) for the best checkpoint. Avg. denotes the macro-average across benchmarks.

[tbl-1.html](tbl-1.html)

Table 3: Ablation analysis on Qwen3-4B-Base. Top: sensitivity to c, k, and λ, and component/directional DHP variants (macro-average Avg@32, %). Bottom: gradient-norm and overall-reward trajectories during training.

[tbl-2.html](tbl-2.html)

![img-10.jpeg](img-10.jpeg)

(a) Gradnorm

![img-11.jpeg](img-11.jpeg)

(b) Overall reward

Hyperparameter sensitivity. Table 3 reports Qwen3-4B-Base ablations using macro-average Avg@32 across the five math benchmarks. The table sweeps the LFM bound c, Weibull shape k, and Weibull scale  \( \lambda \) , and further isolates the two components and the directionality of the DHP. These parameters correspond to the two design axes of [NAME C19]: c controls the fidelity-preserving ratio range, while k and  \( \lambda \)  control the sharpness and onset of tail damping. For the k and  \( \lambda \)  sweeps, other hyperparameters are fixed to the reference setting; for the c sweep, the hazard term is disabled to isolate the smooth bound.

LFM alone reaches 52.0% and DHP alone 50.8%, compared with 52.9% for their combination. The ratio-contraction-stronger variant also exceeds the symmetric (52.4%) and expansion-stronger (52.1%) alternatives. These differences support the complementary roles of the two components and stronger contraction-side control. The hazard-free c sweep spans 50.9–52.0%, and the reported k and  \( \lambda \)  sweeps span 52.0–52.9% and 51.9–52.9%. Performance remains within these ranges across the tested one-factor settings.

Training stability. The lower panel of Table 3 shows gradient norms and rewards. [NAME C19]'s best-to-latest Avg@32 changes from 52.9% to 52.1%, a 0.8-point drop, compared with 6.9–12.2 points for the evaluated baselines (Table 6). The following diagnostics relate this improved checkpoint retention to the token contributions and prefix dynamics targeted by LFM and DHP.

Mechanism evidence. The GRPO-dead set comprises 18.6% of nonzero-advantage tokens and 27.4% of absolute-advantage mass. LFM gives this set 34.7% of its effective coefficient mass, defined

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

[OCR table id=tbl-1.html; page=8]
<table><tr><td>Method</td><td>MATH500</td><td>HMMT25</td><td>AMC23</td><td>AIME25</td><td>AIME24</td><td>Avg.</td></tr><tr><td>Baseline</td><td>76.5 (+0.0)</td><td>1.6 (+0.0)</td><td>43.6 (+0.0)</td><td>9.0 (+0.0)</td><td>14.2 (+0.0)</td><td>29.0 (+0.0)</td></tr><tr><td>GRPO</td><td>82.8 (+6.3)</td><td>35.3 (+33.7)</td><td>78.4 (+34.8)</td><td>28.9 (+19.9)</td><td>31.6 (+17.4)</td><td>51.4 (+22.4)</td></tr><tr><td>GSPO</td><td>84.1 (+7.6)</td><td>36.9 (+35.3)</td><td>80.6 (+37.0)</td><td>29.8 (+20.8)</td><td>32.4 (+18.2)</td><td>52.8 (+23.8)</td></tr><tr><td>DAPO</td><td>84.5 (+8.0)</td><td>37.2 (+35.6)</td><td>81.0 (+37.4)</td><td>30.2 (+21.2)</td><td>32.8 (+18.6)</td><td>53.1 (+24.2)</td></tr><tr><td>SAPO</td><td>83.2 (+6.7)</td><td>34.6 (+33.0)</td><td>76.8 (+33.2)</td><td>30.7 (+21.7)</td><td>29.4 (+15.2)</td><td>50.9 (+22.0)</td></tr><tr><td>CISPO</td><td>85.4 (+8.9)</td><td>37.8 (+36.2)</td><td>82.3 (+38.7)</td><td>31.6 (+22.6)</td><td>33.1 (+18.9)</td><td>54.0 (+25.1)</td></tr><tr><td>MASPO</td><td>81.7 (+5.2)</td><td>33.8 (+32.2)</td><td>75.9 (+32.3)</td><td>28.1 (+19.1)</td><td>28.8 (+14.6)</td><td>49.7 (+20.7)</td></tr><tr><td>[NAME C19] (Ours)</td><td>86.6 (+10.1)</td><td>37.3 (+35.7)</td><td>83.6 (+40.0)</td><td>32.4 (+23.4)</td><td>33.8 (+19.6)</td><td>54.7 (+25.8)</td></tr></table>

[OCR table id=tbl-2.html; page=8]
<table><tr><td colspan="2">(a) Bound c (hazard-free)</td><td colspan="2">(b) Shape k (c=1.5, λ=0.8)</td><td colspan="2">(c) Scale λ (c=1.5, k=3.0)</td><td colspan="2">(d) Components / DHP direction</td></tr><tr><td>c</td><td>Avg@32</td><td>k</td><td>Avg@32</td><td>λ</td><td>Avg@32</td><td>Variant</td><td>Avg@32</td></tr><tr><td>0.5</td><td>50.9</td><td>1.0</td><td>52.0</td><td>0.5</td><td>52.5</td><td>DHP only</td><td>50.8</td></tr><tr><td>1.0</td><td>51.3</td><td>1.5</td><td>52.3</td><td>0.8</td><td>52.9</td><td>LFM only</td><td>52.0</td></tr><tr><td>1.5</td><td>52.0</td><td>2.5</td><td>52.6</td><td>1.0</td><td>52.7</td><td>Pos.-stronger DHP</td><td>52.1</td></tr><tr><td>2.0</td><td>51.7</td><td>3.0</td><td>52.9</td><td>2.0</td><td>51.9</td><td>Symmetric DHP</td><td>52.4</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Neg.-stronger DHP</td><td>52.9</td></tr></table>

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

as $$\sum_{t}D_{t}|\hat{A}_{t}|\mathcal{M}_{\mathrm{LFM}}(z_{t})/\sum_{t}|\hat{A}_{t}|\mathcal{M}_{\mathrm{LFM}}(z_{t})$$. This measures the retained scalar weight entering the policy gradient. The advantage-aligned log-probability change, $$\mathrm{sign}(\hat{A}_{t})(\log p_{\mathrm{after}}-\log p_{\mathrm{before}})$$, is 0.019 for LFM versus 0.002 for GRPO. Removing these specific contributions reduces LFM's best/latest Avg@32 from 52.0/48.5 to 49.2/42.6, while a shuffled mask matched for count, position, advantage sign, $$|A|$$ bin, and removed coefficient mass gives 51.1/46.8. The larger loss from the exact mask shows that the recovered clipped-tail signals contribute to both task performance and checkpoint retention.

DHP reduces the fraction below the negative GRPO clip boundary from 8.9% with LFM to 3.9% with [NAME C19]. A scalar attenuation control matched to [NAME C19]'s update norm remains at 8.0%. Negative-tail 1%-CVaR, the mean contraction severity $$(-\log r)_{+}$$ in the worst 1% of tokens, falls from 1.18 to 0.63, versus 1.09 for the scalar control. [NAME C19] also retains more expansion-side variation than symmetric DHP: upper-boundary exceedance is 7.1% versus 5.8%, with highest-1% mean log ratio 0.91 versus 0.77. On correct responses, the fraction whose prefix likelihood ratio ever falls below 0.1 decreases from 13.2% with LFM and 11.5% with the control to 4.9% with [NAME C19]. Together, the directional-tail contrast and reduced collapse of correct-response prefixes support selective contraction control beyond uniform shrinkage. Appendix C gives the definitions and local derivation.

Tail frequency measures how often contraction exceeds the clip boundary, while CVaR measures its severity in the worst tail. For example, CVaR 1.18 corresponds to a geometric mean token ratio of $$e^{-1.18} \approx 0.307$$ within that tail.

The first-crossing depth is $$\tau_{0.1}(i) = \inf\{t : C_{i,t} < \log 0.1\}$$, using the prefix log ratio in Eq. (11). Among correct responses that cross this threshold, the median depth is 846 tokens with LFM and 1,487 with [NAME C19]. Noncrossing responses have $$\tau_{0.1} = \infty$$ and are excluded from this conditional median. Reporting it alongside the collapse rate captures both the incidence of prefix suppression and its location within affected responses.

### 4.4 TRANSFER TO A DISTILLED REASONING MODEL

Table 4: DeepSeek-R1-Distill-Qwen-1.5B results. Avg@32 (%) and arithmetic mean across the four displayed tasks.

[tbl-3.html](tbl-3.html)

Table 4 evaluates DeepSeek-R1-Distill-Qwen-1.5B under the same Avg@32 protocol. [NAME C19] reaches 58.4%, exceeding MASPO by 1.0 point in the four-task average. It leads on AIME24, AIME25, and MATH500, while SAPO remains best on AMC23. On Qwen2.5-Instruct, Math, and VL backbones, [NAME C19] scores 43.7/47.8/53.0, versus DAPO's 40.2/43.6/52.3 (Table 5). These evaluations cover Qwen-derived dense, MoE, instruction-tuned, distilled, and vision-language backbones, supporting transfer across model scales, training lineages, and modalities.

## 5 CONCLUSION

[NAME C19] separates retained learning signals from directional attenuation through LFM and DHP. Its positive multiplier preserves direct update directions and bounds ratio-induced amplification, yielding a local gradient moment certificate under the stated product-moment condition. Token interventions show that recovered clipped-tail contributions support learning, while directional-tail and prefix diagnostics connect asymmetric damping to reduced contraction of correct-response prefixes. This combination achieves the best benchmark average at both evaluated Qwen3 scales and improves checkpoint retention, with further gains on instruction-tuned, distilled, and vision-language backbones.

[OCR table id=tbl-3.html; page=9]
<table><tr><td>Method</td><td>AIME24</td><td>AIME25</td><td>AMC23</td><td>MATH500</td><td>4-task Avg.</td></tr><tr><td>GRPO</td><td>33.2</td><td>27.7</td><td>79.5</td><td>77.6</td><td>54.5</td></tr><tr><td>SAPO</td><td>39.3</td><td>28.0</td><td><b>82.7</b></td><td>79.1</td><td>57.3</td></tr><tr><td>MASPO</td><td>41.0</td><td>28.4</td><td>82.2</td><td>78.0</td><td>57.4</td></tr><tr><td>[NAME C19]</td><td><b>41.6</b></td><td><b>29.7</b></td><td>82.5</td><td><b>79.6</b></td><td><b>58.4</b></td></tr></table>

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

Generative AI tools assisted with refining the mechanistic explanations and mathematical presentation, checking derivations, designing diagnostic analyses, interpreting results, identifying relevant literature, revising manuscript text, preparing analytical figures, and LaTeX formatting. The empirical results reported here were confirmed by the authors from their experiments. The authors are responsible for the final text, mathematical claims, citations, and experimental evidence.

## REPRODUCIBILITY STATEMENT

Section 3 specifies the objective, gradient multiplier, and update algorithm. Appendix A records the operator settings and training and evaluation protocol, including the definition of Avg@32. Appendix B states the theoretical assumptions and proofs. Appendix C defines the token, directional-tail, and prefix diagnostics and explains the scope of the local update analysis. Additional backbone and checkpoint results appear in Appendices D and E.

## REFERENCES

Aili Chen, Aonian Li, Bangwei Gong, Binyang Jiang, Bo Fei, Bo Yang, Boji Shan, Changqing Yu, Chao Wang, Cheng Zhu, et al. Minimax-m1: Scaling test-time compute efficiently with lightning attention. arXiv preprint arXiv:2506.13585, 2025.

David R. Cox and David Oakes. Analysis of Survival Data. Chapman and Hall, 1984. doi:10.1201/9781315137438.

Xiaoliang Fu, Jiaye Lin, Yangyi Fang, et al. Maspo: Unifying gradient utilization, probability mass, and signal reliability for robust and sample-efficient llm reasoning. arXiv preprint arXiv:2602.17550, 2026.

Chang Gao, Chujie Zheng, Xiong-Hui Chen, et al. Soft adaptive policy optimization. arXiv preprint arXiv:2511.20347, 2025.

Daya Guo, Dejian Yang, Haowei Zhang, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948, 2025.

Dan Hendrycks, Collin Burns, Saurav Kadavath, et al. Measuring mathematical problem solving with the MATH dataset. In Advances in Neural Information Processing Systems, 2021.

HMMT Organization. Harvard-MIT mathematics tournament (HMMT). [URL REDACTED] 2025. Annual mathematics tournament organized by Harvard and MIT students.

John D. Kalbfleisch and Ross L. Prentice. The Statistical Analysis of Failure Time Data. Wiley, 2 edition, 2002. doi: 10.1002/9781118032985.

Pan Lu, Ran Gong, Shibiao Jiang, et al. Inter-GPS: Interpretable geometry problem solving with formal language and symbolic reasoning. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics, 2021.

Pan Lu, Hritik Bansal, Tony Xia, et al. MathVista: Evaluating mathematical reasoning of foundation models in visual contexts. In International Conference on Learning Representations, 2024.

Mathematical Association of America. American invitational mathematics examination (AIME). [URL REDACTED] 2025a. Annual invitational competition for top-scoring AMC participants.

Mathematical Association of America. American mathematics competitions (AMC). [URL REDACTED] 2025b. Annual competition series for students in grades 8–12.

Gongrui Nan, Siye Chen, Jing Huang, et al. NGRPO: Negative-enhanced group relative policy optimization. arXiv preprint arXiv:2509.18851, 2025.

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

OpenAI. Learning to reason with llms, 2024. URL [URL REDACTED]

Long Ouyang, Jeffrey Wu, Xu Jiang, et al. Training language models to follow instructions with human feedback. Advances in neural information processing systems, 2022.

Penghui Qi, Xiangxin Zhou, Zichen Liu, Tianyu Pang, Chao Du, Min Lin, and Wee Sun Lee. Rethinking the trust region in LLM reinforcement learning. arXiv preprint arXiv:2602.04879, 2026. URL https://arxiv.org/abs/2602.04879.

Yun Qu, Qi Wang, Yixiu Mao, Heming Zou, Yuhang Jiang, Yingyue Li, Wutong Xu, Lizhou Cai, Weijie Liu, Clive Bai, Kai Yang, Yangkun Chen, Saiyong Yang, and Xiangyang Ji. Listwise policy optimization: Group-based RLVR as target-projection on the LLM response simplex. arXiv preprint arXiv:2605.06139, 2026. URL https://arxiv.org/abs/2605.06139.

John Schulman, Sergey Levine, Philipp Moritz, Michael Jordan, and Pieter Abbeel. Trust region policy optimization. In International Conference on Machine Learning, 2015.

John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347, 2017.

Zhihong Shao, Peiyi Wang, Qihao Zhu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300, 2024.

Haozhan Shen, Peng Liu, Jingcheng Li, et al. Vlm-r1: A stable and generalizable r1-style large vision-language model. arXiv preprint arXiv: 2504.07615, 2025.

Xinyu Tang, Yuliang Zhan, Zhixun Li, et al. Rethinking sample polarity in reinforcement learning with verifiable rewards. arXiv preprint arXiv:2512.21625, 2025.

Jiakang Wang, Runze Liu, Qingpeng Cai, Lei Lin, Wenping Hu, Xiu Li, Fuzheng Zhang, Guorui Zhou, Kun Gai, and Ling Pan. When importance sampling misallocates credit: Asymmetric ratios for outcome-supervised RL. arXiv preprint arXiv:2510.06062, 2026. URL https://arxiv.org/abs/2510.06062v2.

Ke Wang, Junting Pan, Weikang Shi, Zimu Lu, Mingjie Zhan, and Hongsheng Li. Measuring multimodal mathematical reasoning with MATH-Vision dataset. arXiv preprint arXiv:2402.14804, 2024.

An Yang, Anfeng Li, Baosong Yang, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388, 2025a.

Yi Yang, Xiaoxuan He, Hongkun Pan, et al. R1-onevision: Advancing generalized multimodal reasoning through cross-modal formalization. arXiv preprint arXiv: 2503.10615, 2025b.

Qiying Yu, Zheng Zhang, Ruofei Zhu, et al. Dapo: An open-source llm reinforcement learning system at scale. arXiv preprint arXiv:2503.14476, 2025.

Yufei Zhan, Yousong Zhu, Shurong Zheng, et al. Vision-r1: Evolving human-free alignment in large vision-language models via vision-guided reinforcement learning. arXiv preprint arXiv:2503.18013, 2025.

Renrui Zhang, Dongzhi Jiang, Yichi Zhang, et al. MathVerse: Does your multi-modal LLM truly see the diagrams in visual math problems? In European Conference on Computer Vision, 2024.

Yuzhong Zhao, Yue Liu, Junpeng Liu, Jingye Chen, Xun Wu, Yaru Hao, Tengchao Lv, Shaohan Huang, Lei Cui, Qixiang Ye, Fang Wan, and Furu Wei. Geometric-mean policy optimization. arXiv preprint arXiv:2507.20673, 2025. URL https://arxiv.org/abs/2507.20673.

Chujie Zheng, Shixuan Liu, Mingze Li, et al. Group sequence policy optimization. arXiv preprint arXiv:2507.18071, 2025.

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

# A IMPLEMENTATION DETAILS

This section reports the operator settings and training/evaluation setup used in the main paper and supplementary experiments.

[NAME C19] hyperparameters. The five scalars have distinct roles: c controls the log-ratio fidelity range, k± the directional shape, and λ± the attenuation scale. For the five original backbones, the DHP settings are fixed at (k+, λ+) = (1.5, 1.0) and (k-, λ-) = (2.0, 0.8). We use c = 1.5 on Qwen3-4B and the three Qwen2.5 instruction-tuned variants, and c = 4.0 on Qwen3-30B-A3B. The larger MoE value permits a wider log-ratio fidelity range. Softplus smoothing is fixed at β = 1 throughout.

Training data and protocol. The policy is optimized on DAPO-Math-17k-Processed (Yu et al., 2025) with verifiable outcome-based rewards, following the standard GRPO pipeline. We sample K = 16 responses per prompt during rollout for policy updates, and the maximum response length is 4,096 tokens for the Qwen3 foundation models (both the 4B dense and the 30B-A3B MoE) and 2,048 tokens for the Qwen2.5 variants used in the supplementary experiments. Reward normalization, advantage computation, and the underlying actor update follow standard GRPO practice.

Evaluation protocol. For math benchmarks (MATH-500 (Hendrycks et al., 2021), HMMT25 (HMMT Organization, 2025), AMC 2023 (Mathematical Association of America, 2025b), AIME 2024/2025 (Mathematical Association of America, 2025a)), we sample n = 32 responses per prompt and report Avg@32. For the vision-language benchmarks in Section D (MathVista (Lu et al., 2024), MathVision (Wang et al., 2024), MathVerse (Zhang et al., 2024)), we use the same Avg@32 protocol. All evaluations are zero-shot with respect to the reported benchmarks; only DAPO-Math-17k-Processed is used for policy optimization on text backbones, and only Geometry3K (Lu et al., 2021) is used for the Qwen2.5-VL-7B-Instruct results in Subtable (C) of Table 5.

Baselines. The main baseline comparisons use the same codebase, training data, and total update budget. GRPO (Shao et al., 2024) uses ε = 0.2, and the DAPO-style clip configuration (Yu et al., 2025) uses (εlow, εhigh) = (0.2, 0.28). SAPO (Gao et al., 2025) uses soft gating, GSPO (Zheng et al., 2025) sequence-level ratio control, and CISPO (Chen et al., 2025) detached clipped importance weights. MASPO (Fu et al., 2026) combines Gaussian gating, a mass-adaptive limiter, and asymmetric control. These comparisons evaluate the policy-update operators within a common training framework.

Meaning of Avg@32. For N evaluation prompts, let Xij ∈ {0, 1} denote correctness of completion j for prompt i. We report

$$\text{Avg@32} = \frac{100}{N} \sum_{i=1}^{N} \widehat{p}_i, \quad \widehat{p}_i = \frac{1}{32} \sum_{j=1}^{32} X_{ij}. \tag{16}$$

If the completions are sampled independently with success probability pi, then E[p̂i | i] = pi and Var(p̂i | i) = pi(1 - pi)/32. Thus Avg@32 estimates the single-sample pass@1 of the specified sampling distribution with lower Monte Carlo variance than one draw per prompt. By comparison, pass@32 measures the probability of at least one successful completion, with per-prompt target 1 - (1 - pi)32. Repeated-sample pass-rate estimation is used in DeepSeek-R1 and DAPO (Guo et al., 2025; Yu et al., 2025).

Computational cost. The training platform uses NVIDIA H20 GPUs. Relative to the existing actor loss, [NAME C19] adds token-wise tanh, softplus, powers, and exponentiation on already available log-probabilities. The work is O(BT) and can require O(BT) temporary scalar storage, with no extra model evaluation, rollout, or trainable state.

# B THEORETICAL ANALYSIS AND PROOFS

This appendix is organized to mirror the theoretical narrative in the main paper. We first introduce the generic log-form view of ratio operators, then define the hazard-shaping components used by

## A-page-0013

target PDF page 13

[NAME C19], next establish the gradient identities and boundedness certificates that support the stability claims, and finally explain why the semi-gradient implementation is adopted in place of the fully differentiable variant. For self-containedness, we restate the main multiplier-to-moment certificate (Theorem 2 below) before giving its proof.

Restatement of the main stability certificate. Let $\psi(\cdot) = c \tanh(\log(\cdot)/c)$ be the Log-Fidelity Modulator (LFM) and let $\zeta(\cdot)$ be the Decoupled Hazard Penalty (DHP) composed of Weibull cumulative hazards on one-sided softplus magnitudes, as used in the main paper. Under the semi-gradient implementation (a stop-gradient is applied to $\psi$ inside $\zeta$), the [NAME C19] gradient multiplier is

$$\mathcal{M}(r) = \exp\bigl(\psi(r) - \zeta(r)\bigr) \operatorname{sech}^2 \left( \frac{\log r}{c} \right). \tag{17}$$

Theorem 2 ([NAME C19] multiplier-to-moment stability certificate; restated from the main paper). Consider the normalized mini-batch semi-gradient $g(\theta) = K^{-1} \sum_{i=1}^{K} T_i^{-1} \sum_{t=1}^{T_i} \mathcal{M}(r_t^i(\theta)) s_t^i \hat{A}_t^i$, where $s_t^i = \nabla_\theta \log \pi_\theta(q_t^i \mid p, q_{<t}^i)$. At the current parameter value, assume the normalized product moment

$$\mathbb{E}_\mu \left[ \frac{1}{K} \sum_i \frac{1}{T_i} \sum_t (\hat{A}_t^i)^2 \| s_t^i \|^2 \right] \le C. \tag{18}$$

Define the exact LFM multiplier certificate

$$M_\psi(c) = \frac{2}{1 + \sqrt{1 + c^2}} \exp \left( \frac{c^2}{1 + \sqrt{1 + c^2}} \right).$$

Then, for all $r > 0$ and $\tau > 0$,

$$0 \le \mathcal{M}(r) \le M_\psi(c),$$

$$\mathbb{E}_\mu \big[ \| g(\theta) \|^2 \big] \le C M_\psi(c)^2, \quad \Pr_\mu(\| g(\theta) \| \ge \tau) \le \frac{C M_\psi(c)^2}{\tau^2}. \tag{19}$$

The proof is given in Section B.5 below, after the supporting lemmas.

### B.1 FORMAL EQUIVALENCE OF THE LOG-FORM SURROGATE

Proposition 3 (Any positive ratio operator admits a log-form). Let $\omega : (0, \infty) \to (0, \infty)$ be any positive ratio operator applied to the importance ratio $r = \exp(z)$. Define $\phi : \mathbb{R} \to \mathbb{R}$ by $\phi(z) \triangleq \log \omega(\exp(z))$. Then $\omega(r) = \exp(\phi(\log r))$, i.e., the per-token ratio operator can always be written as $\exp(\phi(z))$ in log-ratio space.

Proof. Substitute $r = \exp(z)$ to obtain $\exp(\phi(z)) = \exp(\log \omega(\exp(z))) = \omega(\exp(z)) = \omega(r)$. $\square$

### B.2 DEFINITIONS AND PROPERTIES OF WEIBULL HAZARD SHAPING

For an absolutely continuous survival law, $S(x) = \Pr(T > x)$, $H(x) = -\log S(x)$, and $h(x) = H'(x)$ are respectively the survival function, cumulative hazard, and instantaneous hazard (Cox & Oakes, 1984; Kalbfleisch & Prentice, 2002). Weibull survival has $S(x) = \exp[-(x/\lambda)^k]$. [NAME C19] uses this established functional family for deterministic attenuation of directional ratio magnitudes.

Let $u(z) \triangleq c \tanh(z/c)$ and $\beta > 0$ (fixed to 1 in the implementation). We define ratio-expansion/contraction magnitudes using softplus:

$$x_+(u) = \frac{\operatorname{softplus}(\beta u)}{\beta} = \frac{\log(1 + e^{\beta u})}{\beta}, \tag{20}$$

$$x_-(u) = \frac{\operatorname{softplus}(-\beta u)}{\beta} = \frac{\log(1 + e^{-\beta u})}{\beta}. \tag{21}$$

These satisfy $x_+(u), x_-(u) > 0$ and $x_+(u) + x_-(u) = |u| + 2 \log(1 + e^{-\beta|u|})/\beta$, approaching $|u|$ at large magnitudes. At the anchor, both branches equal $\log 2/\beta$, giving finite baseline attenuation. Because $|u| \le c$, both magnitudes lie in the compact interval $[\log(1 + e^{-\beta c})/\beta, \log(1 + e^{\beta c})/\beta]$.

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

For \(x \geq 0\), define the cumulative hazards

\[
H _ {+} (x) \triangleq \left(\frac {x}{\lambda_ {+}}\right) ^ {k _ {+}}, \quad H _ {-} (x) \triangleq \left(\frac {x}{\lambda_ {-}}\right) ^ {k _ {-}}, \tag {22}
\]

with shape parameters \( k_{\pm} > 0 \) and scales \( \lambda_{\pm} > 0 \). The DHP composes \( u \mapsto x_{\pm}(u) \mapsto H_{\pm}(x_{\pm}) \), yielding a nonnegative hazard penalty \( \Omega(z) = H_{+}(x_{+}(u(z))) + H_{-}(x_{-}(u(z))) \) and survival weight \( w(z) = \exp(-\Omega(z)) \in (0,1] \).

### B.3 DIFFERENTIATION IDENTITIES AND GRADIENT BOUNDS

Lemma 4 (Gradient form and gradient multiplier). For \(\ell_t(\theta) \triangleq -A_t \exp(\phi(z_t(\theta)))\), the gradient satisfies

\[
\nabla_ {\theta} \ell_ {t} (\theta) = - A _ {t} \exp (\phi (z _ {t} (\theta))) \phi^ {\prime} (z _ {t} (\theta)) \nabla_ {\theta} z _ {t} (\theta). \tag {23}
\]

Equivalently, defining the gradient multiplier \(\mathcal{M}_{\phi}(z) \triangleq \exp(\phi(z)) \phi'(z)\), we have \(\nabla_{\theta} \ell_t(\theta) = -A_t \mathcal{M}_{\phi}(z_t(\theta)) \nabla_{\theta} z_t(\theta)\).

Proof. Since \(\ell_t(\theta) = -A_t g(z_t(\theta))\) with \(g(z) = \exp (\phi (z))\), the chain rule gives

\[
\nabla_ {\theta} \ell_ {t} (\theta) = - A _ {t} g ^ {\prime} (z _ {t} (\theta)) \nabla_ {\theta} z _ {t} (\theta).
\]

Moreover, \( g'(z) = \exp(\phi(z)) \phi'(z) \) by differentiating \( g(z) = \exp(\phi(z)) \). Substituting \( g'(z_t(\theta)) \) yields the claimed expression.

Lemma 5 (Gradient of the log-ratio). With \( z_{t}(\theta) = \log \pi_{\theta}(y_t \mid x, y_{<t}) - \log \pi_{\theta_{\mathrm{old}}}(y_t \mid x, y_{<t}) \), we have

\[
\nabla_ {\theta} z _ {t} (\theta) = \nabla_ {\theta} \log \pi_ {\theta} (y _ {t} \mid x, y _ {<   t}). \tag {24}
\]

Proof. The behavior policy \(\pi_{\theta_{\mathrm{old}}}\) is fixed during the update, so its log-probability term is constant w.r.t. \(\theta\).

Proposition 6 (Per-token gradient bound via \(M\)). Assume \(\| \nabla_{\theta} \log \pi_{\theta}(y_t \mid x, y_{<t}) \| \leq G\) for all tokens in the update. Then the per-token gradient magnitude satisfies

\[
\left\| \nabla_ {\theta} \ell_ {t} (\theta) \right\| \leq \left| A _ {t} \right| M G, \tag {25}
\]

Proof. By Lemma 4, \(\nabla_{\theta}\ell_t(\theta) = -A_t\exp (\phi (z_t(\theta)))\phi '(z_t(\theta))\nabla_\theta z_t(\theta) = -A_t\mathcal{M}_\phi (z_t(\theta))\nabla_\theta z_t(\theta)\). Lemma 5 gives \(\nabla_{\theta}z_{t}(\theta) = \nabla_{\theta}\log \pi_{\theta}(y_{t}\mid x,y_{< t})\). Taking norms and using \(\| \nabla_{\theta}\log \pi_{\theta}(\cdot)\| \leq G\) yields

\[
\left\| \nabla_ {\theta} \ell_ {t} (\theta) \right\| \leq \left| A _ {t} \right| \left| \mathcal {M} _ {\phi} \left(z _ {t} (\theta)\right) \right| G \leq \left| A _ {t} \right| \left(\sup _ {z} \left| \mathcal {M} _ {\phi} (z) \right|\right) G = \left| A _ {t} \right| M G,
\]

where we define \(M \triangleq \sup_{z} |\mathcal{M}_{\phi}(z)|\).

### B.4 LOG-FIDELITY MODULATOR DERIVATIVES AND PROOF OF THEOREM 8

Lemma 7 (Derivatives and bounds for \( u(z) = c \tanh(z/c) \)). For \( u(z) = c \tanh(z/c) \) (equivalently, \( u(z) = \psi(e^z) \) with the LFM \( \psi \)),

\[
u ^ {\prime} (z) = \operatorname{sech} ^ {2} (z / c) \in (0, 1 ], \quad | u ^ {\prime \prime} (z) | \leq \frac {2}{c}. \tag {26}
\]

Proof. Differentiate tanh and use \( |\tanh(\cdot)| \leq 1 \) and \( \operatorname{sech}^2(\cdot) \leq 1 \).

Theorem 8 (Closed-form \( M_{\psi}(c) \) for the Log-Fidelity Modulator). Let \( u(z) = c \tanh(z/c) \) with parameter \( c > 0 \), and define \( M_{\psi}(c) \triangleq \sup_{z \in \mathbb{R}} \exp(u(z)) u'(z) \). Then

\[
M _ {\psi} (c) = \frac {2}{1 + \sqrt {1 + c ^ {2}}} \exp \left(\frac {c ^ {2}}{1 + \sqrt {1 + c ^ {2}}}\right). \tag {27}
\]

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

Proof of Theorem 8. Let $t = z/c$. Then $u(z) = c \tanh t$ and $u'(z) = \operatorname{sech}^2 t$. We maximize $f(t) \triangleq \exp(c \tanh t) \operatorname{sech}^2 t$ over $t \in \mathbb{R}$. Differentiate $\log f(t) = c \tanh t + \log(\operatorname{sech}^2 t)$ to obtain $\frac{d}{dt} \log f(t) = c \operatorname{sech}^2 t - 2 \tanh t$. Setting it to zero gives $c(1 - y^2) = 2y$ with $y = \tanh t \in (-1, 1)$. Solving $cy^2 + 2y - c = 0$ yields the feasible root $y^\star = \frac{\sqrt{1+c^2}-1}{c} = \frac{c}{1+\sqrt{1+c^2}}$. At $y^\star$, $\operatorname{sech}^2 t = 1 - (y^\star)^2 = \frac{2}{1+\sqrt{1+c^2}}$ and $c \tanh t = \frac{c^2}{1+\sqrt{1+c^2}}$. Substituting into $f(t)$ gives Eq. (27).

### B.5 CERTIFIED PER-TOKEN GRADIENT CONTROL AND SMOOTHNESS GUARANTEES

This subsection provides the full statements and proof details for the certified moment-control chain of Theorem 2. We keep the assumptions explicit and local to one policy update, which is the regime in which PPO/GRPO-style policy-gradient estimators are applied.

Assumptions. Fix the current parameter value and behavior law $\mu$. The main theorem assumes Eq. (18), retaining any dependence between advantages, score norms, and response lengths. For the auxiliary per-token bounds below, stronger sufficient conditions are

$$\mathbb{E}_{\mu}[A_t^2] \leq \sigma_A^2, \tag{28}$$

$$\|\nabla_{\theta} \log \pi_{\theta}(y_t \mid x, y_{<t})\| \leq G \quad \mu\text{-a.s.} \tag{29}$$

Eq. (29) is an almost-sure per-token score assumption. For a fixed token, these stronger assumptions imply $\mathbb{E}[A_t^2 \|s_t\|^2] \leq \sigma_A^2 G^2$ by pointwise domination. For the random-length mini-batch, Eq. (18) is stated directly on the normalized sum at the current parameter value.

For curvature discussions one may additionally assume, along the line segment of the realized update, that

$$\|\nabla_{\theta}^2 \log \pi_{\theta}(y_t \mid x, y_{<t})\| \leq H, \tag{30}$$

where $\|\cdot\|$ denotes the Euclidean norm for vectors and the induced operator norm for matrices. This curvature condition is not needed for Theorem 2; it only supports smoothness interpretations of the LFM path.

For the scalar LFM log-operator $u(z) = c \tanh(z/c)$, Lemma 7 gives $0 < u'(z) \leq 1$ and $|u''(z)| \leq 2/c$. For [NAME C19] under the semi-gradient implementation, the effective derivative is $u'(z)$ because $\Omega$ is stop-gradient, while the operator value is $\exp(u(z) - \Omega(z)) \leq \exp(u(z)) \leq e^c$ by construction. This operator-value interval is distinct from the sharper multiplier certificate $M_{\psi}(c)$ used for second-moment and tail control.

Lemma 9 (Certified operator-value interval). For $u(z) = c \tanh(z/c)$, we have $|u(z)| \leq c$ and hence $\exp(u(z)) \in [e^{-c}, e^c]$ for all $z \in \mathbb{R}$. In [NAME C19], since the hazards are nonnegative, $\Omega(z) \geq 0$ and thus $\omega(e^z) = \exp(u(z) - \Omega(z)) \leq \exp(u(z)) \leq e^c$.

Proof. Since $|\tanh(t)| \leq 1$ for all $t \in \mathbb{R}$, we have

$$|u(z)| = c \left| \tanh(z/c) \right| \leq c.$$

Thus $-c \leq u(z) \leq c$, and exponentiating yields $e^{-c} \leq \exp(u(z)) \leq e^c$ for all $z$. For [NAME C19], since $\Omega(z) \geq 0$, we have $\omega(e^z) = \exp(u(z) - \Omega(z)) \leq \exp(u(z)) \leq e^c$. This bounds the forward ratio operator value; the gradient multiplier is additionally scaled by $u'(z)$ and is therefore controlled by the exact supremum $M_{\psi}(c)$ in Theorem 8.

Proposition 10 (Bounded gradient multiplier implies per-token gradient control). Let $\ell_t(\theta) = -A_t \exp(\phi(z_t(\theta)))$ and $\mathcal{M}_{\phi}(z) = \exp(\phi(z))\phi'(z)$. Under Assumption (29),

$$\|\nabla_{\theta} \ell_t(\theta)\| \leq |A_t| \sup_z |\mathcal{M}_{\phi}(z)| G.$$

Moreover, if $\mathbb{E}[A_t^2] \leq \sigma_A^2$, then

$$\mathbb{E}\left[\|\nabla_{\theta} \ell_t(\theta)\|^2\right] \leq G^2 \mathbb{E}\left[A_t^2 \mathcal{M}_{\phi}(z_t(\theta))^2\right] \leq \sigma_A^2 G^2 \left(\sup_z |\mathcal{M}_{\phi}(z)|\right)^2.$$

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

Proof. Lemma 4 gives the chain-rule form

$$\nabla_\theta \ell_t(\theta) = -A_t \exp(\phi(z_t(\theta))) \phi'(z_t(\theta)) \nabla_\theta z_t(\theta) = -A_t \mathcal{M}_\phi(z_t(\theta)) \nabla_\theta z_t(\theta),$$

where $\mathcal{M}_\phi(z) \triangleq \exp(\phi(z))\phi'(z)$. By Lemma 5, $\nabla_\theta z_t(\theta) = \nabla_\theta \log \pi_\theta(y_t \mid x, y_{<t})$. Substituting yields

$$\nabla_\theta \ell_t(\theta) = -A_t \mathcal{M}_\phi(z_t(\theta)) \nabla_\theta \log \pi_\theta(y_t \mid x, y_{<t}).$$

Taking norms and using Assumption (29) gives

$$\begin{aligned} \|\nabla_\theta \ell_t(\theta)\| &\leq |A_t| \left| \mathcal{M}_\phi(z_t(\theta)) \right| \left\| \nabla_\theta \log \pi_\theta(y_t \mid x, y_{<t}) \right\| \\ &\leq |A_t| \left| \mathcal{M}_\phi(z_t(\theta)) \right| G \\ &\leq |A_t| \left( \sup_{z \in \mathbb{R}} |\mathcal{M}_\phi(z)| \right) G, \end{aligned}$$

which proves the first inequality.

Squaring the exact expression and applying $\|\nabla_\theta \log \pi_\theta(\cdot)\| \leq G$ yields

$$\|\nabla_\theta \ell_t(\theta)\|^2 = A_t^2 \mathcal{M}_\phi(z_t(\theta))^2 \left\| \nabla_\theta \log \pi_\theta(y_t \mid x, y_{<t}) \right\|^2 \leq G^2 A_t^2 \mathcal{M}_\phi(z_t(\theta))^2.$$

Taking expectations gives

$$\begin{aligned} \mathbb{E}\big[\|\nabla_\theta \ell_t(\theta)\|^2\big] &\leq G^2 \mathbb{E}\big[A_t^2 \mathcal{M}_\phi(z_t(\theta))^2\big] \\ &\leq G^2 \left( \sup_{z \in \mathbb{R}} |\mathcal{M}_\phi(z)| \right)^2 \mathbb{E}[A_t^2] \\ &\leq \sigma_A^2 G^2 \left( \sup_{z \in \mathbb{R}} |\mathcal{M}_\phi(z)| \right)^2, \end{aligned}$$

which proves the second-moment bound.

Lemma 11 (Markov's inequality). Let $X$ be a nonnegative random variable with $\mathbb{E}[X] < \infty$. Then for any $\tau > 0$,

$$\Pr(X \geq \tau) \leq \frac{\mathbb{E}[X]}{\tau}.$$

Proof. Since $X \geq 0$, we have $X\mathbf{1}\{X \geq \tau\} \geq \tau\mathbf{1}\{X \geq \tau\}$. Taking expectations yields

$$\mathbb{E}[X] \geq \mathbb{E}\big[X\mathbf{1}\{X \geq \tau\}\big] \geq \tau \Pr(X \geq \tau),$$

which rearranges to the claimed bound.

Corollary 12 (Tail bound from a second moment). Let $Z$ be a (possibly vector-valued) random variable with $\mathbb{E}[\|Z\|^2] < \infty$. Then for any $\tau > 0$,

$$\Pr(\|Z\| \geq \tau) = \Pr(\|Z\|^2 \geq \tau^2) \leq \frac{\mathbb{E}[\|Z\|^2]}{\tau^2}.$$

Proof. Apply Lemma 11 to the nonnegative random variable $X = \|Z\|^2$ with threshold $\tau^2$.

Proof of Theorem 2. Because $\Omega(z) \geq 0$ and $u_c'(z) = \operatorname{sech}^2(z/c) > 0$, the semi-gradient multiplier satisfies

$$0 \leq \mathcal{M}(z) = \exp(u_c(z) - \Omega(z))u_c'(z) \leq \exp(u_c(z))u_c'(z).$$

Taking the supremum over $z$ and applying Theorem 8 gives the multiplier bound in Eq. (19).

For a token in response $i$, define

$$v_t^i = \mathcal{M}(z_t^i(\theta)) \nabla_\theta \log \pi_\theta(q_t^i \mid p, q_{<t}^i) \hat{A}_t^i.$$

By the pointwise multiplier bound,

$$\|v_t^i\|^2 \leq M_\psi(c)^2 (\hat{A}_t^i)^2 \|s_t^i\|^2.$$

## A-page-0017

target PDF page 17

For each realized mini-batch, let $h_i = (1/T_i) \sum_{t=1}^{T_i} v_t^i$. Convexity of $\| \cdot \|^2$ gives

$$\| h_i \|^2 = \left\| \frac{1}{T_i} \sum_{t=1}^{T_i} v_t^i \right\|^2 \leq \frac{1}{T_i} \sum_{t=1}^{T_i} \| v_t^i \|^2.$$

Applying the same convexity argument to $g(\theta) = (1/K) \sum_i h_i$ gives

$$\| g(\theta) \|^2 \leq \frac{1}{K} \sum_{i=1}^{K} \| h_i \|^2 \leq \frac{1}{K} \sum_{i=1}^{K} \frac{1}{T_i} \sum_{t=1}^{T_i} \| v_t^i \|^2.$$

Substituting the pointwise bound and taking expectations of the entire normalized sum yields $\mathbb{E}_\mu \| g \|^2 \leq M_\psi(c)^2 C$ by Eq. (18). This handles random lengths without assuming that unconditional token moments also bound length-conditional moments. Corollary 12 gives the tail bound. No token independence is used. The pointwise multiplier factor remains valid under any behavior law, but its associated product-moment constant must be established for that law.

### B.6 MISMATCH ROBUSTNESS AND THE RATIONALE FOR ASYMMETRIC ACCELERATING HAZARDS

We next state three results connecting the operator to changed behavior laws, autoregressive branch contraction, and accelerating tail regularization.

**Proposition 13** (Multiplier control under a changed behavior law). *Let $\mu$ be any behavior distribution for which the per-token semi-gradient*

$$g_t(\theta) \triangleq -A_t \mathcal{M}(z_t(\theta)) \nabla_\theta \log \pi_\theta(a_t \mid s_t)$$

is well-defined, where $z_t(\theta) = \log[\pi_\theta(a_t \mid s_t)/\pi_{\theta_{\text{old}}}(a_t \mid s_t)]$ and $\mathcal{M}(z) = e^{u(z)-\Omega(z)} u'(z)$ is the implemented semi-gradient multiplier. Assume $\mathbb{E}_\mu [A_t^2] \leq \sigma_A^2$ and $\| \nabla_\theta \log \pi_\theta(a_t \mid s_t) \| \leq G$ almost surely. Then

$$\mathbb{E}_\mu [\| g_t(\theta) \|^2] \leq \sigma_A^2 G^2 M_\psi(c)^2.$$

The same bound holds for deterministic convex averages of these gradients. For random response lengths and weights, the normalized product-moment condition in Eq. (18) gives the main theorem's bound instead.

Proof. By Proposition 10 and Theorem 8,

$$\| g_t(\theta) \| \leq |A_t| \sup_z |\mathcal{M}(z)| G \leq |A_t| M_\psi(c) G.$$

Squaring and taking expectation under $\mu$ gives

$$\mathbb{E}_\mu [\| g_t(\theta) \|^2] \leq M_\psi(c)^2 G^2 \mathbb{E}_\mu [A_t^2] \leq \sigma_A^2 G^2 M_\psi(c)^2.$$

If $\bar{g} = \sum_{j=1}^N \alpha_j g_j$ with deterministic $\alpha_j \geq 0$ and $\sum_j \alpha_j = 1$, then convexity of $\| \cdot \|^2$ yields

$$\| \bar{g} \|^2 \leq \sum_{j=1}^N \alpha_j \| g_j \|^2.$$

Taking expectation and applying the per-token bound to each $g_j$ proves the mini-batch claim.

Proposition 13 separates the pointwise ratio-multiplier bound from the advantage–score moments. The multiplier bound holds under each behavior law, while the corresponding gradient moment bound uses the moments under that law.

**Proposition 14** (Ratio contractions contribute multiplicatively to prefix occupancy). *Let $\pi$ and $\mu$ be two autoregressive policies on the same support. For any realized prompt–trajectory pair $(x, y)$ and any prefix length $t \geq 1$, define the prefix occupancies*

$$d_\pi(x, y_{<t}) = P(x) \prod_{j=0}^{t-1} \pi(y_j \mid x, y_{<j}), \qquad d_\mu(x, y_{<t}) = P(x) \prod_{j=0}^{t-1} \mu(y_j \mid x, y_{<j}),$$

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

(a) Gradient Concentration under Positive Shift

![img-12.jpeg](img-12.jpeg)

(b) Occupancy Decay under Negative Shifts

![img-13.jpeg](img-13.jpeg)

Figure 4: Gradient concentration and prefix contraction. (a) Cumulative gradient contribution sorted in descending order measures the concentration of the learning signal across tokens. (b) Prefix likelihood ratios $R_t = \bar{\rho}^t$ for constant token ratios $\bar{\rho} = 0.90$ and 0.97. At 50 tokens, the ratios are 0.0052 and 0.218, respectively. Both contract relative to the behavior policy, with slower contraction for $\bar{\rho} = 0.97$. These curves evaluate the fixed-ratio product identity.

and the token ratios $\rho_j = \frac{\pi(y_j|x,y_{<j})}{\mu(y_j|x,y_{<j})}$ with $z_j = \log \rho_j$. Then

$$\frac{d_\pi(x, y_{<t})}{d_\mu(x, y_{<t})} = \prod_{j=0}^{t-1} \rho_j = \exp\left(\sum_{j=0}^{t-1} z_j\right).$$

Consequently, if a subset $J \subseteq \{0, \dots, t-1\}$ satisfies $z_j \leq -\delta_j < 0$ for all $j \in J$, then every descendant prefix containing those contractions obeys

$$\frac{d_\pi(x, y_{<t})}{d_\mu(x, y_{<t})} \leq \exp\left(-\sum_{j \in J} \delta_j\right) \prod_{k \notin J, k < t} \rho_k.$$

In particular, $n$ contractions of magnitude at least $\delta$ contribute a factor at most $e^{-n\delta}$ relative to the product of the remaining ratios. The full occupancy ratio combines this contraction factor with the remaining factors, including expansions.

Proof. Substituting the definitions of $d_\pi$ and $d_\mu$ gives

$$\frac{d_\pi(x, y_{<t})}{d_\mu(x, y_{<t})} = \frac{P(x) \prod_{j=0}^{t-1} \pi(y_j \mid x, y_{<j})}{P(x) \prod_{j=0}^{t-1} \mu(y_j \mid x, y_{<j})} = \prod_{j=0}^{t-1} \frac{\pi(y_j \mid x, y_{<j})}{\mu(y_j \mid x, y_{<j})} = \prod_{j=0}^{t-1} \rho_j.$$

Writing $\rho_j = e^{z_j}$ yields the exponential form. If $z_j \leq -\delta_j$ for $j \in J$, then

$$\prod_{j=0}^{t-1} \rho_j = \left(\prod_{j \in J} e^{z_j}\right) \left(\prod_{k \notin J, k < t} \rho_k\right) \leq \exp\left(-\sum_{j \in J} \delta_j\right) \prod_{k \notin J, k < t} \rho_k.$$

Setting $\delta_j \geq \delta$ for $n = |J|$ gives the final bound.

Proposition 14 identifies how repeated contractions reduce the likelihood of a fixed branch relative to its other ratio factors. This motivates protecting useful prefixes against cumulative contraction. Section C connects the identity to local updates and empirical prefix diagnostics.

Proposition 15 ($k > 1$ is the accelerating-hazard regime). Let $H(x) = (x/\lambda)^k$ be the Weibull cumulative hazard, where $\lambda > 0$ and $x > 0$. Then

$$\frac{H(x)}{x} = \frac{x^{k-1}}{\lambda^k}.$$

## A-page-0019

target PDF page 19

If $k > 1$, this ratio is strictly increasing, with

$$\lim_{x \downarrow 0} \frac{H(x)}{x} = 0, \quad \lim_{x \to \infty} \frac{H(x)}{x} = \infty.$$

Hence for any $0 < \eta_{\text{in}} < \eta_{\text{out}}$, there exist $0 < x_{\text{in}} < x_{\text{out}} < \infty$ such that

$$H(x) \leq \eta_{\text{in}} x \quad \text{for all } x \in [0, x_{\text{in}}], \quad H(x) \geq \eta_{\text{out}} x \quad \text{for all } x \geq x_{\text{out}}.$$

If $k = 1$, then $H(x)/x \equiv 1/\lambda$ is constant, so no such scale separation is possible.

Proof. The identity $H(x)/x = x^{k-1}/\lambda^k$ is immediate. When $k > 1$, its derivative

$$\frac{d}{dx} \left( \frac{H(x)}{x} \right) = \frac{k-1}{\lambda^k} x^{k-2}$$

is strictly positive for $x > 0$, so the ratio is strictly increasing. The two limits follow directly. Therefore, given $0 < \eta_{\text{in}} < \eta_{\text{out}}$, we may choose $x_{\text{in}}$ small enough that $H(x)/x \leq \eta_{\text{in}}$ on $(0, x_{\text{in}}]$ and $x_{\text{out}}$ large enough that $H(x)/x \geq \eta_{\text{out}}$ on $[x_{\text{out}}, \infty)$. When $k = 1$, the ratio is the constant $1/\lambda$, so it cannot be simultaneously arbitrarily small near the origin and arbitrarily large in the tail.

Proposition 15 describes the Weibull family on the domain $x > 0$. In [NAME C19], $x_{\pm}(u(z))$ remain in a compact interval because LFM bounds $u$. The operational property is therefore the increase of $H(x)/x$ over the attained magnitudes. Also, $\partial H/\partial k = H \log(x/\lambda)$, so increasing $k$ strengthens attenuation for $x > \lambda$ and weakens it for $x < \lambda$. This gives separate control over attenuation scale and central-to-tail contrast.

Connection to the design. The three propositions explain complementary design choices. Proposition 13 bounds ratio-induced amplification under the stated moment conditions. Proposition 14 identifies the cumulative effect of contraction on branch likelihood. Proposition 15 explains how Weibull shaping controls the increase in attenuation across directional magnitudes.

### B.7 FULL-GRADIENT ANALYSIS OF HAZARD SHAPING AND FAILURE MODES

This final subsection provides the formal justification for the semi-gradient (stop-gradient) implementation of hazard shaping adopted in the main paper. After establishing the bounded semi-gradient analysis above, we contrast it with the fully differentiable (no stop-gradient) variant, which can reverse the gradient sign and does not inherit the same $c$-only attenuation certificate.

### B.7.1 FULL-GRADIENT DERIVATION OF $\Omega'(z)$

Let $u(z) = c \cdot \tanh(z/c)$ (equivalently, $u(z) = \psi(e^z)$), so that $u'(z) = \text{sech}^2(z/c)$. The one-sided magnitudes are $x_+(u) = \text{softplus}(\beta u)/\beta$ and $x_-(u) = \text{softplus}(-\beta u)/\beta$, with derivatives

$$\frac{dx_+}{du} = \text{sigmoid}(\beta u), \quad \frac{dx_-}{du} = -\text{sigmoid}(-\beta u) = -(1 - \text{sigmoid}(\beta u)). \tag{31}$$

The cumulative Weibull hazard $H_+(x_+) = (x_+/\lambda_+)^{k_+}$ has derivative

$$\frac{dH_+}{dx_+} = \frac{k_+}{\lambda_+} \left( \frac{x_+}{\lambda_+} \right)^{k_+ - 1}. \tag{32}$$

Applying the chain rule through $H_+ \circ x_+ \circ u$ and $H_- \circ x_- \circ u$, the full derivative of $\Omega(z) = H_+(x_+(u(z))) + H_-(x_-(u(z)))$ is

$$\Omega'(z) = \text{sech}^2 \left( \frac{z}{c} \right) \left[ \frac{k_+}{\lambda_+} \left( \frac{x_+}{\lambda_+} \right)^{k_+ - 1} \text{sigmoid}(\beta u) - \frac{k_-}{\lambda_-} \left( \frac{x_-}{\lambda_-} \right)^{k_- - 1} (1 - \text{sigmoid}(\beta u)) \right]. \tag{33}$$

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

### B.7.2 FULL-GRADIENT MULTIPLIER ANALYSIS AND SIGN-REVERSAL PHENOMENON

Without stop-gradient, the log-form $\phi(z) = u(z) - \Omega(z)$ is fully differentiable, and the gradient multiplier becomes

$$\mathcal{M}_{\text{full}}(z) = \exp(\phi(z)) \cdot \phi'(z) = \exp(u(z) - \Omega(z)) \cdot [u'(z) - \Omega'(z)]. \tag{34}$$

The critical term is $u'(z) - \Omega'(z)$, which determines the sign of the gradient multiplier. Substituting and factoring out $\text{sech}^2(z/c)$, we obtain

$$\phi'(z) = \text{sech}^2\left(\frac{z}{c}\right) \underbrace{\left[ 1 - \frac{k_+}{\lambda_+}\left(\frac{x_+}{\lambda_+}\right)^{k_+ - 1} \text{sigmoid}(\beta u) + \frac{k_-}{\lambda_-}\left(\frac{x_-}{\lambda_-}\right)^{k_- - 1} (1 - \text{sigmoid}(\beta u)) \right]}_{\triangleq D(z)}. \tag{35}$$

Since $\text{sech}^2(z/c) > 0$ everywhere, the sign of $\mathcal{M}_{\text{full}}(z)$ is entirely determined by $D(z)$.

Problem 1: Parameter-dependent gradient sign reversal. LFM bounds $u(z)$ inside $[-c, c]$, keeping the composed hazard derivative bounded. The full-gradient multiplier changes sign wherever $\Omega'(z) > u'(z)$, which is determined by the directional parameters after removing the common factor $\text{sech}^2(z/c)$. Define, for $a \in [-c, c]$,

$$D_c(a) = 1 - \frac{k_+}{\lambda_+}\left(\frac{x_+(a)}{\lambda_+}\right)^{k_+ - 1} \text{sigmoid}(\beta a) + \frac{k_-}{\lambda_-}\left(\frac{x_-(a)}{\lambda_-}\right)^{k_- - 1} (1 - \text{sigmoid}(\beta a)).$$

Since $u(z) \to c$ as $z \to \infty$ and $u(z) \to -c$ as $z \to -\infty$, we have $\lim_{z \to \infty} D(z) = D_c(c)$ and $\lim_{z \to -\infty} D(z) = D_c(-c)$. Therefore, if $D_c(c) < 0$, there exists a positive-tail region in which $\mathcal{M}_{\text{full}}(z) < 0$; if $D_c(-c) < 0$, the analogous negative-tail sign flip occurs. For such configurations, a token with positive advantage can receive a reversed gradient contribution, because

$$\nabla_\theta \ell_t = -\hat{A}_t \mathcal{M}_{\text{full}}(z_t) \nabla_\theta \log \pi_\theta(\cdot)$$

changes direction when $\mathcal{M}_{\text{full}}(z_t)$ becomes negative. The semi-gradient implementation removes this failure mode by replacing $\phi'(z) = u'(z) - \Omega'(z)$ with the nonnegative effective derivative $u'(z)$.

Problem 2: Loss of the $c$-only attenuation certificate. Under the semi-gradient implementation, the gradient multiplier becomes $\mathcal{M}_{\text{sg}}(z) = \exp(u(z) - \Omega(z)) u'(z) = \exp(u(z)) w(z) u'(z)$ with $w(z) = \exp(-\Omega(z)) \in (0, 1]$. Therefore, its peak is bounded by the exact LFM base certificate $M \le M_\psi(c)$ (Theorem 8). In the full-gradient case, bounding $|\mathcal{M}_{\text{full}}(z)|$ requires analyzing $|D(z)|$, which simultaneously depends on the Weibull parameters $(k_\pm, \lambda_\pm)$, the softplus smoothing $\beta$, and the bound $c$. The branch magnitudes are bounded away from zero and infinity, so $D_c(a)$ is continuous on $[-c, c]$ and yields the finite bound $|\mathcal{M}_{\text{full}}(z)| \le M_\psi(c) \max_{a \in [-c, c]} |D_c(a)|$. Nonnegativity additionally requires $D_c(a) \ge 0$ throughout the attained interval. The implemented semi-gradient removes this parameter-dependent factor, preserving the $c$-only bound and the direction of each direct contribution.

### C MECHANISM: RETAINED SIGNALS, DIRECTIONAL TAILS, AND PREFIX DYNAMICS

[NAME C19] retains useful policy-gradient signals while limiting the influence of extreme ratio deviations. The analysis connects three effects: LFM restores useful clipped-tail contributions, DHP selectively reduces contraction tails, and these directional changes accompany improved retention of correct-response prefixes. Token interventions and directional diagnostics connect the operators to their observed effects.

### C.1 FROM GRPO CLIPPING TO RETAINED TOKEN CONTRIBUTIONS

Fix a sampled token, its advantage $\hat{A}_t$, and the behavior policy. Let $z_t = \log r_t$ and $s_t = \nabla_\theta \log \pi_\theta(a_t \mid s_t^{\text{state}})$. The symbol $s_t^{\text{state}}$ denotes the conditioning prefix, while the vector $s_t$ denotes the score. For the maximization surrogate,

$$J_{\text{GRPO}, t} = \min\{r_t \hat{A}_t, \text{clip}(r_t, 1 - \epsilon, 1 + \epsilon) \hat{A}_t\}, \quad \nabla_\theta r_t = r_t s_t. \tag{36}$$

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

When $\hat{A}_t > 0$, the upper branch becomes constant for $r_t > 1 + \epsilon$. When $\hat{A}_t < 0$, the lower branch becomes constant for $r_t < 1 - \epsilon$. Away from the boundaries,

$$D_t = \mathbf{1}[(\hat{A}_t > 0 \land r_t > 1 + \epsilon) \lor (\hat{A}_t < 0 \land r_t < 1 - \epsilon)], \tag{37}$$

$$\nabla_\theta J_{\text{GRPO},t} = \hat{A}_t r_t (1 - D_t) s_t. \tag{38}$$

Zero-advantage tokens contribute nothing regardless of clipping and are excluded from the dead-token diagnostics. A nonzero-advantage token outside the clip interval is not necessarily dead. For instance, $\hat{A}_t < 0$ and $r_t > 1$ gives an active corrective contribution that decreases the token probability locally.

LFM instead uses $u(z) = c \tanh(z/c)$ and

$$\mathcal{M}_{\text{LFM}}(z) = e^{u(z)} u'(z) = e^{c \tanh(z/c)} \text{sech}^2(z/c), \quad \nabla_\theta J_{\text{LFM},t} = \hat{A}_t \mathcal{M}_{\text{LFM}}(z_t) s_t. \tag{39}$$

Its multiplier is positive for finite $z$, locally agrees with $r = e^z$, and decays in both tails. Hard clipping switches some contributions off, whereas LFM attenuates them continuously. The following diagnostics quantify their retained mass, update alignment, and contribution to performance.

For a diagnostic token set $\mathcal{I}$ with $\hat{A}_t \neq 0$, define

$$f_D = \frac{\sum_{t \in \mathcal{I}} D_t}{|\mathcal{I}|}, \quad m_D = \frac{\sum_{t \in \mathcal{I}} D_t |\hat{A}_t|}{\sum_{t \in \mathcal{I}} |\hat{A}_t|}, \tag{40}$$

$$m_D^{\text{LFM}} = \frac{\sum_{t \in \mathcal{I}} D_t |\hat{A}_t| \mathcal{M}_{\text{LFM}}(z_t)}{\sum_{t \in \mathcal{I}} |\hat{A}_t| \mathcal{M}_{\text{LFM}}(z_t)}, \tag{41}$$

$$\Delta_{\text{align},t} = \text{sign}(\hat{A}_t) \left[ \log \pi_{\text{after}}(a_t \mid s_t^{\text{state}}) - \log \pi_{\text{before}}(a_t \mid s_t^{\text{state}}) \right]. \tag{42}$$

Here $f_D$ counts tokens, $m_D$ weights them by advantage magnitude, and $m_D^{\text{LFM}}$ weights them by LFM's effective scalar coefficient. Coefficient mass is not parameter-gradient norm mass, because score-vector norms and directions also matter. Positive $\Delta_{\text{align}}$ means the realized log-probability change agrees with the advantage direction. GRPO can have nonzero realized changes on its dead set through other tokens' gradients, parameter sharing, and optimizer state.

Signal-retention evidence. At late checkpoints, $f_D = 18.6\%$, $m_D = 27.4\%$, and $m_D^{\text{LFM}} = 34.7\%$. On this set, the average advantage-aligned log-probability change is 0.002 with GRPO and 0.019 with LFM. LFM's best/latest Avg@32 is 52.0/48.5. Applying the exact GRPO-tail mask to its contributions lowers these scores to 49.2/42.6. A shuffled mask matched in count, position, advantage sign, $|A|$ bin, and removed coefficient mass gives 51.1/46.8. The exact mask is more damaging than removing comparable mass elsewhere, showing that the recovered clipped-tail signals contribute to task performance and checkpoint retention.

### C.2 WHAT DHP DOES TO A LOCAL UPDATE

Under the implemented stop-gradient,

$$\mathcal{M}_{\text{[NAME C19]}}(z) = w(z) \mathcal{M}_{\text{LFM}}(z), \quad w(z) = e^{-\Omega(z)} \in (0, 1]. \tag{43}$$

This is an exact identity for a direct token contribution. To connect it to a probability change, consider one isolated-token SGD ascent step at the same initial $\theta$, with fixed $\hat{A}_t$, $s_t$, and learning rate $\eta$:

$$\delta\theta_{\text{LFM}} = \eta \hat{A}_t \mathcal{M}_{\text{LFM}}(z_t) s_t, \tag{44}$$

$$\delta\theta_{\text{[NAME C19]}} = \eta \hat{A}_t \mathcal{M}_{\text{[NAME C19]}}(z_t) s_t = w(z_t) \delta\theta_{\text{LFM}}. \tag{45}$$

$\delta\theta_{\text{LFM}}$ denotes the parameter displacement caused by this token under LFM alone, evaluated at the common initial $\theta$.

Let $\Delta z_X = z_t(\theta + \delta\theta_X) - z_t(\theta)$ for $X \in \{\text{LFM}, \text{[NAME C19]}\}$. If the score Hessian has norm at most $H$ along the two step segments, Taylor's theorem gives

$$\Delta z_{\text{LFM}} = s_t^\top \delta\theta_{\text{LFM}} + R_L, \quad |R_L| \le \frac{H}{2} \|\delta\theta_{\text{LFM}}\|^2, \tag{46}$$

$$\Delta z_{\text{[NAME C19]}} = w(z_t) s_t^\top \delta\theta_{\text{LFM}} + R_M, \quad |R_M| \le \frac{H}{2} w(z_t)^2 \|\delta\theta_{\text{LFM}}\|^2. \tag{47}$$

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

Subtracting $w(z_t)\Delta z_{\mathrm{LFM}}$ yields

$$|\Delta z_{\mathrm{[NAME C19]}} - w(z_t)\Delta z_{\mathrm{LFM}}| \leq \frac{H}{2} \left(w(z_t)^2 + w(z_t)\right) \|\delta\theta_{\mathrm{LFM}}\|^2 = O(\eta^2). \tag{48}$$

The parameter-step relation is exact in this isolated-token setup, whereas the log-probability relation is first-order. Since $s_t^\top \delta\theta_{\mathrm{LFM}} = \eta \hat{A}_t \mathcal{M}_{\mathrm{LFM}} \|s_t\|^2$, a negative advantage causes a direct decrease. If $z_t < 0$ already, this reinforces an existing contraction, and DHP reduces its first-order magnitude. If $\hat{A}_t > 0$ with $z_t < 0$, the update is corrective, and DHP also attenuates that correction. Thus ratio direction controls attenuation, while advantage sign determines the direct update direction.

**Shared-parameter updates.** For a mini-batch with normalized weights $\alpha_t$, the first-order SGD expansion underlying Eq. (12) gives the evaluated token $j$

$$\Delta z_j = \eta \sum_t \alpha_t \hat{A}_t \mathcal{M}_t s_j^\top s_t + O(\eta^2). \tag{49}$$

Cross-token inner products can have either sign, and DHP applies a token-specific $w_t$ to each term. Consequently, mini-batch updates combine differently weighted score interactions. Optimizer state and repeated actor steps further shape the realized probability changes. The directional-tail and prefix diagnostics below measure these effects during training.

### C.3 DIRECTIONAL-TAIL SEVERITY AND CVAR

Negative-tail 1%-CVaR (conditional value at risk) is the mean contraction severity in the worst 1% of tokens. Define $L = (-z)_+ = \max(0, -\log r)$ and tail fraction $\alpha = 0.01$. A definition valid even when the distribution has atoms is

$$\mathrm{CVaR}_\alpha^{\mathrm{upper}}(L) = \min_{v \in \mathbb{R}} \left\{ v + \frac{1}{\alpha} \mathbb{E}[(L - v)_+] \right\}. \tag{50}$$

For a continuous distribution, this equals $\mathbb{E}[L \mid L \geq Q_{1-\alpha}(L)]$. For an empirical sample, replace the expectation with its sample mean. This averages the top $\alpha$ fraction, with fractional boundary weight if necessary. VaR identifies where the worst tail starts. CVaR says how severe that tail is on average. Because larger $L$ means a smaller token ratio, a lower value indicates less severe contraction. CVaR 1.18 corresponds to a geometric mean ratio $e^{-1.18} \approx 0.307$ within that negative tail, not to an arithmetic mean ratio or a prefix probability.

Tail frequency and severity measure different properties. With GRPO's $\epsilon = 0.2$, define

$$f_- = \operatorname{Pr}(z < \log(1 - \epsilon)), \quad f_+ = \operatorname{Pr}(z > \log(1 + \epsilon)). \tag{51}$$

Unlike the dead set, these quantities describe ratio direction without conditioning on advantage sign. The negative-tail frequency and CVaR are 8.9% and 1.18 with LFM, versus 3.9% and 0.63 with [NAME C19]. A per-batch scalar attenuation control matched to [NAME C19]'s update norm gives 8.0% and 1.09. [NAME C19] therefore reduces contraction frequency and severity beyond the uniform attenuation control. Compared with symmetric DHP, [NAME C19] retains more expansion-side variation, with $f_+ = 7.1\%$ versus 5.8% and a highest-1% mean $z$ of 0.91 versus 0.77. Together, these comparisons show selective regulation of the two directional tails.

### C.4 FROM TOKEN CONTRACTION TO PREFIX LIKELIHOOD

For a fixed response with a common prompt and behavior-policy reference,

$$C_{i,t} = \sum_{j=1}^t \log r_{i,j} = \log \frac{\pi_\theta(q_{\leq t}^i \mid p)}{\pi_{\theta_{\mathrm{old}}}(q_{\leq t}^i \mid p)}, \quad R_{i,t} = e^{C_{i,t}}. \tag{52}$$

Each token ratio is a multiplicative factor in $R_{i,t}$. For example, ten factors of 0.9 contribute $0.9^{10} \approx 0.349$ relative to the remaining factors. The full prefix ratio combines these contractions with the expansions along the same response, motivating a trajectory-level measure of their cumulative effect.

For threshold $a = 0.1$, define

$$F_a(i) = \mathbf{1} \left[ \min_{1 \leq t \leq T_i} C_{i,t} < \log a \right], \quad \tau_a(i) = \inf\{t : C_{i,t} < \log a\}. \tag{53}$$

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

The collapse rate is the fraction of responses with $F_a(i) = 1$. It means that at some depth the prefix is assigned less than one tenth of its behavior-policy likelihood, not that the final answer is incorrect. For noncrossing responses, $\tau_a = \infty$. The reported first-crossing median is conditional on $F_a = 1$, excluding noncrossers rather than assigning them the maximum response length. Because the crossing subset can differ between methods, the conditional median should be interpreted alongside the collapse rate, not as an unconditional delay estimate.

On correct responses, the collapse rate is 13.2% for LFM, 11.5% for the norm-matched scalar control, and 4.9% for [NAME C19]. Among crossing responses, the median first-crossing depth changes from 846 tokens with LFM to 1,487 with [NAME C19]. Correct responses directly expose the loss of useful trajectory probability. Their lower collapse rate connects the observed directional-tail reduction to improved prefix retention.

Connection back to the motivation. The evidence follows the design's two roles. LFM retains nonnegligible, advantage-aligned coefficients in regions that GRPO clips away, and masking those specific contributions harms performance. DHP changes contraction-tail frequency and severity beyond the tested scalar control, accompanied by fewer collapsed correct-response prefixes. The component results (50.8 for DHP, 52.0 for LFM, and 52.9 for the combination) and checkpoint retention in Table 6 are consistent with this division of labor. Together, the results support useful signal retention and selective contraction control as complementary mechanisms underlying [NAME C19]'s performance.

### D ADDITIONAL RESULTS ACROSS BACKBONE SETTINGS

This appendix provides additional main-result evaluations on instruction-tuned backbones, which complement the foundation-model results reported in the main paper on Qwen3-4B-Base and Qwen3-30B-A3B-Base. Table 5 reports Avg@32 on three instruction-tuned backbones: a general-purpose model (Qwen2.5-7B-Instruct), a domain-specialized model (Qwen2.5-Math-7B-Instruct), and a vision-language model (Qwen2.5-VL-7B-Instruct).

Domain-specialized and general-purpose models. On the general-purpose Qwen2.5-7B-Instruct backbone (Table 5A), [NAME C19] reaches a macro-average of 43.7%, outperforming the strongest baseline DAPO by 3.5 points. On the domain-specialized Qwen2.5-Math-7B-Instruct (Table 5B), [NAME C19] reaches 47.8%, exceeding DAPO by 4.2 points. The gains are largest on the most challenging benchmarks. On HMMT25, [NAME C19] reaches 17.9% against DAPO's 11.5%, a gap of +6.4 points. On AIME25, [NAME C19] reaches 21.6% against 15.0%, a gap of +6.6 points. These results indicate that the proposed framework delivers consistent improvements even when the backbone already carries strong domain priors.

Text-only and vision-language models. On Qwen2.5-VL-7B-Instruct (Table 5C), [NAME C19] reaches 53.0%, 5.5 points above the initial backbone and 0.7 points above DAPO. The MathVision gains are 5.3 and 1.4 points, respectively. These results extend the observed improvements from text-only to vision-language reasoning.

The complementary distilled-model comparison appears in Section 4.4 and Table 4. Across these Qwen-derived backbones, [NAME C19] uses the same operator interface of token log-probabilities and advantages.

### E CHECKPOINT ROBUSTNESS ANALYSIS

This appendix provides the full per-benchmark comparison between the best (peak) and latest (final) checkpoints on Qwen3-4B-Base. Table 6 expands the summary statement given in the training-stability analysis of the main paper.

DAPO's macro-average drops from 43.6% to 31.4%, while the other baselines lose 6.9–8.2 points. [NAME C19] loses 0.8 points, from 52.9% to 52.1%. This improved checkpoint retention is consistent with the token and prefix diagnostics in Section C: LFM retains useful learning signals, DHP reduces directional contraction, and their combination retains more of its achieved task performance.

## A-page-0024

target PDF page 24

1242
1243
1244
1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295

Table 5: Additional results on instruction-tuned backbones. We report Avg@32 (%) for the best checkpoint. Subtable (A) uses Qwen2.5-7B-Instruct, Subtable (B) uses Qwen2.5-Math-7B-Instruct, and Subtable (C) uses Qwen2.5-VL-7B-Instruct.

[tbl-4.html](tbl-4.html)

(B) Qwen2.5-Math-7B-Instruct

[tbl-5.html](tbl-5.html)

(C) Qwen2.5-VL-7B-Instruct

[tbl-6.html](tbl-6.html)

Table 6: Training stability comparison between the best and latest checkpoints on Qwen3-4B-Base. We report Avg@32 (%) with separate columns for the best checkpoint and the final checkpoint.  \( \Delta \)  denotes the change from best to latest. [NAME C19] shows the smallest degradation.

[tbl-7.html](tbl-7.html)

## F LIMITATIONS

The empirical scope is verifiable mathematical reasoning on Qwen-derived text and vision-language backbones. Mechanism diagnostics use Qwen3-4B, and the reported prefix-collapse comparisons focus on correct responses. Four DHP parameters are shared across the five original backbones, while the LFM range c is backbone-dependent. The sensitivity analysis varies one factor at a time.

[OCR table id=tbl-4.html; page=24]
<table><tr><td colspan="7">(A) Qwen2.5-7B-Instruct</td></tr><tr><td>Method</td><td>MATH500</td><td>HMMT25</td><td>AMC23</td><td>AIME25</td><td>AIME24</td><td>Avg.</td></tr><tr><td>Baseline</td><td>70.0 (+0.0)</td><td>5.6 (+0.0)</td><td>52.4 (+0.0)</td><td>3.5 (+0.0)</td><td>16.4 (+0.0)</td><td>29.6 (+0.0)</td></tr><tr><td>GRPO</td><td>79.2 (+9.2)</td><td>7.8 (+2.2)</td><td>68.3 (+15.9)</td><td>8.6 (+5.1)</td><td>27.4 (+11.0)</td><td>38.3 (+8.7)</td></tr><tr><td>GSPO</td><td>80.6 (+10.6)</td><td>8.5 (+2.9)</td><td>70.1 (+17.7)</td><td>10.8 (+7.3)</td><td>26.8 (+10.4)</td><td>39.4 (+9.8)</td></tr><tr><td>DAPO</td><td>81.2 (+11.2)</td><td>9.1 (+3.5)</td><td>71.3 (+18.9)</td><td>11.4 (+7.9)</td><td>28.0 (+11.6)</td><td>40.2 (+10.6)</td></tr><tr><td>SAPO</td><td>80.4 (+10.4)</td><td>8.0 (+2.4)</td><td>69.2 (+16.8)</td><td>10.1 (+6.6)</td><td>27.1 (+10.7)</td><td>39.0 (+9.4)</td></tr><tr><td>[NAME C19] (Ours)</td><td>82.1 (+12.1)</td><td>13.8 (+8.2)</td><td>74.6 (+22.2)</td><td>16.7 (+13.2)</td><td>31.5 (+15.1)</td><td>43.7 (+14.1)</td></tr></table>

[OCR table id=tbl-5.html; page=24]
<table><tr><td>Method</td><td>MATH500</td><td>HMMT25</td><td>AMC23</td><td>AIME25</td><td>AIME24</td><td>Avg.</td></tr><tr><td>Baseline</td><td>73.1 (+0.0)</td><td>7.5 (+0.0)</td><td>56.3 (+0.0)</td><td>7.7 (+0.0)</td><td>15.1 (+0.0)</td><td>31.9 (+0.0)</td></tr><tr><td>GRPO</td><td>82.3 (+9.2)</td><td>9.6 (+2.1)</td><td>72.4 (+16.1)</td><td>11.0 (+3.3)</td><td>30.8 (+15.7)</td><td>41.2 (+9.3)</td></tr><tr><td>GSPO</td><td>83.8 (+10.7)</td><td>10.9 (+3.4)</td><td>74.6 (+18.3)</td><td>14.2 (+6.5)</td><td>30.1 (+15.0)</td><td>42.7 (+10.8)</td></tr><tr><td>DAPO</td><td>84.4 (+11.3)</td><td>11.5 (+4.0)</td><td>75.8 (+19.5)</td><td>15.0 (+7.3)</td><td>31.2 (+16.1)</td><td>43.6 (+11.7)</td></tr><tr><td>SAPO</td><td>83.6 (+10.5)</td><td>10.0 (+2.5)</td><td>72.5 (+16.2)</td><td>13.1 (+5.4)</td><td>30.0 (+14.9)</td><td>41.8 (+9.9)</td></tr><tr><td>[NAME C19] (Ours)</td><td>85.2 (+12.1)</td><td>17.9 (+10.4)</td><td>79.3 (+23.0)</td><td>21.6 (+13.9)</td><td>35.1 (+20.0)</td><td>47.8 (+15.9)</td></tr></table>

[OCR table id=tbl-6.html; page=24]
<table><tr><td>Method</td><td>MathVista</td><td>MathVision</td><td>MathVerse</td><td>Avg.</td></tr><tr><td>Baseline</td><td>67.8 (+0.0)</td><td>25.2 (+0.0)</td><td>49.5 (+0.0)</td><td>47.5 (+0.0)</td></tr><tr><td>GRPO</td><td>68.6 (+0.8)</td><td>27.3 (+2.1)</td><td>52.7 (+3.2)</td><td>49.5 (+2.0)</td></tr><tr><td>GSPO</td><td>69.1 (+1.3)</td><td>27.4 (+2.2)</td><td>52.1 (+2.6)</td><td>49.5 (+2.0)</td></tr><tr><td>DAPO</td><td>71.2 (+3.4)</td><td>29.1 (+3.9)</td><td>56.5 (+7.0)</td><td>52.3 (+4.8)</td></tr><tr><td>SAPO</td><td>70.7 (+2.9)</td><td>28.6 (+3.4)</td><td>56.3 (+6.8)</td><td>51.9 (+4.4)</td></tr><tr><td>[NAME C19] (Ours)</td><td>71.8 (+4.0)</td><td>30.5 (+5.3)</td><td>56.7 (+7.2)</td><td>53.0 (+5.5)</td></tr></table>

[OCR table id=tbl-7.html; page=24]
<table><tr><td rowspan="2">Method</td><td colspan="2">MATH500</td><td colspan="2">HMMT25</td><td colspan="2">AMC23</td><td colspan="2">AIME25</td><td colspan="2">AIME24</td><td colspan="2">Avg.</td><td rowspan="2">\( \Delta \)</td></tr><tr><td>Best</td><td>Latest</td><td>Best</td><td>Latest</td><td>Best</td><td>Latest</td><td>Best</td><td>Latest</td><td>Best</td><td>Latest</td><td>Best</td><td>Latest</td></tr><tr><td>GRPO</td><td>64.8</td><td>58.9</td><td>11.1</td><td>8.8</td><td>81.3</td><td>72.5</td><td>30.8</td><td>23.3</td><td>40.4</td><td>24.2</td><td>45.7</td><td>37.5</td><td>-8.2</td></tr><tr><td>GSPO</td><td>66.2</td><td>59.9</td><td>12.4</td><td>8.6</td><td>83.5</td><td>75.9</td><td>34.0</td><td>25.9</td><td>39.7</td><td>27.0</td><td>47.2</td><td>39.5</td><td>-7.7</td></tr><tr><td>DAPO</td><td>64.0</td><td>47.5</td><td>14.9</td><td>7.0</td><td>75.8</td><td>66.3</td><td>29.2</td><td>17.9</td><td>34.2</td><td>18.4</td><td>43.6</td><td>31.4</td><td>-12.2</td></tr><tr><td>SAPO</td><td>66.4</td><td>59.2</td><td>11.5</td><td>7.3</td><td>81.4</td><td>77.6</td><td>32.9</td><td>23.4</td><td>39.6</td><td>24.0</td><td>46.4</td><td>38.3</td><td>-8.1</td></tr><tr><td>CISPO</td><td>69.0</td><td>63.2</td><td>11.0</td><td>7.8</td><td>85.3</td><td>78.4</td><td>33.5</td><td>26.0</td><td>43.7</td><td>32.5</td><td>48.5</td><td>41.6</td><td>-6.9</td></tr><tr><td>MASPO</td><td>67.5</td><td>60.8</td><td>12.8</td><td>8.3</td><td>82.6</td><td>76.0</td><td>34.5</td><td>26.8</td><td>40.8</td><td>29.1</td><td>47.6</td><td>40.2</td><td>-7.4</td></tr><tr><td>[NAME C19] (Ours)</td><td>70.9</td><td>70.1</td><td>19.4</td><td>19.4</td><td>88.2</td><td>88.2</td><td>41.4</td><td>40.8</td><td>44.7</td><td>41.8</td><td>52.9</td><td>52.1</td><td>-0.8</td></tr></table>

## A-page-0025

target PDF page 25

1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
1335
1336
1337
1338
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348
1349

The gradient moment certificate is local to the current parameter value and requires the stated advantage–score product-moment condition. DHP attenuates direct contributions according to ratio direction, including corrective updates when $\hat{A}_t > 0$ and $z_t < 0$. Shared-parameter interactions and optimizer state determine how these contributions combine into realized probability changes, as detailed in Appendix C.2.
