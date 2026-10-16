# What Algorithm Can Transformers Learn in Closed-Loop Interaction?

## B-0289c0705bb84b

candidate openreview-8OOMlVFxb0 PDF page 19

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
Accumulated error. Let B uniformly bound all routed value vectors, chooseC ≥ log((NH −1)/ξ),
and set rξ := 2Bξ. Choose ξ small enough that validity routing remains in the two saturation regions
above. Lemma D.1 bounds the error of each copied observation, action, or state by rξ. Let LU be a
Lipschitz constant for the shared update under the product norm ∥(s, a, x)∥⊕ := ∥s∥ + ∥a∥ + ∥x∥,
let et = ∥bst − st∥∞, and put η := δU + 3LU rξ. The first update obeys e1 ≤ η, and for t > 1,
et ≤ LU et−1 + δU + 3LU rξ, e t ≤ η
t−1X
j=0
Lj
U . (36)
If the shared logit map has Lipschitz constant Lℓ and uniform approximation error δℓ, andbλt denotes
the logits written at Dt, the readout bound is
∥bλt − ℓt(st)∥∞ ≤ δℓ + Lℓ

rξ + η
t−1X
j=0
Lj
U

 . (37)
For finite logits, TV(softmax(u), softmax(v)) ≤ ∥u − v∥∞. Because H is finite, ξ, δU , δℓ can be
chosen so that the right-hand side of (37) is at most ϵ uniformly over t ≤ H. The construction uses
H copies of one shared three-head update block and one single-head readout block, with residual
width counted above; hence it proves the result. □
E C OMPILATION DEPTH : G ENERIC AND ADDITIVE RECURSIONS
Compilation depth depends on update structure. The generic compiler applies one shared update
block sequentially, whereas attention can aggregate a sum of per-interaction statistics in parallel. Call
a recursion additive-sufficient when
st = F

x0, t,
Xt−1
u=1
ψ(x0, au, xu)

. (38)
The following proposition summarizes the resulting constructive depth upper bounds.
Proposition E.1 (Depth bounds for generic and additive recursions) . Under the conditions of
Theorem 4.1, every regular horizon-H recursion admits uniform action-kernel approximation using
H applications of one shared update block and one readout block. Under the additional regularity
conditions stated below, the state and all policies of any additive-sufficient recursion can, for every
fixed maximum horizon and ϵ > 0, be uniformly ϵ-approximated with at most three attention-
feed-forward blocks. Thus the generic construction has O(H) block depth, whereas the additive
construction has O(1) block depth. Conditionally independent Bayesian updating and UCB count-
sum updates are additive-sufficient instances.
These are constructive block-depth upper bounds under the stated conditions for each fixed max-
imum horizon H; they do not imply horizon-independent bounds on model size, runtime, or
planning complexity.
Appendix D proves the generic bound. We now give the additive construction.
Assumptions and resource accounting. (38) is assumed to hold on compact encodings, withF, ψ, ℓ
uniformly Lipschitz and admitting feed-forward approximations, and with Gt the masked softmax
of ℓ(st). The proposition inherits the finite-vocabulary and public legality-mask assumptions of
Theorem 4.1. For each fixed maximum horizon H, the attention scale and feed-forward approximator
size may depend on H and ϵ; only the number of Transformer blocks is independent ofH. A returned
record may copy its action or tool identifier, as ordinary tool logs do; otherwise one preliminary
routing block pairs them.
Construction. Reserve immutable coordinates for token type, turn, the initial record x0, a com-
pleted action-observation record, and scratch/state slots. A completed record token contains (au, xu).
If the prompt stores them separately, one preliminary causal routing block copies au to the returned-
record token with the typed-turn construction of Lemma D.1; a position-wise approximator then
19

## B-06f467d459890c

candidate openreview-8OOMlVFxb0 PDF page 15

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
Linear contextual bandit. LinUCB (Li et al., 2010) maintains(ct, Vt, qt), initialized with V1 = λI
and q1 = 0. For ϕt = ϕ(ct, it), it updates Vt+1 = Vt + ϕtϕ⊤
t , qt+1 = qt + rtϕt, and stores ct+1. Its
decision rule is
Gt = δi∗
t , i ∗
t = tieargmaxi∈[K]

ϕ(ct, i)⊤V −1
t qt + βt
q
ϕ(ct, i)⊤V −1
t ϕ(ct, i)

. (14)
EXP3 adversarial bandit. With w1(i) = 1, exploration probability γt ∈ (0, 1], and learning rate
ηt > 0, EXP3 (Auer et al., 2002b) uses
pt(i) = Gt(i | st) = (1 − γt) wt(i)P
j wt(j) + γt
K ,
wt+1(i) = wt(i) exp

ηt
rt(it)1{i = it}
pt(i)

.
(15)
The environment may choose a history-dependent reward vector; only the selected coordinate rt(it)
is observed.
Q-learning. Q-learning is the canonical off-policy TD-control instance (Watkins & Dayan, 1992).
Let st = (Qt, ot). With a fixed tie convention and legal set Lt(o), define the ϵt-greedy kernel
a∗
t = tieargmaxu∈Lt(ot) Qt(ot, u),
Gϵ
t(a | Qt, ot) =
(1 − ϵt)1{a = a∗
t } + ϵt/|Lt(ot)|, a ∈ L t(ot),
0, a / ∈ L t(ot),
(16)
After at ∼ Gϵ
t(· | Qt, ot) returns xt = (rt, ot+1, dt), Ut stores ot+1 and applies
Qt+1(o, a) = Qt(o, a) + αt1{(o, a) = (ot, at)}
×

rt + γ(1 − dt) max
u∈Lt+1(ot+1)
Qt(ot+1, u) − Qt(ot, at)

. (17)
The max target is independent of the next behavior action, which makes the update off-policy.
SARSA with an explicit pending transition. Because the on-policy target uses the next sampled
action, take st = ( Qt, ot, pt), where pt = ( ot−1, at−1, rt−1, ot, dt−1) is pending and p1 = ⊥.
SARSA uses the same legal ϵt-greedy kernel as Q-learning:
Gt(a | st) = Gϵ
t(a | Qt, ot). (18)
After sampling, at completes the pending target. For pt ̸= ⊥, Ut(st, at, xt) applies
Qt+1(ot−1, at−1) = Qt(ot−1, at−1) +αt[rt−1 + γ(1 − dt−1)Qt(ot, at) − Qt(ot−1, at−1)] , (19)
leaves every other entry unchanged and stores (ot, at, rt, ot+1, dt) as the new pending transition. If
pt = ⊥, it only stores the new transition. A terminal pending tuple uses zero bootstrap. If the final
internal Q-update must also be represented, one can append a dummy absorbing action. This one-step
augmentation represents standard SARSA, rather than expected SARSA, within (2).
Actor-critic. Let st = ( θt, wt, ot), Gt(a | st) = πθt(a | ot), and vwt be the critic. For xt =
(rt, ot+1, dt), a standard one-step actor-critic update (Sutton & Barto, 2018) is
δt = rt + γ(1 − dt)vwt(ot+1) − vwt(ot),
wt+1 = wt + αcδt∇wvwt(ot),
θt+1 = θt + αaδt∇θ log πθt(at | ot).
(20)
Model-based online RL with learned-model planning. For finite state and action spaces,
Nt(o, a, o′), Zt(o, a), and Ct(o, a) store transition counts, visit counts, and reward sums (Sutton &
Barto, 2018; Sutton, 1990). After (ot, at, rt, ot+1), increment the corresponding entries of Nt, Zt, Ct
by 1, 1, rt, store ot+1, and normalize:
bPt+1(o′ | o, a) = Nt+1(o, a, o′)
Zt+1(o, a) , bRt+1(o, a) = Ct+1(o, a)
Zt+1(o, a) . (21)
15

## B-0c17648651fc9d

candidate openreview-8OOMlVFxb0 PDF page 2

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
Agentic ICL: closed-loopICL: one-step#₁ #₂Prompt ℎ₀
Model
Prompt ℎ₁
Model
Prompt ℎ₂
ModelEnv. Env. ···output output
Generalagentictasks ICRL: a special case where each %ₜ contains Markov state and scalar rewardCodingWeb search…⊊
Figure 1: Illustrative comparison of Agentic ICL, ICL and ICRL. Agentic ICL studies how agents
solve general agentic tasks.
included in the interaction history. However, an agent usually receives non-reward feedback: a search
result, compiler diagnostic, or measurement can guide the next action. We therefore develop Agentic
ICL allowing agents to learn from non-reward feedback. This also separates the evidence used for
in-context adaptation from the objective used for training and evaluation. Agentic ICL includes ICRL
as a special case. Figure 1 illustrates this relationship.
Task performance alone does not reveal the interactive algorithm. Answering these questions requires
both a construction showing what Transformers can execute and experiments examining what they
learn under different objectives. Our contributions are fourfold:
• Closed-loop framework (Section 3). We factor an interactive learner into a sufficient state, a
feedback update, and a decision rule. The same interface covers active learning, bandits, and
online RL.
• Transformer realization (Section 4). We give a constructive proof that compiles regular finite-
horizon recursions into causal Transformers. The construction realizes their action choices and
yields a bound on autonomous return loss.
• Training objectives and diagnosis (Section 5). We theoretically characterize when pro-
cess supervision preserves outcome-optimal behavior, then develop behavioral diagnostics for
trained Transformers.
• What training learns (Section 6). Supervised distillation tests learned execution of supplied
interactive recursions. RL without oracle action shows how outcome and process rewards lead to
different decisions, and how those decisions change with controllable reward intervention.
2 R ELATED WORK
Learning algorithm views of ICL and ICRL. ICL has been characterized as implicit Bayesian
inference, regression, gradient descent, algorithm selection, and data-dependent learning-to-learn
(Xie et al., 2022; Garg et al., 2022; Akyürek et al., 2023; von Oswald et al., 2023; Bai et al., 2023;
Wu et al., 2025). Constructive, behavioral, and mechanistic studies identify familiar estimators
inside Transformers (Akyürek et al., 2023; von Oswald et al., 2023; Bai et al., 2023); we extend
this standard to closed-loop recursions whose decisions determine subsequent in-context data. ICRL
extends this perspective to RL updates and control, including pretraining on stored state-action-reward
trajectories with source-policy or oracle actions (Laskin et al., 2023; Lee et al., 2023; Lin et al.,
2024). These models can nevertheless generate their own interaction histories at deployment. Prior
work implements posterior sampling, bandit, TD, SARSA, or policy-improvement computations
and distinguishes model-free from model-based strategies (Wang et al., 2025; Fang & Rajan, 2025;
Liang & Lai, 2026). Our interface permits both reward-hidden and history-dependent feedback.
Rewards used for training and evaluation need not be revealed in the agent’s transcript, and individual
returned records need not be Markov states: the feedback law may depend on the full interaction
history, from which the learner constructs its sufficient state. Agentic ICL unifies active learning,
bandits, online RL, and tool use. The primary discovery experiments provide neither oracle actions
nor sufficient-state targets.
2

## B-17c8de0ce36886

candidate openreview-8OOMlVFxb0 PDF page 31

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
horizon at history h, and let q0 and H0 be their initial values. We first define the confidence potential
Φ0(h) = δC(h) max
z
bh(z), Φ0(hterminal) = 0.
We perturb it with the fixed resource- and belief-dependent function
ψ(h) = 1
3
 H(bh)
log K + qh
q0
+ ℓh
H0

, ψ (hterminal) = 0,
where H is Shannon entropy. Each normalized term lies in[0, 1], so 0 ≤ ψ(h) ≤ 1. With a coefficient
ϵ = 0.05, fixed before diagnostic evaluation and shared by every task and seed, the perturbed potential
and trainer-side reward are
Φϵ(h) = Φ0(h) + ϵψ(h), erpreserve,ϵ
t = rout
t + Φϵ(ht) − Φϵ(ht−1), γ PPO = 1.
The terminal outcome lies in [0, 1], so ϵ = 0.05 bounds the potential perturbation by five percent
of the outcome scale. It also bounds the additional change to any individual transition reward,
ϵ|ψ(ht) − ψ(ht−1)|, by 0.05. The perturbation is deterministic given the trainer-side history and is
not included in the transcript or resampled during training.
The outcome reward remains zero on calls and equals discounted correctness on termination. Applying
Appendix C with β = 1 gives, at every legal pre-action history,
Q∗
preserve,ϵ,t(h, a) = Q∗
out,t(h, a) − Φϵ(h).
The action-independent shift preserves the optimal-action sets exactly, satisfying Proposition 5.1
without the approximate margin condition in (24). Potentials and rewards remain outside the
transcript; advantage standardization is retained without reward clipping or nonlinear normalization.
The posterior probe follows the primary conditions’ layer, task splits, normalization, and ridge-
selection protocol. The control uses a hand-specified reward.
Table 20: Outcome-preserving process-reward control with the fixed perturbed potentialΦϵ, ϵ = 0.05.
The perturbation changes intermediate reward values while leaving the unregularized outcome-
optimal policy set unchanged. Architecture, training budget, seed identities, and evaluation tasks are
matched to the outcome-reward condition. Values are mean ± standard deviation across five seeds.
Condition Bayes DP-score TV ↓ KG-score TV ↓ Two-step-score TV ↓ Return ↑ Post. NRMSE ↓ Update NRMSE ↓
Outcome-preserving
process reward 0.046 ± 0.007 0.184± 0.015 0.084± 0.010 0.752± 0.009 0.023± 0.004 0.030± 0.005
Its oracle ordering-violation fraction is exactly zero on both D and DBK , as follows from the
action-value identity above. The earlier measurements of optimal-action mass, regret, and agreement
with Bayes DP and KG show that the model trained with this reward also behaves similarly to the
outcome-trained model.
G.8 W HEN DOES EXTENDING VERIFIER CREDIT PRESERVE OUTCOME -OPTIMAL ACTIONS ?
Cost-consistent reward and cumulative objective. We fix α = τv = 1 and vary the credit
discount γ, using the same cost-scaled local reward throughout:
dh = δC(h), ¯rα,τv(h, a, h′) = dher1V
α,τv(h, a, h′), G (γ)
t =
TX
u=t
γu−t¯ru. (48)
Here γ = β = γPPO is the process-return discount; it is distinct from the task’s cost discountδ, and
λGAE = 1. The reward in (48) is identical across γ conditions: in particular, its utility difference
is not replaced by γΦ(h′) − Φ(h). The verifier still accesses neither the sampled target nor oracle
action or continuation values. Multiplication by dh changes the scale across histories, so these trained
models are reported separately from the unscaled one-step conditions.
Calibrated endpoints and boundary existence. Write cb(h) = maxz bh(z). At α = τv = 1, the
immediate endpoint satisfies
Q∗
1,1,0(h, a) = dh[QKG(h, a) − cb(h)], A∗
1,1,0(h) = A∗
KG(h). (49)
31

## B-1be4e366dae9ed

candidate openreview-8OOMlVFxb0 PDF page 32

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
For a completed episode with answer gT , summing the cost-scaled local rewards telescopes to
TX
t=1
¯rt = δCT [αqτv(gT | hT −1) + (1 − α)I(qτv(· | hT −1))] − Uα(qτv(· | h0)).
At calibration the terminal posterior probability is the conditional expectation of correctness. Conse-
quently, for every policy,Eπ
P
t ¯rt = EπRout − maxz p0(z), and at any legal pre-action history,
Q∗
1,1,1(h, a) = Q∗
out(h, a) − dhcb(h), A∗
1,1,1(h) = A∗
out(h). (50)
The outcome values here are in raw return units, including already-incurred cost. This establishes
equivalence in conditional expectation and action values, rather than equality with sampled correctness
on every trajectory. Away from calibrated α, τv, undiscounted accumulation instead optimizes
terminal verifier utility and need not preserve outcome behavior. The calibrated γ = 1 treatment also
differs from the perturbed-potential reward realization in Table 20.
Optimal actions under the cumulative reward. At each parameter setting we compute the
complete finite-tree Bellman optimum,
Q∗
α,τv,γ(h, a) = EH ′|h,a

¯rα,τv(h, a, H′) + γV ∗
α,τv,γ(H ′)

,
V ∗(h) = max
a
Q∗(h, a), V ∗(hterminal) = 0. (51)
The expectation uses the true posterior-predictive law pb, even when the reward uses qτv. DP is an
objective audit only; training receives realized scalar rewards. Let W = DBK ; it is not assumed to
be a subset of D. On either fixed set S ∈ {D, W }, define
bgh = d−1
h

max
a∈A∗
out(h)
Q∗
α,τv,γ(h, a) − max
a /∈A∗
out(h)
Q∗
α,τv,γ(h, a)

,
GS = min
h∈S
bgh, v S = 1
|S|
X
h∈S
1{bgh ≤ 0}.
(52)
The gap is +∞ when every legal action is outcome-optimal. Strict preservation on S is equivalent to
GS > 0, or vS = 0; a zero gap already permits an outcome-suboptimal tie. The positive normalization
changes neither signs nor boundaries and is used only for gap display. OptMass and regret use raw
cumulative Q∗, following Appendix G.2.
On W , the margin conditions imply bgh(1, 1, 0) ≤ − 0.02 andbgh(1, 1, 1) ≥ 0.02. Finite-horizon
action values and the minimum over this finite set are continuous in γ. Hence GW crosses zero at
least once in (0, 1), and a neighborhood of γ = 1 preserves all histories in W . The gap need not be
monotone in γ, so the crossing need not be unique.
Training. At α = τv = 1, we train at
γ ∈ {0, .25, .50, .70, .85, .90, .95, .98, .99, 1}.
All ten configurations follow Appendix G.5, with five seeds, matched initialization and task distribu-
tion, and final-budget checkpoints. We set γPPO = γ and λGAE = 1, so value targets are the returns
in (48). Oracle ordering is audited on both D and W ; candidate distances and objective alignment use
D, and Bayes/KG top-action agreements use W . The specification and credit sweeps have separate
recorded configurations.
32

## B-31c41dbed7fe4b

candidate openreview-8OOMlVFxb0 PDF page 11

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
Michael Laskin, Luyu Wang, Junhyuk Oh, Emilio Parisotto, Stephen Spencer, Richie Steigerwald,
DJ Strouse, Steven Hansen, Angelos Filos, Ethan Brooks, Maxime Gazeau, Himanshu Sahni,
Satinder Singh, and V olodymyr Mnih. In-context reinforcement learning with algorithm distillation.
In International Conference on Learning Representations, 2023.
Dahyun Lee, Jonghyeon Choi, Jiyoung Han, and Kunwoo Park. Journalism-guided agentic in-context
learning for news stance detection. In Proceedings of the 2025 Conference on Empirical Methods
in Natural Language Processing, 2025.
Jonathan N. Lee, Annie Xie, Aldo Pacchiano, Yash Chandak, Chelsea Finn, Ofir Nachum, and Emma
Brunskill. Supervised pretraining can learn in-context reinforcement learning. In Advances in
Neural Information Processing Systems, 2023.
Lihong Li, Wei Chu, John Langford, and Robert E. Schapire. A contextual-bandit approach to
personalized news article recommendation. In International Conference on World Wide Web, 2010.
Haodong Liang and Lifeng Lai. Transformers provably implement in-context reinforcement learning
with policy improvement. arXiv preprint arXiv:2605.05755, 2026.
Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan
Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step.arXiv preprint
arXiv:2305.20050, 2023.
Licong Lin, Yu Bai, and Song Mei. Transformers as decision makers: Provable in-context reinforce-
ment learning via supervised pretraining. In International Conference on Learning Representations,
2024.
Michael Lutz, Arth Bohra, Manvel Saroyan, Artem Harutyunyan, and Giovanni Campagna. WILBUR:
Adaptive in-context learning for robust and accurate web agents. arXiv preprint arXiv:2404.05902,
2024.
Andrew Y . Ng, Daishi Harada, and Stuart Russell. Policy invariance under reward transformations:
Theory and application to reward shaping. In International Conference on Machine Learning,
1999.
Qwen, An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, et al. Qwen2.5 technical
report. arXiv preprint arXiv:2412.15115, 2025.
Alessio Russo, Ryan Welch, and Aldo Pacchiano. In-context learning for pure exploration. In
International Conference on Learning Representations, volume 2026, pp. 14493–14509, 2026.
Daniel Russo, Benjamin Van Roy, Abbas Kazerouni, Ian Osband, and Zheng Wen. A tutorial on
thompson sampling. Foundations and Trends in Machine Learning, 2018.
Burr Settles. Active learning literature survey. Technical report, University of Wisconsin–Madison,
2009.
Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion:
Language agents with verbal reinforcement learning. InAdvances in Neural Information Processing
Systems, 2023.
Richard S. Sutton. Integrated architectures for learning, planning, and reacting based on approximat-
ing dynamic programming. In International Conference on Machine Learning, 1990.
Richard S. Sutton and Andrew G. Barto. Reinforcement Learning: An Introduction. MIT Press, 2018.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz
Kaiser, and Illia Polosukhin. Attention is all you need. Advances in neural information processing
systems, 30, 2017.
Johannes von Oswald, Eyvind Niklasson, Ettore Randazzo, João Sacramento, Alexander Mordvintsev,
Andrey Zhmoginov, and Max Vladymyrov. Transformers learn in-context by gradient descent. In
International Conference on Machine Learning, 2023.
11

## B-385a6972885ab0

candidate openreview-8OOMlVFxb0 PDF page 33

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
Table 21: Ordering violations and minimum action-value gaps at α = τv = 1. Counts and cost-
normalized gaps are computed on the indicated diagnostic sets. Zero counts denote no violations,
rather than a rounded small percentage. Values bracket crossings on W in (.90, .95) and on D in
(.98, .99), subject to the numerical precision scope stated below.
D, 4,096 histories W , 1,024 histories
γ Violations GD Violations GW
.00 1540 -.078000 1024 -.103180
.25 1428 -.069700 1001 -.101249
.50 1076 -.043800 836 -.087732
.70 628 -.020600 482 -.060792
.85 231 -.006280 164 -.027286
.90 110 -.002570 58 -.013090
.95 24 -.000410 0 +.002774
.98 3 -.000026 0 +.013133
.99 0 +.000014 0 +.016730
1.00 0 +.000057 0 +.020400
The last observed violations occur in different intervals on W and D. At γ = 1, their minimum
gaps are 0.0204 and 0.000057, respectively, consistent with the margin filter used only forW . The
numerical brackets apply to these finite sets.
Numerical precision of the brackets. The endpoint action-set identities and existence of a crossing
on W follow analytically. Interior brackets in Table 21 are reported numerical DP results; an exact
critical discount or uniqueness is not claimed. The small positive gap GD(.99) = 1 .4 × 10−5
is sensitive to numerical error. Certifying its sign requires verified outcome-optimal sets and an
action-value error bound: if ϵQ bounds cost-normalized value error, an estimated positive gap must
exceed 2ϵQ; a raw-value bound must first be divided by dh.
Table 22: Complete five-candidate profiles for the credit-assignment sweep at α = τv = 1 on D,
mean ± SD across five seeds. These are distances to behavioral references, not hard cumulative-
objective optima.
γ Bayes TV Two-step TV KG TV Entropy TV Open-loop TV
.00 .218 ± .012 .172± .013 .038± .006 .142± .012 .277± .014
.25 .211 ± .012 .166± .012 .048± .007 .151± .012 .278± .013
.50 .179 ± .011 .129± .011 .073± .009 .172± .013 .281± .014
.70 .128 ± .010 .077± .008 .118± .011 .205± .013 .283± .013
.85 .081 ± .010 .063± .009 .157± .013 .226± .014 .285± .015
.90 .061 ± .008 .069± .010 .168± .014 .239± .014 .286± .014
.95 .052 ± .007 .080± .010 .177± .014 .247± .014 .288± .014
.98 .049 ± .007 .084± .013 .180± .014 .250± .012 .290± .016
.99 .048 ± .007 .085± .010 .180± .014 .249± .014 .289± .012
1.00 .049 ± .007 .086± .011 .178± .014 .249± .015 .287± .011
Table 23: Performance across credit discounts, agreement with the cumulative objective on D, and
agreement with Bayes DP and KG on W . Return, OptMass and raw-unit regret are mean ± SD
across five seeds. Agreement columns are means only and sum to 100%. Except at γ = .90, the same
candidate is nearest in all five seeds. At γ = .90, three seeds are closest to Bayes DP and two to
two-step, so the condition is labeled hybrid/unidentified.
γ Nearest Return OptMass Regret Hard agreement on W
Bayes KG Neither
.00 KG .711 ± .009 .830± .018 .005± .001 6.9% 90.5% 2.6%
.25 KG .716 ± .010 .824± .019 .006± .002 9.1% 87.3% 3.6%
.50 KG .725 ± .010 .809± .020 .008± .002 21.0% 72.1% 6.9%
.70 Two-step .737 ± .011 .786± .023 .009± .002 49.0% 42.4% 8.6%
.85 Two-step .744 ± .011 .792± .022 .010± .002 76.7% 17.5% 5.8%
.90 Hybrid .748 ± .010 .796± .021 .010± .002 84.3% 11.4% 4.3%
.95 Bayes .750 ± .010 .797± .020 .011± .002 87.8% 8.8% 3.4%
.98 Bayes .751 ± .010 .801± .020 .011± .002 88.4% 8.4% 3.2%
.99 Bayes .750 ± .011 .800± .021 .011± .002 88.6% 8.2% 3.2%
1.00 Bayes .750 ± .011 .796± .020 .011± .002 87.9% 8.8% 3.3%
33

## B-40ea9f18b7941f

candidate openreview-8OOMlVFxb0 PDF page 1

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
WHAT ALGORITHM CAN TRANSFORMERS LEARN IN
CLOSED -L OOP INTERACTION ?
Anonymous authors
Paper under double-blind review
ABSTRACT
The learning algorithm view of in-context learning (ICL) studies how fixed-
parameter Transformers learn from supplied examples. Language model agents
extend this setting through interaction: their actions determine what evidence en-
ters context next. We call this regime Agentic In-Context Learning (Agentic ICL).
Existing studies largely depend on externally supplied contexts or reward-bearing
interaction histories, while work on general tool-using agents lacks a learning
algorithm view. We represent an interactive learner by its state, update, and de-
cision rule, covering active learning, bandits, and online reinforcement learning
(RL). For expressivity, we construct causal Transformers that approximate these
algorithms over a finite horizon, and bound the resulting loss in return. For training,
we characterize when optimizing process rewards preserves behavior that maxi-
mizes the final outcome. Distillation experiments show that Transformers can learn
to execute three representative recursions. We then train models from outcome
or process rewards without oracle action or state targets, as in RL post-training.
Different rewards yield distinct decision policies. Improving the alignment of pro-
cess supervision with outcome-optimal action preferences shifts learned decisions
accordingly. Such behavioral differences persist in a pretrained language model
across textual paraphrases.
1 I NTRODUCTION
In-context learning (ICL) is a central way in which language models adapt at inference time: informa-
tion in the prompt changes subsequent predictions while the model parameters remain fixed. This has
motivated a learning algorithm view of ICL, which asks what estimator, update rule, or other learning
computation a Transformer (Vaswani et al., 2017) implements through its forward passes over an
externally supplied prompt (Xie et al., 2022; Garg et al., 2022; Akyürek et al., 2023; von Oswald
et al., 2023; Bai et al., 2023; Wu et al., 2025).
Modern language-model agents routinely operate in an analogous but closed-loop regime. An agent
can browse the web, call tools, edit code, or run experiments, then use the returned results to choose
later actions (Yao et al., 2023; Shinn et al., 2023; Zhao et al., 2024; Lutz et al., 2024). A search
query determines which page is read, a code edit determines the next test result, and an experiment
determines the next measurement. The agent therefore does not merely learn from a supplied context:
through its actions, it helps determine the context from which it will learn next.
We call this execution regimeAgentic In-Context Learning (Agentic ICL). Starting from an initial
prompt or task description, a fixed-parameter model chooses an action, receives feedback, and
incorporates that feedback into its next decision. Its context grows through interaction with the
environment. The returned feedback can be a search result, compiler error, measurement, critique, or
reward. This motivates extending the learning algorithm view of ICL to interactive computations in
which decisions shape subsequent evidence. The central question is:
What interactive algorithms can Transformers learn in context, and how do training
objectives shape their behavior?
In-context reinforcement learning (ICRL) provides the closest precedent (Laskin et al., 2023; Lee
et al., 2023; Lin et al., 2024; Wang et al., 2025; Liang & Lai, 2026), but requires scalar rewards to be
1
Reviewers:pleasereadtheReviewerGuidelines(iclr.cc/Conferences/2027/ReviewerGuidelines)andtheAIPolicyforReviewers(iclr.cc/Conferences/2027/AIPolicyForReviewers).
If you used AI to expand, edit, or polish your review, please provide the input text to the LLM. Better still, consider skipping the LLM and submitting your original text: we,
and the authors, are much more interested in your unedited thoughts than in what an LLM has to say. AI-assisted or not, you are putting your name and reputation behind
your review: LLM-generated falsehoods, hallucinations or misrepresentations are subject to disciplinary action, which may include desk-rejecting all papers you have authored.

## B-4347e3c72e3df3

candidate openreview-8OOMlVFxb0 PDF page 8

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
Bayes
DP*
One-step
KG
Entropy Open-loop0.0
0.1
0.2
0.3Action-kernel TV ↓
0.043
0.182
0.249
0.286
(a) Outcome
reward
Autonomous return = 0.755
Bayes
DP
One-step
KG*
Entropy Open-loop
0.219
0.047
0.138
0.275
(b) One-step
process reward
Autonomous return = 0.710
Bayes
DP*
One-step
KG
Entropy Open-loop
0.046
0.184
0.254
0.289
(c) Outcome-preserving
process reward
Autonomous return = 0.752
Bayes
DP*
One-step
KG
Entropy Open-loop
0.018
0.214
0.267
0.301
(d) Bayes DP-score
distillation
Autonomous return = 0.764
Figure 3: Distances to candidate policies under four training objectives. Each panel reports policy
TV to the four candidates on a shared diagnostic set.
0 .25 .50 .70 .85 .90 .95 .98 .99 1
Credit discount γ (evaluated grid)
0
20
40
60
80
100Diagnostic histories (\%)
(a) Ordering condition
Preserved ratio
Violated ratio
0 .25 .50 .70 .85 .90 .95 .98 .99 1
Credit discount γ (evaluated grid)
0
20
40
60
80
100Hard top-action agreement (\%)
(b) Learned decisions
Bayes
KG
0 .25 .50 .70 .85 .90 .95 .98 .99 1
Credit discount γ (evaluated grid)
0.70
0.72
0.74
0.76Terminal return
(c) Autonomous return
Figure 4: Varying the credit discount γ at α = τv = 1. The gray band marks the common order-
ing/decision crossover; the green band marks zero oracle violations, after which learned agreement is
nearly constant.
sweep over (α, τv) (Appendix G.6). The primary (.75, .75) result is not an isolated parameter setting:
the nearest candidate changes with the verifier reward specification, while the primary KG-like
behavior persists across a neighborhood of tested settings. All tested one-step reward settings with
γ = 0 exhibit ordering violations on the diagnostic set and are closest to candidates other than Bayes
DP.
Verifier calibration and credit assignment. We next isolate credit assignment γ while holding
the local score (α, τv) fixed. We vary γ to test when the objective satisfies the ordering condition
in Proposition 5.1. We fix α = τv = 1 because at γ = 0, its optimal-action set coincides with that
of one-step KG; at γ = 1, its expected cumulative return equals the expected outcome return up
to an action-independent baseline, so its optimal-action set coincides with that of Bayes DP. Now
the ordering condition in Proposition 5.1 depends on γ and on the histories being evaluated. We
prespecify a margin-separated set of diagnostic histories that distinguish Bayes DP from KG and use
it to evaluate how ordering preservation and learned behavior change with γ.
Figure 4 tests Proposition 5.1’s ordering criterion empirically. Panel (a) reports the fractions of
diagnostic histories satisfying or violating A∗
S,t(h) ⊆ A ∗
out,t(h), and panel (b) reports the learned
policies’ top-action agreement with Bayes DP and KG. Both pairs of curves cross betweenγ = .50
and .70. On this diagnostic set, the proposition’s strict condition is reached between .90 and .95,
when the violation rate becomes zero; thereafter learned agreement and terminal return remain
nearly constant. Thus extending credit moves the objective from KG-like local ordering to Bayes
DP-consistent ordering, and the trained policies follow the same transition. Appendix G.8 describes
how we construct the diagnostic sets and reports agreement with each objective’s optimal actions,
minimum action-value gaps, and comparisons with additional candidates.
Returning to the state–update–decision decomposition, posterior decoding and update-identity checks
yield similar errors across objectives despite their different decisions. These supporting diagnostics
and controlled decision tests are reported in Appendix G.3.
8

## B-43e9425595b186

candidate openreview-8OOMlVFxb0 PDF page 4

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
3.2 I NTERACTIVE LEARNING ALGORITHM
In the coding example, the agent maintains an information state, updates it after each tool result, and
uses it to select the next search or code execution. Thus an interactive learner can be described by a
sufficient state st before action t, an update Ut, a decision rule Gt, and legal actions Lt(st). Coupled
to the environment step in Definition 3.1, its learner’s recursion is
s1 = U0(x0), a t ∼ Gt(· | st), s t+1 = Ut(st, at, xt), t =1 , . . . , H. (2)
The induced history policy is Gt(· | st(ht−1)). The environment KM supplies feedback, while the
learner maps (Ut, Gt) incorporate it and select the next action.
This factorization separates how evidence is incorporated from how actions are selected. Consider
three representative and widely studied settings of learning problems: active learning selects queries
and receives labels to improve downstream predictions; bandits select an arm and reveal its outcome
for cumulative reward or regret; and online RL controls both immediate feedback and future states
for long-horizon return or regret. They are all included in this framework and distinguished by how
actions shape future context. At the interface level, any finite-horizon policy can be expressed in this
recursive form by taking st = ht−1. Importantly, the feedback need not itself be the task reward,
separating the records used for in-context adaptation from the task objective. Appendix A gives
instantiations.
4 COMPILING INTERACTIVE LEARNING ALGORITHMS INTO TRANSFORMERS
The framework expresses an interactive algorithm through its state, update, and decision rule. We
now construct a frozen causal Transformer that executes (2) by serializing the transcript, routing the
state between turns, incorporating feedback, and producing the next action distribution.
Assume fixed-width encoders Ex and Ea for public records and actions. We serialize the prompt and
extend it recursively, for1 ≤ t < H :
Prompt(h0) = [Ex(x0), SUM, ACT],
Prompt(ht) = [Prompt(ht−1), Ea(at), Ex(xt), SUM, ACT]. (3)
Each field occupies one vector token. The SUM token provides workspace for the learner state; the
final ACT token emits the next action. The action and its returned record are then appended to form the
next prompt. This encoding makes the learner’s computation explicit. It is a non-exclusive abstraction
of LLM agents’ data flow, not a lossless encoding of arbitrary natural-language records.
Given this serialization, the following theorem states that a frozen causal Transformer can uniformly
realize the policy of any regular finite-horizon recursion with arbitrarily small error. Appendix D
gives the proof.
Theorem 4.1 (Interactive-algorithm compilation). Fix H and a learner of the form in (2). Assume
compact fixed-width encodings of records, actions, and learner states; uniformly Lipschitz initializa-
tion, updates, and finite decision logits admitting feed-forward approximation; and a finite action
vocabulary with a public-history legality mask. Let each decision kernel be the masked softmax of
these logits. For every ϵ > 0, there is a frozen causal Transformer of depth at most O(H) satisfying
max
1≤t≤H
sup
legal ht−1
TV(πθ(· | Prompt(ht−1)), Gt(· | st(ht−1))) ≤ ϵ.
Table 1 illustrates how representative learners instantiate the state-update-decision interface. Both
the settings and the algorithms within each setting are illustrative rather than exhaustive. Details are
provided in Appendix A.
5 T RAINING OBJECTIVES AND BEHAVIORAL DIAGNOSIS
Section 4 establishes that Transformers can represent these interactive policies. We next characterize
which decisions different training objectives favor, and introduce diagnostics for examining the
policies beyond task performance alone. We first define task value to evaluate their autonomous
performance.
4

## B-44b9551cbbd692

candidate openreview-8OOMlVFxb0 PDF page 20

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
writes bψ(x0, au, xu) into its statistic slot. One additional head can broadcast the unique initial-task
token to every record position. These operations occur simultaneously for every completed turn.
At the workspace for decision t, an aggregation head assigns score C to every preceding completed-
record token and score zero to every other token. Conditional on the target set, softmax is uniform,
so for n = t − 1 ≥ 1 the head returns an approximation to
1
n
nX
u=1
bψ(x0, au, xu). (39)
There are at most NH tokens. The total attention mass on non-record tokens is at most NH e−C;
hence bounded value vectors give uniform aggregation error tending to zero as C → ∞. The public
turn coordinate supplies n. A position-wise network multiplies (39) by n, uses a zero-count gate at
t = 1, and applies bF . A final block appliesbℓ and the legal-action mask.
Let Bψ bound ψ, let δψ be its feed-forward approximation error, and let rC → 0 bound the attention-
average error. Before applying F , the summed-statistic error is at most
H(δψ + rC). (40)
Uniform continuity (or the stated Lipschitz constants) of F and ℓ, followed by the softmax TV bound
used in (37), shows that choosing C and the feed-forward approximators sufficiently accurately
makes the state and action-kernel errors at most ϵ. The pairing/statistic block, aggregation/state block,
and readout block give depth at most three for every H. Their weights may depend on the fixed
maximum horizon through C and their approximator sizes, as the proposition states.
For a finite Bayesian task with reference hypothesis m0, conditional independence gives
log bt(m)
bt(m0) = log b1(m)
b1(m0) +
X
u<t
log Km(xu | au)
Km0(xu | au) . (41)
Positive likelihoods make every summand bounded and Lipschitz on the stated compact domain;
softmax recovers bt. For UCB, summing [eau , rueau] gives (Nt, St), after which the pseudocount-
regularized index is a continuous readout. These are the two claimed instances. □
Tabular Q-learning generally lacks (38) because each target depends on the previously updatedQ-
table, so its available guarantee remains the sequential construction of Theorem 4.1. This comparison
concerns only the two constructive upper bounds.
F F ROM POLICY APPROXIMATION TO RETURN BOUNDS
Action-kernel agreement on fixed histories must also control autonomous execution, where an action
mismatch can change subsequent observations. The following result uses the task value defined in
(4).
Proposition F.1 (Closed-loop outcome bridge). For policies π and µ, let Ht−1 denote the pre-action
history generated by π in task M. Then
|VM(π) − VM(µ)| ≤ B min
(
1,
HX
t=1
E TV(π(· | Ht−1), µ(· | Ht−1))
)
.
Consequently, Theorem 4.1 implies an outcome gap at most BHϵ .
Couple actions from π and µ maximally at every history generated by π, and, while their actions
agree, use the same environment randomness. At turn t, conditional on no previous mismatch, the
probability of a new mismatch is the action TV at the common history. A union bound and iterated
expectation give the sum of the expected action TV distances in Proposition F.1. If no action differs,
the coupled trajectories and outcomes are identical. Since the outcome range has length at most B,
their expectation difference is at most B times the mismatch probability, capped at B. □
20

## B-48033c04ba230a

candidate openreview-8OOMlVFxb0 PDF page 6

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
The set is algorithm-separating at scale ∆D > 0 when every candidate pair is at least that far apart.
Because ordinary rollouts may miss budget, posterior, or confidence boundaries where algorithms
disagree, we find legal high-disagreement histories by exact search and freeze D before inspecting
the Transformer.
Proposition 5.2 (Identification on separating histories). Suppose D is algorithm-separating at scale
∆D, and for some k, dD(π, πk) ≤ ϵ. Then πk is the unique closest candidate whenever ∆D > 2ϵ. If
every empirically estimated candidate distance has absolute error at most ζ, the empirical nearest
candidate is still k whenever ∆D > 2ϵ + 2ζ.
This follows directly from the triangle inequality and provides a sufficient condition for stable nearest-
candidate identification. This diagnostic identifies the closest policy within the specified candidate
family. It does not identify a unique internal algorithm.
6 E XPERIMENTS : E XECUTING AND DISCOVERING INTERACTIVE
ALGORITHMS
Our experiments examine learned execution and objective-dependent decisions. Section 6.1 introduces
an exactly diagnosable environment and task; Section 6.2 tests learned compilation from oracle
algorithm supervision, to support Theorem 4.1; Section 6.3 diagnoses behavior under outcome and
process objectives and how it changes under objective interventions, supporting Proposition 5.1;
Section 6.4 confirms these results using a pretrained LLM with natural-language tools. Unless noted
otherwise, metrics are averaged within each seed and reported as mean ± standard deviation across
five independently trained seeds.
6.1 BTS: AN EXACTLY DIAGNOSABLE AGENTIC ICL ENVIRONMENT
Multi-round Bayesian Tool Selection (BTS) models sequential tool use while keeping its optimal
policy exactly computable. Each task asks the agent to predict a hidden target Z ∈ [K] using tools
e ∈ [E] with likelihoods Le(y | z) = Pr(Y = y | Z = z, tool e), costs ce, discount δ, and a query
budget. A tool-call action e returns an observation Y ∼ Le(· | Z), which is appended to the next
prompt; an answer action g ∈ [K] terminates the episode with reward δC1{g = Z}, where C is
the total call cost. Tools are legal only while calls remain and their costs fit the budget; answers
are always legal. The initial prompt contains all task-specific parameters, and is followed by the
action-evidence transcript.
Bayes dynamic programming (Bayes DP) computes an optimal policy for this task. At history ht−1,
Bayes DP makes decisions from a sufficient state, consisting of the posterior bt(z) = Pr(Z = z |
ht−1), remaining call horizon, and remaining budget. It compares immediate answers with the
discounted value of future adaptive queries and is exactly outcome-optimal in this finite known
environment. Appendix G gives details of this optimal policy.
Priors, likelihood matrices, labels, costs, discounts, budgets, and query horizons are randomized
across episodes, preventing a fixed tool-calling script from matching the task-specific oracle. We
evaluate autonomous return on fresh tasks and exact action probabilities on frozen diagnostic histories.
Longer-horizon results control for budget feasibility and realized interaction length; Appendix G
gives the complete task distribution and protocol.
6.2 L EARNED COMPILATION : CAN TRANSFORMERS EXECUTE THE RECURSION ?
The construction establishes the existence of Transformer parameters that execute interactive recur-
sions. We now test whether supervised training can recover such behavior. We select representative
algorithms whose states, updates, and policies can all be computed exactly, allowing us to check
each part of the learned recursion. We train a Transformer by supervised distillation from three such
algorithms: Bayes DP for active learning, Beta-Bernoulli UCB for bandits, and tabular Q-learning
for online RL. Within the same interface, these algorithms require Bayesian updating with planning,
count-sum confidence statistics, and bootstrapped value updates, respectively.
Figure 2 compares distilled models with task-specific random Transformer baselines on action choices,
state reconstruction, updates, and autonomous performance, and shows the change in action TV
6

## B-4d969d9dd70143

candidate openreview-8OOMlVFxb0 PDF page 23

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
Softening unregularized scores differs from solving an entropy-regularized objective, which also
changes continuation values. All reward-trained conditions have an entropy-free final phase; their
objective alignment is evaluated against the corresponding unregularized optimal-action sets.
The one-step KG candidate replaces the continuation value after a query by maxz B(b; e, y)(z):
QKG(b, e) = δce
X
y
pb(y | e) max
z
B(b; e, y)(z).
It compares this value with immediate stopping but ignores the value of later adaptive queries. At a
history with remaining query horizonℓ, the receding two-query-lookahead candidate instead evaluates
the Bayes recursion after replacing ℓ by min{2, ℓ}. It uses the same budget, likelihoods, costs, and
score temperature τ = 0 .02, and replans after every returned observation; it is not an open-loop
two-tool sequence. Candidate kernels that coincide on an evaluation set share an equivalence label,
as full Bayes and two-step lookahead do throughout any at-most-two-query evaluation.
The entropy candidate ranks legal tools by {H(b) −P
y pb(y | e)H(B(b; e, y))}/ce, with the same
stopping comparison. The open-loop oracle chooses an entire legal tool sequence from public task
fields before observing any query outcome, then makes the Bayes-optimal final prediction from all
returned observations. Enumeration covers every sequence within the total budget and every possible
stopping length. Its final answer is therefore observation-dependent even though its acquisition plan
is feedback-insensitive.
Autonomous returns use fresh tasks with sampled environment outcomes; action-kernel metrics use
exact frozen-model logits. The candidate distance in (7) uses uniform history weights on the primary
diagnostic set. For evaluations using task-balanced weights, we average multiple prefixes within each
task before averaging across tasks; the length decomposition uses its stated horizon/depth weights.
Candidate distances, runner-up gaps dsecond − dfirst, and other metrics are computed per seed before
means and standard deviations are formed. Tables identify entries available only as means.
For objective alignment, let A∗
S(h) and Q∗
S(h, a) be the hard optimal set and unregularized action
values for the condition’s actual final-phase objective. On the frozen histories{hi}N
i=1, we report
OptMassS(π) = 1
N
NX
i=1
X
a∈A∗
S(hi)
π(a | hi),
RegretS(π) = 1
N
NX
i=1
"
max
a
Q∗
S(hi, a) −
X
a
π(a | hi)Q∗
S(hi, a)
#
.
We additionally report hard top-action agreement on histories with a unique maximizing action and
an action-value margin of at least 0.02. For the outcome-reward condition, S is terminal BTS return
and the aligned set is hard Bayes DP. For the one-step process reward condition,S is the expected
immediate verifier score and the aligned set is computed by exact enumeration of the next observation;
the verifier-optimal action set need not coincide with a candidate’s maximizing-action set, except at
the analytically characterized endpoints.
For outcome regret in the trainer’s return units, the Bayes recursion values cached after a history are
multiplied by the positive factor δC(h) accounting for already-incurred cost. This does not change
hard optimal actions.
Regret is measured in each objective’s own units, so values across different objectives or credit
discounts are not directly comparable.
G.3 C ANDIDATE -DISAGREEMENT DIAGNOSTIC HISTORIES
We construct the diagnostic sets from task and oracle quantities before evaluating the models, then
hold the histories and evaluation weights fixed. On 200,000 independently generated BTS tasks,
a proposal mixture of the original four candidates and a random legal policy generates reachable
prefixes. For each history, we compute the exact policies, all pairwise TVs, posterior entropy, and
remaining resources. After requiring a maximum pairwise TV of at least 0.10, a deterministic
round-robin procedure selects D, a set of 4,096 histories balanced across (i) the maximally separated
23

## B-50994562f36c87

candidate openreview-8OOMlVFxb0 PDF page 21

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
G A DDITIONAL EXPERIMENTAL DETAILS
G.1 BTS TASK DISTRIBUTION AND INTERACTION LENGTHS
We sample each complete task before its trajectory begins. The default family has K = 4 hypotheses,
E = 6 tools, and three outcomes per tool. Each hypothesis combines a binary group with a within-
group bit. The tool library contains a noisy group diagnostic, two group-specific bit specialists, weaker
group and bit shortcuts, and one random distractor. Tool accuracies are perturbed independently
across tasks, and every categorical probability is at least 0.02, and hypothesis, tool, and per-tool
outcome labels are randomly permuted. The useful hierarchy therefore persists without admitting a
fixed token-level routing codebook. The prior is a perturbed near-uniform Dirichlet draw.
For the BTS protocol used by both the symbolic and textual conditions, task content and resource
variables are sampled independently except for the cost-support condition below. In primary training,
H ∼ Unif{2, 3, 4}, q ∼ Unif{2, . . . ,8}, c e
iid
∼ Unif{1, 2} conditional on min
e
ce = 1,
and δ ∼ Unif[0.96, 0.995], independently. Thus budget is not capped by the sampled horizon, and
every budget value later used in the longer-horizon evaluation already occurs during short-horizon
training. Tools may be called repeatedly while legal. Training, diagnostic selection, and evaluation
use independently seeded task streams.
The complete longer-horizon test distribution retains the training distributions of q, c1:E, δ, priors,
and likelihood libraries and fixes H ∈ {6, 8}. We prespecify two resource strata within this common
distribution. The nominal-horizon control has q ≤ 4, so it cannot execute more than four calls despite
the larger value of H. The feasible-long stratum has q ≥ H, namely q ∈ { 6, 7, 8} at H = 6 and
q = 8 at H = 8. Because mine ce = 1, this stratum admits H calls, although a policy may stop
earlier. For every task and policy we record
Ncalls ≤ min
n
H,
j
q/ min
e
ce
ko
,
and report its empirical probability mass function, mean, median, 90th percentile, Pr(Ncalls > 4),
and Pr(Ncalls = H). We use longer-interaction extrapolation only for results supported by executed
trajectories with Ncalls > 4; a change in nominal H alone is described as a horizon-field intervention.
Table 3: Joint budget-horizon protocol for symbolic BTS. The two longer-horizon rows are pre-
specified strata of a test distribution whose budget values and cost support are already present
during training. Feasibility does not imply execution; actual policy-dependent call lengths are
reported separately.
Split H q Cost law Purpose
Training Unif{2, 3, 4} Unif{2, . . . ,8} ce ∼ Unif{1, 2}, c min = 1 short-horizon training
In-distribution test {2, 4} same same short-horizon reference
Nominal-horizon control {6, 8} q ≤ 4 same no calls beyond four
Feasible-long test 6 / 8 q ≥ 6 / q = 8 same longer calls feasible
We evaluate 8,192 fresh feasible-long tasks per seed at H0 = 6 and q ∈ {6, 7, 8}, with the remaining
generator distributions unchanged and task selection independent of realized policy behavior. The
complete aggregate call-count probability vectors for Ncalls = 0, . . . ,6 are
hard Bayes: [.000, .040, .390, .320, .170, .060, .020],
outcome reward, 6L/256W: [.010, .090, .350, .320, .180, .040, .010],
Table 4: Autonomously executed interaction lengths on the prespecified feasible-long stratum. The
distribution is H0 = 6, q ∈ {6, 7, 8}, with unchanged likelihood, prior, cost, and discount laws. Value
gaps use the same unfiltered stratum; a nonzero long-call tail supports limited autonomous length
extrapolation, not a claim that most episodes require six calls.
Policy Mean Median 90th pct. Pr(N > 4) Pr( N = 6) Gap to Bayes ↓
Hard Bayes oracle 2.88 3 4 8.0% 2.0% 0
Outcome reward, 6L/256W 2.73 3 4 5.0% 1.0% 0.019 ± 0.004
21

## B-5153ff5e1dc1f3

candidate openreview-8OOMlVFxb0 PDF page 3

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
Tool agents and interactive language feedback. Tool agents append search results, test outputs,
or other feedback to the context (Yao et al., 2023; Shinn et al., 2023; Zhao et al., 2024; Lutz et al.,
2024), but are usually evaluated by success or transfer. Work on language feedback instead studies
when language feedback is informative enough to enable efficient online learning (Xu et al., 2026)
or how to incorporate teacher-selected critique (Klissarov et al., 2026). We treat language as one
possible returned record and compare candidate descriptions of the model’s state, update rule, and
decision rule, separating compilation from behavior learned with terminal outcome reward. “Agentic
in-context learning” has also named a stance-aggregation method (Lee et al., 2025); we use the term
for the interaction regime in Definition 3.1.
Closed-loop learning settings and algorithms. We focus on learning settings in which the learner’s
input history is generated online through interaction: its actions affect which observations enter
context, rather than merely processing a dataset fixed in advance. This includes adaptive data
collection, where decisions determine which labels, measurements, rewards, or state transitions arrive
next. In active learning, previously observed labels guide the choice of subsequent queries to improve
downstream predictions (Settles, 2009); bandits reveal selected-arm rewards (Auer et al., 2002a; Li
et al., 2010; Russo et al., 2018; 2026); and online RL also controls persistent state and long-horizon
return (Sutton & Barto, 2018; Zanette & Brunskill, 2018). We instantiate BALD for active learning;
Thompson sampling, UCB, LinUCB, and EXP3 for bandits; and Q-learning, SARSA, actor-critic, and
learned-model planning for online RL, alongside VOI and KG for adaptive query selection (Frazier
et al., 2008; Auer et al., 2002b; Watkins & Dayan, 1992; Azar et al., 2017). Bayesian updating,
optimism, and planning recur across these settings.
Transformer expressivity for recursive algorithms. Universal approximation and recurrent-
depth Transformers establish broad expressivity (Yun et al., 2020; Dehghani et al., 2019). Our
construction exposes a sufficient-state wavefront, shares parameters across turns, and converts per-
action approximation into an autonomous return bound.
Process supervision and reward shaping. Process supervision scores intermediate steps, but
shaping can change the optimal policy unless action-value ordering is preserved (Lightman et al.,
2023; Cui et al., 2025; Cheng et al., 2025; Ng et al., 1999). We use potential-based shaping to
construct an outcome-preserving process-reward control.
3 A GENTIC ICL: A C LOSED -LOOP LEARNING FRAMEWORK
Consider an LLM agent asked to solve a coding task. It searches for documentation, executes code,
and uses the returned pages or errors to decide what to try next. Each action changes its future
evidence. We separate this process into the interaction that generates the transcript and the learner
computation that updates evidence and selects actions.
3.1 I NTERACTION WITH THE ENVIRONMENT
We first specify how the agent’s actions determine the observations added to its context. Let x0
be the initial prompt, containing the task description and any public information available before
interaction. Fix a task M, which contains the task parameters and any fixed episode-level latent state,
with environment kernel KM , a finite action space, and horizon H. Write πθ for the action policy
induced by the frozen causal Transformer Tθ. Define h0 = x0 and ht = (ht−1, at, xt), where at is
the t-th action and xt its returned record. Before action t, the model receives ht−1.
Definition 3.1 (Agentic in-context learning). An Agentic ICL episode is the closed loop
at ∼ πθ(· | ht−1), x t ∼ KM(· | ht−1, at), t = 1, . . . , H, (1)
This is called Agentic ICL as the parameters θ remain fixed during deployment, and learning in
context occurs through the dependence of πθ on the growing transcript ht−1.
This definition specifies the execution regime. For an LLM agent, πθ is typically a Transformer.
3

## B-59c779fcb368ef

candidate openreview-8OOMlVFxb0 PDF page 5

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
Table 1: Illustrative settings and algorithms covered by Theorem 4.1.
Setting State st Update Ut Decision Gt / examples
Active learning Labeled set, query pool,
posterior
Add queried label, update
posterior
BALD, value-of-information
query selection
Bandits Posterior or reward
statistics
Posterior or statistical
update
Thompson sampling, UCB
Online RL Values, policy parameters,
or learned model
TD, policy-gradient, or
model update
Q-learning, SARSA, actor-critic,
learned-model planning
Let M ∼ ρ be a task drawn from the training or evaluation distribution, and let RM(hH) ∈ [0, B]
score the final trajectory. For any policy π, its expected task value is
VM(π) = EhH ∼(π,KM)RM(hH). (4)
The return RM(hH) is trainer-side information and need not be revealed in xt.
Theorem 4.1 also controls this task value: if policies agree within ϵ at every legal history, autonomous
return differs by at most BHϵ (Proposition F.1, Appendix F).
5.1 W HAT IS THE OPTIMAL BEHAVIOR UNDER A SPECIFIC SUPERVISION OBJECTIVE ?
We consider outcome reward and process reward, which are commonly used in RL post-training of
language model agents. We characterize when maximizing cumulative process reward preserves
the actions that maximize the final outcome. For a supervision objective S, let RS,t(hH) be its
trainer-side return from decision t onward and µ a continuation policy. Define
Q∗
S,t(h, a) = sup
µ
Eµ[RS,t(HH) | Ht−1 = h, At = a], A∗
S,t(h) = arg max
legal a
Q∗
S,t(h, a). (5)
A policy is S-optimal at h when its support lies in A∗
S,t(h). This defines objective-optimal behavior,
not a unique implementation or a finite-sample convergence guarantee.
Terminal outcome reward provides the simplest instance. With terminal task return RM(hH),
set Rout,t(hH) = RM(hH) and write Q∗
out,t(h, a) = sup µ Eµ[RM(HH) | Ht−1 = h, At =
a], A∗
out,t(h) = arg maxlegal a Q∗
out,t(h, a). Then A∗
out,t(h) is the set of terminal-outcome-optimal
actions at h. For process supervision with step rewards erS
t and discount β, set RS,t(hH) =PH
u=t βu−terS
u , Q ∗
S,t(h, a) = supµ Eµ[RS,t(HH) | Ht−1 = h, At = a]. Process-optimal behavior
is determined by cumulative action values, not isolated step scores. To provide dense supervision
while preserving outcome-optimal behavior, the process reward must satisfy the ordering condi-
tion below.
Proposition 5.1 (When process supervision preserves outcome-optimal behavior). On any history
set, every process-optimal behavior is also outcome-optimal if and only if
A∗
S,t(h) ⊆ A ∗
out,t(h) at every history h. (6)
A strict ordering reversal makes process-optimal behavior outcome-suboptimal; a process tie that
includes an outcome-suboptimal action permits the two behaviors to differ.
A common way to densify supervision is to assign local step rewards (Ng et al., 1999; Lightman
et al., 2023; Cui et al., 2025) but this can violate the ordering condition above. A particularly myopic
scoreer(xt−1, a) depends only on the latest record and can overlook earlier evidence that changes the
value of an action. Appendix B proves the proposition. And when outcome rewards are available,
potential-based shaping can provide intermediate rewards while preserving outcome-optimal action
sets (Appendix C).
5.2 W HICH CANDIDATE ALGORITHM BEST DESCRIBES THE MODEL ’S ACTIONS ?
To examine what training produces, we compare the learned policy with candidate algorithms
on histories where their decisions differ. For candidate policies π1, . . . , πL and legal histories
D = {(hi, wi)}N
i=1 with wi ≥ 0 andP
i wi = 1, define
dD(π, µ) =
XN
i=1
wi TV(π(· | hi), µ(· | hi)) . (7)
5

## B-5aacc412fa6363

candidate openreview-8OOMlVFxb0 PDF page 22

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
In the q ≤ 4 nominal-horizon control, Pr(Ncalls > 4) = 0 is a structural budget bound and is not
interpreted as learned length control.
The corresponding H0 = 8, q = 8 feasible-long evaluation retains the likelihood, prior, cost, and
discount laws. Its aggregate call-count probability vectors for Ncalls = 0, . . . ,8 are
hard Bayes: [.000, .034, .351, .336, .176, .067, .026, .008, .002],
outcome reward, 6L/256W: [.009, .080, .340, .330, .176, .048, .014, .003, .000],
Table 5: Autonomous call counts on the separate H0 = 8 , q = 8 feasible-long stratum. The tail
beyond four calls supports limited autonomous length extrapolation; most episodes still terminate
earlier. Return gaps are mean ± SD across five seeds.
Policy Mean Median 90th pct. Pr(N > 4) Pr( N = 8) Gap to Bayes ↓
Hard Bayes oracle 3.011 3 5 10.3% 0.2% 0
Outcome reward, 6L/256W 2.799 3 4 6.5% 0.0% 0.028 ± 0.005
Differences from Table 4 cannot be attributed solely to horizon, since the budget strata also differ.
These autonomous distributions are distinct from the forced-prefix diagnostics used to evaluate
execution on long transcripts.
An oracle audit of 256 generated tasks yields mean values of 0.7701 for Bayes DP,0.7156 for KG,
and 0.6833 for the best open-loop design, corresponding to a mean adaptivity gap of 0.0868. Bayes
DP and KG differ at the initial decision by TV greater than 0.05 on 96.9% of these tasks. These
values diagnose the executable task generator rather than a learned model.
G.2 C ANDIDATE POLICIES AND EVALUATION CONVENTIONS
The prompt contains the prior, likelihood table, costs, discount, initial budget and horizon, and
the typed action-observation transcript. Before each decision, a public resource record repeats the
mechanically updated remaining budget and call horizon; this permits resource interventions without
editing evidence. The prompt never contains the sampled Z, posterior bt, oracle action values,
correctness, or return. For a query e, the exact predictive law and Bayes update are
pb(y | e) =
X
z
b(z)Le(y | z), B(b; e, y)(z) = b(z)Le(y | z)/pb(y | e).
For remaining query horizon ℓ and budget q, the legal set Lℓ(q) contains every answer and, when
ℓ ≥ 1, each tool with ce ≤ q. In units excluding already-incurred cost, the oracle recursion is
Qℓ(b, q, answer(g)) = b(g),
Qℓ(b, q, call(e)) = δce
X
y
pb(y | e)Vℓ−1(B(b; e, y), q − ce),
Vℓ(b, q) = max
a∈Lℓ(q)
Qℓ(b, q, a).
Memoized recursion over the finite outcome tree assigns each answer its posterior probability, each
query its discounted expected continuation value, and takes the maximum over legal actions to
compute unregularized Bayes DP action values Q∗
B(h, a). We distinguish two references derived
from these values:
A∗
B(h) = arg max
a∈Lℓ(q)
Q∗
B(h, a), π hard
B (a | h) = 1{a ∈ A ∗
B(h)}
|A∗
B(h)| ,
πscore
B,τ (a | h) = exp(Q∗
B(h, a)/τ)P
a′∈Lℓ(q) exp(Q∗
B(h, a′)/τ) .
We use πhard
B for outcome-optimal execution and the score-softened kernel for distillation and
behavioral comparison. The latter assigns positive mass to suboptimal actions. Bayes, KG, and two-
step candidate distances use the fixed temperature τ = 0.02, chosen independently of trained-model
distances. Entropy and open-loop acquisition are deterministic with lexicographic tie-breaking; the
open-loop terminal answer uses the same score-softened answer kernel.
22

## B-60d794395d59b7

candidate openreview-8OOMlVFxb0 PDF page 29

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
reward condition uses γPPO = 0, so every visited decision is trained from its own immediate verifier
score, Gt =er1V
t , without credit from later verifier scores. All decision positions still contribute to
the PPO loss. Value targets and standardized advantages follow the same implementation, and the
optimization budget is unchanged. Five initialization seeds are fixed in advance, all final-budget
checkpoints are reported, and no diagnostic history is used for checkpoint selection.
G.6 O NE-STEP PROCESS REWARD AND SPECIFICATION SENSITIVITY
The verifier forms an evidence aggregate from the public prior and likelihood rows in the transcript.
If history h contains completed calls (ei, yi), its evidence-temperature distribution is
qτv(z | h) = p0(z)Q
i Lei(yi | z)τv
P
z′ p0(z′)Q
i Lei(yi | z′)τv
, τ v > 0. (43)
Thus τv < 1 conservatively underweights each observation, τv > 1 overweights it, and τv = 1
recovers the exact Bayesian posterior. The verifier never observes the sampled targetZ, a candidate
action value, or a continuation value.
For a distribution q, define top-answer confidence C(q) = maxz q(z), normalized certainty I(q) =
1 − H(q)/ log K, and
Uα(q) = αC(q) + (1 − α)I(q), α ∈ [0, 1]. (44)
The two bounded terms capture complementary forms of apparent progress: confidence in the best
current answer and concentration of the full answer distribution. A query is scored by the verifier
utility after its returned observation. An answer g is scored by αq(g) + (1 − α)I(q); the certainty
term is common to all answer labels. Subtracting the best current utility Uα(q) gives the trainer
reward
er1V
α,τv(h, a, h′) =
(
δce Uα(qτv(· | h′)) − Uα(qτv(· | h)), a = call(e),
α[qτv(g | h) − C(qτv(· | h))] , a = answer(g).
(45)
This is a cost-adjusted local progress score in [−1, 1]. The subtraction is an action-independent
baseline: the best immediate answer receives zero, an inferior answer receives a negative score, and a
query receives a positive score only when its post-observation verifier utility offsets its cost. (45) is
computed after the realized observation and contains neither QKG nor any maximization over future
action sequences.
Because the process discount is β = 0, its exact action scores are simply
Sα,τv(h, a) = E

er1V
α,τv(h, a, H′) | h, a

, A1V
α,τv(h) = arg max
a
Sα,τv(h, a). (46)
The expectation in (46) is used only to audit the objective; training receives the realized scalar in (45).
At (α, τv) = (1, 1), for a query e,
S1,1(h, e) = δce
X
y
pb(y | e) max
z
B(b; e, y)(z) − max
z
b(z),
while S1,1(h, answer(g)) = b(g) − maxz b(z). The common baseline leaves action ordering un-
changed, so (α, τv) = (1, 1) has exactly the one-step KG maximizing set under immediate credit.
The primary setting (.75, .75) places three quarters of the utility weight on top-answer confidence
and conservatively tempers each likelihood contribution.
Immediate-credit specification sweep. To test sensitivity to the local verifier specification, we
fix immediate credit assignment, γPPO = β = 0 , and cross α ∈ { 0.50, 0.75, 1.00} with τv ∈
{0.50, 0.75, 1.00, 1.25}. All twelve cells use the shared architecture, training budget, and final-
checkpoint rule. This sweep varies confidence weighting and evidence tempering; Section G.8
instead fixes α = τv = 1 and varies the credit horizon γ. Let A∗
out(h) be the outcome-optimal action
set and define the exact ordering gap
gh(α, τv) = max
a+∈A∗
out(h)
Sα,τv(h, a+) − max
a− /∈A∗
out(h)
Sα,τv(h, a−). (47)
If every legal action is outcome-optimal, the second term is defined as −∞. Proposition 5.1 implies
exact preservation on a diagnostic family W if and only if gh(α, τv) > 0 for every h ∈ W . Equality
29

## B-6a6678d4db0dfd

candidate openreview-8OOMlVFxb0 PDF page 17

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
t < H , rR
H = RM(hH). Let Φt be any bounded real-valued potential on pre-action histories at turn
t, with terminal potential ΦH+1 ≡ 0. Set
erS
t = rR
t + βΦt+1(Ht) − Φt(Ht−1). (25)
The return telescopes, so Q∗
S,t(h, a) = βH−tQ∗
out,t(h, a) − Φt(h). Therefore, Q∗
S,t and Q∗
out,t have
the same greedy action sets. Appendix G.7 specifies the potential used in our experimental control.
D P ROOF OF THE PROMPT -LEVEL TRANSFORMER REALIZATION
Assumptions, architecture, and scope. Adjoin the turn counter to st, so the time-varying updates
and logits become common maps U and ℓ. Assume compact vector-token encodings, a finite global
action vocabulary, and a public-history legal-action mask supplied to the decoder. AssumeU0, U, ℓ
are uniformly Lipschitz and admit feed-forward approximations, withGt the masked softmax of ℓ(st).
The construction applies one weight-tied three-head update block H times and then one readout
block. Its residual width is O(H + dx + da + ds + |A|), aside from feed-forward approximator
width, and it neither allocates parameters per history nor enumerates histories.
The construction identifies residual coordinates for the learner state and its feedback-conditioned
update. It uses residual attention-ReLU blocks without layer normalization and treats empirical-model
states as pre-normalized. The result concerns representability of a fixed-width learner core; it does not
establish training convergence or lossless text encoding. We now give the construction for one vector
token per encoded field, using standard causal softmax attention and position-wise ReLU networks.
The proof follows explicit-coordinate constructions for static learner functions (Wu et al., 2025) and
exact RL updates (Liang & Lai, 2026); here, one shared block propagates a general recursive state
through a prompt generated by agent-environment interaction.
Transformer block. For residual vectors z1, . . . , zN ∈ Rdmodel, one causal head is
HeadQ,K,V (z)i =
X
j≤i
αijV zj, α ij = exp(⟨Qzi, Kzj⟩)P
k≤i exp(⟨Qzi, Kzk⟩) . (26)
A residual block first adds an output projection of the concatenated head outputs. It then adds a
position-wise feed-forward map. Scale factors such as 1/√dk are absorbed into Q. The H update
blocks below share all attention and feed-forward parameters; the final readout block is separate.
Token coordinates. Let T = {X, S, D, A} denote observation, summary, decision, and emitted-
action types. Each prompt position has a type one-hot eτ(j) ∈ R4 and turn one-hot eℓ(j) ∈ RH.
Turn tags index decisions: Xt holds the record xt−1 available before decision t, and the observation,
summary, decision, and emitted-action positions for that decision receive tag et. Thus X1 holds
x0. The longest decision prompt contains NH = 4 H − 1 tokens. We reserve the following
disjoint coordinates:
z(0)
j =

1; eτ(j); eℓ(j); cx(j); ca(j); cs(j); rx(j); ra(j); rs(j); λ(j)

. (27)
Here cx = Ex(xt−1) only at Xt, ca = Ea(at) only at At, and all other content coordinates initially
vanish. The augmented state slot is cs = (v, s) ∈ R1+ds, where v is a validity coordinate; its scratch
copy is rs = (rv, rstate). These slots, rx, ra, and the action-logit slot λ ∈ R|A| are initially zero. (27)
requires
1 + 4 +H + 2(dx + da + ds + 1) + |A|
residual coordinates, giving the residual-width bound stated above.
Lemma D.1 (Typed-turn softmax routing). Fix a query position i and suppose its causal prefix
contains a unique position j∗ with target typeτ ∗ and target turnℓ∗. Let the key and query maps satisfy
Kz j = [eτ(j); eℓ(j)], Qz i = C[eτ ∗; eℓ∗].
Then the target score is 2C, every off-target score is at most C, and
1 − αij∗ ≤ (N − 1)e−C. (28)
If ∥V zj∥∞ ≤ B, the head output differs from V zj∗ by at most 2B(N − 1)e−C in ℓ∞.
17

## B-6fe56f88cc2da2

candidate openreview-8OOMlVFxb0 PDF page 12

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
Jiuqi Wang, Ethan Blaser, Hadi Daneshmand, and Shangtong Zhang. Transformers can learn temporal
difference methods for in-context reinforcement learning. In International Conference on Learning
Representations, 2025.
Christopher J. C. H. Watkins and Peter Dayan. Q-learning. Machine Learning, 1992.
Shiguang Wu, Yaqing Wang, and Quanming Yao. Why in-context learning models are good few-shot
learners? In International Conference on Learning Representations, 2025.
Sang Michael Xie, Aditi Raghunathan, Percy Liang, and Tengyu Ma. An explanation of in-context
learning as implicit Bayesian inference. In International Conference on Learning Representations,
2022.
Wanqiao Xu, Allen Nie, Ruijie Zheng, Aditya Modi, Adith Swaminathan, and Ching-An Cheng. For-
malizing learning from language feedback with provable guarantees. In International Conference
on Machine Learning, 2026.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao.
ReAct: Synergizing reasoning and acting in language models. In International Conference on
Learning Representations, 2023.
Chulhee Yun, Srinadh Bhojanapalli, Ankit Singh Rawat, Sashank J. Reddi, and Sanjiv Kumar.
Are transformers universal approximators of sequence-to-sequence functions? In International
Conference on Learning Representations, 2020.
Andrea Zanette and Emma Brunskill. Problem dependent reinforcement learning bounds which can
identify bandit structure in MDPs. In International Conference on Machine Learning, 2018.
Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, and Gao Huang. ExpeL:
LLM agents are experiential learners. In AAAI Conference on Artificial Intelligence, 2024.
12

## B-7d4c006522390b

candidate openreview-8OOMlVFxb0 PDF page 10

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
8 AI U SE STATEMENT
In this work, we used generative AI tools to assist with proof writing and method implementation,
obtain feedback on research methodology and experiments, propose or refine hypotheses, and generate
synthetic datasets. We did not use these tools to develop theoretical models or conceptual frameworks,
formulate mathematical claims, provide critical ingredients for mathematical proofs, translate text,
conduct qualitative or thematic data analysis, or interpret results. Dataset cleaning and reformatting
are not applicable to this work. We reviewed all AI-assisted work. We checked LLM-generated
proofs for errors and tested generated code for correctness. We take responsibility for all final text,
claims, and artifacts, including AI-assisted content.
REFERENCES
Ekin Akyürek, Dale Schuurmans, Jacob Andreas, Tengyu Ma, and Denny Zhou. What learning
algorithm is in-context learning? investigations with linear models. In International Conference
on Learning Representations, 2023.
Peter Auer, Nicolò Cesa-Bianchi, and Paul Fischer. Finite-time analysis of the multiarmed bandit
problem. Machine Learning, 2002a.
Peter Auer, Nicolò Cesa-Bianchi, Yoav Freund, and Robert E. Schapire. The nonstochastic multiarmed
bandit problem. SIAM Journal on Computing, 2002b.
Mohammad Gheshlaghi Azar, Ian Osband, and Rémi Munos. Minimax regret bounds for reinforce-
ment learning. In International Conference on Machine Learning, 2017.
Yu Bai, Fan Chen, Huan Wang, Caiming Xiong, and Song Mei. Transformers as statisticians: Provable
in-context learning with in-context algorithm selection. In Advances in Neural Information
Processing Systems, 2023.
Kathryn Chaloner and Isabella Verdinelli. Bayesian experimental design: A review. Statistical
Science, 1995.
Jie Cheng, Gang Xiong, Ruixi Qiao, Lijun Li, Chao Guo, Junle Wang, Yisheng Lv, and Fei-Yue Wang.
Stop summation: Min-form credit assignment is all process reward model needs for reasoning. In
Advances in Neural Information Processing Systems, 2025.
Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Yuchen Zhang, Jiacheng Chen, Wendi Li,
Bingxiang He, Yuchen Fan, Tianyu Yu, et al. Process reinforcement through implicit rewards.
arXiv preprint arXiv:2502.01456, 2025.
Mostafa Dehghani, Stephan Gouws, Oriol Vinyals, Jakob Uszkoreit, and Lukasz Kaiser. Universal
transformers. In International Conference on Learning Representations, 2019.
Ching Fang and Kanaka Rajan. From memories to maps: Mechanisms of in-context reinforcement
learning in transformers. arXiv preprint arXiv:2506.19686, 2025.
Peter I. Frazier, Warren B. Powell, and Savas Dayanik. A knowledge-gradient policy for sequential
information collection. SIAM Journal on Control and Optimization, 2008.
Shivam Garg, Dimitris Tsipras, Percy Liang, and Gregory Valiant. What can transformers learn
in-context? a case study of simple function classes. In Advances in Neural Information Processing
Systems, 2022.
Neil Houlsby, Ferenc Huszár, Zoubin Ghahramani, and Máté Lengyel. Bayesian active learning for
classification and preference learning. arXiv preprint arXiv:1112.5745, 2011.
Martin Klissarov, Jonathan Cook, Diego Antognini, Hao Sun, Jingling Li, Natasha Jaques, Claudiu
Musat, and Edward Grefenstette. Improving interactive in-context learning from natural language
feedback. arXiv preprint arXiv:2602.16066, 2026.
10

## B-7d679430fa948c

candidate openreview-8OOMlVFxb0 PDF page 16

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
A prior or pseudocount handles unvisited pairs. Planning uses the estimated model:
supp Gt(· | st) ⊆ arg max
a
"
bRt(ot, a) + γ
X
o′
bPt(o′ | ot, a)V
cMt
t+1(o′)
#
. (22)
Simulated transitions are internal computations; only environment observations enter the transcript.
UCBVI-style optimistic model-based RL. For length-L episodic MDPs, UCBVI (Azar et al.,
2017) uses t = (k − 1)L + j to index episode k and stage j in the transcript, with H = KepL for
Kep episodes. Before each episode, compute the empirical model from past transitions and, with
confidence bonus bk,j and V +
k,L+1 = 0, solve
Q+
k,j(o, a) = min
(
L − j + 1,bRk(o, a) +
X
o′
bPk(o′ | o, a)V +
k,j+1(o′) + bk,j(o, a)
)
,
V +
k,j(o) = max
a∈Lj(o)
Q+
k,j(o, a), G k,j = δtieargmaxa∈Lj (ok,j ) Q+
k,j(ok,j ,a).
(23)
The state stores the episode, stage, current observation, empirical statistics, and optimistic value
tables. Each transition updates the statistics; each episode boundary triggers replanning. Reset
records enter the transcript as observations.
B C UMULATIVE -R ETURN ORDERING UNDER PROCESS SUPERVISION
We prove Proposition 5.1, stated in Section 5.1, and give a sufficient condition based on the outcome-
action margin. Throughout, Q∗
out,t and A∗
out,t are the outcome action values and optimal-action sets
defined in that section, and Lt(h) denotes the legal actions at h. Appendix C gives potential-based
shaping as an exact order-preserving construction.
Fix sets Wt of legal histories and suppose every outcome-suboptimal action at these histories has
value at least γW > 0 below the optimal outcome action value. Then
sup
t,h∈Wt,a∈Lt(h)
|Q∗
S,t(h, a) − Q∗
out,t(h, a)| < γ W /2 (24)
is sufficient for the process-greedy decisions to remain terminal-optimal.
Proof. If the inclusion condition in Proposition 5.1 holds, the support of every process-greedy
policy lies in A∗
S,t(h) ⊆ A ∗
out,t(h), so it preserves outcome-optimal decisions at every history of
interest. Conversely, if the inclusion fails, some a− ∈ A ∗
S,t(h) \ A∗
out,t(h) can be selected by a
process-greedy policy at h; hence not every such policy preserves the terminal-optimal decision.
Because the legal action set is finite, this inclusion is equivalent to strict separation between the largest
terminal-optimal and terminal-suboptimal process values. A strict reversal makes every maximizer
terminal-suboptimal, whereas equality includes at least one terminal-suboptimal maximizer.
For the uniform-error sufficient condition, fix h ∈ W t, an outcome-optimal action a+, and a
suboptimal action a−. If the left side of (24) is ζ, then
Q∗
S,t(h, a+) − Q∗
S,t(h, a−) ≥ Q∗
out,t(h, a+) − Q∗
out,t(h, a−) − 2ζ ≥ γW − 2ζ > 0.
Thus no suboptimal action can maximize the cumulative process-return value. Finally, if cumulative
process values are identical at two histories with the same legal action set, their nonempty greedy
action sets are identical. When the two terminal-optimal action sets are disjoint, this common greedy
set cannot be a subset of both, so policy consistency fails for at least one history. □
C P OTENTIAL -BASED PROCESS REWARDS
When outcome rewards are available, potential-based shaping preserves optimal-action sets by adding
differences of bounded history-dependent potentials (Ng et al., 1999). The shaping discount must
match the return discount, and the terminal potential must be zero. For 0 < β ≤ 1, let rR
t = 0 for
16

## B-7d6e0cc68b208f

candidate openreview-8OOMlVFxb0 PDF page 30

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
is the parameter boundary: at gh = 0, a process-optimal tie already permits an outcome-suboptimal
action, and gh < 0 predicts a strict ordering reversal.
Table 18 reports the minimum gap and violation fraction |D|−1P
h∈D 1{gh ≤ 0}, computed from
oracle scores. All twelve tested settings have a negative minimum gap.
Table 18: Immediate-credit verifier-specification audit on the fixed 4,096-history setD. Entries are
deterministic oracle quantities. ⋆ marks the primary setting; □ marks the exact KG specification. Its
violation fraction is 100% on DBK , where Bayes and KG optima differ by construction.
α τ v Violation fraction on D minh∈D gh
.50 .50 52.4% -.124
.50 .75 48.5% -.101
.50 1.00 45.1% -.086
.50 1.25 47.9% -.112
.75 .50 45.7% -.117
.75 .75 ⋆ 41.3% -.096
.75 1.00 38.5% -.081
.75 1.25 40.6% -.107
1.00 .50 44.3% -.113
1.00 .75 40.1% -.092
1.00 1.00 □ 37.6% -.078
1.00 1.25 42.0% -.109
Table 19: Learned policies in the immediate-credit verifier-specification sweep. Candidate TV uses
behavioral references; hard-objective TV uses the uniform kernel on exact verifier optima. Entries
with uncertainty are mean ± SD across five seeds; the primary KG distance is available as a mean
only. †: the displayed distance is to KG, not a distance to a hybrid reference.
(α, τv) Nearest candidate Candidate TV Hard-objective TV Verifier regret Return
(.50,.50) Entropy .091 ± .010 .238± .024 .012± .003 .668± .014
(.50,.75) Entropy .079 ± .009 .211± .021 .009± .002 .687± .012
(.50,1.00) Hybrid † .087± .010 .198± .020 .008± .002 .696± .011
(.50,1.25) Entropy .098 ± .012 .226± .025 .011± .003 .679± .014
(.75,.50) KG .076 ± .009 .219± .022 .010± .002 .696± .013
(.75,.75)⋆ KG .047 .188 ± .019 .007± .002 .710± .009
(.75,1.00) KG .043 ± .006 .174± .018 .006± .001 .714± .009
(.75,1.25) KG .067 ± .008 .202± .023 .009± .002 .701± .012
(1.00,.50) KG .081 ± .010 .206± .023 .009± .002 .701± .012
(1.00,.75) KG .056 ± .007 .178± .020 .006± .002 .709± .010
(1.00,1.00)□ KG .034 ± .005 .158± .017 .004± .001 .712± .008
(1.00,1.25) KG .061 ± .008 .189± .021 .008± .002 .700± .011
At (α, τv) = ( .50, 1.00), KG and entropy have mean distances 0.087 and 0.091, with paired dif-
ference 0.004 ± 0.007; they are nearest in three and two seeds, respectively. This cell is therefore
hybrid/unidentified. Other labels in Table 19 indicate the reported nearest candidates; the summary
results do not establish their seedwise stability. For a unique objective optimum, hard-objective TV
equals 1 − OptMass. With ties, TV to the specified uniform-on-optima kernel must be evaluated
directly. The primary hard-objective TV of 0.188 and KG-score TV of 0.047 accordingly measure
different comparisons.
The twelve cells isolate local-score specification from credit assignment. All twelve tested immediate-
credit settings have outcome-ordering violations, so none preserves outcome-optimal behavior across
D. Settings with lower confidence weight are entropy-like, whereas the primary setting and its
neighboring α ≥ .75 cells are KG-like; low verifier regret links these behavioral changes to the
objectives being optimized. The next experiment varies the credit discount and tests when process-
optimal actions become outcome-optimal on the diagnostic sets.
G.7 O UTCOME -PRESERVING PROCESS REWARD
The outcome-preserving control follows Appendix G.5, with the same initial weights and task
distribution as outcome training and no warm start. Let qh and ℓh be the remaining budget and query
30

## B-7e23a6c41f7e23

candidate openreview-8OOMlVFxb0 PDF page 28

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
Horizon and prefix-depth decomposition. Table 15 separates the Bayes-distilled model’s initial
horizon H0 from completed-call depth k. Equal weighting of depths within each horizon gives the last
column; equal weighting of its four means gives (0.024 + 0.028 + 0.033 + 0.039)/4 = 0.031. Deep
prefixes are legal continuations generated independently of the evaluated model; these execution
diagnostics need not be visited by its autonomous policy. At k = H0, only terminal answers
remain legal.
Table 15: Bayes distillation: action TV to the score teacher by initial horizon and prefix depth.
Individual depth entries are means; SDs are available for the horizon-level aggregates. Prefixes with
only one query remaining test execution rather than Bayes/KG planning separation.
H0 k = 0 1 2 3 4 5 6 7 8 Depth mean
5 .019 .020 .021 .024 .028 .032 — — — .024 ± .003
6 .020 .021 .024 .027 .032 .035 .037 — — .028 ± .004
7 .021 .024 .027 .029 .035 .039 .043 .046 — .033 ± .005
8 .024 .026 .030 .034 .038 .042 .047 .052 .058 .039 ± .006
For the nominal-horizon control, we pair the same task and evidence at q ≤ 4, changing only an
inactive horizon field from H0 = 4 to the indicated value. The exact Bayes reference is unchanged.
Table 16 shows much smaller model changes than the deepest-prefix errors; transcript depth and an
inactive horizon field therefore have distinct effects.
Table 16: Changes in the Bayes-distilled model when only the inactive horizon field is increased,
mean ± SD across five seeds.
Paired with H0 = 4 5 6 7 8
Model action TV .010 ± .002 .011± .002 .013± .003 .014± .003
G.5 S HARED ARCHITECTURE AND OPTIMIZATION
The primary symbolic conditions in Table 12 and Figure 3, including the outcome-preserving
process-reward control, use a pre-layer-normalized causal Transformer with six layers, residual
width 256, eight attention heads, feed-forward width 1,024, GELU activations, and zero dropout.
Field, token-type, turn, and action embeddings are learned; scalar probabilities and costs use a
fixed Fourier-feature map followed by a learned projection. A linear policy head at each ACT token
produces global-vocabulary logits, and a public-history mask removes illegal actions. A separate
value head is present only during policy optimization and is discarded for every behavioral evaluation.
Table 17: Alignment between the primary experimental objectives and policy references. The three
reward conditions are optimized with PPO, have an entropy-free final phase, and are evaluated against
hard unregularized references. The credit-assignment sweep is specified separately below.
Condition Trainer objective Entropy protocol Aligned reference
Outcome reward terminal BTS return 0.01 → 0 in first 30%;
then 0
hard Bayes DP
Outcome-preserving
process reward
outcome plus perturbed
telescoping potential
same hard Bayes DP
Primary one-step
process reward
er1V
t , β = 0 0 .01 → 0 in first 30%;
then 0
exact one-step process
reward optimum
Bayes DP-score
distillation cross-entropy to score
teacher
none πscore
B,0.02
Distillation uses AdamW with learning rate3 ×10−4, zero weight decay, batch size 256, and gradient-
norm clipping at 1. The reward conditions share the same initialization distribution and clipped PPO
implementation. Each of 100,000 updates collects multiple fresh on-policy episodes and performs
four full-batch PPO epochs using learning rate 3 × 10−4, clip ratio 0.2, value-loss coefficient 0.5, and
gradient-norm clipping at 1. The entropy coefficient decreases linearly from 0.01 to zero during the
first 30% of updates and remains zero for the final70%. Outcome reward and the outcome-preserving
control use GAE with γPPO = 1 and λ = 1. On complete finite-horizon episodes, this reduces to the
Monte Carlo advantage bAt = Gt − Vϕ(ht−1), where Gt =PT
u=t ru. The primary one-step process
28

## B-8359258c385f8a

candidate openreview-8OOMlVFxb0 PDF page 18

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
Proof. The one-hot inner product gives score2C exactly when both tags match. Uniqueness implies
that any other token matches at most one tag and has score at most C. Dividing the total off-target
exponential mass by the target mass gives (28). The value error is at most (1 − αij∗)∥V zj∗ ∥∞ +P
j̸=j∗ αij∥V zj∥∞, which proves the second claim. □
Explicit query, key, and value maps. Let R− :=PH
u=2 eu−1e⊤
u be the backward turn-shift. Every
state-update block uses three heads with the common key map in Lemma D.1. On a summary query
Su, their query maps are
Qx[eS; eu] = C[eX; eu], Q x = C diag(eXe⊤
S , IH), (29)
Qa[eS; eu] = C[eA; eu−1], Q a = C diag(eAe⊤
S , R−), (30)
Qs[eS; eu] = C[eS; eu−1], Q s = C diag(eSe⊤
S , R−), (31)
where only the displayed type/turn blocks are nonzero. The displayed action and state query identities
apply for u ≥ 2; at u = 1, R−e1 = 0 and their outputs are ignored. The corresponding value/output
maps are coordinate projections
cx(Xu) 7→ rx(Su), c a(Au−1) 7→ ra(Su), c s(Su−1) 7→ rs(Su).
Thus, at St, the heads retrieve Ex(xt−1), Ea(at−1), and the previously constructed state. For t = 1,
only the initial-record output is used; the action and state outputs are ignored by the first-turn gate
below. Every required source position precedes St, so the causal mask preserves the construction.
The initial-record token already supplies a nonempty causal prefix, and no BOS token is needed.
Validity gating and the tied update block. The exact summary and first-turn gates are
qS(z) = ⟨eS, eτ(z)⟩, q 1(z) = ReLU

qS(z) + ⟨e1, eℓ(z)⟩ − 1

. (32)
For a routed validity coordinate, use the saturating ReLU gate
χ(v) = 3 ReLU(v − 1
3) − 3 ReLU(v − 2
3).
It is zero for v ≤ 1/3 and one for v ≥ 2/3. Choose the routing accuracy in Lemma D.1 so a copied
zero or one falls in the corresponding interval. Then
qlater(z) = ReLU(qS(z) − q1(z) + χ(rv) − 1) , q ready = q1 + qlater
are binary: the first summary is always ready, and a later summary is ready exactly when its
predecessor was valid at the input to the current layer.
For any binary q and bounded scalar |y| ≤ Bf , the ReLU circuit
Gateq(y) = ReLU(y − Bf(1 − q)) − ReLU(−y − Bf(1 − q)) (33)
equals y for q = 1 and zero for q = 0; below it is applied coordinatewise. Choose shared feed-forward
approximatorsbU0,bU with uniform error at most δU . After the shared routing heads fill the scratch
slots, every copy of the update block uses
(∆rx, ∆ra, ∆rs) = −(rx, ra, rs),
¯starget = Gateq1([1;bU0(rx)]) + Gateqlater([1;bU(rstate, ra, rx)]),
∆cs = Gateqready(¯starget − cs),
(34)
and leaves all other content coordinates unchanged. The turn counter is part of the learner state, so
onebU covers scheduled updates. At the first tied layer onlyS1 becomes valid. If the first r summaries
are valid before a layer, simultaneous attention reads those old values, so the next layer makes Sr+1
valid while recomputing the earlier states. Induction shows that after H copies every summary in any
length-H prefix contains the desired recursive state. No layer has turn-specific trainable parameters.
Action readout. A final head uses
Qout[eD; eu] = C[eS; eu], Q out = C diag(eSe⊤
D , IH), (35)
and the same key map as before. At decision position Du, the head uniquely selects Su and copies
cs(Su) = ( vu, su) to rs(Du). After the H tied update blocks, vu = 1 at every available decision.
One shared position-wise approximatorbℓ, gated only by the decision-token type, writesbℓ(rstate) into
λ(Du) and clears rs. Because the turn counter is part of su, no turn-specific readout is needed. The
external masked softmax over Lu(hu−1) produces the approximating action distribution. Since Su
precedes Du, this readout is causal.
18

## B-897d11b80e4ef3

candidate openreview-8OOMlVFxb0 PDF page 26

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
Table 10: Action TV between paired resource prompts, with current legal actions unchanged.
Reference entries are deterministic; model entries are mean ± SD across five seeds. The outcome
model responds to continuation opportunities, whereas the model trained with one-step process
reward responds much less.
Paired intervention Bayes ref. Exact verifier Outcome model
One-step process
reward model
Remaining horizon 2 → 4 .204 0 .187 ± .020 .021± .005
Remaining budget 2 → 4 .173 0 .161 ± .018 .018± .004
Table 11: State, update, and generalization diagnostics. Values are mean ± standard deviation across
five seeds; hard Bayes/KG agreement is reported in Table 6.
Diagnostic Outcome reward
One-step
process reward
posterior log-odds NRMSE ↓ 0.021± 0.003 0.024± 0.004
Bayes-update identity NRMSE ↓ 0.028± 0.004 0.031± 0.004
action TV on state-equivalent order swaps ↓ 0.014± 0.002 0.016± 0.003
unseen H = 6 value gap ↓ 0.019± 0.004 0.052± 0.007
likelihood-intervention TV to score reference ↓ 0.058± 0.006 0.073± 0.009
Outcome and verifier policies have similar posterior and update errors but opposite Bayes/KG
decisions. The resource interventions show greater continuation sensitivity in the outcome model,
supporting a difference in how similarly available evidence is used for decisions.
G.4 C OMPILATION TASKS
Bayes DP is distilled using horizons one through four for training and horizons five through eight
only for longer-horizon evaluation. The initial budget is sampled independently from {2, . . . ,8}, and
the budget values and cost distribution are identical at train and test. Its targets are the score-softened
kernels πscore
B,0.02 derived from exact unregularized DP action values, following Appendix G.2. The
aggregate long-horizon TV uses depth-balanced prefixes from feasible-long, horizon-active tasks; the
nominal-horizon control and per-prefix-depth TVs are reported separately. The UCB condition uses
four Bernoulli arms, positive pseudocounts, and indexbµi + 1.5
p
log(t + 1)/Ni; training transcripts
contain at most 16 pulls, compared with 32 at length evaluation. The tabular Q-learning condition
uses five states, three actions,α = 0.2, γ = 0.9, and an ϵ = 0.1-greedy behavior kernel; random finite
MDPs generate at most 16 training transitions and 32 length-test transitions. In all three conditions,
the transcript exposes only the inputs available to the corresponding recursion. Oracle posterior,
count-sum, and Q-table states remain trainer-side and are used only as probe targets.
Distillation minimizes action cross-entropy on freshly generated transcripts. After freezing all
Transformer parameters, we fit a linear decoder fdec from the summary representation z(h) to the
corresponding oracle state. Its normalized held-out reconstruction error is the state NRMSE. With the
decoder frozen, we test the one-step identity
fdec(z(h, a, x)) ≈ U(fdec(z(h)), a, x).
The normalized residual on held-out transitions is the update NRMSE. Both metrics normalize each
state coordinate by its held-out standard deviation. Action TV compares the complete legal action
distributions and is averaged over evaluation histories; long-horizon TV uses the same metric on
the extrapolation sets specified above. Value gaps compare autonomous execution of the model and
reference policies in fresh environments.
Table 13 gives the per-task random baselines underlying the null ranges in Table 12, which reports
the distilled models.
26

## B-8faefcdc734203

candidate openreview-8OOMlVFxb0 PDF page 27

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
Table 12: Algorithm-compilation tests. Task rows report distilled models. Null ranges are the
minimum and maximum task means for untrained Transformers.
Reference action TV ↓ state / update NRMSE ↓ long-horizon TV ↓ value gap ↓
Bayes DP 0.018± 0.002 0.013± 0.002 / 0.019± 0.003 0.031± 0.004 0.006± 0.001
UCB bandit 0.009± 0.001 0.006± 0.001 / 0.008± 0.001 0.019± 0.003 0.004± 0.001
Q-learning 0.016± 0.003 0.011± 0.002 / 0.017± 0.002 0.067± 0.007 0.008± 0.002
Null range 0.408-0.760 0.895-1.000 / 0.216-0.691 0.481-0.732 0.031-0.533
Table 13: Random Transformer baselines for Table 12. Values are mean± standard deviation; lower
is better for every metric. Long-horizon evaluation uses Bayes DP horizons five through eight and
doubles transcript length for UCB and Q-learning, as specified above.
Oracle
action TV
↓
state / update NRMSE
↓
long-horizon TV
↓
value gap
↓
Bayes DP 0.760± 0.001 1.000± 0.001 / 0.691± 0.002 0.732± 0.002 0.533± 0.002
UCB bandit 0.490± 0.001 1.000± 0.001 / 0.308± 0.001 0.481± 0.003 0.031± 0.002
Q-learning 0.408± 0.002 0.895± 0.001 / 0.216± 0.002 0.490± 0.004 0.035± 0.001
Two additional probe controls are fixed in advance: shuffling feedback across histories tests whether
decoded-state and update accuracy depends on the correct transcript, whereas independently permut-
ing trainer-side state targets tests for decoder leakage without changing the already-trained policy.
Table 14 reports both controls alongside the unmodified probe results. The target-permutation values
range from 0.989 to 1.010, characterizing a unit-NRMSE null for state correspondence in the probe.
These controls retain the trained Transformer weights.
Table 14: Negative controls for the post hoc probes. Metrics are NRMSE. The feedback shuffle
breaks the correspondence between a history and its returned records; the target permutation breaks
the correspondence between frozen representations and trainer-side states. Target permutation leaves
the trained policy unchanged.
Probe evaluation Metric Bayes DP UCB Q-learning
unmodified state 0.013 ± 0.002 0.006± 0.001 0.011± 0.002
update 0.019 ± 0.003 0.008± 0.001 0.017± 0.002
feedback shuffled state 1.153 ± 0.061 0.741± 0.048 1.062± 0.057
update 1.089 ± 0.055 0.697± 0.043 0.986± 0.051
targets permuted state 1.003 ± 0.024 0.994± 0.021 1.005± 0.026
update 0.989 ± 0.022 1.010± 0.025 0.997± 0.023
Both controls sharply increase state and update NRMSE from below 0.02 to 0.697-1.153. Target
permutation drives every error to the unit-NRMSE null scale, arguing against decoder leakage;
feedback shuffling similarly destroys probe accuracy, with the smaller UCB increase expected
because arm counts remain recoverable from the unshuffled action sequence.
For longer-horizon extrapolation, let din
A and dlong
A denote action TV on the training-horizon and
specified longer-horizon evaluations, and define∆len
A = dlong
A − din
A. We double transcript length for
UCB and Q-learning. For BTS, we report results by initial horizonH0 = 5, 6, 7, 8 and completed-call
depth, together with the nominal-horizon control. Motivated by Proposition E.1, we test whether
∆len
Q-learning > max{∆len
BTS, ∆len
UCB}. (42)
If either contrast does not have the same sign in all five seeds, we report a null result; the proposition
is an existence construction and does not guarantee that distillation finds its parallel implementation.
The observed increases are ∆len
BTS = 0.013, ∆len
UCB = 0.010, and ∆len
Q-learning = 0.051. The paired
contrasts ∆len
Q − ∆len
BTS and ∆len
Q − ∆len
UCB are respectively 0.038 ± 0.007 and 0.041 ± 0.006, with
positive signs in all five seeds for both. These results satisfy the stated sign criterion and support
greater length degradation for Q-learning in these tasks, without identifying the implementation
learned by the Transformer.
27

## B-94555e6fa71333

candidate openreview-8OOMlVFxb0 PDF page 13

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
A I NSTANCES OF THE AGENTIC ICL R ECURSION
The examples below instantiate (2) for sequential information acquisition, bandits, and online RL.
Sequential information acquisition includes active learning and Bayesian experimental design, where
queries may return measurements used for a terminal decision (Chaloner & Verdinelli, 1995). Table 2
summarizes the interfaces; the equations below specify their updates and decision rules.
Let δa denote a point mass, B(b; a, x) the action-conditioned Bayes update, andSoftArgMaxβ{q(a)}
the distribution proportional toexp(βq(a)) over legal actions. All argmax rules use a fixed measurable
tie convention.
Regularity qualifications for Table 1. The listed instances inherit the sufficient conditions of The-
orem 4.1: a fixed finite horizon, compact fixed-width encodings, a finite global action vocabulary, and
a public-history legal-action mask. Decision kernels must have continuous finite logits; deterministic
argmax rules are therefore softened, or the approximation is restricted to positive-margin subdomains.
Bayesian likelihoods are bounded below by pmin > 0, and empirical quotients use positive pseudo-
counts so their updates remain regular; empirical-model states are pre-normalized. These conditions
are sufficient for the compiler, not necessary conditions for Transformer implementation.
Time-varying spaces can be embedded by padding into fixed ambient spaces.
Table 2: Observations, actions, environment kernels, and learner states for each algorithm, grouped
by interaction setting. Nt, St are bandit statistics; Nt, Ct, Zt in the model-based rows are transition
counts, reward sums, and visit counts. Terminal flags dt make bootstrapping conventions explicit.
Algorithmic
instance
Returned record
xt ∈ X t
Action
at ∈ A t
Environment kernel KM Information state st ∈ S t
Setting: sequential information acquisition
Pool-based
active learning
(BALD)
(zt, yt) ∈ Z × Y query(zt),
zt ∈ P t
pM (yt | zt), with the
queried zt copied into the
record
(Dt, Pt, bt): labeled set,
unlabeled pool, posterior
Bayesian
sequential
design
(VOI/KG)
xt ∈ X t(at) query or
experiment
KM (x | ht−1, at) ( ht−1, bt), bt(m) =
P(M = m | ht−1)
Setting: bandits
Thompson
sampling
reward rt ∈ [0, 1] arm it ∈ [K] rt ∼ PM,it posterior bt(M ) over
arm-reward models
UCB reward rt ∈ [0, 1] arm it ∈ [K] rt ∼ PM,it (t, Nt, St), with counts
and reward sums in RK
Linear
contextual
bandit
(rt, ct+1) arm it ∈ [K]
after seeing ct
rt = ϕ(ct, it)⊤θ∗ + εt,
then ct+1 ∼ ν
(ct, Vt, qt), ridge matrix
and response vector
EXP3 selected-arm reward
rt(it) ∈ [0, 1]
arm it ∈ [K] arbitrary reward vector
rM,t(ht−1), with only
coordinate it revealed
(t, wt), positive arm
weights in RK
Setting: online reinforcement learning
Q-learning (rt, ot+1, dt) off-policy
control at
controlled
transition/reward law
(Qt, ot)
SARSA (rt, ot+1, dt) on-policy
control at
controlled
transition/reward law
(Qt, ot, pt), pt a pending
transition or ⊥
Actor-critic (rt, ot+1, dt) at ∼ πθt (· |
ot)
controlled
transition/reward law
(θt, wt, ot): actor, critic,
current observation
Learned-model
planning
(rt, ot+1, dt) control action unknown controlled
model (PM , RM )
(ot, Nt, Ct, Zt, bPt, bRt)
UCBVI (rk,j , ok,j+1, dk,j ) episodic
control ak,j
unknown length-L
episodic MDP
(k, j, ok,j ); empirical
model statistics;
optimistic Q+
k , V +
k
13

## B-aa5f77f9070559

candidate openreview-8OOMlVFxb0 PDF page 14

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
Pool-based active learning. For a label model pm(y | z), initialize b1 by conditioning the prior on
the seed labels D1. Querying zt ∈ P t returns yt and gives
bt+1(m) ∝ bt(m)pm(yt | zt), U t(st, at, xt) = (Dt ∪ {(zt, yt)}, Pt \ {zt}, bt+1). (8)
BALD (Houlsby et al., 2011) selects queries using Gt = SoftArgMaxβt {αt(z)}z∈Pt, where
αt(z) = H
 X
m
bt(m)pm(· | z)
!
−
X
m
bt(m)H(pm(· | z)) . (9)
A terminal prediction can be included as an answer action.
Bayesian sequential experimental design and value of information. At the pre-action history
h = ht−1, let bt(m) = P(M = m | h). For a finite task family, the update and decision rule are
bt+1(m) = Km(xt | h, at)bt(m)P
m′ Km′(xt | h, at)bt(m′) , (10)
supp Gt(· | h, bt) ⊆ arg max
a
Em∼bt

rm(h, a) + Ex′∼Km(·|h,a)Vt+1(B(bt; a, x′), (h, a, x′))

,
(11)
where B is the update in (10); for pure acquisition, rm may be zero and utility may be terminal.
This is a Bayesian sequential experimental-design instance: at is a query or experiment and xt is its
outcome. Sequential active learning is the label-query specialization given above. The continuation
term captures the feedback loop: an experiment is valuable partly because it changes the posterior
used to select later experiments or make a terminal decision.
A concrete one-step value-of-information rule is the knowledge gradient (Frazier et al., 2008). Let D
be a terminal decision set, u(d, m) its utility under task m, and
W (b) := max
d∈D
Em∼bu(d, m).
For the posterior-predictive law K b(x | h, a) =P
m b(m)Km(x | h, a), define
νKG
t (a | h, b) = Ex∼Kb(·|h,a)[W (B(b; a, x)) − W (b)] ,
Gt(a | h, b) = exp{βt[νKG
t (a | h, b) − ct(a)]}P
a′∈Lt(h) exp{βt[νKG
t (a′ | h, b) − ct(a′)]} , a ∈ L t(h),
(12)
where ct(a) is an optional experiment cost. The finite-horizon rule in (11) values all adaptive
continuations, whereas (12) values the expected one-step improvement in terminal utility. Both use
the same posterior state and Bayes update.
Thompson sampling. Initialize b1 from x0 and update by (10) using the selected arm’s reward
law Pm,it(rt). With µi(m) = EPm,i r, Thompson sampling (Russo et al., 2018) drawsfMt ∼ bt and
selects tieargmaxi µi(fMt). For Theorem 4.1, the full-support relaxation (1 − η)Gt + η Unif([K]),
η > 0, has finite logits given by its log probabilities.
UCB bandit. For a stochastic K-armed bandit with revealed reward rt, let st = (t, Nt, St), where
Nt(i) and St(i) are the pre-decision pull count and reward sum, initialized to zero. The UCB
recursion (Auer et al., 2002a) is, for every arm i,
Nt+1(i) = Nt(i) + 1{i = it},
St+1(i) = St(i) + rt1{i = it},
bµt+1(i) = St+1(i)/Nt+1(i),
i∗
t+1 = tieargmaxi∈[K]
"
bµt+1(i) + βt+1
s
log(t + 1)
Nt+1(i)
#
, G t+1 = δi∗
t+1 .
(13)
Set the index of an unpulled arm to +∞; use the quotient above only after the arm’s first pull. A
softened UCB kernel replaces the final point mass by softmax over the displayed indices.
14

## B-bf12c3eb03742e

candidate openreview-8OOMlVFxb0 PDF page 7

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
Action
TV
State
NRMSE
Update
NRMSE
Long-hor.
TV
Value
gap
10−3
10−2
10−1
100
Error (log scale; lower is better)
(a) Bayes DP
0.018 0.013 0.019
0.031
0.006
0.760 1.000 0.691 0.732 0.533
Action
TV
State
NRMSE
Update
NRMSE
Long-hor.
TV
Value
gap
(b) UCB bandit
0.009 0.006 0.008
0.019
0.004
0.490
1.000
0.308
0.481
0.031
Action
TV
State
NRMSE
Update
NRMSE
Long-hor.
TV
Value
gap
(c) Q-learning
0.016 0.011 0.017
0.067
0.008
0.408
0.895
0.216
0.490
0.035
Distilled Null baseline
Figure 2: Learned execution from supervised distillation. Each panel compares a distilled model with
its corresponding random Transformer (null baseline). x−ticks are different metrics. Full values are
provided in Appendix Tables 12 and 13.
at longer horizons; lower is better. Appendix G.4 gives full baselines, training details, and metric
definitions.
Figure 2 shows that the distilled models closely match all three supplied recursions. Distillation
substantially reduces every metric relative to the corresponding random Transformer baseline. Thus
optimization can reach qualitatively different realizations permitted by Theorem 4.1. Bayes DP and
UCB degrade less than Q-learning on their respective longer-horizon evaluations, consistent with the
additive-state distinction in Appendix E, while the length extrapolation remains empirical.
6.3 T RAINING OBJECTIVES CHANGE WHICH CANDIDATE BEST MATCHES THE MODEL
Distillation demonstrates learned execution when the target policy is supplied. We next remove oracle
action and state targets and train only from rewards, as in RL post-training of language model agents.
The central question is how training objectives shape candidate-relative decisions. In particular, we
test whether learned behavior tracks changes in the training objective under controlled interventions.
We consider four supervision conditions. Outcome reward targets terminal BTS return, for which
Bayes DP is optimal; one-step process reward scores immediate local progress; outcome-preserving
process reward adds a potential-based shaping term with a fixed bounded perturbation; and Bayes
DP-score distillation provides a supervised reference using a softmax over unregularized Bayes DP
action values.
A verifier scores immediate information gain or apparent progress without computing globally optimal
continuation values. Its three parameters (α, τv, γ) control the local score and credit assignment. A
call is rewarded when its realized gain in answerability and distributional certainty offsets its cost.
The confidence weight α trades top-answer probability against normalized certainty, τv controls how
strongly each observation updates the verifier belief, and the credit discountγ controls how much later
verifier progress is assigned to the current action. The primary setting uses (α, τv, γ) = (.75, .75, 0),
and we refer to its γ = 0 objective as the one-step process reward. Following Proposition 5.1, the
outcome-preserving process reward uses a perturbed potential-shaped dense signal while preserving
the outcome-optimal policy set.
To describe the learned policy with (7), here we consider four candidates sharing the Bayesian
update but using different decision rules: Bayes DP, one-step knowledge gradient (KG), one-step
entropy reduction, and an open-loop oracle. These candidates distinguish outcome-optimal planning,
one-step value of information, a surrogate information objective, and feedback-insensitive acquisition.
Appendix G gives the formal definitions of the rewards and candidate policies, the diagnostic histories,
and the complete training protocol.
Figure 3 shows that outcome reward training produces behavior closest to Bayes DP, whereas one-step
process reward training produces behavior closest to KG. The latter is consistent with the one-step
objective violating the ordering condition in Proposition 5.1. The outcome-preserving process reward
instead remains Bayes DP-like. The bounded perturbation changes individual step rewards, but
telescoping leaves the ordering of cumulative action values unchanged. This provides an empirical
test of the proposition’s ordering criterion without requiring the process and outcome rewards to be
numerically equal. Appendix Table 8 reports the full candidate comparison. We also perform a 12-cell
7

## B-c28dffc10abeca

candidate openreview-8OOMlVFxb0 PDF page 24

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
candidate pair, (ii) stopping versus acquisition decisions, and (iii) horizon and budget. The expanded
evaluation adds the two-step candidate on D.
The selection threshold targets the largest pairwise disagreement at each history. It does not certify
Proposition 5.2, whose condition depends on ∆D = minj̸=k dD(πj, πk) after grouping coincident
candidates. We report nearest-candidate distances and runner-up gaps without a separation guarantee.
From the same proposal pool, we also select histories where Bayes DP and KG choose
different actions:
DBK = {h : a∗
B(h) ̸= a∗
KG(h), m B(h) ≥ 0.02, m KG(h) ≥ 0.02},
where mB and mKG are the best-minus-second-best legal action-value gaps under the respective
unregularized reference scores. Both maximizing actions must be unique. A deterministic saved
rule selects 1,024 histories from distinct tasks, balanced across stop/query disagreement types. We
evaluate the same model top action on every selected history and report agreement with Bayes,
agreement with KG, and agreement with neither; the three categories sum to 100% within each seed.
For longer-horizon diagnostics, let H0 be the initial query horizon, k the number of completed calls,
and ℓ = H0 − k the remaining horizon. Horizon activity is evaluated at the task’s initial history by
comparing the Bayes score kernels under H0 and min(H0, 4), holding the public task and budget
fixed and requiring TV at least 0.10. Once a task qualifies, its legal prefixes are retained for length
evaluation without reapplying that root-level condition at every prefix. Planner comparisons use
early histories on which the relevant candidates differ; long-prefix execution is evaluated separately,
including histories on which candidates coincide. At H0 = 6, k = 5, only one query remains, so full
Bayes and one-step KG have identical action values. We report such prefixes as transcript-length
tests, not nonmyopic-planning witnesses.
Table 6: Agreement with Bayes DP and KG on the shared diagnostic set. Every entry usesDBK , with
unique, different Bayes and KG maximizing actions and a margin of at least0.02 under both reference
score functions. The set contains one history from each of 1,024 qualifying tasks. Values are mean ±
standard deviation across five seeds, and the three columns sum to 100% within each seed.
Training condition Bayes agreement ↑ KG agreement ↑ Neither
Outcome reward 88.7% ± 1.9% 8.1%± 1.4% 3.2%± 0.7%
One-step
process reward 11.4% ± 2.2% 86.5%± 2.0% 2.1%± 0.9%
Outcome-preserving 87.9% ± 2.0% 8.8%± 1.5% 3.3%± 0.8%
Bayes DP-score
distillation 93.4% ± 1.1% 4.3%± 0.8% 2.3%± 0.5%
Table 7: Objective alignment and candidate separation on frozen diagnostic set D. Optimal-action
mass and regret use unregularized maximizing sets and action values; candidate distances use the
specified behavioral kernels and include receding two-query lookahead. Differences between nearest
and runner-up distances are computed within seed before summarization. Distillation is audited
against outcome optimality but was trained against a score-softened teacher.
Condition Objective audited Opt. mass ↑ Regret ↓ Nearest / runner-up Gap ↑
Outcome reward outcome reward 0.803 ± 0.018 0.010± 0.002 Bayes / two-step 0.038 ± 0.008
One-step
process reward
one-step
verifier score 0.812 ± 0.019 0.007± 0.002 KG / entropy 0.091 ± 0.010
Bayes DP-score
distillation outcome, audit only 0.771 ± 0.014 0.013± 0.002 Bayes / two-step 0.057 ± 0.007
The outcome-preserving condition has outcome OptMass 0.797 ± 0.020 and regret 0.011 ± 0.002.
Its agreement with Bayes DP and KG on DBK appears in Table 6.
24

## B-c311dec7ab892c

candidate openreview-8OOMlVFxb0 PDF page 25

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
Table 8: Mean distances to the expanded candidate family on D, using the reference policies defined
in Appendix G.2. †: means obtained by adding the paired Bayes/two-step gap in Table 7 to the Bayes
distance, with the same histories and weights; no SD is inferred from this addition. The verifier’s
two-step distance is 0.174 ± 0.013; the preserving condition’s is0.084 ± 0.010.
Condition Bayes Two-step KG Entropy Open-loop
Outcome reward .043 .081 † .182 .249 .286
One-step
process reward .219 .174 .047 .138 .275
Outcome-preserving .046 .084 .184 .254 .289
Bayes DP-score
distillation .018 .075 † .214 .267 .301
Adding two-step leaves the nearest candidates unchanged, while narrowing the runner-up gaps for
outcome training and distillation.
Agreement after excluding near-ties. For each audited objective, we retain histories with a unique
optimum and a best-minus-second-best action-value margin of at least 0.02, selecting only with
oracle values. Outcome, outcome-preserving, and distillation audits share the outcome-defined
subset; the primary verifier uses its own objective-defined subset. Table 9 reports alignment on these
objective-specific subsets; common Bayes/KG decisions use DBK .
Table 9: Objective alignment after excluding near-ties, using objective-specific margin ≥ 0.02.
Values are mean ± SD across five seeds. Distillation has the highest top-action agreement but lower
optimal-action mass, consistent with learning a soft teacher.
Condition / audit Top-action agreement ↑ OptMass ↑ Regret ↓
Outcome / outcome 96.9% ± 1.0% .923± .014 .006± .001
One-step process reward /
immediate score 95.7% ± 1.4% .916± .017 .005± .001
Distillation / outcome 98.1% ± 0.8% .891± .012 .008± .001
Preserving / outcome 96.6% ± 1.2% .918± .015 .006± .001
State and decision diagnostics. To assess whether the decision shifts reflect differences in evidence
estimates, we test posterior decoding and the Bayes-update identity, permute evidence order at fixed
posterior, intervene on remaining resources at fixed evidence, and alter likelihood rows.
Posterior probes use the final SUM residual stream. We fit a ridge-regularized linear map fdec on
20,000 histories and evaluate it on histories from 20,000 disjoint tasks; the target is the centered
log posterior odds relative to hypothesis K. Regularization is selected entirely within the training
split. For a fresh legal extension (e, y), the update residual compares fdec(z(h, e, y)) with the exact
Bayes update applied to fdec(z(h)), after mapping the decoded log odds back to the simplex. Neither
quantity is used to train the Transformer.
We construct state-equivalent pairs by permuting evidence records while preserving the exact posterior,
remaining budget, horizon, and public task. Likelihood interventions change one public likelihood
row and recompute both the posterior and oracle target. Bayes-KG decisions use the common set
DBK (Table 6). Probe results are supporting diagnostics; state-equivalent behavior and candidate
policies are invariant to hidden-state reparameterization.
Resource interventions change a public budget or horizon field while fixing the prior, likelihoods,
costs, discount, evidence records, transcript length, and current legal-action mask (Table 10). We
select histories where future resource opportunities change Bayes continuation values; current action
availability alone therefore cannot explain the response. The exact immediate verifier optimum is
unchanged because neither its evidence aggregate nor its legal action scores change.
25

## B-d440a79ab26fc8

candidate openreview-8OOMlVFxb0 PDF page 34

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
Learned policies remain imperfectly aligned with their cumulative objectives at every discount. At
γ = .95, Bayes is already the nearest candidate, althoughD still contains ordering violations. Average
candidate proximity and preservation at every audited history therefore yield different transition
points; γ controls credit discounting rather than an exact lookahead depth.
G.9 N ATURAL -LANGUAGE EXPERIMENTS WITH A PRETRAINED LLM
Text interface. We render the same BTS task distribution as a chat transcript for Qwen2.5-1.5B-
Instruct, including the independently sampled training-time horizons and budgets in Table 3. The
initial user message states the four candidate targets and their prior probabilities, the six tool cards
and their conditional outcome probabilities, tool costs, the cost discount, and the initial budget and
call horizon. Subsequent user messages append the selected tool, its returned outcome, and the
mechanically updated resources. Every probability used by the simulator and the exact oracles is
the value printed in the prompt; the sampled target, posterior belief, oracle values, correctness, and
trainer reward are never shown. Target, tool, and outcome names are random nonce words, and their
order is independently permuted across tasks. We use four training-template families and reserve
eight disjoint paraphrase families for evaluation; a family jointly specifies the wording of the task,
tool cards, resource records, and returned observations.
The model emits no rationale. Ten tokenizer-verified single-token action identifiers represent the
four terminal answers and six tool calls, and their assignment is randomly permuted and stated in
each initial prompt. At the first assistant-token position we restrict the softmax to the legal identifiers,
sample one action during autonomous rollouts, and append the sampled identifier to the transcript.
Thus the complete legal-policy is obtained directly from the corresponding next-token logits, without
parsing free-form generations. An abbreviated example of the initial user message follows; every
actual prompt enumerates all ten action-ID assignments and all six complete tool cards.
Identify one hidden target. Output exactly one legal action ID.
Prior: norvik 0.28; pelnor 0.24; saiven 0.26; tudor 0.22.
Score: 0.98^(total tool cost) if the final answer is correct; otherwise 0.
Budget: 3. Remaining calls: 3.
Action B: answer norvik. Action G: answer pelnor. ...
Action E: call tool mira, cost 1.
If norvik: amber .80, blue .15, gray .05.
If pelnor: amber .69, blue .21, gray .10. ...
Legal actions: A B C D E F G H I J.
After a call, the environment appends, for example, “Tool mira returned amber. Remaining budget: 2.
Remaining calls: 2,” followed by the current legal-action list.
Training conditions. All three conditions start from the same pretrained checkpoint and use full-
parameter fine-tuning: all Transformer blocks, token embeddings, and the language-model head are
updated, with neither adapters nor a frozen backbone. The two policy-optimization conditions attach
a scalar value head at assistant decision positions; this head is removed for behavioral evaluation.
The outcome-reward condition receives zero reward after a tool call and the single terminal reward
rH = δ
P
e cene 1{g = Z}. The one-step process reward condition instead receives the realized
local-progress score in (45) at the primary parameters (α, τv) = (0.75, 0.75); no verifier distribution
or reward is added to the prompt. It uses the same clipped-PPO implementation, task streams,
and optimization budget, with the one-step credit assignment described below. The Bayes DP-
score distillation condition rolls out πscore
B,0.02 and minimizes cross-entropy to its complete masked
policy at every assistant decision position. It receives neither outcome nor process rewards and
serves as a supervised smooth-reference condition rather than an algorithm-discovery or outcome-
optimal condition.
Optimization. We fine-tune in bfloat16 with a maximum context length of 4,096 and zero dropout.
Each PPO update collects multiple fresh episodes, followed by four epochs over episode minibatches
of size 32. We use AdamW with actor learning rate 1 × 10−6, value-head learning rate 5 × 10−6,
weight decay 0.01, a 3% linear warmup followed by cosine decay, PPO clip ratio 0.2, value-loss
coefficient 0.5, and gradient-norm clipping at 1. Outcome-reward advantages use GAE withγPPO = 1
and λ = 1, which reduces to the Monte Carlo return on complete episodes. One-step process reward
advantages use γPPO = 0, so the target at each decision is its immediate realized verifier reward.
34

## B-d568f605591a86

candidate openreview-8OOMlVFxb0 PDF page 35

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
All visited decision positions contribute to the PPO loss, but a later verifier score is not credited to
an earlier action. Value targets and advantages are standardized over all decision positions in each
rollout batch. The entropy coefficient decreases linearly from 0.01 to zero during the first 30% of
updates; no reference-policy KL reward is used.
Distillation uses the same pretrained initialization, context length, full-parameter update, batch size of
128 fresh oracle trajectories, and 4,000-update budget. It uses AdamW with learning rate 1 × 10−5,
weight decay 0.01, the same warmup and cosine schedule, and gradient-norm clipping at 1. Five
seeds are fixed before training. Every result uses the final-budget checkpoint; neither candidate
distances nor paraphrase evaluations are used for hyperparameter choice or checkpoint selection.
Text evaluations. We evaluate each trained condition on fresh BTS tasks rendered with (i) the
training-template families, (ii) each of the eight held-out paraphrase families, and (iii) a description-
kernel mismatch control. In the mismatch control, tool-card bodies are permuted among action
identifiers while the simulator kernels associated with those identifiers remain fixed. We pair the
same canonical tasks and histories across textual renderings and denote the text evaluation histories
by Dtext. We report text and symbolic results separately, with candidate-distance profiles evaluated
at the fixed temperature τ = 0.02.
Table 24: Natural-language tool use under three training objectives. The shuffled-card control breaks
the mapping between tool descriptions and environment kernels.
Training Evaluation Bayes-ref. TV ↓ KG-ref. TV ↓ return ↑
Outcome reward
training templates 0.131 ± 0.012 0.191± 0.015 0.676± 0.018
unseen paraphrases 0.178 ± 0.014 0.245± 0.019 0.641± 0.021
shuffled cards 0.674 ± 0.023 0.698± 0.020 0.296± 0.015
One-step
process reward
training templates 0.268 ± 0.018 0.114± 0.011 0.629± 0.020
unseen paraphrases 0.277 ± 0.021 0.153± 0.013 0.602± 0.023
shuffled cards 0.671 ± 0.019 0.685± 0.022 0.290± 0.014
Bayes DP-score
distillation
training templates 0.082 ± 0.008 0.127± 0.010 0.726± 0.016
unseen paraphrases 0.104 ± 0.010 0.143± 0.012 0.691± 0.019
shuffled cards 0.676 ± 0.021 0.689± 0.018 0.289± 0.013
Table 25: Additional candidate-distance means for the text conditions in Table 24, evaluated with
the same text histories and weights as its Bayes/KG columns. These three distances are available as
means only; they do not certify a seed-stable nearest-candidate label.
Training Evaluation Two-step TV Entropy TV Open-loop TV
Outcome reward
training templates .155 .232 .288
unseen paraphrases .206 .282 .334
shuffled cards .683 .708 .721
One-step
process reward
training templates .229 .199 .300
unseen paraphrases .244 .220 .313
shuffled cards .678 .704 .720
Bayes DP-score
distillation
training templates .089 .174 .251
unseen paraphrases .123 .211 .290
shuffled cards .680 .713 .718
Together with Table 24, the expanded means remain closest to Bayes for outcome training and
distillation, and to KG for the verifier, on both normal templates and paraphrases. For distilled models
on paraphrases, Bayes and two-step distances are 0.104 and 0.123; the mean gap is 0.019, but these
aggregate results do not establish seedwise stability. In the mismatch control, distances to every
candidate are large, so a small relative advantage is not interpreted as reliable algorithm recovery.
35

## B-f011baf45fde87

candidate openreview-8OOMlVFxb0 PDF page 9

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
0.0
0.2
0.4
0.6
0.8Candidate TV ↓
(a) Outcome reward
0.131 0.178
0.674
0.191
0.245
0.698
(b) One-step process reward
0.268 0.277
0.671
0.114 0.153
0.685
(c) Bayes DP-score distillation
0.082 0.104
0.676
0.127 0.143
0.689
Training
templates
Unseen
paraphrases
Shuffled
cards
0.0
0.2
0.4
0.6
0.8Return ↑
0.676 0.641
0.296
Training
templates
Unseen
paraphrases
Shuffled
cards
0.629 0.602
0.290
Training
templates
Unseen
paraphrases
Shuffled
cards
0.726 0.691
0.289
Bayes DP reference KG reference Return
Figure 5: Natural-language tool use under three training objectives. Top: paired bars compare
distances to Bayes DP and KG references; the closer candidate is unchanged under unseen paraphrases.
Bottom: task returns decrease modestly under paraphrases and sharply under shuffled cards, and
move all policies far from both references. Appendix Table 24 reports all values.
6.4 N ATURAL -LANGUAGE TOOL USE WITH A PRETRAINED LLM
The symbolic experiments show that learned decisions change with the training objective. We now
test whether these differences persist when a pretrained language model receives the same task
information through natural-language descriptions. We fine-tune Qwen2.5-1.5B-Instruct (Qwen et al.,
2025) on BTS with outcome reward, one-step process reward, and Bayes DP-score distillation, then
evaluate training templates, unseen paraphrases, and a shuffled-description control. Appendix G.9
gives the protocol.
Figure 5 shows that these behavioral differences persist with language inputs and unseen paraphrases.
Outcome reward training is Bayes DP-like, whereas one-step process reward training is KG-like.
Distillation most closely matches its supplied Bayes DP reference. Appendix Table 25 compares the
models with additional candidates. The same nearest-candidate relationships persist across unseen
paraphrases with modest return degradation. Shuffling tool cards instead collapses returns and moves
every policy far from both candidates. Though the model receives numerical observation models
and a fixed action vocabulary that departures from real agentic task, generalization across task and
tool paraphrases, together with the shuffled-description control, indicates dependence on description
semantics rather than a fixed token-level rule.
7 C ONCLUSION AND LIMITATIONS
We formalize Agentic ICL as interactive adaptation in which a fixed-parameter Transformer shapes its
future evidence through actions, without requiring observations to reveal rewards. Our construction
realizes regular finite-horizon recursions with a bound on autonomous return loss, and distillation
demonstrates learned execution. Reward experiments link decision differences to outcome-optimal
action ordering: a perturbed process reward that preserves this ordering retains behavior close to
outcome training, while objective interventions shift learned decisions as alignment changes. The out-
come/process decision contrast also persists across textual paraphrases in a pretrained language model.
The theory establishes expressivity under regularity assumptions without guaranteeing optimization
convergence. Behavioral comparisons are candidate-relative, and probes do not identify a unique
internal algorithm. Experiments use small structured tasks, hand-specified verifiers, and a potential-
based control whose perturbation preserves optimal actions exactly. These results do not establish
robustness to arbitrary process-reward errors or learned verifiers. Language-model tests supply
observation models and constrain actions, leaving generalization to open-ended agents with unknown
tool semantics, longer interactions, and context compression unresolved.
9
