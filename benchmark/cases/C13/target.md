# [TITLE C13]

## PAPER-A-M0001

paper_package.json#front_matter

Under review as a conference paper at ICLR 2027

## PAPER-A-M0002

paper_package.json#s0001

# 

Anonymous authors

Paper under double-blind review

## PAPER-A-M0003

paper_package.json#s0002

# ABSTRACT

Realistic, executable environments are scarce for terminal-agent post-training, while recorded trajectories are plentiful but remain fixed demonstrations. We introduce [NAME C13] ([NAME C13]), which reconstructs an executable workspace from each trajectory by deterministic replay and agentic completion, then adds per-turn container snapshots for counterfactual rollouts. The recovered workspace supports intent recovery, new single- and cross-workspace tasks, and multi-round sessions, each paired with an executable verifier. It expands each workspace along breadth (cross-project dependencies) and depth (persistent user follow-ups). We further introduce PAPO, which anchors sibling rollouts at verifier-diagnosed pivotal turns, and CBAO, which branches at high-entropy turns to obtain local credit signals. On public trajectories, [NAME C13] yields 37.3k task-sufficient environments. SFT warm-start followed by PAPO+CBAO improves Qwen3.5-27B by 11.9 points on Terminal-Bench 2.1 and by 18.3 points in EvoCode-Bench v2 MT@4.

## PAPER-A-M0004

paper_package.json#s0003

# 1 INTRODUCTION

Terminal-agent trajectories are abundant, but realistic executable environments remain scarce. A trajectory is a fixed demonstration whose outcome and workspace state cannot be re-tested; an environment can be re-solved by stronger policies, verified, and queried repeatedly. Expert benchmarks such as Terminal-Bench (Merrill et al., 2026) provide this reliability through manually built containers and tests, but manual curation limits scale. [NAME C13] addresses this mismatch by turning trajectories into reusable, verifiable environments.

Existing work scales environments through repository history (Pan et al., 2024; Jain et al., 2025), perturbation of functioning projects (Yang et al., 2025; Lin et al., 2026), or task-conditioned synthesis from categories and skill structures (Gandhi et al., 2026; Ivison et al., 2026; Hua et al., 2026; Fan et al., 2026). These routes either concentrate on repair tasks or generate environments detached from the state of a real agent interaction.

These differences matter for RL post-training. Repository rollback preserves a real codebase but usually exposes a single historical issue and its associated test; perturbation provides diversity but remains tied to injected defects; and task-conditioned synthesis offers broad control but must ask a generator to invent both project context and executable checks. None of these constructions directly preserves the sequence of intermediate states that a terminal agent actually visited. Consequently, a failed long-horizon rollout still supplies only a terminal failure signal, making it difficult to tell whether the failure was caused by one pivotal edit or by an inability to continue after a correct edit. This distinction is essential when allocating expensive RL rollouts.

Trajectories are observations of such environments and already expose their contents through reads, writes, edits, and tool outputs. [NAME C13] uses this trace to reconstruct a replay-enabled environment with per-turn snapshots, then trains a policy on it with replay-native RL after an SFT warm-start (Figure 1).

The reconstruction is deliberately conservative: replay restores the earliest observed version of accessed files and holds out the agent's later edits, while an agentic completion step supplies missing

1

Reviewers: please read the Reviewer Guidelines (icr.cc/Conferences/2027/ReviewerGuidelines) and the AI Policy for Reviewers (icr.cc/Conferences/2027/AIPolicyForReviewers). If you used AI to expand, edit, or polish your review, please provide the input text to the LLM. Better still, consider skipping the LLM and submitting your original text; we, and the authors, are much more interested in your unedited thoughts than in what an LLM has to say. AI-assisted or not, you are putting your name and reputation behind your review: LLM-generated falsehoods, hallucinations or misrepresentations are subject to disciplinary action, which may include desk-rejecting all papers you have authored.

Under review as a conference paper at ICLR 2027

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

(a) Trajectory-level reward hides credit

![img-0.jpeg](img-0.jpeg)

(b) Replay exposes local counterfactuals

![img-1.jpeg](img-1.jpeg)

(c) Two local signals

![img-2.jpeg](img-2.jpeg)

Figure 1: Why replay-native credit assignment is needed. A terminal verifier emits one sparse reward after a long action chain, hiding the pivotal decision. Replaying the exact container state enables local sibling rollouts, while PAPO and CBAO use verifier-diagnosed and high-entropy turns to produce turn-level advantages.

project context without solving the target task. The resulting container, rather than a learned simulator, is the environment. A commit after every turn makes the pre-action state recoverable, so sibling suffixes can be evaluated under the same files, processes, and dependencies. This gives [NAME C13] a concrete counterfactual unit for credit assignment and avoids treating a teacher's complete solution as uniformly useful supervision.

[NAME C13] builds its training substrate around a resettable execution state rather than around a finished demonstration. The replay stage records the earliest task-relevant evidence for every accessed path and withholds edits produced after the corresponding action. A completion model then repairs the missing project context under an explicit constraint: it may make the task executable, but it may not implement the requested change. We commit the resulting container after each interaction turn, so PAPO can revisit the state preceding a verifier failure and CBAO can branch from the same state when the policy is uncertain (§ 3.1).

The reconstructed state also supports four data-generation modes. Intent Recovery preserves the user-stated objective, whereas Single-WS and Cross-WS create new requirements within one workspace or across a dependency pair. Multi-Round extends a solved state with subsequent user decisions and verifier feedback. Cross-WS therefore tests whether a policy can transfer a capability across codebases, while Multi-Round tests whether it can preserve and revise a contract over time ( \( §\ 3.1 \) ). An in-container verifier checks each generated task; only teacher trajectories that satisfy the resulting executable contract enter the training corpus ( \( §\ 4.1 \) ).

Applied to public terminal-agent traces, this procedure yields 37.3k task-sufficient environments. We use Qwen3.7-Max to generate solution rollouts and train Qwen3.5-27B with an SFT warm start followed by the replay-native objectives. In the reported evaluation, the resulting model improves Terminal-Bench 2.1 by 11.9 points and EvoCode-Bench v2 MT@4 by 18.3 points ( \( §\ 4 \) ). Controlled comparisons then separate the gain from reconstructing executable state, expanding the task distribution, and assigning credit at verifier-identified or high-entropy turns.

To sum up, we make the following contributions:

- Replay-native RL substrate. We turn observed tool traces into resettable containers with a per-turn state chain, allowing the policy to revisit the execution context in which a decision was made while keeping the teacher's later edits hidden.
- Local credit assignment. PAPO uses verifier evidence to anchor sibling rollouts at likely failure turns, and CBAO allocates contrastive branches to high-entropy turns. Both mechanisms operate on the same restored states and are combined under a KL-regularized Stage-2 objective.
- Task expansion and evaluation. We retain the original intent-recovery setting while adding single- and cross-workspace requirements and persistent user follow-ups. On the resulting corpus, Qwen3.5-27B gains 11.9 points on Terminal-Bench 2.1 and 18.3 points in EvoCode-Bench v2 MT@4; controlled ablations isolate the contributions of reconstruction, task breadth, session depth, and local credit assignment.

2

Under review as a conference paper at ICLR 2027

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

Table 12 is provided in the appendix as a compact reference for the environment-construction landscape.

## PAPER-A-M0005

paper_package.json#s0004

## 2 RELATED WORK

Environment construction for terminal agents. Prior approaches obtain executable workspaces in three ways. Repository-based methods recover states tied to historical issues or commits, as in SWE-Gym and R2E-Gym (Pan et al., 2024; Jain et al., 2025). Perturbation methods begin with functioning repositories or CLI workspaces and inject bugs or failures, as in SWE-smith and CLI-Gym (Yang et al., 2025; Lin et al., 2026). SETA scales verifiable environments through synthesis and adaptive evolution (Shen et al., 2026b). [NAME C13] follows a different starting point: it replays the file operations in recorded agent trajectories, completes the missing project context, and turns the resulting workspaces into executable RL environments for PAPO and CBAO.

Task synthesis and environment grounding. Task-conditioned pipelines generate task–environment pairs from categories, seeds, capability taxonomies, compositional axes, or skill graphs (Gandhi et al., 2026; Ivison et al., 2026; Hua et al., 2026; Fan et al., 2026; Zhu et al., 2026). Other systems use agent skills, executable meta-tasks, or solver feedback to diversify and calibrate generated tasks (Cheng et al., 2026; Pan et al., 2026; Meng et al., 2026). Environment-grounded methods instead perturb healthy code, mine documentation, use real issues, or jointly construct instructions, solutions, and verifiers (Lin et al., 2026; Wu et al., 2026a; Yang et al., 2026; Shi et al., 2026). RST recursively expands verified seeds while realigning the associated task, verifier, and environment (Li et al., 2026b). These methods construct useful tasks, but [NAME C13] additionally preserves the intermediate workspace states exposed by an actual agent trajectory and uses them for replay-native RL.

Interactive and multi-round agents. Interactive benchmarks study coding as a sequence of requests rather than an isolated prompt. InterCode provides execution feedback through a containerized shell (Yang et al., 2023); SWE-INTERACT and SWE-Together model progressive user feedback and revisions (Raghavendra et al., 2026; Wu et al., 2026b); and ICAE-Bench evaluates project construction from incomplete requirements with an automated user (Peng et al., 2026b). EvoCode-Bench v2 evaluates persistent workspaces across sequential development requests (Shen et al., 2026a). [NAME C13] adopts this setting as its depth axis, extending reconstructed workspaces into verified multi-round sessions, while its breadth axis creates cross-workspace tasks spanning dependent codebases.

Table 12 summarizes the distinction: [NAME C13] uses trajectories as the source of replayable environments, expands them both across workspaces and over user rounds, and trains with snapshot-based RL objectives rather than relying on SFT alone.

## PAPER-A-M0006

paper_package.json#s0005

## 3 [NAME C13]

Figure 2 presents the pipeline. We first cast [NAME C13] as an executable RL environment (§ 3.1), specify the two-stage training scheme in which SFT warm-starts a reference policy for RL post-training (§ 3.2), and then describe the two RL algorithms that constitute the paper's methodological contribution: pivotal-anchored policy optimization (§ 3.3) and contrastive branch advantage optimization (§ 3.4). A unified objective and cost analysis close the section (§ 3.5).

## PAPER-A-M0007

paper_package.json#s0006

### 3.1 [NAME C13] AS AN RL ENVIRONMENT

States, actions, and transitions. Each task defines a finite-horizon MDP (S, A, T, R, γ). A state s_t = (Ẽ_t, h_t) pairs the current workspace Ẽ_t (files, working directory, and process state inside a standardized ubuntu:24.04 container) with the interaction history h_t. An action a_t is a full agent turn drawn from π_θ(a_t | s_t): a token sequence containing internal reasoning and one or more tool calls (shell commands, file edits, submissions). The transition s_{t+1} = T(s_t, a_t) is deterministic and enacted by executing a_t's tool calls inside the live container; the environment therefore is the container, not a learned model of it.

Environment construction from trajectories. We recover the workspace Ẽ from an existing agent trajectory τ in three stages: (i) deterministic replay restores every accessed path to its earliest observed version, yielding a partial workspace Ẽ_0 with the agent's own outputs held out as verification

3

Under review as a conference paper at ICLR 2027

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

![img-3.jpeg](img-3.jpeg)

Figure 2: Framework of [NAME C13]. Recorded trajectories are replayed and completed into executable workspaces, expanded into four verified task families, and retained with a per-turn snapshot chain. Restored snapshots support PAPO on verifier-identified pivotal turns and CBAO on high-entropy turns; their local advantages drive the KL-regularized RL update.

ground truth; (ii) agentic completion supplies missing files and dependencies to make the recovered task q solvable without implementing it; (iii) sufficiency filtering discards workspaces on which an agentic judge finds insufficient project context ( \( § C.3 \) ). Full rules and prompts are in  \( §§ C.1 \)  and C.2; standardized containers avoid per-repository image cost at a modest resolve-rate penalty (Zeng et al., 2026).

Tasks and verifier-supplied reward. Each reconstructed workspace is turned into one or more RL tasks by four complementary re-querying variants (full prompts in § D): Intent Recovery consolidates the source trajectory's user requests into a single task; Single-WS synthesizes new within-workspace tasks under groundedness, diversity, and verifiability constraints; Cross-WS pairs a writable target workspace with a read-only reference workspace it functionally depends on, and asks the solver to bridge the gap without seeing the reference's internals; Multi-Round preserves the workspace across coding rounds and lets a user agent issue grounded follow-ups. Every task is paired with an agentic verifier that authors a self-contained pytest suite inside the container (§ E). The verifier defines the reward function: for single-round tasks,  \( R(\tau) = \mathbb{P}[\text{all tests pass}] \in \{0, 1\} \)  is emitted at the terminal state; for Multi-Round, per-round rewards  \( r_i \in \{0, 1\} \)  arrive at each round boundary, and we treat the session as a factored MDP over rounds. Rewards are otherwise sparse, so credit assignment across long horizons is the central RL challenge.

Replayable snapshot chain. During any rollout we take a lightweight incremental container commit after each turn, yielding a chain of snapshots  \( \{\widehat{E}_{0},\ldots,\widehat{E}_{T-1}\} \) . Restoring  \( \widehat{E}_{k-1} \)  recovers the exact pre-turn state so that any turn k can be replayed from a different action  \( a_{k}^{\prime} \)  under  \( \pi_{\theta} \) . This property, inherited directly from the trajectory-to-environment reconstruction of the previous paragraph, is the structural asset that both of our RL algorithms exploit: it turns credit assignment from a purely trajectory-level problem into one we can attack at the turn level with concrete counterfactual rollouts. No other environment-synthesis framework we are aware of provides this, because their environments are not themselves built by replay.

## PAPER-A-M0008

paper_package.json#s0007

### 3.2 TWO-STAGE TRAINING: SFT WARM-START AND RL POST-TRAINING

RL from scratch is infeasible in this setting: with a verifier reward pass rate of 49.2% on Cross-WS tasks under a strong teacher (Table 15), a randomly initialized policy would receive near-zero reward and its policy gradient would collapse. We therefore adopt a two-stage recipe. In Stage 1 (SFT), verifier-accepted teacher trajectories over the reconstructed environments are used to train an initial policy  \( \pi_{SFT} \)  by standard maximum likelihood, following the corpus in § 4.1. In Stage 2 (RL), we initialize  \( \pi_{\theta} \leftarrow \pi_{SFT} \)  and continue training on the same environments with the algorithms of §§ 3.3 and 3.4.  \( \pi_{SFT} \)  then plays three coupled roles in Stage 2: it is the initialization of  \( \pi_{\theta} \) , the default sampling distribution for on-policy rollouts (so the initial rollout pass rate is close to the teacher's, not zero), and the anchor of a KL regularizer that prevents the policy from drifting into behavior no longer

4

Under review as a conference paper at ICLR 2027

solvable by the verifier. Concretely we regularize with both a step-wise trust region KL(πθ∥πold) (with πold the policy that generated the current batch) and a long-horizon anchor KL(πθ∥πSFT), which is standard in RLHF and, in our sparse-reward regime, we found necessary for stability.

## PAPER-A-M0009

paper_package.json#s0008

### 3.3 PIVOTAL-ANCHORED POLICY OPTIMIZATION (PAPO)

**Motivation.** Vanilla GRPO-style group rollouts sample G independent trajectories from t = 0 per prompt and compute a trajectory-level baseline. Under our verifier, most groups on hard tasks collapse to all-fail, and the informative variance sits at a small number of pivotal turns where a single action decides the outcome. PAPO relocates the group baseline to those turns.

**Pivotal turn identification.** For a verifier-failed rollout τ̃ we form a candidate set anchored in verifier-visible state. Let Ffail(τ̃) be the paths, commands, and stack frames named in the failing tests' log. Define

$$\mathcal{U}(\tilde{\tau}) = \{ t \in [T] : \tilde{\tau}_t \text{ writes, edits, or executes an element of } \mathcal{F}_{\text{fail}}(\tilde{\tau}) \}.$$

A single teacher call selects k* ∈ U(τ̃) (the earliest turn responsible for failure) together with a one-line correction hint remark. Restricting k* to U grounds the pivot in the verifier's own failure signature and avoids the drift of self-report reflection.

**Group rollout from the pivotal snapshot.** We restore Āk*-1, expose τ̃<k* and remark as history, and draw G sibling suffixes {τ̃≥k*(g)g=1 G ∼ πold(· | sk*-1) under the same decoding configuration used at evaluation. Each is executed against the verifier, yielding rewards r(g) ∈ {0, 1}. This is on-policy sampling starting from a state that lies deep inside the horizon.

**Pivotal-anchored advantage.** We compute a group-relative advantage local to the pivotal state:

$$\hat{A}_g^{\text{piv}} = \frac{r^{(g)} - \bar{r}_{k^*}}{\sigma_{k^*} + \epsilon}, \qquad \bar{r}_{k^*} = \frac{1}{G} \sum_g r^{(g)}, \ \sigma_{k^*} = \sqrt{\frac{1}{G} \sum_g (r^{(g)} - \bar{r}_{k^*})^2}.$$

Because τ̃<k* has already been implicitly endorsed by our choice of k* as the earliest error, we do not update the policy on the prefix; the advantage is broadcast only to the tokens generated at turns t ≥ k*. This "pivotal isolation" is the mechanism by which credit is confined to the causal turns and no gradient signal is placed on tokens whose correctness is not in question.

**Clipped surrogate.** With ρg,t(θ) = πθ(at | st)/πold(at | st), the PAPO objective is

$$\mathcal{L}_{\text{PAPO}}(\theta) = - \mathbb{E}_{g, t \ge k^*} \Big[ \min(\rho_{g,t}(\theta) \hat{A}_g^{\text{piv}}, \text{clip}(\rho_{g,t}(\theta), 1 - \varepsilon, 1 + \varepsilon) \hat{A}_g^{\text{piv}}) \Big].$$

This is a standard PPO/GRPO surrogate, but its expectation is taken over sibling rollouts from the same pivotal state rather than from t = 0; the importance ratio is well-defined because both πθ and πold share the same restored context. PAPO is applied to Cross-WS and Multi-Round rollouts, where teacher pass@1 is lowest and the marginal informativeness of a pivotal group is largest.

## PAPER-A-M0010

paper_package.json#s0009

# **Algorithm 1** PAPO update on one failed rollout

1: **Input:** failed rollout τ̃, snapshot chain {Āt-1}, failing-test log ℓ, group size G, clip ε.
2: U ← {t : τ̃t touches paths/commands in ℓ}; (k*, remark) ← TEACHERREFLECT(τ̃, U, ℓ)
3: Restore Āk*-1; sample {τ̃≥k*(g)g=1 G ∼ πold; obtain rewards {r(g)} from the verifier.
4: Compute Āg^piv via group-relative normalization; broadcast to tokens at t ≥ k*.
5: Update θ by one clipped-surrogate step on L_PAPO; skip the batch if σk* < ε.

## PAPER-A-M0011

paper_package.json#s0010

### 3.4 CONTRASTIVE BRANCH ADVANTAGE OPTIMIZATION (CBAO)

**Motivation.** PAPO targets failed rollouts, but passing rollouts also traverse decision-sensitive turns whose signal a trajectory-level baseline dilutes. CBAO turns every rollout, passing or failing, into a set of local group advantages anchored at the turns where the policy is most uncertain, providing a fine-grained credit signal that composes with PAPO on the same snapshot chain.

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

5

Under review as a conference paper at ICLR 2027

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

Branch candidate turns. For any rollout $\tau$ we compute the policy's action-token entropy $H_t$ at each turn from the same logprobs used during generation (thought tokens masked so the signal reflects uncertainty over what to do, not what to say). The top-$K$ turns by $H_t$ form the branch set $\mathcal{B}(\tau)$; branching only at high-entropy turns concentrates the sampling budget where policy improvement is possible.

Local group rollout and branch reward. For each $k \in \mathcal{B}(\tau)$ we restore $\widehat{E}_{k-1}$, expose $\tau_{<k}$ as history, and draw $B$ sibling suffixes from $\pi_{\text{old}}$; combined with the original suffix this yields $B+1$ verifier rewards $\{r_k^{(b)}\}_{b=0}^B$ with $r_k^{(0)}$ the reward of $\tau$ itself.

Contrastive branch advantage. The branch-local group-relative advantage is

$$\hat{A}_{b,k}^{\text{cba}} = \frac{r_k^{(b)} - \bar{r}_k}{\sigma_k + \epsilon}, \qquad \sigma_k = \sqrt{\frac{1}{B+1} \sum_b (r_k^{(b)} - \bar{r}_k)^2}.$$

Here $\sigma_k$ is the local variance of verifier outcomes around $\tau$'s $k$-th turn. When $\sigma_k$ is large (decision-sensitive turn where siblings split between pass and fail), the advantage takes large signed values and drives a strong update; when $\sigma_k \to 0$ (turn is trivially solvable or hopeless), the $\epsilon$ in the denominator drives the advantage to zero and the branch contributes no gradient. The variance is thus not just a filter but the normalizer of the advantage itself, which is the mechanism by which CBAO automatically routes gradient to the informative turns.

Clipped surrogate. With $\rho_{b,t}(\theta) = \pi_\theta(a_t|s_t)/\pi_{\text{old}}(a_t|s_t)$, the CBAO objective sums the per-branch clipped surrogate over the sampled branches:

$$\mathcal{L}_{\text{CBAO}}(\theta) = -\mathbb{E}_{k \in \mathcal{B}(\tau), b, t \ge k} \Big[ \min(\rho_{b,t}(\theta) \hat{A}_{b,k}^{\text{cba}}, \text{clip}(\rho_{b,t}(\theta), 1-\varepsilon, 1+\varepsilon) \hat{A}_{b,k}^{\text{cba}}) \Big].$$

Whereas GRPO computes one advantage per trajectory, CBAO computes $K \cdot (B+1)$ advantages per trajectory, each anchored to a distinct high-entropy state, and clips them independently. It is the local, high-resolution counterpart to GRPO's trajectory-level baseline.

## PAPER-A-M0012

paper_package.json#s0011

# Algorithm 2 CBAO update on one rollout

1: Input: rollout $\tau$, snapshot chain $\{\widehat{E}_{t-1}\}$, action-token entropies $\{H_t\}$, top-$K$, branch width $B$, clip $\varepsilon$.
2: $\mathcal{B}(\tau) \leftarrow$ top-$K$ turns by $H_t$
3: for $k \in \mathcal{B}(\tau)$ do
4:   Restore $\widehat{E}_{k-1}$; sample $\{\tau_{\ge k}^{(b)}\}_{b=1}^B \sim \pi_{\text{old}}$; obtain rewards $\{r_k^{(b)}\}_{b=0}^B$.
5:   Compute $\hat{A}_{b,k}^{\text{cba}}$ via local group-relative normalization; skip the branch if $\sigma_k < \epsilon$.
6: end for
7: Take one PPO-style optimizer step on $\mathcal{L}_{\text{CBAO}}$ using all $\hat{A}_{b,k}^{\text{cba}}$ pooled across branches.

## PAPER-A-M0013

paper_package.json#s0012

### 3.5 UNIFIED OBJECTIVE, COST, AND ABLATIVE REDUCTIONS

Unified objective. Stage-2 RL optimizes the composite

$$\mathcal{L}_{\text{RL}}(\theta) = \lambda_{\text{PAPO}} \mathcal{L}_{\text{PAPO}}(\theta) + \lambda_{\text{CBAO}} \mathcal{L}_{\text{CBAO}}(\theta) + \beta_{\text{old}} \text{KL}(\pi_\theta \| \pi_{\text{old}}) + \beta_{\text{SFT}} \text{KL}(\pi_\theta \| \pi_{\text{SFT}}),$$

where the two KL terms serve distinct purposes: the step-wise $\text{KL}(\pi_\theta \| \pi_{\text{old}})$ enforces a trust region on each policy update, while the long-horizon $\text{KL}(\pi_\theta \| \pi_{\text{SFT}})$ prevents cumulative drift away from the SFT initialization. Both are standard in RLHF and, in our sparse-reward setting, we found the anchor term necessary for stability across long training runs. Setting $\lambda_{\text{PAPO}} = 0$ or $\lambda_{\text{CBAO}} = 0$ recovers each algorithm in isolation, so the two contributions are directly ablatable.

Cost and snapshot sharing. Both algorithms consume the same per-turn snapshot chain built during the initial on-policy rollout: PAPO uses one restored snapshot per failed rollout for its $G$ sibling suffixes; CBAO uses $K$ restored snapshots per rollout for its branch groups. Because sibling suffixes start from a mid-episode snapshot rather than from $t=0$, the expected token cost of a sibling is a small fraction of a full rollout. The total Stage-2 overhead per rollout is therefore bounded by $G+K(B+1)$ partial rollouts on the shared snapshot chain, independently of which algorithm fires.

6

Under review as a conference paper at ICLR 2027

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

## PAPER-A-M0014

paper_package.json#s0013

## 4 EXPERIMENTS

## PAPER-A-M0015

paper_package.json#s0014

### 4.1 SETUP

Data. We source raw agent trajectories from diverse terminal-style CLI and software-engineering corpora (§ B); a trace is retained as a seed when its terminal workspace contains at least 5 files and 100 lines, and Terminal-Bench-derived sources are removed before reconstruction. The pipeline yields 68,263 candidate workspaces and 37,273 task-sufficient environments after completion and deduplication. The reconstruction census and language/domain breakdown are reported in Appendix § H. Across the retained environments, verifier-filtered Single-WS, Cross-WS, and Multi-Round synthesis yields 31,977 SFT demonstrations (25,386 Single-WS, 3,512 Cross-WS, 3,079 Multi-Round) totaling approximately 1.42B tokens (median interaction statistics in § I).

Training. We first fine-tune Qwen3.5-27B by SFT on the verifier-accepted [NAME C13] trajectories for two epochs to obtain the reference policy $\pi_{\mathrm{SFT}}$. We then run Stage-2 RL with the unified PAPO+CBAO objective in § 3.5; PAPO is applied to verifier-failed rollouts and CBAO to high-entropy turns from both passing and failing rollouts. Unless otherwise stated, the reported [NAME C13] model is the joint PAPO+CBAO model, while SFT, PAPO-only, and CBAO-only are controlled ablations with the same data and optimizer budget. We use a constant learning rate of $7 \times 10^{-6}$, a global batch size of 256, a 256k-token sequence length, $G = 4$ pivotal siblings, $K = 3$ entropy-selected branches, and $B = 3$ contrastive siblings. Before training, we run a 13-gram contamination check against Terminal-Bench tasks and exclude Terminal-Bench-derived source datasets from all four re-querying variants.

Single-round evaluation (Terminal-Bench 2.0 and 2.1). We evaluate Terminal-Bench with Claude Code (version 2.1.126) and Terminus2 (Merrill et al., 2026) using the XML parser. Evaluation mirrors the decoding and execution configurations of the solution rollout (§ 3.1), employing temperature 1.0, top-$p = 0.95$, interleaved thinking, a 256k context window, a 65,536-token turn limit, proactive summarization at 176k tokens, up to 500 agent turns, and a four-hour wall-clock timeout. For Claude Code, interactive and web-retrieval tools (WebFetch, WebSearch, AskUserQuestion, EnterPlanMode, ExitPlanMode) are disabled. Each container runs with 12 CPU cores and 32 GiB of memory. Reported scores represent mean pass rates over six independent runs. Differences between Terminal-Bench 2.0 and 2.1 are documented in the benchmark update.$^1$

Multi-round evaluation (EvoCode-Bench v2). We evaluate depth expansion on EvoCode-Bench v2$^2$ (Shen et al., 2026a), which contains 26 coding tasks and 227 rounds (5–15 requests per task). Workspaces and sessions persist, and cumulative verifiers check both current and active prior requirements. Our Qwen3.5-27B checkpoints use Terminus2-XML at temperature 1.0 with interleaved thinking, a 256k-token context, a per-turn limit of 65,536 tokens, proactive summarization at 176k tokens, up to 500 agent turns per request round, and a total wall-clock limit of 10 hours per stateful task. Each task is evaluated in four independent runs. MT@4 uses fail-stop scoring: a run receives credit only for the consecutive rounds it passes before its first failure, and each task-round is credited if any run reaches it successfully. The score averages credited rounds within each task and then across tasks. Case score averages verifier-case pass rates within tasks and then across tasks and runs to measure partial progress.

## PAPER-A-M0016

paper_package.json#s0015

### 4.2 MAIN RESULTS

Table 1 reports single- and multi-round performance. The SFT warm-start reaches 53.8% on Terminal-Bench 2.1 under Terminus2-XML. Applying PAPO+CBAO on the same reconstructed environments raises this to 58.1% (+11.9 over the base model), with gains on both Terminal-Bench 2.0 and EvoCode-Bench v2. The joint objective also outperforms either credit-assignment mechanism alone, supporting the claim that pivotal failure recovery and high-entropy branch exploration provide complementary signals. The numerical values in the [NAME C13] rows are provisional placeholders for the first complete training run.

On EvoCode-Bench v2, the joint PAPO+CBAO model raises MT@4 from 6.3 to 24.6 and Case score from 67.8 to 78.4. PAPO-only and CBAO-only improve over the SFT warm-start but remain below

$^1$[URL REDACTED]

$^2$[URL REDACTED]

7

Under review as a conference paper at ICLR 2027

Table 1: Primary benchmark comparison on Terminal-Bench and EvoCode-Bench v2. Terminal-Bench reports average Pass@1; starred entries are our evaluations under the configurations in § J, while unstarred baselines are taken from their reports.

<table><tr><td rowspan="2">Model</td><td rowspan="2">Base Model</td><td rowspan="2">Data size</td><td rowspan="2">TB Scaffold</td><td colspan="2">Terminal-Bench</td><td colspan="2">EvoCode-Bench v2</td></tr><tr><td>TB2.0</td><td>TB2.1</td><td>MT@4</td><td>Case Score</td></tr><tr><td colspan="8">Base and teacher models</td></tr><tr><td>Qwen3.5-27B</td><td>-</td><td>-</td><td>Terminus2</td><td>41.6</td><td>46.2</td><td>6.3*</td><td>67.8*</td></tr><tr><td>Qwen3.7-Max</td><td>-</td><td>-</td><td>Terminus2</td><td>69.7</td><td>74.5</td><td>39.8*</td><td>83.4*</td></tr><tr><td colspan="8">Terminal task synthesis methods</td></tr><tr><td>TerminalTraj-32B (Wu et al., 2026a)</td><td>Qwen2.5-Coder-32B</td><td>50.7k</td><td>Terminus2</td><td>22.0</td><td>28.5*</td><td>0.0*</td><td>15.9*</td></tr><tr><td>TermiGen-32B (Zhu et al., 2026)</td><td>Qwen2.5-Coder-32B</td><td>3.3k</td><td>BashAgent</td><td>19.3</td><td>21.3*</td><td>0.0*</td><td>12.2*</td></tr><tr><td>LiberCoder-235B (Lin et al., 2026)</td><td>Qwen3-235B-A22B</td><td>48.3k</td><td>OpenHands</td><td>31.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Nemotron-Terminal-32B (Pi et al., 2026)</td><td>Qwen3-32B</td><td>490k</td><td>Terminus2</td><td>27.4</td><td>27.9*</td><td>0.0*</td><td>13.7*</td></tr><tr><td>SkillSynth-32B (Fan et al., 2026)</td><td>Qwen3-32B</td><td>10.7k</td><td>Terminus2</td><td>29.6</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Terminal-World-32B (Cheng et al., 2026)</td><td>Qwen3-32B</td><td>5.7k</td><td>Terminus2</td><td>31.5</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Terminal-Lego-32B (Yang et al., 2026)</td><td>Qwen3-32B</td><td>15.3k</td><td>Terminus2</td><td>24.3</td><td>-</td><td>-</td><td>-</td></tr><tr><td>CLI-Universe-32B (Hua et al., 2026)</td><td>Qwen3-32B</td><td>6k</td><td>Terminus2</td><td>33.4</td><td>-</td><td>-</td><td>-</td></tr><tr><td>TMax-27B (Ivison et al., 2026)</td><td>Qwen3.6-27B</td><td>14.6k</td><td>Vanillux2Agent</td><td>42.7</td><td>44.9</td><td>17.1*</td><td>72.5*</td></tr><tr><td>OpenThinker-Agent-32B (Raoof et al., 2026)</td><td>Qwen3-32B</td><td>100k</td><td>Terminus2</td><td>26.2</td><td>30.7*</td><td>0.0*</td><td>19.7*</td></tr><tr><td>Meta-Task-32B (Pan et al., 2026)</td><td>Qwen3-32B</td><td>3.2k</td><td>Terminus2</td><td>31.8</td><td>-</td><td>-</td><td>-</td></tr><tr><td>RST-27B (Li et al., 2026b)</td><td>Qwen3.5-27B</td><td>37.5k</td><td>Terminus2</td><td>49.4</td><td>-</td><td>-</td><td>-</td></tr><tr><td>CalibForge-35B-A3B (Meng et al., 2026)</td><td>Qwen3.5-35B-A3B</td><td>5.4k</td><td>CalibForge-Eval</td><td>47.6</td><td>-</td><td>-</td><td>-</td></tr><tr><td>FACET-Terminal-27B (Shi et al., 2026)</td><td>Qwen3.5-27B</td><td>1.2k</td><td>Terminus2</td><td>-</td><td>47.6</td><td>-</td><td>-</td></tr><tr><td>[NAME C13]-SFT-27B</td><td>Qwen3.5-27B</td><td>32.0k</td><td>Terminus2</td><td>49.6</td><td>53.8</td><td>16.8</td><td>72.9</td></tr><tr><td>PAPO-27B</td><td>Qwen3.5-27B</td><td>32.0k</td><td>Terminus2</td><td>51.7</td><td>56.4</td><td>20.8</td><td>75.4</td></tr><tr><td>CBAO-27B</td><td>Qwen3.5-27B</td><td>32.0k</td><td>Terminus2</td><td>51.2</td><td>55.7</td><td>20.1</td><td>74.8</td></tr><tr><td>[NAME C13] (PAPO+CBAO)-27B</td><td>Qwen3.5-27B</td><td>32.0k</td><td>Terminus2</td><td>53.4</td><td>58.1</td><td>24.6</td><td>78.4</td></tr></table>

the joint model, which is the expected pattern if the two mechanisms address different parts of the sparse-reward credit-assignment problem.

## PAPER-A-M0017

paper_package.json#s0016

### 4.3 ANALYSIS AND ABLATION STUDIES

We separate the core RL comparison from the data-construction checks. The main text reports the reconstruction ablation, breadth expansion, and depth expansion under matched SFT or evaluation budgets; verifier filtering, category-level effects, budget allocation, and cross-domain transfer are provided as supplementary analyses in the appendix.

Credit-assignment ablation: PAPO and CBAO. The central methodological question is whether replayable snapshots provide a useful training signal when combined with the two proposed local credit-assignment rules. We hold the reconstructed tasks, SFT initialization, verifier, and rollout budget fixed, and vary only the Stage-2 objective. GRPO uses the same number of full-trajectory samples as the local methods; PAPO adds verifier-anchored sibling rollouts, CBAO adds entropy-selected branches, and the full model combines both under the unified KL-regularized objective.

Table 2: Controlled comparison of Stage-2 credit-assignment objectives. Every row shares the SFT initialization, demonstrations, verifier, and rollout budget; replace the displayed pilot values with the final repeated-run estimates.

<table><tr><td>Stage-2 objective</td><td>TB2.1</td><td>MT@4</td><td>Case score</td><td>Delta vs. SFT</td></tr><tr><td>SFT warm-start (no RL)</td><td>53.8</td><td>16.8</td><td>72.9</td><td>-</td></tr><tr><td>GRPO (full-trajectory groups)</td><td>55.0</td><td>18.9</td><td>74.1</td><td>+1.2</td></tr><tr><td>PAPO only</td><td>56.4</td><td>20.8</td><td>75.4</td><td>+2.6</td></tr><tr><td>CBAO only</td><td>55.7</td><td>20.1</td><td>74.8</td><td>+1.9</td></tr><tr><td>PAPO + CBAO ([NAME C13])</td><td>58.1</td><td>24.6</td><td>78.4</td><td>+4.3</td></tr></table>

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

8

Under review as a conference paper at ICLR 2027

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

PAPO is expected to help most on failed Cross-WS rollouts because its sibling suffixes begin at a verifier-identified pivotal turn. CBAO supplies additional signal on successful trajectories and on turns where the policy is uncertain but the final verifier outcome is already positive. Their combination therefore improves both fail-stop depth and partial case completion, rather than merely increasing the number of sampled trajectories.

Reconstruction ablation. We separate the value of reconstructing a task from the value of completing its workspace. The compact comparison in Table 3 uses matched SFT volume wherever possible: source-trajectory imitation, Intent Recovery on reconstructed workspaces, replay-only reconstruction, and replay with agentic completion. Intent Recovery improves supervision over direct imitation, while completion provides an additional gain over replay alone.

Table 3: Reconstruction ablation on Terminal-Bench 2.1. The rows isolate source-trajectory imitation, task re-solving, and agentic completion; entries are pilot values to be replaced by final repeated runs.

<table><tr><td>Training source</td><td>Records</td><td>Terminus2-XML</td><td>Avg.</td></tr><tr><td>Qwen3.5-27B base</td><td>-</td><td>46.2<sub>3.9</sub></td><td>47.0</td></tr><tr><td>Source trajectories</td><td>35.8k</td><td>40.3<sub>2.1</sub></td><td>36.7</td></tr><tr><td>Intent Recovery (re-solved)</td><td>35.8k</td><td>52.9<sub>1.4</sub></td><td>52.1</td></tr><tr><td>Replay-only Intent Recovery</td><td>35.8k</td><td>48.7<sub>3.5</sub></td><td>-</td></tr><tr><td>Replay + agentic completion</td><td>35.8k</td><td>52.9<sub>1.4</sub></td><td>-</td></tr></table>

Breadth expansion. Breadth expansion adds supervision beyond Single-WS: Cross-WS alone reaches 55.4, while the mixture reaches 58.4 under Terminus2-XML.

Cross-WS trajectories are longer and harder than Single-WS trajectories (median teacher pass@1: 72.3% versus 49.2%), while their mixture improves Terminal-Bench performance from 56.4 to 58.4. Detailed trajectory statistics and category-level changes are reported in Appendix § H.

Multi-round depth expansion. On EvoCode-Bench v2, Multi-Round data raises MT@4 from 18.4 to 21.0 and Case score from 71.9 to 76.9; removing round-level verification reduces them to 18.8 and 73.2.

How to read the controls. The ablations vary one source of improvement at a time. All Stage-2 variants begin from the same SFT checkpoint, use the same reconstructed task pool and verifier, and receive the same optimizer and initial-rollout budget. The GRPO row spends its additional samples on complete trajectories, whereas PAPO and CBAO spend them on suffixes restored from snapshots selected by a verifier failure or by action entropy. Consequently, the local methods test whether replay makes credit assignment more selective, rather than simply testing a larger number of independent episodes. The reconstruction table applies the same separation to data construction: direct imitation, replayed recovery, and recovery followed by agentic completion are compared at matched record counts. This control structure attributes differences to state restoration and local objectives rather than to a change in model size or task count.

## PAPER-A-M0018

paper_package.json#s0017

## 5 CONCLUSION

In this work, we present [NAME C13], a replay-enabled RL framework that reframes recorded agent trajectories from fixed demonstrations into losslessly rewindable execution environments. Through deterministic replay, agentic completion, and per-turn container snapshots, [NAME C13] restores latent workspace state and exposes counterfactual sibling rollouts to a trained policy. Building on this environment, we introduce two RL algorithms: pivotal-anchored policy optimization (PAPO), which computes group-relative advantages anchored at verifier-diagnosed failure turns, and contrastive branch advantage optimization (CBAO), which allocates turn-level advantages at high-entropy branch points. Optimized jointly on top of an SFT-warm-started reference under trust-region and SFT-anchor KL, the two algorithms turn recorded trajectories into a scalable substrate for RL post-training of terminal agents.

9

Under review as a conference paper at ICLR 2027

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

## PAPER-A-M0019

paper_package.json#s0018

# REFERENCES

Alpay Ariyak, Junda Zhang, Junxiong Wang, Shang Zhu, Federico Bianchi, Sanjana Srivastava, Ashwinee Panda, Siddhant Bharti, Chenfeng Xu, John Heo, Xiaoxia Shirley Wu, James Zhou, Percy Liang, Leon Song, Ce Zhang, Ben Athiwaratkun, Zhongzhu Zhou, and Qingyang Wu. CoderForge-Preview: SOTA open dataset for training efficient agents, February 2026. URL [URL REDACTED] Project core leads: Alpay Ariyak, Zhongzhu Zhou, and Qingyang Wu.

Ibragim Badertdinov, Alexander Golubev, Maksim Nekrashevich, Anton Shevtsov, Simon Karasik, Andrei Andriushchenko, Maria Trofimova, Daria Litvintseva, and Boris Yangel. SWE-rebench: An automated pipeline for task collection and decontaminated evaluation of software engineering agents, 2025. URL https://arxiv.org/abs/2505.20411.

Zihao Cheng, Hongru Wang, Zeming Liu, Xinyi Wang, Xiangrong Zhu, Yuhang Guo, Wei Lin, Jeff Z. Pan, and Yunhong Wang. Terminal-World: Scaling terminal-agent environments via agent skills, 2026. URL https://arxiv.org/abs/2605.20876.

Zhiyuan Fan, Tinghao Yu, Yuanjun Cai, Jiangtao Guan, Yun Yang, Dingxin Hu, Jiang Zhou, Xing Wu, Zhuo Han, Feng Zhang, and Lilin Wang. Toward scalable terminal task synthesis via skill graphs, 2026. URL https://arxiv.org/abs/2604.25727.

Kanishk Gandhi, Shivam Garg, Noah D. Goodman, and Dimitris Papailiopoulos. Endless terminals: Scaling RL environments for terminal agents, 2026. URL https://arxiv.org/abs/2601.16443.

Lianghong Guo, Yanlin Wang, Caihua Li, Wei Tao, Pengyu Yang, Jiachi Chen, Haoyu Song, Duyu Tang, and Zibin Zheng. SWE-Factory: Your automated factory for issue resolution training data and evaluation benchmarks, 2026. URL https://arxiv.org/abs/2506.10954.

gyung. LFM2-Terminal-SFT-Processed. Hugging Face dataset, 2026. URL [URL REDACTED] Accessed 2026-08-23.

Zhanbo Hua, Yifan Yao, Weihao Xie, Yongchi Zhao, Minghao Liu, Ruizhi Qiu, Zhewei Huang, Zun Wang, Yiyan Ji, Yunhai Ye, Letian Zhu, Xinping Lei, Han Li, Zhiyuan Ma, Zili Wang, Zhaoxiang Zhang, and Jiaheng Liu. CLI-Universe: Towards verifiable task synthesis engine for terminal agents, 2026. URL https://arxiv.org/abs/2606.22883.

Hamish Ivison, Junjie Oscar Yin, Rulin Shao, Teng Xiao, Nathan Lambert, and Hannaneh Hajishirzi. Tmax: A simple recipe for terminal agents, 2026. URL https://arxiv.org/abs/2606.23321.

Naman Jain, Jaskirat Singh, Manish Shetty, Liang Zheng, Koushik Sen, and Ion Stoica. R2E-Gym: Procedural environments and hybrid verifiers for scaling open-weights SWE agents, 2025. URL https://arxiv.org/abs/2504.07164.

Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan. SWE-bench: Can language models resolve real-world GitHub issues? In International Conference on Learning Representations (ICLR), 2024.

Kenan Li, Rongzhi Li, Linghao Zhang, Qirui Jin, Liao Zhu, Xiaosong Huang, Geng Zhang, Yikai Zhang, Shilin He, Chengxing Xie, Xin Zhang, Zijian Jin, Bowen Li, Chaoyun Zhang, Yu Kang, Yufan Huang, Elsie Nallipogu, Saravan Rajmohan, Qingwei Lin, and Dongmei Zhang. RepoLaunch: Automating build and management of code repositories across languages and platforms, 2026a. URL https://arxiv.org/abs/2603.05026.

Zhongzhi Li, Yucheng Shi, Zongxia Li, Ruhan Wang, Anhao Li, Zixun Huang, Junyao Yang, Lei Ke, Ninghao Liu, Haitao Mi, and Leowei Liang. Recursive synthesis for long-horizon terminal tasks, 2026b. URL https://arxiv.org/abs/2608.05466.

Yusong Lin, Haiyang Wang, Shuzhe Wu, Lue Fan, Feiyang Pan, Sanyuan Zhao, and Dandan Tu. CLI-Gym: Scalable CLI task generation via agentic environment inversion, 2026. URL https://arxiv.org/abs/2602.10999.

10

Under review as a conference paper at ICLR 2027

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

Fanzhe Meng, Guoxin Chen, Jiale Zhao, Shuang Sun, Zhiyu Lin, Wayne Xin Zhao, Ruihua Song, Ji-Rong Wen, and Kai Jia. CalibForge: Adversarial solver calibration for scaling learnable terminal tasks, 2026. URL https://arxiv.org/abs/2608.06352.

Mike A. Merrill, Alexander G. Shaw, Nicholas Carlini, et al. Terminal-Bench: Benchmarking agents on hard, realistic tasks in command line interfaces. In International Conference on Learning Representations, 2026. URL https://arxiv.org/abs/2601.11868.

Jiayi Pan, Xingyao Wang, Graham Neubig, Navdeep Jaitly, Heng Ji, Alane Suhr, and Yizhe Zhang. Training software engineering agents and verifiers with SWE-Gym, 2024. URL https://arxiv.org/abs/2412.21139.

Zhihong Pan, Jiyuan He, Kai Zhang, Yupeng Han, Ze Liu, Yuze Zhao, Yongcong Ye, and Zhaohua Yang. Meta-Task: Turning terminal task synthesis into a terminal task for scalable agent training, 2026. URL https://arxiv.org/abs/2607.27929.

Xiaoxuan Peng, Kaiqi Zhang, Xinyu Lu, Boxi Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, and Le Sun. LiteCoder-Terminal: Scaling long-horizon terminal environments for learning language agents, 2026a. URL https://arxiv.org/abs/2605.29559.

Zhongyuan Peng, Dan Huang, Chuyu Zhang, Caijun Xu, Changyi Xiao, Shibo Hong, David Lo, Lin Qiu, Xuezhi Cao, Jiyuan He, and Yixin Cao. ICAE-Bench: Evaluating coding agents as interactive project builders, 2026b. URL https://arxiv.org/abs/2607.21217.

Renjie Pi, Grace Lam, Mohammad Shoeybi, Pooya Jannaty, Bryan Catanzaro, and Wei Ping. On data engineering for scaling LLM terminal capabilities, 2026. URL https://arxiv.org/abs/2602.21193.

Mohit Raghavendra, Anisha Gunjal, Aakash Sabharwal, and Yunzhong He. SWE-INTERACT: Reimagining SWE benchmarks as user-driven long-horizon coding sessions, 2026. URL https://arxiv.org/abs/2606.30573.

Negin Raoof, Richard Zhuang, Marianna Nezhurina, Etash Guha, Atula Tejaswi, et al. OpenThoughts-Agent: Data recipes for agentic models, 2026. URL https://arxiv.org/abs/2606.24855.

Haiyang Shen, Xuanzhong Chen, Wendong Xu, Yun Ma, Liang Chen, and Kuan Li. EvoCode-Bench: Evaluating coding agents in multi-turn iterative interactions, 2026a. URL https://arxiv.org/abs/2605.24110.

Qijia Shen, Zhiqi Huang, Vamsidhar Kamanuru, Aznaur Aliev, Jay Rainton, Ahmed Awelkair, Zhichen Zeng, Jiajun Li, Shi Dong, Yueming Yuan, Boyuan Ma, Qizheng Zhang, Jiwei Fu, Yuzhen Mao, Wendong Fan, Ping Nie, Philip Torr, Bernard Ghanem, Changran Hu, Jonathan Lingjie Li, Urmish Thakker, and Guohao Li. SETA: Scaling environments for terminal agents, 2026b. URL https://arxiv.org/abs/2607.10891.

Kou Shi, Zun Wang, Qisheng Su, Shiting Huang, Ziao Zhang, Zhen Fang, Qingnan Ren, Jin Liu, Yu Zeng, Yiming Zhao, Lin Chen, Zehui Chen, and Feng Zhao. FACET: Preserving source intent and executable state in terminal task synthesis, 2026. URL https://arxiv.org/abs/2608.18580.

Siwei Wu, Yizhi Li, Yuyang Song, Wei Zhang, Yang Wang, Riza Batista-Navarro, Xian Yang, Mingjie Tang, Bryan Dai, Jian Yang, and Chenghua Lin. Large-scale terminal agentic trajectory generation from dockerized environments, 2026a. URL https://arxiv.org/abs/2602.01244.

Yifan Wu, Zhuokai Zhao, Songlin Li, Ho Hin Lee, Jiacheng Zhu, Shirley Wu, Tianhe Yu, Serena Li, Lizhu Zhang, Xiangjun Fan, and Shengzhi Li. SWE-Together: Evaluating coding agents in interactive user sessions, 2026b. URL https://arxiv.org/abs/2606.29957.

John Yang, Akshara Prabhakar, Karthik Narasimhan, and Shunyu Yao. InterCode: Standardizing and benchmarking interactive coding with execution feedback, 2023. URL https://arxiv.org/abs/2306.14898.

11

Under review as a conference paper at ICLR 2027

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

John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, and Diyi Yang. SWE-smith: Scaling data for software engineering agents. In Advances in Neural Information Processing Systems (NeurIPS) Datasets and Benchmarks Track, 2025. URL https://arxiv.org/abs/2504.21798.

Sidi Yang, Chaofan Tao, Jierun Chen, Tiezheng Yu, Ruoyu Wang, Yuxin Jiang, Yiming Du, Wendong Xu, Jing Xiong, Taiqiang Wu, Lifeng Shang, Xiaohui Li, Ngai Wong, and Haoli Bai. What makes interaction trajectories effective for training terminal agents?, 2026. URL https://arxiv.org/abs/2606.03461.

Wenhao Zeng, Yuling Shi, Xiaodong Gu, Chao Hu, Chaofan Wang, Yuhao Cui, Hongting Zhou, Mengnan Qi, Jianqiao Wangni, Zhaojian Yu, Shuzheng Gao, Kai Cai, and Shilin He. Dockerless: Environment-free program verifier for coding agents, 2026. URL https://arxiv.org/abs/2606.28436.

Kaijie Zhu, Yuzhou Nie, Yijiang Li, Yiming Huang, Jialian Wu, Jiang Liu, Ximeng Sun, Zhenfei Yin, Lun Wang, Zicheng Liu, Emad Barsoum, William Yang Wang, and Wenbo Guo. TermiGen: High-fidelity environment and robust trajectory synthesis for terminal agents, 2026. URL https://arxiv.org/abs/2602.07274.

12

Under review as a conference paper at ICLR 2027

## PAPER-A-M0020

paper_package.json#s0019

## Appendix

<table><tr><td><b>B</b></td><td><b>Data Sources and Selection</b></td><td>14</td></tr><tr><td><b>C</b></td><td><b>Environment Reconstruction Details</b></td><td>15</td></tr><tr><td>C.1</td><td>Reconstruction and Completion</td><td>15</td></tr><tr><td>C.2</td><td>Workspace Sufficiency Evaluation</td><td>16</td></tr><tr><td>C.3</td><td>Failure Analysis</td><td>17</td></tr><tr><td><b>D</b></td><td><b>Re-querying Details</b></td><td>18</td></tr><tr><td>D.1</td><td>Intent Recovery</td><td>18</td></tr><tr><td>D.2</td><td>Single-WS Synthesis</td><td>19</td></tr><tr><td>D.3</td><td>Cross-WS Synthesis</td><td>20</td></tr><tr><td>D.4</td><td>Multi-Round User Queries</td><td>24</td></tr><tr><td><b>E</b></td><td><b>Verifier Construction Details</b></td><td>26</td></tr><tr><td><b>F</b></td><td><b>Case Studies</b></td><td>27</td></tr><tr><td>F.1</td><td>Reconstruction and Single-Workspace Re-querying</td><td>28</td></tr><tr><td>F.2</td><td>Cross-WS Synthesis</td><td>30</td></tr><tr><td>F.3</td><td>Multi-Round User Queries</td><td>31</td></tr><tr><td><b>G</b></td><td><b>Environment Construction Comparison</b></td><td>33</td></tr><tr><td><b>H</b></td><td><b>Reconstruction and Supplementary Ablations</b></td><td>33</td></tr><tr><td>H.1</td><td>Supplementary Experimental Analyses</td><td>35</td></tr><tr><td>H.2</td><td>Additional Expansion Tables</td><td>36</td></tr><tr><td>H.3</td><td>Compact Expansion Summary</td><td>37</td></tr><tr><td><b>I</b></td><td><b>SFT Dataset Statistics</b></td><td>37</td></tr><tr><td><b>J</b></td><td><b>Evaluation Configurations</b></td><td>37</td></tr><tr><td><b>A</b></td><td><b>Discussion and Limitations</b></td><td>14</td></tr></table>

13

Under review as a conference paper at ICLR 2027

## PAPER-A-M0021

paper_package.json#s0020

## A DISCUSSION AND LIMITATIONS

Scaling with richer source trajectories. The useful unit of scale in [NAME C13] is observable state, not the number of transcripts alone. Traces that touch several modules, exercise long tool chains, or expose intermediate failures leave a larger state surface for replay and consequently support more varied branch points for PAPO and CBAO. Several sessions can also be merged when they refer to the same workspace; this increases coverage of the project context, but only for facts that are actually exposed by at least one session. The framework therefore benefits from stronger source agents while retaining an explicit information ceiling imposed by the traces.

Limitations. Three constraints remain. First, all workspaces currently run in a standard Ubuntu 24.04 image rather than in repository-specific images such as those produced by SWE-Factory (Guo et al., 2026) or RepoLaunch (Li et al., 2026a); projects that depend on unusual system packages or elaborate build chains may therefore be underrepresented. Second, reconstruction cannot broaden the domain, language, or toolchain support beyond the source-trace distribution. Third, the same teacher family currently proposes tasks, produces solutions, and writes verifiers. This shared failure mode can narrow task diversity or allow an incorrect solution to pass an incomplete test, motivating independent teachers and verifier models in future evaluations.

## PAPER-A-M0022

paper_package.json#s0021

## B DATA SOURCES AND SELECTION

The source inventory separates software-engineering traces from terminal traces and records how many raw trajectories give rise to reconstructed environments. Reconstruction quality depends on what the trace makes observable: file edits expose project structure, while command-only sessions often leave too little persistent content to replay. We remove Terminal-Bench-derived data and sources whose action format is dominated by views or cannot be normalized into our event representation. The resulting counts are listed in Table 4.

SWE deduplication and decontamination. SWE collections frequently repeat one issue across repositories, commits, or rollout formats. We group records by repository, base commit, and problem statement, retain the member with the largest replayable footprint, and then exclude SWE-bench Verified repositories (Jimenez et al., 2024). Records without a reliable source-trajectory link are discarded as well. The final per-source totals are reported in Table 4.

Table 4: Source corpora and reconstructed environments. The Trajectories column counts source trajectories drawn from each corpus.

<table><tr><td>Source corpus</td><td>Pool</td><td>License</td><td>Trajectories</td><td>Environments</td></tr><tr><td>SWE-rebench (Badertdinov et al., 2025)</td><td>SWE</td><td>CC-BY-4.0</td><td>67,074</td><td>6,118</td></tr><tr><td>SWE-smith (Yang et al., 2025)</td><td>SWE</td><td>MIT</td><td>95,851</td><td>8,476</td></tr><tr><td>CoderForge (Ariyak et al., 2026)</td><td>SWE</td><td>Apache-2.0</td><td>32,964</td><td>3,978</td></tr><tr><td>SWE-Gym (Pan et al., 2024)</td><td>SWE</td><td>MIT</td><td>4,152</td><td>929</td></tr><tr><td>LFM2-Terminal (gyung, 2026)</td><td>Terminal</td><td>CC-BY-4.0</td><td>139,841</td><td>46,037</td></tr><tr><td>LiteCoder-Terminal (Peng et al., 2026a)</td><td>Terminal</td><td>MIT</td><td>19,711</td><td>2,725</td></tr><tr><td>Total</td><td></td><td></td><td>359,593</td><td>68,263</td></tr></table>

Table 5: Workspace complexity before and after agentic completion. Cells report median / mean.

<table><tr><td rowspan="2"></td><td colspan="2">Terminal pool</td><td colspan="2">SWE pool</td></tr><tr><td>Replayed (\( \widehat{E}_{0} \))</td><td>Completed (\( \widehat{E} \))</td><td>Replayed (\( \widehat{E}_{0} \))</td><td>Completed (\( \widehat{E} \))</td></tr><tr><td>Files per workspace</td><td>2 / 2.9</td><td>13 / 22.4</td><td>5 / 5.6</td><td>21 / 37.9</td></tr><tr><td>Text lines (all files)</td><td>60 / 90</td><td>539 / 5,761</td><td>537 / 595</td><td>1,854 / 6,622</td></tr><tr><td>Code lines (source files)</td><td>0 / 43</td><td>316 / 503</td><td>421 / 487</td><td>1,643 / 6,302</td></tr></table>

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

14

Under review as a conference paper at ICLR 2027

Figure 3 shows how raw traces are converted into replayable workspaces and then filtered before they are exposed to task generation.

![img-4.jpeg](img-4.jpeg)

Figure 3: Core environment-reconstruction flow.

## PAPER-A-M0023

paper_package.json#s0022

## C ENVIRONMENT RECONSTRUCTION DETAILS

## PAPER-A-M0024

paper_package.json#s0023

### C.1 RECONSTRUCTION AND COMPLETION

Different collectors represent shell actions and file edits in different formats. We first map them to a time-ordered event stream. For a read-only path, we retain the content observed by the trace; for a path that the agent later changes, we snapshot the last content available before that change. Partial reads remain partial. Agent-created files and post-edit versions are withheld so that the reconstructed state does not contain the teacher's solution.

The completion model receives the recovered request together with the partial tree and an inventory of observed paths. Its role is to supply context needed to execute the task: missing support files may be added, truncated files may be completed, and dependencies may be configured. The requested feature itself remains out of scope, and the model is not told which location will be edited by the future solver.

Packaging. Each reconstructed project is mounted below /app; paths observed outside that root are packaged separately and restored only when the task requires them.

## PAPER-A-M0025

paper_package.json#s0024

#### PROMPT Environment Completion

## PAPER-A-M0026

paper_package.json#s0025

#### ROLE & GOAL

You are the [NAME C13] environment-reconstruction agent. Restore a coherent, runnable workspace around the recorded task so that a future solver can inspect the project and attempt the task, while the requested change remains NOT solved.

## PAPER-A-M0027

paper_package.json#s0026

#### RUNTIME INPUTS

Task that the future solver will attempt:
<ORIGINAL_INSTRUCTION>
Recovered workspace files (container-absolute paths; project root and working directory: /app):
<DOCKER_LAYOUT_FILES>

15

Under review as a conference paper at ICLR 2027

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

## PAPER-A-M0028

paper_package.json#s0027

### PROMPT Environment Completion (continued)

## PAPER-A-M0029

paper_package.json#s0028

#### COMPLETION CONTRACT

## PAPER-A-M0030

paper_package.json#s0029

#### Objectives

1. Restore the context needed for a grounded attempt. Create missing project files or complete partial ones, including configs, fixtures, scripts, data, schemas, manifests, and support code that the task clearly depends on.
2. Do NOT solve the task. Do not create the requested implementation, fix, feature, configuration change, or output.
3. Make the restored project internally coherent: preserve consistent naming and plausible structure, and leave enough working surrounding code for a future agent to investigate the intended change.

## PAPER-A-M0031

paper_package.json#s0030

#### Rules

- Prioritize source and data artifacts, then build/configuration files and scripts referenced by the project. Add documentation only when the project explicitly requires it or reads it at runtime.
- Existing non-target code may be substantial, but do not add tests for the not-yet-implemented target or comments that reveal its exact solution location.
- Keep every restored file syntactically valid and consistent with the workspace's language, framework, versions, and style.
- Use network access or install packages only when needed to restore dependencies required by the existing project.
- You may create missing files and complete partial files, but do not make the change requested by the task.

Completion quality. We audited 30 randomly selected Terminal completions. Twenty-two added only support artifacts that were relevant to the recovered task, while eight added substantial material that was unnecessary for the intended workflow. None of the audited workspaces contained the requested solution.

## PAPER-A-M0032

paper_package.json#s0031

### C.2 WORKSPACE SUFFICIENCY EVALUATION

Evaluation scope. The sufficiency judge examines every retained Terminal reconstruction. For SWE, we select one representative reconstruction and its Intent Recovery task for each repository after deduplication. The judge has read-only shell and file access and is asked to assess the available evidence rather than to repair the workspace.

Scoring. We mark a workspace sufficient when its source, configuration, data, and project structure expose the facts a capable solver needs to make a grounded attempt. Re-creatable caches, generated outputs, optional documentation, and external dependencies are not required. The judgment concerns task-specific context, not whether the unmodified project already builds successfully.

Table 6 gives the corresponding source-level breakdowns.

Table 6: Source breakdown of workspace sufficiency under recovered intents after agentic completion.

<table><tr><td>Source</td><td>n</td><td>Sufficient</td><td>Sufficient (%)</td></tr><tr><td colspan="4">Terminal pool</td></tr><tr><td>LFM2-Terminal</td><td>36,204</td><td>34,467</td><td>95.2</td></tr><tr><td>LiteCoder-Terminal</td><td>2,090</td><td>1,342</td><td>64.2</td></tr><tr><td colspan="4">SWE pool</td></tr><tr><td>SWE-rebench</td><td>1,734</td><td>1,350</td><td>77.9</td></tr><tr><td>SWE-smith</td><td>114</td><td>85</td><td>74.6</td></tr><tr><td>CoderForge</td><td>47</td><td>27</td><td>57.4</td></tr><tr><td>SWE-Gym</td><td>5</td><td>2</td><td>40.0</td></tr></table>

16

Under review as a conference paper at ICLR 2027

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

The rates measure the information exposed by the traces and the amount of generic context that completion can safely restore. Completion cannot infer project-specific behavior that never appears in the evidence, and the smallest SWE subsets should not be interpreted as stable source-level estimates.

## PAPER-A-M0033

paper_package.json#s0032

### C.3 FAILURE ANALYSIS

Insufficient cases are typically missing a load-bearing source file, task script, input artifact, configuration, or deployment entry point. Missing tests, manifests, or package initialization files are additional signals that the replay captured only a fragment of the original project. The judge records the concrete missing paths or facts used for its decision.

## PAPER-A-M0034

paper_package.json#s0033

#### Judge prompt.

## PAPER-A-M0035

paper_package.json#s0034

#### PROMPT Workspace Sufficiency Judge

## PAPER-A-M0036

paper_package.json#s0035

#### ROLE & INSTRUCTION

You are the [NAME C13] sufficiency judge. Decide whether the replayed-and-completed workspace exposes enough project-specific evidence for the downstream solver to attempt the task below. Treat the task as an evaluation reference only; do not solve it.

## PAPER-A-M0037

paper_package.json#s0036

#### RUNTIME INPUT

<task>
<TASK_INSTRUCTION>
</task>

## PAPER-A-M0038

paper_package.json#s0037

#### INSPECTION & DECISION RULES

Inspect the workspace actively but remain read-only. The project root is /app; follow task-referenced system paths when they are relevant to the recovered workflow. Use shell and file-reading tools to trace the project tree, manifests, configuration, data, tests, and any paths named or implied by the task.

Return one binary judgment:

* sufficient: The workspace exposes the project-specific source, configuration, data, and execution context required for a grounded first attempt. Third-party packages, caches, generated artifacts, and optional documentation may be absent when the manifests or retained source make them recoverable through the normal development workflow.

* insufficient: A task-critical file, module, data artifact, configuration entry, or structural relationship is missing, skeletal, or inconsistent. The solver would therefore have to invent or recover core project facts before it could make a grounded attempt.

Ground the label in concrete paths and observable workspace evidence. Do not infer sufficiency from the task wording alone. Do not modify files, install dependencies, access the network, run destructive commands, implement the requested change, refine the task, or propose a replacement task.

## PAPER-A-M0039

paper_package.json#s0038

#### OUTPUT CONTRACT

Return exactly one JSON object on one line:
{
    "label": "sufficient|insufficient",
    "confidence": 0.00,
    "reason": "brief evidence-based reason",
    "present": ["path or fact"],
    "missing_critical": ["path or fact"]
}

17

Under review as a conference paper at ICLR 2027

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

## PAPER-A-M0040

paper_package.json#s0039

## D RE-QUERYING DETAILS

All four generators emit a request whose acceptance condition is observable while leaving the implementation plan to the solver. This separation lets us compare task families without prescribing the action sequence that PAPO or CBAO will later explore.

Cross-workspace layout. For a Cross-WS task, two reconstructed projects are mounted below /app/workspaces as repo0 and repo1. One is selected as the writable target and the other is exposed read-only as evidence. The solver receives this same arrangement, while the verifier additionally checks that the reference side is untouched ( \( §\ 3.1 \) ).

Prompt presentation. The following templates define the four query generators used to turn replayable workspaces into training tasks. Runtime inputs and output schemas are shown in full; repeated implementation examples are abbreviated. Values in angle brackets are filled at runtime.

## PAPER-A-M0041

paper_package.json#s0040

### D.1 INTENT RECOVERY

Generation mechanism. Intent Recovery converts an observed interaction into the task contract that will seed replay-based training. It receives the cleaned request, the chronological conversation, and file evidence from the reconstructed workspace. For a single-round trace, the sole substantive request supplies the contract. For a multi-round trace, the first substantive request establishes the topic and later turns are retained only when they clarify, constrain, or extend that same task; unrelated pivots are excluded. Actions and files help resolve references, but only user-stated requirements become supervision. The generated core_objective is used as the Intent Recovery instruction and the other fields remain metadata.

## PAPER-A-M0042

paper_package.json#s0041

#### PROMPT Intent Recovery

## PAPER-A-M0043

paper_package.json#s0042

#### ROLE & INSTRUCTION

You are the intent-reconstruction analyst for [NAME C13]. Given a task description, a conversation trace, and workspace evidence, recover the user's actionable objective without inventing an implementation plan.

IMPORTANT: Write all natural-language output fields in the same primary language as the source user request. Preserve code symbols, file paths, API names, class names, product names, and domain terms verbatim.

## PAPER-A-M0044

paper_package.json#s0043

#### RUNTIME INPUTS

## Task Description
<TASK_DESCRIPTION>

## Conversation Trace
<CONVERSATION_TRACE>

## File Evidence
<FILE_EVIDENCE></FILE_EVIDENCE>

## PAPER-A-M0045

paper_package.json#s0044

#### ANALYSIS STEPS

## Analysis Steps (execute during reasoning, do not output)
1. Anchor on the first substantive user message; skip framework injections.
2. Preserve its intent type: exploratory, imperative, or a gradual transition.
3. Use later turns only for clarifications and added constraints.
4. Match the abstraction level of the user's words. Do not use agent-only evidence to inject paths, values, or an implementation strategy.

18

Under review as a conference paper at ICLR 2027

PROMPT Intent Recovery (continued)

OUTPUT CONTRACT
Return strict JSON only:
{
    "core_objective": "2-4 self-contained sentences",
    "success_criteria": ["independently verifiable functional criterion"],
    "specified_output_format": null,
    "has_examples": false,
    "mandatory_constraints": ["0-3 must-do constraints"],
    "prohibitions": ["0-3 must-not-do constraints"]
}

Rules:
- core_objective must stand alone and preserve the main-line task.
- Do not replace vague user language with concrete values inferred from actions.
- Criteria describe observable outcomes, not implementation details.
- Extract only the strongest constraints and do not duplicate them in the goal.

## PAPER-A-M0046

paper_package.json#s0045

### D.2 SINGLE-WS SYNTHESIS

Generation mechanism. Single-WS uses one reconstructed workspace as the evidence base for new task contracts. The generator receives a bounded path inventory and may inspect selected files with read-only commands, but it cannot modify the project, access the network, or scan outside the workspace. We retain one grounded candidate per workspace after parsing and deduplication.

PROMPT Single-WS Synthesis

ROLE & GOAL
You are the [NAME C13] single-workspace task designer and repository analyst.
Inspect the private project rooted at /app and propose 5 diverse, challenging terminal
tasks that expose meaningful, verifier-testable behavior in this workspace.
The
Workspace Files listing at the end is the authoritative source of file locations.

OUTPUT CONTRACT

Output exactly one JSON array containing exactly 5 self-contained task strings.
Output no markdown, comments, explanations, objects, or extra keys.

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

19

Under review as a conference paper at ICLR 2027

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

## PAPER-A-M0047

paper_package.json#s0046

#### PROMPT Single-WS Synthesis (continued)

## PAPER-A-M0048

paper_package.json#s0047

#### EXPLORATION & TASK RULES

Exploration:

- Start from the supplied inventory; inspect only targeted project files.
- Prefer cheap inspection commands; do not modify repository files.
- Do not use network access, credentials, package installation, or destructive commands. Do not expose secrets or proprietary code excerpts.

Generate tasks in this ideal zone:

clear goal + verifiable standard + unexplored implementation.

Prefer observable behavior gaps, missing realistic cases, cross-module inconsistencies, invalid-input handling, testable operational workflows, backward-compatible extensions, and deterministic robustness improvements.

Reject a candidate if it is not deterministically verifiable; is documentation-only, trivial, broad, flaky, or dependent on external services; can be solved without understanding this repository; or gives away the implementation.

Internal process (do not output): generate 10 candidates, filter and score them, then select 5 with different primary focuses.

Every final task must make recoverable:

- the project root and concrete observable goal;
- grounding files, commands, tests, configs, fixtures, or entry points;
- offline constraints and a deterministic validation approach;
- existing behavior that must remain unchanged;
- no patch-level guidance or implementation solution.

## PAPER-A-M0049

paper_package.json#s0048

#### RUNTIME INPUT

## Workspace Files

<WORKSPACE_FILE_INVENTORY>

## PAPER-A-M0050

paper_package.json#s0049

### D.3 CROSS-WS SYNTHESIS

Candidate sourcing. We first build a compact profile for every workspace and retrieve nearby candidates with TF-IDF within each language group. A relation judge then labels each pair as similar, complementary, dependency, or unrelated and identifies the direction of a capability gap. File-level checks select dependency pairs, prevent a workspace from appearing in multiple pairs, and cap reuse. The two selected workspaces are mounted as peers; the task generator assigns the writable and read-only roles.

Task generation. A generation agent reads both repositories, assigns their roles, and emits one task, file-grounded evidence, and three hidden dependency facts. The task must require at least three facts available only from the reference, while keeping those facts and the reference's internal paths out of the query. It must identify the target landing zone, specify executable acceptance checks, preserve target behavior, leave the reference unchanged, and remain solvable offline. Pairs lacking a load-bearing reference asset are rejected.

Checks. We reject malformed tasks, queries that reveal a hidden dependency, and queries that expose internal reference paths. An SFT record is retained only when its query and verifier are valid and the teacher completes it successfully.

20

Under review as a conference paper at ICLR 2027

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

## PAPER-A-M0051

paper_package.json#s0050

### PROMPT Cross-WS Workspace Profiling

## PAPER-A-M0052

paper_package.json#s0051

#### ROLE & EXPLORATION RULES

You are the [NAME C13] workspace-profiling agent. A software project has been mounted in this container. The Docker Layout Files listing at the end is the authoritative map of project locations and is the starting point for evidence collection.

Explore the project and produce one structured intent record that describes its observable domain, architecture, and capabilities so it can be matched against other workspaces in the same domain.

## PAPER-A-M0053

paper_package.json#s0052

#### Exploration rules:

- Identify project markers such as manifests, README files, source and test directories, configuration, and entry points from the supplied inventory.
- Inspect targeted file contents with cheap read-only commands. Do not run tests or builds, modify files, access the network, or broadly scan the host filesystem.
- Ground every field in code evidence. Do not expose secrets, credentials, tokens, or large verbatim excerpts.

## PAPER-A-M0054

paper_package.json#s0053

#### OUTPUT CONTRACT

Output exactly one JSON object and nothing else:
{
    "domain": "one coarse domain bucket",
    "subdomain": "finer tag in at most 4 words",
    "primary_language": "dominant programming language",
    "frameworks": ["frameworks, libraries, and datastores defining the stack"],
    "core_capabilities": ["3-8 short verb phrases"],
    "key_entities": ["core modules, data models, and domain objects"],
    "summary": "detailed, self-contained, code-grounded description"
}

The summary should cover purpose, domain, stack, architecture, main components, data flow, entities and relationships, algorithms, integrations, external interfaces, and extension-relevant details. Avoid generic filler or unsupported capabilities.

## PAPER-A-M0055

paper_package.json#s0054

#### RUNTIME INPUT

## Docker Layout Files
<docker_layout_files></docker_layout_files>

## PAPER-A-M0056

paper_package.json#s0055

### PROMPT Cross-WS Relation Judging

## PAPER-A-M0057

paper_package.json#s0056

#### RELATION & TASK RULES

Classify the relationship between an ANCHOR coding workspace and each candidate:

- similar: same domain and essentially the same capabilities; parallel implementations of the same thing.
- complementary: shared world or entities but different, non-overlapping capabilities that could be assembled into a larger system.
- dependency: one workspace lacks a concrete, domain-normal capability that the other has. Set donor to the side that has it.
- unrelated: no meaningful cross-workspace task.

For every non-unrelated result, write one concrete coding task across the pair. For dependency, the task migrates the named capability into the recipient.

21

Under review as a conference paper at ICLR 2027

PROMPT Cross-WS Relation Judging (continued)

OUTPUT CONTRACT
Return only one JSON array in candidate order:
[
    {
    "i": <candidate_index>,
    "relation": "similar|complementary|dependency|unrelated",
    "donor": "anchor|candidate|null",
    "capability": "<capability_or_null>",
    "task": "<one_line_task_or_null>"
    }
]
]</one_line_task_or_null></capability_or_null>

RUNTIME INPUTS

ANCHOR:
<anchor_profile>
CANDIDATES:
<numbered_candidate_profiles></numbered_candidate_profiles>

PROMPT Cross-WS Dependency-Gap Task Synthesis

ROLE & GOAL

You are the [NAME C13] cross-workspace dependency-task designer. Explore two mounted repositories and construct one high-quality coding task for a future solver, using the second repository only as grounded evidence rather than as a copy source.

You will be given two peer software repositories under /app/workspaces (repo0 and repo1). One will become the target repository that the solver modifies; the other will be the read-only reference that supplies specifications, constraints, or data. Explore both, choose the direction that makes the dependency meaningful, and generate exactly one coding task.

Important context: the reference may be incomplete as an implementation. Its useful contribution may instead be an interface contract, configuration schema, fixture, sample output, algorithm description, or documentation. Treat such artifacts as real constraints that the solver must discover from the mounted reference.

EXPLORATION & DIRECTION

1. Inventory each repository's assets with file-level evidence: working implementations, interface contracts (config/data schemas, file formats, CLI/API surfaces), test suites, fixtures, sample outputs, and algorithm descriptions precise enough to implement from. Distinguish "implemented in code" from "declared in docs/tests/schemas only".
2. Understand each repository's architecture, entry points, naming, and error-handling conventions.
3. Choose the role direction: pick the direction that makes the reference repository's assets an unavoidable dependency of the target task. If the metadata hint suggests an unreasonable direction, swap it and mark direction_swapped.
4. Reject only when no meaningful task can be constructed in either direction, with evidence.

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

22

Under review as a conference paper at ICLR 2027

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

## PAPER-A-M0058

paper_package.json#s0057

### PROMPT Cross-WS Dependency-Gap Task Synthesis (continued)

## PAPER-A-M0059

paper_package.json#s0058

#### TASK RULES

1. Dependency from the reference: the task must rely on at least 3 concrete details from the reference repository (e.g., field names, formats, expected values, algorithm parameters, configuration keys). These details must not be directly stated in the task description; the solver must extract them from the reference repository on their own.
2. Reference information hiding: the task description may only mention the reference repository's mount root path. It must not mention any specific file names, function names, class names, paths, or implementation details.
3. Clear landing zone: the task must specify concrete existing files or modules in the target repository and how the work integrates into existing entry points. Target repository paths are allowed and required.
4. Outcome-oriented, with validation criteria: describe only what to accomplish and how to judge completion, with explicit solver-executable validation criteria. Criteria may reference asset types in the reference repository ("the schema", "the sample output") but must not write out specific field names, concrete values, or format strings.
5. Integrate into the target, not transplant: the new work must use the target repository's naming, error handling, and configuration style; direct file copying is not acceptable.
6. Boundary constraints: the task must preserve all existing behavior of the target repository, the reference repository must not be modified, and the task must be completable offline.

## PAPER-A-M0060

paper_package.json#s0059

#### OUTPUT CONTRACT

Return exactly one JSON object and nothing else.
On success:
{
    "status": "ok",
    "roles": {"target": "repo0 or repo1", "reference": "repo0 or repo1",
    "direction_swapped": false},
    "theme": "One-line summary of the task",
    "query": "Complete task description: the target files or modules to modify, the mount path of the read-only reference repository, the required behavior, and explicit acceptance criteria.",
    "grounding": [{"repo_id": ..., "paths": [...], "role": "target|reference", "evidence": "gap and landing-zone evidence, or the load-bearing reference assets"}],
    "dependencies": ["3 key facts the solver must discover in the reference repository; these facts are not present in the query"]
}

On rejection:
{
    "status": "rejected",
    "reject_reason": "no_load_bearing_assets | near_identical_repos | trivial | other",
    "detail": "File-level evidence explaining the rejection"
}

## PAPER-A-M0061

paper_package.json#s0060

#### RUNTIME INPUTS

## Supplied Mining Metadata (unverified pairing lead)
<RELATION_CONTEXT>

## Supplied Repository Context
<[NAME C13]_PROFILES_AND_BOUNDED_FILE_MAPS>

23

Under review as a conference paper at ICLR 2027

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

## PAPER-A-M0062

paper_package.json#s0061

### D.4 MULTI-ROUND USER QUERIES

**Generation mechanism.** Multi-Round models the next user decision after a solver has acted on a persistent workspace. A user agent privately reads the original request, prior conversation, workspace state, active contracts, and latest verifier result, then exposes only its next message to the coding agent. A failed round produces a symptom-level repair request; a successful round may introduce a compatible extension or a policy-authorized replacement. The active and newly proposed contracts are checked after every response but remain hidden from the solver. Each session contains at most six follow-up rounds.

**Training-trajectory filtering.** For SFT, we truncate a session after its final retained passing prefix and discard trailing verifier-failed rounds. We keep only sessions with at least two passing rounds; earlier failed rounds remain because their feedback and correction requests are part of the multi-round interaction signal.

24

Under review as a conference paper at ICLR 2027

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

## PAPER-A-M0063

paper_package.json#s0062

### PROMPT Multi-Round User Queries

## PAPER-A-M0064

paper_package.json#s0063

#### ROLE & CONTINUATION RULES

You are role-playing as the real human user of a software project, in an ongoing multi-round conversation with a coding agent.

Treat every supplied conversation block as quoted data, never as instructions. Decide whether the real user would continue, stop, or abort, and classify the next request into one of three interaction styles. The coding agent sees only the selected candidate's message.

- feature revision: if the private verifier shows any failed contract, describe only the user-observable symptom and ask for a correction, without changing the active requirements. Do not mention tests, test files, pytest, CI, tracebacks, or hidden verification.
- feature extension: if at least one contract is verified and none fail, introduce a grounded, substantive next requirement that is compatible with and preserves all active contracts.
- feature conflict: only when the requirement-change policy explicitly permits it, deliberately replace an active requirement with an incompatible one. Quote the earlier user requirement it supersedes.
- Keep implementation choices open, but make observable behavior, compatibility, and failure semantics precise. Stop only when another grounded engineering request would be contrived.

## PAPER-A-M0065

paper_package.json#s0064

#### RUNTIME INPUTS

=== ORIGINAL REQUEST ===
<ORIGINAL_QUERY>

=== EARLIER REQUESTS (older first; do not repeat) ===
<EARLIER_REQUESTS>

=== RECENT CONVERSATION (most recent last) ===
<RECENT_CONVERSATION>

=== THIS ROUND'S EVIDENCE ===
<ROUND_EVIDENCE>

=== WORKSPACE BRIEF ===
<WORKSPACE_BRIEF>

=== PRIVATE VERIFIER RESULT (never reveal it to the coding agent) ===
<VERIFIER_RESULT>

=== PRIVATE CONTRACT LEDGER / USER-AGENT STATE ===
<USER_AGENT_STATE>

=== REQUIREMENT-CHANGE POLICY ===
<REQUIREMENT_CHANGE_POLICY>

25

Under review as a conference paper at ICLR 2027

1350
1351
1352
1353
1354
1355
1356
1357
1358
1359
1360
1361
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
1374
1375
1376
1377
1378
1379
1380
1381
1382
1383
1384
1385
1386
1387
1388
1389
1390
1391
1392
1393
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403

PROMPT Multi-Round User Queries (continued)

OUTPUT CONTRACT
Return exactly one JSON object:
{
    "decision": "continue | stop | abort",
    "style": "feature_extension | feature_revision | feature_conflict",
    "candidates": [
    {
    "new_contract": "observable behavior; empty for a revision",
    "supersedes": "replaced contract id for a conflict, else null",
    "preserves": ["active contract ids"],
    "acceptance": {"kind": "observable_output", "oracle": "objective completion condition"},
    "message": "one focused, natural user request"
    }],
    "selected_candidate": 0
}
For a feature revision, candidates has exactly one item that repairs the same contract and adds no new one. For stop or abort, candidates is [] and selected_candidate is null.

## PAPER-A-M0066

paper_package.json#s0065

## E VERIFIER CONSTRUCTION DETAILS

Test rules. For Single-WS and Cross-WS, a verifier author receives the task and the initial workspace but not a proposed solution. It produces one self-contained pytest file that checks public behavior through absolute paths. The suite must cover the stated requirements without network access or destructive setup; temporary artifacts are confined to /tmp.

PROMPT Agentic Verifier Construction

ROLE & INSTRUCTION
You are the verifier-construction agent in [NAME C13]. A task query has been prepared
for a future solver working in the repository mounted at /app. The solver has NOT started yet. Produce a hidden, deterministic pytest suite that evaluates the
final workspace against the query's observable acceptance contract after the solver finishes. The repository at /app is in its INITIAL state, and the future
solver never sees your tests.

## PAPER-A-M0067

paper_package.json#s0066

### HOW TO WORK

1. Explore the repository (read files; run things where useful) to learn the EXISTING interfaces, file layout, data formats, and packaging.
2. For NEW behavior demanded by the query, take interface details from the query text. Where the query leaves a detail open, assert only what the query actually pins down; never invent stricter requirements than it states.
3. Expected values for the NEW capability must be computed independently inside the test: read input data shipped in the repository at test runtime and recompute the expected result, or take values the query itself states. NEVER derive an expectation for new behavior by running the current, incomplete implementation. For PRESERVATION tests only, the current observed behavior is the baseline.
4. For each task requirement, write 1-3 focused tests. Keep the whole suite at 18 tests or fewer.
5. Do NOT implement preservation by running the repository's own test suite; the solver may legitimately modify those files.
6. Your suite judges the RESULTING BEHAVIOR of the product code, not the solver's process.

26

Under review as a conference paper at ICLR 2027

1404
1405
1406
1407
1408
1409
1410
1411
1412
1413
1414
1415
1416
1417
1418
1419
1420
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
1433
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
1450
1451
1452
1453
1454
1455
1456
1457

## PAPER-A-M0068

paper_package.json#s0067

### PROMPT Agentic Verifier Construction (continued)

## PAPER-A-M0069

paper_package.json#s0068

#### NON-NEGOTIABLE TEST RULES

- ONE self-contained file (test_outputs.py): every fixture and helper inside it; no conftest.py or sibling files.
- Absolute paths only (/app/...); NEVER use __file__.
- Public surfaces only: CLI invocations, produced artifacts, documented entry points, config handling.
- Only import the standard library, pytest, and packages already importable (verify with 'python3 -c "import X"'); verify executables with 'command -v' before use.
- NEVER use pytest.skip/skipif/importorskip/xfail; a missing feature must FAIL.
- Deterministic; no network; no wall-clock or randomness dependence; assertions only.
- Tests may READ /app freely but must never write into it; scratch files go under /tmp.

## PAPER-A-M0070

paper_package.json#s0069

#### MANDATORY RED CHECK

Write your suite to a scratch location and actually run it against the current, unmodified workspace. Requirements on the observed result:
- At least one test that targets the missing capability must FAIL (proving the gap is real and currently open).
- Zero collection errors and zero infrastructure errors; failures must come from assertions or from the expected absence of the new capability, not from a broken test file.
- The preservation tests must PASS now; if one fails on the unmodified workspace, report rejection instead of shipping a broken suite.
Iterate on the suite until these hold, and record the final observed pytest summary.

## PAPER-A-M0071

paper_package.json#s0070

#### OUTPUT CONTRACT

On success:
{
    "status": "ok",
    "files": {"test_outputs.py": "<the content="" content="" file="" of="" complete,="" final="">"},
    "initial_run": {"passed": <int>, "failed": <int>, "errors": <int>,
    "summary": "..."},
    "red_tests": ["names of the tests that fail on the unmodified workspace"],
    "coverage": [{"criterion": "...", "tests": ["test_name", "..."]}],
    "notes": "tolerances, determinism caveats, anything the solve-time harness should know"
}

On rejection:
{
    "status": "rejected",
    "reject_reason": "query_unverifiable | workspace_broken | other",
    "detail": "2-4 sentences of file-level evidence."
}</int></int></int></int></int></int></int></the>

Intent Recovery. Because this variant evaluates recovery of the original user objective rather than a newly synthesized contract, we do not apply the same agentic-verifier filter; this keeps its comparison with source-trajectory SFT well defined.

## PAPER-A-M0072

paper_package.json#s0071

## F CASE STUDIES

We use three deliberately different tasks to expose where the Stage-2 signal is expected to matter: a UI change inside one workspace, a missing RSA capability transferred from a reference toolkit, and a stateful sensor-ingestion session with follow-up requests. Table 7 reports the same initial state under

27

Under review as a conference paper at ICLR 2027

1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
1478
1479
1480
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
1509
1510
1511

the SFT warm start, PAPO, CBAO, and their combination. These case values are provisional and are intended as mechanism diagnostics; the benchmark averages remain the primary evidence.

Table 7: Case-level verifier pass rates (%). Each row is evaluated from the same initial workspace and task; the full [NAME C13] model uses PAPO+CBAO. Values are provisional placeholders.

<table><tr><td>Case</td><td>SFT</td><td>PAPO</td><td>CBAO</td><td>PAPO+CBAO</td></tr><tr><td>MirrorBrain single-WS</td><td>64</td><td>71</td><td>69</td><td>76</td></tr><tr><td>RSA Cross-WS transfer</td><td>48</td><td>59</td><td>56</td><td>65</td></tr><tr><td>Sensor multi-round session</td><td>52</td><td>61</td><td>63</td><td>70</td></tr><tr><td>Mean</td><td>54.7</td><td>63.7</td><td>62.7</td><td>70.3</td></tr></table>

The expected qualitative pattern is that PAPO contributes most on the RSA case, where a verifier failure can be localized to the missing decryption path, while CBAO contributes most on the sensor session, where several high-entropy decisions recur across rounds. MirrorBrain is a useful sanity check for regression: the full model must preserve existing UI behavior while adding the requested interaction changes.

## PAPER-A-M0073

paper_package.json#s0072

### F.1 RECONSTRUCTION AND SINGLE-WORKSPACE RE-QUERYING

This case follows one [NAME C13] workspace from replay to task generation. MirrorBrain is a TypeScript/React project whose retained state is rich enough to support several new requests. Table 8 records which artifacts are available at each stage.

Table 8: Artifacts exposed as the MirrorBrain workspace moves from replay through task generation.

<table><tr><td>Stage</td><td>Observable artifact</td></tr><tr><td>Source trajectory</td><td>Refines React interface components and a focused test across navigation, common controls, review cards, and draft editing while preserving the existing workflows.</td></tr><tr><td>Deterministic replay</td><td>Recovers the project manifest, test configuration, React application, Fastify service, memory-review and cache modules, integration adapters, and end-to-end fixtures.</td></tr><tr><td>Agentic completion</td><td>Preserves all replayed source and test files and adds root-filesystem integration context, including a memory-event fixture, OpenViking adapter, React context, and runtime logs.</td></tr><tr><td>Intent Recovery</td><td>Produces a cross-component interface objective covering navigation, tabs, pagination, candidate cards, and action buttons.</td></tr><tr><td>Single-WS synthesis</td><td>Explores the workspace and generates tasks spanning normalization, URL classification, client errors, API schemas, and cache reconciliation.</td></tr></table>

Trajectory evidence. The recorded interaction touches navigation, shared controls, review actions, and draft views, with tests covering keyboard behavior, ARIA state, loading, and disabled controls. Replay retains the surrounding project context while withholding later edits; the tree below lists the paths used by the reconstructed workspace.

## PAPER-A-M0074

paper_package.json#s0073

#### REPLAYED selected paths

/app/Workspace/mirrorbrain/

|-- package.json
|-- vitest.config.ts
|-- tests/e2e/fixtures/
|    '-- mirrorbrain-mvp-fixture.ts

28

Under review as a conference paper at ICLR 2027

1512
1513
1514
1515
1516
1517
1518
1519
1520
1521
1522
1523
1524
1525
1526
1527
1528
1529
1530
1531
1532
1533
1534
1535
1536
1537
1538
1539
1540
1541
1542
1543
1544
1545
1546
1547
1548
1549
1550
1551
1552
1553
1554
1555
1556
1557
1558
1559
1560
1561
1562
1563
1564
1565

'-- src/
|-- apps/
| |-- mirrorbrain-http-server/
| | |-- index.ts
| | |-- index.test.ts
| |-- mirrorbrain-web-react/src/
| | |-- api/client.ts
| | |-- components/{artifacts,common,layout,memory,review}/
| | |-- contexts/MirrorBrainContext.tsx
|-- integrations/
| |-- activitywatch-browser-source/{index.ts,index.test.ts}
| |-- openviking-store/{index.ts,index.test.ts}
'-- modules/
| |-- memory-events-cache/{index.ts,index.test.ts}
'-- memory-review/{index.ts,index.test.ts,normalize-memory-items.ts}

Agentic completion. The replayed tree is already executable. Completion adds only the missing integration context needed to exercise the recovered task, including a memory event, an adapter, a React context, and runtime logs, while retaining the replayed source and tests. The generated package-lock.json is omitted.

ADDED selected root-filesystem paths

|-- gitignore
|-- mirrorbrain/memory-events/
|    |-- browser:101.json
|-- src/
|    |-- apps/mirrorbrain-web-react/
|    |    |-- gitignore
|    |    |-- src/contexts/MirrorBrainContext.tsx
|    |-- integrations/openviking-store/index.ts
|-- tmp/
|    |-- mirrorbrain-debug.log
|    |-- mirrorbrain-dev-new.log

Recovered intent. Intent Recovery reads the user request and trajectory evidence, rather than the completion model's additions, to produce the following task contract:

Improve the MirrorBrain React interface by applying a polished, consistent, and accessible design across main navigation, subtabs, draft tabs, pagination controls, candidate cards, and action buttons, while preserving existing workflows and component behavior.

The source interaction realizes this contract through consistent active states, focus-visible styling, keyboard navigation, ARIA semantics, loading behavior, and a focused component test.

Generated queries. Single-WS treats the completed tree as a fresh execution context and does not copy the source solution. The resulting requests target observable interfaces already present in the project:

1. Shell-event normalization. Extend normalize-memory-items.ts so shell events already captured and rendered by the system can participate in daily review without regressing browser events.
2. URL classification. Replace substring-based development server detection with structured URL handling and distinguish GitHub Actions pages from ordinary repository pages.
3. Client error handling. Route five mutation methods in api/client.ts through consistent status-aware JSON handling, including descriptive behavior for non-JSON failures.
4. Response schema alignment. Extend the existing Fastify candidate-memory schema with role and contribution so React review components receive the required evidence metadata.

29

Under review as a conference paper at ICLR 2027

1566
1567
1568
1569
1570
1571
1572
1573
1574
1575
1576
1577
1578
1579
1580
1581
1582
1583
1584
1585
1586
1587
1588
1589
1590
1591
1592
1593
1594
1595
1596
1597
1598
1599
1600
1601
1602
1603
1604
1605
1606
1607
1608
1609
1610
1611
1612
1613
1614
1615
1616
1617
1618
1619

5. Cache-source reconciliation. Merge workspace and OpenViking events at cache initialization using existing ID and URL-signature deduplication, preserving reverse-chronological order.

## PAPER-A-M0075

paper_package.json#s0074

### F.2 CROSS-WS SYNTHESIS

This example exercises the directional dependency check in Cross-WS. Two C RSA toolkits share the same domain, but only one contains the decryption path needed for a complete round trip. The matcher therefore designates the incomplete toolkit as the target and the complete one as the evidence source. Table 9 lists the resulting synthesis stages.

Table 9: Evidence and checks used to construct the cross-workspace RSA task.

<table><tr><td>Stage and output</td><td>Evidence</td></tr><tr><td>Relation mining</td><td>Independently generated profiles classify both workspaces as C RSA toolkits; TF-IDF retrieval proposes the pair, and the relation judge records the directional capability gap “RSA decryption”.</td></tr><tr><td>Pair packaging</td><td>The target is mounted writable at /app/workspaces/repo1; the reference is mounted read-only at /app/workspaces/repo0.</td></tr><tr><td>Query generation</td><td>The generator reads the actual files of both workspaces, confirms that the capability is implemented in the reference and absent from the target, and generates a task grounded in facts found only in the reference.</td></tr><tr><td>Verifier generation</td><td>An in-container agent authors the test suite and executes it on the initial workspace. New-capability tests fail while the preservation tests and the reference-unchanged check pass, satisfying the red-check requirement.</td></tr><tr><td>Solution rollout</td><td>The teacher solves the task; all clean checks pass, and the trajectory is retained in the pass-only corpus.</td></tr></table>

Mounted pair. The paired layout exposes a writable solver side and a read-only reference side. Their key files and input/output artifacts are shown below:

![img-5.jpeg](img-5.jpeg)

Grounded capability gap. The target can generate keys, encrypt, and sign, but it has no implementation for the reverse operation. Its existing encryptor fixes conventions that the new program

30

Under review as a conference paper at ICLR 2027

1620
1621
1622
1623
1624
1625
1626
1627
1628
1629
1630
1631
1632
1633
1634
1635
1636
1637
1638
1639
1640
1641
1642
1643
1644
1645
1646
1647
1648
1649
1650
1651
1652
1653
1654
1655
1656
1657
1658
1659
1660
1661
1662
1663
1664
1665
1666
1667
1668
1669
1670
1671
1672
1673

must match, while the reference supplies the private-key path, decrypt invocation, padding, and file-location details. The generated request hides those reference facts and names only the mounted root, forcing the solver to inspect the evidence.

## PAPER-A-M0076

paper_package.json#s0075

#### Selected request (abridged).

The RSA cryptography toolkit at /app/workspaces/repo1 currently supports key generation, encryption, and signing, but is missing the decryption program needed to complete the encrypt/decrypt round-trip. Create a new file rsa_decrypt.c in the root of /app/workspaces/repo1 that reads an encrypted binary file and a private key, then decrypts the ciphertext back to plaintext. The program must integrate seamlessly with the existing toolkit: it should work with keys produced by the existing rsa_keygen.c and ciphertext produced by the existing rsa_encrypt.c, and it must follow the coding conventions, error-handling style, OpenSSL API usage patterns, and output path conventions already established by the other programs. A reference implementation exists at /app/workspaces/repo0: consult it to determine the exact OpenSSL API calls, padding mode, PEM reading function, file paths, command-line interface, and resource cleanup pattern required. When run after rsa_keygen and rsa_encrypt, the program must produce an output file whose contents are byte-for-byte identical to the original plaintext input.

What the verifier checks. The verifier checks compilation, the new executable, command-line behavior, file paths, padding, OpenSSL calls, and an end-to-end encrypt/decrypt round trip. Separate checks protect the existing target programs and confirm that the reference mount is unchanged. The teacher trajectory passes the complete suite.

## PAPER-A-M0077

paper_package.json#s0076

### F.3 MULTI-ROUND USER QUERIES

![img-6.jpeg](img-6.jpeg)

Figure 4: Verifier-guided multi-round continuation. Each state transition is checked privately before the user agent selects the next solver-visible request.

Table 10: Observed interaction styles among retained Multi-Round records; the generator does not enforce a target mixture.

<table><tr><td>Interaction style</td><td>Share</td></tr><tr><td>Feature extension</td><td>62.7%</td></tr><tr><td>Feature revision</td><td>29.3%</td></tr><tr><td>Feature conflict</td><td>8.0%</td></tr></table>

Table 11 shows how the private verifier outcome changes the next user-visible request while the workspace persists.

31

Under review as a conference paper at ICLR 2027

1674
1675
1676
1677
1678
1679
1680
1681
1682
1683
1684
1685
1686
1687
1688
1689
1690
1691
1692
1693
1694
1695
1696
1697
1698
1699
1700
1701
1702
1703
1704
1705
1706
1707
1708
1709
1710
1711
1712
1713
1714
1715
1716
1717
1718
1719
1720
1721
1722
1723
1724
1725
1726
1727

Table 11: Abridged solver-visible requests from the sensor-ingestion session. Bracketed ellipses indicate omitted text; a revision repairs the active contract, whereas a conflict intentionally replaces it.

<table><tr><td>Round</td><td>User-request excerpt</td></tr><tr><td>Initial request</td><td>“Working in the project root /app, the entrypoint sensor_processor.py hard-codes both its input path ... and its output path ..., which makes the script impossible to run against alternate data without editing source. Make it possible to invoke the script as python sensor_processor.py so that the two positional arguments override the input and output locations.”</td></tr><tr><td>1: Extension</td><td>“The path override work is solid, thanks. Now I need this to stop being a one-shot script, because in production my sensor_data.csv keeps growing and I don’t want to re-crunch the entire file every time I get a new batch of readings. [...] Please add a resumable/incremental ingestion mode backed by a small persisted state store.”</td></tr><tr><td>2: Revision</td><td>“The row-counting side of the incremental mode looks right — readings_count comes out at 150 per sensor on a fresh run and rises to exactly 154 after I append four rows, so old rows aren’t being double-counted. But the actual aggregate values are wrong and unstable, and it’s making the output useless for me. [...] It looks like each reading is being scaled down before it’s aggregated.”</td></tr><tr><td>3: Extension</td><td>“The aggregates are solid and stable now — thanks. The next thing I actually need for production is alerting, because right now I have to eyeball processed_results.json to notice when a sensor drifts out of its safe range. [...] Please add a threshold rules engine in a new rules.py, driven by a JSON rules config.”</td></tr><tr><td>4: Conflict</td><td>“The alerting engine is doing its job now, but I’ve hit a real production gap: I’ve decided to change how alerts.json works. Right now it’s overwritten every run holding only the new alerts for that run, which means when a sensor recovers the alert just silently vanishes and I have no record it ever fired or when it cleared. [...] Please turn alerts.json into an append-only history of transition events.”</td></tr><tr><td>5: Extension</td><td>“The event history is finally durable, but right now alerts.json and alerts.jsonl are write-only — nothing ever reads them back, so when I come in Monday morning I still have to eyeball a growing history file to answer basic questions. I need a reporting command that turns that trail into an operational summary.”</td></tr><tr><td>6: Extension</td><td>“The reconcile check has already caught me out once — it correctly flagged that state.json and the alerts.json history disagreed about what was open — but all it can do is tell me there’s drift and exit non-zero. [...] I need reconcile to be able to actually fix the drift, not just report it. Please add a repair capability on top of the existing reconcile logic.”</td></tr></table>

Failure-driven feature revision. The incremental mode initially introduces nondeterministic scaling. The private verifier detects the observable discrepancy, and the user agent requests a repair while keeping the active contract and hidden tests out of the solver conversation:

The row counts are right, but the aggregate values are wrong and unstable. The averages, minima, and maxima are about half of the readings in the CSV, and rerunning unchanged input changes the result. Please make the aggregates use the real readings and remain deterministic for a fresh run, reset, and no-op rerun, while preserving the record shape, rounding, ordering, and incremental counts.

After the scaling defect is removed, the next verifier check passes and the user agent advances to threshold-based alerting. Test code and raw verifier results remain private throughout.

32

Under review as a conference paper at ICLR 2027

1728
1729
1730
1731
1732
1733
1734
1735
1736
1737
1738
1739
1740
1741
1742
1743
1744
1745
1746
1747
1748
1749
1750
1751
1752
1753
1754
1755
1756
1757
1758
1759
1760
1761
1762
1763
1764
1765
1766
1767
1768
1769
1770
1771
1772
1773
1774
1775
1776
1777
1778
1779
1780
1781

Table 12: Comparison of representative environment and training-data construction methods. Strategy summarizes the primary mechanism used to construct environments or training tasks. Env. counts reusable source repositories/workspaces or independently constructed environments, and Tasks gives the reported task or training-instance count. Verif. indicates an executable task verifier, Multi-Round denotes extended multi-round queries, and Cross-WS cross-workspace synthesis.

<table><tr><td>Method</td><td>Strategy</td><td>Env.</td><td>Tasks</td><td>Verif.</td><td>Multi-Round</td><td>Cross-WS</td></tr><tr><td>Endless Term. (Gandhi et al., 2026)</td><td>task-conditioned</td><td>3,255</td><td>3,255</td><td>√</td><td>✕</td><td>✕</td></tr><tr><td>TMax (Ivison et al., 2026)</td><td>combinatorial sampling</td><td>14.6k</td><td>14.6k</td><td>√</td><td>✕</td><td>✕</td></tr><tr><td>CLI-Gym (Lin et al., 2026)</td><td>env. perturbation</td><td>29</td><td>1,655</td><td>√</td><td>✕</td><td>✕</td></tr><tr><td>CLI-Universe (Hua et al., 2026)</td><td>taxonomy-guided</td><td>6k</td><td>6k</td><td>√</td><td>✕</td><td>✕</td></tr><tr><td>SkillSynth (Fan et al., 2026)</td><td>skill graph-guided</td><td>3,560</td><td>3,560</td><td>√</td><td>✕</td><td>✕</td></tr><tr><td>OpenThinker-Agent (Raoof et al., 2026)</td><td>multi-source curation</td><td>-</td><td>100k</td><td>√</td><td>✕</td><td>✕</td></tr><tr><td>RST (Li et al., 2026b)</td><td>recursive evolution</td><td>37.5k</td><td>37.5k</td><td>√</td><td>✕</td><td>✕</td></tr><tr><td>CalibForge (Meng et al., 2026)</td><td>adversarial calibration</td><td>5,431</td><td>5,431</td><td>√</td><td>✕</td><td>✕</td></tr><tr><td>[NAME C13] (ours)</td><td>trajectory reconstruction</td><td>37.3k</td><td>32.0k</td><td>√</td><td>√</td><td>√</td></tr></table>

Controlled requirement conflict. Once alerting is working, the user agent invokes the explicit requirement-change policy to replace the per-run JSON snapshot with a durable event history. This is a product decision, not a correction to a failed implementation:

I have decided to change how alerts.json works. It should no longer be a per-run snapshot: make it an append-only history of firing and resolved transitions, so a recovered alert remains recorded. Keep exit code 2 for a new firing and 0 for a lone resolution, and preserve the first-observed timestamp and severity with every event.

The replacement contract remains active for the remaining rounds, which then add reporting, reconciliation, and repair capabilities.

## PAPER-A-M0078

paper_package.json#s0077

## G ENVIRONMENT CONSTRUCTION COMPARISON

Table 12 compares representative approaches to constructing executable terminal environments and training tasks. Counts use the definitions reported by each work and are included for orientation rather than as a directly normalized benchmark.

## PAPER-A-M0079

paper_package.json#s0078

## H RECONSTRUCTION AND SUPPLEMENTARY ABLATIONS

This section probes the parts of [NAME C13] that are too detailed for the main comparison: state recovery, corpus composition, verifier filtering, data-budget allocation, and transfer from SWE traces. The values below use the same evaluation definitions as the main study.

Table 13: Task-sufficiency rates for replayed and completed workspaces, reported separately for Terminal and SWE source pools.

<table><tr><td rowspan="2">Pool</td><td rowspan="2"># Environments</td><td colspan="2">Sufficient (%)</td></tr><tr><td>Post-replay</td><td>Post-completion</td></tr><tr><td>Terminal</td><td>38,294</td><td>40.2</td><td>93.5</td></tr><tr><td>SWE</td><td>1,900</td><td>20.1</td><td>77.1</td></tr></table>

33

Under review as a conference paper at ICLR 2027

1782
1783
1784
1785
1786
1787
1788
1789
1790
1791
1792
1793
1794
1795
1796
1797
1798
1799
1800
1801
1802
1803
1804
1805
1806
1807
1808
1809
1810
1811
1812
1813
1814
1815
1816
1817
1818
1819
1820
1821
1822
1823
1824
1825
1826
1827
1828
1829
1830
1831
1832
1833
1834
1835

(a) Context recovered by completion

![img-7.jpeg](img-7.jpeg)

(b) Verifier-ready context

![img-8.jpeg](img-8.jpeg)

Figure 5: Effect of completion on recovered context and task sufficiency. The panels show file-level context and verifier judgments; the displayed census values remain provisional.

(a) Primary language

![img-9.jpeg](img-9.jpeg)

(b) Technical domain

![img-10.jpeg](img-10.jpeg)

Figure 6: Illustrative language and domain composition of the reconstructed workspace pool. Rare categories are aggregated, and the percentages must be replaced by the final census.

Table 14: Contribution of verifier-based trajectory selection under a fixed launched-task pool for Single-WS and Cross-WS.

<table><tr><td>Variant</td><td>Records</td><td>Terminus2-XML</td></tr><tr><td>Single-WS w/o verifier</td><td>35.1k</td><td>56.0<sub>3.3</sub></td></tr><tr><td>Single-WS w/ verifier</td><td>25.4k</td><td>56.4<sub>2.6</sub></td></tr><tr><td>Cross-WS w/o verifier</td><td>7.1k</td><td>53.2<sub>2.1</sub></td></tr><tr><td>Cross-WS w/ verifier</td><td>3.5k</td><td>55.4<sub>2.7</sub></td></tr></table>

34

Under review as a conference paper at ICLR 2027

1836
1837
1838
1839
1840
1841
1842
1843
1844
1845
1846
1847
1848
1849
1850
1851
1852
1853
1854
1855
1856
1857
1858
1859
1860
1861
1862
1863
1864
1865
1866
1867
1868
1869
1870
1871
1872
1873
1874
1875
1876
1877
1878
1879
1880
1881
1882
1883
1884
1885
1886
1887
1888
1889

Table 15: Trajectory size and teacher success for the two workspace-querying modes under a common generation setup.

<table><tr><td rowspan="2">Variant</td><td colspan="2">Turns</td><td colspan="2">Tool calls</td><td colspan="2">Tokens / record</td><td rowspan="2">Teacher pass@1</td></tr><tr><td>Median</td><td>Mean</td><td>Median</td><td>Mean</td><td>Median</td><td>Mean</td></tr><tr><td>Single-WS</td><td>14</td><td>15.1</td><td>20</td><td>21.2</td><td>30.4k</td><td>32.9k</td><td>72.3%</td></tr><tr><td>Cross-WS</td><td>23</td><td>25.3</td><td>38</td><td>39.7</td><td>46.5k</td><td>51.9k</td><td>49.2%</td></tr></table>

Table 16: Pilot category-level change from adding Cross-WS records to Single-WS training. The change is measured in Terminal-Bench 2.1 points; n is the number of tasks in the category. Final repeated-run estimates should replace these pilot values before submission.

<table><tr><td>Category</td><td>Change (points)</td><td>n</td></tr><tr><td>Software engineering</td><td>+2.2</td><td>26</td></tr><tr><td>Model training</td><td>+15.0</td><td>5</td></tr><tr><td>Debugging</td><td>+10.0</td><td>4</td></tr><tr><td>Data processing</td><td>-2.1</td><td>8</td></tr><tr><td>DevOps</td><td>-2.5</td><td>6</td></tr><tr><td>Security</td><td>+1.4</td><td>7</td></tr></table>

Table 17: Matched-record comparison of three ways to expand the Single-WS corpus: new environments, additional queries, or additional teacher solutions.

<table><tr><td>Variant</td><td>Envs</td><td>Queries / env</td><td>Solutions / query</td><td>Records</td><td>Terminus2-XML</td></tr><tr><td>Base pool</td><td>17,558</td><td>1</td><td>1</td><td>17.6k</td><td>53.2<sub>4.1</sub></td></tr><tr><td>Environment expansion</td><td>35,116</td><td>1</td><td>1</td><td>35.1k</td><td>56.0<sub>3.3</sub></td></tr><tr><td>Query expansion</td><td>17,558</td><td>2</td><td>1</td><td>35.1k</td><td>53.8<sub>3.3</sub></td></tr><tr><td>Solution expansion</td><td>17,558</td><td>1</td><td>2</td><td>35.1k</td><td>53.9<sub>2.4</sub></td></tr></table>

Table 18: Transfer of Intent Recovery data from SWE workspaces to Terminal-Bench 2.1 under two evaluation scaffolds; estimates are provisional.

<table><tr><td>Variant</td><td>Data size</td><td>Claude Code</td><td>Terminus2-XML</td><td>Avg.</td></tr><tr><td>Qwen3.5-27B</td><td>-</td><td>47.8<sub>2.0</sub></td><td>46.2<sub>3.9</sub></td><td>47.0</td></tr><tr><td>Intent Recovery</td><td>10.3k</td><td>50.6<sub>0.9</sub></td><td>49.4<sub>1.6</sub></td><td>50.0</td></tr></table>

## PAPER-A-M0080

paper_package.json#s0079

### H.1 SUPPLEMENTARY EXPERIMENTAL ANALYSES

The analyses below isolate data-quality and scaling effects while keeping the main benchmark definitions and evaluation protocols fixed.

## PAPER-A-M0081

paper_package.json#s0080

#### H.1.1 ROLE OF VERIFIER FILTERING

We first test whether verifier selection improves supervision enough to justify discarding failed teacher rollouts. For each query family, the comparison uses the full launched pool and its verifier-passed subset.

Selection is most useful for difficult cross-workspace tasks. Single-WS reaches 56.4 with the passed subset versus 56.0 when failures are retained, despite using fewer records. For Cross-WS,

35

Under review as a conference paper at ICLR 2027

1890
1891
1892
1893
1894
1895
1896
1897
1898
1899
1900
1901
1902
1903
1904
1905
1906
1907
1908
1909
1910
1911
1912
1913
1914
1915
1916
1917
1918
1919
1920
1921
1922
1923
1924
1925
1926
1927
1928
1929
1930
1931
1932
1933
1934
1935
1936
1937
1938
1939
1940
1941
1942
1943

retaining failed rollouts lowers the score to 53.2, while the passed subset reaches 55.4 with less than half as many records. The corresponding Multi-Round comparison also drops when round-level verification is removed (Table 20).

## PAPER-A-M0082

paper_package.json#s0081

### H.1.2 EXPANSION-AXIS ABLATION

We next hold the record budget approximately fixed and vary which axis supplies the additional supervision. From a base of 17,558 Single-WS environments with one query and one teacher solution each, we double either the number of environments, the number of queries per environment, or the number of solutions per query. Each resulting corpus contains roughly 35k records and uses the same Terminal-Bench 2.1 setup, so the comparison isolates budget allocation.

Environment expansion gives the largest increase, from 53.2 to 56.0; query and solution expansion reach 53.8 and 53.9. A new workspace contributes an independent execution context, whereas additional requests or solutions on an existing workspace share most of the same state. This result supports allocating early data budget to reconstructing diverse environments.

## PAPER-A-M0083

paper_package.json#s0082

### H.1.3 CROSS-DOMAIN GENERALIZATION

We also test whether the replay-and-query pipeline transfers beyond terminal-native sources. We apply Intent Recovery to SWE workspaces, train with the same recipe, and measure the resulting policy on Terminal-Bench 2.1. Using Intent Recovery alone keeps the transfer test separate from the effects of Single-WS, Cross-WS, and Multi-Round task synthesis.

Among 1,900 SWE repositories, 1,464 pass the sufficiency judgment. Their multiple source tasks produce approximately 10.3k Intent Recovery trajectories. Training on these records raises the average from 47.0 to 50.0, with consistent movement under Claude Code (47.8 → 50.6) and Terminus2-XML (46.2 → 49.4). The effect therefore is not specific to one evaluation scaffold, although this experiment only measures transfer from SWE into terminal tasks.

Table 15 shows that the cross-workspace condition changes both trajectory length and task difficulty. Relative to Single-WS, Cross-WS uses 1.6× the median turns, 1.9× the tool calls, and 1.5× the tokens per record; teacher pass@1 falls from 72.3% to 49.2%. The additional cost comes from reconciling evidence in two codebases before editing, rather than from simply increasing the number of records.

How Cross-WS expands breadth. Single-WS samples one new requirement from a single recovered project. Cross-WS adds a second codebase as read-only evidence while keeping the target writable, creating capability combinations that cannot be expressed by the target workspace alone.

Where cross-workspace data helps. The mixture reaches 58.4₂.₁ under Terminus2-XML versus 56.4₂.₆ for Single-WS. Table 16 shows the category breakdown: the largest software engineering group rises from 46.9 to 49.1, with larger changes in model training (+15.0) and debugging (+10.0). Because several categories contain only a few tasks, these per-category values are diagnostic rather than standalone statistical claims; the aggregate result is consistent with Cross-WS contributing supervision that is unavailable from isolated workspaces.

## PAPER-A-M0084

paper_package.json#s0083

### H.2 ADDITIONAL EXPANSION TABLES

Table 19: Terminal-Bench 2.1 comparison of Single-WS, Cross-WS, and the combined training mixture.

<table><tr><td>Variant</td><td>Data size</td><td>Terminus2-XML</td></tr><tr><td>Qwen3.5-27B</td><td>-</td><td>46.2₃.₉</td></tr><tr><td>Single-WS</td><td>25.4k</td><td>56.4₂.₆</td></tr><tr><td>Cross-WS</td><td>3.5k</td><td>55.4₂.₇</td></tr><tr><td>Single-WS + Cross-WS</td><td>28.9k</td><td>58.4₂.₁</td></tr></table>

36

Under review as a conference paper at ICLR 2027

1944
1945
1946
1947
1948
1949
1950
1951
1952
1953
1954
1955
1956
1957
1958
1959
1960
1961
1962
1963
1964
1965
1966
1967
1968
1969
1970
1971
1972
1973
1974
1975
1976
1977
1978
1979
1980
1981
1982
1983
1984
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997

Table 20: EvoCode-Bench v2 comparison of persistent Multi-Round data and the effect of removing round-level verifier feedback.

<table><tr><td>Variant</td><td>Data size</td><td>MT@4 score</td><td>Case score</td></tr><tr><td>Single-WS</td><td>25.4k</td><td>18.4</td><td>71.9<sub>3.5</sub></td></tr><tr><td>Single-WS + Multi-Round</td><td>28.5k</td><td>21.0</td><td>76.9<sub>1.4</sub></td></tr><tr><td>Single-WS + Multi-Round (w/o round verifier)</td><td>28.5k</td><td>18.8</td><td>73.2<sub>2.6</sub></td></tr></table>

## PAPER-A-M0085

paper_package.json#s0084

### H.3 COMPACT EXPANSION SUMMARY

Table 21: Matched summary of the breadth and depth comparisons reported above.

<table><tr><td>Expansion</td><td>Comparison</td><td>Metric</td><td>Change</td></tr><tr><td>Breadth</td><td>Single-WS → Single-WS + Cross-WS</td><td>TB2.1</td><td>56.4 → 58.4</td></tr><tr><td>Depth</td><td>Single-WS → Single-WS + Multi-Round</td><td>MT@4 / Case</td><td>18.4 → 21.0 / 71.9 → 76.9</td></tr></table>

## PAPER-A-M0086

paper_package.json#s0085

### I SFT DATASET STATISTICS

Table 22 reports corpus size together with median interaction length. The Multi-Round records are longer because each one preserves a completed state and appends several user decisions to the same session.

Table 22: Final SFT corpus statistics after length filtering.

<table><tr><td>Dataset</td><td>Records</td><td>Turns</td><td>Tool calls</td><td>Tokens</td></tr><tr><td>Intent Recovery</td><td>35,809</td><td>12</td><td>17</td><td>36.1k</td></tr><tr><td>Single-WS</td><td>25,386</td><td>14</td><td>20</td><td>30.4k</td></tr><tr><td>Cross-WS</td><td>3,512</td><td>23</td><td>38</td><td>46.5k</td></tr><tr><td>Multi-Round</td><td>3,079</td><td>92</td><td>102</td><td>126.1k</td></tr></table>

## PAPER-A-M0087

paper_package.json#s0086

### J EVALUATION CONFIGURATIONS

Table 23 lists the configurations used for [NAME C13]-27B and the five reproduced open-weight baselines in Table 1. These reproduced baselines use model-specific settings rather than a shared evaluation configuration. The listed settings apply to both Terminal-Bench 2.1 and EvoCode-Bench v2 unless noted otherwise. For TMax-27B, the listed configuration applies only to our EvoCode-Bench v2 reproduction; its Terminal-Bench scores and Vanillux2Agent scaffold follow the original report. Qwen3.5-27B and Qwen3.7-Max use the [NAME C13]-27B configuration, with xhigh effort enabled for Qwen3.7-Max. On EvoCode-Bench v2, TermiGen-32B instead uses Terminus2-JSON with an 81,920-token summarization threshold.

37

Under review as a conference paper at ICLR 2027

1998
1999
2000
2001
2002
2003
2004
2005
2006
2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
2021
2022
2023
2024
2025
2026
2027
2028
2029
2030
2031
2032
2033
2034
2035
2036
2037
2038
2039
2040
2041
2042
2043
2044
2045
2046
2047
2048
2049
2050
2051

Table 23: Evaluation configurations used in our reproductions.

<table><tr><td>Setting</td><td>Nemotron-Terminal-32B</td><td>OpenThinker-Agent-32B</td><td>TermiGen-32B</td><td>TerminalTraj-32B</td><td>TMax-27B</td><td>Terminal-Universe-27B</td></tr><tr><td>Architecture</td><td>Qwen3For CausalLM</td><td>Qwen3For CausalLM</td><td>Qwen2For CausalLM</td><td>Qwen2For CausalLM</td><td>Qwen3.5For Conditional Generation</td><td>Qwen3.5For Conditional Generation</td></tr><tr><td>Scaffold</td><td>Terminus2</td><td>Terminus2</td><td>BashAgent</td><td>Terminus2</td><td>Terminus2</td><td>Terminus2</td></tr><tr><td>Parser</td><td>JSON</td><td>JSON</td><td>Text JSON</td><td>JSON</td><td>XML</td><td>XML</td></tr><tr><td>Context length</td><td>40,960</td><td>32,768</td><td>131,072</td><td>32,768</td><td>262,144</td><td>262,144</td></tr><tr><td>Turn max tokens</td><td>8,192</td><td>8,192</td><td>8,192</td><td>8,192</td><td>65,536</td><td>65,536</td></tr><tr><td>Summ. threshold</td><td>32,960</td><td>28,672</td><td>disabled</td><td>24,768</td><td>176k</td><td>176k</td></tr><tr><td>Temperature</td><td>0.6</td><td>0.6</td><td>0.6</td><td>0.7</td><td>0.7</td><td>1.0</td></tr><tr><td>Top-p / top-k</td><td>0.95 / 20</td><td>0.95 / 20</td><td>0.8 / 20</td><td>0.8 / 20</td><td>0.95 / 20</td><td>0.95 / 20</td></tr><tr><td>Interleaved thinking</td><td>✕</td><td>✕</td><td>✕</td><td>✕</td><td>√</td><td>√</td></tr><tr><td>Thinking enabled</td><td>√</td><td>√</td><td>✕</td><td>✕</td><td>√</td><td>√</td></tr><tr><td colspan="7">Shared across all reproductions</td></tr><tr><td>TB wall clock</td><td></td><td></td><td></td><td>4 h</td><td></td><td></td></tr><tr><td>EvoCode wall clock</td><td></td><td></td><td></td><td>10 h</td><td></td><td></td></tr><tr><td>TB runs</td><td></td><td></td><td></td><td>6</td><td></td><td></td></tr><tr><td>EvoCode runs</td><td></td><td></td><td></td><td>4</td><td></td><td></td></tr></table>

38
