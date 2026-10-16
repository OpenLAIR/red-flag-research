# [TITLE C11]

## A-page-0001

target PDF page 1

# [TITLE C11]

Anonymous authors

Paper under double-blind review

# ABSTRACT

Internal attribution explains predictions by assigning credit to hidden units. Yet a network function does not determine hidden coordinates: a compensated invertible affine change can preserve outputs while changing coordinate scores. We formulate this as an identifiability problem for function-level interventions. For conductance, we derive the similarity law under the full affine gauge and show that, for nonscalar conductance matrices, every trace-compatible coordinate attribution vector is attainable under a function-preserving gauge; completeness therefore constrains only the trace. We replace coordinate credit with isolated spectral subspaces defined by Riesz projectors, whose interventions commute with the hidden gauge, and evaluate this criterion with a frozen protocol across vision and language modalities. Specifically, gauges change conventional coordinate winners, while spectral scores remain invariant and dominant clusters yield larger target-conditioned effects than matched-rank comparators; they also beat the entire complement on a text holdout. Attack paths show conditional magnitude but mixed direction, with near-modulus ties failing the isolation gate. Thus, spectral subspaces provide function-compatible intervention targets, while coordinate conductance remains parameterization-relative. The code is available at an anonymous repository.

# 1 INTRODUCTION

Attribution asks which part of a model deserves credit for a prediction. Input coordinates are externally fixed, but a hidden layer is a representation space: an invertible change of hidden coordinates can be canceled downstream without changing any input-output behavior. Internal attribution nevertheless often treats a named neuron as functionally intrinsic. Conductance makes this concrete. It extends Integrated Gradients to hidden neurons, satisfies completeness, and supports ranking, pruning, and mechanistic narratives (Sundararajan et al., 2017; Dhamdhere et al., 2018; Lundstrom et al., 2022); yet completeness fixes only their sum, not whether any individual score belongs to the represented function. That distinction matters whenever a claim uses neuron identity, sign, ordering, or sparsity. Figure 1 visualizes this ambiguity: function-preserving hidden-basis changes move coordinate credit while preserving its total. Thus, in general, coordinate conductance is not a function-level object under the full affine gauge; we therefore seek a gauge-equivariant intervention target.

We expose the exact algebra behind this ambiguity. For a hidden path, each coordinate score is one diagonal entry of a conductance matrix. Changing hidden coordinates and compensating

downstream leaves model outputs unchanged, but can change these diagonal entries while preserving their sum. Fillmore's theorem (Fillmore, 1969) says that, for a nonscalar matrix, every coordinate attribution vector with the same total can be reached by such a function-preserving change. When the completeness total is nonzero, a coordinate that starts at the bottom can become uniquely top-ranked and absorb essentially all absolute attribution mass while logits remain unchanged.

![img-0.jpeg](img-0.jpeg)

Figure 1: For a nonscalar conductance matrix, coordinate conductance is not determined by the represented function. The axes are its diagonal entries $C_{11}, C_{22}, C_{33}$; function-preserving hidden-basis changes move between points with the same total $C_{11} + C_{22} + C_{33}$. The star marks the original gauge.

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

The negative result also tells us what a function-level intervention target must preserve: it should transform with the hidden representation rather than depend on its coordinate axes. Similarity does not preserve coordinate axes, but it carries isolated spectral subspaces equivariantly. We therefore use a Riesz projector (Kato, 1995) to select such a subspace. Removing the displacement in that subspace defines a gauge-compatible intervention, including for non-normal matrices when the cluster is isolated. Figure 2¹ depicts this replacement as an equivariant projector and projected displacement.

![img-1.jpeg](img-1.jpeg)

Figure 2: Gauge-equivariant spectral intervention. Gray arrows show the original displacement Δz. Red and blue arrows show the removed PΔz and retained (I - P)Δz projections. The right panel is the M-transformed decomposition.

This construction gives a concrete methodological criterion: an attribution intended to support a function-level intervention should be gauge-equivariant, and the induced intervention should commute with the gauge. The spectral projector meets that algebraic criterion; the experiments test its numerical stability, output effect, cross-modal replication of the protocol, and behavior on attack-generated endpoints. We evaluate this criterion under a frozen protocol, with a matched-rank comparator and separate tests of gauge validity, intervention utility, and adversarial endpoint stress. In summary, our contributions are as follows:

- Conceptually, we formulate internal attribution as identifiability under the full affine gauge of a hidden representation, separating useful parameterization-relative scores from credit intrinsic to the represented network function, clarifying when internal scores can support function-level claims.
- Theoretically, we prove the nonlinear conductance similarity law and combine it with the prescribed-diagonal theorem to characterize the coordinate orbit: outside the scalar exception, completeness constrains only the trace, thereby ruling out function-intrinsic coordinate rankings.
- Technically, we introduce Riesz-projector interventions that commute with invertible basis changes, and make them auditable through cluster, eigengap, projector-norm, collision, and conditioning diagnostics, with theoretical coverage of non-normal matrices for isolated spectral clusters.
- Empirically, we cover 27 vision and 9 text-environment cells, relocation, 2,592 gauges, conditioning, rank-matched/complement holdouts, and attack-path tests across architectures and non-saturated budgets; magnitude and signed direction are estimands, while isolation is a validity diagnostic.

## 2 RELATED WORK

Internal attribution and feature interpretation. Integrated Gradients attributes a prediction difference along a baseline-to-input path and motivates implementation invariance for fixed input features (Sundararajan et al., 2017); related methods propagate relevance, localize gradients, or fit local surrogates (Bach et al., 2015; Shrikumar et al., 2017; Selvaraju et al., 2017; Smilkov et al., 2017; Ribeiro et al., 2016; Lundberg & Lee, 2017; Ancona et al., 2018). Conductance applies the chain rule along the same path to hidden neurons, with later work studying its axioms and extensions (Dhamdhere et al., 2018; Lundstrom et al., 2022). These guarantees do not imply invariant hidden-coordinate attributions under basis changes. We instead ask whether conductance's coordinate decomposition is identifiable when a compensated affine map is inserted at a hidden cut.

Unit and concept interpretation. Interpretability often studies individual neurons or directions through activation maximization, unit selection, probing, ablation, or concept alignment. Network Dissection aligns units with labeled concepts, while TCAV tests concept directions rather than single units (Bau et al., 2017; Kim et al., 2018); related work studies concept discovery, feature visualization, ablation, and superposition (Ghorbani et al., 2019; Koh et al., 2020; Olah et al., 2017; Bau et al., 2020; Elhage et al., 2022). Sanity checks, removal and faithfulness benchmarks, infidelity analyses, and alternative Shapley formulations show that interpretation depends on estimator, perturbation, and reference choices (Adebayo et al., 2018; Kindermans et al., 2019; Hooker et al., 2019; Yeh et al., 2019; Sundararajan & Najmi, 2020; Edin et al., 2025). Recent work also shows that influence-based attributions can be systematically altered by small model perturbations (Yadav et al., 2026),

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

reinforcing the need to state which transformations an attribution claim is meant to survive. Sparse dictionary learning adds an explicit sparsity prior to select a preferred feature basis (Huben et al., 2024); this is a gauge-fixing assumption, not a proof that the selected coordinate is function-intrinsic. Our theorem instead holds the represented function exactly fixed and varies only its hidden basis, so unit-level tools remain useful as parameterization-relative analyses.

**Adversarial robustness and endpoint geometry.** Adversarial robustness work uses optimization-generated endpoint perturbations to test model behavior, including projected-gradient procedures and strong parameter-free attack suites (Madry et al., 2018; Croce & Hein, 2020). We use these endpoints as controlled stress tests rather than as a robustness benchmark; recent evaluation work emphasizes that local adversarial statistics need not summarize global robustness (Li et al., 2024).

**Representation similarity and identifiability.** Representation-similarity and identifiability work compares activation spaces or recoverability under restricted transformation classes (Raghu et al., 2017; Morcos et al., 2018; Kornblith et al., 2019; Ding et al., 2021; Williams et al., 2021; Roeder et al., 2021). Permutation and broader parameter symmetries also affect model comparison and merging (Entezari et al., 2022; Ainsworth et al., 2023; Godfrey et al., 2022), while other attribution results study rescaling or translation invariance (Xu et al., 2020; Lundstrom et al., 2022). Related identifiability theory for unsupervised concept extraction treats guarantees for latent concepts as a prerequisite for downstream steering and unlearning (Squires, 2026). These lines either compare representations or impose restricted equivalences. Our cut-level functional-equivalence construction permits arbitrary $M \in GL(d)$, including dense basis changes, without requiring $M$ and $M^{-1}$ to be absorbable into the original layer types; we derive its action on a path-integrated attribution matrix and distinguish invariant scalars from equivariant subspaces that can support interventions.

**Causal interventions and algebraic scope.** Causal abstraction and mediation approaches use internal interventions to connect neural states with higher-level variables (Pearl, 2009; Geiger et al., 2021; Vig et al., 2020; Meng et al., 2022). Our criterion is algebraic rather than semantic: changing coordinates and then intervening must agree with intervening and then changing coordinates, which excludes conclusions created solely by the hidden basis without claiming a causal model. Fillmore's prescribed-diagonal theorem is classical (Fillmore, 1969); we apply it to conductance, derive the nonlinear gauge law, and construct and validate a Riesz-projector intervention on its similarity orbit.

### 3 METHODOLOGY

Figure 3 traces the matrix, gauge, and equivariant-intervention steps tested across modalities. Table 7 provides a compact reference for the notation and terminology used throughout the paper.

![img-2.jpeg](img-2.jpeg)

Figure 3: Method overview. Path integration constructs the conductance matrix; a compensated hidden-basis change preserves the network function but moves coordinate credit; an isolated spectral cluster yields an equivariant projector; and the resulting intervention is tested with the same rule in vision and language models.

### 3.1 CONDUCTANCE IS A MATRIX DIAGONAL

Let a scalar network output factor at a hidden cut be $F = G \circ H$, with $\mathcal{X} \subseteq \mathbb{R}^m$, $H : \mathcal{X} \to \mathbb{R}^d$, and $G : \mathbb{R}^d \to \mathbb{R}$. For a piecewise continuously differentiable input path $\gamma : [0, 1] \to \mathcal{X}$, write

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

$z(t) = H(\gamma(t))$. Using column-vector gradients, define the conductance matrix

$$C(\gamma; H, G) = \int_0^1 \dot{z}(t) \nabla G(z(t))^{\top} dt. \tag{1}$$

The conventional conductance of hidden coordinate $i$ is $\text{Cond}_i = C_{ii}$. Summing coordinates gives

$$\sum_{i=1}^d \text{Cond}_i = \text{tr}(C) = \int_0^1 \nabla G(z(t))^{\top} \dot{z}(t) dt = F(\gamma(1)) - F(\gamma(0)). \tag{2}$$

Thus Eq. 2 is the trace identity for $C$. Equation 1 retains cross-coordinate transport terms that the conventional diagonal discards. Figure 1 visualizes this fixed-trace coordinate orbit.

### 3.2 THE AFFINE HIDDEN GAUGE

For $M \in GL(d)$ and $c \in \mathbb{R}^d$, define

$$\widetilde{H}(x) = MH(x) + c, \quad \widetilde{G}(\widetilde{z}) = G\big(M^{-1}(\widetilde{z} - c)\big). \tag{3}$$

The transformed network is pointwise identical: $\widetilde{G} \circ \widetilde{H} = G \circ H$. This is not an approximation, retraining procedure, or distributional equivalence; it preserves every network output on every input. It is a function-equivalence construction: unless the adjacent layers can absorb $M$, $M^{-1}$, and $c$, it is an equivalent implementation with an inserted affine interface rather than a reparameterization inside the original architecture.

**Theorem 1** (Conductance similarity law). Assume that $z$ is absolutely continuous and that $G$ is locally Lipschitz near the path, with the pathwise chain rule holding almost everywhere; $C^1$ smoothness is a sufficient special case. Under the compensated affine gauge in Eq. 3,

$$\widetilde{C} = M C M^{-1}. \tag{4}$$

Proof. Translation vanishes on differentiation, so $\dot{\widetilde{z}} = M\dot{z}$. The a.e. chain rule gives $\nabla_{\widetilde{z}}\widetilde{G} = M^{-\top}\nabla_z G$ wherever the derivatives exist; the exceptional null set does not change the integral. Substitution into Eq. 1 yields $\widetilde{C} = \int M\dot{z}\nabla G(z)^{\top}M^{-1}dt = M C M^{-1}$. $\square$

The theorem applies to cuts whose pathwise chain rule holds, including the evaluated ReLU paths; for vector outputs, fix a scalar logit, margin, or loss, since target choice is part of the estimand.

### 3.3 COMPLETE COORDINATE CONTROLLABILITY

Similarity preserves trace, determinant, characteristic polynomial, Jordan structure, and traces of powers. It does not preserve the diagonal.

**Theorem 2** (Complete coordinate controllability). Let $C \in \mathbb{R}^{d \times d}$ be nonscalar. For every $a \in \mathbb{R}^d$ satisfying $\mathbf{1}^{\top}a = \text{tr}(C)$, there exists $M \in GL(d)$ such that

$$\text{diag}(M C M^{-1}) = a. \tag{5}$$

If $C = \lambda I$, its diagonal is fixed under every similarity.

Proof. The nonscalar statement is Fillmore's prescribed-diagonal theorem applied to $C$ (Fillmore, 1969). The exception follows immediately from $M(\lambda I)M^{-1} = \lambda I$. $\square$

**Corollary 3** (Coordinate claims are not identified). For nonscalar $C$, the maximally credited coordinate, coordinate ranking, sign pattern subject to the trace, and coordinate sparsity can all be changed by an exact function-preserving gauge.

This result is stronger than exhibiting one counterexample. The attainable set in Eq. 5 is the entire affine hyperplane defined by completeness. Declaring a smaller gauge group can restore coordinate structure, but that declaration is an additional modeling assumption. For example, an orthogonal gauge preserves Euclidean geometry but still mixes axes; a permutation gauge preserves the multiset of scores but not neuron names.

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

### 3.4 GAUGE-IDENTIFIED SPECTRAL SUBSPACES

To replace coordinate credit, we seek an object that transforms with the representation. Let $\Lambda$ be a separated cluster of eigenvalues of $C$ and let $\Gamma$ be a positively oriented contour enclosing only that cluster. Its Riesz projector (Kato, 1995) is defined by Eq. 6:

$$P_{\Lambda}(C) = \frac{1}{2\pi i} \oint_{\Gamma} (\xi I - C)^{-1} d\xi. \tag{6}$$

This definition remains valid for non-normal matrices and repeated eigenvalues, provided the selected cluster is isolated.

**Proposition 4** (Projector equivariance). *For every invertible $M$,*

$$P_{\Lambda}(MCM^{-1}) = MP_{\Lambda}(C)M^{-1}. \tag{7}$$

*Proof.* The relation in Eq. 7 follows because the resolvent satisfies $(\xi I - MCM^{-1})^{-1} = M(\xi I - C)^{-1}M^{-1}$. Integrating around the same spectral cluster proves the claim. $\square$

Given the endpoint displacement $\Delta z = z(1) - z(0)$, write $P = P_{\Lambda}(C)$ for a selected cluster and remove its selected spectral projection via

$$\mathcal{I}_P(\Delta z) = (I - P)\Delta z. \tag{8}$$

The corresponding intervened endpoint is $z(0) + \mathcal{I}_P(\Delta z)$. In the transformed basis, $(I - MPM^{-1})M\Delta z = M(I - P)\Delta z$. After mapping back, the intervened hidden state and downstream output are identical in every gauge. Figure 2 depicts commutation. Coordinate ablation fails this commutation relation because a coordinate axis does not generally map to a coordinate axis.

### 3.5 SELECTION RULE AND NUMERICAL DIAGNOSTICS

Equivariance alone does not choose among spectral clusters: the theory permits any isolated cluster. The protocol takes the largest-modulus candidate as dominant and records frozen isolation diagnostics; utility results require the gate, whereas the attack grid retains near-tie cells as flagged boundary cases. Its utility comparator is the largest remaining isolated cluster of the dominant rank (the same-rank runner-up by modulus). For a real-valued intervention, the selected cluster must be closed under complex conjugation; the implementation enforces this by grouping a non-real eigenvalue with its numerically matched conjugate. It computes the selected projector from left and right eigenvectors, so the evaluated protocol is restricted to simple, numerically diagonalizable eigenvalues or conjugate pairs; the broader Riesz-projector construction is not claimed to be numerically covered for defective matrices or unresolved modulus ties. We track relative eigengap, nearest modulus-tie gap, projector operator norm, covariance error after pullback, and target-logit intervention discrepancy. Utility holdouts enforce these thresholds for both clusters; near-tie attack cells remain flagged boundary cases rather than passing the gate. This is a retained-data criterion rather than a general collision-handling algorithm; a production implementation near a collision should use a Schur- or resolvent-based projector, enlarge the cluster, or abstain. For a selected projector $P$, intervention utility is measured by the absolute target-logit change between the original endpoint and the endpoint after Eq. 8. This estimand tests whether the chosen invariant subspace carries output effect. It does not assert semantic alignment, human interpretability, unique causal status, or global optimality.

### 3.6 ADVERSARIAL ENDPOINTS AS A SPECTRAL STRESS TEST

For a clean input $x_0$, an attack algorithm $A$, a budget $\varepsilon$, and its perturbed endpoint $x_1^{A,\varepsilon}$, we use the clean-to-perturbed path

$$\gamma_{A,\varepsilon}(t) = x_0 + t \left( x_1^{A,\varepsilon} - x_0 \right). \tag{9}$$

The attack-path conductance matrix is Eq. 1 evaluated on this path, with a fixed scalar target $G_y$ given by the true-class logit. Write $z_0 = H(x_0)$, $z_1^{A,\varepsilon} = H(x_1^{A,\varepsilon})$, and $\Delta z_{A,\varepsilon} = z_1^{A,\varepsilon} - z_0$. For its dominant spectral projector $P_{A,\varepsilon}$, we define the restored target-logit effect

$$R_{A,\varepsilon}(x_0; y) = G_y(z_0 + (I - P_{A,\varepsilon})\Delta z_{A,\varepsilon}) - G_y(z_1^{A,\varepsilon}), \tag{10}$$

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

It is the target-logit change obtained by removing the selected spectral displacement from the attacked endpoint. The primary magnitude estimand is $A_{A,\varepsilon} = |R_{A,\varepsilon}|$; signed $R_{A,\varepsilon}$ is retained as a directional diagnostic.

**Proposition 5** (Attack-path equivariance). *For any fixed endpoint produced by an input-space endpoint generator, including PGD and APGD (Madry et al., 2018; Croce & Hein, 2020), the matrix on Eq. 9 obeys the same similarity law as Eq. 4; hence $P_{A,\varepsilon} \mapsto MP_{A,\varepsilon}M^{-1}$ and $R_{A,\varepsilon}$ is unchanged by the compensated hidden gauge.*

*Proof.* The hidden image of Eq. 9 is an admissible path, so the conductance similarity law applies directly. The displacement transforms as $\Delta\bar{z} = M\Delta z$, and therefore $(I - MPM^{-1})M\Delta z = M(I - P)\Delta z$ before applying the compensated downstream map. □

The endpoint target-logit drop $D_{A,\varepsilon} = G_y(z_0) - G_y(z_1^{A,\varepsilon})$ is reported descriptively. We do not divide by $D_{A,\varepsilon}$ as a primary metric because matched random paths can have a near-zero or sign-changing denominator. For each clean sample and budget, an attack endpoint is paired with a box-feasible magnitude-permutation/sign control from the same clean image: its displacement magnitudes are randomly reassigned subject to image-box feasibility, with feasible signs randomized, preserving the attack endpoint's $\ell_2$ and $\ell_\infty$ scales. This is a structured randomized control, not a uniform draw from the feasible box-constrained shell. The attack-success AUC is computed only within a frozen case-control sample containing equal attack-success and attack-failure strata; it is a conditional separation statistic, not a population attack rate or calibrated vulnerability probability. We report both the AUC of $A_{A,\varepsilon}$ and the signed AUC of $R_{A,\varepsilon}$, because a larger output-relevant magnitude need not have a common direction across architectures or attacks. The attack algorithm selects the endpoint, while the conductance matrix and spectral intervention diagnose its hidden displacement; no attack optimization is performed in representation space. This separation makes the endpoint grid a stress test of the proposed equivariant diagnostic: a positive result would show that the same subspace object used for ordinary intervention also resolves structured attack-generated displacement, while a failure would delimit its scope rather than falsify the gauge theorem.

## 4 EXPERIMENTS

### 4.1 QUESTIONS AND FROZEN PROTOCOL

**Experimental questions.** We organize the experiments around five questions. **Q1:** Does the implementation preserve the network and obey the exact similarity and projector laws? **Q2:** Does conventional hidden-coordinate conductance expose consequential non-identifiability rather than a formal curiosity? **Q3:** Are spectral interventions stable across architectures, datasets, seeds, and conditioned dense gauges? **Q4:** Does the selected invariant subspace carry more target-logit effect than a matched-rank invariant alternative? **Q5:** Across architectures, attack algorithms, and non-saturated budgets, does the magnitude $|R|$ of the dominant restored effect exceed the matched-random endpoint effect while preserving gauge covariance, and is its signed direction consistent?

**Vision matrix.** The balanced matrix uses ResNet-18 (He et al., 2016), WRN-28-2 (Zagoruyko & Komodakis, 2016), and our PlainConvNet architecture control on CIFAR-10 and CIFAR-100 (Krizhevsky, 2009) and SVHN (Netzer et al., 2011). Three independently trained seeds produce 27 architecture–dataset–seed cells and 324 correctly classified input paths. Paths run from a fixed baseline to the input; conductance is evaluated at nonlinear cuts with true-label targets and clean-correct filtering. Each path receives condition-bounded gauges, totaling 2592 trials. Thresholds, model checkpoints, path identities, cluster rules, and seeds are stored in frozen configs.

**Utility holdouts.** The 48-path development utility study fixes the dominant-versus-runner-up comparison. Five subsequent holdouts contain 24 paths each: ResNet-18/CIFAR-10 seed 2027, WRN-28-2/CIFAR-10 seed 2030, PlainConvNet/CIFAR-10 seed 2030, ResNet-18/CIFAR-100 seed 2030, and ResNet-18/SVHN seed 2030. The sampled paths are retained only when both compared projectors satisfy the frozen numerical-isolation policy; all sampled paths and exclusions remain recorded in the artifacts. No threshold or selection rule is fitted after observing those outcomes; the runner-up comparator and spectral-isolation protocol are frozen in advance.

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

Text replication. The text replication uses a two-layer, four-head Transformer (Vaswani et al., 2017) trained from scratch on AG News (Zhang et al., 2015), with a 128-dimensional CLS cut and a nonlinear GELU MLP head (Hendrycks & Gimpel, 2016). Conductance follows a null-token embedding baseline rather than an interpolation of discrete token IDs. A seed-2026 pilot freezes the protocol; seeds 2027–2029 are untouched holdouts under clean text, deterministic word dropout, and deterministic character deletion, yielding the nine cells and 144 paths summarized in Table 4.

Evidence hierarchy. These evidence blocks are deliberately non-substitutable: Q1 and Q3 test exact gauge implementation and numerical equivariance, Q2 realizes the conventional-coordinate negative control, Q4 tests paired target-conditioned utility, and Q5 tests conditional endpoint-magnitude separation. Gauge draws validate covariance but are not independent utility replicates; paths are the experimental units, while training seeds and architecture–dataset or text-environment cells are replication axes.

Table 1: Frozen gauge audit. Spectral residuals test exact identities; coordinate variation is a gauge-sensitive negative control, not a utility score.

[tbl-0.html](tbl-0.html)

### 4.2 Q1: EXACT GAUGE VALIDITY

Table 1 summarizes the implementation audit. The general nonlinear check attains similarity-law, diagonal, and trace errors of \(1.03 \times 10^{-13}\), \(5.33 \times 10^{-14}\), and \(4.62 \times 10^{-14}\); a separate nine-cell holdout preserves logits to \(4.04 \times 10^{-13}\) and complete conductance totals to relative error \(2.54 \times 10^{-14}\). Across the balanced matrix, projector covariance and spectral-score errors remain at 1.16e-11 and 3.6e-06, respectively. These are implementation checks against exact identities, not empirical approximations to the theorem. The direct relocation pilot uses penultimate linear heads for transparent prescribed-diagonal constructions;

separate probes at nonlinear cuts on all three architectures recover full-rank conductance with nontrivial power-trace structure, with worst completeness error  \( 9.74 \times 10^{-3} \) . We treat those probes as a scope check rather than utility evidence; the balanced matrix supplies the nonlinear-cut gauge and projector tests.

Table 2: Representative direct coordinate-credit relocation pilot on CIFAR-10. The targeted bottom-decile coordinate becomes the unique credit winner while logits remain unchanged; mass is the gauged top-coordinate absolute attribution fraction, and effect is the selected top-coordinate ablation change.

[tbl-1.html](tbl-1.html)

### 4.3 Q2: COORDINATE CREDIT CAN BE MADE CONSEQUENTIALLY WRONG

The controllability theorem predicts more than ranking noise; conventional hidden-coordinate conductance is the gauge-sensitive negative control here. Table 2 reports a CIFAR-10 construction in which a bottom-decile coordinate becomes the top coordinate in all three architectures while the maximum logit difference stays below \(2 \times 10^{-13}\), captures more than \(1 - 2.1 \times 10^{-13}\) of absolute attribution mass, and changes the selected top-coordinate ablation effect from \(0.35 \rightarrow 9.44\), \(3.23 \rightarrow 13.16\), and \(0.92 \rightarrow 16.70\) logits for ResNet-18, WRN-28-2, and PlainConvNet. This realizes the theorem's worst case rather than claiming that training dis

Table 3: Disaggregated balanced matrix over three training seeds. Top-change is the seed-wise minimum; range and error are worst cases. Each row contains 36 paths and 288 gauges.

[tbl-2.html](tbl-2.html)

covers arbitrary gauges; independently sampled gauges still give a path-cluster bootstrap lower bound

[OCR table id=tbl-0.html; page=7]
<table><tr><td>Quantity</td><td>Result</td></tr><tr><td>Architectures / datasets / seeds</td><td>3/3/3</td></tr><tr><td>Cells / paths / gauges</td><td>27/324/2592</td></tr><tr><td>Maximum projector residual</td><td>1.16e-11</td></tr><tr><td>Maximum spectral-score residual</td><td>3.6e-06</td></tr><tr><td>Path-cluster bootstrap LB</td><td>98.78%</td></tr><tr><td>Balanced-matrix maximum coordinate range</td><td>22.71 logits</td></tr><tr><td>Relocation success</td><td>3/3 architectures</td></tr><tr><td>Utility / complement wins</td><td>5/5 cells; 72/72 paths</td></tr></table>

[OCR table id=tbl-1.html; page=7]
<table><tr><td>Architecture</td><td>d</td><td>\( \kappa(M) \)</td><td>Logit res.</td><td>Original mass</td><td>Gauged mass</td><td>Effect</td></tr><tr><td>ResNet-18</td><td>512</td><td>115.6</td><td>1.9e-13</td><td>3.67%</td><td>&gt;99.99%</td><td>0.35→9.44</td></tr><tr><td>WRN-28-2</td><td>128</td><td>31.0</td><td>2.8e-14</td><td>24.54%</td><td>&gt;99.99%</td><td>3.23→13.16</td></tr><tr><td>PlainConvNet</td><td>256</td><td>47.4</td><td>9.6e-14</td><td>5.52%</td><td>&gt;99.99%</td><td>0.92→16.70</td></tr></table>

[OCR table id=tbl-2.html; page=7]
<table><tr><td>Architecture</td><td>Data</td><td>Top-change</td><td>Coord. range</td><td>Proj. error</td></tr><tr><td>ResNet-18</td><td>CIFAR-10</td><td>99.0%</td><td>6.20</td><td>2.5e-13</td></tr><tr><td>ResNet-18</td><td>CIFAR-100</td><td>100.0%</td><td>6.76</td><td>1.2e-11</td></tr><tr><td>ResNet-18</td><td>SVHN</td><td>100.0%</td><td>3.71</td><td>2.4e-13</td></tr><tr><td>WRN-28-2</td><td>CIFAR-10</td><td>97.9%</td><td>10.93</td><td>2.9e-13</td></tr><tr><td>WRN-28-2</td><td>CIFAR-100</td><td>97.9%</td><td>21.16</td><td>1.7e-13</td></tr><tr><td>WRN-28-2</td><td>SVHN</td><td>99.0%</td><td>5.64</td><td>1.4e-13</td></tr><tr><td>PlainConvNet</td><td>CIFAR-10</td><td>97.9%</td><td>22.71</td><td>6.3e-13</td></tr><tr><td>PlainConvNet</td><td>CIFAR-100</td><td>99.0%</td><td>21.38</td><td>1.1e-13</td></tr><tr><td>PlainConvNet</td><td>SVHN</td><td>96.9%</td><td>14.92</td><td>8.0e-14</td></tr></table>

## A-page-0008

target PDF page 8

of 98.78% for winner changes and up to 11.08 logits of intervention variation across five holdouts (the representative pilot is in Table 2; the untouched-seed holdout is in Appendix Table 9).

### 4.4 Q3: SPECTRAL INTERVENTIONS SURVIVE BROAD GAUGE VARIATION

Vision matrix. Every one of the 27 balanced vision cells passes the frozen covariance and score criteria across residual, wide-residual, and plain convolutional models on CIFAR-10, CIFAR-100, and SVHN; Table 3 reports the disaggregated seed results rather than a pooled average. The conventional coordinate negative control changes winners broadly while projector covariance remains far below tolerance, and the path-cluster bootstrap—not repeated gauge draws—is the primary uncertainty summary.

![img-3.jpeg](img-3.jpeg)

Figure 4: Frozen utility holdouts across five settings (120 paths). (a) Paired-win fraction of the dominant cluster with 95% Wilson confidence intervals against chance (0.5). (b) Absolute true-class-target effects: circles denote medians, horizontal bars denote interquartile ranges (IQR, 25th–75th percentiles), and numbers show median paired effect ratios. (c) Path-level parity landscape (n = 120); points above the dashed y = x parity line denote dominant-cluster wins (109/120 paths). Next-class control results are reported in the text.

Text modality. The same gauge/intervention rule is applied to a from-scratch two-layer Transformer on AG News: across 9 seed–environment cells and 144 paths, accuracy remains at least 73.60%, conventional coordinate winners change at least 97.92%, projector covariance is at most 1.64e-14, and the dominant cluster wins the paired absolute target-logit comparison against the matched-rank runner-up on every path. On the fresh seed-2029 text holdout it also beats the entire spectral complement on 72 of 72 paths, with median effects 2.21 versus 0.004 logits;

Table 4 reports the seed-level summary and the full environment breakdown is in Appendix Table 16.

Table 4: Seed-level AG News gauge audit in the main text. Acc. is clean accuracy; Coord. is coordinate-winner change; RU win is the dominant-cluster win rate against the matched-rank runner-up.

[tbl-3.html](tbl-3.html)

Numerical stress checks. Conditioning stress with  \( \kappa(M) \leq 100 \)  still changes every coordinate winner while spectral scores remain identical at reported precision; the minimum dominant eigengap is 0.243 and maximum projector norm is 21.75 (Appendix Table 12). Against a finer quadrature reference, the production integral has maximum relative matrix error 1.18e-03 and maximum intervention-effect error 3.99e-03, separating numerical approximation from the exact gauge claims.

Table 5: Complete frozen vision utility summary. LB is the 95% Wilson lower bound; D/RU gives median dominant/runner-up absolute effects for the true-class target; ratio is the median paired effect ratio.

[tbl-4.html](tbl-4.html)

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

[OCR table id=tbl-3.html; page=8]
<table><tr><td>Seed</td><td>Paths</td><td>Acc.</td><td>Coord.</td><td>Proj. err.</td><td>RU win</td></tr><tr><td>2027</td><td>36</td><td>73.70%</td><td>97.9%</td><td>8.8e-15</td><td>100.0%</td></tr><tr><td>2028</td><td>36</td><td>73.60%</td><td>97.9%</td><td>1.6e-14</td><td>100.0%</td></tr><tr><td>2029</td><td>72</td><td>73.85%</td><td>97.9%</td><td>1.5e-14</td><td>100.0%</td></tr></table>

[OCR table id=tbl-4.html; page=8]
<table><tr><td>Setting</td><td>Wins/n</td><td>LB</td><td>D/RU</td><td>Ratio</td></tr><tr><td>RN18/C10/2027</td><td>21/24</td><td>69.0%</td><td>6.74/1.38</td><td>4.07</td></tr><tr><td>WRN/C10/2030</td><td>23/24</td><td>79.8%</td><td>9.53/3.25</td><td>3.37</td></tr><tr><td>Plain/C10/2030</td><td>17/24</td><td>50.8%</td><td>12.64/4.32</td><td>1.85</td></tr><tr><td>RN18/C100/2030</td><td>24/24</td><td>86.2%</td><td>11.26/3.29</td><td>3.35</td></tr><tr><td>RN18/SVHN/2030</td><td>24/24</td><td>86.2%</td><td>6.09/1.45</td><td>4.37</td></tr></table>

## A-page-0009

target PDF page 9

### 4.5 Q4: INVARIANT DOES NOT MEAN VACUOUS

This conditional utility test compares the frozen dominant rule with a rank-matched invariant comparator; conventional coordinate conductance is retained separately as a gauge-sensitive negative control. On 47 of 48 development paths, the dominant cluster wins 87.23% with Wilson lower bound (Brown et al., 2001) 74.83% and median effect ratio 2.92; true-class effects are 6.25 versus 1.86 logits. The next-class control favors the dominant cluster on 70.21%, but the weakest holdout is only 50.00%, so the result is target-conditioned. All five holdouts retain majority wins after the pre-registered isolation gates: 120 of 120 paths remain, and the weakest cell reaches 70.83% wins with Wilson lower bound 50.83% and median ratio 1.85 (Table 5). The corresponding paired-effect landscape is shown in Figure 4.

### 4.6 Q5: ADVERSARIAL ENDPOINTS STRESS-TEST THE EQUIVARIANT DIAGNOSTIC

Q5 applies the same dominant spectral rule used in Q4 to attack-generated endpoints, then compares them with box-feasible magnitude-permutation/sign endpoint controls under a frozen case-control protocol. Table 6 reports the core cell-level results. Its primary endpoint estimand is within-cell separation of the absolute restored effect \( |R| \), not attack-success rate or calibrated robustness. The grid uses the frozen 129-point path discretization, so its covariance checks apply to that discretized estimator; the finer

Table 6: Core adversarial endpoint grid.  \( AUC_{|R|} \)  separates attack-success from attack-failure strata using the absolute restored effect; A/R gives median  \( |R| \)  for attack and matched-random endpoints; signed AUC is a secondary directional diagnostic; gap is the minimum dominant modulus gap in the cell.

[tbl-5.html](tbl-5.html)

quadrature audit in Q3 is a separate clean-to-input audit. The grid covers 12 architecture–attack-budget cells and 576 endpoint paths; all cells pass implementation checks, norm matching is within 7.6e-06 / 3.6e-07, and spectral isolation passes 10 cells, with 2 near-modulus ties retained. Attack median  \( |R| \)  exceeds matched random in 12/12 cells,  \( AUC_{|R|} \)  is above chance in 9 cells, and the paired bootstrap lower bound is positive in 9 cells. This supports a conditional magnitude stress-test claim, not a universal attack mechanism: signed AUC is above chance in 7 cells and signed paired difference is positive in 7 cells, so magnitude does not imply one common direction. The complete cell-level bootstrap intervals, signed effects, and near-tie diagnostics are in Appendix Table 13.

## 5 CONCLUSION

Taken together, these results delimit what internal attribution can support under the hidden-basis gauge. Coordinate conductance is a useful parameterization-relative negative control, but cannot support function-level claims about neuron identity, ordering, sign, or sparsity: completeness preserves only the trace and the full coordinate orbit remains attainable. A spectral projector supports a narrower claim: its intervention commutes with the gauge and, under the frozen selection rule, carries more target-logit effect than the matched-rank comparator across the retained vision and text holdouts.

For practice, coordinate scores should be treated as parameterization-relative diagnostics unless the basis is externally privileged or explicitly gauge-fixed. When it is not, the paper's replacement is to report the selected equivariant subspace together with its separation diagnostics and a paired intervention effect; this makes the intervention claim well-defined on the gauge orbit without turning the subspace into a semantic oracle. The empirical scope is conditional: the adversarial grid is a stress test of the same diagnostic, not a robustness benchmark. Its results support a bounded attack-path diagnostic, with mixed directional effects and reduced reliability near spectral ties; they do not establish a universal mechanism, semantic interpretation, causal claim, or robustness predictor.

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

[OCR table id=tbl-5.html; page=9]
<table><tr><td>Architecture</td><td>Attack</td><td>\( \varepsilon \)</td><td>\( AUC_{|R|} \)</td><td>A/R \( |R| \)</td><td>\( \Delta |R| \)</td><td>\( AUC_R \)</td><td>Gap</td></tr><tr><td>ResNet-18</td><td>PGD-40</td><td>1/255</td><td>0.500</td><td>0.02/0.01</td><td>0.015</td><td>0.535</td><td>2.9e-03</td></tr><tr><td>ResNet-18</td><td>PGD-40</td><td>2/255</td><td>0.681</td><td>0.04/0.02</td><td>0.016</td><td>0.660</td><td>1.3e-03</td></tr><tr><td>ResNet-18</td><td>APGD-CE</td><td>1/255</td><td>0.556</td><td>0.02/0.02</td><td>0.012</td><td>0.528</td><td>3.4e-04</td></tr><tr><td>ResNet-18</td><td>APGD-CE</td><td>2/255</td><td>0.590</td><td>0.02/0.01</td><td>0.019</td><td>0.576</td><td>1.4e-02</td></tr><tr><td>WRN-28-2</td><td>PGD-40</td><td>1/255</td><td>0.674</td><td>0.04/0.02</td><td>0.013</td><td>0.403</td><td>6.5e-03</td></tr><tr><td>WRN-28-2</td><td>PGD-40</td><td>2/255</td><td>0.451</td><td>0.05/0.03</td><td>0.025</td><td>0.340</td><td>2.0e-03</td></tr><tr><td>WRN-28-2</td><td>APGD-CE</td><td>1/255</td><td>0.792</td><td>0.04/0.02</td><td>0.016</td><td>0.514</td><td>4.8e-04</td></tr><tr><td>WRN-28-2</td><td>APGD-CE</td><td>2/255</td><td>0.861</td><td>0.02/0.02</td><td>0.003</td><td>0.500</td><td>9.2e-03</td></tr><tr><td>PlainConvNet</td><td>PGD-40</td><td>1/255</td><td>0.500</td><td>0.11/0.04</td><td>0.079</td><td>0.583</td><td>1.3e-02</td></tr><tr><td>PlainConvNet</td><td>PGD-40</td><td>2/255</td><td>0.576</td><td>0.18/0.08</td><td>0.095</td><td>0.583</td><td>5.1e-03</td></tr><tr><td>PlainConvNet</td><td>APGD-CE</td><td>1/255</td><td>0.694</td><td>0.10/0.04</td><td>0.064</td><td>0.396</td><td>4.0e-03</td></tr><tr><td>PlainConvNet</td><td>APGD-CE</td><td>2/255</td><td>0.882</td><td>0.16/0.08</td><td>0.050</td><td>0.333</td><td>3.4e-03</td></tr></table>

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

Generative AI tools were used only in an auxiliary capacity for limited drafting and language editing, manuscript organization and formatting, reproducibility documentation, consistency checks of reported artifacts, and editing implementation scripts and scientific figures. They were not used to generate data, formulate the central mathematical claims, develop or prove the theory, design the experiments, or determine the interpretation and conclusions. All AI-assisted text, code, and figure changes were reviewed, tested, and revised by the authors, who take full responsibility for the final manuscript, claims, and artifacts.

## REPRODUCIBILITY STATEMENT

The assumptions and complete proofs for the gauge and projector results are given in the Methodology and Appendix. The experimental sections specify the models, datasets and preprocessing, baselines, path and intervention definitions, selection rules, thresholds, random seeds, and evaluation metrics; supplementary materials and code include the implementation and analysis scripts, frozen configurations, and input indices needed to reproduce the reported analyses.

## REFERENCES

Julius Adebayo, Justin Gilmer, Michael Muelly, Ian Goodfellow, Moritz Hardt, and Been Kim. Sanity checks for saliency maps. In Advances in Neural Information Processing Systems, volume 31, 2018.

Samuel K. Ainsworth, Jonathan Hayase, and Siddhartha Srinivasa. Git Re-Basin: Merging models modulo permutation symmetries. In International Conference on Learning Representations, 2023.

Marco Ancona, Enea Ceolini, Cengiz Öztireli, and Markus Gross. Towards better understanding of gradient-based attribution methods for deep neural networks. In International Conference on Learning Representations, 2018.

Sebastian Bach, Alexander Binder, Grégoire Montavon, Frederick Klauschen, Klaus-Robert Müller, and Wojciech Samek. On pixel-wise explanations for non-linear classifier decisions by layer-wise relevance propagation. PLoS ONE, 10(7):e0130140, 2015.

David Bau, Bolei Zhou, Aditya Khosla, Aude Oliva, and Antonio Torralba. Network dissection: Quantifying interpretability of deep visual representations. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 6541–6549, 2017.

David Bau, Jun-Yan Zhu, Hendrik Strobelt, Agata Lapedriza, Bolei Zhou, and Antonio Torralba. Understanding the role of individual units in a deep neural network. Proceedings of the National Academy of Sciences, 117(48):30071–30078, 2020.

Lawrence D. Brown, T. Tony Cai, and Anirban DasGupta. Interval estimation for a binomial proportion. Statistical Science, 16(2):101–133, 2001. doi: 10.1214/ss/1009213286.

Francesco Croce and Matthias Hein. Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks. In Proceedings of the 37th International Conference on Machine Learning, pp. 2206–2216, 2020.

Kedar Dhamdhere, Mukund Sundararajan, and Qiqi Yan. How important is a neuron? arXiv preprint arXiv:1805.12233, 2018.

Frances Ding, Jean-Stanislas Denain, and Jacob Steinhardt. Grounding representation similarity through statistical testing. Advances in neural information processing systems, 34:1556–1568, 2021.

Joakim Edin, Andreas Geert Motzfeldt, Casper L. Christensen, Tuukka Ruotsalo, Lars Maaløe, and Maria Maistro. Normalized AOPC: Fixing misleading faithfulness metrics for feature attributions explainability. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 1715–1730. Association for Computational Linguistics, 2025. doi: 10.18653/v1/2025.acl-long.86.

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

Nelson Elhage, Tristan Hume, Catherine Olsson, Nicholas Schiefer, Tom Henighan, Shauna Kravec, Zac Hatfield-Dodds, Robert Lasenby, Dawn Drain, Carol Chen, et al. Toy models of superposition. arXiv preprint arXiv:2209.10652, 2022.

Rahim Entezari, Hanie Sedghi, Olga Saukh, and Behnam Neyshabur. The role of permutation invariance in linear mode connectivity of neural networks. In International Conference on Learning Representations, 2022.

Peter A. Fillmore. On similarity and the diagonal of a matrix. The American Mathematical Monthly, 76(2):167–169, 1969. doi: 10.1080/00029890.1969.12000162.

Atticus Geiger, Hanson Lu, Thomas Icard, and Christopher Potts. Causal abstractions of neural networks. Advances in neural information processing systems, 34:9574–9586, 2021.

Amirata Ghorbani, James Wexler, James Y Zou, and Been Kim. Towards automatic concept-based explanations. Advances in neural information processing systems, 32, 2019.

Charles Godfrey, Davis Brown, Tegan Emerson, and Henry Kvinge. On the symmetries of deep learning models and their internal representations. In Advances in Neural Information Processing Systems, volume 35, pp. 11893–11905, 2022.

Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 770–778, 2016.

Dan Hendrycks and Kevin Gimpel. Gaussian error linear units (GELUs). arXiv preprint arXiv:1606.08415, 2016.

Sara Hooker, Dumitru Erhan, Pieter-Jan Kindermans, and Been Kim. A benchmark for interpretability methods in deep neural networks. Advances in neural information processing systems, 32, 2019.

Robert Huben, Hoagy Cunningham, Logan Smith, Aidan Ewart, and Lee Sharkey. Sparse autoencoders find highly interpretable features in language models. In International Conference on Learning Representations, volume 2024, pp. 7827–7845, 2024.

Tosio Kato. Perturbation Theory for Linear Operators, volume 132. Springer, 1995.

Been Kim, Martin Wattenberg, Justin Gilmer, Carrie Cai, James Wexler, Fernanda Viegas, et al. Interpretability beyond feature attribution: Quantitative testing with concept activation vectors (tcav). In International conference on machine learning, pp. 2668–2677. PMLR, 2018.

Pieter-Jan Kindermans, Sara Hooker, Julius Adebayo, Maximilian Alber, Kristof T. Schütt, Sven Dähne, Dumitru Erhan, and Been Kim. The (un)reliability of saliency methods. In Explainable AI: Interpreting, Explaining and Visualizing Deep Learning, pp. 267–280. Springer, 2019.

Pang Wei Koh, Thao Nguyen, Yew Siang Tang, Stephen Mussmann, Emma Pierson, Been Kim, and Percy Liang. Concept bottleneck models. In International conference on machine learning, pp. 5338–5348. PMLR, 2020.

Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. Similarity of neural network representations revisited. In International conference on machine learning, pp. 3519–3529. PMLR, 2019.

Alex Krizhevsky. Learning multiple layers of features from tiny images. Technical report, University of Toronto, 2009.

Zaitang Li, Pin-Yu Chen, and Tsung-Yi Ho. GREAT Score: Global robustness evaluation of adversarial perturbation using generative models. In Advances in Neural Information Processing Systems, volume 37, pp. 39158–39189, 2024.

Scott M Lundberg and Su-In Lee. A unified approach to interpreting model predictions. Advances in neural information processing systems, 30, 2017.

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

Daniel D Lundstrom, Tianjian Huang, and Meisam Razaviyayn. A rigorous study of integrated gradients method and extensions to internal neuron attributions. In International Conference on Machine Learning, pp. 14485–14508. PMLR, 2022.

Aleksander Madry, Aleksandar Makelov, Ludwig Schmidt, Dimitris Tsipras, and Adrian Vladu. Towards deep learning models resistant to adversarial attacks. In International Conference on Learning Representations, 2018.

Kevin Meng, David Bau, Alex Andonian, and Yonatan Belinkov. Locating and editing factual associations in GPT. In Advances in Neural Information Processing Systems, volume 35, pp. 17359–17372, 2022.

Ari S. Morcos, Maithra Raghu, and Samy Bengio. Insights on representational similarity in neural networks with canonical correlation. In Advances in Neural Information Processing Systems, volume 31, 2018.

Yuval Netzer, Tao Wang, Adam Coates, Alessandro Bissacco, Bo Wu, and Andrew Y. Ng. Reading digits in natural images with unsupervised feature learning. In NIPS Workshop on Deep Learning and Unsupervised Feature Learning, 2011.

Chris Olah, Alexander Mordvintsev, and Ludwig Schubert. Feature visualization. Distill, 2(11):e7, 2017.

Judea Pearl. Causality: Models, Reasoning, and Inference. Cambridge University Press, 2 edition, 2009.

Maithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein. SVCCA: Singular vector canonical correlation analysis for deep learning dynamics and interpretability. In Advances in Neural Information Processing Systems, volume 30, 2017.

Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. Why should I trust you? explaining the predictions of any classifier. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 1135–1144, 2016.

Geoffrey Roeder, Luke Metz, and Durk Kingma. On linear identifiability of learned representations. In International Conference on Machine Learning, pp. 9030–9039. PMLR, 2021.

Ramprasaath R. Selvaraju, Michael Cogswell, Abhishek Das, Ramakrishna Vedantam, Devi Parikh, and Dhruv Batra. Grad-CAM: Visual explanations from deep networks via gradient-based localization. In Proceedings of the IEEE International Conference on Computer Vision, pp. 618–626, 2017.

Avanti Shrikumar, Peyton Greenside, and Anshul Kundaje. Learning important features through propagating activation differences. In International conference on machine learning, pp. 3145–3153. PMLR, 2017.

Daniel Smilkov, Nikhil Thorat, Been Kim, Fernanda Viégas, and Martin Wattenberg. Smoothgrad: removing noise by adding noise. arXiv preprint arXiv:1706.03825, 2017.

Chandler Squires. A unifying framework for unsupervised concept extraction. In Proceedings of the 29th International Conference on Artificial Intelligence and Statistics, volume 300 of Proceedings of Machine Learning Research, pp. 4393–4401. PMLR, 2026.

G. W. Stewart and Ji-guang Sun. Matrix Perturbation Theory. Academic Press, 1990.

Mukund Sundararajan and Amir Najmi. The many shapley values for model explanation. In International conference on machine learning, pp. 9269–9278. PMLR, 2020.

Mukund Sundararajan, Ankur Taly, and Qiqi Yan. Axiomatic attribution for deep networks. In Proceedings of the 34th International Conference on Machine Learning, pp. 3319–3328, 2017.

Lloyd N Trefethen. Spectra and pseudospectra: The behaviour of non-normal matrices and operators. In The graduate student's guide to numerical analysis' 98: Lecture notes from the VIII EPSRC Summer School in Numerical Analysis, pp. 217–250. Springer, 2005.

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

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In Advances in Neural Information Processing Systems, volume 30, 2017.

Jesse Vig, Sebastian Gehrmann, Yonatan Belinkov, Sharon Qian, Daniel Nevo, Yaron Singer, and Stuart Shieber. Investigating gender bias in language models using causal mediation analysis. In Advances in Neural Information Processing Systems, volume 33, pp. 12388–12401, 2020.

Alex H. Williams, Erin Kunz, Simon Kornblith, and Scott Linderman. Generalized shape metrics on neural representations. In Advances in Neural Information Processing Systems, volume 34, pp. 4738–4750, 2021.

Shawn Xu, Subhashini Venugopalan, and Mukund Sundararajan. Attribution in scale and space. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 9680–9689, 2020.

Chhavi Yadav, Ruihan Wu, and Kamalika Chaudhuri. Influence attributions can be systematically altered by model manipulation. In Proceedings of the 29th International Conference on Artificial Intelligence and Statistics, volume 300 of Proceedings of Machine Learning Research, pp. 1396–1404. PMLR, 2026.

Chih-Kuan Yeh, Cheng-Yu Hsieh, Arun Suggala, David I Inouye, and Pradeep K Ravikumar. On the (in) fidelity and sensitivity of explanations. Advances in neural information processing systems, 32, 2019.

Sergey Zagoruyko and Nikos Komodakis. Wide residual networks. In British Machine Vision Conference, 2016.

Xiang Zhang, Junbo Zhao, and Yann LeCun. Character-level convolutional networks for text classification. In Advances in Neural Information Processing Systems, volume 28, pp. 649–657, 2015.

## A-page-0014

target PDF page 14

# A APPENDIX

# A.1 NOTATION AND TERMINOLOGY

[tbl-6.html](tbl-6.html)

Table 7: Notation and terminology used throughout the paper.

# A.2 ADDITIONAL THEORY AND SCOPE

# A.2.1 ASSUMPTIONS AND ARCHITECTURAL SCOPE

The hidden space is finite-dimensional and real, z(t) ∈ R^d; the target G is scalar and locally Lipschitz on a neighborhood of the hidden path, differentiable along the path almost everywhere with the standard a.e. chain rule; z is absolutely continuous (piecewise C^1 is sufficient); and the entries of z(t)∇G(z(t))^T are integrable. For the evaluated ReLU paths, the path composition is absolutely continuous and piecewise smooth, and the conductance integrand uses a specified almost-everywhere gradient representative. The gauge matrix M ∈ GL(d, R) is constant along the path. These assumptions are sufficient for the a.e. chain rule, the matrix integral, and the similarity action used above; C^1 smoothness remains a sufficient special case. A vector output must first be reduced to a fixed scalar logit, margin, or loss.

Equation 3 may be implemented by inserting an affine map and its inverse around a cut. It need not be absorbable into the original layer types. When the adjacent layers are affine, it can instead be absorbed into their parameters. The theorem concerns equality of the represented function, not membership of the transformed parameters in a narrower architectural parameterization.

# A.2.2 TRANSLATIONS, TARGETS, AND PATHS

Translation does not enter C because z̃ = Mẑ. The inverse translation in G̃ restores z before differentiation, so the full affine gauge has the same matrix action as its linear part. The input path itself need not be linear; only piecewise continuous differentiability is required. For vector outputs, fixing a scalar target before constructing C is essential because different logits, margins, or losses generally induce different similarity orbits.

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

[OCR table id=tbl-6.html; page=14]
<table><tr><th>Symbol / term</th><th>Meaning</th></tr><tr><td>F</td><td>Scalar network output factor at the hidden cut, with F = G ∘ H.</td></tr><tr><td>H</td><td>Hidden representation map H : X → R^d from the input space.</td></tr><tr><td>G</td><td>Scalar downstream map that turns the hidden state into the selected target output.</td></tr><tr><td>C^1</td><td>Continuously differentiable; a sufficient regularity condition for the conductance theorem.</td></tr><tr><td>Locally Lipschitz</td><td>Weaker regularity of G used in the theorem, together with the standard chain rule almost everywhere along the path.</td></tr><tr><td>Absolutely continuous</td><td>Regularity of z(t) that permits an almost-everywhere derivative and the matrix path integral.</td></tr><tr><td>γ</td><td>Input path γ : [0, 1] → X used for path integration; t is its path parameter.</td></tr><tr><td>z(t)</td><td>Hidden trajectory, defined by z(t) = H(γ(t)) in a d-dimensional hidden space.</td></tr><tr><td>Δz</td><td>Endpoint displacement in hidden space, z(1) - z(0).</td></tr><tr><td>C</td><td>Path-integrated conductance matrix ∫ z(t)∇G(z(t))^T dt; i, j index its hidden coordinates.</td></tr><tr><td>C_{ij}</td><td>(i, j) entry of C; off-diagonal entries retain cross-coordinate transport discarded by coordinate scores.</td></tr><tr><td>diag(C)</td><td>Vector of diagonal entries of C, i.e., the coordinate conductance scores.</td></tr><tr><td>Cond_i</td><td>Conventional conductance of coordinate i, defined as Cond_i = C_{ij}.</td></tr><tr><td>tr(C)</td><td>Sum of coordinate conductances; completeness identifies it with the selected output difference.</td></tr><tr><td>M</td><td>Invertible linear change of hidden coordinates in the compensated affine gauge.</td></tr><tr><td>c</td><td>Constant hidden translation paired with M; it does not affect C because differentiation removes it.</td></tr><tr><td>GL(d)</td><td>Group of invertible real d × d matrices allowed for M.</td></tr><tr><td>γ</td><td>Transformed quantity under the compensated hidden-coordinate gauge, e.g., C̃ = MCM^{-1}.</td></tr><tr><td>a</td><td>Prescribed diagonal vector in the controllability theorem.</td></tr><tr><td>1</td><td>All-ones vector in 1^T a = tr(C).</td></tr><tr><td>Λ</td><td>Selected isolated cluster of eigenvalues of C.</td></tr><tr><td>Γ</td><td>Contour in the complex plane enclosing Λ and no other eigenvalues.</td></tr><tr><td>P_Λ(C)</td><td>Riesz projector onto the generalized eigenspace associated with the isolated cluster Λ.</td></tr><tr><td>P</td><td>Shorthand for the selected projector P_Λ(C) in the intervention definition.</td></tr><tr><td>I</td><td>Identity matrix of the hidden-space dimension.</td></tr><tr><td>S_Γ</td><td>Invariant spectral subspace im P_Λ(C) selected by Γ.</td></tr><tr><td>I_P(Δz)</td><td>Projector intervention (I - P)Δz, which removes the selected spectral component; ||P||_2 is monitored for oblique-projector sensitivity.</td></tr><tr><td>x_1^{A,ε}</td><td>Endpoint from generator A (such as PGD/APGD) at budget ε, starting from clean input x_0; κ(M) is the gauge condition number.</td></tr><tr><td>R_{A,ε}</td><td>Signed restored target-logit effect of the dominant spectral intervention.</td></tr><tr><td>A_{A,ε}</td><td>Absolute magnitude estimand, defined by A_{A,ε} = |R_{A,ε}|.</td></tr><tr><td>Gauge</td><td>Function-preserving affine change of hidden coordinates, possibly implemented at an inserted cut.</td></tr><tr><td>Invariant</td><td>A scalar or matrix property unchanged by the hidden-coordinate gauge.</td></tr><tr><td>Equivariant</td><td>An object that transforms covariantly, such as P → MPM^{-1}, so its abstract meaning is preserved.</td></tr><tr><td>Estimand</td><td>A quantity specified in advance as the target of an analysis, rather than a post hoc summary.</td></tr></table>

## A-page-0015

target PDF page 15

### A.2.3 REAL PRESCRIBED DIAGONALS AND THE LINEAR-HEAD BOUNDARY

The controllability theorem is used over the real field: for real nonscalar $C$ and real $a$ with $\mathbf{1}^{\top}a = \operatorname{tr}(C)$, the similarity matrix can be chosen in $GL(d, \mathbb{R})$ (Fillmore, 1969). Complex eigenvalues enter only the spectral construction, where conjugate pairs are grouped to retain a real invariant subspace. They are not needed for prescribing the conductance diagonal.

For a linear downstream head $G(z) = w^{\top}z + b$,

$$C = \Delta z \, w^{\top}, \qquad \operatorname{rank}(C) \le 1, \qquad \operatorname{tr}(C) = w^{\top} \Delta z. \tag{11}$$

If this matrix is nonscalar, Fillmore's theorem still realizes every real diagonal with the required sum. Thus a zero output difference permits any zero-sum coordinate-credit vector, including nonzero positive and negative entries. The only fixed case is $C = \lambda I$; for rank-one $C$ and $d > 1$, this reduces to $C = 0$. The targeted relocation experiments use this transparent rank-one boundary, while the nonlinear probes verify that the general matrix law is not confined to it.

### A.2.4 SPECTRAL CLUSTERS VERSUS EIGENVECTORS

An eigenvector is scale ambiguous, may be complex, and is unstable or undefined as an individual object at repeated eigenvalues. A Riesz projector identifies the entire generalized eigenspace associated with an isolated cluster and is defined by the resolvent even for defective matrices. The numerical experiments use the simpler left/right-eigenvector formula for simple eigenvalues and conjugate pairs, so defective matrices and unresolved modulus ties remain outside the evaluated implementation. If a desired cluster collides with its complement, no continuous rule can preserve the original separation; a robust extension should merge clusters or abstain rather than select an unstable individual eigenvector.

### A.2.5 INVARIANT SCALARS VERSUS EQUIVARIANT INTERVENTIONS

Traces of powers, determinant, and characteristic-polynomial coefficients are similarity invariants. They summarize an orbit but do not specify where to intervene. A projector is equivariant rather than invariant: its matrix changes as $P \mapsto MPM^{-1}$, while its image denotes the same abstract subspace. This covariance is what makes Eq. 8 operational.

### A.2.6 ENDPOINT COMMUTATION

Let $z_1 = z(1)$, $z_0 = z(0)$, and $z_1^{(-P)} = z_0 + (I - P)(z_1 - z_0)$. In the transformed coordinates, $\widetilde{z}_j = M z_j + c$, $\widetilde{\Delta} z = M \Delta z$, and $\widetilde{P} = MPM^{-1}$. Therefore

$$\widetilde{z}_1^{(-\widetilde{P})} = \widetilde{z}_0 + (I - \widetilde{P}) \widetilde{\Delta} z \tag{12}$$

$$= M \{ z_0 + (I - P) \Delta z \} + c = M z_1^{(-P)} + c. \tag{13}$$

Pullback by $M^{-1}(\cdot - c)$ returns exactly $z_1^{(-P)}$, so the compensated downstream maps produce identical outputs. This proves endpoint equality, not only covariance of a matrix score.

### A.2.7 CLUSTER COLLISIONS AND NON-NORMAL CONDITIONING

The evaluated scripts sort simple eigenvalue or conjugate-pair clusters by modulus and require the aggregate minimum relative separation to exceed the frozen threshold $10^{-3}$. They do not dynamically merge all modulus ties or return per-path abstentions; no evaluated path falls below the retained-data threshold. The broader collision-handling rule remains a methodological extension rather than an executed part of this study.

For non-normal $C$, eigengap alone does not control sensitivity. The resolvent may be large far from the spectrum, and the oblique Riesz projector can have $\|P\|_2 \gg 1$ (Kato, 1995; Trefethen, 2005; Stewart & Sun, 1990). We therefore monitor both relative separation and $\|P\|_2$, together with a direct pullback covariance residual. The selected subspace varies continuously only while the contour remains in the resolvent set; no method can continuously preserve the same split through a cluster collision.

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

### A.3 COMPLETE EXPERIMENTAL RESULTS

#### A.3.1 NUMERICAL THEOREM IDENTITIES

Table 8 reports every residual in the general nonlinear theorem check. These are implementation tests against exact identities, not sampling-based estimates.

Table 8: General conductance-similarity implementation checks.

[tbl-7.html](tbl-7.html)

#### A.3.2 TARGETED COORDINATE-CREDIT RELOCATION

The pilot deliberately selects an originally bottom-decile coordinate and prescribes it as the unique credit winner. The representative three-architecture pilot is reported in Table 2 in the main text. Table 9 repeats direct prescription on two untouched seeds in each architecture–dataset cell.

Table 9: Complete untouched-seed direct-prescription holdout. Logit, attribution, and total residuals are reported separately for every seed; mass is the gauged top-coordinate absolute attribution fraction.

[tbl-8.html](tbl-8.html)

#### A.3.3 NONLINEAR CONDUCTANCE MATRICES

Table 10 separates the exact synthetic similarity check from quadrature-based trained-network probes. Every path has rank above one and a nontrivial spectrum. The trained rows report completeness error, whereas the synthetic row reports the maximum invariant residual.

#### A.3.4 BALANCED MATRIX AND CONDITIONING

Figure 5 visualizes the nine architecture–dataset aggregates without pooling away weak cells; Table 3 gives their values. Table 11 exposes all 27 independently trained seed cells underlying that summary. Each row aggregates exactly 12 paths; all 324 path rows and 2,592 gauge trials remain in the named JSON source artifacts. The complete condition-number-100 path-level stress rows are reported in Appendix Table 12, alongside Figure 6 and the protocol details.

[OCR table id=tbl-7.html; page=16]
<table><tr><td>Identity</td><td>Maximum residual</td><td>Tolerance</td></tr><tr><td>Similarity law</td><td>1.03e-13</td><td>1.0e-10</td></tr><tr><td>Conductance diagonal</td><td>5.33e-14</td><td>1.0e-10</td></tr><tr><td>Completeness / trace</td><td>4.62e-14</td><td>1.0e-10</td></tr><tr><td>Normalized power traces</td><td>8.13e-14</td><td>1.0e-10</td></tr></table>

[OCR table id=tbl-8.html; page=16]
<table><tr><td>Architecture</td><td>Dataset</td><td>Seed</td><td>\( \kappa (M) \)</td><td>Logit res.</td><td>Attr. res.</td><td>Gauged mass</td><td>Total res.</td></tr><tr><td>ResNet-18</td><td>CIFAR-10</td><td>2029</td><td>114.2</td><td>4.0e-13</td><td>2.3e-13</td><td>&gt;99.99%</td><td>2.5e-14</td></tr><tr><td>ResNet-18</td><td>CIFAR-10</td><td>2030</td><td>115.2</td><td>2.1e-14</td><td>1.4e-14</td><td>&gt;99.99%</td><td>1.1e-15</td></tr><tr><td>WRN-28-2</td><td>CIFAR-10</td><td>2029</td><td>30.3</td><td>2.3e-14</td><td>2.0e-14</td><td>&gt;99.99%</td><td>4.0e-16</td></tr><tr><td>WRN-28-2</td><td>CIFAR-10</td><td>2030</td><td>30.0</td><td>3.3e-14</td><td>1.1e-14</td><td>&gt;99.99%</td><td>6.6e-16</td></tr><tr><td>PlainConvNet</td><td>CIFAR-10</td><td>2029</td><td>48.6</td><td>4.3e-14</td><td>5.7e-15</td><td>&gt;99.99%</td><td>2.2e-16</td></tr><tr><td>PlainConvNet</td><td>CIFAR-10</td><td>2030</td><td>47.3</td><td>9.2e-14</td><td>1.4e-14</td><td>&gt;99.99%</td><td>2.2e-16</td></tr><tr><td>ResNet-18</td><td>CIFAR-100</td><td>2029</td><td>54.8</td><td>3.1e-14</td><td>7.5e-15</td><td>&gt;99.99%</td><td>5.8e-16</td></tr><tr><td>ResNet-18</td><td>CIFAR-100</td><td>2030</td><td>59.3</td><td>2.1e-14</td><td>7.1e-15</td><td>&gt;99.99%</td><td>3.4e-16</td></tr><tr><td>WRN-28-2</td><td>CIFAR-100</td><td>2029</td><td>21.3</td><td>4.6e-14</td><td>1.8e-14</td><td>&gt;99.99%</td><td>1.2e-15</td></tr><tr><td>WRN-28-2</td><td>CIFAR-100</td><td>2030</td><td>25.5</td><td>3.2e-14</td><td>2.1e-14</td><td>&gt;99.99%</td><td>8.7e-16</td></tr><tr><td>PlainConvNet</td><td>CIFAR-100</td><td>2029</td><td>33.0</td><td>5.0e-14</td><td>1.1e-14</td><td>&gt;99.99%</td><td>6.3e-16</td></tr><tr><td>PlainConvNet</td><td>CIFAR-100</td><td>2030</td><td>42.1</td><td>5.7e-14</td><td>4.6e-15</td><td>&gt;99.99%</td><td>1.4e-16</td></tr><tr><td>ResNet-18</td><td>SVHN</td><td>2029</td><td>102.9</td><td>1.4e-14</td><td>7.1e-15</td><td>&gt;99.99%</td><td>9.4e-16</td></tr><tr><td>ResNet-18</td><td>SVHN</td><td>2030</td><td>109.1</td><td>1.4e-14</td><td>6.5e-15</td><td>&gt;99.99%</td><td>6.0e-16</td></tr><tr><td>WRN-28-2</td><td>SVHN</td><td>2029</td><td>32.9</td><td>2.1e-14</td><td>7.1e-15</td><td>&gt;99.99%</td><td>9.1e-16</td></tr><tr><td>WRN-28-2</td><td>SVHN</td><td>2030</td><td>34.0</td><td>2.3e-14</td><td>8.9e-15</td><td>&gt;99.99%</td><td>1.1e-15</td></tr><tr><td>PlainConvNet</td><td>SVHN</td><td>2029</td><td>59.1</td><td>4.3e-14</td><td>1.5e-14</td><td>&gt;99.99%</td><td>6.8e-16</td></tr><tr><td>PlainConvNet</td><td>SVHN</td><td>2030</td><td>59.4</td><td>5.0e-14</td><td>1.8e-14</td><td>&gt;99.99%</td><td>1.4e-15</td></tr></table>

## A-page-0017

target PDF page 17

Table 10: Nonlinear-cut matrix structure across synthetic and trained paths.

[tbl-9.html](tbl-9.html)

Table 11: Complete seed-level visual gauge matrix. Each cell has 12 paths and 96 dense-gauge trials. Change is the trial-level coordinate-winner change rate; range and residual are path maxima; gap is the minimum dominant relative eigengap and  \( \|P\| \)  the maximum projector norm.

[tbl-10.html](tbl-10.html)

#### A.3.5 CORE ADVERSARIAL ENDPOINT GRID

The core grid evaluates the frozen CIFAR-10 seed-2026 checkpoints with PGD-40 and APGD-CE at 1/255 and 2/255. Each cell selects 12 clean-correct attack successes and 12 clean-correct attack failures, then pairs every attack endpoint with the scale-matched randomized displacement from the same clean image. The labels define a conditional case-control analysis; they do not estimate the dataset-level attack success rate.

The artifact status is FALSIFIED because the frozen all-cell spectral-isolation gate is falsified, while the implementation status is PASS: every cell meets the path-count, matched-norm, projector-covariance, and pulled-back intervention-score criteria. The isolation gate passes 10 of 12 cells; the remaining cells are retained to expose the near-tie boundary. The absolute-effect bootstrap intervals resample endpoint observations within the balanced attack-success and attack-failure strata, and paired intervals resample clean-image pairs. They do not treat the four gauge trials per path as independent evidence.

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

[OCR table id=tbl-9.html; page=17]
<table><tr><td>Setting</td><td>Paths</td><td>Rank range</td><td>Nontrivial spectrum</td><td>Max. residual</td></tr><tr><td>Synthetic nonlinear</td><td>24</td><td>2</td><td>100%</td><td>3.2e-14</td></tr><tr><td>ResNet-18</td><td>8</td><td>256–256</td><td>100%</td><td>8.05e-03</td></tr><tr><td>WRN-28-2</td><td>8</td><td>64–64</td><td>100%</td><td>9.74e-03</td></tr><tr><td>PlainConvNet</td><td>8</td><td>127–128</td><td>100%</td><td>2.44e-03</td></tr></table>

[OCR table id=tbl-10.html; page=17]
<table><tr><td>Architecture</td><td>Dataset</td><td>Seed</td><td>Paths</td><td>Change</td><td>Range</td><td>Proj. residual</td><td>Min. gap</td><td>Max. \( \| P\| \)</td></tr><tr><td>ResNet-18</td><td>CIFAR-10</td><td>2027</td><td>12</td><td>100.0%</td><td>4.45</td><td>1.9e-14</td><td>0.488</td><td>7.41</td></tr><tr><td>ResNet-18</td><td>CIFAR-10</td><td>2028</td><td>12</td><td>99.0%</td><td>1.89</td><td>1.4e-14</td><td>0.628</td><td>6.98</td></tr><tr><td>ResNet-18</td><td>CIFAR-10</td><td>2030</td><td>12</td><td>100.0%</td><td>6.20</td><td>2.5e-13</td><td>0.243</td><td>21.75</td></tr><tr><td>ResNet-18</td><td>CIFAR-100</td><td>2027</td><td>12</td><td>100.0%</td><td>4.90</td><td>1.2e-11</td><td>0.070</td><td>64.47</td></tr><tr><td>ResNet-18</td><td>CIFAR-100</td><td>2028</td><td>12</td><td>100.0%</td><td>6.76</td><td>2.4e-14</td><td>0.558</td><td>8.27</td></tr><tr><td>ResNet-18</td><td>CIFAR-100</td><td>2030</td><td>12</td><td>100.0%</td><td>5.64</td><td>2.5e-13</td><td>0.250</td><td>16.11</td></tr><tr><td>ResNet-18</td><td>SVHN</td><td>2027</td><td>12</td><td>100.0%</td><td>3.23</td><td>2.4e-13</td><td>0.316</td><td>17.31</td></tr><tr><td>ResNet-18</td><td>SVHN</td><td>2028</td><td>12</td><td>100.0%</td><td>3.42</td><td>1.8e-14</td><td>0.452</td><td>7.08</td></tr><tr><td>ResNet-18</td><td>SVHN</td><td>2030</td><td>12</td><td>100.0%</td><td>3.71</td><td>3.0e-14</td><td>0.568</td><td>8.78</td></tr><tr><td>WRN-28-2</td><td>CIFAR-10</td><td>2027</td><td>12</td><td>99.0%</td><td>10.55</td><td>2.4e-13</td><td>0.305</td><td>11.41</td></tr><tr><td>WRN-28-2</td><td>CIFAR-10</td><td>2028</td><td>12</td><td>99.0%</td><td>10.93</td><td>8.0e-14</td><td>0.290</td><td>10.55</td></tr><tr><td>WRN-28-2</td><td>CIFAR-10</td><td>2030</td><td>12</td><td>97.9%</td><td>10.90</td><td>2.9e-13</td><td>0.263</td><td>11.19</td></tr><tr><td>WRN-28-2</td><td>CIFAR-100</td><td>2027</td><td>12</td><td>99.0%</td><td>19.54</td><td>9.3e-14</td><td>0.323</td><td>7.83</td></tr><tr><td>WRN-28-2</td><td>CIFAR-100</td><td>2028</td><td>12</td><td>97.9%</td><td>21.16</td><td>1.7e-13</td><td>0.387</td><td>12.59</td></tr><tr><td>WRN-28-2</td><td>CIFAR-100</td><td>2030</td><td>12</td><td>99.0%</td><td>18.15</td><td>8.0e-14</td><td>0.264</td><td>8.63</td></tr><tr><td>WRN-28-2</td><td>SVHN</td><td>2027</td><td>12</td><td>99.0%</td><td>5.02</td><td>1.4e-13</td><td>0.121</td><td>5.76</td></tr><tr><td>WRN-28-2</td><td>SVHN</td><td>2028</td><td>12</td><td>99.0%</td><td>4.95</td><td>4.4e-14</td><td>0.208</td><td>6.57</td></tr><tr><td>WRN-28-2</td><td>SVHN</td><td>2030</td><td>12</td><td>100.0%</td><td>5.64</td><td>8.8e-14</td><td>0.290</td><td>11.24</td></tr><tr><td>PlainConvNet</td><td>CIFAR-10</td><td>2027</td><td>12</td><td>100.0%</td><td>22.71</td><td>6.3e-13</td><td>0.213</td><td>26.16</td></tr><tr><td>PlainConvNet</td><td>CIFAR-10</td><td>2028</td><td>12</td><td>100.0%</td><td>13.05</td><td>2.3e-13</td><td>0.141</td><td>23.27</td></tr><tr><td>PlainConvNet</td><td>CIFAR-10</td><td>2030</td><td>12</td><td>97.9%</td><td>19.10</td><td>3.4e-14</td><td>0.368</td><td>10.28</td></tr><tr><td>PlainConvNet</td><td>CIFAR-100</td><td>2027</td><td>12</td><td>100.0%</td><td>19.42</td><td>1.1e-13</td><td>0.234</td><td>13.77</td></tr><tr><td>PlainConvNet</td><td>CIFAR-100</td><td>2028</td><td>12</td><td>99.0%</td><td>21.38</td><td>7.8e-14</td><td>0.341</td><td>12.66</td></tr><tr><td>PlainConvNet</td><td>CIFAR-100</td><td>2030</td><td>12</td><td>99.0%</td><td>19.97</td><td>3.7e-14</td><td>0.343</td><td>9.55</td></tr><tr><td>PlainConvNet</td><td>SVHN</td><td>2027</td><td>12</td><td>96.9%</td><td>8.59</td><td>8.0e-14</td><td>0.228</td><td>11.56</td></tr><tr><td>PlainConvNet</td><td>SVHN</td><td>2028</td><td>12</td><td>99.0%</td><td>10.37</td><td>7.3e-14</td><td>0.165</td><td>9.34</td></tr><tr><td>PlainConvNet</td><td>SVHN</td><td>2030</td><td>12</td><td>100.0%</td><td>14.92</td><td>3.7e-14</td><td>0.335</td><td>11.31</td></tr></table>

## A-page-0018

target PDF page 18

Table 12: Path-level condition-number-100 stress results. Each row is one frozen path; spectral score error is zero at reported precision on every row.

[tbl-11.html](tbl-11.html)

![img-4.jpeg](img-4.jpeg)

(a) Minimum winner-change rate over seeds.

![img-5.jpeg](img-5.jpeg)

(b) Worst projector residual over seeds.

Figure 5: Balanced visual gauge matrix by architecture and dataset.

#### A.3.6 HISTORICAL TWO-RESAMPLE PGD PILOT

We reuse the frozen ResNet-18/CIFAR-10 checkpoint and existing matched PGD/random image artifacts, but change the input path from clean-to-input to clean-to-perturbed. The primary setting is  \( \ell_{\infty} \)  2/255, where the PGD success labels are not saturated. For each of two independent selection seeds, we sample 32 clean-correct PGD-success and 32 clean-correct PGD-failure examples, then evaluate both the PGD and matched random endpoint for every selected sample. Thus the balanced PGD success/failure sample is case-control by construction; its 50% success rate is not an estimate of the dataset-level attack rate. Table 14 reports the two historical resamples.

Both resamples pass the exact implementation checks: the maximum projector covariance error is 4.7e-12 and the maximum pulled-back spectral-score discrepancy is 4.8e-07. Across the two resamples, PGD success-stratum AUC ranges from 0.952–0.959 (pooled AUC 0.956), while PGD median  \( R_{P} \)  ranges from 2.68–2.81 logits and matched random medians remain near zero (-0.014 to +0.024 logits). The mean paired PGD-minus-random effect is 3.53 logits. This historical pilot motivated the broader endpoint grid, but its signed separation result is not pooled with the core magnitude estimand. Neither artifact establishes a universal adversarial mechanism, cross-architecture transfer beyond the grid, or calibrated attack-success prediction outside the frozen case-control protocols.

#### A.3.7 COMPARATOR AND ABLATION RATIONALE

The intervention comparison must respect the same gauge symmetry as the proposed method. Conventional hidden-coordinate conductance remains a parameterization-relative diagnostic; the Q2 orbit and relocation experiments use it as a gauge-sensitive negative control, not a gauge-invariant utility

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

[OCR table id=tbl-11.html; page=18]
<table><tr><td>Path</td><td>Rank</td><td>Rel. gap</td><td>\( \|P\|_2 \)</td><td>Coord. range</td><td>Proj. residual</td></tr><tr><td>9967</td><td>1</td><td>0.759</td><td>4.23</td><td>8.89</td><td>1.9e-13</td></tr><tr><td>6907</td><td>2</td><td>0.831</td><td>4.94</td><td>8.00</td><td>1.6e-12</td></tr><tr><td>7413</td><td>2</td><td>0.619</td><td>6.25</td><td>8.41</td><td>6.7e-13</td></tr><tr><td>2648</td><td>1</td><td>0.243</td><td>16.73</td><td>7.89</td><td>1.3e-11</td></tr><tr><td>5113</td><td>1</td><td>0.524</td><td>21.75</td><td>10.23</td><td>9.5e-12</td></tr><tr><td>3463</td><td>2</td><td>0.589</td><td>14.09</td><td>10.52</td><td>3.7e-12</td></tr><tr><td>3098</td><td>2</td><td>0.653</td><td>5.96</td><td>5.84</td><td>1.8e-13</td></tr><tr><td>7427</td><td>1</td><td>0.568</td><td>5.16</td><td>7.28</td><td>2.9e-13</td></tr><tr><td>1769</td><td>1</td><td>0.616</td><td>4.53</td><td>8.36</td><td>1.2e-13</td></tr><tr><td>2091</td><td>1</td><td>0.777</td><td>4.30</td><td>13.66</td><td>9.0e-14</td></tr><tr><td>4132</td><td>1</td><td>0.508</td><td>3.34</td><td>3.73</td><td>5.9e-14</td></tr><tr><td>3399</td><td>1</td><td>0.775</td><td>3.93</td><td>5.95</td><td>5.0e-14</td></tr></table>

## A-page-0019

target PDF page 19

Table 13: Complete adversarial endpoint grid. $AUC_{|R|}$ is the attack-success/failure separation AUC for absolute restored effect, with a bootstrap interval over endpoint strata; $\Delta|R|$ is the paired attack-minus-random mean with its bootstrap interval. Signed quantities are secondary diagnostics. The final column is the maximum paired relative $\ell_2$ norm mismatch; the two smallest modulus gaps identify near-tie cells.

[tbl-12.html](tbl-12.html)

Table 14: Historical two-resample PGD pilot on a frozen ResNet-18/CIFAR-10 checkpoint at 2/255. Paths gives PGD/random counts; AUC is computed only within the balanced PGD success/failure selection; $R_P$ is the dominant restored target-logit effect from Eq. 10.

[tbl-13.html](tbl-13.html)

comparator. We therefore use the runner-up spectral cluster not as a competing attribution method, but as a same-rank, gauge-equivariant spectral comparator computed from the same matrix. Selecting the largest remaining modulus within that rank-matched set makes the comparison deterministic and prevents tuning a weak comparator after seeing outcomes.

This tests whether the dominant-cluster rule contributes beyond spectral invariance alone. The comparison is local rather than exhaustive: random invariant subspaces require an extra gauge-dependent metric, whereas coordinate conductance answers the negative-control question above. Future comparisons should include other analytic matrix functions and task-supervised invariant subspaces, with their selection information and rank controlled explicitly.

Our ablation removes the projected endpoint displacement while retaining the same path baseline and downstream function. Absolute target-logit change is paired within each path, avoiding cross-example scale comparisons in the win metric. The effect ratio supplies magnitude, while Wilson intervals expose uncertainty from the finite number of paths. No result is filtered by whether the dominant cluster wins.

### A.3.8 NONLINEAR CUTS AND SCOPE OF EVIDENCE

The theorem allows arbitrary differentiable downstream networks, while some direct controllability experiments use penultimate linear heads for exact prescription and transparent ablation. Separate trained nonlinear-cut probes on all three architectures recover nontrivial, full-rank conductance matrices and nontrivial power-trace information beyond completeness. Their worst numerical completeness error is $9.74 \times 10^{-3}$. These probes establish that the matrix object is not restricted to a linear head, but we do not count them as intervention-utility evidence. The balanced spectral matrix supplies the nonlinear-cut gauge tests; broader nonlinear downstream utility remains an important extension.

### A.3.9 VISION INTERVENTION UTILITY

Table 5 now reports the complete five-cell utility summary, including both median effect magnitudes rather than ratios alone. The five source artifacts retain all sampled paired path outcomes, including

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

[OCR table id=tbl-12.html; page=19]
<table><tr><th>Architecture</th><th>Attack</th><th>ε</th><th>AUC<sub>|R|</sub> [95%]</th><th>Attack |R|</th><th>Random |R|</th><th>Δ|R| [95%]</th><th>AUC<sub>R</sub></th><th>ΔR</th><th>Eigengap</th><th>Modulus gap</th><th>Norm err.</th></tr><tr><td>ResNet-18</td><td>PGD-40</td><td>1/255</td><td>0.500 [0.264, 0.729]</td><td>0.02</td><td>0.01</td><td>0.015 [0.005, 0.028]</td><td>0.535</td><td>2.16e-02</td><td>0.200</td><td>2.9e-03</td><td>3.6e-07</td></tr><tr><td>ResNet-18</td><td>PGD-40</td><td>2/255</td><td>0.681 [0.438, 0.889]</td><td>0.04</td><td>0.02</td><td>0.016 [-0.004, 0.039]</td><td>0.660</td><td>4.84e-02</td><td>0.212</td><td>1.3e-03</td><td>2.9e-07</td></tr><tr><td>ResNet-18</td><td>APGD-CE</td><td>1/255</td><td>0.556 [0.319, 0.778]</td><td>0.02</td><td>0.02</td><td>0.012 [0.001, 0.023]</td><td>0.528</td><td>1.63e-02</td><td>0.093</td><td>3.4e-04</td><td>2.2e-07</td></tr><tr><td>ResNet-18</td><td>APGD-CE</td><td>2/255</td><td>0.590 [0.340, 0.806]</td><td>0.02</td><td>0.01</td><td>0.019 [0.001, 0.040]</td><td>0.576</td><td>1.33e-02</td><td>0.271</td><td>1.4e-02</td><td>2.3e-07</td></tr><tr><td>WRN-28-2</td><td>PGD-40</td><td>1/255</td><td>0.674 [0.444, 0.903]</td><td>0.04</td><td>0.02</td><td>0.013 [-0.003, 0.026]</td><td>0.403</td><td>1.01e-02</td><td>0.130</td><td>6.5e-03</td><td>2.9e-07</td></tr><tr><td>WRN-28-2</td><td>PGD-40</td><td>2/255</td><td>0.451 [0.215, 0.688]</td><td>0.05</td><td>0.03</td><td>0.025 [0.008, 0.042]</td><td>0.340</td><td>-4.44e-04</td><td>0.194</td><td>2.0e-03</td><td>3.1e-07</td></tr><tr><td>WRN-28-2</td><td>APGD-CE</td><td>1/255</td><td>0.792 [0.590, 0.965]</td><td>0.04</td><td>0.02</td><td>0.016 [0.006, 0.027]</td><td>0.514</td><td>5.47e-03</td><td>0.172</td><td>4.8e-04</td><td>3.0e-07</td></tr><tr><td>WRN-28-2</td><td>APGD-CE</td><td>2/255</td><td>0.861 [0.674, 1.000]</td><td>0.02</td><td>0.02</td><td>0.003 [-0.008, 0.014]</td><td>0.500</td><td>-4.56e-03</td><td>0.232</td><td>9.2e-03</td><td>1.6e-07</td></tr><tr><td>PlainConvNet</td><td>PGD-40</td><td>1/255</td><td>0.500 [0.250, 0.729]</td><td>0.11</td><td>0.04</td><td>0.079 [0.060, 0.099]</td><td>0.583</td><td>-9.20e-03</td><td>0.112</td><td>1.3e-02</td><td>2.1e-07</td></tr><tr><td>PlainConvNet</td><td>PGD-40</td><td>2/255</td><td>0.576 [0.340, 0.806]</td><td>0.18</td><td>0.08</td><td>0.095 [0.058, 0.132]</td><td>0.583</td><td>5.41e-02</td><td>0.171</td><td>5.1e-03</td><td>2.3e-07</td></tr><tr><td>PlainConvNet</td><td>APGD-CE</td><td>1/255</td><td>0.694 [0.465, 0.882]</td><td>0.10</td><td>0.04</td><td>0.064 [0.044, 0.088]</td><td>0.396</td><td>-5.17e-02</td><td>0.112</td><td>4.0e-03</td><td>2.2e-07</td></tr><tr><td>PlainConvNet</td><td>APGD-CE</td><td>2/255</td><td>0.882 [0.715, 0.993]</td><td>0.16</td><td>0.08</td><td>0.050 [0.006, 0.092]</td><td>0.333</td><td>-3.00e-02</td><td>0.131</td><td>3.4e-03</td><td>2.2e-07</td></tr></table>

[OCR table id=tbl-13.html; page=19]
<table><tr><th>Resample</th><th>Paths</th><th>PGD AUC</th><th>PGD median $R_P$</th><th>Random median $R_P$</th><th>Paired mean difference</th></tr><tr><td>Resample 1</td><td>64/64</td><td>0.952</td><td>2.81</td><td>-0.014</td><td>3.41</td></tr><tr><td>Resample 2</td><td>64/64</td><td>0.959</td><td>2.68</td><td>0.024</td><td>3.65</td></tr></table>

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

comparator wins and isolation exclusions; the aggregate artifact records the exact per-cell requested and usable counts and Wilson intervals.

### A.3.10 AG NEWS ENVIRONMENTS AND COMPLEMENT HOLDOUT

We reuse the locally audited AG News corpus but train a new two-layer, four-head Transformer from scratch, with no pretrained data. The 128-dimensional CLS cut feeds a nonlinear GELU MLP head. Conductance follows a differentiable path from a null-token embedding baseline through the Transformer, rather than interpolating discrete token IDs. A seed-2026 pilot freezes the protocol; seeds 2027–2029 are untouched holdouts evaluated on clean text, deterministic word dropout, and deterministic character deletion. Table 15 reports the seed-level worst-environment summary.

Table 15: AG News holdouts. Accuracy and coordinate change are worst-environment values; RU denotes wins over the matched-rank runner-up.

[tbl-14.html](tbl-14.html)

Across 9 seed–environment cells and 144 paths, the weakest environment accuracy is 73.60% and conductance matrices have numerical rank up to 22. The worst completeness error is 1.74e-03, maximum projector covariance error is 1.64e-14, and spectral score discrepancy is zero at reported precision. The minimum environment-level coordinate-winner change rate is 97.92%, while the dominant cluster wins the paired absolute target-logit comparison against the matched-rank runner-up on every path. In the fresh seed-2029 holdout, it also beats the higher-capacity entire spectral complement on 100.0% of 72 paths; median absolute effects are 2.21 versus 0.004 logits.

Table 16: Complete AG News environment holdouts. Each row is one seed–environment cell; Acc. is accuracy, Coord. is coordinate-winner change, RU is the dominant-versus-runner-up win rate, and Ratio is the median paired effect ratio.

[tbl-15.html](tbl-15.html)

Seeds 2027–2028 use the matched-rank runner-up; seed 2029 additionally tests the entire spectral complement on 24 paths per environment. This separately frozen comparison is reported here rather than extrapolated to the two earlier holdouts. This result is a modality replication, not merely another image dataset: the encoder, inputs, perturbations, and nonlinear head all differ. It remains one text corpus and one Transformer family, and the very small complement effect makes universal superiority an inappropriate claim.

### A.4 COMPLETE EXPERIMENTAL PROTOCOL

### A.4.1 BALANCED MATRIX

The primary matrix contains 12 paths per architecture–dataset–seed cell and four dense gauges per path, with both direct and composed checks contributing to the recorded gauge-trial total. Independent

[OCR table id=tbl-14.html; page=20]
<table><tr><td>Seed</td><td>Paths</td><td>Acc.</td><td>Coord.</td><td>Proj. err.</td><td>RU</td></tr><tr><td>2027</td><td>36</td><td>73.70%</td><td>97.9%</td><td>8.8e-15</td><td>100.0%</td></tr><tr><td>2028</td><td>36</td><td>73.60%</td><td>97.9%</td><td>1.6e-14</td><td>100.0%</td></tr><tr><td>2029</td><td>72</td><td>73.85%</td><td>97.9%</td><td>1.5e-14</td><td>100.0%</td></tr></table>

[OCR table id=tbl-15.html; page=20]
<table><tr><td>Seed</td><td>Environment</td><td>Paths</td><td>Accuracy</td><td>Coord. change</td><td>Proj. residual</td><td>RU</td><td>Effect ratio</td></tr><tr><td>2027</td><td>Clean</td><td>12</td><td>74.5%</td><td>100.0%</td><td>8.8e-15</td><td>100%</td><td>237.5</td></tr><tr><td>2027</td><td>Word dropout</td><td>12</td><td>74.0%</td><td>97.9%</td><td>3.2e-15</td><td>100%</td><td>451.9</td></tr><tr><td>2027</td><td>Character deletion</td><td>12</td><td>73.7%</td><td>100.0%</td><td>4.0e-15</td><td>100%</td><td>938.7</td></tr><tr><td>2028</td><td>Clean</td><td>12</td><td>75.4%</td><td>100.0%</td><td>4.0e-15</td><td>100%</td><td>195.4</td></tr><tr><td>2028</td><td>Word dropout</td><td>12</td><td>73.9%</td><td>100.0%</td><td>1.6e-14</td><td>100%</td><td>488.3</td></tr><tr><td>2028</td><td>Character deletion</td><td>12</td><td>73.6%</td><td>97.9%</td><td>7.3e-15</td><td>100%</td><td>351.5</td></tr><tr><td>2029</td><td>Clean</td><td>24</td><td>74.9%</td><td>100.0%</td><td>5.2e-15</td><td>100%</td><td>974.5</td></tr><tr><td>2029</td><td>Word dropout</td><td>24</td><td>73.9%</td><td>97.9%</td><td>1.5e-14</td><td>100%</td><td>232.7</td></tr><tr><td>2029</td><td>Character deletion</td><td>24</td><td>74.3%</td><td>99.0%</td><td>1.0e-14</td><td>100%</td><td>1456.1</td></tr></table>

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

seeds repeat model training and the complete matrix rather than merely resampling gauges. Paths are restricted to correctly classified examples to avoid conflating gauge behavior with an incorrect endpoint prediction.

For every trial we verify original and transformed logits, the conductance similarity residual, projector covariance after pullback, equality of spectral intervention scores, coordinate top selection, and coordinate-selected intervention range. We also record dominant-cluster rank, relative eigengap, and projector norm. A cell passes only when all frozen criteria pass.

#### A.4.2 INTERVENTION-UTILITY PROTOCOL

The development comparison contains 48 paths. The comparator is the largest remaining isolated spectral cluster with the dominant cluster's rank (the same-rank runner-up). Primary effects use the true-class logit on clean-correct paths; the next class modulo the output dimension is evaluated as a frozen target-control diagnostic. Holdout paths, checkpoints, cluster rules, outcome metrics, and thresholds were frozen before execution. We report path-level win fractions with Wilson intervals because each holdout contains 24 independent paired paths; effect ratios summarize magnitude but are not treated as calibrated probabilities.

#### A.4.3 ATTACK-PATH PROTOCOL

The core attack grid uses frozen seed-2026 ResNet-18, WRN-28-2, and PlainConvNet CIFAR-10 checkpoints, PGD-40 and APGD-CE, and 1/255 and 2/255 budgets. For each of 12 cells, selection scans clean-correct examples until it obtains 12 attack successes and 12 attack failures; each selected attack endpoint is paired with a box-feasible randomized assignment/sign control that preserves its displacement magnitudes. The same IDs pair each endpoint type; no endpoint or label is regenerated during conductance evaluation. We compute 129-point clean-to-endpoint paths, use the true-class logit as the scalar target, select the largest-modulus cluster, and apply four condition-bounded dense gauges per endpoint path. The primary estimand is \( |R| \), with signed \( R \) retained as a directional diagnostic. Both AUCs are within-selection descriptive separation statistics, not population attack-success estimates; bootstrap intervals resample endpoint strata or clean-image pairs, never gauge trials. The historical 4/255 pilot is retained only as supplementary magnitude context because its PGD labels were saturated.

#### A.4.4 EVIDENCE LADDER AND STATISTICAL DESIGN

Table 18 separates algebraic verification, adversarial severity, replication, numerical stress, and utility. Accumulating gauge trials cannot strengthen an exact theorem, while utility cannot prove the gauge law; each block therefore has a distinct falsification target.

Table 17 records how the numerical tables relate to the frozen artifacts in experiments/results. PDF tables expose every independent seed or environment cell and all stress paths; the larger utility, matrix, and NLP artifacts retain the paired path rows and gauge draws rather than treating them as independent replications.

Table 17: Numerical provenance and aggregation. “Worst” denotes the maximum error/range or minimum success statistic, as appropriate. Braced names denote one artifact per listed cell.

[tbl-16.html](tbl-16.html)

Invariance reports worst-case residuals because one failed path falsifies the implementation claim; coordinate instability uses per-cell minima and path-cluster bootstrap lower bounds, while gauge-trial Wilson intervals are descriptive. Utility uses paired path-level wins and 95% Wilson intervals. Input

[OCR table id=tbl-16.html; page=21]
<table><tr><td>Evidence block</td><td>PDF rows</td><td>Retained rows</td><td>Source artifact</td><td>Reported aggregation</td></tr><tr><td>Direct relaxation</td><td>3 pilot + 18 holdout</td><td>21 seed trials</td><td>direct, conductance, gauge, [intervention, holdout], vi. +</td><td>per seed, pilot per architecture</td></tr><tr><td>Balanced visual matrix</td><td>27</td><td>324 paths / 2,392 gauges</td><td>conductance, spectral matrix, [arch], [data], seed [x], vi. json</td><td>per seed cell, path worst cases and trial cases</td></tr><tr><td>Quadrature convergence</td><td>5</td><td>9 paths / 5 resolutions</td><td>conductance, quadrature, convergence, vi. json</td><td>production vs reference matrix and effect rows</td></tr><tr><td>Conditioning stress</td><td>12</td><td>12 paths</td><td>conductance, spectral stability, stress, vi. json</td><td>every path, no pooling</td></tr><tr><td>Vision utility</td><td>5</td><td>120 paired paths</td><td>conductance, spectral, causal utility, [cell], vi. json</td><td>wins, Wilson LR, and paired medians per cell</td></tr><tr><td>Attack endpoint grid</td><td>12 cells</td><td>288 attack + 288 random paths</td><td>conductance, attack, path, grid, vi. json</td><td>magnitude AUC, paired absolute effects, signed diagnostics, and isolation gains</td></tr><tr><td>Historical attack plot</td><td>2 resamples</td><td>128 PGD + 128 random paths</td><td>conductance, attack, path, n64, [resample], vi. json</td><td>supplementary signed AUC and paired nontrend effects</td></tr><tr><td>NLP replication</td><td>9</td><td>144 paired paths</td><td>np, conductance, gauge, seed [x], .json</td><td>per seed environment cell, seed worst cases in main text</td></tr></table>

## A-page-0022

target PDF page 22

Table 18: Evidence ladder. Counts are not pooled across incompatible estimands.

[tbl-17.html](tbl-17.html)

paths are experimental units, training seeds and architecture–dataset or text-environment cells are replication axes, and gauge draws are not independent utility evidence.

### A.5 DISCUSSION AND SCOPE

Even apart from feature superposition (Elhage et al., 2022), function-preserving affine gauges make coordinate attribution non-identifiable; sparse dictionary learning can act as a gauge-fixing mechanism. Coordinate attribution therefore requires a privileged or explicitly gauge-fixed basis; otherwise, the fixed spectral rule supplies a gauge-equivariant intervention target.

The evidence supports four bounded claims: theory and trained models permit coordinate reassignment without function change; spectral interventions obey the gauge law and the dominant cluster has a larger target-conditioned effect than the matched-rank comparator; and the attack grid compares restored-effect magnitude with matched-random endpoint controls. We do not establish natural dense gauges, useless neuron analyses, semantic or universally optimal clusters, or coverage of every subspace family. Attack evidence is conditional on PGD/APGD, three seed-2026 CIFAR-10 checkpoints, two non-saturated budgets, and the clean-correct case-control protocol; it does not claim universal robustness prediction or transfer. Magnitude is positive in 12/12 cells with positive paired bootstrap lower bounds in 9 cells; signed direction is mixed and 2 cells approach the modulus-tie boundary. The scope is bounded by the \( GL(d) \) functional equivalence and reported separation/conditioning, with priorities of semantic causal ground truth, multiple layer depths, and low-rank approximations for wide layers.

![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)

Figure 6: Conditioning stress. Projector covariance error remains below the frozen \(10^{-5}\) tolerance at condition number 100.

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

[OCR table id=tbl-17.html; page=22]
<table><tr><td>Block</td><td>Scale</td><td>Role</td></tr><tr><td>Nonlinear theorem check</td><td>general downstream map</td><td>similarity, diagonal, and trace implementation</td></tr><tr><td>Targeted credit relocation</td><td>3 architectures</td><td>realize a bottom-decile unit as the credit winner</td></tr><tr><td>Direct frozen holdout</td><td>9 arch.-data cells</td><td>preserve logits and complete totals on untouched seeds</td></tr><tr><td>Balanced spectral matrix</td><td>27 cells; 324 paths; 2,592 gauges</td><td>replicate instability and projector equivariance</td></tr><tr><td>Quadrature convergence</td><td>3 cells; 9 paths; 3 resolutions</td><td>check the production path-integral discretization</td></tr><tr><td>Conditioning stress</td><td>\( \kappa(M) \leq 100 \)</td><td>expose eigengap and projector-norm sensitivity</td></tr><tr><td>Vision utility holdouts</td><td>5 settings; 120 paths</td><td>test generalization without retuning</td></tr><tr><td>Attack endpoint grid</td><td>12 cells; 576 endpoint paths</td><td>test conditional PGD/APGD magnitude separation and gauge covariance</td></tr><tr><td>Historical attack pilot</td><td>2 resamples; 256 retained paths</td><td>supplementary PGD signed-effect replication</td></tr><tr><td>NLP holdouts</td><td>9 cells; 144 paths</td><td>test cross-modal replication and text-shift behavior</td></tr></table>

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

### A.6 SCOPE

The supported scope is exact gauge non-identifiability, numerical spectral equivariance, and conditional utility in frozen vision and text settings; it does not imply useless neuron analyses, naturally occurring arbitrary gauges, uniquely optimal projectors, or semantic causal discovery.
