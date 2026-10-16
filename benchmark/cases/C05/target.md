# [TITLE C05]

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

# [TITLE C05]

Anonymous authors

Paper under double-blind review

# ABSTRACT

In professional video editing, an agent's output is not a rendered video but an editable project that human editors continue to work on. Thus, rigorous evaluation of video-editing agents requires both scalable construction of realistic editing tasks and systematic verification of such project states. We introduce [NAME C05], a benchmark of 781 video-editing tasks that connects task construction and outcome evaluation through a shared structured specification. [NAME C05] extracts real workflows from official editing tutorials and organizes them into 48 atomic editing operations and 121 reusable task templates. Each atomic operation specifies both the edit to perform and evaluation rules for the requested changes and required preservation, allowing natural-language instructions and their evaluation to come from the same task specification. [NAME C05] evaluates agents directly on the resulting project state, verifying request completion and state preservation, without requiring a reference GUI trajectory or a single gold project. We build [NAME C05] to run the full benchmark and evaluate seven computer-use agents, whose task success rates range from 3.5% to 87.2%, with preservation failures remaining a major source of error. By unifying realistic task construction with systematic outcome evaluation, [NAME C05] provides a scalable and reproducible foundation for [NAME C05].

# 1 INTRODUCTION

Professional video editing is not merely about producing a rendered video, but about creating an editable project that human editors can continue to refine. Evaluating a video-editing agent therefore requires judging not only the rendered video, but also whether the underlying project reflects the intended edits. Prior video-editing research has largely followed two directions. Generative video editing transforms visual content based on natural-language instructions and primarily evaluates the perceptual quality and instruction adherence of rendered videos (Wu et al., 2026; Gao et al., 2026; Chen et al., 2026). Meanwhile, a small but growing body of work benchmarks computer-use agents that operate the GUIs of real video-editing software (Hu et al., 2026). This direction reflects a broader shift in creative-tool research from flattened outputs toward editable artifacts such as PPTX and SVG (Tang et al., 2025; Liang et al., 2025; Xing et al., 2026).

Benchmarking video-editing agents requires both realistic editing tasks and reliable evaluation of the resulting project state. However, existing approaches face limitations on both fronts. For task construction, there is a trade-off between realism and scalability: expert-crafted tasks and demonstrations reflect realistic editing workflows but are costly to scale, whereas LLM-synthesized tasks scale easily but may yield implausible or incoherent editing requests. For evaluation, existing benchmarks commonly rely on rendered videos or editor screenshots. These visual outputs are only partial observations of the underlying project state and cannot systematically verify which objects were modified, which parameter values were applied, or whether unrelated parts of the project were preserved. In summary, a unified approach that supports both scalable construction of realistic video-editing tasks and systematic evaluation of their outcomes remains lacking.

To tackle these challenges, we introduce [NAME C05], a benchmark suite for video-editing agents containing 781 tasks derived from 121 templates (Figure 1). [NAME C05] addresses both components through tutorial-grounded task construction and predicate-based project-state evaluation. Official editing tutorials provide workflows, ordered procedures that accomplish a concrete editing

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

I - Task Instruction "Duplicate the first clip, apply a blur value of 60 to the copy, and do not modify the original clip."

![img-0.jpeg](img-0.jpeg)

Figure 1: An episode of a running example of a [NAME C05] task. A computer-use agent edits the initial project $S_0$ through GUI actions, producing the final project $S_T$. The screenshots are rendered editor views; the evaluator compares the structured project states $S_0$ and $S_T$ using Boolean predicates. The request predicates $P^+$ check the requested edits, the preservation predicates $P^0$ check that the original clip is unchanged, and the unauthorized-change audit $U$ checks for changes that no predicate authorizes. The episode succeeds only if all three checks pass.

goal, which serve as our source of realism. We decompose these workflows into atomic operations such as duplicating a clip or setting an effect parameter, and recompose them into reusable task templates. Binding each template to different media, targets, and parameters constructs diverse, realistic task instances without per-task expert effort. A human validation study on 200 tasks confirms that the generated tasks are meaningful (96.2%) and executable (92.8%). For evaluation, each atomic operation provides predicate templates for the requested changes and required preservation. Instantiating the instruction and these predicates from the same task specification enables systematic, rule-based evaluation of the resulting project state.

To run our benchmark at scale, we build [NAME C05], an instrumented extension of the open-source OpenCut Classic editor, and verify application fidelity in Adobe Premiere Pro. [NAME C05] clearly separates seven computer-use agents by capability: task success spans from 87.2% for the strongest proprietary model to below 5% for both open-weight agents. Substantial headroom remains even for the strongest model: GPT-6 Sol fails on a notable share of animation and timeline-editing tasks, and its success drops from 83.9% to 62.5% when the same tasks are run in Premiere Pro. Altogether, [NAME C05] provides a rigorous and scalable foundation for evaluating the video-editing capabilities of computer-use agents and tracking future progress.

## 2 RELATED WORK

Video editing and generation. Most recent video-editing work modifies the rendered video directly. Diffusion-based and instruction-guided methods are typically evaluated on instruction following, visual quality, and temporal consistency (Sun et al., 2024; Bai et al., 2026), while CoVEBench, VEFX-Bench, and IVEBench similarly score edits mainly from output videos (Wu et al., 2026; Gao et al., 2026; Chen et al., 2026). LAVE (Wang et al., 2024) and EditDuet (Sandoval-Castañeda et al., 2025) instead operate on editing workflows, but are evaluated through user studies and output comparisons rather than as reusable benchmarks.

GUI agents in professional software. WebArena, AndroidWorld, and OSWorld provide evaluation on the web, mobile devices, and desktop (Zhou et al., 2024; Rawles et al., 2025; Xie et al., 2024). Recent benchmarks extend this setting to professional software. VideoGUI derives tasks from instructional videos and human reproduction (Lin et al., 2024), while ProSoftArena curates tasks across 13 professional applications (Ai et al., 2026). CutVerse, the closest to our setting,

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

collects expert demonstrations of post-production workflows across seven applications and derives evaluation milestones from them (Hu et al., 2026). Such human-grounded task construction provides realism but is costly to scale. [NAME C05] instead compositionally instantiates tutorial-grounded editing operations, jointly constructing the initial project, instruction, and evaluation conditions.

Execution- and state-based evaluation. SWE-bench evaluates model patches with executable tests (Jimenez et al., 2024), while AppWorld generates tasks with initial states and programmatic evaluations that accept different valid solutions while detecting unintended changes (Trivedi et al., 2024). Similar state-based evaluation has been applied to editable artifacts: PPTArena uses structural and visual evidence for PowerPoint edits (Ofengenden et al., 2025), and Interactive Reward Agent verifies completion from files and application state (Shi et al., 2026). This approach is particularly important for video editing because rendered outputs do not uniquely determine the underlying project; splitting a clip, for example, may leave the rendered video unchanged. [NAME C05] therefore evaluates predicates over initial and final project states, verifying requested edits and preservation without requiring an exact reference project.

### 3 BENCHMARK FORMULATION AND ENVIRONMENT

### 3.1 FORMULATION

Task Definition. We formulate our task as a tuple $\mathcal{T} = (S_0, I, P^+, P^0)$. The initial project state $S_0$ is already prepared for the task, with the application and sequence open and the required media and timeline set up, reflecting workflows that continue from a human editor's timeline. The instruction $I$ is a natural-language editing request. The request predicates $P^+$ and preservation predicates $P^0$ are Boolean functions of $S_0$ and the final project state $S_T$: those in $P^+$ check whether the requested changes have occurred, and those in $P^0$ check whether the state that must remain unchanged has been preserved. In the running example (Figure 1), $P^+$ checks whether a copy has been created and whether its blur value is 60, while $P^0$ checks whether the original 1.clip remains unmodified. Predicates are hidden from the agent and are only revealed to the evaluator.

Atomic Operations. The edit requested by each [NAME C05] task decomposes into an ordered sequence of one or more atomic operations, the smallest changes to the project state that can be requested on their own (e.g., set_clip_effect or apply_video_transition). Atomicity is defined by the granularity of changes to the project state, not by the granularity of GUI actions. A single operation may be completed through different action sequences. In Premiere Pro, for example, split_clip can be performed with the Ctrl+K shortcut or with the Razor tool. [NAME C05] defines a set $\mathcal{O}$ of 48 atomic operations (Appendix A.1). Each operation $o \in \mathcal{O}$ specifies a precondition $C_o$ on the initial project and predicate templates $\widehat{P}_o^+$ and $\widehat{P}_o^0$, i.e., predicates whose target and value are left as parameters. For example, as a precondition, set_clip_effect(x, e, v) requires that clip $x$ exists. Its request template checks that effect $e$ on $x$ has value $v$, and its preservation template checks that the timeline and source intervals of $x$ are unchanged. The operations are not part of the task tuple and are never shown to the agent; instead, they serve as building blocks from which $I$, $P^+$, and $P^0$ are instantiated (§4). Because each operation carries its own predicate templates, any valid composition of operations comes with evaluation conditions by construction, making task generation and evaluation coherent.

### 3.2 EPISODE PROTOCOL

At each time step, the agent receives the instruction $I$, the current screenshot, its interaction history, and the remaining action budget, together with a fixed system prompt (see Appendix C.2). The history records the agent's previous responses, the GUI actions it executed, and their execution results. It observes neither the DOM nor the internal project state. The agent responds with low-level GUI actions such as click, drag, type, and keypress; the concrete action format follows each agent's native interface. A single response may contain several actions, which the environment executes in order before returning a new screenshot. The episode ends when the agent returns a completion response or exhausts its action budget, after which the resulting project state $S_T$ is evaluated.

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

Figure 2: The [NAME C05] task-generation pipeline. Tutorial workflows are abstracted into task templates ( \( §4.1 \) ), which are bound to instantiate the initial project, instruction, and predicates ( \( §4.2 \) ). Skyblue insets show the running example.

### 3.3 CONTROLLABLE EXECUTION ENVIRONMENT

We use two environments to run [NAME C05]: (1) [NAME C05] as the primary execution environment for large-scale parallel experiments and (2) Adobe Premiere Pro as the target environment for verifying application fidelity in realistic professional video editing.

[NAME C05]. [NAME C05] requires a scalable, web-based video-editing environment for parallel agent testing. We implemented [NAME C05], our benchmark environment built as an instrumented fork of the MIT-licensed OpenCut Classic editor (OpenCut Project). When an episode ends, it automatically exports the current project state in JSON format. Out of the 48 operations defined in [NAME C05], 19 were newly implemented in [NAME C05], while 29 were already provided through existing OpenCut features. See Appendix A.2 for the complete operation list and operation-to-interface mapping. To verify the accuracy and stability of the 19 newly implemented operations, we configured 178 native and web tests, including time and source-range calculations, preservation of unrelated objects, rejection of incorrect edits, undo/redo, and JSON save and restore. All 178 tests passed on the final run.

Adobe Premiere Pro. To verify application fidelity, we also conducted experiments on a 56-task subset in Adobe Premiere Pro, a widely used professional video-editing application. §6 provides the detailed settings. When an episode ends, an evaluator-side UXP extension exports the current project state in Final Cut Pro XML format.

## 4 [NAME C05] TASK GENERATION PIPELINE

Even if the individual operations are feasible, a random combination is not guaranteed to form a plausible editing request. (e.g. "Delete the clip and crop the bottom of the clip.") [NAME C05] tasks stem from official editing tutorials, which pair concrete editing goals with ordered procedures for achieving them. Each procedure thus supplies a realistic and coherent workflow, rather than an arbitrary combination of operations. We abstract these workflows into reusable task templates and instantiate many tasks from each, so that the benchmark scales through binding rather than per-task expert effort. Construction proceeds in two phases (Figure 2). We first build atomic operations and reusable task templates from editing tutorials ( \( §4.1 \) ), and bind each template to compatible media, targets, and parameters to create concrete task instances ( \( §4.2 \) ). After the generation is completed, we assess the quality of the tasks through human validation ( \( §4.3 \) ).

## A-page-0005

target PDF page 5

### 4.1 TUTORIAL-BASED TASK TEMPLATE CONSTRUCTION

We use task templates as the foundation for generating multiple instances. A task template abstracts a single editing request as the required sequence of operations. A concrete task instance is created after binding the video, target clip, and parameter values.

Task template construction proceeds by (1) extracting source workflows from official editing tutorials, (2) organizing these workflows into common atomic operations, and (3) composing the operations into a task template.

Source Workflow Extraction. A workflow is an ordered sequence of editing operations, together with their target relationships, that fulfills a coherent editing request. For example, duplicating a clip and applying an effect to its copy forms a single workflow: creating a modified copy while preserving the original. We collected 45 official tutorial documents for three representative video-editing applications, Adobe Premiere Pro, Final Cut Pro, and DaVinci Resolve, and extracted 165 source workflows from them.

Atomic Operation Set Construction. We derive the operation set O from 165 source workflows, merging equivalent functions across the three editors into 48 atomic operations that cover timeline editing, layout and effects, playback speed, text, transitions, keyframes, and audio. See Appendix A.1 for the complete operation set O. Operations that were unsupported by OpenCut Classic, or whose existing behavior differed from the required semantics, were newly implemented or modified in [NAME C05]. §3.3 describes the [NAME C05] implementation and verification methods.

Task Template Set Construction. A task template M is formulated as an ordered operation sequence  \( M = \langle o_{1}, o_{2}, \ldots, o_{K} \rangle \) , where  \( o_{j} \in O \) . A total of 121 task templates were created: 95 were constructed from contiguous subworkflows of source workflows after verifying their executability, and 26 were manually crafted from the tutorials to supplement atomic-operation coverage. See Appendix A.3 for the complete template set.

### 4.2 TASK INSTANCE CONSTRUCTION

Task Binding. A task template M specifies only the order of operations, not the media, targets, or parameters they act on. To create a concrete task instance, we should assign these elements through what we define as task binding  \( \theta = (B, m, t, v, d) \) . Thus, binding the same template in different ways therefore yields distinct tasks that share a plausible editing goal.

Task binding consists of a base timeline layout B, source media and source range m, targets t and parameter values v for the template's operations, and distractor media d that is present in the project but not needed for the task. The base layout is selected from eight reusable timeline structures that vary in the number of clips, the presence of a text object, and resolution (see Appendix A.4). A target may refer either to an object in the initial project or to an object produced by an earlier operation in the template. The distractor media are imported into the project but not needed for the task, so that the agent must identify the target rather than use whatever is available.

In the running example (Figure 1 and 2), the template that duplicates a clip and applies an effect to the copy is bound to a one-clip layout, the first clip on V1 as the duplication target, the resulting copy as the effect target with a blur value of 60, and a distractor video imported into the source panel but not placed on the timeline.

Not every binding suits every template. The requirements of \( M \) follow from the preconditions \( C_o \) from its atomic operations. For example, a template containing a transition operation and a text editing operation requires two adjacent clips and an existing text object. For each template \( M \), we therefore enumerate the bindings that satisfy these requirements and select \( k \) of them, \( \{\theta_i\}_{i=1}^k \), using a fixed seed.

State and Predicate Instantiation. For each selected binding \(\theta_{i}\), we construct the initial project state \(S_{0,i}\) by placing the source media and range \(m_{i}\) into the base layout \(B_{i}\) and importing the distractor media \(d_{i}\). We then instantiate the predicates by filling each operation's predicate templates

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

with the targets and parameter values in $\theta_i$ and taking the union over the operations of $M$:

$$P_i^+ = \bigcup_{j=1}^K \widehat{P}_{o_j}^+[\theta_i], \quad P_i^0 = \bigcup_{j=1}^K \widehat{P}_{o_j}^0[\theta_i], \tag{1}$$

where $\widehat{P}_{o_j}[\theta_i]$ denotes the template of $o_j$ with its parameters bound by $\theta_i$. When a target is produced by an earlier operation, such as the copy created by a duplication, the predicate refers to that produced object, which the evaluator locates in the final state.

**Instruction Instantiation.** Once $S_{0,i}$ and the target and parameter assignments $t_i$ and $v_i$ are fixed, a deterministic compiler produces a complete concrete instruction. An LLM author then revises it into the final instruction $I_i$ for concision without changing the bound task specification. A separate LLM critic audits the revision against the original instruction, operation program, and predicate sets $P_i^+$ and $P_i^0$ before acceptance. See Appendix B for the prompts, model, and acceptance procedure.

**Task Assembly.** Together, the procedures above form an executable benchmark task $\mathcal{T}_i = \text{Instantiate}(M; \theta_i) = (S_{0,i}, I_i, P_i^+, P_i^0)$.

We automatically validate the task instance through a reference program derived from the task binding. This reference program is used only to verify task executability and evaluator consistency; it is neither exposed to the agent nor treated as a required GUI trajectory.

We instantiate 10 tasks from each of the 21 manually selected templates focused on timeline operations, and 5–10 tasks from each of the remaining 100 templates. After the automatic validation, the pipeline yields the final set of 781 [NAME C05] tasks, spanning 48 atomic operations and 121 task templates. We evaluate the quality of the generated tasks through the human validation study described in §4.3.

### 4.3 HUMAN VALIDATION OF GENERATED TASKS

We assess generated tasks through human annotation on meaningfulness, self-containedness/executability, and language quality. These criteria ask whether the request is plausible for a video-editing user, whether the required edit is determined by the instruction and initial state, and whether the instruction is clear and natural, respectively.

We evaluate 200 tasks with 10 annotators, with 60 tasks per annotator and three independent annotators per task. Annotators provide a binary Yes/No judgment for each criterion. Positive response rates are 96.2% for meaningfulness, 92.8% for self-containedness/executability, and 88.8% for language quality. Pairwise agreement is 92.3%, 88.0%, and 81.3% for the three criteria, respectively. Gwet's AC1 (Gwet, 2008), an inter-annotator agreement measure, is 0.917, 0.862, and 0.767, respectively.

## 5 PREDICATE-BASED PROJECT-STATE EVALUATION

The [NAME C05] evaluator judges an episode by comparing the structured project states before and after editing, rather than the agent's GUI trajectory or visual outputs such as rendered videos and screenshots, which are only partial observations of the project. In particular, because the predicates are instantiated from the same template and binding as the instruction, evaluation conditions come from the task itself. This alignment makes evaluation systematic, scoring every episode by the same deterministic rules over the same project-state representation.

### 5.1 EVALUATION FORMALIZATION

**Project State Representation.** When an episode begins and ends, we export the project as [NAME C05] JSON or Premiere Pro XML and parse it to obtain the initial state $S_0$ and the final state $S_T$. The parser extracts sequence settings, tracks, clips, text, transitions, media references, timeline positions, source timing, effects, and parameters, and converts temporal quantities to a common frame-based representation. Both [NAME C05] and Premiere Pro exports are converted into a common canonical representation and evaluated using the same predicate checks.

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

Object Identification. An object is an individually identifiable editable element. Video clips, audio clips, and text graphics are representative objects, while timing, effects, and parameters are expressed as attributes of these objects. We match objects across $S_0$ and $S_T$ by their object IDs in [NAME C05]. Since IDs are not reliably preserved in XML exports, we additionally use track, media-reference, and timing information in Premiere Pro. Split, duplicate, and insert operations create objects that exist only in $S_T$. For such targets, the evaluator identifies the new object produced by the corresponding operation, using its source media and expected interval, and then evaluates the predicates on that object.

## 5.2 SUCCESS CRITERION

Predicate Checks. Each predicate in $P^+$ and $P^0$ is evaluated on $(S_0, S_T)$ after its target is resolved. Numeric conditions, such as frame positions and effect parameters, are compared within explicit tolerances, whereas categorical values such as transition types and text content must match exactly. In the running example, the evaluator compares $S_0$ with $S_T$ to identify the newly created copy. $P^+$ checks whether the blur value is 60, $P^0$ checks whether the original clip was preserved.

Unauthorized-Change Audit. Preservation predicates protect only the state that a task explicitly declares, so the audit $U$ checks the rest of the project. It compares the full set of changes between $S_0$ and $S_T$, denoted $\Delta(S_0, S_T)$, with the changes authorized by the task's predicates, $A(P^+, P^0)$, and passes only if no unauthorized change remains:

$$U(S_0, S_T; P^+, P^0) = \mathbf{1}[\Delta(S_0, S_T) \setminus A(P^+, P^0) = \varnothing]. \tag{2}$$

In the running example, adding a text graphic fails $U$ even if all predicates hold.

## 5.3 METRICS

Success Rate. An episode succeeds only if all three checks pass.

$$\text{Success}(\mathcal{T}, S_T) = \left(\bigwedge_{p \in P^+} p(S_0, S_T)\right) \wedge \left(\bigwedge_{q \in P^0} q(S_0, S_T)\right) \wedge U(S_0, S_T; P^+, P^0). \tag{3}$$

This criterion leaves the editing route to the agent but is strict about the outcome: any sequence of GUI actions is accepted if the final project satisfies the request, preserves the protected state, and contains no unauthorized change.

Partial Progress. We compute request coverage and preservation coverage for every task, regardless of success. These metrics measure the fraction of requested conditions and preservation conditions satisfied in the final state.

$$\text{Cov}^+ = \frac{1}{|P^+|} \sum_{p \in P^+} \mathbf{1}[p(S_0, S_T)], \quad \text{Cov}^0 = \begin{cases} \frac{1}{|P^0|} \sum_{q \in P^0} \mathbf{1}[q(S_0, S_T)], & |P^0| > 0, \\ 1, & |P^0| = 0. \end{cases} \tag{4}$$

## 6 EXPERIMENTS

### 6.1 EXPERIMENTAL SETUP

We evaluate seven models on all 781 [NAME C05] tasks in [NAME C05]. The five proprietary models are GPT-6 Sol, GPT-5.6 Sol, GPT-6 Luna, GPT-5.6 Luna, and GPT-5.4 mini (OpenAI, b). The two open-weight GUI agents are UI-TARS-1.5-7B (Qin et al., 2025) and OpenCUA-7B (Wang et al., 2025).

We run all models through the [NAME C05] evaluation harness, which executes GUI actions and captures screenshots. GPT models use OpenAI's native computer tool (OpenAI, a), while UI-TARS and OpenCUA use their model-specific prompting and action formats. Agents receive the task instruction, screenshots, and interaction history, with a budget of 80 executed GUI actions per episode. Upon termination, we evaluate the final project state using success rate (SR), request coverage, and preservation coverage as defined in §5. Coverage is macro-averaged over tasks. Appendix C provides model-specific inference settings and history configurations.

## A-page-0008

target PDF page 8

Table 1: Performance of seven models on 781 [NAME C05] tasks in [NAME C05]. All values are percentages. Bold indicates the best value within each model group. Request and preservation coverage are macro-averaged over tasks.

[tbl-0.html](tbl-0.html)

![img-2.jpeg](img-2.jpeg)

![img-3.jpeg](img-3.jpeg)

Figure 3: Failure analysis. (a) Failure outcomes as percentages of all 781 tasks. (b) Request-condition failure rates within each editing category, ordered by decreasing mean failure rate across the seven models. Each category includes tasks with at least one corresponding request condition, with task counts in parentheses. Tasks may belong to multiple categories.

### 6.2 MAIN RESULTS

GPT-6 Sol achieves the highest success rate at 87.20%, followed by GPT-5.6 Sol at 84.25% (Table 1). Both Luna models outperform GPT-5.4 mini, while the two open-weight agents complete fewer than 5% of tasks. OpenCUA has higher request coverage but lower success than UI-TARS, showing that partial completion does not necessarily yield task success. Preservation coverage is high for proprietary models (96.94–99.82%) but lower for UI-TARS (85.70%) and OpenCUA (85.50%).

### 6.3 FAILURE ANALYSIS

Analysis procedure. We analyze failures at two levels: episode outcomes and individual editing conditions. Using the evaluator's checks on the initial and final project states, we distinguish failures involving unmet requests, preservation violations, or both. For these outcome groups, preservation violations include changes outside the permitted edits. We group request conditions into editing categories, such as timeline editing, text, and animation. A task belongs to a category if it contains at least one corresponding condition. For each category, we report the percentage of tasks with at least one unmet condition in that category. Tasks may belong to multiple categories. Appendix C.6 defines each editing category and details the conditions it includes.

Failure outcomes. Request-only failures are the largest group for all proprietary models, accounting for 89 of GPT-6 Sol's 100 failed episodes (Figure 3(a)). For OpenCUA, 426 of its 754 failed episodes involve both unmet requests and preservation violations, including unauthorized changes.

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
<table><tr><td>Model</td><td>SR (%)</td><td>Request coverage (%)</td><td>Preservation coverage (%)</td></tr><tr><td colspan="4">Proprietary models</td></tr><tr><td>GPT-6 Sol</td><td>87.20</td><td>91.11</td><td>99.82</td></tr><tr><td>GPT-5.6 Sol</td><td>84.25</td><td>89.38</td><td>99.52</td></tr><tr><td>GPT-6 Luna</td><td>71.45</td><td>77.98</td><td>99.25</td></tr><tr><td>GPT-5.6 Luna</td><td>69.01</td><td>75.85</td><td>98.91</td></tr><tr><td>GPT-5.4 mini</td><td>47.63</td><td>59.74</td><td>96.94</td></tr><tr><td colspan="4">Open-weight GUI agents</td></tr><tr><td>UI-TARS-1.5-7B</td><td>4.10</td><td>12.24</td><td>85.70</td></tr><tr><td>OpenCUA-7B</td><td>3.46</td><td>14.14</td><td>85.50</td></tr></table>

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

Editing categories. Figure 3(b) shows that both Sol models leave text conditions unmet relatively rarely, but encounter more failures in timeline editing and animation. GPT-6 Sol's failure rate is 1.09% for text, 16.89% for timeline editing, and 23.21% for animation. GPT-5.6 Sol shows the same ordering at 1.82%, 19.41%, and 39.29%, respectively. Timeline editing includes changes to clip timing, arrangement, and source selection, while animation requires specified parameter changes over time. The two open-weight agents show failures across all eight categories, with timeline-editing failure rates above 97% and unmet animation conditions in all 56 tasks in that category.

Case studies. In one [NAME C05] episode, UI-TARS is asked to set a clip's opacity to 60%. It repeats the same click action 48 times within an 80-action episode, yet the final opacity remains at 78%. All four preservation conditions are satisfied. In another, GPT-6 Sol applies the requested 10% left crop and attempts to adjust scale and position. It then declares completion, although the final state fails the framing condition. Supplementary analyses of action-budget exhaustion and task level appear in Appendix C.6 and Appendix C.5, respectively.

### 6.4 CROSS-EDITOR EVALUATION

We evaluate GPT-6 Sol and Luna on the same 56 tasks in [NAME C05] and Adobe Premiere Pro (Table 2). Sol achieves 83.93% success in [NAME C05] and 62.50% in Premiere, while Luna achieves 58.93% and 48.21%, respectively. Both models perform better in [NAME C05], with Sol outperforming Luna in both editors. The editors serve complementary purposes: [NAME C05] supports controlled, large-scale evalua-

tion through structured project-state checks, while Premiere extends the evaluation to a professional desktop editor. Appendix C.4 provides coverage results and execution details.

Table 2: Success rates (%) on the same 56 tasks in both editors.

[tbl-1.html](tbl-1.html)

### 6.5 HUMAN-AGENT COMPARISON

We recruited 10 graduate students with little or no prior video-editing experience and assigned each of the 100 tasks to two participants. Participants succeeded in 129 of 200 assignments (64.50%). On the same task set, both Sol and both Luna models achieve higher success rates than the human participants, while GPT-5.4 mini and the two open-weight agents score lower (Table 3). GPT-6 Sol achieves 92.00%, exceeding the human success rate by 27.50 percentage points on this task set. Scoring details and supplementary human coverage are provided in Appendix C.3.

Table 3: Success rates on the same 100 tasks, with two participant assignments per task for humans.

[tbl-2.html](tbl-2.html)

## 7 CONCLUSION

We introduced [NAME C05], a benchmark for [NAME C05] through the structured state of editable projects. [NAME C05] contains 781 tasks instantiated from 121 tutorial-grounded templates spanning 48 atomic editing operations. Its predicate-based evaluator verifies requested changes, required preservation, and unauthorized changes without requiring agents to follow a reference GUI trajectory or reproduce a single gold project. Experiments with seven computer-use agents reveal substantial differences in video-editing capability, with task success ranging from \(3.5\%\) to \(87.2\%\). The strongest model surpasses novice human editors on a 100-task subset (92.0% vs. 64.5%), whereas the evaluated open-weight agents remain below \(5\%\). Large-scale execution in [NAME C05] demonstrates the scalability of the benchmark, while evaluation on a matched subset in Adobe Premiere Pro examines its applicability to a professional editing environment. Together, these results show that structured project-state evaluation can support rigorous, systematic, and scalable assessment of video-editing agents while preserving the editability that distinguishes professional creative workflows from flattened-output generation.

[OCR table id=tbl-1.html; page=9]
<table><tr><td>Model</td><td>[NAME C05]</td><td>Premiere</td></tr><tr><td>GPT-6 Sol</td><td>83.93</td><td>62.50</td></tr><tr><td>GPT-6 Luna</td><td>58.93</td><td>48.21</td></tr></table>

[OCR table id=tbl-2.html; page=9]
<table><tr><td>Participant / model</td><td>SR (%)</td></tr><tr><td>Human</td><td>64.50</td></tr><tr><td>GPT-6 Sol</td><td>92.00</td></tr><tr><td>GPT-5.6 Sol</td><td>88.00</td></tr><tr><td>GPT-6 Luna</td><td>76.00</td></tr><tr><td>GPT-5.6 Luna</td><td>75.00</td></tr><tr><td>GPT-5.4 mini</td><td>57.00</td></tr><tr><td>UI-TARS-1.5-7B</td><td>9.00</td></tr><tr><td>OpenCUA-7B</td><td>6.00</td></tr></table>

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

In this work, we used generative AI tools for assisting with the generation of a synthetic benchmark dataset, providing feedback on the research methodology and experimental design, implementing methods, translation, cleaning and reformatting dataset, and interpreting results. We have not used generative AI tools for developing the conceptual framework, and formulating mathematical claims, providing critical ingredients for proving mathematical claims, developing or writing proofs, proposing or refining hypotheses, and qualitative or thematic data analysis are not applicable to this work. Additionally, we used generative AI tools to create and edit software code, search for and summarize relevant literature, prepare scientific figures and research artifacts, and revise the manuscript. We have reviewed all AI-assisted work. Each task and its initial instruction were generated deterministically from a tutorial-grounded structured specification, while generative AI was used to revise the instruction for clarity and concision. The revisions were checked against the fixed task conditions by an independent critic and deterministic rule-based validation, and AI-assisted code and reported results were verified through automated tests and saved evaluator outputs. We take responsibility for the final content of this work, including text, claims, code, data, figures, and artifacts produced with the aid of generative AI.

## REPRODUCIBILITY STATEMENT

We plan to publicly release the [NAME C05] code and benchmark artifacts upon acceptance, including the construction pipeline, the predicate-based evaluator, and [NAME C05] artifacts. We detail benchmark construction, evaluation, and implementation in §4, §5, and §6, with further details in Appendices A, B, and C. These resources are intended to support reproduction of our experiments and future evaluations of video-editing agents.

## REFERENCES

Jiaxin Ai, Yukang Feng, Fanrui Zhang, Jianwen Sun, Zizhen Li, Chuanhao Li, Yifan Chang, Wenxiao Wu, Ruoxi Wang, Mingliang Zhai, and Kaipeng Zhang. Prosoftarena: Benchmarking hierarchical capabilities of multi-modal agents in professional software environments. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 34586–34595, June 2026.

Yunpeng Bai, Yossi Gandelsman, Michaël Gharbi, and Qixing Huang. Instruction-based video editing by repurposing an image editing model, 2026. URL https://arxiv.org/abs/2608.14790.

Yinan Chen, Jiangning Zhang, Teng Hu, Yuxiang Zeng, Zhucun Xue, Qingdong He, Chengjie Wang, Yong Liu, Xiaobin Hu, and Shuicheng YAN. IVEBench: Modern benchmark suite for instruction-guided video editing assessment. In The Fourteenth International Conference on Learning Representations, 2026. URL [URL REDACTED]

Xiangbo Gao, Sicong Jiang, Bangya Liu, Xinghao Chen, Minglai Yang, Siyuan Yang, Mingyang Wu, Jiongze Yu, Qi Zheng, Haozhi Wang, et al. Vefx-bench: A holistic benchmark for generic video editing and visual effects. arXiv preprint arXiv:2604.16272, 2026.

Kilem L. Gwet. Computing inter-rater reliability and its variance in the presence of high agreement. British Journal of Mathematical and Statistical Psychology, 61(1):29–48, May 2008. doi: 10.1348/000711006X126600.

Haobo Hu, Xiangwu Guo, Zhiheng Chen, Difei Gao, Haotian Liu, Libiao Jin, and Qi Mao. Cut-Verse: A compositional GUI agents benchmark for media post-production editing. arXiv preprint arXiv:2605.19484, 2026. URL https://arxiv.org/abs/2605.19484.

Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik R Narasimhan. SWE-bench: Can language models resolve real-world github issues? In The Twelfth International Conference on Learning Representations, 2024. URL [URL REDACTED]

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

Xin Liang, Xiang Zhang, Yiwei Xu, Siqi Sun, and Chenyu You. Slidegen: Collaborative multimodal agents for scientific slide generation. arXiv preprint arXiv:2512.04529, 2025.

Kevin Qinghong Lin, Linjie Li, Difei Gao, Qinchen Wu, Mingyi Yan, Zhengyuan Yang, Lijuan Wang, and Mike Zheng Shou. VideoGUI: A benchmark for GUI automation from instructional videos. In Advances in Neural Information Processing Systems, volume 37, 2024. URL https://proceedings.neurips.cc/paper_files/paper/2024/hash/804e757b7d7043c26701c3a313032101-Abstract-Datasets_and_Benchmarks_Track.html.

Michael Ofengenden, Yunze Man, Ziqi Pang, Liang-Yan Gui, and Yu-Xiong Wang. PPTArena: A benchmark for PowerPoint editing. arXiv preprint arXiv:2512.03042, 2025. URL https://arxiv.org/abs/2512.03042v3.

OpenAI. Computer use. [URL REDACTED] a.

OpenAI. Openai models. [URL REDACTED] b.

OpenCut Project. OpenCut Classic. [URL REDACTED] Archived software repository, MIT License; accessed 2026-09-26.

Yujia Qin, Yining Ye, Junjie Fang, Haoming Wang, Shihao Liang, Shizuo Tian, Junda Zhang, Jiahao Li, Yunxin Li, Shijue Huang, et al. Ui-tars: Pioneering automated gui interaction with native agents. arXiv preprint arXiv:2501.12326, 2025.

Christopher Rawles, Sarah Clinckemaillie, Yifan Chang, Jonathan Waltz, Gabrielle Lau, Marybeth Fair, Alice Li, William E Bishop, Wei Li, Folawiyo Campbell-Ajala, Daniel Kenji Toyama, Robert James Berry, Divya Tyamagundlu, Timothy P Lillicrap, and Oriana Riva. Androidworld: A dynamic benchmarking environment for autonomous agents. In The Thirteenth International Conference on Learning Representations, 2025. URL [URL REDACTED]

Marcelo Sandoval-Castañeda, Bryan Russell, Josef Sivic, Gregory Shakhnarovich, and Fabian Caba Heilbron. Editduet: A multi-agent system for video non-linear editing. In Proceedings of the Special Interest Group on Computer Graphics and Interactive Techniques Conference (SIGGRAPH), 2025.

Chenrui Shi, Yuwei Wu, Yang Liu, Ruining Feng, Zirui Shang, Zhi Gao, Lifeng Fan, and Che Sun. Interactive reward agent: Gui task evaluation via environment-state verification, 2026. URL https://arxiv.org/abs/2607.25904.

Wenhao Sun, Rong-Cheng Tu, Jingyi Liao, and Dacheng Tao. Diffusion model-based video editing: A survey, 2024. URL https://arxiv.org/abs/2407.07111.

Wenxin Tang, Jingyu Xiao, Wenxuan Jiang, Xi Xiao, Yuhang Wang, Xuxin Tang, Qing Li, Yuehe Ma, Junliang Liu, Shisong Tang, and Michael R. Lyu. SlideCoder: Layout-aware RAG-enhanced hierarchical slide generation from design. In Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet Peng (eds.), Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pp. 9015–9039, Suzhou, China, November 2025. Association for Computational Linguistics. ISBN 979-8-89176-332-6. doi: 10.18653/v1/2025.emnlp-main.458. URL https://aclanthology.org/2025.emnlp-main.458/.

Harsh Trivedi, Tushar Khot, Mareike Hartmann, Ruskin Manku, Vinty Dong, Edward Li, Shashank Gupta, Ashish Sabharwal, and Niranjan Balasubramanian. AppWorld: A controllable world of apps and people for benchmarking interactive coding agents. In ACL, 2024.

Bryan Wang, Yuliang Li, Zhaoyang Lv, Haijun Xia, Yan Xu, and Raj Sodhi. Lave: Llm-powered agent assistance and language augmentation for video editing. arXiv preprint arXiv:2402.10294, 2024.

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

Xinyuan Wang, Bowen Wang, Dunjie Lu, Junlin Yang, Tianbao Xie, Junli Wang, Jiaqi Deng, Xiaole Guo, Yiheng Xu, Chen Henry Wu, Zhennan Shen, Zhuokai Li, Ryan Li, Xiaochuan Li, Junda Chen, Boyuan Zheng, Peihang Li, Fangyu Lei, Ruisheng Cao, Yeqiao Fu, Dongchan Shin, Martin Shin, Jiarui Hu, Yuyan Wang, Jixuan Chen, Yuxiao Ye, Danyang Zhang, Yipu Wang, Heng Wang, Diyi Yang, Victor Zhong, Y. Charles, Zhilin Yang, and Tao Yu. OpenCUA: Open foundations for computer-use agents. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025. URL [URL REDACTED]

Jiangtao Wu, Jiaming Wang, Yiwen He, Yuanxing Zhang, Shihao Li, Dunyuan Liu, Xuedong Zhao, Jialu Chen, Zekun Moore Wang, and Jiaheng Liu. Covebench: Can video editing models handle complex instructions?, 2026. URL https://arxiv.org/abs/2606.08415.

Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Toh Jing Hua, Zhoujun Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese, Caiming Xiong, Victor Zhong, and Tao Yu. Osworld: Benchmarking multimodal agents for open-ended tasks in real computer environments, 2024.

Ximing Xing, Ziteng Xue, Zhenxi Li, Weicong Liang, Linqing Wang, Zhantao Yang, Tiankai Hang, Zijin Yin, Qinglin Lu, Chunyu Wang, and Qian Yu. Hierarchical svg tokenization: Learning compact visual programs for scalable vector graphics modeling. arXiv preprint arXiv:2604.05072, 2026.

Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, and Graham Neubig. Webarena: A realistic web environment for building autonomous agents. In The Twelfth International Conference on Learning Representations, 2024. URL [URL REDACTED]

## A-page-0013

target PDF page 13

# A BENCHMARK CONSTRUCTION DETAILS

## A.1 ATOMIC OPERATION VOCABULARY

An atomic operation is the smallest change to a project that can be requested on its own, regardless of the editor used. One operation may require several GUI actions. For example, splitting a clip with a keyboard shortcut or a razor tool counts as the same operation, split_clip. A standard trim and a ripple trim are separate operations because they affect the surrounding timeline differently. Table 4 lists all 48 operations.

Table 4: The 48 atomic operations in [NAME C05], grouped by the type of edit.

[tbl-3.html](tbl-3.html)

Some operations cover more than one interface action. For example, set_parameter_keyframe includes both creating a keyframe and updating an existing one. Tasks combine these operations in an ordered sequence, but each combination is not counted as a new atomic operation.

## A.2 OPERATION-TO-INTERFACE MAPPING

Tables 5 and 6 show the controls available for each operation. OpenCut Classic already supported 29 operations. We added or modified controls in [NAME C05] for the remaining 19. Agents may use any valid interaction sequence, including routes other than those listed in the tables.

We tested the added and modified controls with 178 native and browser tests. These check timing and source ranges, preservation of unrelated objects, rejection of invalid edits, undo and redo, and saving and restoring project state. All 178 tests passed in the experiment configuration.

Two dataset operations reuse existing controls: move_clip_group uses the route for move_clip, and replace_clip_preserve_timing uses the route for replace_clip.

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

[OCR table id=tbl-3.html; page=13]
<table><tr><th>Family</th><th>Count</th><th>Atomic operations</th></tr><tr><td>Timeline editing</td><td>20</td><td>split_clip, trim_clip_start, trim_clip_end, delete_clip, delete_gap, move_clip, duplicate_clip, insert_clip, rearrange_clip, ripple_delete_clip, slip_clip, roll_edit, slide_clip, ripple_trim_start, ripple_trim_end, connect_insert_clip, overwrite_clip, replace_clip, replace_clip_preserve_timing, move_clip_group</td></tr><tr><td>Visual layout and effects</td><td>8</td><td>set_scale, set_position, set_rotation, set_opacity, set_crop_side, set_clip_effect, set_dynamic_zoom, frame_clip</td></tr><tr><td>Playback</td><td>2</td><td>set_speed, set_reverse</td></tr><tr><td>Text and graphics</td><td>11</td><td>create_text_graphic, set_text_content, set_text_position, trim_text_start, trim_text_end, delete_text_graphic, set_font_family, set_font_size, set_font_weight, set_text_color, set_text_alignment</td></tr><tr><td>Video transitions</td><td>3</td><td>apply_video_transition, remove_video_transition, set_video_transition_duration</td></tr><tr><td>Keyframes</td><td>1</td><td>set_parameter_keyframe</td></tr><tr><td>Audio editing</td><td>2</td><td>set_audio_gain, set_audio_fades</td></tr><tr><td>Timeline markers</td><td>1</td><td>add_timeline_marker</td></tr><tr><td>Total</td><td>48</td><td></td></tr></table>

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

Table 5: Base [NAME C05] operation-to-interface mapping (29 operations).

[tbl-4.html](tbl-4.html)

Table 6: [NAME C05] workflow-extension mapping (19 operations).

[tbl-5.html](tbl-5.html)

### A.3 TASK TEMPLATE INVENTORY

Of the 121 task templates, 95 come from executable, contiguous subworkflows in the source tutorials. We added 26 tutorial-grounded compositions to cover additional atomic operations. Each template stores an ordered sequence of operations from Appendix A.1.

The list below groups templates by their main requested edit. Templates spanning several editing families appear only once. We use workflow names where available and operation sequences otherwise. The group counts sum to 121.

#### Timeline structure and source selection (35).

close-rejected-interval-gap;
complete-chronological-story-insert; connect_insert_clip;
curate-selects; curate-selects-boundary; delete_clip + delete_gap; duplicate_clip; insert_clip + insert_clip;
middle-shot-placement-and-passage; move-shot-into-free-space;
narrative-rough-cut-repair; open-interval-with-group-offset;
overwrite_clip; remove-obsolete-editorial-note;
remove-unwanted-occurrence-preserve-timing;
reorder-story-clips; replace_clip; restore-hard-cut;
revised-v2-ordered-excerpts; ripple-end-sequence-continuity;
ripple_trim_start; roll-shared-edit; slip-source-content;

[OCR table id=tbl-4.html; page=14]
<table><tr><td>Operations</td><td>Available UI route</td></tr><tr><td>split_clip</td><td>Clip and playhead → Split</td></tr><tr><td>trim_clip_start, trim_clip_end, trim_text_start, trim_text_end</td><td>Drag the object's left or right edge</td></tr><tr><td>delete_clip, delete_text_graphic, delete_gap</td><td>Select object or gap → Delete</td></tr><tr><td>move_clip, duplicate_clip, insert_clip</td><td>Drag, Duplicate, or Asset → Insert</td></tr><tr><td>set_scale, set_position, set_rotation, set_crop_side, set_opacity</td><td>Clip → Properties → Transform, Crop, or Blending</td></tr><tr><td>set_speed, set_reverse</td><td>Clip → Properties → Speed</td></tr><tr><td>create_text_graphic, set_text_content, set_text_position, set_font_family, set_font_size, set_font_weight, set_text_color, set_text_alignment</td><td>Text panel or selected text → Properties</td></tr><tr><td>apply_video_transition, remove_video_transition, set_video_transition_duration</td><td>Timeline transition control or Properties → Transition</td></tr></table>

[OCR table id=tbl-5.html; page=14]
<table><tr><td>Operations</td><td>Available UI route</td></tr><tr><td>ripple_trim_start, ripple_trim_end</td><td>Properties → Ripple Trim</td></tr><tr><td>ripple_delete_clip</td><td>Clip context menu → Ripple Delete</td></tr><tr><td>roll_edit, slip_clip, slide_clip</td><td>Properties → Native Trim → mode</td></tr><tr><td>rearrange_clip</td><td>Clip context menu → Rearrange</td></tr><tr><td>overwrite_clip, replace_clip</td><td>Asset menu → Overwrite or Replace</td></tr><tr><td>connect_insert_clip</td><td>Asset menu → Connect</td></tr><tr><td>frame_clip</td><td>Properties → Framing</td></tr><tr><td>set_clip_effect</td><td>Properties → Effects</td></tr><tr><td>set_parameter_keyframe</td><td>Property diamond and keyframe value field</td></tr><tr><td>set_dynamic_zoom</td><td>Properties → Dynamic Zoom</td></tr><tr><td>set_audio_gain, set_audio_fades</td><td>Properties → Audio or Audio Fade</td></tr><tr><td>add_timeline_marker</td><td>Playhead → marker control</td></tr></table>

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

slip-then-slide-middle-passage; split_clip + delete_clip;
split_clip + split_clip + delete_clip + delete_gap;
state-grounded-v1-ordered-story-sections;
story-relocation-entrance-continuity; trim_clip_start;
v6-dv01-t5; v6-dv02-t1; v6-dv02-t3; v6-tt-extend-clip-edge;
v6-tt-instant-replay; v6-tt-jump-cut-condensation.

Visual properties, playback, and transitions (20).

apply-adjustable-effect; apply_video_transition + set_video_transition_duration; crop-distracting-edge; edge-cleanup-fill; focused-mixed-v1-bounded-blur-treatment; focused-mixed-v2-interior-passage-reverse; grounded-additional-v1-interior-rejection; grounded-additional-v1-purpose-04; grounded-additional-v1-purpose-06; position-shot-within-canvas; reverse-footage; revised-v2-three-shot-full-image-fit; scoped-shot-scale; selected-shot-opacity; shot-rotation-existing-anchor; soft-full-canvas-backing; soften-two-shot-cut; spatially-conform-footage; two-shot-dissolve-duration; v6-tt-constant-speed-change.

Text and graphics (50).

create_text_graphic + set_font_family; create_text_graphic + set_font_family + set_font_weight; create_text_graphic + set_font_family + set_font_weight + set_font_size; create_text_graphic + set_font_family + set_font_weight + set_font_size + set_text_color + set_text_position + trim_text_end; create_text_graphic + set_text_content; create_text_graphic + set_text_content + set_font_family; create_text_graphic + set_text_content + set_font_family + set_font_weight; create_text_graphic + set_text_content + set_font_family + set_font_weight + set_font_size + set_text_alignment + set_text_color + set_text_position + trim_text_start + trim_text_end; opening-identification; opening-identification-alignment; opening-identification-font-size; opening-identification-position; opening-identification-start-trim; opening-identification-trim-end; opening-title-color; opening-title-font-family; opening-title-normal-weight; revise-existing-editorial-note; set_font_family + set_font_weight; set_font_family + set_font_weight + set_font_size; set_font_family + set_font_weight + set_font_size + set_text_alignment; set_font_family + set_font_weight + set_font_size + set_text_color; set_font_size + set_text_alignment; set_font_size + set_text_alignment + set_text_color; set_font_size + set_text_alignment + set_text_color + set_text_position; set_font_size + set_text_color; set_font_size + set_text_color + set_text_position; set_font_size + set_text_color + set_text_position + trim_text_end; set_font_weight + set_font_size; set_font_weight + set_font_size + set_text_alignment; set_font_weight + set_font_size + set_text_alignment + set_text_color; set_font_weight + set_font_size + set_text_color; set_font_weight + set_font_size + set_text_color + set_text_position; set_text_alignment + set_text_color; set_text_alignment + set_text_color + set_text_position; set_text_alignment + set_text_color + set_text_position + trim_text_start; set_text_color + set_text_position; set_text_color + set_text_position +

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

trim_text_end; set_text_color + set_text_position +
trim_text_start; set_text_color + set_text_position +
trim_text_start + trim_text_end; set_text_content +
set_font_family; set_text_content + set_font_family +
set_font_weight; set_text_content + set_font_family +
set_font_weight + set_font_size; set_text_position +
trim_text_end; set_text_position + trim_text_start;
set_text_position + trim_text_start + trim_text_end;
shot-timed-horizontal-title; trim_text_start + trim_text_end;
v6-tt-animated-secondary-credit; v6-tt-timed-closing-title.

#### Audio, animation, and markers (16).

adjust-clip-volume; animate-opening-logo; fade-audio-boundary; grounded-audio-db-v3-p05; incoming-passage-shared-cut; interior-passage-ripple-trims; keyframe-audio-property; movie-opening-identification; movie-opening-identification (variant 2); nudge-clip-exactly; purpose-mixed-db-v1-p08; selects-navigation-marker; set_parameter_keyframe + set_parameter_keyframe; v6-fc09-t2; v6-tt-build-continuous-ambience; v6-tt-duck-music-under-dialogue.

### A.4 BASE TIMELINE LAYOUTS

[NAME C05] constructs initial project states from eight reusable, declarative layout specifications rather than creating each project independently (Table 7). Each specification defines the canvas, frame rate, tracks, objects, and initial intervals. Task materialization binds concrete media and task identifiers while retaining the selected layout's structure and timing. All layouts use 24 fps. Cross-dissolve variants are obtained by adding a transition to the two-clip layout and are therefore not counted as additional base layouts.

Table 7: Reusable base timeline layouts. Clip and text intervals are in frames.

[tbl-6.html](tbl-6.html)

Operation-to-layout compatibility is determined before task instantiation. For example, text-editing templates require a layout containing a text object, whereas two-clip ordering templates require two adjacent clips. This filtering prevents structurally incompatible task bindings.

## B INSTRUCTION REVISION AND VERIFICATION DETAILS

We first fix the initial project, operation sequence, targets, parameter values, and request and preservation predicates. A deterministic compiler uses these fields to write the initial instruction. We then

[OCR table id=tbl-6.html; page=16]
<table><tr><td>Layout</td><td>Canvas</td><td>Objects</td><td>Initial arrangement</td></tr><tr><td>One clip</td><td>\( 1920 \times 1080 \)</td><td>1 video</td><td>One V1 clip in [0, 598).</td></tr><tr><td>Wide-canvas one clip</td><td>\( 1280 \times 720 \)</td><td>1 video</td><td>One V1 clip in [0, 598); varies project resolution.</td></tr><tr><td>Two clips</td><td>\( 1920 \times 1080 \)</td><td>2 video</td><td>Contiguous V1 clips in [0, 598) and [598, 983).</td></tr><tr><td>Three clips</td><td>\( 1920 \times 1080 \)</td><td>3 video</td><td>Contiguous V1 clips in [0, 400), [400, 700), and [700, 950).</td></tr><tr><td>Short gap</td><td>\( 1920 \times 1080 \)</td><td>2 video</td><td>V1 clips in [0, 360) and [420, 805); a 60-frame gap.</td></tr><tr><td>Long gap</td><td>\( 1920 \times 1080 \)</td><td>2 video</td><td>V1 clips in [0, 240) and [420, 720); a 180-frame gap.</td></tr><tr><td>One title</td><td>\( 1920 \times 1080 \)</td><td>1 video, 1 text</td><td>One V1 clip and one title in [72, 240).</td></tr><tr><td>Two titles</td><td>\( 1920 \times 1080 \)</td><td>1 video, 2 text</td><td>One V1 clip and distinguishable titles in [24, 120) and [200, 360).</td></tr></table>

## A-page-0017

target PDF page 17

ask a language-model author to shorten the wording and a separate critic to check it against the same specification. Only the instruction is revised.

### B.1 INPUTS TO THE AUTHOR AND CRITIC

The inputs are listed in Table 8. The author works from the original instruction and task specification. The critic receives both, along with the proposed revision. Evaluation conditions are available to these two models during dataset construction. They are not shown to the agent that performs the task.

Table 8: Inputs to instruction revision and verification.

[tbl-7.html](tbl-7.html)

### B.2 AUTHOR PROMPT

The author is asked to remove unnecessary wording while keeping the requested edits and constraints. We reproduce the prompt below, with the output-schema description abbreviated.

Rewrite each original English instruction as the shortest clear natural request that remains faithful to the supplied concrete specification and evaluator conditions. Keep every requested change, target identifier, independent quantity, source range, title string, necessary neighboring consequence, and non-default property. Preserve operation order only where the requested outcome depends on it, and do not prescribe a unique GUI trajectory.

Treat ordinary preservation of unrelated state as implicit. Remove redundant lists of unchanged media, properties, audio settings, or tracks, and do not replace them with a generic ``leave everything else unchanged.'' Keep an explicit preservation clause only when omitting it permits a materially different valid edit, including gap versus ripple behavior, fixed outer bounds, source-range versus timeline movement, aspect ratio, static versus animated controls, keyframe interpolation, or another stated editorial constraint.

Do not invent semantic video content or repair a questionable specification by adding requirements. If a condition is surprising, conflicting, implementation-dependent, or invalid, report it for specification review. Return the task ID, the complete revised instruction, a brief account of removed boilerplate and retained disambiguation, and any specification concerns.

### B.3 INDEPENDENT CRITIC PROMPT

The critic checks each request and preservation condition against the revised instruction. Its response records how each condition is covered, using one of the four labels defined in the prompt below.

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

[OCR table id=tbl-7.html; page=17]
<table><tr><td>Field</td><td>Information supplied to the model</td></tr><tr><td>Task metadata</td><td>Exact task identity and task purpose, when available</td></tr><tr><td>Original instruction</td><td>Complete instruction produced before concise revision</td></tr><tr><td>Initial state</td><td>Abstract initial requirements and the materialized initial project</td></tr><tr><td>Operation program</td><td>Ordered operations, dependencies, targets, and parameters</td></tr><tr><td>Request conditions</td><td>Every requested final-state condition with a stable condition ID</td></tr><tr><td>Preservation conditions</td><td>Every protected-state condition with a stable condition ID</td></tr><tr><td>Evaluator context</td><td>Clarifications needed to interpret condition fields and temporal signs</td></tr></table>

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
971[{"box_2d": [187, 113, 792, 178], "label":caption", "text", "Independently audit each revised instruction against its original task packet under the same concise-instruction policy. Check every target, value, range, default, audio state, and required neighboring consequence. Do not pass an instruction merely because it is shorter, and flag specification defects rather than masking them."}]

For every supplied condition ID, assign exactly one coverage mode: explicit, implied_by_request, ordinary_preservation, or missing_or_invalid. Quote an exact instruction substring as evidence for explicit or implied coverage, and give a short justification for every mode. Ordinary preservation may normally cover only preservation conditions, never an omitted primary request.

Return a verdict of pass, revise, or spec_review, concrete issues, the complete condition-by-condition coverage record, and Boolean checks that redundant boilerplate was removed and no unsupported requirement was added.

### B.4 ACCEPTANCE GATE AND MODEL

We accept an instruction only if the author reports no specification concerns and the critic returns pass with no issues. The critic must also confirm that the revision removes redundant wording and adds no unsupported requirements. These judgments are followed by checks in code. Every condition ID must have exactly one coverage record and a justification, and the instruction must be nonempty. Explicit and implied coverage require a quote from the revised text. A request condition labeled as ordinary preservation causes rejection.

GPT-6 Astra serves as both author and critic. Each batch contains ten tasks, with at most two author-critic attempts per unresolved task in a run. Accepted revisions are kept without further generation. We save the requests and parsed responses, then check the output files before release. These checks cover the schema, task-set membership, condition coverage, and provenance hashes. We also compare the files with the originals: only the instruction and its provenance metadata may change. The operation program, initial state, targets, parameters, predicates, and evaluator must remain unchanged.

## C SUPPLEMENTARY EXPERIMENTAL DETAILS

### C.1 EXECUTION SETTINGS

[NAME C05] episodes run in a  \( 1280 \times 720 \)  viewport with a limit of 80 actions. For Premiere, screenshots are resized to at most 1280 pixels on the longer side. The [NAME C05] Guide is accessible through an on-screen toggle, rather than included in full in the initial prompt.

Table 9: Model inference settings for OpenCut experiments. Output limits are in tokens per response.

[tbl-8.html](tbl-8.html)

All GPT models use medium reasoning effort and retain conversation history through the provider. UI-TARS receives the current screenshot and text action history. OpenCUA retains three screenshots.

[OCR table id=tbl-8.html; page=18]
<table><tr><td>Model</td><td>Reasoning effort</td><td>Output limit</td><td>History</td></tr><tr><td>GPT-6 Sol</td><td>Medium</td><td>4,096</td><td>Stateful</td></tr><tr><td>GPT-5.6 Sol</td><td>Medium</td><td>4,096</td><td>Stateful</td></tr><tr><td>GPT-6 Luna</td><td>Medium</td><td>4,096</td><td>Stateful</td></tr><tr><td>GPT-5.6 Luna</td><td>Medium</td><td>4,096</td><td>Stateful</td></tr><tr><td>GPT-5.4 mini</td><td>Medium</td><td>4,096</td><td>Stateful</td></tr><tr><td>UI-TARS-1.5-7B</td><td>Not used</td><td>1,024</td><td>Current image</td></tr><tr><td>OpenCUA-7B</td><td>Not used</td><td>4,096</td><td>Three images</td></tr></table>

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

### C.2 AGENT PROMPT

The GPT initial prompt is shown below. UI-TARS and OpenCUA use their native prompt formats with the same Guide and timebase guidance.

You are operating the OpenCut Classic web video editor in Chromium.
If you are unsure how to use a feature, please consult the Guide toggle above. Search the guide for explanations of most features. Also note that the timeline runs at 24 fps: 40 frames corresponds to 00:00:01:16.
Use the computer tool and inspect each resulting screenshot.
Instruction: {natural_instruction}
Remaining action budget: 80
Use only what is visible in the screenshots. Do not guess hidden evaluation criteria.
When the instruction is fully satisfied and visibly confirmed, stop issuing actions and reply with a short message stating the task is complete.

### C.3 HUMAN COMPARISON

Human success rate is computed over all 200 assignments, with skipped assignments counted as failures. Participants succeeded in 129 assignments (64.50%). Supplementary coverage is computed from the 186 completed attempts. We average coverage across completed attempts within each task and then across all 100 tasks, each of which has at least one completed attempt. This gives request coverage of 79.36% and preservation coverage of 98.08%. All completed attempts are evaluated using the same task predicates and evaluator as the agents.

### C.4 CROSS-EDITOR EVALUATION

OpenCut provides an on-screen Guide and is evaluated through project-state JSON, while Premiere is evaluated through exported XML. The final Premiere results include 35 successes and 21 failures for GPT-6 Sol, and 27 successes and 29 failures for GPT-6 Luna. Coverage is averaged over all 56 tasks, assigning preservation coverage of one to the nine tasks without preservation conditions.

Table 10: Performance on the same 56 tasks in OpenCut and Adobe Premiere Pro. All values are percentages and coverage is macro-averaged over tasks.

[tbl-9.html](tbl-9.html)

[OCR table id=tbl-9.html; page=19]
<table><tr><td>Model</td><td>Editor</td><td>SR</td><td>Request cov.</td><td>Preservation cov.</td></tr><tr><td rowspan="2">GPT-6 Sol</td><td>OpenCut</td><td>83.93</td><td>86.43</td><td>100.00</td></tr><tr><td>Premiere</td><td>62.50</td><td>73.30</td><td>98.97</td></tr><tr><td rowspan="2">GPT-6 Luna</td><td>OpenCut</td><td>58.93</td><td>62.80</td><td>97.77</td></tr><tr><td>Premiere</td><td>48.21</td><td>61.85</td><td>94.84</td></tr></table>

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

### C.5 TASK-LEVEL RESULTS

Task level denotes the number of atomic operations in a task. Success rates do not decrease monotonically with level because the groups differ in operation composition. Levels 5–10 contain only 4–10 tasks each.

Table 11: Success rates (%) by task level. Task level is the number of atomic operations in a task.

[tbl-10.html](tbl-10.html)

Entries are success rates (%). Task counts are identical across models.

### C.6 FAILURE ANALYSIS DETAILS

We analyze saved evaluator results for all seven models on 781 tasks, covering 5,467 OpenCut episodes.

Episode outcomes. Failed episodes in Figure 3(a) are assigned to three mutually exclusive groups. Request only indicates unmet request conditions without preservation violations. Preservation only indicates satisfied request conditions with preservation violations, including unrequested changes. Both indicates violations of both kinds.

Editing categories. The eight categories below group conditions by editing functionality. A task may contribute to multiple categories. Text timing belongs to timeline editing, while text content and style belong to text. Fixed visual settings belong to visual properties, while changes to those settings over time belong to animation.

[tbl-11.html](tbl-11.html)

Action-budget exhaustion. UI-TARS and OpenCUA exhaust the 80-action budget on 63.51% and 75.93% of tasks, compared with 2.18% for GPT-6 Sol and 18.31% for GPT-5.4 mini (Table 12). These termination counts overlap the predicate-based failure categories.

[OCR table id=tbl-10.html; page=20]
<table><tr><td>Level</td><td>Tasks</td><td>GPT-6 Sol</td><td>GPT-5.6 Sol</td><td>GPT-6 Luna</td><td>GPT-5.6 Luna</td><td>GPT-5.4 mini</td><td>UI-TARS</td><td>OpenCUA</td></tr><tr><td>1</td><td>303</td><td>92.74</td><td>89.44</td><td>84.49</td><td>79.21</td><td>57.76</td><td>8.25</td><td>7.92</td></tr><tr><td>2</td><td>166</td><td>80.72</td><td>84.94</td><td>51.81</td><td>54.22</td><td>42.77</td><td>4.22</td><td>1.81</td></tr><tr><td>3</td><td>207</td><td>83.57</td><td>78.26</td><td>63.77</td><td>61.84</td><td>40.10</td><td>0.00</td><td>0.00</td></tr><tr><td>4</td><td>71</td><td>94.37</td><td>88.73</td><td>90.14</td><td>83.10</td><td>59.15</td><td>0.00</td><td>0.00</td></tr><tr><td>5</td><td>4</td><td>100.00</td><td>100.00</td><td>75.00</td><td>100.00</td><td>25.00</td><td>0.00</td><td>0.00</td></tr><tr><td>6</td><td>5</td><td>100.00</td><td>40.00</td><td>100.00</td><td>100.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>7</td><td>5</td><td>100.00</td><td>100.00</td><td>40.00</td><td>100.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>8</td><td>10</td><td>40.00</td><td>40.00</td><td>40.00</td><td>40.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>9</td><td>5</td><td>60.00</td><td>20.00</td><td>20.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>10</td><td>5</td><td>100.00</td><td>100.00</td><td>100.00</td><td>80.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr></table>

[OCR table id=tbl-11.html; page=20]
<table><tr><td>Category</td><td>Editing requirements</td></tr><tr><td>Timeline editing</td><td>Set clip or text timing and source intervals. Insert, delete, move, split, duplicate, connect, or replace clips, and maintain the required order and continuity.</td></tr><tr><td>Visual properties</td><td>Set framing, position, scale, crop, opacity, and other fixed effect parameters.</td></tr><tr><td>Text</td><td>Create or remove text elements and set their content and style.</td></tr><tr><td>Animation</td><td>Vary clip parameters over time using keyframes, curves, waypoints, or dynamic zoom.</td></tr><tr><td>Transitions</td><td>Add or remove transitions and set their duration.</td></tr><tr><td>Audio</td><td>Set volume and fades, or preserve whether embedded audio is enabled.</td></tr><tr><td>Playback</td><td>Set playback speed or reverse direction.</td></tr><tr><td>Markers</td><td>Place timeline markers with the required attributes.</td></tr></table>

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

Table 12: Episodes reaching the 80-action limit out of 781 tasks per model. Reaching the limit does not necessarily indicate task failure.

[tbl-12.html](tbl-12.html)

[OCR table id=tbl-12.html; page=21]
<table><tr><td>Model</td><td>Episodes</td><td>Rate (%)</td></tr><tr><td>GPT-6 Sol</td><td>17</td><td>2.18</td></tr><tr><td>GPT-5.6 Sol</td><td>50</td><td>6.40</td></tr><tr><td>GPT-6 Luna</td><td>101</td><td>12.93</td></tr><tr><td>GPT-5.6 Luna</td><td>102</td><td>13.06</td></tr><tr><td>GPT-5.4 mini</td><td>143</td><td>18.31</td></tr><tr><td>UI-TARS-1.5-7B</td><td>496</td><td>63.51</td></tr><tr><td>OpenCUA-7B</td><td>593</td><td>75.93</td></tr></table>
