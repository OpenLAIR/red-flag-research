# GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR

## B-0e0a3b66cf5f40

https://arxiv.org/html/2601.09361v2#chars-1817-5847

## 1 Introduction

Large reasoning models, represented by OpenAI-o1 [Jaech et al. (2024)](#bib.bib45) and DeepSeek-R1 [Guo et al. (2025)](#bib.bib44), have established Reinforcement Learning with Verifiable Rewards (RLVR) as a pivotal paradigm for unlocking complex reasoning capabilities. Distinctively, RLVR exhibits the dynamics of a constrained optimization process [Wu et al. (2025)](#bib.bib31), primarily amplifying latent reasoning behaviors via reward-induced sampling bias [Yue et al. (2025)](#bib.bib27); [Zhao et al. ()](#bib.bib42). This makes the paradigm particularly sensitive to the interaction between optimization constraints (e.g., KL regularization) and the pre-trained representation geometry, where overly aggressive updates can collapse behavior or degrade general capabilities. Empirically, strong gains can emerge from modifying only a small fraction of parameters [Mukherjee et al. (2025)](#bib.bib36), and mechanistic studies suggest that effective RLVR updates are geometrically biased to preserve the pre-trained structure [Zhu et al. (2025)](#bib.bib35); [Cai et al. (2025)](#bib.bib29).

However, current PEFT methodologies encounter significant obstacles when applied to the RLVR paradigm. Firstly, SVD-based low-rank adaptation methods are constrained by a severe geometric dimension mismatch [Yin et al. (2025)](#bib.bib37). PiSSA [Meng et al. (2024)](#bib.bib34), for instance, creates a structural conflict by forcing updates on principal components; this directly violates RLVR’s preference for updating non-principal components to protect principal features. Conversely, while MiLoRA [Wang et al. (2025)](#bib.bib38) attempts to accommodate this geometric property by initializing minor components, it fails due to weak initialization amplitudes, leading to optimization collapse where the model rapidly retreats to the principal subspace. Secondly, sparse fine-tuning [Mukherjee et al. (2025)](#bib.bib36); [Zhu et al. (2025)](#bib.bib35) methods designed to exploit RL update patterns struggle with computational efficiency. Due to a lack of modern hardware support for unstructured sparsity, these methods fail to convert theoretical sparsity into real-world speedups. Consequently, the additional overhead often exacerbates, rather than alleviates, the computational burden.

To this end, we introduce GeoRA (Geometry-Aware Low-Rank Adaptation). Our analysis reveals that the RLVR update subspace is not isotropic but possesses a distinct low-rank structure. Leveraging this, GeoRA extracts dominant trainable directions directly from this subspace for initialization, while keeping residual components frozen to preserve knowledge. This approach achieves a dual advantage: it geometrically aligns with RLVR’s optimization dynamics and inherently preserves dense matrix compatibility, thereby delivering high computational efficiency without the overhead of sparse methods. To the best of our knowledge, GeoRA is the first geometry-based low-rank adaptation framework explicitly tailored to RLVR’s distinctive optimization dynamics. Our contributions are summarized as follows:

We propose GeoRA, a geometry-aware, low-rank, and parameter-efficient adaptation framework tailored to RLVR. By aligning low-rank adaptation with RLVR’s distinctive optimization dynamics, GeoRA mitigates spectral mismatch and enables stable training.

We show that the effective RL update subspace is directional and admits a compressible low-rank structure. GeoRA extracts principal trainable directions via SVD within this subspace to initialize low-rank adapters, while a frozen residual component acts as a structural anchor to preserve pre-trained knowledge.

Experiments on Qwen and Llama models demonstrate that GeoRA improves stability and consistently outperforms leading low-rank baselines on multiple mainstream mathematical benchmarks, while exhibiting superior robustness on out-of-distribution tasks.

![Refer to caption](2601.09361v2/fig1v14.png)
![Refer to caption](2601.09361v2/fig2_5.png)

## B-13a5db2f43cc22

https://arxiv.org/html/2601.09361v2#chars-5866-8039

### 2.1 RLVR and Optimization Geometry

RLVR replaces traditional reward models with deterministic verifiers (e.g., in math or coding) [Zhang et al. (2025)](#bib.bib3); [Lambert et al. (2025)](#bib.bib4); [Yuan et al. (2025)](#bib.bib5). Through outcome-based feedback, it incentivizes emergent reasoning behaviors like Chain-of-Thought (CoT), establishing itself as a core paradigm for enhancing LLM reasoning [Hu et al. (2025)](#bib.bib1); [Liu et al. (2025a)](#bib.bib2).

Recent mechanistic analyses have delineated a sharp dichotomy between supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR). While SFT primarily injects knowledge by modifying principal weight directions [Chu et al. (2025)](#bib.bib43); [Jin et al. (2025b)](#bib.bib25), RLVR is better characterized as a constrained optimization process [Wu et al. (2025)](#bib.bib31) that amplifies latent reasoning behaviors via reward-induced sampling bias rather than introducing new capabilities [Yue et al. (2025)](#bib.bib27); [Zhao et al. ()](#bib.bib42); [Alam and Rastogi (2025)](#bib.bib33). Theoretically, these updates manifest “off the principals,” favoring low-magnitude directions orthogonal to pre-trained features [Zhu et al. (2025)](#bib.bib35), consistent with the rank-1 dominance observed in early training [Cai et al. (2025)](#bib.bib29). However, this regime faces stability trade-offs. KL-regularization (“RL’s Razor”) attempts to limit forgetting [Shenfeld et al. (2025)](#bib.bib30) but can precipitate the “Reasoning Boundary Paradox,” where aggressive reward maximization collapses exploration diversity [Nguyen et al. (2025)](#bib.bib32). Although capability degradation may be partially reversed via singular vector rotation [Jin et al. (2025a)](#bib.bib28); [Jin et al. (2025b)](#bib.bib25), adaptation remains fundamentally constrained by the “Invisible Leash,” which enforces proximity to the pre-training manifold [Wu et al. (2025)](#bib.bib31).
Empirically, strong gains can emerge from updating only a small fraction of parameters, suggesting that RL fine-tuning often concentrates on small subnetworks [Mukherjee et al. (2025)](#bib.bib36).

## B-222fec4467cc09

https://arxiv.org/html/2601.09361v2#chars-31511-32421

## References

![[LOGO]](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)

## B-2a8193053ba0da

https://arxiv.org/html/2601.09361v2#chars-16051-16069

## 4 Experiments

## B-571854751c29bb

https://arxiv.org/html/2601.09361v2#chars-26507-28413

### 5.1 Intrinsic Low-Rank Structure of Updates

To validate the structural foundation of GeoRA, we investigate the physical compressibility of learned updates. We analyze the singular value spectrum of the GeoRA update matrix WG​e​oW\_{Geo} and compare it against the original pre-trained weights, as well as random noise matrices at both full density (ρ=1.0\rho=1.0) and sparse density (ρ=0.2\rho=0.2). Figure [6](#S5.F6 "Figure 6 ‣ 5 Mechanism Analysis ‣ GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR") reveals two critical insights that challenge conventional assumptions in sparse fine-tuning:

Sparsity ≠\neq Low-Rankness (The Isotropic Fallacy): A notable observation is that the spectrum of sparse random noise (ρ=0.2\rho=0.2) almost perfectly overlaps with that of dense random noise (ρ=1.0\rho=1.0). Both exhibit a gentle, slowly decaying trajectory, indicating an isotropic (high-rank) distribution of energy. This proves that unstructured sparsity alone fails to induce true geometric structure; in the spectral domain, a sparse random mask is mathematically equivalent to high-entropy white noise.

Inheritance of Pre-trained Geometry: In sharp contrast, the GeoRA update subspace WG​e​oW\_{Geo} retains the characteristic power-law decay of the original pre-trained weights, concentrating the vast majority of information in a few top singular components. This confirms that effective RL updates are not random, but align with the compressible, low-rank structure of the pre-trained model.

This spectral analysis provides the theoretical justification for GeoRA: Since the optimal update subspace is intrinsically low-rank rather than sparsely random, we can replace inefficient unstructured sparsity with SVD-based initialization. This transforms the optimization into efficient dense parameterization, ensuring rigorous geometric alignment while maximizing computational efficiency.

## B-6c5f79f1afacdd

https://arxiv.org/html/2601.09361v2#chars-21055-26287

### 4.2 Ablation Studies and Robustness Analysis

In this section, we conduct a comprehensive analysis to verify the effectiveness of individual components and the stability of our proposed method. To ensure a controlled and efficient evaluation, all experiments in this section are conducted using the Qwen3-4B-Base [Yang et al. (2025)](#bib.bib13) model, optimized via GRPO on the GSM8K [Cobbe et al. (2021)](#bib.bib7) dataset.

Impact of Initialization Strategies. One of the core contributions of GeoRA is the utilization of a geometric prior to initialize trainable parameters. To validate the necessity of this strategy, we compare three distinct initialization methods in Table [3](#S4.T3 "Table 3 ‣ 4.1 Main Results and Efficiency ‣ 4 Experiments ‣ GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR"): (1) GeoRA, which initializes using the top-rr principal components of WG​e​oW\_{Geo};
(2) Random-rr Init, which initializes the low-rank adapters with a random Gaussian distribution; and
(3) Tail-rr Init, which initializes using the bottom-rr components (tail components) derived from the singular value decomposition (SVD) of WG​e​oW\_{Geo}. The experimental results demonstrate that GeoRA’s initialization strategy achieves the best performance (Avg 25.41, Reward 0.88). In comparison, Random-rr Init exhibits a slight performance degradation (Avg 24.60). This suggests that while random initialization is effective for standard LoRA, the lack of prior information hinders optimization under sparse geometric constraints. More importantly, Tail-rr Init performs the worst (Avg 23.40). This confirms our hypothesis that the “tail” components of the weights primarily consist of noise or redundant information; utilizing these components for initialization is not only unbeneficial but actually interferes with the model’s ability to learn critical features. Therefore, leveraging the principal components (Head) of WG​e​oW\_{Geo} is essential for maintaining high performance in extremely low-parameter regimes.

Training Stability. Training instability remains a notorious bottleneck in RL fine-tuning, typically manifesting as abrupt performance degradation or catastrophic reward collapse. We hypothesize that this stems from a fundamental geometric mismatch: PiSSA enforces updates along principal components—directions often associated with high curvature—which is prone to violating the trust region constraint (DK​L<δD\_{KL}<\delta) essential for stable RLVR. To validate this, Figure [5](#S4.F5 "Figure 5 ‣ 4.2 Ablation Studies and Robustness Analysis ‣ 4 Experiments ‣ GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR") presents a stress test conducted under an aggressive learning rate (5×10−55\times 10^{-5}). As illustrated in Figure [5](#S4.F5 "Figure 5 ‣ 4.2 Ablation Studies and Robustness Analysis ‣ 4 Experiments ‣ GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR")(a), PiSSA suffers a catastrophic reward collapse around step 220. Crucially, Figure [5](#S4.F5 "Figure 5 ‣ 4.2 Ablation Studies and Robustness Analysis ‣ 4 Experiments ‣ GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR")(b) uncovers the root cause: this collapse coincides with an explosive surge in KL divergence, indicating that the model has violated optimization constraints and drifted into a degenerate policy space. In stark contrast, GeoRA demonstrates three distinct advantages rooted in its geometric alignment: (1) Superior Optimality: It establishes a significantly higher performance envelope (green curve), indicating more effective exploration of the reasoning manifold compared to all baselines. (2) Intrinsic Stability: It remains immune to collapse, effectively filtering out the destabilizing updates that plague spectrum-misaligned methods. (3) Constraint Adherence: It achieves these gains while maintaining a flat, controlled KL divergence profile. This confirms that GeoRA’s geometry-aware subspace functions as a natural regularizer, enabling the model to maximize rewards strictly within the safe trust region of the pre-trained backbone.

Furthermore, extensive experiments were conducted to validate the model multidimensionally. As shown in Figure [4](#S4.F4 "Figure 4 ‣ 4.2 Ablation Studies and Robustness Analysis ‣ 4 Experiments ‣ GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR"), since instability is often amplified by overly large learning rates, a broad sweep of learning rates attests to GeoRA’s superior stability, ensuring robust convergence where baselines collapse; and parameter sensitivity analysis underscores the model’s resilience, demonstrating competitive performance even under extreme conditions such as ultra-low rank (4) or high sparsity (10%).

|  | Llama-3.1-8B | | | Qwen3-8B | | |
| --- | --- | --- | --- | --- | --- | --- |
| Method | NSS ↓\downarrow | 𝒮Head\mathcal{S}\_{\text{Head}} ↓\downarrow | 𝒮Tail\mathcal{S}\_{\text{Tail}} ↑\uparrow | NSS ↓\downarrow | 𝒮Head\mathcal{S}\_{\text{Head}} ↓\downarrow | 𝒮Tail\mathcal{S}\_{\text{Tail}} ↑\uparrow |
| PiSSA | 0.395 | 0.98 | 0.01 | 0.418 | 0.95 | 0.03 |
| LoRA | 0.214 | 0.15 | 0.15 | 0.235 | 0.18 | 0.18 |
| MiLoRA | 0.125 | 0.12 | 0.92 | 0.132 | 0.16 | 0.90 |
| GeoRA | 0.092 | 0.005 | 0.98 | 0.096 | 0.015 | 0.96 |

## B-824e41069b1037

https://arxiv.org/html/2601.09361v2#chars-26287-26507

## 5 Mechanism Analysis

To reveal the geometric origins of GeoRA’s superior balance between enhancing in-domain (ID) tasks and preserving out-of-domain (OOD) capabilities, we conduct a quantitative mechanism analysis.

## B-869ebe9805787b

https://arxiv.org/html/2601.09361v2#chars-8039-9864

### 2.2 PEFT and Spectral Priors

To alleviate the computational demands of scaling LLMs, PEFT [Xu et al. (2023)](#bib.bib15); [Han et al. (2024)](#bib.bib16) has emerged as a key paradigm, minimizing memory overhead by updating only a fraction of parameters while matching full fine-tuning performance. Prevailing strategies include partial fine-tuning [Zaken et al. (2022)](#bib.bib17); [Lawton et al. (2023)](#bib.bib18), soft prompt tuning [Hambardzumyan et al. (2021)](#bib.bib19), non-linear adapters [Lin et al. (2020)](#bib.bib20), low-rank adaptation [Li et al. (2018)](#bib.bib21), and importance-aware methods like LIFT [Liu et al. (2025b)](#bib.bib6).

Among these, LoRA [Hu et al. (2022)](#bib.bib41) and its variants are the de facto standard, yet their initialization strategies often diverge based on spectral priors. For instance, PiSSA [Meng et al. (2024)](#bib.bib34) allocates trainable parameters to principal singular components, imposing a strong inductive bias validated primarily in SFT. However, such SFT-oriented spectral priors can create a fundamental geometric mismatch in RLVR, whose optimization dynamics and effective update patterns differ markedly from SFT [Yin et al. (2025)](#bib.bib37); [Zhu et al. (2025)](#bib.bib35); [Mukherjee et al. (2025)](#bib.bib36). MiLoRA [Wang et al. (2025)](#bib.bib38) instead targets minor components, but does not explicitly account for RLVR-specific geometry and dynamics. Other variants like DoRA [Liu et al. (2024)](#bib.bib39), AdaLoRA [Zhang et al. (2023)](#bib.bib26), and VeRA [Kopiczko et al. (2023)](#bib.bib40) focus on weight decomposition or budget allocation without integrating these RLVR-native geometric considerations. Building on these observations, GeoRA translates RLVR-specific mechanistic insights into an actionable PEFT paradigm.

## B-89b9b82f992824

https://arxiv.org/html/2601.09361v2#chars-32421-33760

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

## B-9feccaaf07f8d8

https://arxiv.org/html/2601.09361v2#chars-0-209

##### Report GitHub Issue

Content selection saved. Describe the issue below:

![](/static/base/1.0.1/images/icons/smileybones-small.svg)
![arXiv logo](/static/base/1.0.1/images/arxiv-logo-primary-light.svg)

## B-a522ba08fd6031

https://arxiv.org/html/2601.09361v2#chars-9864-10581

## 3 Methodology

We introduce GeoRA (Geometry-Aware Low-Rank Adaptation), a low-rank adaptation framework tailored for RLVR. GeoRA emphasizes an RL-native, structured low-rank parameterization together with an explicit residual leash for stability. Comparing with SFT-oriented PEFT baselines like LoRA and PiSSA, we first present the low-rank forward architecture and initialization (Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR")), and then describe a lightweight masking instantiation that constructs the geometry-constrained matrix used for initialization (Figure [2](#S1.F2 "Figure 2 ‣ 1 Introduction ‣ GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR")).

## B-a58b0235561c66

https://arxiv.org/html/2601.09361v2#chars-28413-29897

### 5.2 Spectral Efficiency and Alignment

Building on the low-rank structure of RL updates, we validate GeoRA’s geometric superiority via Normalized Spectral Shift (NSS) and Subspace Alignment (Table [4](#S4.T4 "Table 4 ‣ 4.2 Ablation Studies and Robustness Analysis ‣ 4 Experiments ‣ GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR")). First, NSS quantifies the topological distortion of the pre-trained manifold:

|  |  |  |  |
| --- | --- | --- | --- |
|  | NSS=‖σ⁡(Wtuned)−σ⁡(W)‖2‖σ⁡(W)‖2.\text{NSS}=\frac{\|\sigma(W^{\text{tuned}})-\sigma(W)\|\_{2}}{\|\sigma(W)\|\_{2}}. |  | (9) |

While PiSSA exhibits high NSS (>0.39>0.39), indicating aggressive structural modification, GeoRA maintains minimal distortion (≈0.09\approx 0.09), confirming it maximizes reward acquisition while preserving fundamental features.

To pinpoint the update locus, we calculate the alignment between Δ​W\Delta W and the pre-trained singular vectors VV:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮⁡(k)=‖Δ​W​vk‖2‖Δ​W‖F≈|cos⁡(θk)|.\mathcal{S}(k)=\frac{\|\Delta Wv\_{k}\|\_{2}}{\|\Delta W\|\_{F}}\approx|\cos(\theta\_{k})|. |  | (10) |

GeoRA shows a distinct signature: it avoids the high-energy principal subspace (𝒮Head≤0.02\mathcal{S}\_{\text{Head}}\leq 0.02)—enhancing stability—and efficiently adapts the geometry-constrained tail (𝒮Tail≥0.96\mathcal{S}\_{\text{Tail}}\geq 0.96). In contrast, PiSSA’s instability is explained by its high overlap with the head subspace (≈0.98\approx 0.98).

## B-b09893273c56fe

https://arxiv.org/html/2601.09361v2#chars-30843-31511

## Limitations

Despite its effectiveness, GeoRA has certain limitations. First, the initialization process requires performing a truncated SVD and dual-masking operations. While these represent a one-time computational cost at the beginning of training, they introduce an additional pre-processing step compared to the random initialization used in standard LoRA. Second, our experiments primarily focus on RLVR in reasoning domains. Although GeoRA demonstrates strong performance on these tasks, its generalizability needs to be further validated across a broader range of model architectures and diverse reinforcement learning scenarios beyond verifiable rewards.

## B-b3fb06bb3cda98

https://arxiv.org/html/2601.09361v2#chars-13029-16051

### 3.2 Geometric Prior Construction

To instantiate a geometry-aware update region, we construct a geometry-constrained matrix WGeoW\_{\text{Geo}} using a masking strategy. This masking is consistent with prior observations on spectral and magnitude structure and stability in fine-tuning [Liu et al. (2025b)](#bib.bib6); [Zhu et al. (2025)](#bib.bib35).

The Spectral Prior (MSpecM\_{\text{Spec}}) promotes geometric stability by selecting the bottom ρ\rho-fraction of entries from the rank-rr approximation W^r\hat{W}\_{r}. The mask is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (MSpec)i,j=𝕀⁡(|(W^r)i,j|≤τSpec​(ρ))(M\_{\text{Spec}})\_{i,j}=\mathbb{I}\left(|(\hat{W}\_{r})\_{i,j}|\leq\tau\_{\text{Spec}}(\rho)\right) |  | (6) |

where τSpec​(ρ)\tau\_{\text{Spec}}(\rho) is the ρ\rho-th quantile of the absolute values in W^r\hat{W}\_{r}. Intuitively, this mask suppresses high-magnitude (and typically high-curvature) components and constrains updates to a more stable, low-magnitude region, improving spectral stability under RLVR.
Similarly, the Euclidean Prior (MEucM\_{\text{Euc}}) selects low-magnitude weights to capture parameter plasticity, using the same sparsity ratio ρ\rho:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (MEuc)i,j=𝕀⁡(|Wi,j|≤τEuc​(ρ))(M\_{\text{Euc}})\_{i,j}=\mathbb{I}\left(|W\_{i,j}|\leq\tau\_{\text{Euc}}(\rho)\right) |  | (7) |

Here, τEuc​(ρ)\tau\_{\text{Euc}}(\rho) represents the ρ\rho-th quantile of |W||W|. The final geometry-constrained matrix WGeoW\_{\text{Geo}} is formed by the union of these two stable subspaces:

|  |  |  |  |
| --- | --- | --- | --- |
|  | WGeo=W⊙(MSpec∪MEuc)W\_{\text{Geo}}=W\odot(M\_{\text{Spec}}\cup M\_{\text{Euc}}) |  | (8) |

This union ensures that the optimized weights retain the flexibility of small parameters while respecting the spectral constraints of the pre-trained model.

|  | In-Distribution (ID) | | | | | Out-of-Distribution (OOD) | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Method | AIME24 | AIME25 | MATH500 | OlymMATH | Avg. | HumanEval | GPQA | MMLU |
| Qwen3-8B | | | | | | | | |
| FullFT | 23.33 | 22.08 | 78.40 | 11.25 | 33.77 | 76.83 | 36.91 | 71.94 |
| SparseFT | 22.92 | 21.25 | 76.80 | 11.50 | 33.12 | 79.50 | 37.20 | 74.20 |
| LoRA | 19.58 | 19.58 | 75.60 | 10.75 | 31.38 | 81.10 | 37.50 | 75.65 |
| PiSSA | 22.50 | 20.42 | 74.40 | 11.75 | 32.27 | 71.95 | 36.16 | 73.89 |
| MiLoRA | 20.42 | 19.58 | 76.20 | 11.50 | 31.93 | 78.66 | 38.26 | 74.51 |
| GeoRA | 23.75 | 21.67 | 78.00 | 12.75 | 34.04 | 82.93 | 37.92 | 75.96 |
| Llama-3.1-8B | | | | | | | | |
| FullFT | 18.33 | 8.25 | 62.40 | 8.50 | 24.37 | 65.20 | 31.15 | 68.40 |
| SparseFT | 17.92 | 8.10 | 61.50 | 8.25 | 23.94 | 67.80 | 31.65 | 69.10 |
| LoRA | 15.42 | 6.25 | 58.20 | 6.75 | 21.66 | 69.80 | 32.10 | 69.80 |
| PiSSA | 17.50 | 7.92 | 60.50 | 7.75 | 23.42 | 67.50 | 31.80 | 69.20 |
| MiLoRA | 16.25 | 7.08 | 59.10 | 7.25 | 22.42 | 68.20 | 32.00 | 70.50 |
| GeoRA | 18.54 | 8.75 | 61.90 | 8.85 | 24.51 | 70.80 | 32.65 | 70.95 |

## B-b779fad195f88d

https://arxiv.org/html/2601.09361v2#chars-209-263

# GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR

## B-b9d14ce96bbe96

https://arxiv.org/html/2601.09361v2#chars-16069-21055

### 4.1 Main Results and Efficiency

| Method | Params (B) | Time (s/it) | VRAM (%) |
| --- | --- | --- | --- |
| Full FT | 8.00 | 231 | 95.73 |
| SparseFT | |  | | --- | | 2.56 | | (-68.0%) | | |  | | --- | | 256 | | (+10.8%) | | |  | | --- | | 81.25 | | (-15.1%) | |
| GeoRA | |  | | --- | | 0.04 | | (-99.5%) | | |  | | --- | | 185 | | (-19.9%) | | |  | | --- | | 68.43 | | (-28.5%) | |

|  |
| --- |
| 2.56 |
| (-68.0%) |

|  |
| --- |
| 256 |
| (+10.8%) |

|  |
| --- |
| 81.25 |
| (-15.1%) |

|  |
| --- |
| 0.04 |
| (-99.5%) |

|  |
| --- |
| 185 |
| (-19.9%) |

|  |
| --- |
| 68.43 |
| (-28.5%) |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Method | Reward | AIME24 | AIME25 | MATH-500 | OlymMATH | Avg. |
| GeoRA | 0.88 | 13.33 | 9.17 | 73.40 | 5.75 | 25.41 |
| Ablation on Initialization Strategy | | | | | | |
| Random-rr Init | 0.85 | 12.50 | 8.50 | 72.10 | 5.25 | 24.60 |
| Tail-rr Init | 0.82 | 11.67 | 7.50 | 70.80 | 4.50 | 23.40 |
| Ablation on Geometric Masks | | | | | | |
| w/o MSpecM\_{\text{Spec}} | 0.86 | 12.50 | 8.33 | 72.00 | 4.75 | 24.40 |
| w/o MEucM\_{\text{Euc}} | 0.83 | 13.33 | 8.75 | 72.80 | 5.50 | 25.10 |

We conduct a comprehensive performance comparison of GeoRA against MiLoRA [Wang et al. (2025)](#bib.bib38), PiSSA [Meng et al. (2024)](#bib.bib34), LoRA [Hu et al. (2022)](#bib.bib41), Sparse Fine-Tuning (SparseFT, based on  [2](#S1.F2 "Figure 2 ‣ 1 Introduction ‣ GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR")MGeoM\_{\text{Geo}} masking), and Full Fine-Tuning (FullFT). In our experiments, we fine-tune Qwen3-8B-Base [Yang et al. (2025)](#bib.bib13) and Llama-3.1-8B-Instruct [Dubey et al. (2024)](#bib.bib22) on the DeepMath-103K dataset [He et al. (2025)](#bib.bib8) using the GRPO algorithm [Shao et al. (2024)](#bib.bib14), with a fixed rank r=16r=16 and sparsity ratio ρ=0.2\rho=0.2. We use both base and instruction-tuned backbones to reflect robustness across model variants. We evaluate their In-Distribution (ID) problem-solving capabilities on MATH-500 [Hendrycks et al. (2021)](#bib.bib9), AIME [Patel et al. (2024)](#bib.bib24), and OlymMATH [Sun et al. (2025)](#bib.bib12). Furthermore, to assess the preservation of general capabilities and cross-domain generalization, we conduct evaluations on Out-of-Distribution (OOD) benchmarks, including HumanEval (Coding) [Chen (2021)](#bib.bib23), GPQA (Science) [Rein et al. (2024)](#bib.bib11), and MMLU (General Knowledge) [Hendrycks et al. (2020)](#bib.bib10).

Mathematical Reasoning Performance.  Table [1](#S3.T1 "Table 1 ‣ 3.2 Geometric Prior Construction ‣ 3 Methodology ‣ GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR") shows that GeoRA achieves the highest average scores on both Qwen3-8B and Llama-3.1 (34.04 and 24.51, respectively). GeoRA establishes a new state-of-the-art (SOTA) among PEFT methods and further surpasses Full Fine-Tuning (FullFT) and Sparse Fine-Tuning (SparseFT). Notably, on challenging competition-level benchmarks such as AIME and OlymMATH, GeoRA demonstrates superior performance, significantly outperforming LoRA, MiLoRA, and PiSSA. This suggests that the geometric initialization strategy navigates the optimization landscape more effectively than random or magnitude-based initializations, enabling superior convergence even with minimal parameter updates.

Generalization and Forgetting Resistance. GeoRA exhibits remarkable robustness against "catastrophic forgetting" (Table [1](#S3.T1 "Table 1 ‣ 3.2 Geometric Prior Construction ‣ 3 Methodology ‣ GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR"), right). In contrast to FullFT, which causes a substantial degradation in Qwen3’s coding capabilities (dropping to 76.83), GeoRA maintains a high score of 82.93 on HumanEval and achieves the best results on both MMLU and GPQA. This demonstrates that by selectively updating only the "safe" geometric subspaces, GeoRA enhances mathematical reasoning without disrupting pre-existing general knowledge structures.

Training Dynamics and Efficiency.
Figure [3](#S4.F3 "Figure 3 ‣ 4.1 Main Results and Efficiency ‣ 4 Experiments ‣ GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR") reveals that GeoRA converges faster and more stably, identifying a strictly dominant trajectory where it reaches performance levels at step 300 that other PEFT methods struggle to attain even at step 600.
Regarding efficiency (Table [2](#S4.T2 "Table 2 ‣ 4.1 Main Results and Efficiency ‣ 4 Experiments ‣ GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR")), GeoRA reduces trainable parameters by 99.5% and VRAM usage by 28.5% compared to FullFT, while improving training speed by 19.9%.
Crucially, this speedup empirically validates our design choice: by strictly preserving dense matrix compatibility, GeoRA successfully bypasses the hardware overhead associated with unstructured sparsity (e.g., dynamic masking) present in SparseFT, translating theoretical hardware-friendliness into tangible computational acceleration.

## B-bc65e841dcf398

https://arxiv.org/html/2601.09361v2#chars-5847-5866

## 2 Related Work

## B-e545d053f9f698

https://arxiv.org/html/2601.09361v2#chars-10581-13029

### 3.1 Geometry-Aware Low-Rank Structure

Let WGeoW\_{\text{Geo}} denote a geometry-constrained view of the pre-trained weight matrix WW. Unlike standard LoRA which initializes adapters randomly (or with zero), GeoRA leverages the compressible structure within WGeoW\_{\text{Geo}} to derive a structured initialization.

We first perform Singular Value Decomposition (SVD) on the geometry-constrained matrix:

|  |  |  |  |
| --- | --- | --- | --- |
|  | WGeo=UGeo​ΣGeo​VGeo⊤W\_{\text{Geo}}=U\_{\text{Geo}}\Sigma\_{\text{Geo}}V\_{\text{Geo}}^{\top} |  | (1) |

We extract the top-rr singular components that capture the principal geometric information. The low-rank adapters AGeoA\_{\text{Geo}} and BGeoB\_{\text{Geo}} are then initialized to approximate this geometry-aware subspace:

|  |  |  |  |
| --- | --- | --- | --- |
|  | AGeo=ΣGeo[:r,:r]1/2VGeo[:,:r]⊤A\_{\text{Geo}}=\Sigma\_{\text{Geo}[:r,:r]}^{1/2}V\_{\text{Geo}[:,:r]}^{\top} |  | (2) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | BGeo=UGeo[:,:r]ΣGeo[:r,:r]1/2B\_{\text{Geo}}=U\_{\text{Geo}[:,:r]}\Sigma\_{\text{Geo}[:r,:r]}^{1/2} |  | (3) |

By this design, the initial product BGeo​AGeoB\_{\text{Geo}}A\_{\text{Geo}} constructs the rank-rr approximation of WGeoW\_{\text{Geo}}.

Crucially, to ensure the model’s output remains unchanged at initialization and to preserve core capabilities during training, we follow the standard LoRA scaling and compute a Residual Matrix WresW\_{\text{res}} by subtracting the scaled initialized adapters from the original weights:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wres=W−αr​BGeo​AGeoW\_{\text{res}}=W-\frac{\alpha}{r}B\_{\text{Geo}}A\_{\text{Geo}} |  | (4) |

During the forward pass, WresW\_{\text{res}} is kept frozen. The hidden state hh is computed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h=Wres⏟Frozen​x+αr​BGeo​AGeo⏟Trainable​xh=\underbrace{W\_{\text{res}}}\_{\text{Frozen}}x+\underbrace{\frac{\alpha}{r}B\_{\text{Geo}}A\_{\text{Geo}}}\_{\text{Trainable}}x |  | (5) |

This construction keeps the model function-preserving at initialization (since Wres​x+αr​BGeo​AGeo​x=W​xW\_{\text{res}}x+\frac{\alpha}{r}B\_{\text{Geo}}A\_{\text{Geo}}x=Wx) and enforces a hard structural constraint: the optimizer can only update the geometry-aligned manifold parameterized by AGeoA\_{\text{Geo}} and BGeoB\_{\text{Geo}}, while WresW\_{\text{res}} acts as a stability anchor preventing the erosion of pre-trained representations.

## B-f118d3d8e4976e

https://arxiv.org/html/2601.09361v2#chars-29897-30843

## 6 Conclusion

In this paper, we bridge the gap between PEFT and the unique optimization dynamics of RLVR. Our investigation suggests that the instability often observed in RL fine-tuning arises from a structural mismatch: SFT-centric methods (e.g., PiSSA) prioritize principal components that may misalign with the geometry-constrained updates required by RLVR. GeoRA addresses this by identifying a compressible, geometry-aligned update subspace and parameterizing it via structured SVD initialization with a residual leash. Extensive evaluations confirm that GeoRA offers a robust solution for deploying large reasoning models, demonstrating exceptional stability under aggressive training conditions and superior generalization on out-of-distribution tasks. By reconciling the plasticity required for policy improvement with the structural integrity of the foundation model, GeoRA establishes a new standard for efficient and stable RLVR.

## B-f714732b7a63c6

https://arxiv.org/html/2601.09361v2#chars-263-1817

###### Abstract

Reinforcement Learning with Verifiable Rewards (RLVR) is crucial for advancing large-scale reasoning models. However, existing parameter-efficient methods, such as PiSSA and MiLoRA, are designed for Supervised Fine-Tuning (SFT) and do not account for the distinct optimization dynamics and geometric structures of RLVR. Applying these methods directly leads to spectral collapse and optimization instability, which severely limit model performance. Meanwhile, alternative approaches that leverage update sparsity encounter significant efficiency bottlenecks on modern hardware due to unstructured computations. To address these challenges, we propose GeoRA (Geometry-Aware Low-Rank Adaptation), which exploits the anisotropic and compressible nature of RL update subspaces. GeoRA initializes adapters by extracting principal directions via Singular Value Decomposition (SVD) within a geometrically constrained subspace while freezing the residual components. This method preserves the pre-trained geometric structure and enables efficient GPU computation through dense operators. Experiments on Qwen and Llama demonstrate that GeoRA mitigates optimization bottlenecks caused by geometric misalignment. It consistently outperforms established low-rank baselines on key mathematical benchmarks, achieving state-of-the-art (SOTA) results. Moreover, GeoRA shows superior generalization and resilience to catastrophic forgetting in out-of-domain tasks.

† Work done during internship at Meituan
‡ Corresponding authors
\* Equal contribution

## B-ocr-2aa3fc6eb29712

B PDF page 15

CQA, and PubMedQA.

Coding RLVR. For coding experiments, we train Qwen3-32B on Eurus-2-RL-Data. The maximum prompt length is set to 1024 tokens and the maximum response length is set to 2048 tokens. We train on 2 nodes with 8 GPUs per node. For reward computation, we extract the generated code from the model output and execute it against the provided test cases in a restricted execution environment. A sample is regarded as correct only when the generated program passes the corresponding test cases within the timeout limit. During evaluation, we follow the official benchmark protocol whenever available, including the same execution environment and decoding configuration across methods. We report results on LiveCodeBench, HumanEval, and MBPP.

ing performance and out-of-distribution generalization under the same evaluation protocol.

## D Robustness Analysis

We evaluate the sensitivity of GeoRA's performance to variations in key hyperparameters on the Qwen3-4B model (Figure 7). (a) Reward trajectories under varying rank \( r \in \{4, 8, 16, 32\} \) (with fixed sparsity \( \rho = 20\% \)). (b) Reward trajectories under varying sparsity levels \( \rho \in \{10\%, 20\%, 30\%, 40\%\} \) (with fixed rank \( r = 16 \)). In both scenarios, GeoRA demonstrates exceptional robustness, maintaining stable convergence and consistent high reward across a wide range of parameter settings, even at extremely low ranks or high sparsity levels.

![img-9.jpeg](img-9.jpeg)

(a) Sensitivity to Rank Variations

![img-10.jpeg](img-10.jpeg)

(b) Sensitivity to Sparsity Variations

Figure 7: Parameter Robustness Analysis.

### C.3 Extended Experiments

We further evaluate GeoRA on additional backbones with different parameter scales (Qwen2.5-1.5B and Qwen3-4B) to assess scalability and generality. Table 8 reports both in-distribution reason-

## B-ocr-4cd920a29039c1

B PDF page 1

arXiv:2601.09361v4 [cs.LG] 31 Jul 2026

# GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR

Jiaying Zhang \( ^{1,2\dagger*} \) , Lei Shi \( ^{1*\dagger} \) , Jiguo Li \( ^{1} \) , Jun Xu \( ^{1\ddagger} \) , Jiuchong Gao \( ^{1\ddagger} \) , Jinghua Hao \( ^{1} \) , Renqing He \( ^{1} \)

\( ^{1} \) Meituan,  \( ^{2} \) Peking University

zhangjy2002@stu.pku.edu.cn

{shilei74, xujun58, gaojiuchong}@meituan.com

## Abstract

Reinforcement Learning with Verifiable Rewards (RLVR) is a key paradigm for improving large-scale reasoning models. Unlike supervised fine-tuning (SFT), RLVR exhibits distinct optimization dynamics and is sensitive to the preservation of pre-trained geometric structures. However, existing parameter-efficient methods face key limitations in this regime. Low-rank adaptation methods, such as PiSSA, are primarily designed for Supervised Fine-Tuning (SFT) and do not account for the distinct optimization dynamics and geometric structures of RLVR. Conversely, directly fine-tuning the unstructured sparse parameter subspace favored by RLVR encounters efficiency bottlenecks on modern hardware. To address these challenges, we propose GeoRA (Geometry-Aware Low-Rank Adaptation), a low-rank adaptation method tailored for RLVR. Specifically, GeoRA exploits the anisotropic and compressible structure of RL update subspace, and extracts its principal directions via Singular Value Decomposition (SVD) to initialize low-rank adapters, while freezing residual components as a structural anchor during training. This design preserves the pre-trained structure and enables efficient dense computation. Experiments on Qwen and Llama models from 1.5B to 32B parameters show that GeoRA consistently outperforms strong low-rank baselines across RLVR settings in mathematics, medicine, and coding, while showing stronger generalization and less forgetting on out-of-domain tasks.

## 1 Introduction

Large reasoning models, represented by OpenAI-o1 (OpenAI et al., 2024) and DeepSeek-R1 (DeepSeek-AI et al., 2025), have established Reinforcement Learning with Verifiable Rewards

(RLVR) as a pivotal paradigm for unlocking complex reasoning capabilities. Unlike supervised fine-tuning (SFT), RLVR is better characterized as a constrained optimization process (Wu et al., 2025) that amplifies latent reasoning behaviors through reward-induced sampling bias (Yue et al., 2025; Zhao et al., 2025). As a result, RLVR is particularly sensitive to update stability and its alignment with pre-trained representation geometry: overly aggressive updates can collapse behavior or degrade general capabilities. Empirically, substantial gains can emerge from modifying only a small fraction of parameters (Mukherjee et al., 2025), and recent mechanistic studies further suggest that effective RLVR updates are geometrically biased toward preserving pre-trained structure (Zhu et al., 2025; Cai et al., 2025).

However, existing PEFT methods face key limitations in this regime. First, SFT-oriented low-rank adaptation methods suffer from a geometric mismatch with RLVR (Yin et al., 2025). PiSSA (Meng et al., 2025), for example, forces updates onto principal components, conflicting with RLVR's preferred subspace while protecting core features. Second, some sparse fine-tuning methods (Mukherjee et al., 2025; Zhu et al., 2025), although more consistent with RLVR update patterns, struggle to achieve practical efficiency. Because modern hardware provides limited support for unstructured sparsity, these methods often fail to translate theoretical sparsity into real-world speedups, and may even introduce additional overhead.

To address these challenges, we introduce GeoRA (Geometry-Aware Low-Rank Adaptation), a low-rank adaptation framework tailored to RLVR. Our analysis shows that the effective RLVR update subspace is anisotropic and compressible rather than isotropic, exhibiting a structured low-rank form. Based on this observation, GeoRA extracts dominant trainable directions from a geometry-constrained subspace for initialization, while keep-

## B-ocr-5cc69aac3b1f06

B PDF page 12

Kaiyan Zhang, Yuxin Zuo, Bingxiang He, Youbang Sun, Runze Liu, Che Jiang, Yuchen Fan, Kai Tian, Guoli Jia, Pengfei Li, Yu Fu, Xingtai Lv, Yuchen Zhang, Sihang Zeng, Shang Qu, Haozhan Li, Shijie Wang, Yuru Wang, Xinwei Long, and 20 others. 2025. A survey of reinforcement learning for large reasoning models. Preprint, arXiv:2509.08827.

Qingru Zhang, Minshuo Chen, Alexander Bukharin, Nikos Karampatziakis, Pengcheng He, Yu Cheng, Weizhu Chen, and Tuo Zhao. 2023. Adalora: Adaptive budget allocation for parameter-efficient fine-tuning. Preprint, arXiv:2303.10512.

Rosie Zhao, Alexandru Meterez, Sham Kakade, Cengiz Pehlevan, Samy Jelassi, and Eran Malach. 2025. Echo chamber: Rl post-training amplifies behaviors learned in pretraining. Preprint, arXiv:2504.07912.

Jeffrey Zhou, Tianlu Lu, Swaroop Mishra, Siddhartha Brahma, Sujoy Basu, Yi Luan, Denny Zhou, and Le Hou. 2023. Instruction-following evaluation for large language models. Preprint, arXiv:2311.07911.

Hanqing Zhu, Zhenyu Zhang, Hanxian Huang, DiJia Su, Zechun Liu, Jiawei Zhao, Igor Fedorov, Hamed Pirsiavash, Zhizhou Sha, Jinwon Lee, David Z. Pan, Zhangyang Wang, Yuandong Tian, and Kai Sheng Tai. 2025. The path not taken: Rlvr provably learns off the principals. Preprint, arXiv:2511.08567.

## B-ocr-6084e9d46bdebd

B PDF page 11

Hao, and Bing Han. 2023. Hierarchical prompt tuning for few-shot multi-task learning. In Proceedings of the 32nd ACM International Conference on Information and Knowledge Management, pages 1556–1565.

Mingjie Liu, Shizhe Diao, Ximing Lu, Jian Hu, Xin Dong, Yejin Choi, Jan Kautz, and Yi Dong. 2025b. Prorl: Prolonged reinforcement learning expands reasoning boundaries in large language models. Preprint, arXiv:2505.24864.

Shih-Yang Liu, Chien-Yi Wang, Hongxu Yin, Pavlo Molchanov, Yu-Chiang Frank Wang, Kwang-Ting Cheng, and Min-Hung Chen. 2024. Dora: Weight-decomposed low-rank adaptation. Preprint, arXiv:2402.09353.

Zihang Liu, Tianyu Pang, Oleg Balabanov, Chaoqun Yang, Tianjin Huang, Lu Yin, Yaoqing Yang, and Shiwei Liu. 2025c. Lift the veil for the truth: Principal weights emerge after rank reduction for reasoning-focused supervised fine-tuning. Preprint, arXiv:2506.00772.

Fanxu Meng, Zhaohui Wang, and Muhan Zhang. 2025. Pissa: Principal singular values and singular vectors adaptation of large language models. Preprint, arXiv:2404.02948.

Sagnik Mukherjee, Lifan Yuan, Dilek Hakkani-Tur, and Hao Peng. 2025. Reinforcement learning fine-tunes small subnetworks in large language models. Preprint, arXiv:2505.11711.

Phuc Minh Nguyen, Chinh D. La, Duy M. H. Nguyen, Nitesh V. Chawla, Binh T. Nguyen, and Khoa D. Doan. 2025. The reasoning boundary paradox: How reinforcement learning constrains language models. Preprint, arXiv:2510.02230.

OpenAI, :, Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, Alex Iftimie, Alex Karpenko, Alex Tachard Passos, Alexander Neitz, Alexander Prokofiev, Alexander Wei, Allison Tam, and 244 others. 2024. Openai o1 system card. Preprint, arXiv:2412.16720.

Ankit Pal, Logesh Kumar Umapathi, and Malaikannan Sankarasubbu. 2022. Medmcqa: A large-scale multi-subject multi-choice dataset for medical domain question answering. In Proceedings of the Conference on Health, Inference, and Learning, pages 248–260.

Bhrij Patel, Souradip Chakraborty, Wesley A. Suttle, Mengdi Wang, Amrit Singh Bedi, and Dinesh Manocha. 2024. Aime: Ai system optimization via multiple llm evaluators. Preprint, arXiv:2410.03131.

David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R. Bowman. 2023. Gpqa: A graduate-level google-proof q&a benchmark. Preprint, arXiv:2311.12022.

Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y. K. Li, Y. Wu, and Daya Guo. 2024. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. Preprint, arXiv:2402.03300.

Idan Shenfeld, Jyothish Pari, and Pulkit Agrawal. 2025. Rl's razor: Why online reinforcement learning forgets less. Preprint, arXiv:2509.04259.

Haoxiang Sun, Yingqian Min, Zhipeng Chen, Wayne Xin Zhao, Lei Fang, Zheng Liu, Zhongyuan Wang, and Ji-Rong Wen. 2025. Challenging the boundaries of reasoning: An olympiad-level math benchmark for large language models. Preprint, arXiv:2503.21380.

Hanqing Wang, Yixia Li, Shuo Wang, Guanhua Chen, and Yun Chen. 2025. Milora: Harnessing minor singular components for parameter-efficient llm fine-tuning. Preprint, arXiv:2406.09044.

Fang Wu, Weihao Xuan, Ximing Lu, Mingjie Liu, Yi Dong, Zaid Harchaoui, and Yejin Choi. 2025. The invisible leash: Why rlvr may or may not escape its origin. Preprint, arXiv:2507.14843.

Lingling Xu, Haoran Xie, Si-Zhao Joe Qin, Xiaohui Tao, and Fu Lee Wang. 2023. Parameter-efficient fine-tuning methods for pretrained language models: A critical review and assessment. Preprint, arXiv:2312.12148.

An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, Chujie Zheng, Dayiheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao Ge, Haoran Wei, Huan Lin, Jialong Tang, and 41 others. 2025. Qwen3 technical report. Preprint, arXiv:2505.09388.

Qingyu Yin, Yulun Wu, Zhennan Shen, Sunbowen Li, Zhilin Wang, Yanshu Li, Chak Tou Leong, Jiale Kang, and Jinjin Gu. 2025. Evaluating parameter efficient methods for rlvr. Preprint, arXiv:2512.23165.

Lifan Yuan, Weize Chen, Yuchen Zhang, Ganqu Cui, Hanbin Wang, Ziming You, Ning Ding, Zhiyuan Liu, Maosong Sun, and Hao Peng. 2025. From \( f(x) \) and \( g(x) \) to \( f(g(x)) \): Llms learn new skills in rl by composing old ones. Preprint, arXiv:2509.25123.

Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, and Gao Huang. 2025. Does reinforcement learning really incentivize reasoning capacity in llms beyond the base model? Preprint, arXiv:2504.13837.

Elad Ben Zaken, Shauli Ravfogel, and Yoav Goldberg. 2022. Bitfit: Simple parameter-efficient fine-tuning for transformer-based masked language-models. Preprint, arXiv:2106.10199.

## B-ocr-7942b8ec07dad8

B PDF page 7

![img-5.jpeg](img-5.jpeg)

(a) Reward Trajectories

![img-6.jpeg](img-6.jpeg)

(b) KL Divergence

Figure 5: Training Stability and Constraint Adherence. Results on Qwen3-4B show that GeoRA demonstrates superior robustness under aggressive learning rates  \( (5 \times 10^{-5}) \) .

[tbl-3.html](tbl-3.html)

Table 4: Ablation study on Qwen3-4B with different initialization strategies and geometric mask variants.

cates that the benefit of GeoRA does not come from low-rank adaptation alone, but from aligning the initialization with the effective RLVR update subspace. In particular, the poor performance of Tail-r suggests that simply selecting low-energy directions is insufficient; the trainable directions must still capture the dominant structure within the geometry-constrained subspace.

Impact of Geometric Masks. We further ablate the two mask components used to construct the geometry-constrained subspace. Removing either  \( M_{Spec} \)  or  \( M_{Euc} \)  consistently degrades performance, confirming that both are necessary for strong results. This suggests that the two priors play complementary roles: the spectral mask helps suppress unstable high-energy directions, while the Euclidean mask preserves adaptation flexibility in low-magnitude regions. Their combination therefore provides a better approximation to the effective RLVR update manifold than either component alone.

Overall Analysis. Taken together, the ablation results show that GeoRA's gains arise from the full geometry-aware design rather than from any single isolated choice. The geometry-constrained

subspace, structured initialization, and frozen residual anchor work together to improve optimization quality while preserving pre-trained structure. This is consistent with the stability and efficiency results in the previous section, and further supports our claim that RLVR benefits from a low-rank parameterization explicitly aligned with its update geometry.

## 5 Mechanism Analysis

### 5.1 Geometric Priors

GeoRA constructs its update subspace from two geometric priors: a spectral prior and a Euclidean prior. The motivation is that RLVR updates are highly selective, tending to exploit under-utilized yet plastic regions of the pre-trained model while avoiding large modifications to dominant principal directions. Accordingly,  \( M_{Spec} \)  suppresses high-energy components in the principal subspace, whereas  \( M_{Euc} \)  selects low-magnitude parameters in the original weight space. Their union defines a subspace that is both stable and expressive for RLVR adaptation.

We further verify that these two priors are complementary rather than redundant in Table 5. On

[OCR table id=tbl-3.html; page=7]
<table><tr><td>Method</td><td>Reward</td><td>AIME24</td><td>AIME25</td><td>MATH-500</td><td>OlymMATH</td><td>Average</td></tr><tr><td>GeoRA</td><td>0.88</td><td>13.33</td><td>9.17</td><td>73.40</td><td>5.75</td><td>25.41</td></tr><tr><td colspan="7">Ablation on Initialization Strategy</td></tr><tr><td>Random-r Init</td><td>0.85</td><td>12.50</td><td>8.50</td><td>72.10</td><td>5.25</td><td>24.60</td></tr><tr><td>Tail-r Init</td><td>0.82</td><td>11.67</td><td>7.50</td><td>70.80</td><td>4.50</td><td>23.40</td></tr><tr><td colspan="7">Ablation on Geometric Masks</td></tr><tr><td>w/o \( M_{\text{Spec}} \)</td><td>0.86</td><td>12.50</td><td>8.33</td><td>72.00</td><td>4.75</td><td>24.40</td></tr><tr><td>w/o \( M_{\text{Euc}} \)</td><td>0.83</td><td>13.33</td><td>8.75</td><td>72.80</td><td>5.50</td><td>25.10</td></tr></table>

## B-ocr-85b85061a9946e

B PDF page 3

(1) Initialization

![img-0.jpeg](img-0.jpeg)

(2) Finetuning

![img-1.jpeg](img-1.jpeg)

Figure 1: Comparison of adapter initialization and forward architectures. LoRA applies low-rank adaptation on the original weight matrix W with standard initialization, while PiSSA initializes adapters from the principal components of W. In contrast, GeoRA initializes from a geometry-constrained matrix  \( W_{Geo} \)  (a different adaptation target than W). Its forward pass incorporates a frozen Residual Matrix in parallel with the trainable adapter to act as a stability anchor for principal components.

![img-2.jpeg](img-2.jpeg)

Figure 2: Geometric Prior Construction via Masking. The process of generating  \( M_{Geo} \)  by combining Spectral Priors (low-curvature regions) and Euclidean Priors (high-plasticity near-zero weights). The resulting  \( W_{Geo} \)  isolates the most stable parameters for RL-native adaptation.

but does not explicitly account for RLVR-specific geometry and dynamics. Other variants like DoRA (Liu et al., 2024), AdaLoRA (Zhang et al., 2023), and VeRA (Kopiczko et al., 2024) focus on weight decomposition or budget allocation without integrating these RLVR-native geometric considerations. Building on these observations, GeoRA translates RLVR-specific mechanistic insights into an actionable PEFT paradigm.

## 3 Methodology

We introduce GeoRA (Geometry-Aware Low-Rank Adaptation), a low-rank adaptation framework tailored for RLVR. GeoRA emphasizes an RL-native, structured low-rank parameterization together with an explicit residual leash for stability. Comparing with classical PEFT baselines like LoRA and PiSSA, we first present the low-rank forward architecture and initialization (Figure 1), and

then describe a lightweight masking instantiation that constructs the geometry-constrained matrix used for initialization (Figure 2).

### 3.1 Geometry-Aware Low-Rank Structure

Let \( W_{\mathrm{Geo}} \) denote a geometry-constrained view of the pre-trained weight matrix \( W \). Unlike standard LoRA which initializes adapters randomly (or with zero), GeoRA leverages the compressible structure within \( W_{\mathrm{Geo}} \) to derive a structured initialization.

We first perform Singular Value Decomposition (SVD) on the geometry-constrained matrix:

\[
W _ {\mathrm{Geo}} = U _ {\mathrm{Geo}} \Sigma_ {\mathrm{Geo}} V _ {\mathrm{Geo}} ^ {\top} \tag {1}
\]

We extract the top-r singular components that capture the principal geometric information. The low-rank adapters  \( A_{Geo} \)  and  \( B_{Geo} \)  are then initialized to approximate this geometry-aware subspace:

## B-ocr-98ab1bc5e13872

B PDF page 5

Table 1: Main results on in-distribution (ID) mathematical RLVR benchmarks and out-of-distribution (OOD) tasks. Base denotes the original model before RLVR. Best results are in bold, and second-best results are underlined.

[tbl-0.html](tbl-0.html)

Table 2: Results on additional medical and coding RLVR tasks. Best results are in bold, and second-best results are underlined.

[tbl-1.html](tbl-1.html)

on MedQA (Jin et al., 2021), MedMCQA (Pal et al., 2022), and PubMedQA (Jin et al., 2019). For coding, we train Qwen3-32B on Eurus-2-RL-Data (Cui et al., 2025) and evaluate on LiveCodeBench (Jain et al., 2025), HumanEval, and MBPP (Austin et al., 2021). The implementation details and hyperparameter settings are provided in the Appendix C.

### 4.2 Main Results

Mathematical Reasoning Performance. Table 1 shows that GeoRA achieves the strongest overall performance on mathematical RLVR benchmarks across both backbones. It obtains the best results on most AIME and OlymMATH settings, while remaining competitive on MATH500. In particular, GeoRA consistently outperforms LoRA, MiLoRA, and PiSSA on challenging competition-style benchmarks, suggesting that geometry-aware initialization provides a more suitable inductive bias for RLVR than classic low-rank initialization.

Out-of-Distribution Performance. GeoRA

also generalizes favorably to OOD tasks. Across both backbones, it achieves the strongest or near-strongest results on HumanEval, GPQA, and MMLU, while generally retaining higher capability than other fine-tuning baselines on IFEval and TruthfulQA. These results indicate that constraining updates to geometry-aligned subspaces can improve in-domain reasoning performance while reducing interference with pre-existing general capabilities.

Extension Beyond Mathematical RLVR. Beyond the main mathematical RLVR setting, we further evaluate GeoRA on medical and coding RLVR tasks. As shown in Table 2, GeoRA consistently outperforms LoRA across both domains and remains competitive with FullFT, suggesting that its advantage is not limited to mathematical reasoning.

### 4.3 Training Stability and Efficiency

Training Dynamics. Figure 3 shows the training dynamics of Qwen3-8B as evaluated on the AIME

[OCR table id=tbl-0.html; page=5]
<table><tr><td rowspan="2">Method</td><td colspan="4">In-Distribution (ID)</td><td colspan="5">Out-of-Distribution (OOD)</td></tr><tr><td>AIME24</td><td>AIME25</td><td>MATH500</td><td>OlymMATH</td><td>HumanEval</td><td>GPQA</td><td>MMLU</td><td>IFEval</td><td>TruthfulQA</td></tr><tr><td colspan="10">Qwen3-8B</td></tr><tr><td>Base</td><td>13.33</td><td>11.67</td><td>71.20</td><td>9.75</td><td>76.83</td><td>36.91</td><td>71.94</td><td>54.32</td><td>68.91</td></tr><tr><td>FullFT</td><td>23.33</td><td>22.08</td><td>78.40</td><td>11.25</td><td>76.83</td><td>36.91</td><td>71.94</td><td>50.45</td><td>65.65</td></tr><tr><td>SparseFT</td><td>22.92</td><td>21.25</td><td>76.80</td><td>11.50</td><td>79.50</td><td>37.20</td><td>74.20</td><td>50.95</td><td>66.05</td></tr><tr><td>LoRA</td><td>19.58</td><td>19.58</td><td>75.60</td><td>10.75</td><td>81.10</td><td>37.50</td><td>75.65</td><td>52.13</td><td>66.82</td></tr><tr><td>PiSSA</td><td>22.50</td><td>20.42</td><td>74.40</td><td>11.75</td><td>71.95</td><td>36.16</td><td>73.89</td><td>48.74</td><td>65.95</td></tr><tr><td>MiLoRA</td><td>20.42</td><td>19.58</td><td>76.20</td><td>11.50</td><td>78.66</td><td>38.26</td><td>74.51</td><td>51.85</td><td>66.46</td></tr><tr><td>GeoRA</td><td>23.75</td><td>21.67</td><td>78.00</td><td>12.75</td><td>82.93</td><td>37.92</td><td>75.96</td><td>53.73</td><td>68.85</td></tr><tr><td colspan="10">Llama-3.1-8B</td></tr><tr><td>Base</td><td>9.58</td><td>2.08</td><td>51.00</td><td>3.25</td><td>65.20</td><td>31.15</td><td>68.40</td><td>79.99</td><td>62.71</td></tr><tr><td>FullFT</td><td>18.33</td><td>8.25</td><td>62.40</td><td>8.50</td><td>65.20</td><td>31.15</td><td>68.40</td><td>75.92</td><td>59.40</td></tr><tr><td>SparseFT</td><td>17.92</td><td>8.10</td><td>61.50</td><td>8.25</td><td>67.80</td><td>31.65</td><td>69.10</td><td>76.61</td><td>60.19</td></tr><tr><td>LoRA</td><td>15.42</td><td>6.25</td><td>58.20</td><td>6.75</td><td>69.80</td><td>32.10</td><td>69.80</td><td>77.93</td><td>61.76</td></tr><tr><td>PiSSA</td><td>17.50</td><td>7.92</td><td>60.50</td><td>7.75</td><td>67.50</td><td>31.80</td><td>69.20</td><td>74.83</td><td>59.83</td></tr><tr><td>MiLoRA</td><td>16.25</td><td>7.08</td><td>59.10</td><td>7.25</td><td>68.20</td><td>32.00</td><td>70.50</td><td>78.31</td><td>61.47</td></tr><tr><td>GeoRA</td><td>18.54</td><td>8.75</td><td>61.90</td><td>8.85</td><td>70.80</td><td>32.65</td><td>70.95</td><td>78.72</td><td>61.61</td></tr></table>

[OCR table id=tbl-1.html; page=5]
<table><tr><td rowspan="2">Method</td><td colspan="4">Medical</td><td colspan="4">Coding</td></tr><tr><td>MedQA</td><td>MedMCQA</td><td>PubMedQA</td><td>Average</td><td>LiveCodeBench</td><td>HumanEval</td><td>MBPP</td><td>Average</td></tr><tr><td>Base</td><td>58.03</td><td>56.42</td><td>74.94</td><td>63.13</td><td>65.75</td><td>87.66</td><td>79.40</td><td>77.60</td></tr><tr><td>FullFT</td><td>75.32</td><td>64.56</td><td>80.12</td><td>73.33</td><td>67.75</td><td>90.26</td><td>81.40</td><td>79.80</td></tr><tr><td>LoRA</td><td>74.23</td><td>62.12</td><td>79.54</td><td>71.96</td><td>67.25</td><td>88.96</td><td>81.00</td><td>79.07</td></tr><tr><td>GeoRA</td><td>76.12</td><td>64.31</td><td>80.64</td><td>73.69</td><td>67.75</td><td>89.61</td><td>81.60</td><td>79.65</td></tr></table>

## B-ocr-aec516482289a0

B PDF page 4

\[
A _ {\mathrm{Geo}} = \Sigma_ {\mathrm{Geo} [: r,: r ]} ^ {1 / 2} V _ {\mathrm{Geo} [:,: r ]} ^ {\top} \tag {2}
\]

\[
B _ {\mathrm{Geo}} = U _ {\mathrm{Geo} [:,: r ]} \Sigma_ {\mathrm{Geo} [: r,: r ]} ^ {1 / 2} \tag {3}
\]

By this design, the initial product  \( B_{Geo}A_{Geo} \)  constructs the rank-r approximation of  \( W_{Geo} \) .

Crucially, to ensure the model's output remains unchanged at initialization and to preserve core capabilities during training, we follow the standard LoRA scaling and compute a Residual Matrix \( W_{\mathrm{res}} \) by subtracting the scaled initialized adapters from the original weights:

\[
W _ {\mathrm{res}} = W - \frac {\alpha}{r} B _ {\mathrm{Geo}} A _ {\mathrm{Geo}} \tag {4}
\]

During the forward pass,  \( W_{res} \)  is kept frozen. The hidden state h is computed as:

\[
h = \underbrace {W _ {\text { res }}} _ {\text { Frozen }} x + \underbrace {\frac {\alpha}{r} B _ {\text { Geo }} A _ {\text { Geo }}} _ {\text { Trainable }} x \tag {5}
\]

This construction keeps the model function-preserving at initialization (since  \( W_{res}x + \frac{\alpha}{r}B_{Geo}A_{Geo}x = Wx \) ) and enforces a hard structural constraint: the optimizer can only update the geometry-aligned manifold parameterized by  \( A_{Geo} \)  and  \( B_{Geo} \) , while  \( W_{res} \)  acts as a stability anchor preventing the erosion of pre-trained representations.

### 3.2 Geometric Prior Construction

To instantiate a geometry-aware update region, we construct a geometry-constrained matrix  \( W_{Geo} \)  using a masking strategy. This masking is consistent with prior observations on spectral and magnitude structure and stability in fine-tuning (Liu et al., 2025c; Zhu et al., 2025).

The Spectral Prior  \( (M_{\mathrm{Spec}}) \)  promotes geometric stability by selecting the bottom  \( \rho \) -fraction of entries from the rank-r approximation  \( \hat{W}_{r} \) . The mask is defined as:

\[
(M _ {\text { Spec }}) _ {i, j} = \mathbb {I} \left(| (\hat {W} _ {r}) _ {i, j} | \leq \tau_ {\text { Spec }} (\rho)\right) \tag {6}
\]

where  \( \tau_{\mathrm{Spec}}(\rho) \)  is the  \( \rho \) -th quantile of the absolute values in  \( \hat{W}_{r} \) . Intuitively, this mask suppresses high-magnitude (and typically high-curvature) components and constrains updates to a more stable, low-magnitude region, improving spectral stability under RLVR. Similarly, the Euclidean Prior ( \( M_{Euc} \) ) selects low-magnitude weights to capture

parameter plasticity, using the same sparsity ratio  \( \rho \) :

\[
(M _ {\mathrm{Euc}}) _ {i, j} = \mathbb {I} \left(| W _ {i, j} | \leq \tau_ {\mathrm{Euc}} (\rho)\right) \tag {7}
\]

Here,  \( \tau_{\mathrm{Euc}}(\rho) \)  represents the  \( \rho \) -th quantile of  \( |W| \) . The final geometry-constrained matrix  \( W_{Geo} \)  is formed by the union of these two stable subspaces:

\[
W _ {\mathrm{Geo}} = W \odot (M _ {\mathrm{Spec}} \cup M _ {\mathrm{Euc}}) \tag {8}
\]

This union ensures that the optimized weights retain the flexibility of small parameters while respecting the spectral constraints of the pre-trained model.

## 4 Experiments

### 4.1 Experimental Setup

We compare GeoRA against MiLoRA (Wang et al., 2025), PiSSA (Meng et al., 2025), LoRA (Hu et al., 2021), Sparse Fine-Tuning (SparseFT) (Zhu et al., 2025), and Full Fine-Tuning (FullFT). Our main experiments are conducted on mathematical RLVR, where we fine-tune Qwen3-8B-Base (Yang et al., 2025) and Llama-3.1-8B-Instruct (Grattafiori et al., 2024) on the DeepMath-103K dataset (He et al., 2025) using the GRPO algorithm (Shao et al., 2024), with a fixed rank r = 16 and sparsity ratio  \( \rho = 0.2 \) . We include both base and instruction-tuned backbones to evaluate robustness across model variants. In addition, we further validate our method on mathematical RLVR tasks with the 4B and 1.5B models on the GSM8K (Cobbe et al., 2021) dataset; details are provided in the Appendix C.

For in-distribution (ID) evaluation, we assess mathematical reasoning performance on AIME24, AIME25 (Patel et al., 2024), MATH-500 (Hendrycks et al., 2021b), and Olym-MATH (Sun et al., 2025). For out-of-distribution (OOD) evaluation, we consider HumanEval (Coding) (Chen et al., 2021), GPQA (Science) (Rein et al., 2023), MMLU (General Knowledge) (Hendrycks et al., 2021a), IFEval (Instruction Following) (Zhou et al., 2023), and TruthfulQA (Truthfulness) (Lin et al., 2022) to measure cross-domain generalization and capability preservation. We also report the pre-RLVR Base model performance for direct comparison.

Beyond the main mathematical setting, we further evaluate GeoRA on additional RLVR domains, including medical reasoning and coding. For medical RLVR, we train Llama-3.1-8B-Instruct on AlphaMed19K (Liu et al., 2025a) and report results

## B-ocr-b3916fcb66ea1e

B PDF page 14

Table 8: Comprehensive performance comparison on Qwen2.5-1.5B and Qwen3-4B. We report In-Distribution (ID) mathematical reasoning scores and Out-of-Distribution (OOD) generalization scores.

[tbl-7.html](tbl-7.html)

across model scales. For reference, we also include the training cost of Qwen3-8B under our RLVR setting. In practice, randomized SVD reduces initialization time by roughly two orders of magnitude compared with standard SVD, making initialization a sub-minute operation even at 72B scale. Moreover, this memory cost is a one-off preprocessing overhead and can be released before training.

## C Implementation Details

### C.1 General Training Setup

We adopt GRPO as the default RLVR optimization algorithm for all experiments. To ensure fair comparison, we keep the training data, rollout configuration, and optimization budget identical across compared methods whenever applicable. Specifically, all PEFT methods use rank r = 16 and scaling factor  \( \alpha = 32 \) , with target_modules set to all-linear, i.e., adapters are applied to all linear layers. For GeoRA, we use sparsity ratio  \( \rho = 0.2 \)  unless otherwise specified. We train all models with AdamW in bfloat16 precision on 80GB GPUs. Unless otherwise specified, the learning rate is set to  \( 1 \times 10^{-6} \) , the global batch size is 128, and the rollout number is 8. When KL regularization is enabled, we use a shared reference policy and set the KL coefficient to 0.001. Unless otherwise specified, all methods are trained under the same decoding configuration and differ only in the adaptation parameterization based on a single random run.

### C.2 Task-Specific Details

Mathematical RLVR. For the main mathematical RLVR experiments, we fine-tune Qwen3-8B-Base and Llama-3.1-8B-Instruct on DeepMath-103K using GRPO. In addition, we evaluate smaller-scale settings on Qwen3-4B-Base and Qwen2.5-1.5B-Instruct using GSM8K to verify whether the gains of GeoRA persist across model scales. The maximum prompt length is set to 1024 tokens and the maximum response length is set to 4096 tokens. We train on 1 node with 8 GPUs. For DeepMath-103K, we use math-verify for answer verification by comparing the model output against the boxed ground-truth answer under expression- and LaTeX-based extraction rules. For GSM8K, we extract the final numerical answer from the model output and compare it against the ground-truth answer using exact match. Evaluation is conducted on AIME24, AIME25, MATH500, and OlymMATH.

Medical RLVR. For medical reasoning, we train Llama-3.1-8B-Instruct on AlphaMed. We use the AlphaMed training split for RL training and the corresponding test split for validation. The maximum prompt length is set to 1024 tokens and the maximum response length is set to 4096 tokens. We train on 1 node with 8 GPUs. For reward computation, we extract the final predicted option from the model output, primarily using the \boxed{X} format and several common variants, and compare it against the ground-truth choice. A binary reward is assigned, with 1.0 for a correct answer and 0.0 otherwise. We report results on MedQA, MedM-

[OCR table id=tbl-7.html; page=14]
<table><tr><td rowspan="2">Method</td><td colspan="4">In-Distribution (ID)</td><td colspan="3">Out-of-Distribution (OOD)</td></tr><tr><td>AIME24</td><td>AIME25</td><td>MATH500</td><td>OlymMATH</td><td>HumanEval</td><td>GPQA</td><td>MMLU</td></tr><tr><td colspan="8">Qwen2.5-1.5B</td></tr><tr><td>Full FT</td><td>7.92</td><td>1.25</td><td>53.00</td><td>4.00</td><td>45.73</td><td>25.10</td><td>55.40</td></tr><tr><td>SparseFT</td><td>8.33</td><td>1.67</td><td>53.60</td><td>4.50</td><td>51.83</td><td>27.50</td><td>59.80</td></tr><tr><td>LoRA</td><td>7.50</td><td>0.83</td><td>52.60</td><td>3.75</td><td>59.15</td><td>29.10</td><td>62.10</td></tr><tr><td>PiSSA</td><td>8.75</td><td>1.67</td><td>53.40</td><td>4.50</td><td>57.32</td><td>29.50</td><td>62.50</td></tr><tr><td>MiLoRA</td><td>9.58</td><td>2.08</td><td>54.80</td><td>5.25</td><td>58.54</td><td>29.80</td><td>62.80</td></tr><tr><td>GeoRA</td><td>10.83</td><td>2.50</td><td>54.60</td><td>5.50</td><td>58.54</td><td>30.23</td><td>62.40</td></tr><tr><td colspan="8">Qwen3-4B</td></tr><tr><td>Full FT</td><td>12.92</td><td>9.58</td><td>73.80</td><td>5.00</td><td>3.66</td><td>31.46</td><td>61.15</td></tr><tr><td>SparseFT</td><td>12.92</td><td>9.17</td><td>72.20</td><td>5.25</td><td>4.27</td><td>31.96</td><td>63.50</td></tr><tr><td>LoRA</td><td>10.83</td><td>8.33</td><td>71.20</td><td>4.75</td><td>3.05</td><td>31.04</td><td>62.80</td></tr><tr><td>PiSSA</td><td>12.50</td><td>8.75</td><td>70.00</td><td>5.25</td><td>4.88</td><td>32.47</td><td>64.95</td></tr><tr><td>MiLoRA</td><td>11.25</td><td>8.33</td><td>71.80</td><td>5.25</td><td>4.88</td><td>33.22</td><td>64.80</td></tr><tr><td>GeoRA</td><td>13.33</td><td>9.17</td><td>73.40</td><td>5.75</td><td>5.38</td><td>33.04</td><td>65.23</td></tr></table>

## B-ocr-c466b726369dd2

B PDF page 10

Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, Amy Yang, Angela Fan, Anirudh Goyal, Anthony Hartshorn, Aobo Yang, Archi Mitra, Archie Sravankumar, Artem Korenev, Arthur Hinsvark, and 542 others. 2024. The llama 3 herd of models. Preprint, arXiv:2407.21783.

Karen Hambardzumyan, Hrant Khachatrian, and Jonathan May. 2021. Warp: Word-level adversarial reprogramming. Preprint, arXiv:2101.00121.

Zeyu Han, Chao Gao, Jinyang Liu, Jeff Zhang, and Sai Qian Zhang. 2024. Parameter-efficient fine-tuning for large models: A comprehensive survey. Preprint, arXiv:2403.14608.

Zhiwei He, Tian Liang, Jiahao Xu, Qiuzhi Liu, Xingyu Chen, Yue Wang, Linfeng Song, Dian Yu, Zhenwen Liang, Wenxuan Wang, Zhuosheng Zhang, Rui Wang, Zhaopeng Tu, Haitao Mi, and Dong Yu. 2025. Deepmath-103k: A large-scale, challenging, decontaminated, and verifiable mathematical dataset for advancing reasoning. Preprint, arXiv:2504.11456.

Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. 2021a. Measuring massive multitask language understanding. Preprint, arXiv:2009.03300.

Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. 2021b. Measuring mathematical problem solving with the math dataset. Preprint, arXiv:2103.03874.

Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. 2021. Lora: Low-rank adaptation of large language models. Preprint, arXiv:2106.09685.

Jingcheng Hu, Yinmin Zhang, Qi Han, Daxin Jiang, Xiangyu Zhang, and Heung-Yeung Shum. 2025. Openreasoner-zero: An open source approach to scaling up reinforcement learning on the base model. Preprint, arXiv:2503.24290.

Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, and Ion Stoica. 2025. Live-codebench: Holistic and contamination free evaluation of large language models for code. In The Thirteenth International Conference on Learning Representations.

Di Jin, Eileen Pan, Nadav Oufattole, Wei-Hung Weng, Hanyi Fang, and Peter Szolovits. 2021. What disease does this patient have? a large-scale open domain question answering dataset from medical exams. Applied Sciences, 11(14):6421.

Hangzhan Jin, Sitao Luan, Sicheng Lyu, Guillaume Rabusseau, Reihaneh Rabbany, Doina Precup, and Mohammad Hamdaqa. 2025a. Rl fine-tuning heals ood forgetting in sft. Preprint, arXiv:2509.12235.

Hangzhan Jin, Sicheng Lv, Sifan Wu, and Mohammad Hamdaqa. 2025b. Rl is neither a panacea nor a mirage: Understanding supervised vs. reinforcement learning fine-tuning for llms. Preprint, arXiv:2508.16546.

Qiao Jin, Bhuwan Dhingra, Zhengping Liu, William Cohen, and Xinghua Lu. 2019. Pubmedqa: A dataset for biomedical research question answering. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 2567–2577.

Dawid J. Kopiczko, Tijmen Blankevoort, and Yuki M. Asano. 2024. Vera: Vector-based random matrix adaptation. Preprint, arXiv:2310.11454.

Nathan Lambert, Jacob Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze Brahman, Lester James V. Miranda, Alisa Liu, Nouha Dziri, Shane Lyu, Yuling Gu, Saumya Malik, Victoria Graf, Jena D. Hwang, Jiangjiang Yang, Ronan Le Bras, Oyvind Tafjord, Chris Wilhelm, Luca Soldaini, and 4 others. 2025. Tulu 3: Pushing frontiers in open language model post-training. Preprint, arXiv:2411.15124.

Neal Lawton, Anoop Kumar, Govind Thattai, Aram Galstyan, and Greg Ver Steeg. 2023. Neural architecture search for parameter-efficient fine-tuning of large pre-trained language models. Preprint, arXiv:2305.16597.

Chunyuan Li, Heerad Farkhoor, Rosanne Liu, and Jason Yosinski. 2018. Measuring the intrinsic dimension of objective landscapes. Preprint, arXiv:1804.08838.

Zujie Liang, Feng Wei, Yin Jie, Yuxi Qian, Zhenghong Hao, and Bing Han. 2023. Prompts can play lottery tickets well: Achieving lifelong information extraction via lottery prompt tuning. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 277–292.

Stephanie Lin, Jacob Hilton, and Owain Evans. 2022. Truthfulqa: Measuring how models mimic human falsehoods. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 3214–3252.

Zhaojiang Lin, Andrea Madotto, and Pascale Fung. 2020. Exploring versatile generative language model via parameter-efficient transfer learning. Preprint, arXiv:2004.03829.

Che Liu, Haozhe Wang, Jiazhen Pan, Zhongwei Wan, Yong Dai, Fangzhen Lin, Wenjia Bai, Daniel Rueckert, and Rossella Arcucci. 2025a. Beyond distillation: Pushing the limits of medical llm reasoning with minimalist rule-based rl. Preprint, arXiv:2505.17952.

Jingping Liu, Tao Chen, Zujie Liang, Haiyun Jiang, Yanghua Xiao, Feng Wei, Yuxi Qian, Zhenghong

## B-ocr-c4b674c1328797

B PDF page 2

ing residual components frozen as a structural anchor. In this way, GeoRA simultaneously aligns adaptation with RLVR-specific optimization geometry and preserves dense matrix computation, achieving both stable optimization and hardware-efficient training. To the best of our knowledge, GeoRA is the first geometry-aware low-rank adaptation framework explicitly designed for RLVR. Our contributions are summarized as follows:

- We propose GeoRA, a geometry-aware, low-rank, and parameter-efficient adaptation framework tailored to RLVR. By aligning low-rank adaptation with RLVR-specific optimization geometry while preserving dense computation, GeoRA overcomes the geometric mismatch of SFT-oriented low-rank methods and the efficiency bottleneck of sparse methods.
- We show that the effective RL update subspace is directional and admits a compressible low-rank structure. GeoRA extracts dominant trainable directions via SVD within this subspace to initialize low-rank adapters, while a frozen residual component acts as a structural anchor to preserve pre-trained structure.
- Experiments on Qwen and Llama models from 1.5B to 32B parameters demonstrate that GeoRA improves training stability and consistently outperforms strong low-rank baselines across diverse RLVR settings, while showing stronger generalization and less forgetting on out-of-domain tasks.

## 2 Related Work

### 2.1 RLVR and Optimization Geometry

RLVR replaces traditional reward models with deterministic verifiers (e.g., in math or coding) (Zhang et al., 2025; Lambert et al., 2025; Yuan et al., 2025). Through outcome-based feedback, it incentivizes emergent reasoning behaviors like Chain-of-Thought (CoT), establishing itself as a core paradigm for enhancing LLM reasoning (Hu et al., 2025; Liu et al., 2025b).

Recent mechanistic analyses have delineated a sharp dichotomy between supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR). While SFT primarily injects knowledge by modifying principal weight directions (Chu et al., 2025; Jin et al., 2025b), RLVR is better characterized as a constrained optimization

process (Wu et al., 2025) that amplifies latent reasoning behaviors via reward-induced sampling bias rather than introducing new capabilities (Yue et al., 2025; Zhao et al., 2025; Alam and Rastogi, 2025). Theoretically, these updates manifest “off the principals,” favoring low-magnitude directions orthogonal to pre-trained features (Zhu et al., 2025), consistent with the rank-1 dominance observed in early training (Cai et al., 2025). However, this regime faces stability trade-offs. KL-regularization (“RL’s Razor”) attempts to limit forgetting (Shenfeld et al., 2025) but can precipitate the “Reasoning Boundary Paradox,” where aggressive reward maximization collapses exploration diversity (Nguyen et al., 2025). Although capability degradation may be partially reversed via singular vector rotation (Jin et al., 2025a,b), adaptation remains fundamentally constrained by the “Invisible Leash,” which enforces proximity to the pre-training manifold (Wu et al., 2025). Empirically, strong gains can emerge from updating only a small fraction of parameters, suggesting that RL fine-tuning often concentrates on small subnetworks (Mukherjee et al., 2025).

### 2.2 PEFT and Spectral Priors

To alleviate the computational demands of scaling LLMs, PEFT (Xu et al., 2023; Han et al., 2024) has emerged as a key paradigm, minimizing memory overhead by updating only a fraction of parameters while matching full fine-tuning performance. Prevailing strategies include partial fine-tuning (Zaken et al., 2022; Lawton et al., 2023), soft prompt tuning (Hambardzumyan et al., 2021), non-linear adapters (Lin et al., 2020), low-rank adaptation (Li et al., 2018), and importance-aware methods like LIFT (Liu et al., 2025c). As a practical paradigm, PEFT has also been effectively adapted to continual learning (Liang et al., 2023) and multi-task learning (Liu et al., 2023) scenarios.

Among these, LoRA (Hu et al., 2021) and its variants are the de facto standard, yet their initialization strategies often diverge based on spectral priors. For instance, PiSSA (Meng et al., 2025) allocates trainable parameters to principal singular components, imposing a strong inductive bias validated primarily in SFT. However, such SFT-oriented spectral priors can create a fundamental geometric mismatch in RLVR, whose optimization dynamics and effective update patterns differ markedly from SFT (Yin et al., 2025; Zhu et al., 2025; Mukherjee et al., 2025). MiLoRA (Wang et al., 2025) instead targets minor components,

## B-ocr-d9f77f48ca57f8

B PDF page 6

![img-3.jpeg](img-3.jpeg)

Figure 3: Training dynamics of Qwen3-8B as evaluated on the AIME benchmark (average of 2024 and 2025). GeoRA remains consistently top-performing throughout training.

benchmark. GeoRA remains consistently top-performing throughout training and reaches strong performance substantially earlier than other low-rank baselines. In contrast, LoRA, MiLoRA, and PiSSA improve more slowly and plateau at lower levels. This indicates that GeoRA not only yields better final accuracy, but also provides a more favorable optimization trajectory under RLVR.

Hyperparameter Robustness. We first evaluate performance under different learning rates on Qwen3-4B in Figure 4. GeoRA maintains high reward across a broad range of learning rates, while other low-rank baselines are much more sensitive to this choice. In particular, PiSSA and MiLoRA degrade rapidly under larger learning rates, and LoRA also exhibits a clear drop in performance at the high end of the sweep. These results suggest that GeoRA is more robust to hyperparameter variation and requires less delicate tuning in practice. Similar robustness trends are also observed for other hyperparameters, including rank and sparsity, as shown in Appendix D.

Stability Under Aggressive Optimization. To stress-test optimization stability, we further compare reward and KL divergence under an aggressive learning rate in Figure 5. GeoRA maintains the highest reward trajectory without collapse, whereas PiSSA suffers a catastrophic drop late in training. At the same time, GeoRA keeps KL divergence at a low and controlled level throughout training. These results are highly relevant to RLVR optimization, which often requires stable policy updates within trust-region-like boundaries. The combination of higher reward and smoother KL behavior suggests that GeoRA improves exploration and policy refinement without inducing the destabilizing updates

![img-4.jpeg](img-4.jpeg)

Figure 4: Performance comparison across different learning rates. GeoRA demonstrates superior stability and robust convergence even at higher learning rates.

caused by geometry-misaligned adaptation.

Efficiency. Table 3 compares the training efficiency of FullFT, SparseFT, and GeoRA. GeoRA updates only a tiny fraction of parameters, reducing trainable parameters by 99.5% relative to FullFT, while also lowering VRAM usage and improving per-iteration training speed. Compared with SparseFT, GeoRA avoids the overhead of unstructured sparse computation and therefore translates its parameter efficiency into actual hardware efficiency. Although GeoRA introduces an SVD-based initialization step, this cost is a one-time preprocessing overhead and is negligible compared with RLVR training; detailed profiling is provided in the appendix. Overall, these results show that GeoRA improves not only effectiveness and stability, but also practical training efficiency.

Table 3: Efficiency Comparison between Full FT, SparseFT, and GeoRA. Relative reductions compared to Full FT are shown in parentheses.

[tbl-2.html](tbl-2.html)

### 4.4 Ablation and Analysis

Impact of Initialization Strategy. Table 4 shows that GeoRA's geometry-aware initialization is critical to its performance. Replacing the proposed initialization with Random-r initialization leads to a clear drop across all benchmarks, while Tail-r initialization performs even worse. This indi-

[OCR table id=tbl-2.html; page=6]
<table><tr><td>Method</td><td>Params (B)</td><td>Time (s/it)</td><td>VRAM (%)</td></tr><tr><td>Full FT</td><td>8.00</td><td>231</td><td>95.73</td></tr><tr><td>SparseFT</td><td>2.56(-68.0%)</td><td>256(+10.8%)</td><td>81.25(-15.1%)</td></tr><tr><td>GeoRA</td><td>0.04(-99.5%)</td><td>185(-19.9%)</td><td>68.43(-28.5%)</td></tr></table>

## B-ocr-e1c4f2990c0d3e

B PDF page 13

## A Algorithm

Algorithm 1 GeoRA Initialization Algorithm

Require: Pre-trained weights  \( W \in R^{m \times n} \) , rank r, sparsity ratio  \( \rho \) .

Ensure: Initialized adapters A, B, Frozen residual matrix  \( W_{res} \) .

1: Phase 1: Geometric Prior Construction
2:  \( \hat{W}_{r} \leftarrow \text{SVD}_{r}(W) \)  {Compute rank-r approximation}
3: Determine thresholds  \( \tau_{spec} \)  and  \( \tau_{euc} \)  corresponding to bottom  \( \rho \)  quantile
4:  \( M_{\text{spec}} \leftarrow \mathbb{I}(|\hat{W}_{r}| \leq \tau_{\text{spec}}) \)  {Spectral Prior}
5:  \( M_{\text{euc}} \leftarrow \mathbb{I}(|W| \leq \tau_{\text{euc}}) \)  {Euclidean Prior}
6:  \( W_{\text{geo}} \leftarrow W \odot (M_{\text{spec}} \cup M_{\text{euc}}) \)  {Union of priors (unconstrained sparsity)}
7: Phase 2: Geometry-Aware Decomposition
8:  \( U_{g}, \Sigma_{g}, V_{g}^{\top} \leftarrow \text{SVD}(W_{\text{geo}}) \) 
9:  \( A \leftarrow U_{g}[:, : r] \Sigma_{g}^{1/2} \) 
10:  \( B \leftarrow \Sigma_{g}^{1/2} V_{g}^{\top}[:, : r] \) 
11: Phase 3: Residual Leash Instantiation
12:  \( W_{res} \leftarrow W - AB \) 
13: Freeze  \( W_{res} \)  during training
14: return A, B,  \( W_{res} \)

## B GeoRA Initialization Properties

This section provides lightweight theoretical justifications for GeoRA's initialization and reparameterization.

### B.1 Optimality of the Geo-SVD Initialization

Proposition 1 (Eckart–Young optimality within  \( W_{geo} \) ). Let  \( W_{geo} \in R^{m \times n} \)  admit an SVD  \( W_{geo} = U \Sigma V^{\top} \) , and define the truncated reconstruction  \( W_{\mathrm{geo}}^{(r)} \triangleq U_{[:,:r]} \Sigma_{[:,:r]} V_{[:,:r]}^{\top} \) . Then  \( W_{\mathrm{geo}}^{(r)} \)  is the best rank-r approximation under the Frobenius norm:

\[
W _ {\mathrm{geo}} ^ {(r)} \in \arg \min _ {\operatorname{rank} (X) \leq r} \| W _ {\mathrm{geo}} - X \| _ {F}. \tag {11}
\]

With the initialization \(B \leftarrow U_{[:,:r]}\Sigma_{[:,r,:r]}^{1/2}\) and \(A \leftarrow \Sigma_{[:,r,:r]}^{1/2}V_{[:,:r]}^{\top}\), we have \(BA = W_{\mathrm{geo}}^{(r)}\).

### B.2 Initialization and Residual Leash

Proposition 2 (Function-preserving at initialization). Define  \( W_{res} \triangleq W - \frac{\alpha}{r} BA \)  and the effective weight  \( W_{\mathrm{eff}}(A, B) \triangleq W_{\mathrm{res}} + \frac{\alpha}{r} BA \) . Then for any input x, the forward pass satisfies  \( W_{\mathrm{eff}}(A, B)x = Wx \)  at initialization, hence GeoRA is function-preserving at t = 0.

Table 7: Empirical initialization cost of GeoRA. We compare standard SVD and randomized SVD across model scales, and report the training cost of Qwen3-8B for reference.

[tbl-6.html](tbl-6.html)

Gradient mapping (useful for understanding stability). Let  \( G \triangleq \frac{\partial L}{\partial W_{eff}} \)  denote the gradient w.r.t. the effective weight. By matrix calculus,

\[
\frac {\partial \mathcal {L}}{\partial A} = \frac {\alpha}{r} B ^ {\top} G, \quad \frac {\partial \mathcal {L}}{\partial B} = \frac {\alpha}{r} G A ^ {\top}. \tag {12}
\]

Freezing  \( W_{res} \)  constrains learning to the rank-r manifold  \( \left\{\frac{\alpha}{r}BA:A\in\mathbb{R}^{r\times n},B\in\mathbb{R}^{m\times r}\right\} \) , while the residual leash keeps the model anchored near W.

### B.3 Compute and Memory Complexity

The truncated SVD on  \( W_{geo} \)  is a one-off preprocessing step. In practice, one can use truncated or randomized SVD with time roughly linear in r (e.g.,  \( \tilde{O}(mnr) \)  for dense operators), which substantially reduces the initialization overhead compared with full SVD.

GeoRA uses dense low-rank updates. Computing  \( \left(\frac{\alpha}{r}BA\right)x \)  can be decomposed into two matrix multiplications, costing  \( O(rn+mr) \)  per layer, which is typically more GPU-friendly than irregular sparse updates at the same parameter budget.

### B.4 Empirical Initialization Cost

Practical overhead of SVD initialization. Although GeoRA introduces an additional SVD-based preprocessing step, this cost is incurred only once before training. Since GeoRA only requires the top-r singular components, the initialization can be accelerated with randomized SVD, whose complexity is approximately linear in r for dense operators.

Table 7 reports the wall-clock time and peak VRAM of standard SVD and randomized SVD

[OCR table id=tbl-6.html; page=13]
<table><tr><td>Model</td><td>Method</td><td>Wall-clock Time (min)</td><td>Peak VRAM (GB)</td></tr><tr><td>8B</td><td>Training</td><td>838</td><td>~384</td></tr><tr><td>8B</td><td>Standard SVD</td><td>18.87</td><td>16.48</td></tr><tr><td>8B</td><td>Rand. SVD</td><td>0.21</td><td>15.78</td></tr><tr><td>14B</td><td>Standard SVD</td><td>25.78</td><td>29.63</td></tr><tr><td>14B</td><td>Rand. SVD</td><td>0.26</td><td>28.43</td></tr><tr><td>32B</td><td>Standard SVD</td><td>35.23</td><td>64.05</td></tr><tr><td>32B</td><td>Rand. SVD</td><td>0.47</td><td>62.38</td></tr><tr><td>72B</td><td>Standard SVD</td><td>97.82</td><td>146.87</td></tr><tr><td>72B</td><td>Rand. SVD</td><td>0.72</td><td>140.41</td></tr></table>

## B-ocr-fa93bb4c8d71bf

B PDF page 9

Table 6: Geometric mechanism analysis.

[tbl-5.html](tbl-5.html)

high-energy principal subspace ( \( S_{Head} \leq 0.02 \) )—enhancing stability—and efficiently adapts the geometry-constrained tail ( \( S_{Tail} \geq 0.96 \) ). In contrast, PiSSA's instability is explained by its high overlap with the head subspace ( \( \approx 0.98 \) ).

## 6 Conclusion

In this paper, we bridge the gap between parameter-efficient fine-tuning and the distinctive optimization geometry of RLVR. Our study suggests that existing PEFT methods often yield suboptimal results in RLVR due to a structural mismatch. SFT-oriented low-rank methods prioritize directions that may be misaligned with the geometry-constrained updates favored by RLVR, while some sparse update methods better reflect RLVR dynamics but fail to translate into practical hardware efficiency. GeoRA addresses these challenges by identifying a compressible, geometry-aligned update subspace and parameterizing it through structured SVD initialization with a frozen residual anchor. Experiments on Qwen and Llama models from 1.5B to 32B parameters show that GeoRA consistently improves mathematical RLVR performance, extends effectively to medical and coding RLVR settings, and exhibits stronger generalization with less forgetting on out-of-domain tasks. Overall, GeoRA provides an effective, stable, and hardware-efficient adaptation strategy for RLVR.

### Limitations

Despite its effectiveness, GeoRA has certain limitations. First, the initialization process requires performing a truncated SVD and dual-masking operations. While these represent a one-time computational cost at the beginning of training, they introduce an additional pre-processing step compared to the random initialization used in standard LoRA. Second, our experiments primarily focus on RLVR in reasoning domains. Although GeoRA

demonstrates strong performance on these tasks, its generalizability needs to be further validated across a broader range of model architectures and diverse reinforcement learning scenarios beyond verifiable rewards.

## References

Md Tanvirul Alam and Nidhi Rastogi. 2025. Limits of generalization in rlvr: Two case studies in mathematical reasoning. Preprint, arXiv:2510.27044.

Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, and Quoc Le. 2021. Program synthesis with large language models. arXiv preprint arXiv:2108.07732.

Yuchen Cai, Ding Cao, Xin Xu, Zijun Yao, Yuqing Huang, Zhenyu Tan, Benyi Zhang, Guiquan Liu, and Junfeng Fang. 2025. On predictability of reinforcement learning dynamics for large language models. Preprint, arXiv:2510.00553.

Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, and 39 others. 2021. Evaluating large language models trained on code. Preprint, arXiv:2107.03374.

Tianzhe Chu, Yuexiang Zhai, Jihan Yang, Shengbang Tong, Saining Xie, Dale Schuurmans, Quoc V. Le, Sergey Levine, and Yi Ma. 2025. Sft memorizes, rl generalizes: A comparative study of foundation model post-training. Preprint, arXiv:2501.17161.

Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman. 2021. Training verifiers to solve math word problems. Preprint, arXiv:2110.14168.

Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Yuchen Zhang, Jiacheng Chen, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, Jiarui Yuan, Huayu Chen, Kaiyan Zhang, Xingtai Lv, Shuo Wang, Yuan Yao, Xu Han, and 6 others. 2025. Process reinforcement through implicit rewards. Preprint, arXiv:2502.01456.

DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhi-hong Shao, Zhuoshu Li, Ziyi Gao, and 181 others. 2025. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. Preprint, arXiv:2501.12948.

[OCR table id=tbl-5.html; page=9]
<table><tr><td rowspan="2">Method</td><td colspan="3">Llama-3.1-8B</td><td colspan="3">Qwen3-8B</td></tr><tr><td>NSS↓</td><td>\( S_H \) ↓</td><td>\( S_T \) ↑</td><td>NSS↓</td><td>\( S_H \) ↓</td><td>\( S_T \) ↑</td></tr><tr><td>PiSSA</td><td>0.395</td><td>0.98</td><td>0.01</td><td>0.418</td><td>0.95</td><td>0.03</td></tr><tr><td>LoRA</td><td>0.214</td><td>0.15</td><td>0.15</td><td>0.235</td><td>0.18</td><td>0.18</td></tr><tr><td>MiLoRA</td><td>0.125</td><td>0.12</td><td>0.92</td><td>0.132</td><td>0.16</td><td>0.90</td></tr><tr><td>GeoRA</td><td>0.092</td><td>0.005</td><td>0.98</td><td>0.096</td><td>0.015</td><td>0.96</td></tr></table>

## B-ocr-febb156614fa27

B PDF page 8

Table 5: Overlap analysis of the spectral prior  \( M_{Spec} \)  and Euclidean prior  \( M_{Euc} \)  on Qwen3-8B with  \( \rho = 0.2 \) .

[tbl-4.html](tbl-4.html)

Qwen3-8B with  \( \rho = 0.2 \) , both  \( M_{Spec} \)  and  \( M_{Euc} \)  select 20.0% of parameters, but their overlap remains small: the overall intersection is only 4.55%, with a Jaccard index of 0.128. Similar patterns are observed in both MLP layers (4.63%, 0.131) and attention layers (4.25%, 0.119). This limited overlap indicates that the two masks capture largely distinct parameter subsets and therefore serve complementary geometric roles. This is also consistent with the ablation results in Table 4: removing either prior leads to a clear performance drop.

### 5.2 Low-Rank Structure

To validate the structural basis of GeoRA, we analyze the singular value spectrum of the geometry-constrained subspace. We compare  \( W_{Geo} \)  with the original pre-trained weights, as well as random noise matrices at both full and sparse density. Figure 6a yields two key insights. First, sparsity does not by itself induce low-rankness. The spectrum of sparse random noise is nearly indistinguishable from that of dense random noise, and both follow a relatively flat decay pattern. This indicates that unstructured sparsity alone remains essentially isotropic in the spectral domain. Second,  \( W_{Geo} \)  preserves a pronounced heavy-tailed spectrum similar to that of the pre-trained weights, with most spectral mass concentrated in a small number of leading components. This shows that the selected update region inherits a structured and compressible low-rank form rather than behaving like random sparse noise.

We further find that the actual FullFT update,  \( \Delta W_{FullFT} = W_{FullFT} - W_{Pretrain} \) , exhibits a similarly compressible heavy-tailed spectrum. This strongly supports the low-rank inductive bias of GeoRA: the effective RLVR update space is not isotropic, but already structured and highly compressible. GeoRA therefore captures an intrinsic property of RLVR updates, instead of imposing an artificial low-rank constraint.

![img-7.jpeg](img-7.jpeg)

(a) Singular value spectrum of the geometry-constrained subspace \( W_{\mathrm{Geo}} \).

![img-8.jpeg](img-8.jpeg)

(b) Singular value spectrum of the full fine-tuning update \(\Delta W_{\mathrm{FullFT}}\).

Figure 6: Spectral analysis of RLVR update structure.

### 5.3 Spectral Efficiency and Alignment

Building on the low-rank structure of RL updates, we validate GeoRA's geometric superiority via Normalized Spectral Shift (NSS) and Subspace Alignment(Table 6). First, NSS quantifies the topological distortion of the pre-trained manifold:

\[
\mathrm{NSS} = \frac {\| \sigma (W ^ {\text { tuned }}) - \sigma (W) \| _ {2}}{\| \sigma (W) \| _ {2}}. \tag {9}
\]

While PiSSA exhibits high NSS (> 0.39), indicating aggressive structural modification, GeoRA maintains minimal distortion ( \( \approx \)  0.09), confirming it maximizes reward acquisition while preserving fundamental features.

To pinpoint the update locus, we calculate the alignment between \(\Delta W\) and the pre-trained singular vectors \(V\):

\[
\mathcal {S} (k) = \frac {\| \Delta W v _ {k} \| _ {2}}{\| \Delta W \| _ {F}} \approx | \cos (\theta_ {k}) |. \tag {10}
\]

GeoRA shows a distinct signature: it avoids the

[OCR table id=tbl-4.html; page=8]
<table><tr><td>Group</td><td>\( M_{\text{Spec}} \)</td><td>\( M_{\text{Euc}} \)</td><td>Intersection</td><td>Jaccard</td></tr><tr><td>MLP</td><td>20.0%</td><td>20.0%</td><td>4.63%</td><td>0.131</td></tr><tr><td>Attn</td><td>20.0%</td><td>20.0%</td><td>4.25%</td><td>0.119</td></tr><tr><td>All</td><td>20.0%</td><td>20.0%</td><td>4.55%</td><td>0.128</td></tr></table>
