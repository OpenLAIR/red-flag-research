# Muon on the Quotient: Gauge-Equivariant Descent for Homogeneous Networks

## B-04bf675f459fc8

candidate openreview-yHxCX7wnSJ PDF page 28

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
Under review as a conference paper at ICLR 2027
Equivalently, Euclidean radial flow is a mirror flow with a separable potential of curvatureψ′′
ci(p) =
(4p2 +c 2
i )−1/2 and dual coordinate
ψ′
ci(p) =
 1
2 arsinh(2p/|ci|), c i ̸= 0,
1
2 logp, c i = 0,
up to additive constants. At balance, its dynamics coincide with the α= 0 reduced flow up to a factor
of two in time. Away from balance, the mirror geometry depends on the conserved, gauge-dependent
imbalance. The mobility p1−α
i prescribed by Gauge-Muon depends only on the invariant path mass.
Together with the capacity budget, this shows how α controls both the available path motion and the
geometry of the reduced model, without implying a generalization advantage for any exponent.
F.6 SHARE AND LOG-VARIANCE BALANCE LAWS
Consider a continuous-time path flow with pi(t)>0 , such as the reduced dynamics ˙pi =ν ip1−α
i of
Lemma F.4, whereνi is the demand the task places on pathi. Define the total path massP= Ph
j=1 pj,
the path shares πi =p i/P , the log-masses ℓi = logp i with mean ¯ℓ= 1
h
P
i ℓi, and the log-growth
ratesψ i = ˙ℓi = ˙pi/pi (under these dynamics,ψ i =ν ip−α
i ).
Lemma F.7(Share and log-variance balance laws).The path shares follow the replicator equation
˙πi =π i

ψi −
X
j
πjψj

,(55)
and the log-path varianceV logp = 1
h
P
i(ℓi − ¯ℓ)2 satisfies
d
dt Vlogp = 2Covi(logp i, ψi),(56)
whereCov i(ai, bi) = 1
h
P
i(ai −¯a)(bi − ¯b)is the uniform covariance over hidden units.
Proof.Since˙p i =p iψi,
˙P=
X
i
˙pi =
X
i
piψi =P
X
i
πiψi.(57)
Differentiateπ i =p i/P:
˙πi = ˙piP−p i ˙P
P 2 (58)
= piψi
P − pi
P
X
j
πjψj (59)
=π i

ψi −
X
j
πjψj

 ,(60)
which proves Equation 55.
Next, ˙ℓi =ψ i and ˙¯ℓ= ¯ψ:= 1
h
P
i ψi. Differentiating the variance gives
d
dt Vlogp = 2
h
X
i
(ℓi − ¯ℓ)(ψi − ¯ψ) = 2Covi(logp i, ψi),(61)
which proves Equation 56. Note that P
i(ℓi − ¯ℓ) = 0 , so the ¯ψ term contributes nothing and the
derivative also equals 2
h
P
i(ℓi − ¯ℓ)ψi.
G EXPERIMENTALRESULTS
Compute.All experiments were run on a single NVIDIA RTX PRO 6000 GPU.
28

## B-07b53114d60d75

candidate openreview-yHxCX7wnSJ PDF page 6

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
Under review as a conference paper at ICLR 2027
Why this is a quotient geometry.The tangent directions of the gauge orbit, (ΛU,−VΛ) for
diagonal Λ, change the parameterization but not the function, so the loss is flat along them and its
gradient annihilates them. Consequently, maximizing the gradient’s action over the unit ball of Equa-
tion 8 or over classes modulo these directions gives the same value χα, and Gauge-Muon is steepest
descent on the quotient of parameter space by the rescaling group. Comparing to Muon (Bernstein &
Newhouse, 2024b), only the unit ball changes and the polar oracle is the same but acts on invariant
covectors. Unlike natural gradient (Amari, 1998), which targets all smooth reparameterizations
with a Riemannian metric, Gauge-Muon removes one known architectural symmetry and uses a
non-Riemannian max-of-operator-norms geometry. Appendix D gives the derivation.
6 WHAT THE EXPONENTαCONTROLS
To this end, we have established the symmetry and geometry property of Gauge-Muon(α) for every
α. That is, every exponent α is equivariant and quotient steepest descent. This section presents how
different exponentαdistribute motions across paths of different invariant strength.
6.1 FIRST ORDER FUNCTIONAL MOBILITY
We examine functional mobility which characterize how a hidden unit change the functional output.
Consider the contribution of hidden unit i as fi(x) =v i ReLU(u⊤
i x). If we perturb the incoming
and outgoing path(u i, vi)with(δu i, δvi), the first-order perturbation is written as
δfi(x) =δv i ReLU(u⊤
i x)| {z }
outgoing branch
+v i1u⊤
i x>0 δu⊤
i x
| {z }
incoming branch
.(11)
The norm of ∥δfi(x)∥ can be bounded as ∥δfi(x)∥ ≤ ∥δv i∥ ∥ui∥ ∥x∥+∥v i∥ ∥δui∥= (∥δv i∥r i +
∥δui∥s i)∥x∥.Under Gauge-Muon step, we have the following proposition.
Proposition 6.1(Pathwise first-order functional-mobility bound).Suppose one Gauge-Muon step
with exponent α and learning rate η generate perturbation on path i, the first-order perturbation is
bounded as
∥δfi(x)∥2 ≤2η∥x∥ 2 p 1−α
i .(12)
This proposition says that up to factors independent of the path mass pi, the largest first-order
functional displacement available to a hidden path scales as mα(p) :=p 1−α. We call mα(p) the
functional-mobility scale. Its log-log elasticity with respect to path mass is dlogm α(p)
dlogp = 1−α. This
gives important interpretability for Gauge-Muon family. That is, for α <1 , larger-mass paths have a
larger first-order mobility scale. Forα= 1 , the mobility scale is independent of path mass. Forα >1 ,
smaller-mass paths have a larger first-order mobility scale. Also, when α= 1/2 , Gauge-Muon has
balanced canonical scalings
p
ri/si and
p
si/ri.
RemarkWe have show that the exponent has an exact power-law interpretation in function space.
Hence, we should not treat it as an optimizer parameters. While gauge invariance eliminates scaling
symmetry in ReLU network, α decides how the optimization is distributed across invariant path
strengths. Path-SGD (Neyshabur et al., 2015a) also normalizes updates using complementary path
information, but it does not expose a matrix-spectral mobility family. Our α= 1 case shares the
intuition of complementary-side normalization, while the polar operation couples directions through
singular vectors. PathCond (Lebeurrier et al., 2026) instead changes an orbit representative to improve
conditioning before optimization.
Capacity and implicit geometry.The mobility law also has statistical and geometric consequences,
developed in Appendix F.1. The total path mass P(θ) = P
i pi is gauge invariant and bounds
generalization; at α= 1 every path receives the same capacity-growth allowance (Theorem F.1). In
an idealized path flow, the exponent selects a mirror geometry that interpolates between entropic
(α= 0 ) and Euclidean ( α= 1 ), independently of the gauge, whereas the implicit geometry of
Euclidean gradient flow depends on the gauge.
6

## B-0bc58caebf1f8b

candidate openreview-yHxCX7wnSJ PDF page 3

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
Under review as a conference paper at ICLR 2027
LMO. Specifically, Gauge-Muon treats the balancing exponent α as a free geometric parameter,
which yields a path-mobility degree of freedom that canonical Euclidean descent does not have.
Conservation laws and implicit bias.Under Euclidean gradient flow, rescaling symmetry con-
serves (Du et al., 2018; Kunin et al., 2020; Marcotte et al., 2023), and reparameterization-induced
implicit bias is well described by mirror descent (Gunasekar et al., 2018; Li et al., 2022), with
potentials that interpolate between entropic and Euclidean geometry as a function of the initialization
scale or shape (Woodworth et al., 2019; Azulay et al., 2021). The conserved quantity depends on the
gauge, so the implicit bias of these flows depends on the initial representative. Under Gauge-Muon,
path masses follow a mirror flow under a Box–Cox potential indexed by theoptimizerparameter α,
independent of the gauge of the initialization.
3 BACKGROUND AND MOTIVATION
In this section, we review the necessary background on the Muon optimizer, and explain how gauge
symmetry motivates our approach. Note that notations used in the paper are provided in Appendix A
3.1 MUON FROM FIRST PRINCIPLES
Here, we start with the exact matrix opertion that Muon optimizer (Jordan et al., 2024) tries to
approximate.
The support polar factorGiven H∈R m×n with compact SVD H=PΣQ ⊤, thesupport polar
factorof H is defined as polar(H) =P Q ⊤. Here, only singular directions with positive singular
value are involved. We can write the support polar factor in terms of the duality norm
polar(H)∈arg max
∥Q∥op≤1
⟨H, Q⟩F ,⟨H,polar(H)⟩ F =∥H∥ ∗ .(1)
This means that we can understand that polar(H) is the direction of largest first-order decrease if
one is allowed a unit operator-norm step.
Consider L(W) be differentiable loss function of a matrix parameter W , with gradient G=
∇W L(W) . One can show that among all perturbations ∆W satisfying ∥∆W∥ op ≤1 , the most
negative first-order change1 is attained by ∆W=−polar(G), and equals to − ∥G∥∗. This is the
gradient step that Muon optimiers wish to update model parameters.
Momentum.Practical implementations of Muon employ momentum. Specifically, given a momen-
tum coefficient µ∈(0,1) , the momentum matrix is computed as an exponential moving average of
the gradients Gt via the online update Mt =µM t−1 + (1−µ)G t. The Muon parameter update is
then applied to the momentum matrix asW t+1 =W t −ηpolar(M t)..
Newton-Schulz approximation.To avoid the computational cost of an explicit SVD, practical
Muon implementations approximate the polar factor using a small number of Newton-Schulz it-
erations. This procedure progressively maps the nonzero singular values toward one using only
matrix multiplications (Jordan et al., 2024). Throughout this paper, we use the exact polar factor
in our theoretical derivations. Nevertheless, it may be replaced in practice by any deterministic
approximation to the polar map.
3.2 MOTIVATION
ReLU NetworkOur central subject in two-layer neural networks with ReLU activation
fU,V (x) =VReLU(U x) =
hX
i=1
vi ReLU(u⊤
i x),(2)
where x∈R d is the input, U∈R h×d is the incoming matrix, V∈R k×h is the outgoing matrix, u⊤
i
denotes row i of U, and vi denotes column i of V . Thus hidden unit i contributes vi ReLU(u⊤
i x)
1First-order change according to Talor approximation is⟨G,∆W⟩ F
3

## B-0be4377664c879

candidate openreview-yHxCX7wnSJ PDF page 36

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
Under review as a conference paper at ICLR 2027
10 20 30
100
training loss
CIFAR-100 / ResNet-18
10 20 30
10−3
10−2
10−1
100
CIFAR-100 / ResNet-50
10 20 30
100
training loss
SVHN / ResNet-18
10 20 30
100
SVHN / ResNet-50
10 20 30
10−3
10−2
10−1
100
training loss
FashionMNIST / MLP
2 4 6 8 10
epoch
10−2
10−1
100
CIFAR-100 / ViT-S/16 ReLU FT
2 4 6 8 10
epoch
10−1
100
training loss
CIFAR-100 / ViT-B/16 ReLU FT
Muon
Gauge-Muon(1)
Gauge-Muon(0.5)
Path-SGD
Adam
Figure 13: Mean training loss per epoch (log scale) at each method’s selected learning rate, with
standard-error bands over seeds.
G.5 LANGUAGEMODELINGTASK
G.5.1 ARCHITECTURES
We used the same GPT-2 small setup for our experiments in the language modeling tasks including
dmodel = 768, pre-norm, a 512-token context and GPT-2 tokenizer. We only change the feed-forward
block which is the main focus of Gauge-Muon.
In our main text, we consider two settings of feed-forward blocks including dense feed-forward and
mixture of experts.
Dense feed-forwardEach block has incoming and outgoing matrices form the pair (Wup, Wdown)
that Gauge-Muon is defined on. There are two options for our activations: ReLU and SwiGLU.
36

## B-141c466970299c

candidate openreview-yHxCX7wnSJ PDF page 34

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
Under review as a conference paper at ICLR 2027
10−1 100 101 102
40
50
60
validation accuracy (%)
CIFAR-100 / ResNet-18
10−1 100 101 102
60
65
70
75
CIFAR-100 / ResNet-50
10−1 100 101
50
60
70
validation accuracy (%)
SVHN / ResNet-18
10−1 100 101 102
50
55
60
65
SVHN / ResNet-50
10−1 100 101
70
75
80
85
90
validation accuracy (%)
FashionMNIST / MLP
10−1 100 101 102
learning rate / selected learning rate
82
84
86
88
90
CIFAR-100 / ViT-S/16 ReLU FT
10−3 10−2 10−1 100 101
learning rate / selected learning rate
80
85
validation accuracy (%)
CIFAR-100 / ViT-B/16 ReLU FT
Muon
Gauge-Muon(1)
Gauge-Muon(0.5)
Path-SGD
Adam
Figure 11: Learning-rate sensitivity for all seven settings. Tuning validation accuracy is plotted
against the learning rate divided by each method’s own selected rate, so every curve peaks at1 on the
horizontal axis and the shapes are directly comparable; rings mark the selected rates.
G.4.3 TRAINING CURVES
Figure 12 shows the validation accuracy per epoch at the selected learning rate of each method.
Figure 13 provides the corresponding training loss on a log axis. The bands in each plot are the
standard errors over seeds.
DiscussionWe observe that Gauge-Muon tends to fits later in the accuracy curves and takes over
Muon near the end. Other hand, the loss curves reveals that Gauge-Muon may have higher training
loss but still maintain higher accuracies. This may suggest that Gauge-Muon reaches a comparable or
better solution while fitting the training set markedly less. This behavior is expected from a method
that constrains path mass rather than merely descending faster.
34

## B-1a8cff6b915ed3

candidate openreview-yHxCX7wnSJ PDF page 43

2268
2269
2270
2271
2272
2273
2274
2275
2276
2277
2278
2279
2280
2281
2282
2283
2284
2285
2286
2287
2288
2289
2290
2291
2292
2293
2294
2295
2296
2297
2298
2299
2300
2301
2302
2303
2304
2305
2306
2307
2308
2309
2310
2311
2312
2313
2314
2315
2316
2317
2318
2319
2320
2321
Under review as a conference paper at ICLR 2027
−6 −4 −2 0 2 4
Gauge-Muon vs Muon (%)
MoE: ® = 0:25
MoE: ® = 0:5
MoE: no geo-mean normalization
MoE: router on SGD
dense h=256: Gauge-Muon
dense h=256: no normalization
-3.62
-3.36
+3.06
+0.26
-2.02
+3.09
Muon Gauge-
Muon(1)
43.5
44.0
44.5
45.0
val. perplexity
3 seeds
SwiGLU MoE
150M
Figure 16: Left: Gauge-Muon’s delta against Muon in the same setting after removing one ingredient
(SwiGLU MoE, 150M; last two rows dense h= 256 ). Right: three seeds of the SwiGLU MoE at
150M, paired by seed.
0 1 2
initial gauge strength q
10−1
100
101
PTQ accuracy drop (pp)
as trained
gauge fixed
Muon GM(1) GM(0.5) Path-SGD Adam
89.0
89.5
90.0
90.5
QAT test accuracy (%) q = 0
q = 2
Muon Gauge-Muon(1) Gauge-Muon(0.5) Path-SGD Adam
Figure 17: W4 per-channel quantization on FashionMNIST. Left: post-training accuracy drop
against the initial gauge, rounding the checkpoint as trained (dashed) or after moving it to the
vcolrepresentative (solid). Right: accuracy after quantization-aware training with the gauge-fixed
quantizer, atq= 0(open) andq= 2(filled); mean and standard error over three seeds.
43

## B-26b9b0ddea48b1

candidate openreview-yHxCX7wnSJ PDF page 10

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
Under review as a conference paper at ICLR 2027
REPRODUCIBILITYSTATEMENT
Our source code for all experiments is provided as supplementary material. Full experimental settings,
including model architectures, datasets, training procedures, and all hyperparameters, are provided in
Appendix G.4 for image classification and Appendix G.5 for language modeling.
AI USESTATEMENT
We used large language models (LLMs) to polish the writing, including editing for clarity and
correcting grammar. We also used Claude Code to help refine our experimental pipeline and to run
experiments under our direction. All research ideas, methods, and conclusions are our own.
REFERENCES
P-A Absil, Robert Mahony, and Rodolphe Sepulchre.Optimization algorithms on matrix manifolds.
Princeton University Press, 2008.
Kwangjun Ahn, Byron Xu, Natalie Abreu, Ying Fan, Gagik Magakyan, Pratyusha Sharma,
Zheng Zhan, and John Langford. Dion: Distributed orthonormalized updates.arXiv preprint
arXiv:2504.05295, 2025.
Shun-Ichi Amari. Natural gradient works efficiently in learning.Neural computation, 10(2):251–276,
1998.
Noah Amsel, David Persson, Christopher Musco, and Robert M Gower. The polar express: Optimal
matrix sign methods and their application to the muon algorithm. InInternational Conference on
Learning Representations, volume 2026, pp. 138323–138360, 2026.
Sanjeev Arora, Zhiyuan Li, and Kaifeng Lyu. Theoretical analysis of auto rate-tuning by batch
normalization.ArXiv, abs/1812.03981, 2018. URL https://api.semanticscholar.
org/CorpusID:54464191.
Shahar Azulay, Edward Moroshko, Mor Shpigel Nacson, Blake E. Woodworth, Nathan Srebro, Amir
Globerson, and Daniel Soudry. On the implicit bias of initialization shape: Beyond infinitesimal
mirror descent.ArXiv, abs/2102.09769, 2021. URL https://api.semanticscholar.
org/CorpusID:231979226.
Francis R. Bach. Breaking the curse of dimensionality with convex neural networks.
ArXiv, abs/1412.8690, 2014. URL https://api.semanticscholar.org/CorpusID:
1474026.
Francis R. Bach, Camille Dubois, Nicolas Thiou, Damien Ergun, and Ruben Ifrah. Learning
theory from first principles. URL https://api.semanticscholar.org/CorpusID:
273899875.
Vijay Badrinarayanan, Bamdev Mishra, and Roberto Cipolla. Symmetry-invariant optimization in
deep networks.arXiv preprint arXiv:1511.01754, 2015.
Kimi Team Yifan Bai, Yifan Bai, Yiping Bao, Chandru. M, Jianfeng Cai, Xin-Hao Cai, Peizhou Cao,
Yuxuan Cao, Ziwei Chai, Y . Charles, Hu-Sen Che, Guan-Duo Chen, Guang-Yu Chen, Guan-Zheng
Chen, Huarong Chen, Jia Chen, Jian-Long Chen, Jun Chen, Kexin Chen, Peng Chen, Ruijue
Chen, Wentao Chen, Xinxian Chen, Yang Chen, Yan-Ru Chen, Yi-Fei Chen, Ying-Jiang Chen,
Yuan-Kun Chen, Yu-Jie Chen, Yu-Tian Chen, Zhi-Rong Chen, Dazhi Cheng, Yean Cheng, Jia-Lei
Cui, Jing-Bing Cui, An-Bang Dai, Jiaqi Deng, Haochen Ding, Rui Ding, Shaofeng Ding, Meng-Fan
Dong, Meng-Nan Dong, Yu-Hao Dong, Yu-Xin Dong, Angang Du, Chenzhuang Du, Dikang Du,
Jusen Du, Yulun Du, Yu Fan, Jing Feng, Qiulin Feng, Yichen Feng, Kelin Fu, Qiang Fu, Fu-Juan
Gao, Hongcheng Gao, Jingyue Gao, Tong Gao, Wei Gao, Shang-Yi Geng, Jie Gong, Lin Gong,
Sheng Gong, Xiaocheng Gong, Qi-Zheng Gu, Yicheng Gu, Shuhao Guan, Haiqing Guo, Shiqi
Guo, Xiang Guo, Zhen Guo, Beixi Hao, Wenxing Hao, Xiaoru Hao, Dailan He, Haotian He, Lehan
He, Qi He, Weiran He, Xin-Ran He, Xin-Yi He, Yi-Bo He, Yun-Jia He, Chao Hong, Tiange Hong,
Hao-Xing Hu, Jiaxi Hu, Rui-Jia Hu, Weiming Hu, Yangyang Hu, Zhenxing Hu, Liang Hua, Jinbin
10

## B-2a561f05e6bcae

candidate openreview-yHxCX7wnSJ PDF page 9

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
Under review as a conference paper at ICLR 2027
10−2
learning rate ´
102
104
106
path-mass growth PT=P0
1018(a) 1B tokens
h = 256
h = 2048
10−1 100
aspect ratio h=d
10−2
10−1
Varilog pi at end
(b)
Muon
Gauge-Muon(1)
0 500 1000
tokens (M)
0
5
10
15
pplGM=pplMuon ¡ 1 (%)
(c) 1B tokens
dense h = 256
dense h = 512
MoE 8£256
ReLU MoE 8£384
dense h = 2048
ReLU h = 3072
Figure 6: Why narrow blocks and short budgets favor Gauge-Muon. (a) Path-mass growth against the
learning rate at 1B tokens; rings mark tuned rates. (b) Spread of log path mass at the end of training
against the aspect ratio h/d, at tuned rates; lines are least-squares fits in log–log scale, with slope
0.44 for Muon and 0.16 for Gauge-Muon. (c) Perplexity gap to Muon over training at 1B tokens;
solid lines are narrow blocks, dashed lines wide ones.
means narrower experts (Figure 5, bottom). The gain over Muon holds from 4 to 16 experts but
vanishes at 32 experts of width 64, where the shared learning rate is likely too large for Gauge-Muon
(Appendix G.5.5).
256 512 768 2048
dense hidden width h  (d = 768)
−2
0
2
vs Muon (%)
GM(1), 150M
GM(1), 1B
4
(512)
8
(256)
16
(128)
32
(64)
experts (expert width), 150M
−4
−2
0
vs Muon (%)
Figure 5: Perplexity relative to Muon at tuned
rates. Top: dense hidden width. Bottom: ex-
pert count at fixed MLP parameters.
Why width and budget matterWe investigate two
properties that can explain this in Figure 6. First,
Gauge-Muon moves every hidden unit by a fixed frac-
tion of its own size, thereby path mass compounds
and grows exponentially in the learning rate (see The-
orem F.3). On the other hand, Muon steps have a fixed
absolute size and its path mass grows only polyno-
mially. Gauge-Muon’s usable learning rate therefore
has to shrink as the budget grows, which slows its
early phase and delays the point where it overtakes
Muon. Second, the aspect ratio of the block decides
how Muon distributes its update. In a narrow block,
Muon’s orthogonalized update moves every hidden
unit by the same amount. In a wide block, it moves
units with larger gradients more and concentrates
path mass on them, while Gauge-Muon keeps path
mass evenly spread at every width (Figure 6 b). This
concentration appears to help early in training: at
1B tokens every narrow block eventually overtakes
Muon, while the wide blocks never do (Figure 6c).
Appendix G.5.5 gives the details.
8 CONCLUSION
We introduced Gauge-Muon, a family of orthogonal-
ized optimizers that respects the hidden-unit rescaling
symmetry of ReLU and SwiGLU networks. It keeps Muon’s polar map but applies it to gauge-
invariant covectors, which makes every member of the family exactly equivariant and steepest descent
on the quotient by the rescaling group. The family’s exponent sets how functional motion is allocated
across paths. Empirically, Gauge-Muon is unaffected by function-preserving rescalings and improves
on Muon in image classification and in GPT-2 language modeling, most consistently with narrow
feed-forward layers.
Limitations.Our language-modeling experiments are limited to small-scale models and token
budgets. An open question that whether the gains persist at larger model and data scales is left for
future work. We view the current study as a first characterization of Gauge-Muon rather than a scaling
result.
9

## B-2ab9efe359c998

candidate openreview-yHxCX7wnSJ PDF page 29

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
Under review as a conference paper at ICLR 2027
G.1 WHYMUON BREAKS SYMMETRY INRELUNETWORKS
We would like to note here that the problem is not that Muon optimizer is “badly scaled”. It is that two
sets of parameters (U, V) and (DV, V D −1) encoding the exactsamefunction can producedifferent
polar matrices. When a parameter coordinate is enlarged, the corresponding gradient coordinate
shrinks. A symmetry-compatible optimizer must account for this contravariant transformation before
applying its matrix oracle. To solve this, optimimizers must satisfy an exact computing diagram
that rescale-then-optimize must equal optimize-then-rescale. Path-SGD (Neyshabur et al., 2015a)
directly targets ReLU rescaling invariance. PathCond (Lebeurrier et al., 2026) chooses a favorable
orbit representative. In contrast, our goal in this paper is different. That is, we want to retain
Muon’s spectral oracle while making the covector (U, V) exact invariant. LoRA-Muon (Cesista
et al., 2026) addresses a related factor-rescaling issue for low-rank adaptation, but for a different
matrix-factorization symmetry.
Example 1Let ϕ(u, v) = 1
2(uv−y) 2 with scalar parameter u and v. At a minimizer, the only
nonzero Hessian eigenvalue is u2 +v 2. Suppose we transform (u, v)7→(cu, v/c) which preserves
the output of ϕ(u, v), this eigenvalue becomes c2u2 +c −2v2. It will diverges as c→0 or c→ ∞
and is minimized at c2 =v/u . Therefore, there is Euclidean learning rate that is uniformly stable
across all the representation of on function.
0 1 2
initial gauge strength q
101
102
canonical ¸1(H)
0 1 2
initial gauge strength q
102
canonical tr(H)
0 1 2
initial gauge strength q
10−3
10−2
10−1
training cross-entropy
Muon
Gauge-Muon(1)
Gauge-Muon(0.5)
Path-SGD
Adam
rate retuned vs. q = 0
Figure 7: Canonical-gauge top Hessian eigenvalue (left), trace (middle) and training loss (right) at
the solution each optimizer reaches, as a function of the gauge strength q at initialization. Sharpness
is measured after canonicalizing each checkpoint to the balanced gauge (making ri =s i for every i).
1 2
initial gauge strength q
0.1
0.2
0.4
kfq ¡ f0kF=kf0kF
1 2
initial gauge strength q
0.98
0.99
1.00
agreement with q = 0
Muon GM(1) GM(.5)
10−15
10−10
10−5
100
drift at q = 2
float32 float64
Muon
Gauge-Muon(1)
Gauge-Muon(0.5)
Path-SGD
Adam
rate retuned vs. q = 0
Figure 8: Change of the learned function when only the initial gauge changes. Left: relative drift
from the q= 0 run at matched seed. Middle: agreement of predictions with the q= 0 run. Right:
drift atq= 2in float32 and float64 after30epochs.
Loss landscape between optimizers.We trained a two-layer ReLU network on FashionMNIST
with optimizers including Muon, Adam, Path-SGD and Gauge-Muon(α), α∈ {0.5,1} . We setup the
initial gauge di = 10qzi, q∈ {0,1,2} that constructs the diagonal matrix D. Since the loss depends
on(U, V)only through the predictor, all optimizers descend one and the same surface.
29

## B-2d460e6d0e22ab

candidate openreview-yHxCX7wnSJ PDF page 4

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
Under review as a conference paper at ICLR 2027
to the output. We define its incoming magnitude ri and outgoing magnitude si and path mass pi
associated with hidden uniti
ri =∥u i∥2 , s i =∥v i∥2 , p i =r isi.(3)
Here, the path mass pi is understood as the product of the two side magnitudes ri and si with a
hidden route from input to output.
Function-preserving hidden-unit rescalingLet D= diag(d 1, . . . , dh) with every di >0 . Since
the positive homogeneity of ReLU activation,ReLU(cz) =cReLU(z), c >0, we can write
fDU,V D −1(x) =V D −1 ReLU(DU x) =VReLU(U x) =f U,V (x).(4)
Therefore all pairs (U, V)∼(DU, V D −1) represent the same function output. Let G= (R >0)h be
the set of all such D forms the positive diagonal group. We call this agauge symmetrythat move
along the orbit generated by G changes coordinates but not the represented function. Under this
action, the incomming, outgoing magnitudes and path mass is updated as r′
i =d iri, s′
i =d −1
i si,
p′
i =r ′
is′
i =p i. Thererfore, the path massp i is an exact gauge invariant.
Figure 1: Loss landscape of three
optimizers under diagonal rescaling
D=diag(d 1, . . . , dh), di = 10 z
i
or di = 102zi with zi ∼ U(−1,1) .
See Appendix G.1 for a detailed dis-
cussion including the sharpness of
loss landscape (Dinh et al., 2017).
Why ordinary Muon breaks the symmetryLet L(U, V) be
any differentiable loss function that depends on (U, V) only
through the predictor. We have L(DU, V D−1) =L(U, V).
Let GU =∇ U L(U, V) and GV =∇ V L(U, V) . At the trans-
formed point (U ′, V ′) = (DU, V D−1), the inverse coordinate
map is U=D −1U ′ and V=V ′D. Applying the chain rule
gives G′
U =D −1GU and G′
V =G V D. This means incoming
and outgoing gradients therefore transform in theoppositeway
from the corresponding parameters.
Suppose vanilla Muon optimizer is applied independently to
the two blocks U, V in ReLU neural network. Gauge equivari-
ance may require its incoming update to transform as ∆U ′ =
D∆U . However, the raw gradient transforms as D−1GU , and
in general, we have polar(D−1GU)̸=Dpolar(G U). This
mismatch is exactly analogous to the classical observation
that Euclidean SGD is not rescaling invariant in ReLU net-
works (Neyshabur et al., 2015a). Muon optimizer solves op-
timization setting involved matrices. However, in the setting
of ReLU network, those matrices are gauge-dependent objects.
For an illustration, Figure 1 shows how the loss landscapes (Li
et al., 2018) of different optimizers change under gauge rescal-
ing. The loss landscape of Muon and Adam optimizer change
under the rescaling while our Gauge-Muon is invariant under
gauge. A detailed discusion on the sharpness of their loss
landscape (Dinh et al., 2017) is provided in Appendix G.1.
4 GAUGE-MUONOPTIMIZER
Motivated by the gauge symmetry of ReLU networks, we now introduce Gauge-Muon. Rather than
treating the incoming and outgoing weights of a hidden layer as independent matrices, Gauge-Muon
updates them jointly as a pair (U, V) . We first constructcovariantscaling factors that combine
information from bothUandV.
Construct covariant scaling factorsLet us define Aα = diag

rip−α
i

and Bα = diag

sip−α
i

for an exponent α∈R . Because pi is invariant while ri and si transform oppositely, A′
α =DA α,
B′
α =D −1Bα. The transformed gradient blocks HU =A αGU , H V =G V Bα are therefore
invariant:
H ′
U =A ′
αG′
U = (DAα)(D−1GU) =H U , H ′
V =G ′
V B′
α = (GV D)(D−1Bα) =H V .(5)
We callH U , HV thecanonical covectors. The “canonical” here means gauge independent.
4

## B-3b74fd387ca57b

candidate openreview-yHxCX7wnSJ PDF page 33

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
Under review as a conference paper at ICLR 2027
images with a random horizontal flip and a reflect-padded random crop, then upsampled bilinearly to
224×224following the transfer protocol of Dosovitskiy et al. (2020).
Table 3 collects all the detailed information of architectures for the image classification task.
Table 3: Architecture of each cell. din is the input dimension of the trained two-layer ReLU pair; for
the fine-tuned transformers it is the MLP hidden width of each of the twelve blocks. Split sizes are
train/validation/test.
dataset backbone trained partd in split
FashionMNIST none (raw pixels) two-layer ReLU78454,000 / 6,000 / 10,000
CIFAR-100 frozen ResNet-18 two-layer ReLU51245,000 / 5,000 / 10,000
CIFAR-100 frozen ResNet-50 two-layer ReLU204845,000 / 5,000 / 10,000
SVHN frozen ResNet-18 two-layer ReLU51265,931 / 7,326 / 26,032
SVHN frozen ResNet-50 two-layer ReLU204865,931 / 7,326 / 26,032
CIFAR-100 ReLU ViT-S/16 all, MLP pairs gauged153645,000 / 5,000 / 10,000
CIFAR-100 ReLU ViT-B/16 all, MLP pairs gauged307245,000 / 5,000 / 10,000
G.4.2 LEARNING-RATE SENSITIVITY
Figure 11 plots tuning validation accuracy against the learning rate divided by the selected learning
of each method. Here, all curves peak at 1 on the horizontal axis to make theirshapesdirectly
comparable.
33

## B-3fd4737ab40256

candidate openreview-yHxCX7wnSJ PDF page 5

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
Under review as a conference paper at ICLR 2027
Apply Muon to the invariant covectorsThe main idea of our approach is that we apply Muon’s
polar operation on HU and HV , which aregauge invariant. We then pull the resulting polar factors
back with the same factors that created the covectors.
Definition 4.1(Gauge-Muon(α)).For learning rateη >0, one exact Gauge-Muon step is
U+ =U−ηA α polar(HU), V + =V−ηpolar(H V )Bα. (6)
Theorem 4.2(Exact finite-step gauge equivariance).Let (U ′, V ′) = (DU, V D −1) for a positive
diagonal D. If the two runs use the same learning rate and the same deterministic polar rule, then
after one Gauge-Muon step
(U ′+, V ′+) = (DU +, V +D−1).(7)
By induction, gauge-equivalent initializations remain gauge equivalent for all subsequent steps as
long as every active path has positive side norms.
In summary, Gauge-Muon works in three steps: (i) it first makes the covectors (HU , HV ) gauge
invariant, (ii) then applies Muon unchanged, (iii) and finally pulls the resulting direction back
through the covariant factors. This differs from existing approaches to rescaling invariance. Path-
SGD (Neyshabur et al., 2015a) obtains invariance through a path-normalized geometry, G-SGD (Meng
et al., 2019) optimizes directly in an explicit parameterization of invariant path coordinates, and
PathCond (Lebeurrier et al., 2026) rebalances the representative before training begins. In contrast,
Gauge-Muon maintains Muon’s matrix-level polar coupling. Thus, it cannot be viewed as spectral
restatement of Path-SGD. Specifically, Path-SGD links each edge to others through the input-output
paths they share, whereas in Gauge-Muon the singular vectors couple all units globally within each
matrix block.
Extension to SwiGLU networks.Transformer feed-forward blocks typically use
SwiGLU (Shazeer, 2020), F(x) =V(SiLU(W gx)⊙(U x)) by having a gate projec-
tion Wg. Because SiLU is not positively homogeneous, the continuous symmetry is now
(Wg, U, V)∼(W g, DU, V D−1). Gauge-Muon therefore applies to (U, V) unchanged, with ri, si,
and pi computed from U and V alone. For the gate, we use the invariant factor Ωα = diag(p −α
i )
and update W +
g =W g −ηΩ α polar(ΩαGg). This exponent is the only one under which the
gate branch moves the function at the same path scale p1−α
i as the up and down branches (cf.
Proposition 6.1). The three-block update here is exactly equivariant under both the rescaling and
hidden-unit permutations. Furthermore, it is steepest descent in a three-block case of the norm
introduced in Section 5. Appendix E gives the detailed derivation of SwiGLU extension.
5 GAUGE-MUON IS QUOTIENT SPECTRAL STEEPEST DESCENT
The exact equivariance in Theorem 4.2 does not tell us how the optimization perform. This section
will show the local geometry of Gauge-Muon update.
A state-dependent operator normConsider a parameter perturbation Ξ = (Ξ U ,Ξ V ) with the
same shapes as (U, V) . We introduce the following norm measuring the perturbation after removing
the path-dependent pullback factors
∥Ξ∥θ,α = max
n

A−1
α ΞU


op ,


ΞV B−1
α


op
o
, θ= (U, V).(8)
To derive its dual, we denote any unit perturbation as ΞU =A αZU , ΞV =Z V Bα with
∥ZU ∥op ,∥Z V ∥op ≤1. Then for a covectorG= (G U , GV ),
⟨G,Ξ⟩:=⟨G U ,Ξ U ⟩F +⟨G V ,Ξ V ⟩F =⟨A αGU , ZU ⟩F +⟨G V Bα, ZV ⟩F .(9)
Applying operator–nuclear duality to the two blocks separately yields the dual norm
∥G∥θ,α,∗ =∥A αGU ∥∗ +∥G V Bα∥∗ .(10)
Theorem 5.1(Variational characterization of Gauge-Muon).Let Sα(θ) =
(Aα polar(AαGU),polar(G V Bα)Bα). Then Sα(θ)∈arg max ∥Ξ∥θ,α≤1 ⟨∇L(θ),Ξ⟩, and
the attained value is χα(θ) :=∥A αGU ∥∗ +∥G V Bα∥∗ . Consequently, the Gauge-Muon update,
θ+ =θ−ηS α(θ)is exact steepest descent in the local norm in Equation 8.
5

## B-49e89eefc85d0c

candidate openreview-yHxCX7wnSJ PDF page 42

2214
2215
2216
2217
2218
2219
2220
2221
2222
2223
2224
2225
2226
2227
2228
2229
2230
2231
2232
2233
2234
2235
2236
2237
2238
2239
2240
2241
2242
2243
2244
2245
2246
2247
2248
2249
2250
2251
2252
2253
2254
2255
2256
2257
2258
2259
2260
2261
2262
2263
2264
2265
2266
2267
Under review as a conference paper at ICLR 2027
42.5
45.0
47.5
50.0
val. perplexity
dense SwiGLU, 150M
26
28
30
32
dense SwiGLU, 1B
45
50
val. perplexity
dense ReLU, 150M
28
30
32
dense ReLU, 1B
45
50
55
val. perplexity
SwiGLU MoE, 150M
28
30
32
34
SwiGLU MoE, 1B
10−2 100 102
´MLP
45
50
55
val. perplexity
ReLU MoE, 150M
10−2 100 102
´MLP
28
30
32
34
ReLU MoE, 1B
Muon
Gauge-Muon(1)
Gauge-Muon(0.5)
Path-SGD
Adam
Figure 15: Validation perplexity against the MLP learning rate for every setting and budget. Rings
mark each optimizer’s tuned rate; a dotted ring marks an optimum at the edge of its grid. The vertical
axis is cut at28%above the best perplexity in each panel.
42

## B-4ddaf930d20558

candidate openreview-yHxCX7wnSJ PDF page 23

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
Under review as a conference paper at ICLR 2027
The gate factor is therefore derived rather than chosen for symmetry: with γ=α , the gate is not
gauge-equivalent to the other blocks, but its update mobility is matched to the same invariant path
scalep 1−α
i . We writeΩ α = diag(p−α
i )from now on.
E.3 THE UPDATE AND ITS GUARANTEES
LetG g, GU , GV denote the gradients with respect toW g, U, V. The canonical covectors are
Hg = ΩαGg, H U =A αGU , H V =G V Bα,(34)
and one Gauge-Muon step for SwiGLU is
W +
g =W g −ηΩ α polar(Hg),
U+ =U−η A α polar(HU),
V + =V−ηpolar(H V )Bα.
(35)
The up and down updates are exactly those of Definition 4.1. The gate adds a third block whose
factor is invariant.
Theorem E.2(Exact monomial equivariance).Assume the same deterministic polar rule is used in
both runs and that it commutes with row and column permutations, as the support polar does. Then
the update in Equation 35 commutes exactly with the rescaling in Equation 30 and the permutation in
Equation 31. In particular, gauge-equivalent or permuted initializations produce the same function-
space trajectory in exact arithmetic.
Proof. Under Equation 30, pi is unchanged, so Ω′
α = Ωα, while A′
α =DA α and B′
α =D −1Bα
as in the ReLU case. By the chain rule, G′
g =G g, G′
U =D −1GU , and G′
V =G V D, so all three
covectors in Equation 34 are invariant. The gate update is then identical in both runs, and the up and
down updates transform as in the proof of Theorem 4.2.
Under Equation 31, the path masses are permuted, so Ω′
α =PΩ αP ⊤, A′
α =P A αP ⊤, and B′
α =
P BαP ⊤. The gradients transform as G′
g =P G g, G′
U =P G U , and G′
V =G V P ⊤, which
gives H ′
g =P H g, H ′
U =P H U , and H ′
V =H V P ⊤. Since polar(P H) =Ppolar(H) and
polar(HP ⊤) = polar(H)P ⊤, each pulled-back update permutes exactly as its parameter block.
Quotient steepest descent.The argument of Section 5 carries over block by block. The local norm
∥Ξ∥sw,θ,α = max
n

Ω−1
α Ξg


op ,


A−1
α ΞU


op ,


ΞV B−1
α


op
o
(36)
has dual
∥G∥sw,θ,α,∗ =∥Ω αGg∥∗ +∥A αGU ∥∗ +∥G V Bα∥∗ ,(37)
and, by the proof of Theorem 5.1 applied to each of the three blocks, Equation 35 is exact steepest
descent in the norm of Equation 36. The vertical space is now Vθ ={(0,ΛU,−VΛ) : Λdiagonal} ,
which has no gate component because the continuous gauge fixesWg. The loss gradient is orthogonal
to Vθ by the same argument as in Section 5, so the step is also steepest descent on the quotient by
positive up–down rescaling.
Relation to other symmetry-aware optimizers.Recent symmetry-compatible optimizers derive
block-specific updates from permutation and other architectural symmetries (Lau & Su, 2026).
The continuous up–down quotient used here is complementary: permutations reorder hidden units,
whereas positive diagonal scaling changes how each unit is factored between U and V without
changing the block function.
F PATH CAPACITY AND IMPLICIT GEOMETRY
F.1 OVERVIEW
The mobility law of Proposition 6.1 also has statistical and geometric consequences. By positive
homogeneity, fθ(x) =P
i(rivi) ReLU(ˆu⊤
i x) with unit-norm features ˆui =u i/ri, so the total path
23

## B-53569285ab5fbc

candidate openreview-yHxCX7wnSJ PDF page 38

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
Under review as a conference paper at ICLR 2027
G.5.3 MORERESULTS
Figure 14 and Table 7 summarize all 32 settings. At 150M tokens Gauge-Muon beats Muon in every
setting (−1.8%to−4.0%). At 1B tokens the result splits by architecture: Gauge-Muon stays ahead
in both mixtures ( −2.46%, −2.33%) but falls behind in both dense models ( +1.01%, +1.90%).
Activation changes the size of the delta, not its sign. Path-SGD, although gauge-equivariant, trails
Muon everywhere, so equivariance alone does not produce the gain.
−5 0 5 10
final perplexity vs Muon (%)
ReLU MoE
SwiGLU MoE
dense ReLU
dense SwiGLU
-1.82
-2.20
+14+21
-3.09
-4.03
+17
150M tokens
−5 0 5 10
final perplexity vs Muon (%)
+1.01
+1.90
-2.46
-2.33
1B tokens
Gauge-Muon(1) Adam Path-SGD
Figure 14: Final validation perplexity relative to Muon, every optimizer at its own tuned ηMLP.
Negative favours the optimizer; values beyond+12%are clipped and labelled.
Table 7: Final validation perplexity at each optimizer’s tuned rate (in parentheses ηMLP). Best of
the listed columns in bold; Gauge-Muon(0.5), run only on ReLU MoE at 1B, reaches 27.93 at .005.
Perplexities are comparable only within a row.
budget setting Muon Gauge-Muon(1) Adam Path-SGD
150M dense SwiGLU 41.47 (.015)40.72(.02) 45.98 (.001) 45.75 (2.56)
dense ReLU 43.71 (.01)42.75(.02) 49.94 (.002) 52.79 (5.12)
SwiGLU MoE 44.81 (.01)43.42(.01) 48.18 (.001) 47.15 (.64)
ReLU MoE 45.35 (.01)43.52(.02) 49.70 (.001) 52.92 (.64)
1B dense SwiGLU 25.89 (.02) 26.15 (.01)25.86(.004) 26.45 (40.96)
dense ReLU26.55(.02) 27.05 (.01) 26.94 (.002) 28.34 (10.24)
SwiGLU MoE 28.08 (.0025)27.39(.005) 28.82 (.001) 28.34 (1.28)
ReLU MoE 28.64 (.01)27.97(.005) 28.59 (.002) 30.32 (10.24)
Figure 15 shows the full learning-rate sweeps behind these numbers. Gauge-Muon’s optimum is
sharp, with perplexity rising steeply one grid step above it, whereas Muon’s is flat over a wider range
of rates; Appendix G.5.5 traces this to the compounding of path mass under Gauge-Muon’s relative
step. Path-SGD’s tuned rate varies by almost two orders of magnitude across settings, which is why
every optimizer is tuned on its own grid.
G.5.4 ABLATIONS
IngredientsFigure 16 (left) changes one ingredient at a time in the SwiGLU MoE at 150M and
measures each variant against Muon in the same setting. The gain does not depend on the exact
exponent: smaller values of α keep it. Two changes remove it. Dropping the geometric-mean
normalization turns the gain into a loss, even after retuning the learning rate, and does so in the
dense h= 256 model as well, which has no router; the normalization is therefore necessary in both
settings. Training the router with SGD instead of AdamW makes the two optimizers tie. Muon is
barely affected, while Gauge-Muon loses its whole gain.
38

## B-577c790e036a24

candidate openreview-yHxCX7wnSJ PDF page 25

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
Under review as a conference paper at ICLR 2027
Theorem F.2(Generalization under a path-mass budget).Under these assumptions,
Rn(ℓ◦ F D)≤ 4kGDR√n ,E S
"
sup
f∈F D

R(f)− bRS(f)

#
≤ 8kGDR√n .(42)
An empirical risk minimizer bf over FD, when it exists, satisfies ER(bf)−inf f∈F D R(f)≤
8kGDR/√n.
Proof. Let σj be independent Rademacher signs and σjc, c= 1, . . . , k , independent Rademacher
signs arranged as vectors σj ∈ {±1} k. Subtracting ℓ(yj,0) does not change the Rademacher
complexity, so we may assumeℓ(y j,0) = 0.
By the vector-contraction inequality (Maurer, 2016),
Eσ sup
f∈F D
X
j
σjℓ(yj, f(x j))≤
√
2GE σ sup
f∈F D
X
j
⟨σj, f(x j)⟩.
Forf= P
i ai ReLU(w⊤
i ·)∈ F D, we have
X
j
⟨σj, f(x j)⟩=
X
i
D
ai,
X
j
σj ReLU(w⊤
i xj)
E
≤Dsup
∥w∥2=1



X
j
σj ReLU(w⊤xj)



2
≤D
kX
c=1
sup
∥w∥2=1

X
j
σjc ReLU(w⊤xj)
,
where the last step uses∥z∥ 2 ≤ ∥z∥ 1.
Since ReLU is 1-Lipschitz with ReLU(0) = 0, the contraction principle (Ledoux & Talagrand, 1991)
and Jensen’s inequality give, for eachc,
Eσ sup
∥w∥2=1

X
j
σjc ReLU(w⊤xj)
 ≤2E σ



X
j
σjcxj



2
≤2
X
j
∥xj∥2
2
1/2
≤2R √n.
Combining the three steps and dividing by n gives Rn(ℓ◦ F D)≤2
√
2kGDR/ √n≤4kGDR/ √n.
Symmetrization doubles this and yields the uniform bound. For any fixed f∈ F D, empirical
optimality of bfgives
R(bf)− R(f)≤sup
g∈FD

R(g)− bRS(g)

+ bRS(f)− R(f).
The last term has zero expectation. Taking expectations and then the infimum over f proves the
estimation bound.
At fixed D the bound does not depend on the width h. The factor k comes from the crude step
∥z∥2 ≤ ∥z∥ 1 and is not optimized. By Theorem 4.2, gauge-equivalent Gauge-Muon runs have
identical P(θ t), so their capacity certificates agree throughout training. Equivariance alone, however,
does not imply a smaller certificate or a smaller population risk.
F.3 FINITE-STEP CAPACITY GROWTH
We use the exact update of Definition 4.1, without additional blockwise multipliers or damping. Let
qU
i denote row i of polar(HU) and qV
i column i of polar(HV ). Both have Euclidean norm at most
one, and
∆ui =−ηr ip−α
i qU
i ,∆v i =−ηs ip−α
i qV
i , ρ i :=ηp −α
i .(43)
The bounds below assume positive path masses at every pre-update state.
25

## B-60756f1d89cfc2

candidate openreview-yHxCX7wnSJ PDF page 21

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
Under review as a conference paper at ICLR 2027
If ρ <1 , both factors stay positive, so the path cannot cross zero in one step. When φ′(p)̸= 0 we
haveκ 2 = 1, and expanding the last line gives
p+ −p=−2ηκ p 1−α +η 2p1−2α.(24)
The first-order term has magnitude 2ηp1−α, matching the mobility scale mα(p) =p 1−α, and the
ratio of the second-order term to it is exactly
η2p1−2α
2ηp1−α = ηp−α
2 = ρ
2 .(25)
Thus the trust ratio ρ that keeps the path positive also measures how accurate the first-order
(continuous-time) mobility picture is.
D QUOTIENT GEOMETRY OFGAUGE-MUON
This section gives the derivation behind the quotient statement in Section 5.
Vertical space.Thegauge orbitthrough θ= (U, V) is {(DU, V D−1) :D∈ G} . Writing D(t) =
exp(tΛ) with Λ diagonal, its tangent directions are d
dt(D(t)U, V D(t)−1)

t=0 = (ΛU,−VΛ) , and
we call
Vθ ={(ΛU,−VΛ) : Λdiagonal}(26)
thevertical space. A vertical vector is an infinitesimal change of parameterization, not of the
represented function.
The loss differential annihilates vertical directions.Assume L(U, V) depends on the parameters
only through the represented function. Since fθ(t) is constant along the gauge curve, so is L(θ(t)),
and by the chain rule
0 = d
dt L(θ(t))

t=0
=⟨∇ U L,ΛU⟩ F − ⟨∇V L, VΛ⟩ F =⟨∇L(θ),(ΛU,−VΛ)⟩.(27)
Hence ⟨∇L(θ), Z⟩= 0 for all Z∈ V θ: the loss is flat along the orbit, so its gradient is orthogonal to
the orbit’s tangent space.
Quotient norm.A tangent vector on the quotient is an equivalence class [Ξ] = Ξ +V θ, with
quotient norm
∥[Ξ]∥θ/G,α = inf
Z∈V θ
∥Ξ +Z∥ θ,α .(28)
Because the loss differential vanishes on Vθ, maximizing its action over the ambient unit ball of
Equation 8 or over quotient classes gives the same dual value χα(θ). The projection of −Sα is
therefore a steepest-descent direction on the quotient space of functions modulo positive hidden-unit
rescaling.
Remark D.1(Comparison with vanilla Muon).Bernstein & Newhouse (2024b) view optimizers as
steepest descent under architecture-dependent norms, and in this view Muon is steepest descent under
the spectral norm. Theorem 5.1 identifies the state-dependent norm that makes this spectral geometry
compatible with hidden-unit rescaling. Relative to Muon, only the unit ball changes, through the
diagonal factors Aα, Bα; the polar oracle is the same but acts on the gauge-invariant covectors
(HU , HV ) rather than on the raw gradients, and the first-order decrease is measured by the invariant
dual valueχ α instead of the nuclear norm of the raw gradient.
Remark D.2(Comparison with natural gradient).Natural gradient (Amari, 1998) replaces the
Euclidean metric with the Fisher information and, in the ideal setting, is invariant to all smooth
reparameterizations. Gauge-Muon instead quotients out only a known architectural symmetry
and equips the remaining directions with the norm of Equation 8. That norm is a maximum of
operator norms rather than a quadratic form, so the resulting geometry is symmetry-specific and
non-Riemannian.
21

## B-64473b37284c7e

candidate openreview-yHxCX7wnSJ PDF page 16

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
Under review as a conference paper at ICLR 2027
Jinghui Yuan, Jiaxuan Zou, Shuo Wang, Yong Liu, and Feiping Nie. Nora: Normalized orthogonal
row alignment for scalable matrix optimizer.arXiv preprint arXiv:2605.03769, 2026.
Bo Zhao, Nima Dehmamy, Robin Walters, and Rose Yu. Symmetry teleportation for accelerated
optimization, 2023a. URLhttps://arxiv.org/abs/2205.10637.
Bo Zhao, Robert Mansel Gower, Robin Walters, and Rose Yu. Improving convergence and
generalization using parameter symmetries.ArXiv, abs/2305.13404, 2023b. URL https:
//api.semanticscholar.org/CorpusID:258840961.
Bo Zhao, Robin Walters, and Rose Yu. Symmetry in neural network parameter spaces.Trans. Mach.
Learn. Res., 2026, 2025. URL https://api.semanticscholar.org/CorpusID:
279402205.
16

## B-65ae7b6b85299e

candidate openreview-yHxCX7wnSJ PDF page 19

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
Under review as a conference paper at ICLR 2027
on function or parameter space. Gauge-Muon achieves invariance with anon-Riemannian, state-
dependent operator norm whose dual is a sum of nuclear norms of canonical covectors. Its update is
therefore an LMO rather than a metric inverse, and it needs no curvature estimate.
Implicit bias.Beyond the mirror-descent characterizations cited in the main text (Gunasekar et al.,
2018; Li et al., 2022), see also Gunasekar et al. (2020); the hyperbolic-entropy potentials of Ghai
et al. (2019) are consistent with the entropic-to-Euclidean interpolation of Woodworth et al. (2019);
Azulay et al. (2021). For homogeneous networks, steepest descent under different norms converges to
different margin-maximizing solutions (Lyu & Li, 2019; Chizat & Bach, 2020; Tsilivis et al., 2024);
related results characterize spectral descent and Muon (Chen et al., 2025). The capacity measure
associated with our Box–Cox mirror flow is the gauge-invariant path/variation norm (Bach, 2014;
Bach et al.).
Rescaling-aware quantization.Equivalence-preserving per-channel rescaling is a standard quanti-
zation tool. Cross-layer equalization (Nagel et al., 2019), SmoothQuant (Xiao et al., 2022), AWQ (Lin
et al., 2023) and OmniQuant (Shao et al., 2023) all move scale between adjacent operators to reduce
quantization error. We observe that per-row quantization is gauge-covariant, and we propose path-
mass-based bit allocation, which, unlike magnitude heuristics, is gauge-invariant. We view this as a
unifying lens rather than a new quantizer.
Other symmetry-aware matrix optimizers.Several recent works study symmetry and scale in
matrix optimizers from complementary angles. Intrinsic Muon (Li et al., 2026) lifts unitarily invariant
norm constraints through a Riemannian metric, which gives symmetry-preserving Muon updates
on matrix manifolds such as fixed-rank, Stiefel, Grassmann, and SPD spaces; these manifolds are
compact or unitarily invariant, whereas the hidden-unit rescaling quotient is noncompact and positive
diagonal. Singh (2026) study gauge equivariance in factored matrix models under the orthogonal
action (U, V)7→(U Q, V Q) and show that Muon respects it whereas coordinatewise adaptive
methods do not. Orthogonal transformations are isometries of the spectral norm, whereas nonuniform
positive diagonal rescalings are not, so ordinary Muon is equivariant to the orthogonal basis gauge but
not to the multiplicative ReLU gauge. Xu et al. (2026) show that Muon’s spectral geometry can have
unfavorable width dependence and derive mean-normalized row/column geometries with improved
smoothness and learning-rate transfer; width scaling is orthogonal to rescaling invariance. Nora (Yuan
et al., 2026) projects row-wise momentum onto directions orthogonal to the current weights before
row normalization, which suppresses radial jitter and gives anO(mn)Muon-like update respecting
the single-weight radial symmetry w∼λw ; the ReLU gauge (ui, vi)∼(d iui, d−1
i vi) instead
couples adjacent blocks. Closest in spirit is the unit-consistent adjoint framework (Uhlmann, 2026),
which enforces diagonal-rescaling consistency at the level of the backward operator and addresses
the same symmetry class. It asks how to make Euclidean descent consistent; we ask how to build a
Muon-style spectral LMO after moving to gauge-consistent coordinates.
C PROOFS
C.1 PROOF OFTHEOREM4.2
Proof. Assume ri, si >0 for every i, so that Aα and Bα are well defined. At the transformed point
(U ′, V ′) = (DU, V D −1) we have r′
i =d iri, s′
i =d −1
i si, and p′
i =p i, so all side norms remain
positive and
A′
α = diag

dirip−α
i

=DA α, B ′
α = diag

d−1
i sip−α
i

=D −1Bα.(13)
Since L(DU, V D−1) =L(U, V) , the chain rule gives G′
U =D −1GU and G′
V =G V D (Sec-
tion 3.2). By Equation 5, the two runs therefore feed identical matrices H ′
U =H U and H ′
V =H V to
the polar oracle. Because the polar rule is deterministic, both runs obtain the same QU = polar(HU)
andQ V = polar(HV ). Substituting into Equation 6,
U ′+ =DU−η(DA α)QU =D(U−ηA αQU) =DU +,(14)
V ′+ =V D −1 −ηQ V (D−1Bα) = (V−ηQ V Bα)D−1 =V +D−1,(15)
which is Equation 7.
19

## B-65d7f5ea593248

candidate openreview-yHxCX7wnSJ PDF page 8

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
Under review as a conference paper at ICLR 2027
50
75
100
125
150
175
validation perplexity
SwiGLU MoE
112 150
45
48
51
0 50 100 150
−6
0
6
12
18
¢ from Muon (%)
ReLU MoE
112 150
45
50
55
0 50 100 150
Dense SwiGLU
112 150
44
48
0 50 100 150
Dense ReLU
112 150
42
48
54
0 50 100 150 0 10
final ppl vs Muon (%)
Dense ReLU
Dense SwiGLU
ReLU MoE
SwiGLU MoE
-3.09
-4.03
+17
-1.82
-2.20
+14
+21
Final vs Muon
tokens (M)
Muon Gauge-Muon(1) Path-SGD Adam
Figure 3: Training curves in the 150M-token setting. : validation perplexities, each at its tuned
rate. The lower row is the difference from Muon at matched steps.Right: final validation perplexity
relative to Muon. Large validation perplexity are clipped and labelled.
25
30
35
40
45
50
55
validation perplexity
SwiGLU MoE
750 1000
28.5
30.0
0 250 500 750 1000
−3
0
3
6
9
¢ from Muon (%)
ReLU MoE
750 1000
28.0
28.8
29.6
0 250 500 750 1000
Dense SwiGLU
750 1000
26.4
27.2
0 250 500 750 1000
Dense ReLU
750 1000
27.0
28.5
30.0
0 250 500 750 1000
 0 10
final ppl vs Muon (%)
Dense ReLU
Dense SwiGLU
ReLU MoE
SwiGLU MoE
-2.46
-2.33
+1.01
+1.90
Final vs Muon
tokens (M)
Muon Gauge-Muon(1) Path-SGD Adam
Figure 4: Training curves in the 1B-token setting.
validation perplexity by 1.8% to 4.0%. At 1B tokens, the result splits by architecture. In both
mixture-of-experts models, Gauge-Muon(1) stays ahead of Muon (−2.5% and −2.3%), and the gap
is still widening at the end of training. In both dense models, it falls behind we return to this case
below.
The training curves share one pattern that Gauge-Muon(1) starts behind Muon, because its relative
step ramps up from a small initialization, and then overtakes it in every setting except the dense
models at 1B. The activation (SwiGLU or ReLU) changes the size of the difference but never its sign.
Path-SGD, although also gauge-equivariant, trails Muon in every setting. Appendix G.5.3 gives the
full results.
Width ablationSince the dense and mixture models differ mainly in the width of their feed-forward
blocks, we vary the hidden width of the dense model to understand why Gauge-Muon trails Muon in
the dense setting at 1B tokens (Figure 5, top). At 150M tokens, Gauge-Muon(1) leads Muon at every
width. At 1B tokens, its advantage shrinks as the block widens and turns into a deficit once the width
approaches the model dimension. Narrow blocks and short budgets therefore favor Gauge-Muon.
Mixture of expertsModern mixture-of-experts models use many experts that are each narrower
than the model dimension, which is the regime the width ablation favors. We therefore vary the
number of experts while holding the total feed-forward parameters fixed, so that more experts
8

## B-6de2fee1768797

candidate openreview-yHxCX7wnSJ PDF page 41

2160
2161
2162
2163
2164
2165
2166
2167
2168
2169
2170
2171
2172
2173
2174
2175
2176
2177
2178
2179
2180
2181
2182
2183
2184
2185
2186
2187
2188
2189
2190
2191
2192
2193
2194
2195
2196
2197
2198
2199
2200
2201
2202
2203
2204
2205
2206
2207
2208
2209
2210
2211
2212
2213
Under review as a conference paper at ICLR 2027
QAT implementation.During quantization-aware training, each forward pass substitutes
WSTE =W+ stopgrad(W q −W),(70)
so its value is quantized while its derivative with respect to the float32 master weight is the identity.
Gauge scales and quantization scales are detached. Quantization is performed in float32 with autocast
disabled, after which the surrounding autocast may use bf16 for the matrix multiplication. A non-STE
quantizer is active only in evaluation mode; enabling hard rounding during training would make the
weight gradient zero almost everywhere.
The same hook is attached to every (Wup, Wdown) pair in a transformer MLP and independently
to every expert in a mixture-of-experts layer. The homogeneity degree is taken from the model
configuration (ν= 1 for ReLU and SwiGLU, ν= 2 for squared ReLU), since an incorrect degree
silently breaks function preservation. For SwiGLU the continuous gauge acts on (Wup, Wdown) only;
Wgate is therefore quantized separately without gauge fixing. The optimizer continues to update the
master parameters and is otherwise unaware of the quantizer.
G.6.1 EXPERIMENTS
Setup.We use the bias-free two-layer ReLU network of width 512 on FashionMNIST, which
has the shape of a transformer feed-forward block, and initialize it in the gauge di = 10 qzi with
q∈ {0,1,2} , as in Appendix G.1. Every optimizer is trained for 30 epochs with a cosine schedule;
its learning rate is tuned on three seeds for each quantizer configuration and evaluated on three fresh
seeds. We report W4 per-channel quantization in the main comparison; W8 and groupwise grids
show the same pattern with smaller drops. Because moving a checkpoint along its gauge orbit is
exactly function preserving, the float32 network is identical before and after gauge fixing.
Post-training quantization.Figure 17 (left) shows that the damage of rounding a checkpoint as
trained grows with q, and grows fastest for the gauge-equivariant optimizers. This is the expected
cost of equivariance: Gauge-Muon and Path-SGD keep the representative they were given, so an
unbalanced initial gauge is still present at the end of training, whereas Muon and Adam partly
rebalance it. Gauge fixing before rounding removes this dependence for every optimizer and costs
nothing in float32 accuracy. With a quantizer that sees only a canonical representative, what remains
is the quantization error of the function itself.
Quantization-aware training.Figure 17 (right) and Table 9 train through the quantizer. With
the gauge-fixed quantizer, Gauge-Muon reaches the same accuracy at q= 2 as at q= 0 (within
0.2 percentage points), while Muon and Adam lose accuracy as the initial gauge is perturbed. The
quantizer is now covariant, so the remaining sensitivity of Muon comes from the optimizer itself:
combining a covariant quantizer with an equivariant optimizer makes the whole QAT pipeline
independent of the initial gauge. Path-SGD is also unaffected by q, but trails the spectral methods
at both values. Gauge fixing matters most for a per-tensor grid: without it, QAT at q= 2 fails for
both equivariant optimizers, since a single scale must cover the widely spread rows and columns they
preserve, while with equalization Gauge-Muon again matches itsq= 0accuracy.
Table 9: W4 quantization-aware training on FashionMNIST: test accuracy (%) for each quantizer
configuration and initial gauge q, mean over three seeds. Standard errors are at most 0.23 except
Gauge-Muon(0.5) with a per-tensor grid and no gauge at q= 2 (2.07). Best in each column in bold.
Path-SGD’s selected rate lies at the top of its grid.
per-channel per-tensor
no gaugevcolno gauge equalized
optimizerq= 0q= 2q= 0q= 2q= 0q= 2q= 0q= 2
Muon 90.05 88.73 90.19 89.33 90.0186.6190.06 88.93
Gauge-Muon(1)90.22 89.43 90.4090.2390.0910.00 90.11 90.08
Gauge-Muon(0.5) 90.13 89.20 90.1890.2489.74 70.9590.25 90.13
Path-SGD 88.76 87.66 88.82 88.69 88.73 10.00 88.74 88.67
Adam 89.51 88.76 89.66 89.31 89.35 84.40 89.49 89.23
41

## B-70b4c52241e175

candidate openreview-yHxCX7wnSJ PDF page 15

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
Under review as a conference paper at ICLR 2027
Chongjie Si, Debing Zhang, and Wei Shen. Adamuon: Adaptive muon optimizer.arXiv preprint
arXiv:2507.11005, 2025.
Devender Singh. The loss does not see the basis, but adam does.arXiv preprint arXiv:2608.05136,
2026.
Pierre Stock, Benjamin Graham, R´emi Gribonval, and Herv´e J´egou. Equi-normalization of neural
networks.arXiv preprint arXiv:1902.10416, 2019.
Nikolaos Tsilivis, Eitan Gronich, Julia Kempe, and Gal Vardi. Flavors of margin: Implicit bias
of steepest descent in homogeneous neural networks.ArXiv, abs/2410.22069, 2024. URL
https://api.semanticscholar.org/CorpusID:273662400.
Jeffrey Uhlmann. Unit-consistent (uc) adjoint for gsd and backprop in deep learning applications.
arXiv preprint arXiv:2601.10873, 2026.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz
Kaiser, and Illia Polosukhin. Attention is all you need, 2023. URL https://arxiv.org/
abs/1706.03762.
Andrey Veprikov, Arman Bolatov, Aleksandr Bogdanov, Samuel Horv´ath, Aleksandr Beznosikov,
Martin Tak´aˇc, and Slavomir Hanzely. Preconditioned norms: A unified framework for steepest
descent, quasi-newton and adaptive methods.arXiv preprint arXiv:2510.10777, 2025.
Nikhil Vyas, Depen Morwani, Rosie Zhao, Itai Shapira, David Brandfonbrener, Lucas Janson, and
Sham Kakade. Soap: Improving and stabilizing shampoo using adam for language modeling. In
International Conference on Learning Representations, volume 2025, pp. 93423–93444, 2025.
Blake E. Woodworth, Suriya Gunasekar, J. Lee, Edward Moroshko, Pedro H. P. Savarese, Itay
Golan, Daniel Soudry, and Nathan Srebro. Kernel and rich regimes in overparametrized models.
ArXiv, abs/2002.09277, 2019. URL https://api.semanticscholar.org/CorpusID:
211252492.
Guang-Xuan Xiao, Ji Lin, Micka¨el Seznec, Hao Wu, Julien Demouth, and Song Han. Smoothquant:
Accurate and efficient post-training quantization for large language models.ArXiv, abs/2211.10438,
2022. URLhttps://api.semanticscholar.org/CorpusID:253708271.
Han Xiao, Kashif Rasul, and Roland V ollgraf. Fashion-mnist: a novel image dataset for benchmarking
machine learning algorithms.arXiv preprint arXiv:1708.07747, 2017.
Ruihan Xu, Jiajin Li, and Yiping Lu. On the width scaling of neural optimizers under matrix operator
norms i: Row/column normalization and hyperparameter transfer.arXiv preprint arXiv:2603.09952,
2026.
Ge Yang, Edward Hu, Igor Babuschkin, Szymon Sidor, Xiaodong Liu, David Farhi, Nick Ryder,
Jakub Pachocki, Weizhu Chen, and Jianfeng Gao. Tuning large neural networks via zero-shot
hyperparameter transfer.Advances in Neural Information Processing Systems, 34:17084–17097,
2021.
Greg Yang and Edward J Hu. Tensor programs iv: Feature learning in infinite-width neural networks.
InInternational Conference on Machine Learning, pp. 11727–11737. PMLR, 2021.
Greg Yang, James B Simon, and Jeremy Bernstein. A spectral condition for feature learning.arXiv
preprint arXiv:2310.17813, 2023.
Jui-Nan Yen, Si Si, Zhao Meng, Felix Yu, Venkata Sai Surya Subramanyam Duvvuri, Inderjit Dhillon,
Cho-Jui Hsieh, and Sanjiv Kumar. Lora done rite: Robust invariant transformation equilibration
for lora optimization. InInternational Conference on Learning Representations, volume 2025, pp.
75815–75834, 2025.
Kang You, Zekai Xu, Chen Nie, Zhijie Deng, Qinghai Guo, Xiang Wang, and Zhezhi He. SpikeZIP-
TF: Conversion is all you need for transformer-based SNN. InProceedings of the 41st International
Conference on Machine Learning, volume 235 ofProceedings of Machine Learning Research, pp.
57367–57383. PMLR, 21–27 Jul 2024.
15

## B-7f6319a2e3262f

candidate openreview-yHxCX7wnSJ PDF page 1

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
Under review as a conference paper at ICLR 2027
MUON ON THEQUOTIENT: GAUGE-EQUIVARIANTDE-
SCENT FORHOMOGENEOUSNETWORKS
Anonymous authors
Paper under double-blind review
ABSTRACT
Positively homogeneous networks, including ReLU networks and the SwiGLU
blocks of modern transformers, have a rescaling symmetry. That is, scaling up the
incoming weights of a hidden unit and scaling down its outgoing weights leaves
the function unchanged. Orthogonalized optimizers such as Muon do not respect
this symmetry, thereby equivalent parameterizations of the same function receive
different updates, and a function-preserving rescaling can lead Muon to a sharper
basin with a higher loss. We introduce Gauge-Muon, a family of optimizers that
keeps Muon’s orthogonalized update but applies it to gradients rescaled by per-unit
factors computed from the weights, and then undoes the rescaling. Every member
of the family is exactly equivariant under hidden-unit rescaling at every finite step
size, and performs exact steepest descent in the quotient geometry that identifies
all equivalent parameterizations. We further show how the family’s exponent
allocates functional motion across hidden units, and derive an invariant capacity
bound on generalization. Empirically, Gauge-Muon is unaffected by rescalings that
degrade Muon and improves on Muon in image classification and GPT-2 language
modeling, with the most consistent gains in mixture-of-experts models with narrow
experts.
1 INTRODUCTION
Orthogonalized optimizers such as Muon (Jordan et al., 2024) have become an important alternative
to Adam (Kingma & Ba, 2014) for training deep networks. Iterative approximations such as Newton–
Schulz iterations (Bj¨orck & Bowie, 1971; Amsel et al., 2026) make Muon cheap enough to use in
LLM pretraining (Liu et al., 2025; Bai et al., 2026). The core idea of Muon is to perform steepest
descent under the spectral norm (Bernstein & Newhouse, 2024b). More generally, one can design an
optimizer by choosing a norm on parameter space and solving the corresponding linear minimization
oracle (Large et al., 2024; Bernstein & Newhouse, 2024a; Pethick et al., 2025). This view carries an
implicit assumption that the weight matrix is the right object on which to place a norm.
ReLU networks and the SwiGLU feed-forward blocks of modern transformers (Vaswani et al., 2023;
Shazeer, 2020) have a rescaling symmetry. That is, scaling up the incoming weights of a hidden
unit and scaling down its outgoing weights by the same factor leaves the function unchanged. In
a layer, this corresponds to multiplying the two weight matrices by a positive diagonal matrix and
its inverse. The polar map of Muon does not commute with such rescalings, thereby Muon assigns
different updates to different parameterizations of thesamefunction. These rescalings can occur in
practice from initialization and from the per-channel scale folding used in quantization (Nagel et al.,
2019; Xiao et al., 2022). After a function-preserving rescaling at initialization, Muon converges to a
sharper basin with a higher loss (Figure 1, Appendix G.1).
In this paper, we ask:can we design an optimizer that keeps Muon’s spectral oracle, the polar map,
while guaranteeing that its updates depend only on the function a network represents and not on
how that function is parameterized?To answer this, we introduce preconditioners that transform
together with the rescaling. They are built from the norms of each hidden unit’s incoming and
outgoing weights and from its path mass which is the product of these two norms. This path mass is
invariant under any rescaling. Applying the preconditioners to the gradients yields covectors that are
identical across all parameterizations of the same function. To this end, we introduceGauge-Muonby
applying the polar map to these covectors and maps the result back through the same preconditioners
1
Reviewers:pleasereadtheReviewerGuidelines(iclr.cc/Conferences/2027/ReviewerGuidelines)andtheAIPolicyforReviewers(iclr.cc/Conferences/2027/AIPolicyForReviewers).
If you used AI to expand, edit, or polish your review, please provide the input text to the LLM. Better still, consider skipping the LLM and submitting your original text: we,
and the authors, are much more interested in your unedited thoughts than in what an LLM has to say. AI-assisted or not, you are putting your name and reputation behind
your review: LLM-generated falsehoods, hallucinations or misrepresentations are subject to disciplinary action, which may include desk-rejecting all papers you have authored.

## B-88226186f23101

candidate openreview-yHxCX7wnSJ PDF page 24

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
Under review as a conference paper at ICLR 2027
mass P(θ) = P
i pi is the sum of the Euclidean norms of the output coefficients. It is gauge invariant
and certifies the capacity of the current representation, independently of how each unit is balanced
betweenUandV.
Theorem F.1(Invariant capacity budget, informal).Let ∥x∥2 ≤R and let the loss be G-Lipschitz
in the prediction f(x)∈R k. Uniformly over networks with P(θ)≤D , the expected generalization
gap is at most 8kGDR/√n. Moreover, if a T -step Gauge-Muon run with α= 1 , whose horizon and
initialization are fixed independently of the sample, satisfies the trust boundηp −1
i,t ≤ρ 0, then
P(θ T )≤P(θ 0)+(2+ρ0)ηhT,E

R(fθT )−bRS(fθT )

≤ 8kGR√n

P(θ 0)+(2+ρ0)ηhT

.(38)
The exponent that equalizes first-order functional mobility therefore also gives every active path
the same worst-case capacity-growth allowance, and early stopping acquires a direct meaning as
control of an invariant capacity budget. The guarantee is conservative: the statistical bound is width
independent at fixed P , but the trajectory-based budget grows with hT , and neither claims that α= 1
always generalizes best.
The exponent also selects the geometry in which paths compete. With frozen feature directions and
the polar demand idealized by the loss gradient, the reduced dynamics˙pi =−p 1−α
i ∂iF(p) are exactly
mirror flow under a Box–Cox potential with curvature pα−1. The range 0≤α≤1 interpolates
between entropic (α= 0 ) and Euclidean (α= 1 ) path geometry, and, conditional on positivity and
convergence, the limiting interpolator is the Bregman projection of the initialization. Euclidean
gradient flow, in contrast, induces a path mobility that depends on the gauge-dependent imbalance
∥ui∥2
2 − ∥vi∥2
2, which a function-preserving rescaling can distort without bound. Gauge-Muon thus
makes both the capacity certificate and the reduced implicit geometry properties of the invariant paths.
The rest of this section gives the precise statements, proofs, and limitations.
This section connects the invariant path coordinates of Gauge-Muon to statistical capacity and
optimization geometry. We first bound generalization by the total path mass and control its growth
under finite Gauge-Muon steps. We then characterize the mirror geometry of an idealized path flow
and quantify how Euclidean gradient flow depends on the choice of gauge.
Throughout, we consider the ReLU layer of Equation 2 with vector output, fθ(x) =Ph
i=1 vi ReLU(u⊤
i x)∈R k, and the magnitudes of Equation 3: ri =∥u i∥2, si =∥v i∥2, and
pi =r isi. The scalar-output case isk= 1, wheres i =|v i|. The total path mass is
P(θ) :=
hX
i=1
pi =
hX
i=1
∥ui∥2 ∥vi∥2 .(39)
F.2 PATH MASS AS A CAPACITY CERTIFICATE
Path normalization.According to positive homogeneity of ReLU, we have
fθ(x) =
X
i
ai ReLU(ˆu⊤
i x),ˆu i =u i/ri, a i =r ivi ∈R k, P(θ) =
X
i
∥ai∥2 .(40)
We omit any units withr i = 0. We define the variation norm
γ1(f) := inf



X
j
∥aj∥2 :f=
X
j
aj ReLU(w⊤
j ·), a j ∈R k,∥w j∥2 = 1


 .(41)
Equation 40 certifies γ1(fθ)≤P(θ) , and P is invariant under (ui, vi)7→(d iui, d−1
i vi) for di >0 .
The certificate refers to the current representation: distinct representations of the same function can
have different total path mass.
Setting.Let FD contain all finite sumsP
j aj ReLU(w⊤
j ·) with ∥wj∥2 = 1 andP
j ∥aj∥2 ≤D ,
for a fixed D. For an i.i.d. sample S={(x j, yj)}n
j=1, let R(f) =Eℓ(y, f(x)) and bRS(f) =
n−1P
j ℓ(yj, f(x j)). Assume ∥x∥2 ≤R almost surely, ℓ(y,·) is G-Lipschitz with respect to the
Euclidean norm onR k, andE|ℓ(y,0)|<∞.
24

## B-89e4faf565264e

candidate openreview-yHxCX7wnSJ PDF page 39

2052
2053
2054
2055
2056
2057
2058
2059
2060
2061
2062
2063
2064
2065
2066
2067
2068
2069
2070
2071
2072
2073
2074
2075
2076
2077
2078
2079
2080
2081
2082
2083
2084
2085
2086
2087
2088
2089
2090
2091
2092
2093
2094
2095
2096
2097
2098
2099
2100
2101
2102
2103
2104
2105
Under review as a conference paper at ICLR 2027
SeedsAcross three seeds (Figure 16, right), the worst Gauge-Muon seed ( 44.49) still beats the best
Muon seed (44.81); the mean gain is2.92%.
ComparabilityMuon’s rectangular scale factor max(1,rows/cols) 1/2 equals 1 for an expert’s
384×768 incoming matrix but 2 for the dense 3072×768 . Every optimizer within the mixture
shares that factor, so comparisonsinsidea panel are unaffected, but mixture perplexities are not
directly comparable to dense ones.
G.5.5 WHY NARROW BLOCKS AND SHORT BUDGETS FAVORGAUGE-MUON
In this section, we expand our inverstiation in Figure 6.
Relative steps make path mass compoundGauge-Muon(1) moves every hidden unit by a fixed
fraction of its own norm, so by Lemma F.4 path mass grows exponentially in the integrated learning
rate; Muon’s step has a fixed absolute size, so its path mass grows polynomially (Figure 6(a)). Every
tuned Gauge-Muon setting sits one grid step below the rate at which growth explodes and perplexity
degrades, whereas Muon’s optimum is flat over a four- to eight-fold range. Since the admissible
growth caps ηT , Gauge-Muon’s tuned rate halves from 150M to 1B tokens in the settings tuned at
both budgets, and at 1B it is at most half of Muon’s in every dense setting (Table 8). The smaller
rate delays the crossing from 40–130M tokens at 150M to 500–900M at 1B, and to 1.77B for wide
experts trained to 2B.
The aspect ratio sets Muon’s allocationLet G be the h×d gradient of a block’s incoming matrix.
For h≤d the polar factor ofG has orthonormal rows, so Muon moves every unit by the same absolute
amount. For h > d its squared row norms are the leverage scores of G, which track the gradient row
norms (correlation 0.9–1.0), so Muon moves units with larger gradients more. Gauge-Muon(1) gives
every unit the same relative motion at every width. Hence Muon’s spread of log path mass is larger in
wide blocks than in narrow ones, while Gauge-Muon’s stays small everywhere (Figure 6(b), Table 8).
Our reading is that uniform relative motion is the right prior when every unit must carry part of the
function, and that gradient-weighted allocation builds a working sub-network faster when the block
is wide; the geometry follows from the polar factor, but no result in the paper says which geometry
trains faster.
Table 8: Tuned rates, concentration and gap trajectory in the 1B-token settings. Spread is Vari logp i
at the end of training; the crossing is the first point after which the gap stays negative.
tunedηMuon
Settingsh/dMuon Gauge-Muon spread crossing final gap
denseh= 256 0.33.01.005.016577M−1.2%
denseh= 512 0.67.02.005.015891M−0.1%
SwiGLU MoE8×256 0.33.0025.005.008498M−2.5%
ReLU MoE8×384 0.50.01.005.021603M−2.3%
denseh= 2048 2.67.02.01.032never+1.0%
ReLUh= 3072 4.0.02.01.036never+1.9%
The two effects are separableThe ramp alone does not explain the wide-block deficit: at 1B
tokens Gauge-Muon’s path mass reaches one at a similar time in narrow and wide blocks (262–511M
tokens), yet only the narrow blocks cross. Conversely, the width effect exists at equal rates: at 150M
tokens with both optimizers at η=.01 , the gap is −2.0%, +1.1% and +4.9% at h= 256 , 512 and
2048. Tuned rates hide this at 150M because the short budget lets Gauge-Muon run at a rate at least
as large as Muon’s.
The differences arise earlyMuon’s absolute steps settle each unit’s ratio of incoming to outgoing
norm within the first 10–25% of training. Consistently, resuming a Muon checkpoint at 100M tokens
for 50M more gives the same perplexity with either optimizer at h= 256 , 768 and 2048 (within
0.15%). The gaps in Figure 6(c) are made while the network grows out of its initialization.
39

## B-8e8287ad07c901

candidate openreview-yHxCX7wnSJ PDF page 32

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
Under review as a conference paper at ICLR 2027
accurate polar approximation primarily improves optimization quality and path utilization, while
seven Newton-Schulz iterations are sufficient to recover nearly all of the benefit of the exact SVD.
Reduced-precision computation is similarly robust. Using bf16 autocast gives a loss of .2775, close
to both the seven-step Newton-Schulz and exact-SVD variants, although its effective path utilization
is moderately lower at Neff/h=.948 . Across all numerical variants, the loss gap between the
gauge-equivalent q= 0 and q= 4 parameterizations remains small, ranging from 2.0×10 −4 to
1.0×10 −3. This indicates that the practical numerical approximations preserve the gauge robustness
of Gauge-Muon even when the resulting parameter trajectories are not numerically identical.
Table 1: Numerical robustness of Gauge-Muon at α= 1 and η=.003 . Probe drift denotes the
relative prediction deviation between pairedq= 0andq= 4runs.
variantq= 0loss loss gap probe driftN eff/h
Newton–Schulz (3 steps) .29602.0×10 −4 0.025 0.880
Newton–Schulz (7 steps) .27781.0×10 −3 0.051 0.981
exact SVD .27655.9×10 −4 0.049 0.982
bf16autocast .27757.0×10 −4 0.044 0.948
G.4 IMAGECLASSIFICATIONTASK
Table 2 reports the learning-rate grids that we used for model selection.
Table 2: Learning-rate search grids for the image-classification experiments, given as span (number
of grid points) on the {1,3} ×10 −k ladder. Muon and both Gauge-Muon variants share one grid per
cell. The fine-tuning setting shifts every grid down by two steps.
Seting Muon, Gauge-Muon AdamW Path-SGD
FashionMNIST MLP0.0003–0.03(5)0.0001–.03(6).1–30(6)
CIFAR-100 ResNet-180.0003–0.03(5)0.0001–.01(5)0.03–10(6)
CIFAR-100 ResNet-500.0003–.03(5)0.0001–.01(5).01–10(7)
SVHN ResNet-180.0003–.03(5)0.0001–.01(5)0.03–10(6)
SVHN ResNet-500.0003–.03(5)0.00003–.01(6)0.003–10(8)
CIFAR-100 ViT-S/16 FT0.00003–0.003(5)0.00001–.001(5)0.00001–.03(8)
CIFAR-100 ViT-B/16 FT0.00003–0.003(5)0.00001–.001(5)0.00001–.03(8)
G.4.1 ARCHITECTURES
We provide the architecture used in our image classification task. We use 2-layer ReLU classifier
f(x) =VReLU(U x), U∈R h×din , V∈R C×h ,(62)
Both matrices use Kaiming-uniform initialization with no bias. We use the hidden width as h= 512 .
For width ablation experiments, we sweepsh∈ {128,256,512,1024,2048}.
MLP (FashionMNIST)The classifier is applied directly to raw pixels, so din = 784 and C= 10 .
ResNet-18 and ResNet-50 (CIFAR-100, SVHN)The colour datasets enter through afrozen
ImageNet-pretrained ResNet. We trained only the two-layer head and freeze the backbone.
ViT-S/16 and ViT-B/16 (CIFAR-100)We perform full fine-tuning ViTfrom the SpikeZIP-TF
ReLU checkpoints2 (You et al., 2024). In this version, GELU activations were replaced by ReLU
before further ImageNet-1k training (82.3% top-1 for ViT-S/16,83.5% for ViT-B/16). The pretrained
classifier is removed and randomly initialized. For data augmentation, we augmented CIFAR-100
2https://huggingface.co/XianYiyk/SpikeZIP-TF-vit-base-patch16-relu and
https://huggingface.co/XianYiyk/SpikeZIP-TF-vit-small-patch16-relu
32

## B-937c30c9b64d4d

candidate openreview-yHxCX7wnSJ PDF page 37

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
Under review as a conference paper at ICLR 2027
For the ReLU variant,the homogeneous theory covers directly, and we set the mutiplicative factor
between hidden unitand hidden dimension as h/d= 4 (h= 3072 ). For the SwiGLU variant, we
usedh/d= 8/3, soh= 2048because it has an extra gate matrixW gate alongsideW up.
Mixture of expertsThe mixture of experts (MoE) settings replace each dense MLP with eight
experts under top-1 routing. The ReLU expert width is 384 while the SwiGLU expert width is 256.
This ensures the MoE settings have the same parameters as the dense settings. The router is a plain
matrix trained with Adam.
For load balancing, we use a Switch-style load-balancing auxiliary (Fedus et al., 2022) to add to the
optimization objective at weight 0.05. This is because at weight 0 and at 10−3 routing collapses onto
a single expert.
Table 4: Feed-forward architecture of the language-model settings. All setting share the GPT-2 small
backbone (12 layers, dmodel = 768, 12 heads, context 512, tied embeddings). h is the hidden width
of one MLP, or of one expert in the mixture settings.
Setting activationhgauged pairs note
dense ReLU3072 12h/d= 4
dense SwiGLU2048 12h/d= 8/3, gate shares the hidden index
mixture ReLU384 96 8experts, top-1
mixture SwiGLU256 96 8experts, top-1
G.5.2 TRAINING SETUP AND OPTIMIZER
All runs train on FineWeb-Edu, tokenised with the GPT-2 BPE, at a batch of 64 sequences with 4
gradient-accumulation steps and a context of 512, giving 131,072 tokens per step. In our experiments,
we consider two token budget settings: low-budget (150M tokens) and high-budget (1B tokens). The
corresponding trainig steps are 1,100 and 7,600 steps. The optimizer scheduler is cosine with 500
warmup steps, gradient clipping at0.5.
We split parameters by their role, as summarized in Table 5. As we focus on studying the gauge
symmetry in feed-forward blocks. Everything else is set with the same settings.
Table 5: Assignment of parameter groups to optimizers. Only the first row changes between arms; the
other two are identical in every run, so the swept rateη MLP governs the feed-forward blocks alone.
parameter group optimizer learning rate settings
MLP pairs (expert pairs in MoE) the swept armη MLP, tuned see Table 6
attention matrices Muon10 −2, fixed momentum.95, Newton–Schulz5
embeddings, LayerNorm, router AdamW10 −3, fixedβ= (.8, .999), weight decay=.1
Table 6 lists the six settings of our experiments for language model. We try our best to tune learning
rates for each setting rather than sharing a default learning rate. Here, we note that Path-SGD’s ratio
match rescales its update to the raw gradient norm.
Table 6: The six arms, their settings on the MLP pairs, and the range of rates they select across the
settings in this section. The selected rates span four decades, which is why a shared grid would make
the comparison meaningless.
arm settings on the MLP pairs selectedη MLP
Muon momentum.95, Newton–Schulz5.0025–.02
Gauge-Muonα= 1geometric-mean gauge.005–.02
Gauge-Muonα=.5geometric-mean gauge.005
Path-SGD momentum.9, ratio match.64–40.96
Adamβ= (.8, .95), no weight decay.001–.004
37

## B-9af9d45e15a46b

candidate openreview-yHxCX7wnSJ PDF page 17

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
Under review as a conference paper at ICLR 2027
TABLE OFAPPENDIXCONTENTS
A Notations 18
B Extended Related Work 18
C Proofs 19
C.1 Proof of Theorem 4.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
C.2 Proof of Theorem 5.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
C.3 Proof of Proposition 6.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
C.4 Exact one-path reduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
D Quotient geometry of Gauge-Muon 21
E Gauge-Muon for SwiGLU networks 22
E.1 Model and exact symmetry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
E.2 Choosing the gate factor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
E.3 The update and its guarantees . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
F Path capacity and implicit geometry 23
F.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
F.2 Path mass as a capacity certificate . . . . . . . . . . . . . . . . . . . . . . . . . . 24
F.3 Finite-step capacity growth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
F.4 Reduced path dynamics and Box–Cox geometry . . . . . . . . . . . . . . . . . . . 26
F.5 Gauge dependence of Euclidean gradient flow . . . . . . . . . . . . . . . . . . . . 27
F.6 Share and log-variance balance laws . . . . . . . . . . . . . . . . . . . . . . . . . 28
G Experimental Results 28
G.1 Why Muon breaks symmetry in ReLU networks . . . . . . . . . . . . . . . . . . . 29
G.2 Theoretical validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
G.3 Numerical robustness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
G.4 Image Classification Task . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
G.5 Language Modeling Task . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
G.6 Gauge-fixed quantization-aware training . . . . . . . . . . . . . . . . . . . . . . . 40
17

## B-a70866e7c48945

candidate openreview-yHxCX7wnSJ PDF page 35

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
Under review as a conference paper at ICLR 2027
10 20 30
64
66
68
validation accuracy (%)
CIFAR-100 / ResNet-18
10 20 30
70
72
74
CIFAR-100 / ResNet-50
10 20 30
70
72
74
validation accuracy (%)
SVHN / ResNet-18
10 20 30
62
64
66
68
SVHN / ResNet-50
10 20 30
86
88
90
validation accuracy (%)
FashionMNIST / MLP
2 4 6 8 10
epoch
84
86
88
CIFAR-100 / ViT-S/16 ReLU FT
2 4 6 8 10
epoch
75
80
85
validation accuracy (%)
CIFAR-100 / ViT-B/16 ReLU FT
Muon
Gauge-Muon(1)
Gauge-Muon(0.5)
Path-SGD
Adam
Figure 12: The validation accuracy per epoch at each method’s selected learning rate, with standard-
error bands over seeds. Each panel is scaled to its converged region, so the first epochs run off the
bottom of the axes.
Comparing to PathSGD and AdamOn FashionMNIST, spectral methods (Gauge-Muon and
Muon) make training loss to about 4×10 −4 while Path-SGD and Adam stall at 0.210 and 0.132. On
the ViT setting, Path-SGD is underperformed, ending at a training loss of .231 against 8.4×10 −3
for Gauge-Muon at α= 1 . This is a clear evidence that our Gauge-Muon wins over PathSGD in this
benchmark.
35

## B-a9ee4e1da180d4

candidate openreview-yHxCX7wnSJ PDF page 22

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
Under review as a conference paper at ICLR 2027
E GAUGE-MUON FORSWIGLUNETWORKS
Transformer feed-forward blocks commonly use a gated SwiGLU layer (Shazeer, 2020) rather than
the ReLU layer of Equation 2. The SiLU activation (Elfwing et al., 2018), SiLU(z) =z/(1 +e −z),
is not positively homogeneous, so replacing ReLU by SiLU and keeping the ReLU gauge would be
incorrect. Instead, we re-derive the symmetry from the SwiGLU computation itself and then extend
Definition 4.1 one block at a time.
E.1 MODEL AND EXACT SYMMETRY
We keep the notation of Section 3.2 and add a gate projection. A SwiGLU block is
F(x) =V(SiLU(W gx)⊙(U x)) =
hX
i=1
vi SiLU(g⊤
i x) (u⊤
i x),(29)
where U∈R h×d is the up projection (incoming matrix), V∈R k×h is the down projection (outgoing
matrix), Wg ∈R h×d is the gate projection with rows g⊤
i , and ⊙ denotes elementwise multiplication.
As in Equation 3, we set ri =∥u i∥2, si =∥v i∥2, and pi =r isi. The gate norm ∥gi∥2 does not enter
pi: because SiLU is not homogeneous, the gate scale generally changes the represented function.
Continuous symmetry.For a positive diagonalD, the map
(Wg, U, V)7→(W g, DU, V D −1)(30)
leaves F unchanged, since SiLU(Wgx)⊙(DU x) =D(SiLU(W gx)⊙(U x)) and D cancels against
D−1 in V D−1. The gate admits no such rescaling, because SiLU(Dz)̸=DSiLU(z) in general.
The ReLU gauge therefore survives only on the linear up branch and the down projection, and the
path massp i remains an exact invariant.
Permutation symmetry.For any permutation matrixP, the map
(Wg, U, V)7→(P W g, P U, V P ⊤)(31)
also preserves F . Together with Equation 30, it generates a monomial action on the hidden units.
The same permutation symmetry holds for the ReLU layer.
E.2 CHOOSING THE GATE FACTOR
For the up and down blocks, we reuse the covariant factors of Section 4, Aα = diag(r ip−α
i ) and
Bα = diag(sip−α
i ). The gate is not rescaled by the gauge, so its factor must itself be gauge invariant.
We therefore take Ωγ = diag(p−γ
i ) for some exponent γ and fix γ by requiring that all three blocks
move the function at the same path scale. This extends Proposition 6.1.
The first-order variation of the contribution of uniti,f i(x) =v i SiLU(g⊤
i x)(u⊤
i x), is
δfi(x) =δv i SiLU(g⊤
i x)(u⊤
i x)| {z }
down
+v i SiLU(g⊤
i x)(δu⊤
i x)| {z }
up
+v i SiLU′(g⊤
i x)(u⊤
i x)(δg ⊤
i x)| {z }
gate
.(32)
Proposition E.1(Three-branch functional mobility).Suppose one step moves the up and down
blocks by ηAαQU and ηQV Bα and the gate by ηΩγQg, where ∥QU ∥op ,∥Q V ∥op ,∥Q g∥op ≤1 . Let
κ= sup z |SiLU ′(z)|<1.1. Then
∥δfi(x)∥2 ≤2η∥x∥ 2 |SiLU(g ⊤
i x)|p 1−α
i +η κ∥x∥ 2
2 p 1−γ
i .(33)
The three branches share the same path-mass exponent for everyp i >0if and only ifγ=α.
Proof. As in the proof of Proposition 6.1, a matrix with unit operator norm has rows and columns of
Euclidean norm at most one. Hence ∥δui∥2 ≤ηr ip−α
i , ∥δvi∥2 ≤ηs ip−α
i , and ∥δgi∥2 ≤ηp −γ
i . By
Cauchy–Schwarz, the down branch is bounded byηsip−α
i |SiLU(g ⊤
i x)|r i ∥x∥2 and the up branch by
si |SiLU(g ⊤
i x)| ∥x∥ 2 ηrip−α
i . Each equals η∥x∥ 2 |SiLU(g ⊤
i x)|p 1−α
i . The gate branch is bounded
by si κ ri ∥x∥2 ∥x∥2 ηp−γ
i =ηκ∥x∥ 2
2 p1−γ
i . Summing the three bounds gives Equation 33. The
exponents1−αand1−γagree for everyp i >0exactly whenγ=α.
22

## B-ac319938a9c674

candidate openreview-yHxCX7wnSJ PDF page 27

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
Under review as a conference paper at ICLR 2027
While the trajectory remains positive, Equation 48 is exactly the mirror flow
d
dt ∇Φα(p(t)) =−∇F(p(t)).(50)
Suppose further thatF(p) =L(Ψp)for a linear mapΨ :R h →R nk and differentiableL, and that
the trajectory converges to a positive interpolatorp ∞ ∈ M:={p >0 : Ψp=y}. Then
p∞ = arg min
p∈M
DΦα(p, p0), D Φ(p, q) := Φ(p)−Φ(q)− ⟨∇Φ(q), p−q⟩.(51)
Proof. Since φ′′
α(z) =z α−1 >0 , the chain rule gives Equation 50, and Φα is strictly convex.
Moreover, ∇F(p)∈range(Ψ ⊤), so integrating and using that this finite-dimensional subspace is
closed gives ∇Φα(p∞)− ∇Φ α(p0)∈range(Ψ ⊤). This is the first-order optimality condition for
minimizing DΦα(·, p0) subject to Ψp=y . Feasibility and strict convexity make the minimizer
unique.
The dual coordinate is the Box–Cox transform φ′
α(z) = (z α −1)/α , with limit logz at α= 0 . In
particular,
DΦ1(p, p0) = 1
2 ∥p−p 0∥2
2 , D Φ0(p, p0) =
X
i

pi log pi
p0,i
−p i +p 0,i

,(52)
so0≤α≤1interpolates between entropic and Euclidean path geometry. Forp 0 =ε1,
DΦ0(p, ε1) = log(1/ε)
X
i
pi +
X
i
(pi logp i −p i) +hε.
After division by log(1/ε), this converges to the total path mass for each fixed p. On a fixed
compact feasible subset of the positive orthant the convergence is uniform, so accumulation points of
minimizers minimize total path mass. Pointwise convergence alone does not establish convergence of
minimizers on the unrestricted interpolation set.
The theorem is conditional on positivity and convergence, neither of which is proved here; for α >0
the flow can reach the boundary. The Bregman projection characterizes the reduced gradient-demand
model, not the implicit bias of the full spectrally coupled optimizer.
F.5 GAUGE DEPENDENCE OFEUCLIDEAN GRADIENT FLOW
For comparison, we keep the same frozen features and optimize the positive radial parameters ri, si
by Euclidean gradient flow on F(r⊙s) . The comparison holds while these parameters remain
positive.
Proposition F.6(Representative-dependent path geometry).The induced dynamics satisfy
˙ri =−s i∂iF(p),˙s i =−r i∂iF(p),˙p i =−
q
4p2
i +c 2
i ∂iF(p),(53)
where the imbalance ci =r 2
i −s 2
i is conserved. The rescaling (ri, si)7→(d iri, d−1
i si) preserves pi
but changesc i tod 2
i r2
i −d −2
i s2
i , and hence generally changes the mobility.
Proof. The first two identities follow from the chain rule. They imply ˙ci = 2ri ˙ri −2s i ˙si = 0 and
˙pi =−(r 2
i +s 2
i )∂iF(p). Finally,(r 2
i +s 2
i )2 = 4p2
i +c 2
i .
Relative to the balanced representative, the mobility is multiplied by
p
4p2
i +c 2
i
2pi
= 1
2
 ri
si
+ si
ri

= cosh

log ri
si

.(54)
This factor is minimized at balance and unbounded along a gauge orbit. Since it can differ across
units, a rescaling can change relative path speeds, not just the global time scale.
27

## B-b352761a875c66

candidate openreview-yHxCX7wnSJ PDF page 7

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
Under review as a conference paper at ICLR 2027
ResNet-18 ResNet-50 ViT-S ViT-B
CIFAR-100
−1
0
1
test accuracy gap
from Muon (pp)
¡1:96
ResNet-18 ResNet-50
SVHN
MLP
FashionMNIST
Gauge-Muon(1) Gauge-Muon(0.5) Path-SGD Adam
Figure 2: Test-accuracy gap against Muon (%), for each dataset and architecture. Bars are paired
differences over matched seeds, with paired standard errors; positive values favor the plotted method.
Bars below−1.5are clipped and labelled with their value.
7 EXPERIMENTALRESULTS
This section studies the empirical behavior of Gauge-Muon. We first validate our theoretical predic-
tions and then compare Gauge-Muon against established optimizers, including Muon (Jordan et al.,
2024), Adam (Kingma & Ba, 2014), and Path-SGD (Neyshabur et al., 2015a).
7.1 IMAGE CLASSIFICATION TASK
Setup.We evaluate on FashionMNIST (Xiao et al., 2017), CIFAR-100 (Krizhevsky, 2009), and
SVHN (Goodfellow et al., 2013), splitting each dataset into training, validation, and test sets. For
each optimizer, we tune the learning rate on the validation split, retrain at the selected rate on five
fresh seeds (three for the fine-tuned ViT), and report test accuracy over these seeds. The split sizes
and learning-rate grids are given in Tables 2 and Table 3 of Appendix G.4.
Models.We consider 7 settings, each pairing a dataset with an architecture: a two-layer ReLU
network on FashionMNIST; a frozen ImageNet-pretrained ResNet-18 or ResNet-50 backbone with a
trainable two-layer ReLU classifier on CIFAR-100 and SVHN; and a ViT-S/16, ViT-B/16 (Dosovitskiy
et al., 2020) fully fine-tuned on CIFAR-100. For the ViT, we use the checkpoint of You et al. (2024),
whose activations are ReLU, so that the network is positively homogeneous as our analysis assumes.
Appendix G.4.1 describes each architecture in detail.
Results.Figure 2 reports the test-accuracy gap of each optimizer relative to Muon. Gauge-Muon
withα= 1improves on Muon in all settings, by up to1.17percentage points, and the gain exceeds
one standard error in six of them. In contrast, Path-SGD falls below Muon in five of the seven settings
and AdamW in four. Path-SGD is also gauge-equivariant, but it does not orthogonalize its update
to have effective descent. Gauge-Muon combines both properties by keeping Muon orthogonalized
update and applying it in a gauge-invariant geometry.
Further analyses can be found to the appendix including learning-rate sensitivity (Appendix G.4.2),
validation-accuracy and training-loss curves (Appendix G.4.3), and robustness to the Newton–Schulz
approximation and reduced precision (Appendix G.3).
7.2 LANGUGE MODELING TASK
SetupWe use GPT-2 small settings (Radford et al., 2019) with 124M parameter to evaluate our
models. We use FineWeb-Edu with two token budgets including 150M tokens and 1B tokens. We
compare Gauge-Muon with three main baselines including Muon, Adam, and PathSGD. We search
the best learning rate over a grid, report and compare best result according to the best learning rate. A
detailed experiment setup is provided in Appendix G.
ResultsFigures 3 and 4 compare each optimizer with Muon, every optimizer at its own tuned
learning rate. At 150M tokens, Gauge-Muon(1) beats Muon in all four settings, lowering the final
7

## B-cfa07ac4981697

candidate openreview-yHxCX7wnSJ PDF page 26

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
Under review as a conference paper at ICLR 2027
Theorem F.3(Capacity budget of Gauge-Muon).For T steps with fixed α and η, suppose ρi,t ≤ρ 0
for every unit and step. Then
P(θ T )≤P(θ 0) + (2 +ρ0)η
T−1X
t=0
hX
i=1
p1−α
i,t .(44)
In particular, atα= 1,
P(θ T )≤D T :=P(θ 0) + (2 +ρ0)ηhT.(45)
Proof.The triangle inequality givesr +
i ≤r i(1 +ρ i)ands +
i ≤s i(1 +ρ i). Hence
p+
i −p i ≤p i(2ρi +ρ 2
i ) = (2 +ρ i)ηp1−α
i .
Summing over units and steps and using ρi ≤ρ 0 gives Equation 44. At α= 1 , each positive path
contributes one to the inner sum.
If P(θ 0), η, T , and ρ0 are fixed independently of the training sample and the trust bound holds almost
surely, thenf θT ∈ F DT and Theorem F.2 gives, atα= 1,
E

R(fθT )− bRS(fθT )

≤ 8kGR√n

P(θ 0) + (2 +ρ0)ηhT

.(46)
An independent random initialization can instead be conditioned on and then averaged over. Neither
empirical optimality nor convexity of the loss is needed. A predetermined training horizon therefore
controls a worst-case capacity budget. The statistical bound is width independent at fixed path mass,
whereas this optimization-based certificate grows withhT.
For α <1 , the growth allowance p1−α
i increases with path mass; for α >1 , it increases as paths
weaken; at α= 1 , it is uniform across paths. These are upper bounds on capacity growth, not
claims about realized growth or about an optimal exponent. The trust condition controls the quadratic
correction and must be verified or enforced; it does not follow from the choice ofα.
F.4 REDUCED PATH DYNAMICS ANDBOX–COX GEOMETRY
Lemma F.4(Realized path demand).At a fixed state with pi >0 , the update in Equation 43 satisfies,
asη→0,
p+
i −p i =ην ip1−α
i +O(η 2p1−2α
i ), ν i =−

ˆui, qU
i

+

ˆvi, qV
i

,|ν i| ≤2,(47)
whereˆui =u i/ri andˆvi =v i/si.
Proof. Differentiating the norms gives ∆ri =⟨ˆui,∆u i⟩+O(r iρ2
i ) and ∆si =⟨ˆvi,∆v i⟩+O(s iρ2
i ).
Expanding (ri + ∆ri)(si + ∆si) and substituting Equation 43 gives the expansion. Cauchy–Schwarz
and the norm bounds onq U
i , qV
i give|ν i| ≤2.
The factor p1−α
i sets the mobility, while νi records the demand realized by the matrix polar and is
coupled across units. To isolate mobility, we freeze the signed featuresϕi(x) = ˆvi ReLU(ˆu⊤
i x)∈R k
and consider fp(x) =P
i piϕi(x) with empirical risk F(p) . Replacing the polar demand by −∂iF(p)
defines the idealized flow
˙pi =−p 1−α
i ∂iF(p).(48)
This replacement is a modeling assumption: the full optimizer also changes feature directions and
generally hasν i ̸=−∂ iF(p).
Theorem F.5(Box–Cox mirror flow).Let α≥0 and let F be differentiable and convex on Rh
>0.
DefineΦ α(p) =P
i φα(pi)with
φα(z) =



zα+1
α(α+ 1) − z
α , α >0,
zlogz−z, α= 0.
(49)
26

## B-d04b018e2536b5

candidate openreview-yHxCX7wnSJ PDF page 40

2106
2107
2108
2109
2110
2111
2112
2113
2114
2115
2116
2117
2118
2119
2120
2121
2122
2123
2124
2125
2126
2127
2128
2129
2130
2131
2132
2133
2134
2135
2136
2137
2138
2139
2140
2141
2142
2143
2144
2145
2146
2147
2148
2149
2150
2151
2152
2153
2154
2155
2156
2157
2158
2159
Under review as a conference paper at ICLR 2027
Thirty-two expertsThe expert series shares η=.01 . At 32 experts of width 64, Gauge-Muon’s
path mass grows 240× against 7.9× at eight experts, above the ceiling where a dense block loses
about 5% to its own optimum. We expect η=.005 or .0025 to recover the 16-expert gain; this has
not been run.
Insensitivity to the exponentWith the geometric-mean normalization, α acts only through the
per-unit weights (˜p/pi)α, whose spread is aboutexp(ασ) for σ the standard deviation oflogp i within
a layer. The runs keep σ≤0.18 , so for α∈[0.25,1] the weights stay within about 15% of one,
which is why α= 0.25 , 0.5 and 1 land within 0.5% of each other in Figure 16 and Gauge-Muon(0.5)
ties Gauge-Muon(1) on the ReLU mixture.
G.6 GAUGE-FIXED QUANTIZATION-AWARE TRAINING
Why a representative is required.Let ϕ be positively homogeneous of degree ν, ϕ(cz) =c νϕ(z),
and consider the feed-forward pair
fU,V (x) =V ϕ(U x),(U, V)∼(DU, V D −ν),(63)
whereD= diag(d 1, . . . , dh)≻0. Although the two parameterizations in Equation 63 compute the
same function, ordinary weight quantization acts on their ambient coordinates and generally gives
different functions. For example, per-output-channel quantization commutes with the row scaling of
U, but not with the column scaling of V . A groupwise quantizer has the same asymmetry because its
groups lie along each matrix’s input dimension.
We use symmetric uniform fake quantization (Jacob et al., 2017). For a tensor or quantization group
w,
Qb(w) = ∆ clip(round(w/∆),−q max, qmax),∆ = ∥w∥∞
qmax
, q max = 2b−1 −1.(64)
The scale ∆ is shared either by the full matrix, by one output row, or by a contiguous group of input
coordinates (group size 128 by default).
Canonical representatives.Write ri =∥U i,:∥ and si =∥V :,i∥, using either the ℓ2 norm or the ℓ∞
norm as indicated below. The implementation supports three data-free gauge choices:
dbal
i = (si/ri)1/(1+ν) (ℓ2-balanced),(65)
deq
i = (si/ri)1/(1+ν) (ℓ∞-equalized),(66)
dvcol
i = s1/ν
i
exp

h−1P
j logs 1/ν
j
 (equalℓ ∞ column ranges inV).(67)
Equalization is best suited to a per-tensor grid, which must control the ranges of both matrices;
vcol is suited to per-channel and groupwise grids, for which row scaling already commutes with
quantization ofUand only the columns ofVremain exposed.
Let D(U, V) denote one of these canonicalizing gauges and let TD(U, V) = (DU, V D −ν). The pair
quantizer is
eQb(U, V) =T D(U,V) −1

Qb(DU), Q b(V D−ν)

.(68)
Because the canonical representative depends only on the gauge orbit (up to a harmless global scale),
this construction is exactly covariant:
eQb(TE(U, V)) =T EeQb(U, V)(69)
for every positive diagonal E, at tensor, channel, and group granularity. Thus the quantized predictor
is a well-defined function on the quotient rather than on an arbitrary checkpoint representative. We
map back in Equation 68 returns weights in the caller’s gauge; omitting it instead returns the canonical
weights expected at export. The two forms represent the same function and, under the straight-through
estimator below, produce the same gradient.
40

## B-de4d342cd29e3c

candidate openreview-yHxCX7wnSJ PDF page 13

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
Under review as a conference paper at ICLR 2027
Vineet Gupta, Tomer Koren, and Yoram Singer. Shampoo: Preconditioned stochastic tensor optimiza-
tion. InInternational Conference on Machine Learning, pp. 1842–1850. PMLR, 2018.
Nicholas J Higham.Functions of matrices: theory and computation. SIAM, 2008.
Elad Hoffer, Ron Banner, Itay Golan, and Daniel Soudry. Norm matters: efficient and accurate
normalization schemes in deep networks. InNeural Information Processing Systems, 2018. URL
https://api.semanticscholar.org/CorpusID:3813742.
Benoit Jacob, Skirmantas Kligys, Bo Chen, Menglong Zhu, Matthew Tang, Andrew G. Howard,
Hartwig Adam, and Dmitry Kalenichenko. Quantization and training of neural networks for
efficient integer-arithmetic-only inference.2018 IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pp. 2704–2713, 2017. URL https://api.semanticscholar.org/
CorpusID:39867659.
Martin Jaggi. Revisiting frank-wolfe: Projection-free sparse convex optimization. InInternational
conference on machine learning, pp. 427–435. PMLR, 2013.
Keller Jordan, Yuchen Jin, Vlado Boza, Jiacheng You, Franz Cesista, Laker Newhouse, and
Jeremy Bernstein. Muon: An optimizer for hidden layers in neural networks, 2024.URL
https://kellerjordan. github. io/posts/muon, 6(3):4, 2024.
Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization.arXiv preprint
arXiv:1412.6980, 2014.
Alex Krizhevsky. Learning multiple layers of features from tiny images. Technical report, 2009.
Daniel Kunin, Javier Sagastuy-Bre ˜na, Surya Ganguli, Daniel L. K. Yamins, and Hidenori
Tanaka. Neural mechanics: Symmetry and broken conservation laws in deep learning dynamics.
ArXiv, abs/2012.04728, 2020. URL https://api.semanticscholar.org/CorpusID:
228063783.
Jungmin Kwon, Jeongseop Kim, Hyunseong Park, and Inae Choi. Asam: Adaptive sharpness-aware
minimization for scale-invariant learning of deep neural networks.ArXiv, abs/2102.11600, 2021.
URLhttps://api.semanticscholar.org/CorpusID:232013927.
Tim Large, Yang Liu, Minyoung Huh, Hyojin Bahng, Phillip Isola, and Jeremy Bernstein. Scalable
optimization in the modular norm.Advances in Neural Information Processing Systems, 37:
73501–73548, 2024.
Tim Tsz-Kit Lau and Weijie Su. Symmetry-compatible principle for optimizer design: Embeddings,
lm heads, swiglu mlps, and moe routers.arXiv preprint arXiv:2605.18106, 2026.
Tim Tsz-Kit Lau, Qi Long, and Weijie Su. Polargrad: A class of matrix-gradient optimizers from a
unifying preconditioning perspective.arXiv preprint arXiv:2505.21799, 2025.
Arthur Lebeurrier, Titouan Vayer, and Remi Gribonval. Path-conditioned training: a principled way
to rescale relu neural networks.arXiv preprint arXiv:2602.19799, 2026.
Michel Ledoux and Michel Talagrand.Probability in Banach Spaces: isoperimetry and processes,
volume 23. Springer, 1991.
Hao Li, Zheng Xu, Gavin Taylor, Christoph Studer, and Tom Goldstein. Visualizing the loss landscape
of neural nets.Advances in neural information processing systems, 31, 2018.
Yibang Li, Bihari Lal Pandey, Ravi Sah, Andi Han, Cyrus Mostajeran, Pratik Jawanpuria, and Bamdev
Mishra. Intrinsic muon: Spectral optimization on riemannian matrix manifolds.arXiv preprint
arXiv:2605.09238, 2026.
Zhiyuan Li, Tianhao Wang, Jason D. Lee, and Sanjeev Arora. Implicit bias of gradient descent on
reparametrized models: On equivalence to mirror descent.ArXiv, abs/2207.04036, 2022. URL
https://api.semanticscholar.org/CorpusID:250407876.
13

## B-df549ca4bae6d4

candidate openreview-yHxCX7wnSJ PDF page 20

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
Under review as a conference paper at ICLR 2027
For the finite-step statement, note that(U ′+, V ′+) and (U+, V +) are again related by thesamegauge
D. Hence, as long as all side norms of the current iterate are positive, the one-step argument applies
again, and induction on the number of steps gives(U ′
t, V ′
t ) = (DUt, VtD−1)for everyt.
C.2 PROOF OFTHEOREM5.1
Proof. Write G=∇L(θ) = (G U , GV ). Since Aα and Bα are invertible, the change of variables
ZU =A −1
α ΞU and ZV = ΞV B−1
α is a bijection, and by Equation 8 it maps the unit ball {∥Ξ∥θ,α ≤
1} onto the product set {∥ZU ∥op ≤1} × {∥Z V ∥op ≤1} . Using ⟨X, DY⟩ F =⟨DX, Y⟩ F for
diagonalDand the analogous identity for right multiplication,
⟨G,Ξ⟩=⟨G U , AαZU ⟩F +⟨G V , ZV Bα⟩F =⟨A αGU , ZU ⟩F +⟨G V Bα, ZV ⟩F .(16)
The constraint set is a product, so the two terms can be maximized independently. By Equation 1,
the first term is maximized over ∥ZU ∥op ≤1 by ZU = polar(A αGU), with value ∥AαGU ∥∗,
and the second by ZV = polar(G V Bα), with value ∥GV Bα∥∗. Mapping back, the maximizer
is Ξ = (A α polar(AαGU),polar(G V Bα)Bα) =S α(θ), and the maximum equals χα(θ). Since
HU =A αGU and HV =G V Bα, the step θ−ηS α(θ) coincides with Equation 6, which is therefore
the steepest-descent step of lengthηin∥·∥ θ,α.
C.3 PROOF OFPROPOSITION6.1
Proof. Let δui and δvi be the perturbations of ui and vi produced by one Gauge-Muon step, and
write QU = polar(HU) and QV = polar(HV ). Row i of AαQU is rip−α
i times row i of QU , and
column i of QV Bα is sip−α
i times column i of QV . Every row and every column of a matrix Q
with ∥Q∥op ≤1 has Euclidean norm at most one, since


Q⊤ei


2 ≤ ∥Q∥op and ∥Qei∥2 ≤ ∥Q∥op.
Because∥polar(H)∥ op ≤1, Equation 6 gives
∥δui∥2 ≤ηr ip−α
i ,∥δv i∥2 ≤ηs ip−α
i .(17)
By Equation 11, the first-order variation off i(x) =v i ReLU(u⊤
i x)is
δfi(x) =δv i ReLU(u⊤
i x) +v i 1{u⊤
i x>0} δu⊤
i x.(18)
At the kink u⊤
i x= 0 the indicator may be replaced by any value in [0,1] without affecting the
argument below. By the triangle inequality,
∥δfi(x)∥2 ≤ ∥δv i∥2
ReLU(u⊤
i x)
 +∥v i∥2
δu⊤
i x
 .(19)
Since |ReLU(z)| ≤ |z| , the Cauchy–Schwarz inequality gives
ReLU(u⊤
i x)
 ≤r i ∥x∥2 andδu⊤
i x
 ≤ ∥δu i∥2 ∥x∥2. Combining these bounds with Equation 17,
∥δfi(x)∥2 ≤ηs ip−α
i ri ∥x∥2 +s i ηrip−α
i ∥x∥2 = 2η∥x∥ 2 risi p−α
i = 2η∥x∥ 2 p1−α
i ,(20)
which is Equation 12.
C.4 EXACT ONE-PATH REDUCTION
The mobility bound of Proposition 6.1 becomes an exact identity in the scalar model with a single
hidden path. Let u, v >0 , p=uv , and suppose the loss is L(u, v) =φ(p) for a differentiable φ.
Herer=u,s=v,A α =up −α, andB α =vp −α. The gradients are
∂L
∂u =φ ′(p)v, ∂L
∂v =φ ′(p)u,(21)
so both canonical covectors equal
Hu =H v =p 1−αφ′(p).(22)
The polar factor of a scalar is its sign, with polar(0) = 0 under the support convention. Writing
κ= signφ ′(p)∈ {−1,0,1}and defining the trust ratioρ=ηp −α, one Gauge-Muon step is
u+ =u−η up −ακ=u(1−ρκ),
v+ =v−η κ vp −α =v(1−ρκ),
p+ =u +v+ =p(1−ρκ) 2 .
(23)
20

## B-e4356d59907f4f

candidate openreview-yHxCX7wnSJ PDF page 14

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
Under review as a conference paper at ICLR 2027
Ji Lin, Jiaming Tang, Haotian Tang, Shang Yang, Xingyu Dang, and Song Han. Awq: Activation-
aware weight quantization for llm compression and acceleration.ArXiv, abs/2306.00978, 2023.
URLhttps://api.semanticscholar.org/CorpusID:271271084.
Jingyuan Liu, Jianlin Su, Xingcheng Yao, Zhejun Jiang, Guokun Lai, Yulun Du, Yidao Qin, Weixin
Xu, Enzhe Lu, Junjie Yan, et al. Muon is scalable for llm training.arXiv preprint arXiv:2502.16982,
2025.
Kaifeng Lyu and Jian Li. Gradient descent maximizes the margin of homogeneous neural networks.
ArXiv, abs/1906.05890, 2019. URL https://api.semanticscholar.org/CorpusID:
189898036.
Sibylle Marcotte, R ´emi Gribonval, and Gabriel Peyr ´e. Abide by the law and follow the flow:
Conservation laws for gradient flows.ArXiv, abs/2307.00144, 2023. URL https://api.
semanticscholar.org/CorpusID:259316537.
James Martens and Roger Baker Grosse. Optimizing neural networks with kronecker-factored
approximate curvature. InInternational Conference on Machine Learning, 2015. URL https:
//api.semanticscholar.org/CorpusID:11480464.
Andreas Maurer. A vector-contraction inequality for rademacher complexities. InInternational
Conference on Algorithmic Learning Theory, pp. 3–17. Springer, 2016.
Qi Meng, Shuxin Zheng, Huishuai Zhang, Wei Chen, Qiwei Ye, Zhi-Ming Ma, Nenghai Yu, and
Tie-Yan Liu. G-sgd: Optimizing relu neural networks in its positively scale-invariant space. In
International Conference on Learning Representations, 2019.
Markus Nagel, Mart van Baalen, Tijmen Blankevoort, and Max Welling. Data-free quantization
through weight equalization and bias correction. InProceedings of the IEEE/CVF international
conference on computer vision, pp. 1325–1334, 2019.
Behnam Neyshabur, Russ R Salakhutdinov, and Nati Srebro. Path-sgd: Path-normalized optimization
in deep neural networks.Advances in neural information processing systems, 28, 2015a.
Behnam Neyshabur, Ryota Tomioka, and Nathan Srebro. Norm-based capacity control in neural
networks. InConference on learning theory, pp. 1376–1401. PMLR, 2015b.
Yann Ollivier. Riemannian metrics for neural networks i: feedforward networks.arXiv: Neu-
ral and Evolutionary Computing, 2013. URL https://api.semanticscholar.org/
CorpusID:506677.
Thomas Pethick, Wanyun Xie, Kimon Antonakopoulos, Zhenyu Zhu, Antonio Silveti-Falls, and
V olkan Cevher. Training deep learning models with norm-constrained lmos.arXiv preprint
arXiv:2502.07529, 2025.
Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. Language
models are unsupervised multitask learners. 2019. URL https://api.semanticscholar.
org/CorpusID:160025533.
Tim Salimans and Diederik P. Kingma. Weight normalization: A simple reparameterization to
accelerate training of deep neural networks.ArXiv, abs/1602.07868, 2016. URL https://api.
semanticscholar.org/CorpusID:151231.
Wenqi Shao, Mengzhao Chen, Zhaoyang Zhang, Peng Xu, Lirui Zhao, Zhiqiang Li, Kaipeng Zhang,
Peng Gao, Yu Qiao, and Ping Luo. Omniquant: Omnidirectionally calibrated quantization for large
language models.ArXiv, abs/2308.13137, 2023. URL https://api.semanticscholar.
org/CorpusID:261214575.
Noam Shazeer. Glu variants improve transformer.arXiv preprint arXiv:2002.05202, 2020.
Tejas Pradeep Shirodkar. Dead-direction conditioners: Gauge-equivariant preconditioning for deep
networks.arXiv preprint arXiv:2606.29176, 2026.
14

## B-e4366b2722d251

candidate openreview-yHxCX7wnSJ PDF page 30

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
Under review as a conference paper at ICLR 2027
Sharpness.We consider to measure the sharpness of loss landscape by λ1(H), the largest eigenvalue
of the Hessian H=∇ 2
(U,V) L of the training loss with respect to all parameters (Dinh et al., 2017).
Figure 7 shows the sharpness of all optimizers under different gauge initialization. We observe that
Gauge-Muon is the only optimizer that reaches a low-lossandflat solution. At q= 0 , Muon and
Gauge-Muon(1) reach comparable solutions. The difference appears once the gauge is perturbed.
At q= 2 , Muon needs a smaller rate, stalls at a much higher loss and ends in a basin about 30×
sharper. Adam’s sharpness also grows withq. Path-SGD is gauge-equivariant, so its sharpness does
not change with q, however it needs its rate retuned and stalls at a high loss in a basin about three
times sharper than Gauge-Muon’s. Gauge-Muon(1) keeps the same rate, loss and sharpness at all
three q. This suggests equivariance alone therefore does not produce a good minimum, and Muon’s
spectral approach alone does not survive a change of gauge. Gauge-Muon is designed to have both
properties.
The same holds for the learned function (Figure 8). At matched seed, we measure the relative drift
∥fq −f 0∥F /∥f 0∥F on a held-out probe batch. For Muon and Adam it grows with q and is two to
five times larger than for Gauge-Muon, i.e. a large part of their solution is an artifact of the initial
parametrization. Gauge-Muon’s drift is small and does not grow withq.
G.2 THEORETICAL VALIDATION
We test four predictions of the theory on the bias-free two-layer ReLU network of width h= 512 on
FashionMNIST. Unless stated otherwise, runs use three seeds, and the initial gauge is di = 10qzi as
in Appendix G.1.
Equivariance protects the learning rate.Theorem 4.2 states that Gauge-Muon’s trajectory in
function space does not depend on the representative. To see whether this matters in practice, we
apply a function-preserving rescaling at the midpoint of training, either a LoRA-style merge that
folds a factor of 10 into one side of every hidden unit, or a per-channel scale folding di = 102zi as
done before post-training quantization, and sweep the learning rate over 10−4 to 0.316. Figure 9
shows that Gauge-Muon’s entire learning-rate curve is reproduced under both perturbations. For
Muon, the same perturbations move the optimal rate, raise the best loss, and make large rates far
more damaging: at η= 0.1 the test loss rises from 0.51 to 1.87 and 5.03. Hidden-unit imbalance
itself is not the problem: every optimizer, including SGD, drifts far from the balanced representative
during training, and Gauge-Muon drifts the most. What separates the methods is whether the update
depends on that position, which is a gauge coordinate rather than a property of the function.
10−4 10−3 10−2 10−1
learning rate ´
100
101
test loss
Muon
10−4 10−3 10−2 10−1
learning rate ´
Gauge-Muon(1)
none LoRA-style merge channel folding
Figure 9: Test loss against learning rate after a function-preserving rescaling at the midpoint of
training (FashionMNIST, h= 512 , mean over three seeds). For Gauge-Muon(1) the three curves
coincide.
30

## B-f66611d939a3dd

candidate openreview-yHxCX7wnSJ PDF page 12

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
Under review as a conference paper at ICLR 2027
Nicolas Boumal. An introduction to optimization on smooth manifolds.Cambridge University
Press,(Apr 2022), 2020.
David Carlson, Edo Collins, Ya-Ping Hsieh, Lawrence Carin, and V olkan Cevher. Preconditioned
spectral descent for deep learning.Advances in neural information processing systems, 28, 2015.
Franz Louis Cesista, Katherine Crowson, C´edric Simal, and Stella Biderman. Lora-muon: Spectral
steepest descent on the low-rank manifold.arXiv preprint arXiv:2606.12921, 2026.
Da Chang, Qiankun Shi, Lvgang Zhang, Yu Li, Ruijie Zhang, Yao Lu, Yongxiang Liu, and Ganzhao
Yuan. Muoneq: Balancing before orthogonalization with lightweight equilibration.arXiv preprint
arXiv:2603.28254, 2026.
Fang-Han Chen, Mark Schmidt, and Christos Thrampoulidis. Implicit bias of spectral descent and
muon on multiclass separable data.Advances in Neural Information Processing Systems 38, 2025.
URLhttps://api.semanticscholar.org/CorpusID:276235400.
L´ena¨ıc Chizat and Francis R. Bach. Implicit bias of gradient descent for wide two-layer neural
networks trained with the logistic loss. InAnnual Conference Computational Learning Theory,
2020. URLhttps://api.semanticscholar.org/CorpusID:211076120.
Minhyung Cho and Jaehyung Lee. Riemannian approach to batch normalization.Advances in neural
information processing systems, 30, 2017.
Laurent Dinh, Razvan Pascanu, Samy Bengio, and Yoshua Bengio. Sharp minima can generalize for
deep nets. InInternational Conference on Machine Learning, pp. 1019–1028. PMLR, 2017.
Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas
Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, et al. An
image is worth 16x16 words: Transformers for image recognition at scale.arXiv preprint
arXiv:2010.11929, 2020.
Simon Shaolei Du, Wei Hu, and J. Lee. Algorithmic regularization in learning deep homogeneous
models: Layers are automatically balanced.ArXiv, abs/1806.00900, 2018. URL https://api.
semanticscholar.org/CorpusID:46927169.
Stefan Elfwing, Eiji Uchibe, and Kenji Doya. Sigmoid-weighted linear units for neural network
function approximation in reinforcement learning.Neural networks, 107:3–11, 2018.
William Fedus, Barret Zoph, and Noam Shazeer. Switch transformers: Scaling to trillion parameter
models with simple and efficient sparsity.Journal of Machine Learning Research, 23(120):1–39,
2022.
Udaya Ghai, Elad Hazan, and Yoram Singer. Exponentiated gradient meets gradient descent. 2019.
URLhttps://api.semanticscholar.org/CorpusID:59606308.
Noah Golowich, Alexander Rakhlin, and Ohad Shamir. Size-independent sample complexity of
neural networks. InConference on learning theory, pp. 297–299. PMLR, 2018.
Antoine Gonon, Nicolas Brisebarre, Elisa Riccietti, and R ´emi Gribonval. A path-norm toolkit
for modern networks: consequences, promises and challenges. InInternational Conference on
Learning Representations, volume 2024, pp. 41108–41152, 2024.
Ian J Goodfellow, Yaroslav Bulatov, Julian Ibarz, Sacha Arnoud, and Vinay Shet. Multi-digit number
recognition from street view imagery using deep convolutional neural networks.arXiv preprint
arXiv:1312.6082, 2013.
Suriya Gunasekar, Jason D. Lee, Daniel Soudry, and Nathan Srebro. Characterizing implicit
bias in terms of optimization geometry.ArXiv, abs/1802.08246, 2018. URL https://api.
semanticscholar.org/CorpusID:3484600.
Suriya Gunasekar, Blake E. Woodworth, and Nathan Srebro. Mirrorless mirror descent: A natural
derivation of mirror descent. InInternational Conference on Artificial Intelligence and Statistics,
2020. URLhttps://api.semanticscholar.org/CorpusID:233237237.
12

## B-f6c05e710e6b88

candidate openreview-yHxCX7wnSJ PDF page 31

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
Under review as a conference paper at ICLR 2027
Path mass is invariant and obeys the capacity budget.The total path mass P(θ) = P
i pi is
gauge invariant and controls generalization (Theorem F.1), so under Gauge-Muon its trajectory should
not depend on q. We train for eight epochs atq∈ {0, . . . ,4} with fixed learning rates and measure the
largest relative deviation ofP(θ t) from the q= 0 run. Figure 10 shows that Gauge-Muon holds P(θ t)
to float32 drift across eight orders of magnitude of rescaling (relative deviation at most 2imes10−3),
whereas Muon and AdamW move it by factors of up to 484 and 355. The growth of path mass tracks
the loss: between q= 0 and q= 4 the final path mass of Muon grows58× and its test loss rises from
.296 to 9.17, while Gauge-Muon(1) stays at a path mass of 472 and a test loss of .278. The capacity
bound of Theorem F.3 holds on all 45 Gauge-Muon runs, with the bound between 6.2 and 7.0 times
the measured growth of path mass, so it is valid but conservative at this scale.
0 500
training step
102
103
104
path mass P(µt)
Muon
0 500
training step
Gauge-Muon(1)
0 1 2 3 4
initial gauge strength q
100
101
final test loss
Muon
Adam
Gauge-Muon(0.5)
Gauge-Muon(1)
q = 0 q = 1 q = 2 q = 3 q = 4
Figure 10: Path mass and test loss under a function-preserving initial gauge di = 10qzi (FashionM-
NIST, h= 512 , mean over three seeds). Left and middle: path-mass trajectory P(θ t) for each q; for
Gauge-Muon(1) the five curvescoincide. Right: final test loss againstq.
Path demand follows a power law in path mass.Lemma F.4 writes the first-order growth of
each path as ηνip1−α
i and bounds the demand by |νi| ≤2 . We record νi every ten steps for
α∈ {0.5,1,1.5} . Late in training, logp i explains a large share of the variance of logν i (R2 between
0.44 and 0.63) but almost none of the variance of the balanced covector norm (R2 between 0.006 and
0.19). The structure therefore lives in the demand that the geometry exposes, not in the raw gradient,
which is what separates Gauge-Muon from Path-SGD. The bound holds with margin: the largest
measured|ν i|is0.72, and no unit exceeds2at any sample.
The tuned learning rate depends on the trajectory.A step is controlled by the trust ratio
ρi =ηp −α
i , which Theorem F.3 requires to stay bounded. If the tuned learning rate keeps this
ratio fixed at a typical path mass ˜p, then η∗ ∝˜pα. Evaluated at the initial ˜p, this gives a slope
dlogη ∗/dα=−3.1 , a 100× fall in η∗ over α∈[0,1.5] . The measured slope is −0.5, a fall of only
2×. The difference comes from ˜p, which grows by one to two orders of magnitude during training,
and faster for larger α. Averaged over the trajectory, the predicted slope lies between −0.5 and −1.9,
which brackets the measurement, so the prediction holds once ˜pis taken along the trajectory rather
than at initialization.
G.3 NUMERICAL ROBUSTNESS
We test the numerical robustness of Gauge-Muon with respect to the accuracy of the Newton-Schulz
polar approximation and reduced-precision computation. Table 1 reports the results at α= 1 and
η=.003 . Three Newton-Schulz iterations can provide a good approximation, but increasing the
number of iterations from three to seven improves the loss from .2960 to .2778 and substantially
increases effective path utilization, with Neff/h rising from .880 to .981. Seven iterations closely
match the exact SVD baseline, which achieves a loss of .2765 and Neff/h=.982 . Therefore, a more
31

## B-fbf72980790dac

candidate openreview-yHxCX7wnSJ PDF page 18

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
Under review as a conference paper at ICLR 2027
A NOTATIONS
Throughout the paper, we use the following notation. For a vector x= (x 1, . . . , xd)⊤ ∈R d, its
Euclidean norm is defined as ∥x∥2 =
Pd
j=1 x2
j
1/2
. For matrices A, B∈R m×n, the Frobenius
inner product is ⟨A, B⟩F = tr(A⊤B), and the corresponding Frobenius norm is∥A∥F =
p
⟨A, A⟩F .
Every real matrix A∈R m×n admits a compact singular value decomposition (SVD) A=PΣQ ⊤,
where P∈R m×r and Q∈R n×r have orthonormal columns, and Σ = diag(σ1, . . . , σr) contains
the positive singular values σ1 ≥ · · · ≥σ r >0 , with r= rank(A) . The operator norm, also known
as the spectral norm, measures the largest factor by which A can stretch a unit Euclidean vector
and is defined as ∥A∥op = max∥x∥2≤1 ∥Ax∥2 =σ 1. Its dual norm is the nuclear norm, defined as
∥A∥∗ = max∥B∥op≤1 ⟨A, B⟩F =Pr
j=1 σj.
B EXTENDEDRELATEDWORK
We provide a broader related work in addition to Section 2 in the main text.
Spectral and orthogonalized optimizers.Beyond the original Muon (Jordan et al., 2024), sub-
sequent work refined the polar iteration (Amsel et al., 2026), added adaptivity (Si et al., 2025),
distributed the method (Ahn et al., 2025), and recast it within a unifying preconditioning view (Lau
et al., 2025). Without accumulation, Shampoo’s update reduces to the polar factor of the gradi-
ent (Bernstein & Newhouse, 2024b); SOAP (Vyas et al., 2025) is a further relative in the same family.
The LMO view of norm-constrained training (Pethick et al., 2025) has roots in Frank-Wolfe (Jaggi,
2013). The spectral scaling condition (Yang et al., 2023) andµP (Yang & Hu, 2021; Yang et al., 2021)
justify the operator-norm geometry through width-robust feature learning. MuonEq (Chang et al.,
2026) also rescales the input to Muon before orthogonalization, but its row/column equilibration is
computed from the current momentum matrix to improve finite-step Newton-Schulz conditioning.
Gauge-Muon instead derives its paired rescaling from a function-preserving symmetry; its factors de-
pend jointly on adjacent parameter blocks and guarantee equivariance across functionally equivalent
representations.
Factor rescaling in low-rank adapters.Factor-rescaling non-invariance has also been identified
for low-rank adapters, where (B, A)7→(BD, D −1A) leaves BA unchanged. LoRA-RITE (Yen
et al., 2025) constructs transformation-invariant adaptive preconditioners, and a Muon-type optimizer
for parametrization-independent LoRA has been proposed (Bogachev et al., 2026). Our setting differs
in that the gauge acts by a positive diagonal on a nonlinear (ReLU/SwiGLU) hidden layer rather than
byGL(r)on a bilinear product.
Rescaling symmetry and path geometry.Rescaling invariance motivates path-norm capacity
control (Neyshabur et al., 2015b; Golowich et al., 2018; Gonon et al., 2024). Besides Equi-
normalization (Stock et al., 2019), cross-layer equalization (Nagel et al., 2019) also selects a canonical
orbit representative. Riemannian and quotient approaches treat the symmetry through the geometry
of the quotient manifold (Absil et al., 2008; Boumal, 2020; Badrinarayanan et al., 2015; Cho & Lee,
2017). DDC (Shirodkar, 2026) lifts adaptive optimizers to architectural quotient spaces by separating
symmetry and functional directions under an invariant metric; our question is narrower, namely
which Muon-like spectral geometry should act on the quotient of the multiplicative hidden-unit gauge.
Symmetry teleportation (Zhao et al., 2023a;b) instead moves along orbits to accelerate descent;
see Zhao et al. (2025) for a survey. Scale symmetry also underlies reparameterization-dependent
sharpness (Dinh et al., 2017) and its scale-invariant fixes (Kwon et al., 2021), as well as the effective-
learning-rate dynamics of normalized layers (Salimans & Kingma, 2016; Hoffer et al., 2018; Arora
et al., 2018). Gauge-Muon shares the orbit-invariance goal of Path-SGD and G-SGD, but, unlike
canonicalization methods, it does not fix a single representative.
Reparameterization-invariant and natural-gradient methods.Natural gradient (Amari, 1998)
and its approximations, such as K-FAC (Martens & Grosse, 2015) and unit-wise Riemannian met-
rics (Ollivier, 2013), are invariant to (classes of) reparameterizations through a Riemannian metric
18

## B-fc6c2ac08b8848

candidate openreview-yHxCX7wnSJ PDF page 2

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
Under review as a conference paper at ICLR 2027
to form the update. Existing rescaling-invariant methods obtain invariance in other ways such as
through a path-normalized Euclidean geometry (Neyshabur et al., 2015a), by optimizing directly in
invariant path coordinates (Meng et al., 2019), by moving to a well-conditioned representative of
each set of equivalent parameters (Stock et al., 2019; Lebeurrier et al., 2026), or by descending in
canonically scaled coordinates (Uhlmann, 2026). None of them keeps the matrix-level coupling of
an orthogonalized update. Conversely, symmetry-aware analyses of Muon (Singh, 2026) concern
orthogonal changes of basis, which the polar map already respects, rather than rescaling. Closest
to our work, Shirodkar (2026) make an adaptive optimizer equivariant by splitting its state into a
component along the symmetry orbit and a component across it, measured in an invariant metric, and
projecting the update back across the orbit. For the rescaling symmetry, however, that construction
runs on an Adam base. It argues that orthogonalization removes the per-channel scale, so its Muon
variant is made equivariant only to attention-head rotations. Gauge-Muon takes a different route. It
uses no projection and no second-moment split. Instead it rescales the gradient by per-unit factors
computed from the weights before the polar map and undoes them afterwards, thereby Muon’s
spectral update is itself equivariant to hidden-unit rescaling. To our knowledge, Gauge-Muon is the
first optimizer that combines exact rescaling invariance with matrix-level orthogonalized updates.
Our contributions are as follows. (i) We introduce Gauge-Muon, a family of optimizers that are
exactly equivariant under hidden-unit rescaling at every finite step size (Theorem 4.2). (ii) We show
that Gauge-Muon is exact steepest descent under a state-dependent operator norm that descends to
the quotient of parameter space by the rescaling group (Theorem 5.1). (iii) We characterize how the
family’s exponent allocates functional mobility across paths of different strength (Proposition 6.1) and
derive an invariant capacity bound on generalization (Theorem F.1). (iv) We validate Gauge-Muon on
image classification and GPT-2 language modeling, where it improves on Muon in all image settings
and in every language-modeling setting at the low token budget; at the higher budget the gain persists
in mixture-of-experts models with narrow experts.
2 RELATEDWORK
Spectral and orthogonalized optimizers.Muon (Jordan et al., 2024) replaces the momentum
matrix by (an approximation to) its polar factor, computed with Newton-Schulz iterations (Bj¨orck &
Bowie, 1971; Higham, 2008), and has been scaled to LLM pretraining (Liu et al., 2025). It descends
from spectral descent (Carlson et al., 2015), is closely related to Shampoo (Gupta et al., 2018), and is
steepest descent under the spectral norm (Bernstein & Newhouse, 2024b); modular norms (Large
et al., 2024; Bernstein & Newhouse, 2024a) and linear-minimization-oracle (LMO) methods (Pethick
et al., 2025) extend this view to whole networks. Muon is equivariant under orthogonal changes of
basis, which commute with the polar map (Singh, 2026). All of these geometries are fixed norms on
parameterspace, and the polar map does not commute with positive diagonal congruences, so none
is invariant under the hidden-unit rescaling. Our Gauge-Muon keeps the spectral LMO but applies it
to state-dependent, gauge-invariant covectors.
Preconditioned norms.A steepest-descent step under a left/right-preconditioned operator norm
can be computed by transforming the gradient, applying the base-norm LMO, and mapping back.
This identity is implicit in the duality maps of Bernstein & Newhouse (2024b;a) and Pethick et al.
(2025), and Veprikov et al. (2025) develop it into a general framework in which invariances are
inherited from the transformation law of preconditioner. In this paper, our main focus is to propose a
preconditioner. We derive the covariant factors from thepairedincoming/outgoing gauge and path
masses, prove exact finite-step equivariance. We show that the induced norm descends to a quotient
norm on function space, giving a family of equivariant spectral geometries.
Rescaling-invariant optimization.There are existing studies on positive homogeneity of ReLU
networks. Path-SGD (Neyshabur et al., 2015a) performs steepest descent under a rescaling-invariant
path regularizer, G-SGD (Meng et al., 2019) optimizes in a basis of positively scale-invariant path
variables, and Equi-normalization (Stock et al., 2019) selects a canonical representative of each orbit.
Most recently, the unit-consistent adjoint framework (Uhlmann, 2026) obtains gauge-equivariant
steepest descent by descending in canonically scaled coordinates. Such methods achieve invariance
with entry-wise or Euclidean geometry, or by fixing one representative. In constrast, to our knowledge,
our Gauge-Muon is the first approach to connect between exact invariance and a matrix-level spectral
2

## B-feb3edbe1fc960

candidate openreview-yHxCX7wnSJ PDF page 11

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
Under review as a conference paper at ICLR 2027
Huang, Ke Huang, Ruiyuan Huang, Siying Huang, Weixiao Huang, Yan Huang, Zheng-Jie Huang,
Zhi-Qi Huang, Yu-Long Hui, Chao Jia, Yu-Tong Jiang, Zhe-Jun Jiang, Zuo-You Jiang, W.M. Jin,
Xinyi Jin, Yu Jing, Huanjun Kong, Guokun Lai, Aidi Li, Cheng Li, Cheng-Yuan Li, Cong Li, Fang
Li, Guanyu Li, Haoyang Li, Jia Li, Jun-Xiong Li, Lei Li, Le-Tian Li, Lin-Can Li, Wei-Hong Li,
Wen-Tao Li, Xintong Li, Yang Li, Yi-Shen Li, Yi-Wei Li, Yu-Xiao Li, Zhao-Wei Li, Zhao-Xi
Li, Zhe-Ming Li, Zheng-Xiao Li, Zhi-Yuan Li, Jiawei Lin, Xiaohan Lin, Yibo Lin, Zi-Chao Lin,
Zi-Yan Lin, Bill Liu, Bo-Xiao Liu, Chuangye Liu, Liang Liu, Shao-Wei Liu, Shu-Dong Liu,
Shu-Ran Liu, Tianwei Liu, Weizhou Liu, Yang-Yang Liu, Yan-Ming Liu, Yi-Bo Liu, Yi-Peng Liu,
Zheng-Ying Liu, Zhi-Heng Liu, Enzhe Lu, Haoyu Lu, Lin Lu, Ting Lu, Zhiyuan Lu, Aotian Luo,
Gen Luo, Junyu Luo, Yi-Fan Luo, Bohan Lyu, Wenzhou Lyu, Shaoguang Mao, Yuan Mei, Xin
Men, Mi Ni, Yixuan Niu, Siyuan Pan, Shujun Peng, Zhang-Yang Qi, Ruoyu Qin, Zeng Qin, Ze-Yu
Qin, Haiquan Qiu, Jian-Xin Qiu, Jie-Zhong Qiu, Bowen Qu, Yuhao Qu, Zeyu Shang, Youbo Shao,
Han Shen, Jin-Cheng Shi, Juan-Feng Shi, Li-Na Shi, Sheng-Peng Shi, Wingchun Siu, Pengwei
Song, Xiao-Xiu Song, Jianlin Su, Yu-Li Su, Zhao-Chen Su, Lin Sui, Jing-Song Sun, Jun-Yao Sun,
Shao-Ning Sun, Shu-Zhe Sun, Tong Sun, Yu-Jun Sun, Yu-Chuan Tai, Chuning Tang, He-Yi Tang,
Si-Si Tang, Ze-Cheng Tang, Chao Tian, Rong Tian, Yu Tian, Wei Tu, Chen-Si Wang, Chuang
Wang, Chun-Jie Wang, Dinglu Wang, Feng Wang, Hai-Long Wang, Hai-Ming Wang, Hao Wang,
Hua-Qing Wang, Hui Wang, Jia-Yi Wang, Jing-Long Wang, Jin-Hong Wang, Jiu-Zheng Wang,
Li-Nian Wang, Shao-Bo Wang, Shen-Zhi Wang, Shu-Yi Wang, Si Wang, Si-Yuan Wang, Tianfu
Wang, Wenju Wang, Xing-Ran Wang, Xin-Mei Wang, Xin-Yuan Wang, Xu-Sheng Wang, Ya-Lin
Wang, Yang-Kun Wang, Yao Wang, Yao-Yu Wang, Ye-Jie Wang, Yi-Qin Wang, Yu-Cheng Wang,
Yu-Zhi Wang, Zhao-Ji Wang, Zhao-Wei Wang, Zheng-Tao Wang, Zhen-Hao Wang, Zhong-Sheng
Wang, Zi-Fan Wang, Chu Wei, Ming Wei, Shouxin Wei, Zichen Wen, Fan Wu, Haoning Wu,
Rucong Wu, Wenhao Wu, Xiaoxue Wu, Ying-Cong Wu, Yong-Qi Wu, Yu-Xin Wu, Zijian Wu,
Xinglang Xian, Chen Xiang, Yu-Ting Xiang, Bo Xiao, Chen-Jun Xiao, Xin Xiao, Jin Xie, Xiao-
Ming Xie, Yifeng Xie, Zhe Xie, Bowei Xing, Yi-Ming Xiong, Bao-Sheng Xu, Bo-Yu Xu, Jia-Le
Xu, Jian-Fan Xu, Jing Xu, Jin-Jing Xu, L.-H. Xu, Qin Xu, Shu-Yao Xu, Su-Ting Xu, Tian-Tian
Xu, Tian-Xiang Xu, Weixin Xu, Xinran Xu, Yang-Chuan Xu, Ye Xu, Yue-Ni Xu, Ziyao Xu, Hao
Xue, Junjie Yan, Yaoyao Yan, Fan Yang, Guang-Fu Yang, Hao Yang, Junwei Yang, Ruo-Tong
Yang, Wenjie Yang, Xiao-Fei Yang, Xin-Yu Yang, Yi Yang, Yi-Ling Yang, Ying Yang, Yu-Chen
Yang, Zhen Yang, Zhi-Lin Yang, Ruihan Yang, Zu-Hao Yang, Haotian Yao, Dan Ye, Hao-Ran Ye,
Wenjie Ye, Zhanbo Ye, Bohong Yin, Haoxiang Yin, Xi Yin, Chengzheng Yu, Haozhe Yu, Long
Yu, Sheng-Nan Yu, Shu-Ying Yu, Tianxiang Yu, Enming Yuan, Mengjie Yuan, Tong-Tian Yue,
Weize Yue, Yang Yue, Dunyuan Zha, Haobing Zhan, B.-H. Zhang, Dehao Zhang, Feichang Zhang,
Hao Zhang, Hao-Yuan Zhang, Huan-Yu Zhang, Jia-Pei Zhang, Jia-Xuan Zhang, Jin Zhang, Kai-Yi
Zhang, Miao Zhang, Pu Zhang, Qingle Zhang, Rong Zhang, Rui Zhang, Shao-Shuai Zhang, Shi-Yi
Zhang, Xiao-Bin Zhang, Xiao-Yun Zhang, Y . Zhang, Yang-Kun Zhang, Ye Zhang, Yi-Chi Zhang,
Yi-Kun Zhang, Yi-Zhi Zhang, Yong-Ting Zhang, Yu Zhang, Yu-Tao Zhang, Yu-Tong Zhang, Zheng
Zhang, Zi-Jing Zhang, Bin Zhao, Chenguang Zhao, Feifan Zhao, Jing-Lun Zhao, Jin-Xiang Zhao,
Shuai Zhao, Wen-Shuo Zhao, Xiang-Yu Zhao, Xuan-Le Zhao, Yikai Zhao, Zijia Zhao, Hao Zheng,
Hua-Bin Zheng, Ruihan Zheng, Shao Jian Zheng, Tengyang Zheng, Haofeng Zhong, Lei Zhong,
Long-Guang Zhong, M. Zhou, Qian Zhou, Run-Jie Zhou, Ruoyv Zhou, Xinyu Zhou, Yiqiao Zhou,
Zaida Zhou, Jinguo Zhu, Liya Zhu, Xinhao Zhu, Yangjunfeng Zhu, Yuxuan Zhu, Zhengxin Zhu,
Chen Zhuang, Weiyu Zhuang, and Xinxing Zu. Kimi k3: Open frontier intelligence. 2026. URL
https://api.semanticscholar.org/CorpusID:290625162.
Jeremy Bernstein and Laker Newhouse. Modular duality in deep learning.arXiv preprint
arXiv:2410.21265, 2024a.
Jeremy Bernstein and Laker Newhouse. Old optimizer, new norm: An anthology.arXiv preprint
arXiv:2409.20325, 2024b.
˚Ake Bj ¨orck and Clazett Bowie. An iterative algorithm for computing the best estimate of an
orthogonal matrix.SIAM Journal on Numerical Analysis, 8(2):358–364, 1971.
Vladimir Bogachev, Vladimir Aletov, Alexander Molozhavenko, Denis Bobkov, Vera Soboleva,
Aibek Alanov, and Maxim Rakhuba. Lora meets riemannion: Muon optimizer for parametrization-
independent low-rank adapters. InInternational Conference on Learning Representations, volume
2026, pp. 82190–82215, 2026.
11
