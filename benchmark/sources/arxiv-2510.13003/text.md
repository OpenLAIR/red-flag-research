# OPLoRA: Orthogonal Projection LoRA Prevents Catastrophic Forgetting during Parameter-Efficient Fine-Tuning

## B-23bc2979dd2f4c

https://arxiv.org/html/2510.13003v1#chars-14775-15492

### Preserving Pre-trained Knowledge via Orthogonal Projection

To avoid disrupting the dominant directions of W0W\_{0}, we confine the LoRA update to the orthogonal complement of its top-kk subspace.
Let Uk∈ℝdout×kU\_{k}\in\mathbb{R}^{d\_{\text{out}}\times k} be the matrix of the top-kk left singular vectors of W0W\_{0} (kk is a hyperparameter). Define the orthogonal projector onto the complement of span​{Uk}\text{span}\{U\_{k}\}

|  |  |  |  |
| --- | --- | --- | --- |
|  | P=I−Uk​Uk⊤.P=I-U\_{k}U\_{k}^{\top}. |  | (6) |

We will show that the LoRA update Δ​W=P​B​A\Delta W=PBA is entirely confined to this complementary subspace, ensuring it contains no components along the dominant kk singular directions.

## B-29beda4865fcfa

https://arxiv.org/html/2510.13003v1#chars-16158-18920

#### Proof.

We first verify that PP is a projection matrix: P2=(I−Uk​Uk⊤)2=I−2​Uk​Uk⊤+Uk​Uk⊤​Uk​Uk⊤=I−Uk​Uk⊤=P,P^{2}=(I-U\_{k}U\_{k}^{\top})^{2}=I-2U\_{k}U\_{k}^{\top}+U\_{k}U\_{k}^{\top}U\_{k}U\_{k}^{\top}=I-U\_{k}U\_{k}^{\top}=P, since Uk⊤​Uk=IU\_{k}^{\top}U\_{k}=I.

Now for any input x∈ℝdinx\in\mathbb{R}^{d\_{\text{in}}}, the LoRA output is Δ​W​x=P​B​A​x.\Delta Wx=PBAx.
We show that this vector is orthogonal to span​(Uk)\text{span}(U\_{k}) by checking:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uk⊤​(P​B​A​x)\displaystyle U\_{k}^{\top}(PBAx) | =Uk⊤​(I−Uk​Uk⊤)​B​A​x\displaystyle=U\_{k}^{\top}(I-U\_{k}U\_{k}^{\top})BAx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(Uk⊤−Uk⊤​Uk​Uk⊤)​B​A​x\displaystyle=(U\_{k}^{\top}-U\_{k}^{\top}U\_{k}U\_{k}^{\top})BAx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(Uk⊤−Uk⊤)​B​A​x\displaystyle=(U\_{k}^{\top}-U\_{k}^{\top})BAx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =0.\displaystyle=0. |  |

Hence, Δ​W​x∈span​(Uk)⟂\Delta Wx\in\text{span}(U\_{k})^{\perp}, and the LoRA update does not interfere with the dominant subspace of the original weight matrix.
■\blacksquare

While Proposition 1 guarantees that the LoRA update Δ​W=P​B​A\Delta W=PBA does not inject any output into the top-kk left singular directions of W0W\_{0}, it is natural to ask whether any stronger preservation property holds. In particular, does the use of the projection P=I−Uk​Uk⊤P=I-U\_{k}U\_{k}^{\top} preserve the original singular vectors uiu\_{i} or the singular values σi\sigma\_{i}?

The answer is no. Even though Δ​W​x\Delta Wx is orthogonal to span​(Uk)\text{span}(U\_{k}) for every xx, this alone does not guarantee that adding Δ​W\Delta W preserves the top-kk singular vectors or singular values of the updated weight matrix W′=W0+Δ​WW^{\prime}=W\_{0}+\Delta W. To see this, assume for contradiction that W′​ui=σi​viW^{\prime}u\_{i}=\sigma\_{i}v\_{i} for some i≤ki\leq k. Then we would imply

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​W​ui=W′​ui−W0​ui=σi​vi−σi​vi=0.\Delta Wu\_{i}=W^{\prime}u\_{i}-W\_{0}u\_{i}=\sigma\_{i}v\_{i}-\sigma\_{i}v\_{i}=0. |  | (8) |

However, this conclusion does not follow from Proposition 1, because Δ​W​ui\Delta Wu\_{i} need not be zero—it only lies in span​(Uk)⟂\text{span}(U\_{k})^{\perp}. Hence, the top-kk left singular vectors of W0W\_{0} are generally not preserved.

This leads to a stronger goal: can we preserve each complete singular triple (ui,σi,vi)(u\_{i},\sigma\_{i},v\_{i})? We can — by projecting on both sides.
Constraining Δ​W\Delta W to the orthogonal complements of the top-kk left and right singular subspaces guarantees that the top-
kk singular vectors and singular values of
W0W\_{0} remain intact. We now state and prove this claim formally.

## B-33af5c75a31b2f

https://arxiv.org/html/2510.13003v1#chars-38133-39043

## References

![[LOGO]](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)

## B-3a8297d6abf829

https://arxiv.org/html/2510.13003v1#chars-22691-24224

## Experiments

We conduct comprehensive experiments to evaluate the effectiveness of OPLoRA in preventing catastrophic forgetting while maintaining competitive fine-tuning performance. Our comparisons include four LoRA-based baselines: LoRA ([Hu et al. 2022](#bib.bib15)), PiSSA ([Meng, Wang, and Zhang 2024](#bib.bib24)), MiLoRA ([Wang et al. 2024](#bib.bib32)), and LoRA-Null ([Tang et al. 2025](#bib.bib30)). Each method is evaluated across three task domains, commonsense reasoning, mathematics, and Python code generation, using two backbone models: LLaMA-2 7B ([Touvron et al. 2023](#bib.bib31)) and Qwen2.5 7B ([Yang et al. 2025a](#bib.bib33)). All methods are trained under the same hyperparameter configuration for fair comparison, with LoRA applied to the self-attention and MLP layers, specifically targeting the modules 𝚚​\_​𝚙𝚛𝚘𝚓,𝚟​\_​𝚙𝚛𝚘𝚓,𝚞𝚙​\_​𝚙𝚛𝚘𝚓,𝚍𝚘𝚠𝚗​\_​𝚙𝚛𝚘𝚓,𝚘​\_​𝚙𝚛𝚘𝚓\mathtt{q\\_proj},\mathtt{v\\_proj},\mathtt{up\\_proj},\mathtt{down\\_proj},\mathtt{o\\_proj}.
For OPLoRA, we fix the projection rank kk to two values, k=16k=16 and k=128k=128, across all experiments. These ranks are not tuned for performance and are chosen to represent low and high subspace preservation regimes. Exploration of optimal projection rank selection is left for future work.

| Method | SVD Without WresW\_{\text{res}} | Forgetting Mitigation |
| --- | --- | --- |
| LoRA | ×\times | ×\times |
| PiSSA | ×\times | ×\times |
| MiLoRA | ×\times | ×\times |
| LoRA-Null | ×\times | ✓\checkmark |
| OPLoRA | ✓\checkmark | ✓\checkmark |

## B-3b794ac0ef6a58

https://arxiv.org/html/2510.13003v1#chars-29057-32097

### Mathematical Reasoning

For mathematical reasoning, we fine-tune each model on the first 100K examples from the MetaMathQA dataset ([Yu et al. 2023](#bib.bib35)). Evaluation is performed on two in-domain tasks: MATH ([Hendrycks et al. 2021](#bib.bib13)) and GSM8K ([Cobbe et al. 2021](#bib.bib9)), and we report Exact Match (EM) against the ground truth for each test set. As shown in Table [4](#Sx4.T4 "Table 4 ‣ Mathematical Reasoning ‣ Experiments ‣ OPLoRA: Orthogonal Projection LoRA Prevents Catastrophic Forgetting during Parameter-Efficient Fine-Tuning") and Table [5](#Sx4.T5 "Table 5 ‣ Mathematical Reasoning ‣ Experiments ‣ OPLoRA: Orthogonal Projection LoRA Prevents Catastrophic Forgetting during Parameter-Efficient Fine-Tuning"), OPLoRA achieves strong adaptation performance compared to baseline methods on both LLaMA-2 7B and Qwen2.5 7B.

On LLaMA-2 7B, OPLoRA-16 achieves the best performance on both MATH (7.04%) and GSM8K (49.73%), with OPLoRA-128 closely following with 6.88% and 49.35%. Both variants outperform all baseline methods. For Qwen2.5 7B, a similar pattern emerges. OPLoRA-16 achieves the highest score on both MATH (47.34%) and GSM8K (83.70%), while OPLoRA-128 is competitive with 46.72% and matches the top GSM8K score (83.70%).

To assess catastrophic forgetting, we evaluate each model on three held-out commonsense reasoning tasks: ARC-e, ARC-c, and SIQA. OPLoRA-128 obtains the best overall forgetting performance on LLaMA-2 7B, with OPLoRA-16 following closely behind. On Qwen2.5 7B, OPLoRA-128 again delivers the strongest forgetting resistance, achieving the best scores on ARC-e and SIQA, and performing competitively on ARC-c. OPLoRA-16 achieves the top score on ARC-c and ranks second on ARC-e and SIQA. Compared to all baselines, both OPLoRA variants show more balanced retention across all three tasks.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Fine-Tuning Eval | | Forgetting Eval | | |  |
| Method | MATH | GSM8K | ARC-e | ARC-c | SIQA | Avg |
| Baseline Methods | | | | | | |
| LoRA | 5.60 | 44.88 | 62.24 | 41.38 | 45.29 | 39.88 |
| PiSSA | 6.56 | 48.06 | 60.04 | 36.35 | 43.86 | 38.97 |
| MiLoRA | 5.84 | 45.26 | 67.12 | 41.21 | 44.92 | 40.87 |
| LoRA-Null | 6.06 | 48.31 | 66.28 | 41.30 | 45.21 | 41.43 |
| Our Methods | | | | | | |
| OPLoRA-16 | 7.04 | 49.73 | 66.88 | 41.47 | 45.19 | 42.06 |
| OPLoRA-128 | 6.88 | 49.35 | 67.26 | 42.24 | 45.50 | 42.25 |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Fine-Tuning Eval | | Forgetting Eval | | |  |
| Method | MATH | GSM8K | ARC-e | ARC-c | SIQA | Avg |
| Baseline Methods | | | | | | |
| LoRA | 45.96 | 82.18 | 81.40 | 50.42 | 51.28 | 62.25 |
| PiSSA | 32.74 | 74.45 | 72.47 | 38.65 | 44.37 | 52.54 |
| MiLoRA | 44.04 | 82.48 | 81.27 | 48.38 | 51.17 | 61.47 |
| LoRA-Null | 43.72 | 75.12 | 73.22 | 49.89 | 46.44 | 57.68 |
| Our Methods | | | | | | |
| OPLoRA-16 | 47.34 | 83.70 | 81.86 | 50.59 | 51.43 | 62.98 |
| OPLoRA-128 | 46.72 | 83.70 | 82.24 | 50.20 | 52.92 | 63.16 |

## B-4148d90b21091a

https://arxiv.org/html/2510.13003v1#chars-5618-5636

## Related Works

## B-4a9b3517ad6aba

https://arxiv.org/html/2510.13003v1#chars-32097-33995

### Python Code Generation

To evaluate code generation capabilities, we fine-tune each model on the CodeFeedback dataset ([Zheng et al. 2025](#bib.bib37)). Performance is assessed using two in-domain benchmarks, MBPP and MBPP++, where we report functional correctness as measured by pass@1 accuracy—the percentage of generated programs that pass all unit tests on the first attempt. The results are presented in Table [6](#Sx4.T6 "Table 6 ‣ Subspace Interference Analysis ‣ Experiments ‣ OPLoRA: Orthogonal Projection LoRA Prevents Catastrophic Forgetting during Parameter-Efficient Fine-Tuning") and Table [7](#Sx4.T7 "Table 7 ‣ Subspace Interference Analysis ‣ Experiments ‣ OPLoRA: Orthogonal Projection LoRA Prevents Catastrophic Forgetting during Parameter-Efficient Fine-Tuning") for LLaMA-2 7B and Qwen2.5 7B.

On LLaMA-2 7B, OPLoRA-16 achieves the highest performance on both MBPP (40.5%) and MBPP++ (34.1%), outperforming all baselines by a notable margin. OPLoRA-128 also performs strongly, achieving 39.2% on MBPP and 31.0% on MBPP++. The trends hold for Qwen2.5 7B as well. OPLoRA-16 obtains the top score on MBPP++ (69.0%) and matches LoRA on MBPP (80.2%), while OPLoRA-128 ranks second on MBPP (80.4%) and MBPP++ (68.8%). These findings confirm the flexibility of OPLoRA in handling both prompt-based and completion-style code generation benchmarks.

For forgetting, we evaluate the models on three held-out commonsense reasoning tasks: HellaSwag, OBQA, and SIQA. On LLaMA-2 7B, OPLoRA-128 achieves the highest accuracy on OBQA (45.6%) and HellaSwag (77.0%), while OPLoRA-16 obtains the best result on SIQA (47.1%) and the second-best on HellaSwag. For Qwen2.5 7B, OPLoRA-128 delivers the highest forgetting resistance overall, achieving the best scores on HellaSwag (79.2%), OBQA (47.4%), and SIQA (55.5%). OPLoRA-16 follows closely with strong performance across all three tasks.

## B-4f49235bb3c32d

https://arxiv.org/html/2510.13003v1#chars-21792-22691

#### Our Method.

Motivated by Proposition 2, we propose our one-line modification to LoRA that constrains the update Δ​W\Delta W to lie entirely in the orthogonal complement of the top-kk singular subspace of the pre-trained weight matrix W0W\_{0}. Specifically, we apply projections on both sides of the low-rank update and define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​W=PL​B​A​PR,\Delta W=P\_{L}BAP\_{R}, |  | (19) |

where PL=I−Uk​Uk⊤P\_{L}=I-U\_{k}U\_{k}^{\top} and PR=I−Vk​Vk⊤P\_{R}=I-V\_{k}V\_{k}^{\top} are orthogonal projectors that remove any component aligned with the top-kk left and right singular vectors of W0W\_{0}, respectively. This construction guarantees that the most informative singular directions of W0W\_{0} are exactly preserved under the update, thus mitigating forgetting while still allowing for expressive task-specific adaptation in the residual subspace.

## B-5268a117ec844d

https://arxiv.org/html/2510.13003v1#chars-33995-36963

### Subspace Interference Analysis

We analyze subspace interference to better understand the mechanism of catastrophic forgetting in LoRA-based fine-tuning. Specifically, we quantify how much the learned LoRA update Δ​W\Delta W aligns with the top-kk singular directions of the frozen pre-trained weights W0W\_{0}.

Figure [2](#Sx3.F2 "Figure 2 ‣ Our Method. ‣ Preserving Pre-trained Knowledge via Orthogonal Projection ‣ Methodology ‣ OPLoRA: Orthogonal Projection LoRA Prevents Catastrophic Forgetting during Parameter-Efficient Fine-Tuning")(a) presents ρk\rho\_{k} values for k∈{8,16,32,64,128}k\in\{8,16,32,64,128\} on the q\_proj layer across LoRA-based methods. We observe that PiSSA has significantly higher ρk\rho\_{k}, suggesting it heavily modifies pre-trained semantics and may cause knowledge overwriting. In contrast, OPLoRA-128 maintains consistently low alignment across all kk, indicating that its updates stay mostly in orthogonal subspaces and are less likely to interfere with prior knowledge. While OPLoRA is designed to project out the top-kk directions explicitly, the ρk\rho\_{k} values are not exactly zero due to the use of an efficient low-rank approximation via svd\_lowrank. Figure [2](#Sx3.F2 "Figure 2 ‣ Our Method. ‣ Preserving Pre-trained Knowledge via Orthogonal Projection ‣ Methodology ‣ OPLoRA: Orthogonal Projection LoRA Prevents Catastrophic Forgetting during Parameter-Efficient Fine-Tuning")(b) shows the average forgetting score across these benchmarks. A higher score indicates stronger retention of general knowledge. As shown, both OPLoRA variants outperform all baselines, achieving the best robustness to forgetting. In particular, OPLoRA-128 yields the highest average score, validating the hypothesis that subspace-aware updates are more effective at preserving pre-trained knowledge.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Fine-Tuning Eval | | Forgetting Eval | | |  |
| Method | MBPP | MBPP++ | HSwag | OBQA | SIQA | Avg |
| Baseline Methods | | | | | | |
| LoRA | 37.6 | 30.4 | 76.9 | 45.0 | 46.5 | 47.28 |
| PiSSA | 39.7 | 31.5 | 75.4 | 44.6 | 46.7 | 47.58 |
| MiLoRA | 37.3 | 30.4 | 77.0 | 44.6 | 47.0 | 47.26 |
| LoRA-Null | 37.0 | 29.4 | 76.7 | 44.8 | 46.7 | 46.92 |
| Our Methods | | | | | | |
| OPLoRA-16 | 40.5 | 34.1 | 76.9 | 44.8 | 47.1 | 48.68 |
| OPLoRA-128 | 39.2 | 31.0 | 77.0 | 45.6 | 47.0 | 47.96 |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Fine-Tuning Eval | | Forgetting Eval | | |  |
| Method | MBPP | MBPP++ | HSwag | OBQA | SIQA | Avg |
| Baseline Methods | | | | | | |
| LoRA | 80.2 | 68.3 | 79.1 | 47.4 | 54.4 | 65.88 |
| PiSSA | 68.3 | 58.2 | 78.0 | 43.2 | 51.7 | 59.88 |
| MiLoRA | 80.7 | 66.7 | 78.6 | 46.2 | 55.1 | 65.46 |
| LoRA-Null | 79.6 | 65.7 | 78.0 | 46.0 | 54.8 | 64.82 |
| Our Methods | | | | | | |
| OPLoRA-16 | 80.2 | 69.0 | 79.1 | 47.4 | 55.0 | 66.14 |
| OPLoRA-128 | 80.4 | 68.8 | 79.2 | 47.4 | 55.5 | 66.26 |

## B-57a629091b6077

https://arxiv.org/html/2510.13003v1#chars-0-209

##### Report GitHub Issue

Content selection saved. Describe the issue below:

![](/static/base/1.0.1/images/icons/smileybones-small.svg)
![arXiv logo](/static/base/1.0.1/images/arxiv-logo-primary-light.svg)

## B-5bd53bd2f6ae73

https://arxiv.org/html/2510.13003v1#chars-39043-40382

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

## B-5d5564f38296ae

https://arxiv.org/html/2510.13003v1#chars-1635-5618

## Introduction

The widespread adoption of large language models has created an urgent need for efficient adaptation techniques that can specialize pre-trained models for downstream tasks without incurring prohibitive computational costs ([Houlsby et al. 2019](#bib.bib14); [Lester, Al-Rfou, and Constant 2021](#bib.bib19); [Liu et al. 2022](#bib.bib23)). Low-Rank Adaptation (LoRA) ([Hu et al. 2022](#bib.bib15)) has emerged as a leading method for parameter-efficient fine-tuning, enabling task-specific customization by learning low-rank updates to frozen weight matrices while significantly reducing memory and compute requirements.

However, despite its computational advantages, LoRA suffers from a critical limitation: it provides no explicit mechanism to preserve the essential knowledge encoded in pre-trained weights, leading to catastrophic forgetting that degrades general capabilities after task-specific fine-tuning ([Biderman et al. 2024](#bib.bib4); [Yang et al. 2025b](#bib.bib34); [Dou et al. 2024](#bib.bib10)). This forgetting phenomenon presents a substantial challenge for real-world deployment, where models are expected to retain their foundational knowledge while acquiring new, task-specific capabilities. The core issue lies in LoRA’s unconstrained optimization process, which permits learned updates to inadvertently interfere with the principal representational subspaces of the pre-trained model.

Our key insight is that essential pre-trained knowledge is concentrated in the dominant singular directions—the subspaces corresponding to the largest singular values of weight matrices. By constraining LoRA updates to lie entirely within the orthogonal complement of these critical subspaces, we can provably prevent interference with pre-trained knowledge while maintaining expressive capacity for task-specific adaptation.

We present Orthogonal Projection LoRA (OPLoRA), which implements this constraint through a simple yet powerful modification: applying orthogonal projections to both sides of the low-rank update. Our method decomposes pre-trained weight matrices using Singular Value Decomposition and constructs projection matrices that remove any component aligned with the top-kk singular directions. This ensures that the learned adaptation Δ​W=PL​B​A​PR\Delta W=P\_{L}BAP\_{R} lies entirely in the orthogonal complement of the dominant subspace, where PLP\_{L} and PRP\_{R} are orthogonal projectors onto the complement of the top-kk left and right singular vectors.

We provide theoretical guarantees proving that this construction exactly preserves the top-kk singular triples of the original weight matrices, offering a principled and mathematically grounded solution to the forgetting problem. To quantify subspace interference, we introduce ρk\rho\_{k}, a novel metric that measures the proportion of update energy residing within the dominant subspace of pre-trained weights.

Extensive experiments across commonsense reasoning, mathematics, and code generation on LLaMA-2 7B ([Touvron et al. 2023](#bib.bib31)) and Qwen2.5 7B ([Yang et al. 2025a](#bib.bib33)) demonstrate that OPLoRA reduces catastrophic forgetting while maintaining competitive task-specific performance. Our approach consistently surpasses existing LoRA variants in retaining knowledge across diverse benchmarks.

We summarize our contributions as follows:

We present an analysis of catastrophic forgetting in LoRA by introducing ρk\rho\_{k}, a subspace alignment metric that quantitatively measures interference with pre-trained knowledge.

We propose Orthogonal Projection LoRA, a theoretically grounded method that provably preserves the dominant singular directions of pre-trained weights through double-sided orthogonal projections.

We validate our approach through extensive experiments across three domains and two model architectures, demonstrating significant improvements in forgetting resistance while maintaining competitive adaptation performance.

## B-8b81bbf1245420

https://arxiv.org/html/2510.13003v1#chars-36963-38133

## Conclusion

In this work, we introduce OPLoRA, a novel fine-tuning strategy that mitigates catastrophic forgetting by constraining LoRA updates to avoid interference with the dominant subspaces of pre-trained weights. Through a rigorous subspace alignment analysis, we demonstrate that previous LoRA-based methods often disrupt critical directions in the model’s weight space, leading to degraded generalization. OPLoRA addresses this issue by projecting updates orthogonally to the top singular vectors of the frozen weight matrices, thereby preserving essential pre-trained knowledge.

Extensive experiments show that OPLoRA consistently achieves competitive or superior performance compared to other LoRA variants while offering significantly improved forgetting resistance. Our results highlight the importance of subspace-aware adaptation in parameter-efficient fine-tuning, paving the way for more robust deployment of language models in continual and task-specific settings. Due to computational resource constraints, we leave the exploration of varying projection ranks and the extension of OPLoRA to larger-scale models such as LLaMA-3 70B for future work.

## B-97478b8b6afff4

https://arxiv.org/html/2510.13003v1#chars-10451-11591

### Preliminaries: Low-Rank Adaptation (LoRA)

Consider a pre-trained weight matrix W0∈ℝdout×dinW\_{0}\in\mathbb{R}^{d\_{\text{out}}\times d\_{\text{in}}}. LoRA proposes that task-specific adaptation can be achieved by learning a low-rank update Δ​W=αr​B​A\Delta W=\frac{\alpha}{r}BA instead of updating the full matrix. The forward pass becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h=W0​x+Δ​W​x=W0​x+αr​B​A​x,h=W\_{0}x+\Delta Wx=W\_{0}x+\frac{\alpha}{r}BAx, |  | (1) |

where B∈ℝdout×rB\in\mathbb{R}^{d\_{\text{out}}\times r} and A∈ℝr×dinA\in\mathbb{R}^{r\times d\_{\text{in}}} are trainable matrices, and r≪min⁡(dout,din)r\ll\min(d\_{\text{out}},d\_{\text{in}}) is the rank. The scaling factor α\alpha ensures the update is appropriately scaled.

During fine-tuning, W0W\_{0} remains frozen while gradients only flow through AA and BB. This strategy significantly reduces the number of trainable parameters and enables efficient adaptation, particularly for large models. LoRA normally preserves the pre-trained model’s behavior by initializing
AA with Kaiming-uniform ([He et al. 2015](#bib.bib12)) values and setting B=0B=0.

## B-9d0da5c3adacef

https://arxiv.org/html/2510.13003v1#chars-24224-29057

### Commonsense Reasoning

The commonsense reasoning benchmark consists of eight sub-tasks, BoolQ ([Clark et al. 2019](#bib.bib7)), PIQA ([Bisk et al. 2020](#bib.bib5)), SIQA ([Sap et al. 2019](#bib.bib29)), HellaSwag ([Zellers et al. 2019](#bib.bib36)), WinoGrande ([Sakaguchi et al. 2021](#bib.bib28)), ARC-e, ARC-c ([Clark et al. 2018](#bib.bib8)), and OBQA ([Mihaylov et al. 2018](#bib.bib25)). Models are fine-tuned on Commonsense170k ([Hu et al. 2023](#bib.bib16)) with evaluation performed on individual task test sets using accuracy as the primary metric. Results are presented in Tables [2](#Sx4.T2 "Table 2 ‣ Commonsense Reasoning ‣ Experiments ‣ OPLoRA: Orthogonal Projection LoRA Prevents Catastrophic Forgetting during Parameter-Efficient Fine-Tuning") and [3](#Sx4.T3 "Table 3 ‣ Commonsense Reasoning ‣ Experiments ‣ OPLoRA: Orthogonal Projection LoRA Prevents Catastrophic Forgetting during Parameter-Efficient Fine-Tuning").

OPLoRA demonstrates exceptional adaptation performance across both model architectures. On LLaMA-2 7B, OPLoRA-128 secures the highest accuracy on four tasks: BoolQ (82.78%), HellaSwag (75.38%), ARC-c (52.39%), and OBQA (45.8%). Meanwhile, OPLoRA-16 consistently achieves second-best performance on BoolQ, PIQA, HellaSwag, and ARC-c. This pattern extends to Qwen2.5 7B, where OPLoRA-16 leads on four tasks (HellaSwag, WinoGrande, ARC-e, OBQA) while OPLoRA-128 excels on PIQA and ARC-c. The consistent top-two ranking across diverse reasoning challenges demonstrates that our orthogonal projection approach preserves adaptation quality across different projection ranks.

To assess catastrophic forgetting, we evaluate retention of general knowledge on three held-out domains: MathQA (mathematical reasoning) ([Amini et al. 2019](#bib.bib2)), MBPP (code generation) ([Austin et al. 2021](#bib.bib3)), and RACE (reading comprehension) ([Lai et al. 2017](#bib.bib18)). These cross-domain evaluations provide critical insights into knowledge preservation during fine-tuning. As shown on the right side of Table [2](#Sx4.T2 "Table 2 ‣ Commonsense Reasoning ‣ Experiments ‣ OPLoRA: Orthogonal Projection LoRA Prevents Catastrophic Forgetting during Parameter-Efficient Fine-Tuning"), OPLoRA exhibits strong resistance to catastrophic forgetting on LLaMA-2 7B. Among all methods, OPLoRA-128 achieves the highest accuracy across all three held-out tasks, closely followed by OPLoRA-16. These results highlight the effectiveness of preserving the dominant subspace of pre-trained weights in maintaining general knowledge during fine-tuning. Similar improvements are observed with Qwen2.5 7B. OPLoRA-16 achieves the highest accuracy on MBPP and ranks second on both MathQA and RACE, while OPLoRA-128 obtains the best performance on MathQA and the second-best on MBPP.

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Fine-Tuning Evaluation | | | | | | | | Forgetting Evaluation | | |  |
| Method | BoolQ | PIQA | SIQA | HSwag | WinoG | ARC-e | ARC-c | OBQA | MathQA | MBPP | RACE | Avg |
| Baseline Methods | | | | | | | | | | | | |
| LoRA | 81.00 | 80.19 | 51.58 | 74.73 | 72.84 | 79.29 | 50.51 | 44.8 | 29.08 | 20.2 | 43.06 | 57.03 |
| PiSSA | 62.11 | 55.11 | 34.80 | 28.33 | 49.32 | 28.45 | 26.79 | 26.4 | 22.88 | 0 | 22.39 | 32.42 |
| MiLoRA | 82.04 | 78.99 | 54.24 | 75.04 | 73.40 | 79.08 | 52.21 | 45.4 | 28.21 | 18.6 | 41.4 | 57.15 |
| LoRA-Null | 82.02 | 77.97 | 51.43 | 74.74 | 72.88 | 77.48 | 48.29 | 42.6 | 28.98 | 9.8 | 42.20 | 55.31 |
| Our Methods | | | | | | | | | | | | |
| OPLoRA-16 | 82.42 | 79.16 | 52.92 | 75.35 | 72.30 | 79.55 | 52.30 | 45.2 | 29.08 | 20.2 | 43.06 | 57.41 |
| OPLoRA-128 | 82.78 | 79.11 | 53.53 | 75.38 | 73.24 | 79.25 | 52.39 | 45.8 | 29.88 | 20.4 | 43.63 | 57.76 |

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Fine-Tuning Evaluation | | | | | | | | Forgetting Evaluation | | |  |
| Method | BoolQ | PIQA | SIQA | HSwag | WinoG | ARC-e | ARC-c | OBQA | MathQA | MBPP | RACE | Avg |
| Baseline Methods | | | | | | | | | | | | |
| LoRA | 86.75 | 79.76 | 51.43 | 78.12 | 73.95 | 76.26 | 55.03 | 45.8 | 50.35 | 58.6 | 39.62 | 63.24 |
| PiSSA | 75.04 | 75.08 | 52.04 | 71.75 | 75.92 | 69.23 | 43.85 | 42.0 | 31.86 | 0.6 | 40.57 | 52.54 |
| MiLoRA | 86.05 | 77.36 | 53.42 | 74.73 | 76.47 | 71.42 | 52.13 | 44.4 | 46.47 | 2.6 | 39.62 | 56.79 |
| LoRA-Null | 83.30 | 77.61 | 51.57 | 75.67 | 74.51 | 75.84 | 54.83 | 46.8 | 50.24 | 19.8 | 40.11 | 59.12 |
| Our Methods | | | | | | | | | | | | |
| OPLoRA-16 | 86.64 | 79.38 | 52.56 | 79.01 | 76.64 | 78.54 | 55.46 | 47.8 | 50.92 | 59.6 | 40.28 | 64.26 |
| OPLoRA-128 | 86.64 | 79.76 | 51.43 | 77.62 | 74.03 | 76.14 | 56.14 | 47.4 | 51.29 | 59.2 | 39.23 | 63.53 |

## B-a0a73708468082

https://arxiv.org/html/2510.13003v1#chars-20467-21792

#### Proof.

By the definitions of PLP\_{L} and PRP\_{R}, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | PL​Uk=0,Uk⊤​PL=0,PR​Vk=0,Vk⊤​PR=0.P\_{L}U\_{k}=0,\quad U\_{k}^{\top}P\_{L}=0,\quad P\_{R}V\_{k}=0,\quad V\_{k}^{\top}P\_{R}=0. |  | (13) |

Applying the identities above:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​W​Vk=PL​B​A​(PR​Vk)=PL​B​A⋅0=0,\Delta WV\_{k}=P\_{L}BA(P\_{R}V\_{k})=P\_{L}BA\cdot 0=0, |  | (14) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​W⊤​Uk=PR​A⊤​B⊤​(PL​Uk)=PR​A⊤​B⊤⋅0=0,\Delta W^{\top}U\_{k}=P\_{R}A^{\top}B^{\top}(P\_{L}U\_{k})=P\_{R}A^{\top}B^{\top}\cdot 0=0, |  | (15) |

For each i≤ki\leq k, since Δ​W​vi=0\Delta Wv\_{i}=0, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | W′​vi=(W0+Δ​W)​vi=W0​vi=σi​ui.W^{\prime}v\_{i}=(W\_{0}+\Delta W)v\_{i}=W\_{0}v\_{i}=\sigma\_{i}u\_{i}. |  | (16) |

Similarly, since Δ​W⊤​ui=0\Delta W^{\top}u\_{i}=0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (W′)⊤​ui=W0⊤​ui=σi​vi.(W^{\prime})^{\top}u\_{i}=W\_{0}^{\top}u\_{i}=\sigma\_{i}v\_{i}. |  | (17) |

Thus, (ui,σi,vi)(u\_{i},\sigma\_{i},v\_{i}) remains an exact singular triple of W′W^{\prime}.

Equivalently we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uk⊤​W′​Vk=Uk⊤​W0​Vk=Σk.U\_{k}^{\top}W^{\prime}V\_{k}=U\_{k}^{\top}W\_{0}V\_{k}=\Sigma\_{k}. |  | (18) |

■\blacksquare

## B-a464355cdae0f1

https://arxiv.org/html/2510.13003v1#chars-10435-10451

## Methodology

## B-ac96611171cd8c

https://arxiv.org/html/2510.13003v1#chars-11591-14775

### Understanding and Quantifying Forgetting in LoRA

While LoRA effectively reduces parameter count, it does not explicitly account for the distribution of information in W0W\_{0}. In practice, fine-tuning with LoRA can lead to catastrophic forgetting, where essential knowledge encoded in the pre-trained model is overwritten during adaptation fine-tuning.

The forgetting phenomenon is often implicit and hard to quantify. To better understand it, we analyze the learned adaptation Δ​W\Delta W relative to the singular directions of W0W\_{0}. Specifically, we ask: Does the LoRA update interfere with the most important components of the W0W\_{0}?

To answer this, we leverage the Singular Value Decomposition, which decomposes the weight matrix W0W\_{0} into:

|  |  |  |  |
| --- | --- | --- | --- |
|  | W0=U​Σ​V⊤,W\_{0}=U\Sigma V^{\top}, |  | (2) |

where UU and VV are orthogonal matrices, and Σ\Sigma is a diagonal matrix of singular values sorted in descending order. The leading kk left singular vectors, Uk∈ℝdout×kU\_{k}\in\mathbb{R}^{d\_{\text{out}}\times k}, define the principal column subspace of W0W\_{0}, embodying the directions with maximal spectral energy or task-critical information.

Empirical observations ([Li et al. 2018](#bib.bib20); [Aghajanyan, Zettlemoyer, and Gupta 2020](#bib.bib1); [Hu et al. 2022](#bib.bib15)) show that singular values of W0W\_{0} decay rapidly, meaning the essential semantics of the layer are concentrated in a low-dimensional subspace. However, since the LoRA weight is unconstrained during training, the resulting update Δ​W\Delta W may interfere with these top directions—modifying them and causing loss of important pre-trained knowledge.

To make this interference measurable, we define a subspace alignment metric ρk\rho\_{k}, which quantifies how much of Δ​W\Delta W lies within the top-kk singular directions of W0W\_{0}.

Let Qk=Uk​Uk⊤Q\_{k}=U\_{k}U\_{k}^{\top} denote the orthogonal projector onto the column space of WW. Then, we can decompose the LoRA update Δ​W\Delta W as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​W=Qk​Δ​W+(I−Qk)​Δ​W,\Delta W=Q\_{k}\Delta W+(I-Q\_{k})\Delta W, |  | (3) |

where the first term lies within the column space of WW, and the second term lies in its orthogonal complement. Using the Pythagorean property of orthogonal projections, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Δ​W‖F2=‖Qk​Δ​W‖F2+‖(I−Qk)​Δ​W‖F2.||\Delta W||\_{F}^{2}=||Q\_{k}\Delta W||\_{F}^{2}+||(I-Q\_{k})\Delta W||\_{F}^{2}. |  | (4) |

Then we define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρk=‖Qk​Δ​W‖F2‖Δ​W‖F2∈[0,1],\rho\_{k}=\frac{||Q\_{k}\Delta W||\_{F}^{2}}{||\Delta W||\_{F}^{2}}\in[0,1], |  | (5) |

which measures the proportion of the updated spectral energy that lies within the original top-k column space of WW.

A value of ρk→1\rho\_{k}\rightarrow 1 implies that the LoRA update stays mostly in the original subspace and may risk interfering with pre-trained features. Conversely, ρk→0\rho\_{k}\rightarrow 0 indicates that the update explores directions orthogonal to the pre-trained space—potentially enabling new task-specific representations while preserving prior knowledge.

## B-b63ccf4145c858

https://arxiv.org/html/2510.13003v1#chars-5636-7668

### Low-Rank Adaptation and Extensions

LoRA ([Hu et al. 2022](#bib.bib15)) is a foundational method for parameter-efficient fine-tuning (PEFT) that introduces trainable low-rank matrices into each weight layer while keeping the pre-trained weights frozen. The core idea is that task-specific knowledge can be captured through a low-dimensional subspace, reducing both memory and computational requirements. Recent work has extended this framework through sophisticated weight decomposition strategies, notably DoRA ([Liu et al. 2024](#bib.bib22)), which addresses the limited expressiveness of vanilla LoRA by decomposing pre-trained weight matrices into magnitude and direction components and applying low-rank adaptation exclusively to the direction component. A parallel line of research has focused on exploiting the inherent structure of pre-trained weights through singular value decomposition, with PiSSA ([Meng, Wang, and Zhang 2024](#bib.bib24)) replacing LoRA’s random initialization with principled construction using the principal singular vectors and values of frozen weight matrices, enabling direct modification of the essential subspace and improved alignment between low-rank updates and full fine-tuning behavior. In contrast, MiLoRA ([Wang et al. 2024](#bib.bib32)) adopts a complementary approach by explicitly preserving the dominant subspace of pre-trained weights, performing SVD on each weight matrix and freezing the principal components during fine-tuning while updating only the minor singular components via low-rank adaptation, thereby constraining initialization to a subspace orthogonal to core pre-trained knowledge and minimizing interference with essential representations. Additionally, OLoRA ([Büyükakyüz 2024](#bib.bib6)) focuses on improving optimization landscapes by initializing adaptation matrices with orthonormal bases derived through QR decomposition, constraining updates to well-conditioned subspaces to promote improved gradient flow and convergence stability across diverse tasks.

## B-b7cb3075d34729

https://arxiv.org/html/2510.13003v1#chars-319-1635

###### Abstract

Low-Rank Adaptation (LoRA) enables efficient fine-tuning of large language models but suffers from catastrophic forgetting when learned updates interfere with the dominant singular directions that encode essential pre-trained knowledge. We propose Orthogonal Projection LoRA (OPLoRA), a theoretically grounded approach that prevents this interference through double-sided orthogonal projections. By decomposing frozen weights via SVD, OPLoRA constrains LoRA updates to lie entirely within the orthogonal complement of the top-kk singular subspace using projections PL=I−Uk​Uk⊤P\_{L}=I-U\_{k}U\_{k}^{\top} and PR=I−Vk​Vk⊤P\_{R}=I-V\_{k}V\_{k}^{\top}. We prove that this construction exactly preserves the top-kk singular triples, providing mathematical guarantees for knowledge retention. To quantify subspace interference, we introduce ρk\rho\_{k}, a metric measuring update alignment with dominant directions. Extensive experiments across commonsense reasoning, mathematics, and code generation demonstrate that OPLoRA significantly reduces forgetting while maintaining competitive task-specific performance on LLaMA-2 7B and Qwen2.5 7B, establishing orthogonal projection as an effective mechanism for knowledge preservation in parameter-efficient fine-tuning.

1University of California, Irvine

## B-d557fc769b0b4a

https://arxiv.org/html/2510.13003v1#chars-209-319

# OPLoRA: Orthogonal Projection LoRA Prevents Catastrophic Forgetting during Parameter-Efficient Fine-Tuning

## B-df1edd529ad89e

https://arxiv.org/html/2510.13003v1#chars-15492-16158

#### Proposition 1.

Let Uk∈ℝdout×kU\_{k}\in\mathbb{R}^{d\_{\text{out}}\times k} be an orthonormal basis for the top-kk left singular vectors of W0∈ℝdout×dinW\_{0}\in\mathbb{R}^{d\_{\text{out}}\times d\_{\text{in}}}. Define the orthogonal projector onto the complement of span​{Uk}\text{span}\{U\_{k}\} as P=I−Uk​Uk⊤P=I-U\_{k}U\_{k}^{\top}. For every LoRA update Δ​W=P​B​A\Delta W=PBA and any input vector xx, the output Δ​W​x=P​B​A​x\Delta Wx=PBAx resides completely in the orthogonal complement of span​{Uk}\text{span}\{U\_{k}\}, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uk⊤​(P​B​A​x)=0for all ​x.U\_{k}^{\top}(PBAx)=0\quad\text{for all }x. |  | (7) |

## B-e0704d69c08656

https://arxiv.org/html/2510.13003v1#chars-18920-20467

#### Proposition 2.

Let W0∈ℝdout×dinW\_{0}\in\mathbb{R}^{d\_{\text{out}}\times d\_{\text{in}}} admit the singular value decomposition

|  |  |  |  |
| --- | --- | --- | --- |
|  | W0=U​Σ​V⊤=Uk​Σk​Vk⊤+U⟂​Σ⟂​V⟂⊤,W\_{0}=U\Sigma V^{\top}=U\_{k}\Sigma\_{k}V\_{k}^{\top}+U\_{\perp}\Sigma\_{\perp}V\_{\perp}^{\top}, |  | (9) |

where Uk=[u1,…,uk]U\_{k}=[u\_{1},\dots,u\_{k}], Vk=[v1,…,vk]V\_{k}=[v\_{1},\dots,v\_{k}] collect the top-kk left and right singular vectors, Σk=diag⁡(σ1,…,σk)\Sigma\_{k}=\operatorname{diag}(\sigma\_{1},\dots,\sigma\_{k}) with σ1≥⋯≥σk>0\sigma\_{1}\geq\dots\geq\sigma\_{k}>0, and U⟂U\_{\perp},Σ⟂\Sigma\_{\perp}, and V⟂V\_{\perp} contain remaining singular triples.
Define the orthogonal projectors on the complements of the dominant subspaces:

|  |  |  |  |
| --- | --- | --- | --- |
|  | PL=I−Uk​Uk⊤,PR=I−Vk​Vk⊤.P\_{L}=I-U\_{k}U\_{k}^{\top},\quad P\_{R}=I-V\_{k}V\_{k}^{\top}. |  | (10) |

Construct the LoRA update as Δ​W=PL​B​A​PR\Delta W=P\_{L}BAP\_{R} for arbitrary matrices AA and BB, and set updated weight matrix W′=W0+Δ​WW^{\prime}=W\_{0}+\Delta W. Then, for every i=1,…,ki=1,\dots,k,

|  |  |  |  |
| --- | --- | --- | --- |
|  | W′​vi=σi​ui,(W′)⊤​ui=σi​vi,W^{\prime}v\_{i}=\sigma\_{i}u\_{i},\quad(W^{\prime})^{\top}u\_{i}=\sigma\_{i}v\_{i}, |  | (11) |

or equivalently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uk⊤​W′​Vk=Σk.U\_{k}^{\top}W^{\prime}V\_{k}=\Sigma\_{k}. |  | (12) |

Thus the top-kk singular vectors and their corresponding singular values of W0W\_{0} remain exactly preserved after the update.

## B-fcdeb4fcdd9c2d

https://arxiv.org/html/2510.13003v1#chars-7668-10435

### Catastrophic Forgetting and Knowledge Preservation

Catastrophic forgetting represents a fundamental challenge in continual learning and fine-tuning, where models lose previously acquired knowledge when learning new tasks ([Ramasesh, Dyer, and Raghu 2020](#bib.bib26)). In the context of large language models, this phenomenon manifests as degraded performance on general capabilities after task-specific fine-tuning, posing significant practical limitations for real-world deployment. The measurement and mitigation of catastrophic forgetting have become critical research directions, with various approaches emerging to quantify and address this problem.
Early mitigation strategies focused on regularization and replay mechanisms. Elastic Weight Consolidation (EWC) ([Kirkpatrick et al. 2017](#bib.bib17)) constrains training updates with a Fisher information-weighted quadratic penalty to identify and protect crucial weights from previous tasks. Learning Without Forgetting (LwF) ([Li and Hoiem 2017](#bib.bib21)) addresses forgetting without retaining old data by recording the original network’s soft outputs on new-task data, then training the model to match those pseudo-labels while learning new labels. Meta-Experience Replay (MER) ([Riemer et al. 2018](#bib.bib27)) combines each incoming example with a small reservoir of past samples and applies lightweight Reptile meta-updates that encourage gradient alignment across old and new data, maximizing transfer while reducing interference. Orthogonal Gradient Descent (OGD) ([Farajtabar et al. 2020](#bib.bib11)) tackles catastrophic forgetting by constraining every new gradient step to be orthogonal to the gradient directions that mattered for earlier tasks. Instead of storing old data, it stores a compact set of per‑task prediction‑gradient vectors; before each parameter update, the current task’s gradient is projected into the null‑space of those stored directions.
Recent research has increasingly explored parameter-efficient fine-tuning techniques as a natural solution to knowledge preservation. Within the LoRA framework, MiLoRA attempts to preserve dominant pre-trained weights by initializing LoRA matrices with minor singular components, constraining adaptation to less critical subspaces. However, MiLoRA does not explicitly address the problem of catastrophic forgetting. The most recent work, LoRA-Null ([Tang et al. 2025](#bib.bib30)), mitigates catastrophic forgetting by leveraging the null space for adapter initialization and constructing LoRA adapters from projections of pre-trained weights onto the null space of representative activations to ensure that update directions do not interfere with pre-trained knowledge.

![Refer to caption](2510.13003v1/initialization2.png)

## B-ocr-0c44626a0457ea

B PDF page 7

[tbl-3.html](tbl-3.html)

Table 4: Comparison of LoRA-based methods fine-tuned on MetaMathQA (first 100K samples) using LLaMA-2 7B. MATH and GSM8K are used to evaluate fine-tuning performance on in-domain tasks, while ARC-e, ARC-c, and SIQA assess the degree of forgetting on held-out reasoning benchmarks. Best and second-best scores are highlighted in bold and underlined.

[tbl-4.html](tbl-4.html)

Table 5: Comparison of LoRA-based methods fine-tuned on MetaMathQA (first 100K samples) using Qwen2.5 7B. Best and second-best scores are highlighted in bold and underlined.

tuning. Specifically, we quantify how much the learned LoRA update \(\Delta W\) aligns with the top-\(k\) singular directions of the frozen pre-trained weights \(W_0\).

Figure 2(a) presents \(\rho_{k}\) values for \(k\in \{8,16,32,64,128\}\) on the q_proj layer across LoRA-based methods. We observe that PiSSA has significantly higher \(\rho_{k}\), suggesting it heavily modifies pre-trained semantics and may cause knowledge overwriting. In contrast, OPLoRA-128 maintains consistently low alignment across all \(k\), indicating that its updates stay mostly in orthogonal subspaces and are less likely to interfere with prior knowledge. While OPLoRA is designed to project out the top-\(k\) directions explicitly, the \(\rho_{k}\) values are not exactly zero due to the use of an efficient low-rank approximation via svd_lowrank. Figure 2(b) shows the average forgetting score across these benchmarks. A higher score indicates stronger retention of general knowledge. As shown, both OPLoRA variants outperform all baselines, achieving the best robustness to forgetting. In particular, OPLoRA-128 yields the highest average score, validating the hypothesis that subspace-aware updates are more effective at preserving pre-trained knowledge.

[tbl-5.html](tbl-5.html)

Table 6: Performance comparison of LoRA-based methods fine-tuned on CodeFeedback dataset using LLaMA-2 7B. MBPP and MBPP++ evaluate in-domain code generation performance, while HSwag, OBQA, and SIQA are used to assess forgetting and generalization to out-of-domain commonsense reasoning tasks. Best and second-best results are highlighted in bold and underlined.

[tbl-6.html](tbl-6.html)

Table 7: Performance comparison of LoRA-based methods fine-tuned on CodeFeedback dataset using Qwen2.5 7B. Best and second-best results are highlighted in bold and underlined.

## Conclusion

In this work, we introduce OPLoRA, a novel fine-tuning strategy that mitigates catastrophic forgetting by constraining LoRA updates to avoid interference with the dominant subspaces of pre-trained weights. Through a rigorous subspace alignment analysis, we demonstrate that previous LoRA-based methods often disrupt critical directions in the model's weight space, leading to degraded generalization. OPLoRA addresses this issue by projecting updates orthogonally to the top singular vectors of the frozen weight matrices, thereby preserving essential pre-trained knowledge.

Extensive experiments show that OPLoRA consistently achieves competitive or superior performance compared to other LoRA variants while offering significantly improved forgetting resistance. Our results highlight the importance of subspace-aware adaptation in parameter-efficient fine-tuning, paving the way for more robust deployment of language models in continual and task-specific settings. Due to computational resource constraints, we leave the exploration of varying projection ranks and the extension of OPLoRA to larger-scale models such as LLaMA-3 70B for future work.

[OCR table id=tbl-3.html; page=7]
<table><tr><td rowspan="2">Method</td><td colspan="2">Fine-Tuning Eval</td><td colspan="3">Forgetting Eval</td><td rowspan="2">Avg</td></tr><tr><td>MATH</td><td>GSM8K</td><td>ARC-e</td><td>ARC-c</td><td>SIQA</td></tr><tr><td colspan="7">Baseline Methods</td></tr><tr><td>LoRA</td><td>5.60</td><td>44.88</td><td>62.24</td><td>41.38</td><td>45.29</td><td>39.88</td></tr><tr><td>PiSSA</td><td>6.56</td><td>48.06</td><td>60.04</td><td>36.35</td><td>43.86</td><td>38.97</td></tr><tr><td>MiLoRA</td><td>5.84</td><td>45.26</td><td>67.12</td><td>41.21</td><td>44.92</td><td>40.87</td></tr><tr><td>LoRA-Null</td><td>6.06</td><td>48.31</td><td>66.28</td><td>41.30</td><td>45.21</td><td>41.43</td></tr><tr><td colspan="7">Our Methods</td></tr><tr><td>OPLoRA-16</td><td>7.04</td><td>49.73</td><td>66.88</td><td>41.47</td><td>45.19</td><td>42.06</td></tr><tr><td>OPLoRA-128</td><td>6.88</td><td>49.35</td><td>67.26</td><td>42.24</td><td>45.50</td><td>42.25</td></tr></table>

[OCR table id=tbl-4.html; page=7]
<table><tr><td rowspan="2">Method</td><td colspan="2">Fine-Tuning Eval</td><td colspan="3">Forgetting Eval</td><td rowspan="2">Avg</td></tr><tr><td>MATH</td><td>GSM8K</td><td>ARC-e</td><td>ARC-c</td><td>SIQA</td></tr><tr><td colspan="7">Baseline Methods</td></tr><tr><td>LoRA</td><td>45.96</td><td>82.18</td><td>81.40</td><td>50.42</td><td>51.28</td><td>62.25</td></tr><tr><td>PiSSA</td><td>32.74</td><td>74.45</td><td>72.47</td><td>38.65</td><td>44.37</td><td>52.54</td></tr><tr><td>MiLoRA</td><td>44.04</td><td>82.48</td><td>81.27</td><td>48.38</td><td>51.17</td><td>61.47</td></tr><tr><td>LoRA-Null</td><td>43.72</td><td>75.12</td><td>73.22</td><td>49.89</td><td>46.44</td><td>57.68</td></tr><tr><td colspan="7">Our Methods</td></tr><tr><td>OPLoRA-16</td><td>47.34</td><td>83.70</td><td>81.86</td><td>50.59</td><td>51.43</td><td>62.98</td></tr><tr><td>OPLoRA-128</td><td>46.72</td><td>83.70</td><td>82.24</td><td>50.20</td><td>52.92</td><td>63.16</td></tr></table>

[OCR table id=tbl-5.html; page=7]
<table><tr><td rowspan="2">Method</td><td colspan="2">Fine-Tuning Eval</td><td colspan="3">Forgetting Eval</td><td rowspan="2">Avg</td></tr><tr><td>MBPP</td><td>MBPP++</td><td>HSwag</td><td>OBQA</td><td>SIQA</td></tr><tr><td colspan="7">Baseline Methods</td></tr><tr><td>LoRA</td><td>37.6</td><td>30.4</td><td>76.9</td><td>45.0</td><td>46.5</td><td>47.28</td></tr><tr><td>PiSSA</td><td>39.7</td><td>31.5</td><td>75.4</td><td>44.6</td><td>46.7</td><td>47.58</td></tr><tr><td>MiLoRA</td><td>37.3</td><td>30.4</td><td>77.0</td><td>44.6</td><td>47.0</td><td>47.26</td></tr><tr><td>LoRA-Null</td><td>37.0</td><td>29.4</td><td>76.7</td><td>44.8</td><td>46.7</td><td>46.92</td></tr><tr><td colspan="7">Our Methods</td></tr><tr><td>OPLoRA-16</td><td>40.5</td><td>34.1</td><td>76.9</td><td>44.8</td><td>47.1</td><td>48.68</td></tr><tr><td>OPLoRA-128</td><td>39.2</td><td>31.0</td><td>77.0</td><td>45.6</td><td>47.0</td><td>47.96</td></tr></table>

[OCR table id=tbl-6.html; page=7]
<table><tr><td rowspan="2">Method</td><td colspan="2">Fine-Tuning Eval</td><td colspan="3">Forgetting Eval</td><td rowspan="2">Avg</td></tr><tr><td>MBPP</td><td>MBPP++</td><td>HSwag</td><td>OBQA</td><td>SIQA</td></tr><tr><td colspan="7">Baseline Methods</td></tr><tr><td>LoRA</td><td>80.2</td><td>68.3</td><td>79.1</td><td>47.4</td><td>54.4</td><td>65.88</td></tr><tr><td>PiSSA</td><td>68.3</td><td>58.2</td><td>78.0</td><td>43.2</td><td>51.7</td><td>59.88</td></tr><tr><td>MiLoRA</td><td>80.7</td><td>66.7</td><td>78.6</td><td>46.2</td><td>55.1</td><td>65.46</td></tr><tr><td>LoRA-Null</td><td>79.6</td><td>65.7</td><td>78.0</td><td>46.0</td><td>54.8</td><td>64.82</td></tr><tr><td colspan="7">Our Methods</td></tr><tr><td>OPLoRA-16</td><td>80.2</td><td>69.0</td><td>79.1</td><td>47.4</td><td>55.0</td><td>66.14</td></tr><tr><td>OPLoRA-128</td><td>80.4</td><td>68.8</td><td>79.2</td><td>47.4</td><td>55.5</td><td>66.26</td></tr></table>

## B-ocr-64446e56f5da61

B PDF page 4

Proof. We first verify that $P$ is a projection matrix: $P^2 = (I - U_k U_k^\top)^2 = I - 2U_k U_k^\top + U_k U_k^\top U_k U_k^\top = I - U_k U_k^\top = P$, since $U_k^\top U_k = I$.

Now for any input $x \in \mathbb{R}^{d_{\mathrm{in}}}$, the LoRA output is $\Delta Wx = PBAx$. We show that this vector is orthogonal to $\operatorname{span}(U_k)$ by checking:

$$\begin{array}{l} U_k^\top (PBAx) = U_k^\top (I - U_k U_k^\top) BAx \\ = (U_k^\top - U_k^\top U_k U_k^\top) BAx \\ = (U_k^\top - U_k^\top) BAx \\ = 0. \end{array}$$

Hence, $\Delta Wx \in \operatorname{span}(U_k)^\perp$, and the LoRA update does not interfere with the dominant subspace of the original weight matrix.

While Proposition 1 guarantees that the LoRA update $\Delta W = PBA$ does not inject any output into the top-$k$ left singular directions of $W_0$, it is natural to ask whether any stronger preservation property holds. In particular, does the use of the projection $P = I - U_k U_k^\top$ preserve the original singular vectors $u_i$ or the singular values $\sigma_i$?

The answer is no. Even though $\Delta Wx$ is orthogonal to $\operatorname{span}(U_k)$ for every $x$, this alone does not guarantee that adding $\Delta W$ preserves the top-$k$ singular vectors or singular values of the updated weight matrix $W' = W_0 + \Delta W$. To see this, assume for contradiction that $W'u_i = \sigma_i v_i$ for some $i \le k$. Then we would imply

$$\Delta W u_i = W' u_i - W_0 u_i = \sigma_i v_i - \sigma_i v_i = 0. \tag{8}$$

However, this conclusion does not follow from Proposition 1, because $\Delta W u_i$ need not be zero—it only lies in $\operatorname{span}(U_k)^\perp$. Hence, the top-$k$ left singular vectors of $W_0$ are generally not preserved.

This leads to a stronger goal: can we preserve each complete singular triple $(u_i, \sigma_i, v_i)$? We can — by projecting on both sides. Constraining $\Delta W$ to the orthogonal complements of the top-$k$ left and right singular subspaces guarantees that the top-$k$ singular vectors and singular values of $W_0$ remain intact. We now state and prove this claim formally.

Proposition 2. Let $W_0 \in \mathbb{R}^{d_{\mathrm{out}} \times d_{\mathrm{in}}}$ admit the singular value decomposition

$$W_0 = U \Sigma V^\top = U_k \Sigma_k V_k^\top + U_\perp \Sigma_\perp V_\perp^\top, \tag{9}$$

where $U_k = [u_1, \dots, u_k]$, $V_k = [v_1, \dots, v_k]$ collect the top-$k$ left and right singular vectors, $\Sigma_k = \operatorname{diag}(\sigma_1, \dots, \sigma_k)$ with $\sigma_1 \ge \dots \ge \sigma_k > 0$, and $U_\perp, \Sigma_\perp$, and $V_\perp$ contain remaining singular triples. Define the orthogonal projectors on the complements of the dominant subspaces:

$$P_L = I - U_k U_k^\top, \quad P_R = I - V_k V_k^\top. \tag{10}$$

Construct the LoRA update as $\Delta W = P_L B A P_R$ for arbitrary matrices $A$ and $B$, and set updated weight matrix $W' = W_0 + \Delta W$. Then, for every $i = 1, \dots, k$,

$$W' v_i = \sigma_i u_i, \quad (W')^\top u_i = \sigma_i v_i, \tag{11}$$

or equivalently,

$$U_k^\top W' V_k = \Sigma_k. \tag{12}$$

Thus the top-$k$ singular vectors and their corresponding singular values of $W_0$ remain exactly preserved after the update.

Proof. By the definitions of $P_L$ and $P_R$, we have:

$$P_L U_k = 0, \quad U_k^\top P_L = 0, \quad P_R V_k = 0, \quad V_k^\top P_R = 0. \tag{13}$$

Applying the identities above:

$$\Delta W V_k = P_L B A (P_R V_k) = P_L B A \cdot 0 = 0, \tag{14}$$

$$\Delta W^\top U_k = P_R A^\top B^\top (P_L U_k) = P_R A^\top B^\top \cdot 0 = 0, \tag{15}$$

For each $i \le k$, since $\Delta W v_i = 0$, we have:

$$W' v_i = (W_0 + \Delta W) v_i = W_0 v_i = \sigma_i u_i. \tag{16}$$

Similarly, since $\Delta W^\top u_i = 0$:

$$(W')^\top u_i = W_0^\top u_i = \sigma_i v_i. \tag{17}$$

Thus, $(u_i, \sigma_i, v_i)$ remains an exact singular triple of $W'$.

Equivalently we have:

$$U_k^\top W' V_k = U_k^\top W_0 V_k = \Sigma_k. \tag{18}$$

Our Method. Motivated by Proposition 2, we propose our one-line modification to LoRA that constrains the update $\Delta W$ to lie entirely in the orthogonal complement of the top-$k$ singular subspace of the pre-trained weight matrix $W_0$. Specifically, we apply projections on both sides of the low-rank update and define:

$$\Delta W = P_L B A P_R, \tag{19}$$

where $P_L = I - U_k U_k^\top$ and $P_R = I - V_k V_k^\top$ are orthogonal projectors that remove any component aligned with the top-$k$ left and right singular vectors of $W_0$, respectively. This construction guarantees that the most informative singular directions of $W_0$ are exactly preserved under the update, thus mitigating forgetting while still allowing for expressive task-specific adaptation in the residual subspace.

## Experiments

We conduct comprehensive experiments to evaluate the effectiveness of OPLoRA in preventing catastrophic forgetting while maintaining competitive fine-tuning performance. Our comparisons include four LoRA-based baselines: LoRA (Hu et al. 2022), PiSSA (Meng, Wang, and Zhang 2024), MiLoRA (Wang et al. 2024), and LoRA-Null (Tang et al. 2025). Each method is evaluated across three task domains, commonsense reasoning, mathematics, and Python code generation, using two backbone models: LLaMA-2 7B (Touvron et al. 2023) and Qwen2.5 7B (Yang et al. 2025a). All methods are trained under the same hyperparameter configuration for fair comparison, with LoRA applied to the self-attention and MLP layers, specifically targeting the modules q_proj, v_proj, up_proj, down_proj, o_proj. For OPLoRA, we fix the projection rank $k$ to two values, $k = 16$ and $k = 128$, across all experiments. These ranks are not tuned for performance and are chosen to represent low and high subspace preservation regimes. Exploration of optimal projection rank selection is left for future work.

## B-ocr-6756d70bc27bc5

B PDF page 9

He, K.; Zhang, X.; Ren, S.; and Sun, J. 2015. Delving deep into rectifiers: Surpassing human-level performance on imagenet classification. In Proceedings of the IEEE international conference on computer vision, 1026–1034.

Hendrycks, D.; Burns, C.; Kadavath, S.; Arora, A.; Basart, S.; Tang, E.; Song, D.; and Steinhardt, J. 2021. Measuring mathematical problem solving with the math dataset. arXiv preprint arXiv:2103.03874.

Houlsby, N.; Giurgiu, A.; Jastrzebski, S.; Morrone, B.; De Laroussilhe, Q.; Gesmundo, A.; Attariyan, M.; and Gelly, S. 2019. Parameter-Efficient Transfer Learning for NLP. In Chaudhuri, K.; and Salakhutdinov, R., eds., Proceedings of the 36th International Conference on Machine Learning, volume 97 of Proceedings of Machine Learning Research, 2790–2799. PMLR.

Hu, E. J.; Shen, Y.; Wallis, P.; Allen-Zhu, Z.; Li, Y.; Wang, S.; Wang, L.; Chen, W.; et al. 2022. Lora: Low-rank adaptation of large language models. ICLR, 1(2): 3.

Hu, Z.; Wang, L.; Lan, Y.; Xu, W.; Lim, E.-P.; Bing, L.; Xu, X.; Poria, S.; and Lee, R. K.-W. 2023. Llm-adapters: An adapter family for parameter-efficient fine-tuning of large language models. arXiv preprint arXiv:2304.01933.

Kirkpatrick, J.; Pascanu, R.; Rabinowitz, N.; Veness, J.; Desjardins, G.; Rusu, A. A.; Milan, K.; Quan, J.; Ramalho, T.; Grabska-Barwinska, A.; et al. 2017. Overcoming catastrophic forgetting in neural networks. Proceedings of the national academy of sciences, 114(13): 3521–3526.

Lai, G.; Xie, Q.; Liu, H.; Yang, Y.; and Hovy, E. 2017. RACE: Large-scale ReAding Comprehension Dataset From Examinations. In Palmer, M.; Hwa, R.; and Riedel, S., eds., Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing, 785–794. Copenhagen, Denmark: Association for Computational Linguistics.

Lester, B.; Al-Rfou, R.; and Constant, N. 2021. The Power of Scale for Parameter-Efficient Prompt Tuning. In Moens, M.-F.; Huang, X.; Specia, L.; and Yih, S. W.-t., eds., Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, 3045–3059. Online and Punta Cana, Dominican Republic: Association for Computational Linguistics.

Li, C.; Farkhoor, H.; Liu, R.; and Yosinski, J. 2018. Measuring the Intrinsic Dimension of Objective Landscapes. arXiv:1804.08838.

Li, Z.; and Hoiem, D. 2017. Learning without forgetting. IEEE transactions on pattern analysis and machine intelligence, 40(12): 2935–2947.

Liu, S.-Y.; Wang, C.-Y.; Yin, H.; Molchanov, P.; Wang, Y.-C. F.; Cheng, K.-T.; and Chen, M.-H. 2024. Dora: Weight-decomposed low-rank adaptation. In Forty-first International Conference on Machine Learning.

Liu, X.; Ji, K.; Fu, Y.; Tam, W. L.; Du, Z.; Yang, Z.; and Tang, J. 2022. P-Tuning v2: Prompt Tuning Can Be Comparable to Fine-tuning Universally Across Scales and Tasks. arXiv:2110.07602.

Meng, F.; Wang, Z.; and Zhang, M. 2024. Pissa: Principal singular values and singular vectors adaptation of large lan-

guage models. Advances in Neural Information Processing Systems, 37: 121038–121072.

Mihaylov, T.; Clark, P.; Khot, T.; and Sabharwal, A. 2018. Can a suit of armor conduct electricity? a new dataset for open book question answering. arXiv preprint arXiv:1809.02789.

Ramasesh, V. V.; Dyer, E.; and Raghu, M. 2020. Anatomy of catastrophic forgetting: Hidden representations and task semantics. arXiv preprint arXiv:2007.07400.

Riemer, M.; Cases, I.; Ajemian, R.; Liu, M.; Rish, I.; Tu, Y.; and Tesauro, G. 2018. Learning to learn without forgetting by maximizing transfer and minimizing interference. arXiv preprint arXiv:1810.11910.

Sakaguchi, K.; Bras, R. L.; Bhagavatula, C.; and Choi, Y. 2021. Winogrande: An adversarial winograd schema challenge at scale. Communications of the ACM, 64(9): 99–106.

Sap, M.; Rashkin, H.; Chen, D.; LeBras, R.; and Choi, Y. 2019. Socialiqa: Commonsense reasoning about social interactions. arXiv preprint arXiv:1904.09728.

Tang, P.; Liu, Y.; Zhang, D.; Wu, X.; and Zhang, D. 2025. Lora-null: Low-rank adaptation via null space for large language models. arXiv preprint arXiv:2503.02659.

Touvron, H.; Martin, L.; Stone, K.; Albert, P.; Almahairi, A.; Babaei, Y.; Bashlykov, N.; Batra, S.; Bhargava, P.; Bhosale, S.; et al. 2023. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288.

Wang, H.; Li, Y.; Wang, S.; Chen, G.; and Chen, Y. 2024. Milora: Harnessing minor singular components for parameter-efficient llm finetuning. arXiv preprint arXiv:2406.09044.

Yang, A.; Yang, B.; Zhang, B.; Hui, B.; Zheng, B.; Yu, B.; Li, C.; Liu, D.; Huang, F.; Wei, H.; Lin, H.; Yang, J.; Tu, J.; Zhang, J.; Yang, J.; Yang, J.; Zhou, J.; Lin, J.; Dang, K.; Lu, K.; Bao, K.; Yang, K.; Yu, L.; Li, M.; Xue, M.; Zhang, P.; Zhu, Q.; Men, R.; Lin, R.; Li, T.; Tang, T.; Xia, T.; Ren, X.; Ren, X.; Fan, Y.; Su, Y.; Zhang, Y.; Wan, Y.; Liu, Y.; Cui, Z.; Zhang, Z.; and Qiu, Z. 2025a. Qwen2.5 Technical Report. arXiv:2412.15115.

Yang, Y.; Li, X.; Zhou, Z.; Song, S. L.; Wu, J.; Nie, L.; and Ghanem, B. 2025b. CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning. arXiv:2406.05223.

Yu, L.; Jiang, W.; Shi, H.; Yu, J.; Liu, Z.; Zhang, Y.; Kwok, J. T.; Li, Z.; Weller, A.; and Liu, W. 2023. Metamath: Bootstrap your own mathematical questions for large language models. arXiv preprint arXiv:2309.12284.

Zellers, R.; Holtzman, A.; Bisk, Y.; Farhadi, A.; and Choi, Y. 2019. Hellaswag: Can a machine really finish your sentence? arXiv preprint arXiv:1905.07830.

Zheng, T.; Zhang, G.; Shen, T.; Liu, X.; Lin, B. Y.; Fu, J.; Chen, W.; and Yue, X. 2025. OpenCodeInterpreter: Integrating Code Generation with Execution and Refinement. arXiv:2402.14658.

## B-ocr-7c84b12bd5c057

B PDF page 3

![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

Figure 1: Comparison of standard LoRA (left) and our proposed OPLoRA (right). The pre-trained weight matrix W is decomposed via singular value decomposition (SVD) as  \( W = U \Sigma V^{\top} \) . During fine-tuning, the standard LoRA update BA is sandwiched between two frozen projection matrices,  \( P_{L} = (I - U_{k} U_{k}^{\top}) \)  and  \( P_{R} = (I - V_{k} V_{k}^{\top}) \) . This structure constrains the low-rank adaptation to lie in the orthogonal complement of the pre-trained dominant subspace, mitigating interference with essential model knowledge and reducing catastrophic forgetting.

In practice, fine-tuning with LoRA can lead to catastrophic forgetting, where essential knowledge encoded in the pre-trained model is overwritten during adaptation fine-tuning.

The forgetting phenomenon is often implicit and hard to quantify. To better understand it, we analyze the learned adaptation  \( \Delta W \)  relative to the singular directions of  \( W_{0} \) . Specifically, we ask: Does the LoRA update interfere with the most important components of the  \( W_{0} \) ?

To answer this, we leverage the Singular Value Decomposition, which decomposes the weight matrix  \( W_{0} \)  into:

\[
W _ {0} = U \Sigma V ^ {\top}, \tag {2}
\]

where U and V are orthogonal matrices, and  \( \Sigma \)  is a diagonal matrix of singular values sorted in descending order. The leading k left singular vectors,  \( U_{k} \in R^{d_{out} \times k} \) , define the principal column subspace of  \( W_{0} \) , embodying the directions with maximal spectral energy or task-critical information.

Empirical observations (Li et al. 2018; Aghajanyan, Zettlemoyer, and Gupta 2020; Hu et al. 2022) show that singular values of  \( W_{0} \)  decay rapidly, meaning the essential semantics of the layer are concentrated in a low-dimensional subspace. However, since the LoRA weight is unconstrained during training, the resulting update  \( \Delta W \)  may interfere with these top directions—modifying them and causing loss of important pre-trained knowledge.

To make this interference measurable, we define a subspace alignment metric \(\rho_{k}\), which quantifies how much of \(\Delta W\) lies within the top-\(k\) singular directions of \(W_{0}\).

Let \( Q_{k} = U_{k}U_{k}^{\top} \) denote the orthogonal projector onto the column space of \( W \). Then, we can decompose the LoRA update \( \Delta W \) as:

\[
\Delta W = Q _ {k} \Delta W + (I - Q _ {k}) \Delta W, \tag {3}
\]

where the first term lies within the column space of W, and the second term lies in its orthogonal complement. Using the

Pythagorean property of orthogonal projections, we have:

\[
\left| \left| \Delta W \right| \right| _ {F} ^ {2} = \left| \left| Q _ {k} \Delta W \right| \right| _ {F} ^ {2} + \left| \left| (I - Q _ {k}) \Delta W \right| \right| _ {F} ^ {2}. \tag {4}
\]

Then we define:

\[
\rho_ {k} = \frac {\left| \left| Q _ {k} \Delta W \right| \right| _ {F} ^ {2}}{\left| \left| \Delta W \right| \right| _ {F} ^ {2}} \in [ 0, 1 ], \tag {5}
\]

which measures the proportion of the updated spectral energy that lies within the original top-k column space of \( W \).

A value of  \( \rho_{k} \rightarrow 1 \)  implies that the LoRA update stays mostly in the original subspace and may risk interfering with pre-trained features. Conversely,  \( \rho_{k} \rightarrow 0 \)  indicates that the update explores directions orthogonal to the pre-trained space—potentially enabling new task-specific representations while preserving prior knowledge.

### Preserving Pre-trained Knowledge via Orthogonal Projection

To avoid disrupting the dominant directions of \( W_0 \), we confine the LoRA update to the orthogonal complement of its top-\( k \) subspace. Let \( U_k \in \mathbb{R}^{d_{\mathrm{out}} \times k} \) be the matrix of the top-\( k \) left singular vectors of \( W_0 \) (\( k \) is a hyperparameter). Define the orthogonal projector onto the complement of \( \operatorname{span}\{U_k\} \)

\[
P = I - U _ {k} U _ {k} ^ {\top}. \tag {6}
\]

We will show that the LoRA update  \( \Delta W = PBA \)  is entirely confined to this complementary subspace, ensuring it contains no components along the dominant k singular directions.

Proposition 1. Let \( U_{k} \in \mathbb{R}^{d_{\mathrm{out}} \times k} \) be an orthonormal basis for the top-\( k \) left singular vectors of \( W_{0} \in \mathbb{R}^{d_{\mathrm{out}} \times d_{\mathrm{in}}} \). Define the orthogonal projector onto the complement of \( \operatorname{span}\{U_k\} \) as \( P = I - U_k U_k^\top \). For every LoRA update \( \Delta W = PBA \) and any input vector \( x \), the output \( \Delta Wx = PBAx \) resides completely in the orthogonal complement of \( \operatorname{span}\{U_k\} \), i.e.,

\[
U _ {k} ^ {\top} (P B A x) = 0 \quad \text { for   all } x. \tag {7}
\]

## B-ocr-802dea000e9ec5

B PDF page 5

![img-2.jpeg](img-2.jpeg)

(a) Subspace alignment with top-k directions.

![img-3.jpeg](img-3.jpeg)

(b) Comparison of Average Forgetting Evaluation Score.

Figure 2: Quantifying and Mitigating Forgetting in LoRA-based Fine-Tuning. (a) Subspace alignment \(\rho_{k}\) between the learned LoRA update and the top-\(k\) singular directions of the pre-trained weight matrix \(W_{0}\) in the LLaMA-2 7B layers.0.self.attn.q_proj. A higher \(\rho_{k}\) indicates stronger interference with pre-trained knowledge. OPLoRA-128 achieves the lowest alignment across all \(k\), indicating better preservation of prior knowledge. Note that \(\rho_{k}\) is not exactly zero for OPLoRA-128 due to the use of a low-rank SVD approximation (svd_lowrank) for computational efficiency. (b) Average forgetting scores evaluated on three held-out commonsense reasoning tasks after fine-tuning. Higher scores indicate better retention of pre-trained knowledge. Methods are sorted by their corresponding subspace alignment value \(\rho_{16}\) (shown in (a)). A clear negative correlation is observed: lower \(\rho_{16}\) aligns with better forgetting robustness.

[tbl-0.html](tbl-0.html)

Table 1: Comparison of LoRA-based methods on whether they utilize SVD-based initialization without requiring the residual weight matrix  \( W_{res} \) , and whether they explicitly address catastrophic forgetting.

### Commonsense Reasoning

The commonsense reasoning benchmark consists of eight sub-tasks, BoolQ (Clark et al. 2019), PIQA (Bisk et al. 2020), SIQA (Sap et al. 2019), HellaSwag (Zellers et al. 2019), WinoGrande (Sakaguchi et al. 2021), ARC-e, ARC-c (Clark et al. 2018), and OBQA (Mihaylov et al. 2018). Models are fine-tuned on Commonsense170k (Hu et al. 2023) with evaluation performed on individual task test sets using accuracy as the primary metric. Results are presented in Tables 2 and 3.

OPLoRA demonstrates exceptional adaptation performance across both model architectures. On LLaMA-2 7B, OPLoRA-128 secures the highest accuracy on four tasks: BoolQ (82.78%), HellaSwag (75.38%), ARC-c (52.39%), and OBQA (45.8%). Meanwhile, OPLoRA-16 consistently achieves second-best performance on BoolQ, PIQA, HellaSwag, and ARC-c. This pattern extends to Qwen2.5 7B, where OPLoRA-16 leads on four tasks (HellaSwag, Wino-Grande, ARC-e, OBQA) while OPLoRA-128 excels on PIQA and ARC-c. The consistent top-two ranking across di

verse reasoning challenges demonstrates that our orthogonal projection approach preserves adaptation quality across different projection ranks.

To assess catastrophic forgetting, we evaluate retention of general knowledge on three held-out domains: MathQA (mathematical reasoning) (Amini et al. 2019), MBPP (code generation) (Austin et al. 2021), and RACE (reading comprehension) (Lai et al. 2017). These cross-domain evaluations provide critical insights into knowledge preservation during fine-tuning. As shown on the right side of Table 2, OPLoRA exhibits strong resistance to catastrophic forgetting on LLaMA-2 7B. Among all methods, OPLoRA-128 achieves the highest accuracy across all three held-out tasks, closely followed by OPLoRA-16. These results highlight the effectiveness of preserving the dominant subspace of pre-trained weights in maintaining general knowledge during fine-tuning. Similar improvements are observed with Qwen2.5 7B. OPLoRA-16 achieves the highest accuracy on MBPP and ranks second on both MathQA and RACE, while OPLoRA-128 obtains the best performance on MathQA and the second-best on MBPP.

### Mathematical Reasoning

For mathematical reasoning, we fine-tune each model on the first 100K examples from the MetaMathQA dataset (Yu et al. 2023). Evaluation is performed on two in-domain tasks: MATH (Hendrycks et al. 2021) and GSM8K (Cobbe et al. 2021), and we report Exact Match (EM) against the ground truth for each test set. As shown in Table 4 and Table 5, OPLoRA achieves strong adaptation performance compared to baseline methods on both LLaMA-2 7B and Qwen2.5 7B.

On LLaMA-2 7B, OPLoRA-16 achieves the best performance on both MATH (7.04%) and GSM8K (49.73%), with

[OCR table id=tbl-0.html; page=5]
<table><tr><td>Method</td><td>SVD Without \( W_{\text{res}} \)</td><td>Forgetting Mitigation</td></tr><tr><td>LoRA</td><td>×</td><td>×</td></tr><tr><td>PiSSA</td><td>×</td><td>×</td></tr><tr><td>MiLoRA</td><td>×</td><td>×</td></tr><tr><td>LoRA-Null</td><td>×</td><td>√</td></tr><tr><td>OPLoRA</td><td>√</td><td>√</td></tr></table>

## B-ocr-b63105c6234b9c

B PDF page 1

arXiv:2510.13003v2 [cs.CL] 8 Nov 2025

# OPLoRA: Orthogonal Projection LoRA Prevents Catastrophic Forgetting during Parameter-Efficient Fine-Tuning

Yifeng Xiong \( ^{1} \) , Xiaohui Xie \( ^{1} \)

\( ^{1} \) University of California, Irvine

## Abstract

Low-Rank Adaptation (LoRA) enables efficient fine-tuning of large language models but suffers from catastrophic forgetting when learned updates interfere with the dominant singular directions that encode essential pre-trained knowledge. We propose Orthogonal Projection LoRA (OPLoRA), a theoretically grounded approach that prevents this interference through double-sided orthogonal projections. By decomposing frozen weights via SVD, OPLoRA constrains LoRA updates to lie entirely within the orthogonal complement of the top-k singular subspace using projections  \( P_{L} = I - U_{k}U_{k}^{\top} \)  and  \( P_{R} = I - V_{k}V_{k}^{\top} \) . We prove that this construction exactly preserves the top-k singular triples, providing mathematical guarantees for knowledge retention. To quantify subspace interference, we introduce  \( \rho_{k} \) , a metric measuring update alignment with dominant directions. Extensive experiments across commonsense reasoning, mathematics, and code generation demonstrate that OPLoRA significantly reduces forgetting while maintaining competitive task-specific performance on LLaMA-2 7B and Qwen2.5 7B, establishing orthogonal projection as an effective mechanism for knowledge preservation in parameter-efficient fine-tuning.

## Introduction

The widespread adoption of large language models has created an urgent need for efficient adaptation techniques that can specialize pre-trained models for downstream tasks without incurring prohibitive computational costs (Houlsby et al. 2019; Lester, Al-Rfou, and Constant 2021; Liu et al. 2022). Low-Rank Adaptation (LoRA) (Hu et al. 2022) has emerged as a leading method for parameter-efficient fine-tuning, enabling task-specific customization by learning low-rank updates to frozen weight matrices while significantly reducing memory and compute requirements.

However, despite its computational advantages, LoRA suffers from a critical limitation: it provides no explicit mechanism to preserve the essential knowledge encoded in pre-trained weights, leading to catastrophic forgetting that degrades general capabilities after task-specific fine-tuning (Biderman et al. 2024; Yang et al. 2025b; Dou et al. 2024). This forgetting phenomenon presents a substantial challenge for real-world deployment, where models are expected to

retain their foundational knowledge while acquiring new, task-specific capabilities. The core issue lies in LoRA's unconstrained optimization process, which permits learned updates to inadvertently interfere with the principal representational subspaces of the pre-trained model.

Our key insight is that essential pre-trained knowledge is concentrated in the dominant singular directions—the subspaces corresponding to the largest singular values of weight matrices. By constraining LoRA updates to lie entirely within the orthogonal complement of these critical subspaces, we can provably prevent interference with pre-trained knowledge while maintaining expressive capacity for task-specific adaptation.

We present Orthogonal Projection LoRA (OPLoRA), which implements this constraint through a simple yet powerful modification: applying orthogonal projections to both sides of the low-rank update. Our method decomposes pretrained weight matrices using Singular Value Decomposition and constructs projection matrices that remove any component aligned with the top-k singular directions. This ensures that the learned adaptation  \( \Delta W = P_{L} B A P_{R} \)  lies entirely in the orthogonal complement of the dominant subspace, where  \( P_{L} \)  and  \( P_{R} \)  are orthogonal projectors onto the complement of the top-k left and right singular vectors.

We provide theoretical guarantees proving that this construction exactly preserves the top-k singular triples of the original weight matrices, offering a principled and mathematically grounded solution to the forgetting problem. To quantify subspace interference, we introduce  \( \rho_{k} \) , a novel metric that measures the proportion of update energy residing within the dominant subspace of pre-trained weights.

Extensive experiments across commonsense reasoning, mathematics, and code generation on LLaMA-2 7B (Touvron et al. 2023) and Qwen2.5 7B (Yang et al. 2025a) demonstrate that OPLoRA reduces catastrophic forgetting while maintaining competitive task-specific performance. Our approach consistently surpasses existing LoRA variants in retaining knowledge across diverse benchmarks.

We summarize our contributions as follows:

- We present an analysis of catastrophic forgetting in LoRA by introducing \(\rho_{k}\), a subspace alignment metric that quantitatively measures interference with pre-trained knowledge.
- We propose Orthogonal Projection LoRA, a theoreti-

## B-ocr-b814d9fe2dbc77

B PDF page 8

## Supplementary

### Experiment Details

All experiments are conducted on a single NVIDIA RTX A6000 GPU. The software environment consists of PyTorch 2.4.0, CUDA 12.1, FlashAttention 2.7.4, Hugging Face Hub 0.30.2, PEFT 0.14.0, and Transformers 4.45.1. We employ DeepSpeed ZeRO-2 for memory-efficient training. Both backbone models, LLaMA-2 7B (Touvron et al. 2023) and Qwen2.5 7B (Yang et al. 2025a), are publicly available via the Hugging Face.

We primarily use the lm_eval 0.4.9 for evaluating commonsense reasoning tasks and measuring forgetting across all held-out benchmarks. For code generation evaluation, we adopt the evalplus 0.3.1. For mathematics-related tasks, we utilize the evaluation scripts provided by the PiSSA (Meng, Wang, and Zhang 2024).

### Computational Efficiency

Although OPLoRA applies double-sided projections, it does not require forming large dense projection matrices. Specifically,  \( \Delta Wx = P_{L}BAP_{R}x = (I - U_{k}U_{k}^{\top})BA(I - V_{k}V_{k}^{\top})x \)  is computed sequentially:  \( x \leftarrow x - V_{k}(V_{k}^{\top}x) \) ;  \( x \leftarrow BAx \) ;  \( x \leftarrow x - U_{k}(U_{k}^{\top}x) \) . All steps are low-rank. Let  \( B \in R^{m \times r} \)  and  \( A \in R^{r \times n} \) . Standard LoRA requires  \( 2r(m + n) \)  FLOPs per layer, while OPLoRA requires approximately  \( (4k + 2r + 1)(m + n) \)  FLOPs per layer. In practice, the overhead is modest: on LLaMA-2 7B (Commonsense task), training with LoRA takes 5 h 13 m, whereas OPLoRA takes 6 h 12 m. This additional cost is small relative to overall training time, and scaling OPLoRA to 70B models is computationally feasible; our experiments are limited primarily by available compute resources.

### Low-Rank SVD

OPLoRA relies on the top-k singular triples of each weight matrix, which we obtain using a truncated SVD that directly extracts the leading singular vectors without a full decomposition. The one-time SVD initialization takes 5.5 minutes, which is negligible compared to the 6 h 12 m training time. Because truncated SVD is an iterative approximation, a small amount of leakage into the preserved subspace may occur. However, the resulting alignment metric  \( \rho_{k} \)  remains extremely small in practice (Figure 2(a)): for OPLoRA-128,  \( \rho_{128} \)  is 0.003, and  \( \rho_{64} \)  and all smaller k are below  \( 1.4 \times 10^{-5} \) . These values confirm that our theoretical preservation guarantee is effectively maintained in practice.

## References

Aghajanyan, A.; Zettlemoyer, L.; and Gupta, S. 2020. Intrinsic dimensionality explains the effectiveness of language model fine-tuning. arXiv preprint arXiv:2012.13255.

Amini, A.; Gabriel, S.; Lin, P.; Koncel-Kedziorski, R.; Choi, Y.; and Hajishirzi, H. 2019. MathQA: Towards Interpretable Math Word Problem Solving with Operation-Based Formalisms. arXiv:1905.13319.

Austin, J.; Odena, A.; Nye, M.; Bosma, M.; Michalewski, H.; Dohan, D.; Jiang, E.; Cai, C.; Terry, M.; Le, Q.; et al.

[tbl-7.html](tbl-7.html)

Table 8: Hyperparameter configuration used across all experiments.

2021. Program synthesis with large language models. arXiv preprint arXiv:2108.07732.

Biderman, D.; Portes, J.; Ortiz, J. J. G.; Paul, M.; Greengard, P.; Jennings, C.; King, D.; Havens, S.; Chiley, V.; Frankle, J.; Blakeney, C.; and Cunningham, J. P. 2024. LoRA Learns Less and Forgets Less. Transactions on Machine Learning Research. Featured Certification.

Bisk, Y.; Zellers, R.; Gao, J.; Choi, Y.; et al. 2020. Piqa: Reasoning about physical commonsense in natural language. In Proceedings of the AAAI conference on artificial intelligence, volume 34, 7432–7439.

Büyükakyüz, K. 2024. Olora: Orthonormal low-rank adaptation of large language models. arXiv preprint arXiv:2406.01775.

Clark, C.; Lee, K.; Chang, M.-W.; Kwiatkowski, T.; Collins, M.; and Toutanova, K. 2019. BoolQ: Exploring the Surprising Difficulty of Natural Yes/No Questions. In Burstein, J.; Doran, C.; and Solorio, T., eds., Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), 2924–2936. Minneapolis, Minnesota: Association for Computational Linguistics.

Clark, P.; Cowhey, I.; Etzioni, O.; Khot, T.; Sabharwal, A.; Schoenick, C.; and Tafjord, O. 2018. Think you have solved question answering? try arc, the ai2 reasoning challenge. arXiv preprint arXiv:1803.05457.

Cobbe, K.; Kosaraju, V.; Bavarian, M.; Chen, M.; Jun, H.; Kaiser, L.; Plappert, M.; Tworek, J.; Hilton, J.; Nakano, R.; Hesse, C.; and Schulman, J. 2021. Training Verifiers to Solve Math Word Problems. arXiv:2110.14168.

Dou, S.; Zhou, E.; Liu, Y.; Gao, S.; Zhao, J.; Shen, W.; Zhou, Y.; Xi, Z.; Wang, X.; Fan, X.; Pu, S.; Zhu, J.; Zheng, R.; Gui, T.; Zhang, Q.; and Huang, X. 2024. LoRAMoE: Alleviate World Knowledge Forgetting in Large Language Models via MoE-Style Plugin. arXiv:2312.09979.

Farajtabar, M.; Azizan, N.; Mott, A.; and Li, A. 2020. Orthogonal gradient descent for continual learning. In International conference on artificial intelligence and statistics, 3762–3773. PMLR.

[OCR table id=tbl-7.html; page=8]
<table><tr><td>Hyperparameter</td><td>Commonsense</td><td>Math</td><td>Python</td></tr><tr><td>LoRA rank (r)</td><td>32</td><td>64</td><td>32</td></tr><tr><td>Scaling factor (α)</td><td>32</td><td>64</td><td>32</td></tr><tr><td>LoRA dropout</td><td></td><td>0.05</td><td></td></tr><tr><td>Learning rate</td><td>2e-4</td><td>3e-4</td><td>2e-4</td></tr><tr><td>Batch size</td><td></td><td>32</td><td></td></tr><tr><td>Epochs</td><td></td><td>1</td><td></td></tr><tr><td>Weight decay</td><td></td><td>0.0</td><td></td></tr><tr><td>Learning rate scheduler</td><td></td><td>Cosine</td><td></td></tr><tr><td>Warmup ratio</td><td></td><td>0.03</td><td></td></tr><tr><td>Precision</td><td></td><td>bfloat16</td><td></td></tr></table>

## B-ocr-dfb5ee45554ea2

B PDF page 6

[tbl-1.html](tbl-1.html)

Table 2: Comparison of LoRA-based fine-tuning methods on commonsense reasoning and forgetting benchmarks. We evaluate each method on eight commonsense tasks (left) to assess fine-tuning performance, and on three held-out tasks (right) to measure the extent of catastrophic forgetting. All models are fine-tuned from LLaMA-2 7B. Bold and underlined values indicate the best and second-best scores.

[tbl-2.html](tbl-2.html)

Table 3: Comparison of LoRA-based fine-tuning methods on commonsense reasoning and forgetting benchmarks. All models are fine-tuned from Qwen2.5 7B. Bold and underlined values indicate the best and second-best scores.

OPLoRA-128 closely following with 6.88% and 49.35%. Both variants outperform all baseline methods. For Qwen2.5 7B, a similar pattern emerges. OPLoRA-16 achieves the highest score on both MATH (47.34%) and GSM8K (83.70%), while OPLoRA-128 is competitive with 46.72% and matches the top GSM8K score (83.70%).

To assess catastrophic forgetting, we evaluate each model on three held-out commonsense reasoning tasks: ARC-e, ARC-c, and SIQA. OPLoRA-128 obtains the best overall forgetting performance on LLaMA-2 7B, with OPLoRA-16 following closely behind. On Qwen2.5 7B, OPLoRA-128 again delivers the strongest forgetting resistance, achieving the best scores on ARC-e and SIQA, and performing competitively on ARC-c. OPLoRA-16 achieves the top score on ARC-c and ranks second on ARC-e and SIQA. Compared to all baselines, both OPLoRA variants show more balanced retention across all three tasks.

### Python Code Generation

To evaluate code generation capabilities, we fine-tune each model on the CodeFeedback dataset (Zheng et al. 2025). Performance is assessed using two in-domain benchmarks, MBPP and MBPP++, where we report functional correctness as measured by pass@1 accuracy—the percentage of generated programs that pass all unit tests on the first attempt. The results are presented in Table 6 and Table 7 for

LLaMA-2 7B and Qwen2.5 7B.

On LLaMA-2 7B, OPLoRA-16 achieves the highest performance on both MBPP (40.5%) and MBPP++ (34.1%), outperforming all baselines by a notable margin. OPLoRA-128 also performs strongly, achieving 39.2% on MBPP and 31.0% on MBPP++. The trends hold for Qwen2.5 7B as well. OPLoRA-16 obtains the top score on MBPP++ (69.0%) and matches LoRA on MBPP (80.2%), while OPLoRA-128 ranks second on MBPP (80.4%) and MBPP++ (68.8%). These findings confirm the flexibility of OPLoRA in handling both prompt-based and completion-style code generation benchmarks.

For forgetting, we evaluate the models on three held-out commonsense reasoning tasks: HellaSwag, OBQA, and SIQA. On LLaMA-2 7B, OPLoRA-128 achieves the highest accuracy on OBQA (45.6%) and HellaSwag (77.0%), while OPLoRA-16 obtains the best result on SIQA (47.1%) and the second-best on HellaSwag. For Qwen2.5 7B, OPLoRA-128 delivers the highest forgetting resistance overall, achieving the best scores on HellaSwag (79.2%), OBQA (47.4%), and SIQA (55.5%). OPLoRA-16 follows closely with strong performance across all three tasks.

### Subspace Interference Analysis

We analyze subspace interference to better understand the mechanism of catastrophic forgetting in LoRA-based fine-

[OCR table id=tbl-1.html; page=6]
<table><tr><td rowspan="2">Method</td><td colspan="8">Fine-Tuning Evaluation</td><td colspan="3">Forgetting Evaluation</td><td rowspan="2">Avg</td></tr><tr><td>BoolQ</td><td>PIQA</td><td>SIQA</td><td>HSwag</td><td>WinoG</td><td>ARC-e</td><td>ARC-c</td><td>OBQA</td><td>MathQA</td><td>MBPP</td><td>RACE</td></tr><tr><td colspan="13">Baseline Methods</td></tr><tr><td>LoRA</td><td>81.00</td><td>80.19</td><td>51.58</td><td>74.73</td><td>72.84</td><td>79.29</td><td>50.51</td><td>44.8</td><td>29.08</td><td>20.2</td><td>43.06</td><td>57.03</td></tr><tr><td>PiSSA</td><td>62.11</td><td>55.11</td><td>34.80</td><td>28.33</td><td>49.32</td><td>28.45</td><td>26.79</td><td>26.4</td><td>22.88</td><td>0</td><td>22.39</td><td>32.42</td></tr><tr><td>MiLoRA</td><td>82.04</td><td>78.99</td><td>54.24</td><td>75.04</td><td>73.40</td><td>79.08</td><td>52.21</td><td>45.4</td><td>28.21</td><td>18.6</td><td>41.4</td><td>57.15</td></tr><tr><td>LoRA-Null</td><td>82.02</td><td>77.97</td><td>51.43</td><td>74.74</td><td>72.88</td><td>77.48</td><td>48.29</td><td>42.6</td><td>28.98</td><td>9.8</td><td>42.20</td><td>55.31</td></tr><tr><td colspan="13">Our Methods</td></tr><tr><td>OPLoRA-16</td><td>82.42</td><td>79.16</td><td>52.92</td><td>75.35</td><td>72.30</td><td>79.55</td><td>52.30</td><td>45.2</td><td>29.08</td><td>20.2</td><td>43.06</td><td>57.41</td></tr><tr><td>OPLoRA-128</td><td>82.78</td><td>79.11</td><td>53.53</td><td>75.38</td><td>73.24</td><td>79.25</td><td>52.39</td><td>45.8</td><td>29.88</td><td>20.4</td><td>43.63</td><td>57.76</td></tr></table>

[OCR table id=tbl-2.html; page=6]
<table><tr><td rowspan="2">Method</td><td colspan="8">Fine-Tuning Evaluation</td><td colspan="3">Forgetting Evaluation</td><td rowspan="2">Avg</td></tr><tr><td>BoolQ</td><td>PIQA</td><td>SIQA</td><td>HSwag</td><td>WinoG</td><td>ARC-e</td><td>ARC-c</td><td>OBQA</td><td>MathQA</td><td>MBPP</td><td>RACE</td></tr><tr><td colspan="13">Baseline Methods</td></tr><tr><td>LoRA</td><td>86.75</td><td>79.76</td><td>51.43</td><td>78.12</td><td>73.95</td><td>76.26</td><td>55.03</td><td>45.8</td><td>50.35</td><td>58.6</td><td>39.62</td><td>63.24</td></tr><tr><td>PiSSA</td><td>75.04</td><td>75.08</td><td>52.04</td><td>71.75</td><td>75.92</td><td>69.23</td><td>43.85</td><td>42.0</td><td>31.86</td><td>0.6</td><td>40.57</td><td>52.54</td></tr><tr><td>MiLoRA</td><td>86.05</td><td>77.36</td><td>53.42</td><td>74.73</td><td>76.47</td><td>71.42</td><td>52.13</td><td>44.4</td><td>46.47</td><td>2.6</td><td>39.62</td><td>56.79</td></tr><tr><td>LoRA-Null</td><td>83.30</td><td>77.61</td><td>51.57</td><td>75.67</td><td>74.51</td><td>75.84</td><td>54.83</td><td>46.8</td><td>50.24</td><td>19.8</td><td>40.11</td><td>59.12</td></tr><tr><td colspan="13">Our Methods</td></tr><tr><td>OPLoRA-16</td><td>86.64</td><td>79.38</td><td>52.56</td><td>79.01</td><td>76.64</td><td>78.54</td><td>55.46</td><td>47.8</td><td>50.92</td><td>59.6</td><td>40.28</td><td>64.26</td></tr><tr><td>OPLoRA-128</td><td>86.64</td><td>79.76</td><td>51.43</td><td>77.62</td><td>74.03</td><td>76.14</td><td>56.14</td><td>47.4</td><td>51.29</td><td>59.2</td><td>39.23</td><td>63.53</td></tr></table>

## B-ocr-f1df3b3bdef289

B PDF page 2

cally grounded method that provably preserves the dominant singular directions of pre-trained weights through double-sided orthogonal projections.

- We validate our approach through extensive experiments across three domains and two model architectures, demonstrating significant improvements in forgetting resistance while maintaining competitive adaptation performance.

## Related Works

### Low-Rank Adaptation and Extensions

LoRA (Hu et al. 2022) is a foundational method for parameter-efficient fine-tuning (PEFT) that introduces trainable low-rank matrices into each weight layer while keeping the pre-trained weights frozen. The core idea is that task-specific knowledge can be captured through a low-dimensional subspace, reducing both memory and computational requirements. Recent work has extended this framework through sophisticated weight decomposition strategies, notably DoRA (Liu et al. 2024), which addresses the limited expressiveness of vanilla LoRA by decomposing pre-trained weight matrices into magnitude and direction components and applying low-rank adaptation exclusively to the direction component. A parallel line of research has focused on exploiting the inherent structure of pre-trained weights through singular value decomposition, with PiSSA (Meng, Wang, and Zhang 2024) replacing LoRA's random initialization with principled construction using the principal singular vectors and values of frozen weight matrices, enabling direct modification of the essential subspace and improved alignment between low-rank updates and full fine-tuning behavior. In contrast, MiLoRA (Wang et al. 2024) adopts a complementary approach by explicitly preserving the dominant subspace of pre-trained weights, performing SVD on each weight matrix and freezing the principal components during fine-tuning while updating only the minor singular components via low-rank adaptation, thereby constraining initialization to a subspace orthogonal to core pre-trained knowledge and minimizing interference with essential representations. Additionally, OLoRA (Büyükkyüz 2024) focuses on improving optimization landscapes by initializing adaptation matrices with orthonormal bases derived through QR decomposition, constraining updates to well-conditioned subspaces to promote improved gradient flow and convergence stability across diverse tasks.

### Catastrophic Forgetting and Knowledge Preservation

Catastrophic forgetting represents a fundamental challenge in continual learning and fine-tuning, where models lose previously acquired knowledge when learning new tasks (Ramasesh, Dyer, and Raghu 2020). In the context of large language models, this phenomenon manifests as degraded performance on general capabilities after task-specific fine-tuning, posing significant practical limitations for real-world deployment. The measurement and mitigation of catastrophic forgetting have become critical research directions, with various approaches emerging to quantify and address

this problem. Early mitigation strategies focused on regularization and replay mechanisms. Elastic Weight Consolidation (EWC) (Kirkpatrick et al. 2017) constrains training updates with a Fisher information-weighted quadratic penalty to identify and protect crucial weights from previous tasks. Learning Without Forgetting (LwF) (Li and Hoiem 2017) addresses forgetting without retaining old data by recording the original network's soft outputs on new-task data, then training the model to match those pseudo-labels while learning new labels. Meta-Experience Replay (MER) (Riemer et al. 2018) combines each incoming example with a small reservoir of past samples and applies lightweight Reptile meta-updates that encourage gradient alignment across old and new data, maximizing transfer while reducing interference. Orthogonal Gradient Descent (OGD) (Farajtabar et al. 2020) tackles catastrophic forgetting by constraining every new gradient step to be orthogonal to the gradient directions that mattered for earlier tasks. Instead of storing old data, it stores a compact set of per-task prediction-gradient vectors; before each parameter update, the current task's gradient is projected into the null-space of those stored directions. Recent research has increasingly explored parameter-efficient fine-tuning techniques as a natural solution to knowledge preservation. Within the LoRA framework, MiLoRA attempts to preserve dominant pre-trained weights by initializing LoRA matrices with minor singular components, constraining adaptation to less critical subspaces. However, MiLoRA does not explicitly address the problem of catastrophic forgetting. The most recent work, LoRA-Null (Tang et al. 2025), mitigates catastrophic forgetting by leveraging the null space for adapter initialization and constructing LoRA adapters from projections of pre-trained weights onto the null space of representative activations to ensure that update directions do not interfere with pre-trained knowledge.

## Methodology

### Preliminaries: Low-Rank Adaptation (LoRA)

Consider a pre-trained weight matrix $W_0 \in \mathbb{R}^{d_{\mathrm{out}} \times d_{\mathrm{in}}}$. LoRA proposes that task-specific adaptation can be achieved by learning a low-rank update $\Delta W = \frac{\alpha}{r} BA$ instead of updating the full matrix. The forward pass becomes:

$$h = W_0 x + \Delta W x = W_0 x + \frac{\alpha}{r} B A x, \tag{1}$$

where $B \in \mathbb{R}^{d_{\mathrm{out}} \times r}$ and $A \in \mathbb{R}^{r \times d_{\mathrm{in}}}$ are trainable matrices, and $r \ll \min(d_{\mathrm{out}}, d_{\mathrm{in}})$ is the rank. The scaling factor $\alpha$ ensures the update is appropriately scaled.

During fine-tuning, $W_0$ remains frozen while gradients only flow through $A$ and $B$. This strategy significantly reduces the number of trainable parameters and enables efficient adaptation, particularly for large models. LoRA normally preserves the pre-trained model's behavior by initializing $A$ with Kaiming-uniform (He et al. 2015) values and setting $B = 0$.

### Understanding and Quantifying Forgetting in LoRA

While LoRA effectively reduces parameter count, it does not explicitly account for the distribution of information in $W_0$.
