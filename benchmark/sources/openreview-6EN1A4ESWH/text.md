# CtrlMol: Controllable Molecular Generation for Drug Design via Flexible Condition-Adaptive Diffusion

## B-08e9e14db4737c

candidate openreview-6EN1A4ESWH PDF page 18

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
B.2 METRICS
Following TarPass, we evaluate CtrlMol from four complementary perspectives: basic performance,
molecular property, binding affinity, and target specificity.
BASICPERFORMANCE
•Validity:Validity measures the proportion of generated molecules that can be successfully
parsed and sanitized by RDKit. A high validity score indicates that the model can reliably
generate chemically interpretable molecules.
•Diversity (Uniq@1k):measures the fraction of unique molecules among the first 1,000 gen-
erated molecules, computed as the number of distinct canonical SMILES divided by 1,000.
MOLECULARPROPERTY
To evaluate whether generated molecules match the physicochemical and structural properties of
target-specific active compounds, we follow TarPass and compute distributional distances over 15
molecular descriptors.
The 15 descriptors are listed below.
•Molecular Weight (MolWt):Molecular weight measures the overall size of a molecule. It is
a basic physicochemical descriptor strongly related to oral bioavailability, docking score bias,
and drug-likeness.
•Heavy Atom Count (HeavyA):Heavy atom count is the number of non-hydrogen atoms in
a molecule. It reflects molecular size while avoiding the variability introduced by implicit or
explicit hydrogens.
•cLogP:cLogP estimates the octanol-water partition coefficient and measures molecular hy-
drophobicity. It is closely associated with permeability, solubility, and nonspecific binding
risk.
•Topological Polar Surface Area (TPSA):TPSA measures the surface area contributed by
polar atoms, mainly oxygen and nitrogen atoms. It is commonly used to estimate membrane
permeability and oral absorption.
•Number of Hydrogen-Bond Donors (HBD):This descriptor counts atoms that can donate
hydrogen bonds. It reflects the molecule’s ability to form directional polar interactions with
protein residues.
•Number of Hydrogen-Bond Acceptors (HBA):This descriptor counts atoms that can accept
hydrogen bonds. It is important for evaluating potential protein-ligand interaction patterns and
drug-likeness.
•Number of Rotatable Bonds (RotBonds):The number of rotatable bonds measures molecular
flexibility. Molecules with too many rotatable bonds may suffer from high conformational
entropy penalties during binding.
•Fraction of sp3 Carbons (Fsp3):Fsp3 measures the fraction of carbon atoms with sp3 hy-
bridization. It reflects molecular three-dimensionality and saturation. Higher Fsp3 is often
associated with more complex and less planar drug-like structures.
•Heteroatom Count (HeteroA):Heteroatom count measures the number of atoms other than
carbon and hydrogen, such as N, O, S, P, and halogens. It reflects the potential for polar
interactions and functional group diversity.
•Molecular Volume (MolVol):Molecular volume estimates the three-dimensional steric size
occupied by a molecule and is related to pocket occupancy, molecular shape, and overall ligand
bulk.
•Number of Rings (Rings):This descriptor counts the total number of ring systems in a
molecule. Ring structures are important for molecular rigidity, binding shape complementarity,
and drug-like scaffold formation.
•Number of Molecular Graph Fragments (MGFrags):MGFrags counts the number of dis-
connected fragments in the molecular graph, where values greater than one may indicate in-
complete or disconnected molecular structures.
18

## B-12d4fa47fcc45c

candidate openreview-6EN1A4ESWH PDF page 20

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
NON-3D MODELS
Non-3D models generate molecular strings, molecular graphs, or building-block combinations with-
out explicitly constructing molecules inside the 3D binding pocket.
•DeepBlock:DeepBlock is a building-block-based ligand generation model designed for ratio-
nal ligand generation with toxicity control. It constructs molecules from chemically meaningful
reactive building blocks and benefits from chemical pretraining.
•DRAGONFLY:DRAGONFLY is a prospective de novo drug design method based on deep
interactome learning. It incorporates target-related information through learned interaction rep-
resentations and generates molecules without explicit 3D in situ construction.
•SimpleSBDD:SimpleSBDD is a simplified structure-based drug design model that generates
2D molecular structures conditioned on target-related information. Although it uses target
information, it does not perform full 3D atom-by-atom construction inside the binding pocket.
•TamGen:TamGen is a target-aware molecule generation model based on a chemical language
model. It generates molecular strings conditioned on target information and benefits from large-
scale pretraining on PubChem and CrossDocked2020. Since it operates mainly in molecular
string space, it is categorized as a non-3D method.
3D INSITUMODELS
3D in situ models directly generate molecules inside target binding pockets. These methods explic-
itly use pocket geometry and are expected to better capture spatial complementarity and protein-
ligand interactions. However, they usually require high-quality target structures, incur higher com-
putational cost, and may suffer from pose plausibility issues such as steric clashes, unrealistic con-
formations, or incomplete molecular graphs.
•DiffSBDD:DiffSBDD is an equivariant diffusion model for structure-based drug design. It
generates 3D molecular structures conditioned on protein binding pockets and is trained on
CrossDocked2020.
•DrugFlow:DrugFlow is a flow-based molecular generation model that learns multi-domain
distributions for de novo drug design. It operates in 3D binding pockets and generates
molecules conditioned on structural information.
•IPDiff:IPDiff is a 3D diffusion model that incorporates protein-ligand interaction priors into
binding-aware molecular generation. It aims to improve interaction fidelity by explicitly mod-
eling interaction-related information.
•Lingo3DMol:Lingo3DMol formulates 3D molecular generation in pockets using a language-
modeling framework. It generates molecules conditioned on pocket environments and incor-
porates interaction-related information during generation.
•MolCraft:MolCraft is a structure-based drug design model that generates molecules in a
continuous parameter space. It is trained on CrossDocked2020 and belongs to the 3D in situ
paradigm.
•PocketFlow:PocketFlow is a data- and knowledge-driven structure-based molecular genera-
tive model. It generates molecules inside protein pockets and incorporates chemical knowledge
constraints to improve chemical validity and plausibility.
•SurfGen:SurfGen generates molecules by learning from topological surface and geometric
structure information. It explicitly uses protein surface and binding geometry to construct 3D
molecules in target pockets.
•TargetDiff:TargetDiff is a 3D equivariant diffusion model for target-aware molecular gen-
eration and affinity prediction. It generates molecules conditioned on target pocket structures
through an equivariant denoising process.
OPTIMIZATION-BASEDMETHODS
Optimization-based methods further guide molecular generation toward desired objectives such as
docking score, binding affinity, drug-likeness, or other molecular properties.
20

## B-17630fbc2bc651

candidate openreview-6EN1A4ESWH PDF page 5

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
molecule( ˆX, ˆA, ˆB)from noise, guided at every step by the condition system. Details are provided
in Appendix A.
Condition Module.Conditions serve as the key mechanism for guiding molecular generation to-
ward specific design requirements. Given a drug design task, relevant reference molecules and target
pockets are retrieved from databases to serve as two set of conditions. Through Arbitrary-Count
Condition Encoding, a set of retrieved reference molecular SMILES are encoded by a molecular
condition encoder into a set of molecular fingerprints; a set of retrieved target pocket structures are
encoded by a pocket condition encoder into a set of pocket fingerprints. The two sets of finger-
prints are respectively aggregated by Self-Adaptive Condition Modulation into the denoising net-
work in a unified manner at every step. Through Independent Dual-Axis Classifier-Free Guidance,
the guidance strengths of molecular and pocket conditions can be independently controlled to adjust
generation toward design requirements. Details are provided in Section 3.4.
Molecular Output Module.The denoised( ˆX, ˆA, ˆB)is converted by a molecular decoder into a
SMILES string. This process checks chemical validity and rationality, and the generation is deemed
unsuccessful if the denoised result violates chemical rules.
3.3 MOLECULARREPRESENTATION ANDCONFORMERGENERATION
Molecular Representation.A molecule is represented by the triplet(X, A, B).
X∈R N×3 denotes the 3D coordinates of N heavy atoms.
A∈ {∅,C, O, N, P, S, X} N denotes atom types, where∅represents a null atom (no atom at that
position), C/O/N/P/S represent common elements, X unifies halogens F/Cl/Br/I, and hydrogens are
implicitly encoded.
B∈ {∅,−,=,#,:} N(N−1)/2 denotes bond type matrix: null bond (∅), single bond (−), double
bond (=), triple bond (#), and aromatic bond (:).
Flexible-size Molecular Generation.Existing molecular generation methods typically require
specifying the number of atoms before inference ( ¨Unl¨u et al., 2025; Peng et al., 2026; Zhang et al.,
2025), which is impractical since molecular size is unknown beforehand. By introducing null atom
type and null bond type, our model eliminates this impractical requirement. It autonomously de-
termines molecular size within a fixed-dimensional tensor, dynamically deciding during denoising
which positions correspond to real atoms and which remain vacant. We setN= 50in this work,
enabling generation of molecules with up to 50 heavy atoms.
Conformer Generation.The SMILES is first parsed into a molecular graph(A, B)via RDKit (Lan-
drum et al.). Initial 3D coordinates are then randomly generated for the molecule, followed by
energy minimization with the MMFF94s force field (Halgren, 1999) to obtain optimized 3D co-
ordinatesX. Through this process, a SMILES string is encoded into a randomly initialized 3D
conformer.
On-the-Fly Conformer Generation.Common training datasets (Tingle et al., 2023; Knox et al.,
2024) maintain a one-to-one mapping between molecular formula and 3D conformer, assuming
each molecule has a unique ground-state structure. In reality, however, molecules adopt different
conformations depending on their binding environment (Zhao et al., 2025a). The same molecule
can exhibit multiple conformations when binding to different targets, or even to the same target.
To address this, we generate conformers on-the-fly during training rather than drawing from a fixed
dataset. Each time a molecule is encoded, a distinct conformer is randomly produced, implicitly
augmenting the training data with conformational diversity. This approach encourages the model
to learn the chemical essence of atomic connectivity rather than memorize specific conformers,
yielding stronger generalization to unseen conformations at inference.
3.4 FLEXIBLECONDITIONENCODING ANDCONTROLLABLEGUIDANCE
Conditions are integrated into the denoising network at every time step to guide the generation
process.
5

## B-190b2b85325d39

candidate openreview-6EN1A4ESWH PDF page 8

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
broader target-specific chemical space coverage over rigid target docking. On this basis, CtrlMol can
further leverage its flexible condition and controllable guidance mechanism to adjust the trade-off
between coverage and binding.
Table 1:Main results on TarPass benchmark.CtrlMol is compared against 15 baseline models
across basic performance, molecular property, binding affinity, and target specificity. The reported
values are averaged across 18 targets (Appendix B.5).
Basic Performance Molecular Property Binding Affinity Target Specificity
Model ValidityDiversity
(Uniq@1k)
Descriptor Distance (↓)Vina Score(Med.,↓)
Ligand
Efficiency (↑)
Molecular Distance in Chemical Space (↓)
Wass. Ref Wass. Shift Sim. Ref (↑) FCD Ref FCD Shift
DRAGONFLY 1 1 0.629 2.166 -8.192 0.261 0.127 27.131 1.443
DeepBlock 1 1 0.884 2.685 -7.776 0.339 0.120 22.982 1.313
SimpleSBDD 0.966 0.987 0.856 2.322 -8.230 0.319 0.112 39.009 2.665
TamGen∼1 0.968 1.346 4.243 -6.890 0.357 0.103 36.648 2.078
DiffSBDD 0.968 0.987 1.170 3.957 -8.032 0.326 0.094 31.824 2.093
DrugFlow 0.831 0.399 0.633 2.512 -9.776 0.3350.13032.178 2.442
IPDiff∼1 0.940 1.906 6.896 -7.7180.4210.069 50.292 3.830
Lingo3DMol∼1 0.906 0.822 3.408 -9.024 0.285 0.122 29.541 2.131
MolCraft 1 0.498 0.763 2.649 -9.987 0.350 0.112 38.369 2.880
PocketFlow 1 0.692 1.414 4.722 -7.795 0.412 0.097 36.967 2.469
SurfGen 1 0.948 1.122 4.126 -9.531 0.377 0.110 42.562 3.245
TargetDiff∼1 0.968 1.233 4.719 -7.583 0.399 0.096 44.594 3.497
DrugFlow-PA 0.600 0.637 0.955 3.658 -10.374 0.404 0.128 42.897 3.371
MolPilot 1 1 0.796 3.156-10.4830.338 0.119 41.495 3.208
REINVENT4 1 1 1.392 5.592 -10.023 0.367 0.103 49.921 3.890
CtrlMol 1 1 0.497 1.760-8.510 0.309 0.128 16.351 1.210
Random — — 0.695 — -7.835 0.293 0.116 26.984 —
4.3 CASESTUDY ANDABLATIONSTUDY
Case Study on ADRB2 Drug Design.We selectedβ2-adrenergic receptor (ADRB2), a well-
studied GPCR target for cardiovascular diseases (Rosenbaum et al., 2007), as a case study to demon-
strate CtrlMol’s flexibility and controllability in drug design. Our objective is to generate novel
molecules covering the target-specific chemical space of known ADRB2 ligands. This addresses a
key need in early drug discovery: exploring broad chemical diversity before selecting candidates for
affinity optimization.
For ADRB2 drug design, we retrieved a natural substrate epinephrine, 13 clinical antagonists, 25
clinical agonists, and hundreds of experimental active ligands for available molecular conditions, as
well as dozens of target-ligand binding structures for available pocket conditions (Table 2). Using
these conditions, we investigated how retrieval conditions and guidance scales affect generation
distribution through two ablation studies. For each experiment, we generate 1,000 molecules and
measure FCD between the generated distribution and ADRB2 reference ligand distribution. Lower
FCD indicates better coverage of the target-specific chemical space.
Ablation Study on Retrieval Conditions.We ablated the retrieval condition quantities by fixing
guidance scales atg M =g P = 1and systematically varying molecular condition countKand
pocket condition countLto analyze their impact on generation quality (Table 2). When both con-
ditions are absent (K= 0, L= 0), the generation distribution stays far from the ADRB2 reference
distribution with an FCD of 27.42, but closely resembles a random drug-like distribution, reaching
an FCD of 9.96 that almost approaches the minimum FCD achievable for a 1,000-molecule set (Ap-
pendix B.7). As the molecular condition countKincreases withL= 0, FCD decreases steadily and
plateaus at∼19onceKreaches∼100, indicating saturation thereafter. Notably, one molecular
condition (K= 1) causes overfocused generation distribution that is also far from the reference
(FCD = 28.33), meanwhile far from random distributions (FCD = 25.02), distinguishing it from
unconditional generation (Appendix B.7). As the pocket condition countLincreases withK= 0,
FCD decreases slowly to∼25onceLreaches∼20, with only limited gains over the unconditioned
8

## B-1b2dbb5173474f

candidate openreview-6EN1A4ESWH PDF page 13

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
Tiqing Liu, Linda Hwang, Stephen K Burley, Carmen I Nitsche, Christopher Southan, W Patrick
Walters, and Michael K Gilson. Bindingdb in 2024: a fair knowledgebase of protein-small
molecule binding data.Nucleic Acids Research, 53(D1):D1633–D1644, 01 2025. ISSN 1362-
4962. doi: 10.1093/nar/gkae1075. URLhttps://doi.org/10.1093/nar/gkae1075.
Edgar L ´opez-L´opez, Pamela I. Hern ´andez-Estrada, Angel N. Toto-Vazquez, Diana V . ´Avila
Mart´ınez, Ola Spjuth, and Jos ´e L. Medina-Franco. Benign-by-design chemistry: Reinvent-
ing ligand-based drug design at the edge of ai.Drug Discovery Today, 31(4):104691, 2026.
ISSN 1359-6446. doi: https://doi.org/10.1016/j.drudis.2026.104691. URLhttps://www.
sciencedirect.com/science/article/pii/S1359644626000966.
Andreas Mayr, G ¨unter Klambauer, Thomas Unterthiner, Marvin Steijaert, J ¨org K. Wegner, Hugo
Ceulemans, Djork-Arn´e Clevert, and Sepp Hochreiter. Large-scale comparison of machine learn-
ing methods for drug target prediction on chembl.Chemical Science, 9(24):5441–5451, 06
2018. ISSN 2041-6520. doi: 10.1039/c8sc00148k. URLhttps://doi.org/10.1039/
c8sc00148k.
Alexander Quinn Nichol and Prafulla Dhariwal. Improved denoising diffusion probabilistic mod-
els. In Marina Meila and Tong Zhang (eds.),Proceedings of the 38th International Confer-
ence on Machine Learning, volume 139 ofProceedings of Machine Learning Research, pp.
8162–8171. PMLR, 18–24 Jul 2021. URLhttps://proceedings.mlr.press/v139/
nichol21a.html.
Noel M. O’Boyle, Michael Banck, Craig A. James, Chris Morley, Tim Vandermeersch, and Ge-
offrey R. Hutchison. Open babel: An open chemical toolbox.Journal of Cheminformatics,
3(1):33, Oct 2011. doi: 10.1186/1758-2946-3-33. URLhttps://doi.org/10.1186/
1758-2946-3-33.
Daniele Pala and David E. Clark. Caught between a rock and a hard place: current challenges in
structure-based drug design.Drug Discovery Today, 29(9):104106, 2024. ISSN 1359-6446. doi:
https://doi.org/10.1016/j.drudis.2024.104106. URLhttps://www.sciencedirect.com/
science/article/pii/S1359644624002319.
Krunoslav Lehman Pavasovic, Jakob Verbeek, Giulio Biroli, and Marc Mezard. Classifier-free
guidance: From high-dimensional analysis to generalized guidance forms, 2025. URLhttps:
//arxiv.org/abs/2502.07849.
William Peebles and Saining Xie. Scalable diffusion models with transformers. In2023 IEEE/CVF
International Conference on Computer Vision (ICCV), pp. 4172–4182, 2023. doi: 10.1109/
ICCV51070.2023.00387.
Jian Peng, Jun-Lin Yu, Zeng-Bao Yang, Yi-Ting Chen, Si-Qi Wei, Fan-Bo Meng, Yao-Geng
Wang, Xiao-Tian Huang, and Guo-Bo Li. Pharmacophore-oriented 3D molecular generation
toward efficient feature-customized drug discovery.Nature Computational Science, 5(10):898–
914, October 2025. ISSN 2662-8457. doi: 10.1038/s43588-025-00850-5. URLhttps:
//doi.org/10.1038/s43588-025-00850-5.
Xingang Peng, Ruihan Guo, Fenglin Guo, Ziyi Wang, Jiayu Sun, Jiaqi Guan, Yinjun Jia, Yan Xu,
Yanwen Huang, Muhan Zhang, Jian Peng, Xinquan Wang, Chuanhui Han, Zihua Wang, and
Jianzhu Ma. Unified modeling of 3d molecular generation via atomic interactions with PocketX-
Mol. 189(7):1904–1922.e28, 2026. ISSN 0092-8674. doi: 10.1016/j.cell.2026.01.003. URL
https://doi.org/10.1016/j.cell.2026.01.003.
Ethan Perez, Florian Strub, Harm de Vries, Vincent Dumoulin, and Aaron Courville. Film: vi-
sual reasoning with a general conditioning layer. InProceedings of the Thirty-Second AAAI
Conference on Artificial Intelligence and Thirtieth Innovative Applications of Artificial Intelli-
gence Conference and Eighth AAAI Symposium on Educational Advances in Artificial Intelli-
gence, AAAI’18/IAAI’18/EAAI’18. AAAI Press, 2018. ISBN 978-1-57735-800-8.
Rui Qin, Zijie Chen, Yurong Li, Meijing Fang, Longji Shen, Yilong Su, Odin Zhang, Qinghan Wang,
Qun Su, Jike Wang, Tingjun Hou, and Yu Kang. Revisiting target-aware de novo molecular
generation with tarpass: Between rational design and texas sharpshooter.Advanced Science,
13

## B-320fd9650b41a3

candidate openreview-6EN1A4ESWH PDF page 11

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
Prafulla Dhariwal and Alexander Nichol. Diffusion models beat gans on image synthesis.
In M. Ranzato, A. Beygelzimer, Y . Dauphin, P.S. Liang, and J. Wortman Vaughan (eds.),
Advances in Neural Information Processing Systems, volume 34, pp. 8780–8794. Curran
Associates, Inc., 2021. URLhttps://proceedings.neurips.cc/paper_files/
paper/2021/file/49ad23d1ec9fa4bd8d77d02681df5cfa-Paper.pdf.
Yuanqi Du, Arian R. Jamasb, Jeff Guo, Tianfan Fu, Charles Harris, Yingheng Wang, Chenru Duan,
Pietro Li`o, Philippe Schwaller, and Tom L. Blundell. Machine learning-aided generative molec-
ular design. 6(6):589–604, 2024. ISSN 2522-5839. doi: 10.1038/s42256-024-00843-5. URL
https://doi.org/10.1038/s42256-024-00843-5.
P. Gainza, F. Sverrisson, F. Monti, E. Rodol `a, D. Boscaini, M. M. Bronstein, and B. E. Cor-
reia. Deciphering interaction fingerprints from protein molecular surfaces using geometric deep
learning.Nature Methods, 17(2):184–192, February 2020. ISSN 1548-7105. doi: 10.1038/
s41592-019-0666-6. URLhttps://doi.org/10.1038/s41592-019-0666-6.
Jiaqi Guan, Wesley Wei Qian, Xingang Peng, Yufeng Su, Jian Peng, and Jianzhu Ma. 3d equivariant
diffusion for target-aware molecule generation and affinity prediction. InInternational Confer-
ence on Learning Representations, 2023.
Zirui Guo, Xubin Ren, Lingrui Xu, Jiahao Zhang, and Chao Huang. Rag-anything: All-in-one rag
framework, 2025. URLhttps://arxiv.org/abs/2510.12323.
Thomas A. Halgren. Mmff vi. mmff94s option for energy minimization studies.Journal
of Computational Chemistry, 20(7):720–729, 1999. doi: https://doi.org/10.1002/(SICI)
1096-987X(199905)20:7⟨720::AID-JCC7⟩3.0.CO;2-X. URLhttps://onlinelibrary.
wiley.com/doi/abs/10.1002/%28SICI%291096-987X%28199905%2920%3A7%
3C720%3A%3AAID-JCC7%3E3.0.CO%3B2-X.
Xu Han, Caihua Shan, Yifei Shen, Can Xu, Han Yang, Xiang Li, and Dongsheng Li. Training-
free multi-objective diffusion model for 3d molecule generation. InThe Twelfth International
Conference on Learning Representations, 2024. URLhttps://openreview.net/forum?
id=X41c4uB4k0.
Jonathan Ho and Tim Salimans. Classifier-free diffusion guidance, 2022. URLhttps://arxiv.
org/abs/2207.12598.
Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. In
H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin (eds.),Advances in Neu-
ral Information Processing Systems, volume 33, pp. 6840–6851. Curran Associates, Inc.,
2020. URLhttps://proceedings.neurips.cc/paper_files/paper/2020/
file/4c5bcfec8584af0d967f1ab10179ca4b-Paper.pdf.
Emiel Hoogeboom, Didrik Nielsen, Priyank Jaini, Patrick Forr ´e, and Max Welling. Argmax
flows and multinomial diffusion: Learning categorical distributions. In M. Ranzato,
A. Beygelzimer, Y . Dauphin, P.S. Liang, and J. Wortman Vaughan (eds.),Advances in Neu-
ral Information Processing Systems, volume 34, pp. 12454–12465. Curran Associates, Inc.,
2021. URLhttps://proceedings.neurips.cc/paper_files/paper/2021/
file/67d96d458abdef21792e6d8e590244e7-Paper.pdf.
Emiel Hoogeboom, V´ıctor Garcia Satorras, Cl´ement Vignac, and Max Welling. Equivariant diffu-
sion for molecule generation in 3D. In Kamalika Chaudhuri, Stefanie Jegelka, Le Song, Csaba
Szepesvari, Gang Niu, and Sivan Sabato (eds.),Proceedings of the 39th International Confer-
ence on Machine Learning, volume 162 ofProceedings of Machine Learning Research, pp.
8867–8887. PMLR, 17–23 Jul 2022. URLhttps://proceedings.mlr.press/v162/
hoogeboom22a.html.
Qiaoyu Hu, Changzhi Sun, Huan He, Jiazheng Xu, Danlin Liu, Wenqing Zhang, Sumeng Shi,
Kai Zhang, and Honglin Li. Target-aware 3d molecular generation based on guided equivari-
ant diffusion.Nature Communications, 16(1):7928, Aug 2025. ISSN 2041-1723. doi: 10.1038/
s41467-025-63245-0. URLhttps://doi.org/10.1038/s41467-025-63245-0.
11

## B-3752f9bc1e514b

candidate openreview-6EN1A4ESWH PDF page 19

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
•Normalized Spacial Score (nSPS):nSPS is a normalized measure of molecular spatial com-
plexity that captures three-dimensional structural features such as hybridization, stereochem-
istry, ring systems, and molecular branching.
•Number of Torsions (Torsions):Torsions measure the number of torsional degrees of freedom
in a molecule and reflect conformational flexibility relevant to ligand binding and pose stability.
•BertzCT Molecular Complexity (BertzCT):BertzCT is a topological complexity index that
measures molecular graph complexity. It captures branching, ring complexity, and overall
structural intricacy.
For each descriptor, we compute the Wasserstein distance between the descriptor distribution of
generated molecules and that of reference active compounds. The final Wasserstein distance is
obtained by averaging over all 15 descriptors. A smaller Wasserstein distance indicates that the
generated molecules better match the molecular property distribution of known active compounds
for the target.
BINDINGAFFINITY
•Vina docking score:Binding affinity is evaluated using the Vina docking score under the
standardized TarPass docking protocol, where each generated molecule is docked to the corre-
sponding target structure and the top-ranked pose is retained, with lower scores indicating more
favorable predicted binding.
•Ligand efficiency:Ligand efficiency normalizes the Vina docking score by the number of
heavy atoms in the molecule, helping distinguish compact and efficient binders from large
molecules that may obtain favorable docking scores mainly due to size-related bias.
TARGETSPECIFICITY
Target specificity evaluates whether the generated molecules are specifically biased toward the
chemical space of active compounds for the given target. We use ECFP4 Tanimoto similarity,
Fr´echet ChemNet Distance, and normalized shift metrics.
•ECFP4 Tanimoto similarity:ECFP4 Tanimoto similarity measures the structural similarity
between generated molecules and target-specific reference actives by averaging, over generated
molecules, the maximum ECFP4 fingerprint similarity to the active set, with higher values
indicating closer structural proximity to known target actives.
•Fr ´echet ChemNet Distance (FCD) distance:FCD distance compares the generated and
target-active molecular distributions in a learned ChemNet embedding space, with lower values
indicating that the generated molecules are distributionally closer to the target-specific active
compounds.
•Fr ´echet ChemNet Distance (FCD) shift:FCD shift measures the normalized deviation of the
generated molecular distribution from both the target-specific active distribution and the ran-
dom ChEMBL distribution, where values close to 1 indicate that generated molecules remain
within the general drug-like and target-relevant chemical region, while larger values suggest
stronger distributional deviation.
In this work, “distance” refers to the direct distributional distance between generated molecules and
reference active molecules. In contrast, “shift” refers to the normalized distance of the generated
distribution from both the reference active distribution and the random ChEMBL distribution. Dis-
tance reflects target-level proximity, while shift reflects whether the generated molecules remain in
a plausible drug-like chemical region.
B.3 BASELINES
Following TarPass, we compare CtrlMol with 15 representative molecular generation models span-
ning three major paradigms: non-3D models, 3D in situ models, and optimization-based methods.
19

## B-4ed64bb113740e

candidate openreview-6EN1A4ESWH PDF page 15

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
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez,
Lukasz Kaiser, and Illia Polosukhin. Attention is all you need, 2023. URLhttps://arxiv.
org/abs/1706.03762.
Enrico Ventura, Beatrice Achilli, Luca Ambrogioni, and Carlo Lucibello. Emergence of distor-
tions in high-dimensional guided diffusion models, 2026. URLhttps://arxiv.org/abs/
2602.00716.
Zixu Wang, Yangyang Chen, Pengsen Ma, Zhou Yu, Jianmin Wang, Yuansheng Liu, Xiucai Ye,
Tetsuya Sakurai, and Xiangxiang Zeng. Image-based generation for molecule design with sketch-
mol.Nature Machine Intelligence, 7(2):244–255, Feb 2025. ISSN 2522-5839. doi: 10.1038/
s42256-025-00982-3. URLhttps://doi.org/10.1038/s42256-025-00982-3.
Thanapat Worakul, Mohammed Azzouzi, Matthew D. Wodrich, and Cl´emence Corminboeuf. Mod-
ular framework for 3d molecular generation in computational chemistry applications.Journal
of the American Chemical Society, 148(25):25370–25388, 07 2026. ISSN 0002-7863. doi:
10.1021/jacs.5c19960. URLhttps://doi.org/10.1021/jacs.5c19960.
wwPDB consortium. Protein data bank: the single global archive for 3d macromolecular structure
data.Nucleic Acids Research, 47(D1):D520–D528, 01 2019. ISSN 0305-1048. doi: 10.1093/nar/
gky949. URLhttps://doi.org/10.1093/nar/gky949.
Weixin Xie, Jianhang Zhang, Qin Xie, Chaojun Gong, Yuhao Ren, Jin Xie, Qi Sun, You-
jun Xu, Luhua Lai, and Jianfeng Pei. Accelerating discovery of bioactive ligands with
pharmacophore-informed generative models. 16(1):2391, 2025. ISSN 2041-1723. doi: 10.1038/
s41467-025-56349-0. URLhttps://doi.org/10.1038/s41467-025-56349-0.
Barbara Zdrazil, Eloy Felix, Fiona Hunter, Emma J Manners, James Blackshaw, Sybilla Cor-
bett, Marleen de Veij, Harris Ioannidis, David Mendez Lopez, Juan F Mosquera, Maria Paula
Magarinos, Nicolas Bosc, Ricardo Arcila, Tevfik Kizil ¨oren, Anna Gaulton, A Patr ´ıcia Bento,
Melissa F Adasme, Peter Monecke, Gregory A Landrum, and Andrew R Leach. The chembl
database in 2023: a drug discovery platform spanning multiple bioactivity data types and time
periods.Nucleic Acids Research, 52(D1):D1180–D1192, 01 2024. ISSN 0305-1048. doi:
10.1093/nar/gkad1004. URLhttps://doi.org/10.1093/nar/gkad1004.
Odin Zhang, Xujun Zhang, Haitao Lin, Cheng Tan, Qinghan Wang, Yuanle Mo, Qiantai Feng,
Gang Du, Yuntao Yu, Zichang Jin, Ziyi You, Peicong Lin, Yijie Zhang, Yuyang Tao, Shicheng
Chen, Jack Xiaoyu Chen, Chenqing Hua, Weibo Zhao, Runze Ma, Yunpeng Xia, Kejun Ying, Jun
Li, Yundian Zeng, Lijun Lang, Peichen Pan, Hanqun Cao, Zihao Song, Bo Qiang, Jiaqi Wang,
Pengfei Ji, Lei Bai, Jian Zhang, Chang yu Hsieh, Pheng Ann Heng, Siqi Sun, Tingjun Hou, and
Shuangjia Zheng. Odesign: A world model for biomolecular interaction design, 2025. URL
https://arxiv.org/abs/2510.22304.
Zaixi Zhang, Wan Xiang Shen, Qi Liu, and Marinka Zitnik. Efficient generation of protein pockets
with PocketGen. 6(11):1382–1395, 2024. ISSN 2522-5839. doi: 10.1038/s42256-024-00920-9.
URLhttps://doi.org/10.1038/s42256-024-00920-9.
Qichang Zhao, Haochen Zhao, Linyuan Guo, Kai Zheng, Yajie Li, Qiao Ling, Jing Tang, Yao-
hang Li, and Jianxin Wang. Coldstartcpi: Induced-fit theory-guided dti predictive model
with improved generalization performance.Nature Communications, 16(1):6436, Jul 2025a.
ISSN 2041-1723. doi: 10.1038/s41467-025-61745-7. URLhttps://doi.org/10.1038/
s41467-025-61745-7.
Yanpeng Zhao, Yuting Xing, Yixin Zhang, Yifei Wang, Mengxuan Wan, Duoyun Yi, Chengkun Wu,
Shangze Li, Huiyan Xu, Hongyang Zhang, Ziyi Liu, Guowei Zhou, Mengfan Li, Xuanze Wang,
Zhengshan Chen, Ruijiang Li, Lianlian Wu, Dongsheng Zhao, Peng Zan, Song He, and Xiaochen
Bo. Evidential deep learning-based drug-target interaction prediction.Nature Communications,
16(1):6915, Jul 2025b. ISSN 2041-1723. doi: 10.1038/s41467-025-62235-6. URLhttps:
//doi.org/10.1038/s41467-025-62235-6.
15

## B-595c6d91fa9601

candidate openreview-6EN1A4ESWH PDF page 6

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
3.4.1 ARBITRARY-COUNTCONDITIONENCODING
Given a specific drug design task, we retrieve relevant reference molecules from any of chemi-
cal databases (e.g., ChEMBL (Zdrazil et al., 2024), PubChem (Kim et al., 2025), BindingDB(Liu
et al., 2025)) and target binding pockets from any of structural databases (e.g., UniProt (Consortium,
2025), PDB (wwPDB consortium, 2019), AlphaFold DB (Varadi et al., 2022)). The retrieval yields
a reference molecule setM={m 1, . . . , mK}and a target pocket setP={p 1, . . . , pL}, where
bothKandLare arbitrary non-negative integers determined by retrieval results and are mutually
independent.
Each moleculem i (provided as a SMILES string) is independently encoded by a molecular con-
dition encoderf M into a fingerprintϕ i =f M(mi), yielding a molecular fingerprint setΦ M =
{ϕ1, . . . , ϕK}. The molecular condition encoder can be a trainable model or any existing molecular
encoder (e.g., ECFP (Rogers & Hahn, 2010), ChemNet (Mayr et al., 2018), Uni-Mol (Ji et al.,
2024)). Likewise, each pocketp j (represented as a 3D structure) is independently encoded by
a pocket condition encoderf P into a fingerprintψ j =f P(pj), yielding a pocket fingerprint set
ΨP ={ψ 1, . . . , ψL}. The pocket condition encoder can also be a trainable model or any existing
pocket encoder (e.g., MaSIF (Gainza et al., 2020), DrugCLIP (Jia et al., 2026)). Empty condition
set (K= 0orL= 0) is regarded as zero padding vector.
3.4.2 SELF-ADAPTIVECONDITIONMODULATION
Each set of arbitrary-count fingerprints must be adaptively integrated into the denoising network in
a unified manner. The standard FiLM mechanism (Perez et al., 2018) maps a condition vectory
through an MLP to channel-wise scale and shift parameters(γ, β) = split
(︁
W2 SiLU(W1y)
)︁
, which
affinely modulate the denoising network’s hidden representation asz←γ⊙z+β. By reparameter-
izing the modulation asz←(1+γ)⊙z+β, the mechanism naturally degenerates to identityz←z
when the condition is absent (y= 0), natively supporting zero-condition cases. Furthermore, given
an arbitrary-count condition sety={y 1, ..., yN }, each conditiony i can independently generate its
modulation parameters through the MLP, which are then aggregated into unified parameters(γ, β)
and applied to the hidden representationz.
(γi, βi) = split
(︁
W2,SiLU(W 1yi)
)︁
, i= 1, ..., N
(γ, β) =
(︁
Agg(γ1, ..., γN),Agg(β 1, ..., βN)
)︁
For molecular conditionsMand pocket conditionsP, we independently apply the aggregation
mechanism to each type, yielding two sets of modulation parameters(γ M, βM)and(γ P , βP). We
implement aggregation as mean pooling. The final modulation averages the two branches
z← 1
2
[︁
(1 +γ M)⊙z+β M + (1 +γ P)⊙z+β P
]︁
When either condition type is absent, the corresponding parameters become zero, reducing to single-
type modulationz←(1 +γ)⊙z+β. When both are absent, it naturally degenerates to identity
z←z. This mechanism self-adaptively modulates the hidden representation given arbitrary-count
or absent conditions at every denoising step.
3.4.3 INDEPENDENTDUAL-AXISCLASSIFIER-FREEGUIDANCE
Classifier-free guidance (CFG) (Ho & Salimans, 2022; Rombach et al., 2022) trains the model by
randomly replacing the conditioncby∅with probabilityp drop, enabling the model to learn both
conditional predicted noiseϵ θ(xt, t, c)and unconditional predicted noiseϵ θ(xt, t,∅). At inference,
CFG extrapolates from the unconditional toward the conditional predicted noise with guidance scale
w, yielding guided noise estimate
ˆϵ=ϵθ(xt, t,∅) +w·(ϵ θ(xt, t, c)−ϵ θ(xt, t,∅)).
However, the conditioncaccommodates only a single condition type.
To independently control the guidance strengths of molecular conditionsMand pocket conditions
P, we extend the standard CFG to a dual-axis formulation. During training,MandPare indepen-
dently dropped with probabilitiesp M andp P, enabling the model to learn all four condition combi-
nations:(M,P),(M,∅),(∅,P), and(∅,∅). At inference, two independent guidance scalesg M
6

## B-6d2b2ab4627e80

candidate openreview-6EN1A4ESWH PDF page 3

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
2.2 CONDITIONALMOLECULARGENERATION
The key challenge in drug design lies in understanding drug-target interactions(Zhao et al., 2025b),
which result in two major paradigms of conditional generation: ligand-based drug design (LBDD)
and structure-based drug design (SBDD). LBDD methods use information from reference ligands as
conditions to guide the generation of similar novel molecules, including molecular physicochemical
properties (e.g., QED, SA) (Hu et al., 2025), molecular structures or fragments (e.g., scaffolds, phar-
macophores) (Peng et al., 2025), molecular-level features or fingerprints (e.g., Morgan fingerprints,
graph embeddings) (Joshi & Guven, 2025). These methods typically accept fixed types and fixed
counts of conditions as input. SBDD methods use information from target proteins as conditions to
guide the generation of novel molecules for binding to specific targets, including target sequences
(e.g., protein language model embeddings) (Su et al., 2026) and target pocket structures (e.g., 2D
surface embeddings, 3D geometry embeddings) (Isert et al., 2023). These methods typically allow
only a single target condition input at a time. Very few works attempt to combine LBDD and SBDD
by leveraging both reference ligand and target pocket information, but these methods still require
fixed types and fix counts of conditions, and even require ligand-pocket interaction information as
additional conditions (Cremer et al., 2026). However, such requirements are impractical in genera-
tion scenarios, as interaction information cannot be predetermined before the molecule is generated.
In recent years, Retrieval-Augmented Generation (RAG) has achieved remarkable success in natural
language processing (NLP) by dynamically retrieving relevant information from knowledge bases,
flexibly handling arbitrary types and counts of retrieval conditions as prompt (Guo et al., 2025).
However, RAG has rarely been introduced into non-NLP-based molecular generation models (Chan
et al., 2026), as these models struggle to handle variable counts of retrieval conditions, despite the
fact that retrieving reference ligands and target structures is the prerequisite step in practical drug
design.
2.3 CONDITIONINGMECHANISMS INDIFFUSIONMODELS
Conditioning mechanisms determine how condition information is incorporated into the denoising
network of diffusion models, directly affecting the responsiveness to conditions. Early diffusion
models simply concatenate condition embeddings with hidden representations and inject them into
the denoising network (Saharia et al., 2023), which requires fixed counts of conditions and lacks
active control over condition embeddings. Cross-attention mechanism treats condition embeddings
as key-value pairs and hidden representations as queries for interaction (Rombach et al., 2022),
enabling handling variable counts of conditions, but the computational complexity is inherently
large and scales linearly with the count of conditions. Feature-wise Linear Modulation (FiLM)
linearly projects condition embeddings into scale and shift parameters for affine transformation of
hidden representations (Perez et al., 2018), achieving direct control over conditions compared to
the concatenation mechanism and lower computational complexity compared to the cross-attention
mechanism. Although original FiLM still requires fixed counts of conditions, a series of adaptive
variants (e.g., AdaLN (Peebles & Xie, 2023)) have been widely adopted in diffusion models. The
controllability, low complexity, and extensibility of FiLM provide potential for adaptation to handle
variable counts of conditions.
2.4 CONTROLLABLEGENERATION VIAGUIDANCE
Guidance mechanisms enable diffusion models to control the influence of conditions at inference
time, without requiring model re-training. Classifier guidance uses gradients from external clas-
sifiers to direct sampling toward desired conditions at inference (Dhariwal & Nichol, 2021), but
requires training a separate classifier for each condition type. Classifier-free guidance (CFG) elimi-
nates the need for external classifiers by jointly training the model on both conditional and uncondi-
tional objectives with a dropout rate (Ho & Salimans, 2022), but requires a separate guidance scale to
adjust each condition type. The theory of one-dimensional CFG with one condition type is relatively
well-understood, and a few studies have applied it to molecular generation (Worakul et al., 2026;
Wang et al., 2025; Hu et al., 2025). However, two- or higher-dimensional CFG with multiple condi-
tion types suffers from a combinatorial explosion, leaving its theory underdeveloped (Schnell et al.,
2025) or even contested (Pavasovic et al., 2025; Ventura et al., 2026), and its applications remain
extremely rare. CFG and its variants have become the mainstream guidance mechanism for condi-
3

## B-768aa406b9b164

candidate openreview-6EN1A4ESWH PDF page 10

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
AIUSE STATEMENT
In this work, we used generative AI tools for writing refinement and language polishing. We have
not used generative AI tools for other tasks with required and recommanded disclosure, and the rest
of the required disclosure and recommanded tasks are not applicable to this work. We have reviewed
all AI-assisted work. All AI-edited text was manually checked by the authors against our original
drafts to ensure the intended meaning was preserved. We take responsibility for the final content of
this work, including text, claims or artifacts produced with the aid of generative AI.
ETHICS STATEMENT
The authors confirm that this work complies with the ICLR Code of Ethics and raises no ethical
concerns.
REPRODUCIBILITY STATEMENT
All experimental and computational details are described in Experiments and Appendix. All datasets
used are publicly available. We will release the code upon publication.
REFERENCES
Sarp Aykent and Tian Xia. Gotennet: Rethinking efficient 3d equivariant graph neu-
ral networks. In Y . Yue, A. Garg, N. Peng, F. Sha, and R. Yu (eds.),In-
ternational Conference on Learning Representations, volume 2025, pp. 40622–40646,
2025. URLhttps://proceedings.iclr.cc/paper_files/paper/2025/file/
64d4ff4fff788cdffe236f9ce8b09400-Paper-Conference.pdf.
Jonathan B. Baell and Georgina A. Holloway. New substructure filters for removal of pan assay
interference compounds (pains) from screening libraries and for their exclusion in bioassays.
Journal of Medicinal Chemistry, 53(7):2719–2740, 04 2010. doi: 10.1021/jm901137j. URL
https://doi.org/10.1021/jm901137j.
A. Patr ´ıcia Bento, Anne Hersey, Eloy F ´elix, Greg Landrum, Anna Gaulton, Francis Atkinson,
Louisa J. Bellis, Marleen De Veij, and Andrew R. Leach. An open source chemical struc-
ture curation pipeline using rdkit.Journal of Cheminformatics, 12(1):51, Sep 2020. ISSN
1758-2946. doi: 10.1186/s13321-020-00456-1. URLhttps://doi.org/10.1186/
s13321-020-00456-1.
G. Richard Bickerton, Gaia V . Paolini, J´er´emy Besnard, Sorel Muresan, and Andrew L. Hopkins.
Quantifying the chemical beauty of drugs.Nature Chemistry, 4(2):90–98, Feb 2012. ISSN 1755-
4349. doi: 10.1038/nchem.1243. URLhttps://doi.org/10.1038/nchem.1243.
Joey Chan, Wonbin Kweon, Ashley Shin, Niharika Bhattacharjee, Pengcheng Jiang, Yue Guo, and
Jiawei Han. Mole-rag: Molecular structure-enhanced retrieval-augmented generation for chem-
istry, 2026. URLhttps://arxiv.org/abs/2606.05693.
Lianghong Chen, Dongkyu Eugene Kim, Mike Domaratzki, and Pingzhao Hu. Uncertainty-aware
multi-objective reinforcement learning-guided diffusion models for 3d de novo molecular design.
InThe Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025. URL
https://openreview.net/forum?id=lu4cGylISh.
The UniProt Consortium. Uniprot: the universal protein knowledgebase in 2025.Nucleic Acids
Research, 53(D1):D609–D617, 01 2025. ISSN 1362-4962. doi: 10.1093/nar/gkae1010. URL
https://doi.org/10.1093/nar/gkae1010.
Julian Cremer, Ross Irwin, Alessandro Tibo, Jon Paul Janet, Simon Olsson, and Djork-Arn ´e
Clevert. FLOWR: flow matching for structure-aware de novo, interaction- and fragment-
based ligand generation.Nature Computational Science, 6(6):565–574, June 2026. ISSN
2662-8457. doi: 10.1038/s43588-026-00998-8. URLhttps://doi.org/10.1038/
s43588-026-00998-8.
10

## B-78e37a16506919

candidate openreview-6EN1A4ESWH PDF page 9

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
baseline. Interestingly, one pocket condition (L= 1) works better than several. Retrieval returns
diverse binding conformations of the eligible ADRB2 target, and pocket fingerprints are sensitive
enough to distinguish them. Aggregating them mixes conflicting geometric signals, which weakens
the guidance toward the target-specific chemical space. When both conditions are present, the re-
sults are overall an interpolation of the two single-condition outcomes with limited synergistic gains,
where molecular conditions dominate whenK≥50, and pocket conditions dominate otherwise. In
summary, retrieving approximately 100 molecular conditions and 1 pocket condition achieves near-
optimal performance.
Table 2: FCD between generated molecules and ADRB2 reference ligands with fixed guidance
scales (gM =g P = 1), and varying molecular condition countKand pocket condition countL.
K= 0K= 1K= 13K= 25K= 50K= 100K= 200K= 300
L= 027.42 28.33 25.68 21.27 19.4119.2519.55 19.57
L= 123.1828.57 25.07 21.24 20.48 19.63 19.92 20.63
L= 426.75 26.31 25.00 23.50 21.53 21.52 20.93 21.08
L= 1025.48 29.22 24.46 23.87 21.44 21.04 20.67 21.41
L= 2024.86 27.87 24.90 23.86 22.00 21.60 21.84 21.02
Ablation Study on Guidance Scales.We ablated the guidance scales by fixing retrieval condition
quantities atK= 300, L= 1and systematically varyingg M andg P to analyze their impact
on generation quality (Table 3). When both guidance scales vanish (g M = 0, gP = 0), the model
degenerates to unconditional generation, consistent with results in Table 2. Across all configurations,
gM = 2generally achieves optimal performance fixingg P, whileg P = 1does likewise fixingg M.
The two guidance scales jointly achieve optimal performance atgM = 2, gP = 1with FCD = 17.52,
demonstrating clear synergistic gains from independent dual-axis control (Appendix B.7 and B.8).
Conversely, excessively high guidance scales degrade performance.
Table 3: FCD between generated molecules and ADRB2 reference ligands with fixed retrieval con-
dition quantities (K= 300, L= 1), and varying guidance scalesg M andg P.
gM = 0g M = 1g M = 2g M = 3
gP = 027.42 19.57 19.19 20.34
gP = 123.18 20.6317.5219.31
gP = 224.48 21.48 18.19 19.35
gP = 326.35 21.99 18.75 19.15
5 CONCLUSION
In this work, we proposed CtrlMol, a controllable molecular generation framework via flexible
condition-adaptive diffusion model that addresses the limitations of existing methods in handling
diverse condition configurations and adjusting generation behavior. Through Arbitrary-Count Con-
dition Encoding, Self-Adaptive Condition Modulation, and Independent Dual-Axis Classifier-Free
Guidance, CtrlMol achieves both flexibility in accepting zero or more molecular and pocket condi-
tions, and controllability in separately adjusting their guidance strengths during inference. Extensive
experiments on the TarPass benchmark demonstrate that CtrlMol consistently outperforms existing
methods across molecular properties and target specificity, while case studies on target ADRB2
confirm that the flexibility and controllability jointly enable effective adjustment of generation dis-
tribution toward desired molecular profiles. CtrlMol provides a promising direction toward shift-
ing molecular generation from developer-centric technical implementations to user-centric practical
design requirements. Future work may explore additional condition types and multi-objective opti-
mization for broader drug design scenarios.
9

## B-93ae877187cfc7

candidate openreview-6EN1A4ESWH PDF page 2

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
On the other hand, without controllability over condition influence, overly strict adherence to refer-
ence conditions would eliminate the exploratory power of generative models. An ideal generation
system should be able to control how closely generated molecules match the conditions to balance
fidelity and novelty. Existing methods ( ¨Unl¨u et al., 2025; Xie et al., 2025; Zhang et al., 2024)
are commonly trained with fixed condition configurations and cannot adjust guidance strengths at
inference time, thus lacking the ability to control desired generation behavior. This mismatch be-
tween fixed input requirements and variable practical needs limits the utility of existing methods in
real-world drug design.
To address these challenges, we propose CtrlMol, a controllable molecular generation framework
via flexible condition-adaptive diffusion model. CtrlMol supports zero or more reference molecu-
lar conditions and/or target pocket conditions as input via an Arbitrary-Count Condition Encoding
mechanism, and natively adapts to different condition configurations within a unified framework
to meet customized design requirements. Through a Self-Adaptive Condition Modulation mecha-
nism, CtrlMol adaptively aggregates heterogeneous condition information of different counts and
types, and injects them into the diffusion process in a unified manner. At inference time, CtrlMol
employs an Independent Dual-Axis Classifier-Free Guidance mechanism that allows users to sep-
arately adjust the guidance strengths of molecular and pocket conditions, flexibly controlling the
generation direction toward desired design requirements. Extensive experiments on the TarPass
benchmark demonstrate that CtrlMol consistently outperforms existing methods across basic per-
formance, molecular properties, and achieves a 28.8% improvement over the second-best baseline
in target specificity. Further case studies on a cardiovascular target ADRB2 and systematic ablation
studies confirm that the flexibility in handling arbitrary-count conditions and the controllability in
adjusting dual-axis guidance scales jointly enable effective tuning of generation distribution toward
desired molecular profiles.
Our main contributions can be summarized as follows:
• We propose CtrlMol, a controllable molecular generation framework via flexible condition-
adaptive diffusion model, shifting drug design from developer-centric technical implementa-
tions to user-centric practical design requirements.
• We introduce Arbitrary-Count Condition Encoding (ACCE) and Self-Adaptive Condition Mod-
ulation (SACM) mechanisms that jointly enable flexible handling of variable or absent condi-
tions and their adaptive aggregation for unified modulation throughout the denoising process.
• We develop Independent Dual-Axis Classifier-Free Guidance (IDA-CFG) to separately control
the guidance strengths of molecular and pocket conditions during inference, achieving flexible
adjustment of the generation fidelity-diversity trade-off.
2 RELATEDWORK
2.1 DIFFUSIONMODELS FORMOLECULEGENERATION
Diffusion models (Ho et al., 2020) have been widely adopted for molecular generation tasks (Hooge-
boom et al., 2022) in recent years following their success in image generation, demonstrating su-
perior performance over V AEs and GANs in generation quality and sample diversity (Sun et al.,
2025). Early molecular generation primarily focused on generating SMILES strings or 2D molecu-
lar graphs, while recent research has shifted toward directly generating 3D molecular conformations
comprising atomic coordinates, atom types, and bond types (Sun et al., 2025). To ensure that gen-
erated molecular coordinates are equivariant to translation and rotation, these methods typically
employ SE(3)-equivariant network architectures (Liao et al., 2026; Aykent & Xia, 2025) and com-
bine hybrid diffusion processes that separately model continuous atomic coordinates and discrete
atom types and bond types (Peng et al., 2026). While unconditional diffusion models generate
diverse molecules, they lack specificity for practical drug design, which requires conditional guid-
ance to generate molecules satisfying particular property requirements or target binding constraints.
Existing conditional molecular diffusion methods typically inject condition information into the de-
noising network during training (Huang et al., 2024), or achieve conditional control during inference
through gradient guidance based on energy functions (Han et al., 2024) or predictive models (Chen
et al., 2025).
2

## B-9c471481416aa7

candidate openreview-6EN1A4ESWH PDF page 4

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
tional diffusion models owing to their flexible adjustment of condition strength, while independent
guidance on multiple condition types is a genuine requirement in real-world applications.
3 METHOD
3.1 PROBLEMFORMULATION
We study the task of molecular generation guided by two types of conditions: a set of refer-
ence moleculesM={m 1, . . . , mK}(K≥0)and a set of reference target pocketsP=
{p1, . . . , pL}(L≥0). We represent a molecule as a triplet(X, A, B), whereXdenotes atomic
coordinates,Adenotes atom types, andBdenotes bond types. We formulate the task by learning a
conditional distributionp θ(X, A, B| M,P)and sampling chemically valid, geometrically reason-
able molecules from it. BothMandPare mutually independent and can be arbitrary or absent.
Our model natively handles all condition configurations within a unified framework.
3.2 OVERVIEW
We present CtrlMol, an end-to-end framework for controllable molecular generation via flexible
condition-adaptive diffusion. As illustrated in Figure 1, the pipeline takes a SMILES string as input,
encodes an initial 3D conformer, diffuses and denoises the 3D molecular structure under indepen-
dent dual-axis guidance from arbitrary-count molecular and pocket conditions, finally decodes the
resulting structure back into a SMILES string.
Figure 1:Overview of CtrlMol framework.Training follows steps 1-2-3-4, inference follows
steps 3-4-5.
Molecular Representation Module.During training, each molecule in the dataset is provided as a
SMILES string and converted by a molecular encoder into a 3D conformer representation(X, A, B).
Details are provided in Section 3.3.
Diffusion Module.A hybrid diffusion process is employed: continuous diffusion for atomic coor-
dinatesX, and discrete diffusion for atom typesAand bond typesB. The forward process grad-
ually corrupts the real molecule(X, A, B)into noise; the reverse process reconstructs a structured
4

## B-a84003cabf3ce5

candidate openreview-6EN1A4ESWH PDF page 7

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
andg P control the contribution of each condition axis, yielding the guided estimate
ˆϵ= (1−α−β 1 −β 2)ϵθ(xt, t,∅,∅) +αϵ θ(xt, t,M,P) +β 1ϵθ(xt, t,M,∅) +β 2ϵθ(xt, t,∅,P),
whereα= min(g M, gP),β 1 =g M −α, andβ 2 =g P −α. This dual-axis CFG enables indepen-
dent control of molecular and pocket guidance strengths, allowing flexible adjustment of generation
toward specific design requirements.
4 EXPERIMENTS
4.1 EXPERIMENTALSETUP
Datasets.We trained CtrlMol on a combination of ChEMBL and BindingDB. ChEMBL provides
broad chemical diversity (2.8 M molecules), while BindingDB contributes target-ligand binding
annotations (2.7 M pairs), jointly covering both molecular properties and binding knowledge. The
same datasets serve as the retrieval source for molecular and pocket conditions during both training
and inference, and can be freely replaced by other databases. We evaluated CtrlMol on TarPass (Qin
et al., 2026), an external benchmark for fair evaluation of target-aware de novo molecular generation
models, comprising 18 well-studied targets and approximately 1,000 experimentally validated active
compounds per target. Details are provided in Appendix B.1.
Evaluation Metrics.Following TarPass, we evaluated CtrlMol across four complementary aspects:
basic performance (validity, diversity), molecular property (Wasserstein distance over 15 molecular
descriptors), binding affinity (Vina docking score, ligand efficiency), and target specificity (ECFP4
Tanimoto similarity, Fr ´echet ChemNet Distance (FCD) distance and shift). Distance means the
distance between generated distribution and reference distribution. Shift means the normalized dis-
tance of generated distribution from both reference and random distributions. Details are provided
in Appendix B.2.
Baselines.Following TarPass, we compared against 15 representative molecular generation models
spanning three paradigms: (i) non-3D models (DeepBlock, DRAGONFLY , SimpleSBDD, and Tam-
Gen), which generate 2D molecular graphs or strings without explicit structural geometry; (ii) 3D
in situ models (DiffSBDD, DrugFlow, IPDiff, Lingo3DMol, MolCraft, PocketFlow, SurfGen, and
TargetDiff), which operate directly on target pocket structures; and (iii) optimization-based methods
(DrugFlow-PA, MolPilot, and REINVENT), which further optimize generated molecules toward
desired properties to guide sampling. Details are provided in Appendix B.3.
4.2 MAINRESULTS
We present the main results on TarPass benchmark across 18 diverse targets in Table 1. CtrlMol
achieves perfect validity and diversity while demonstrating the best performance in molecular prop-
erty control and target specificity among all baselines. CtrlMol achieves perfect validity (1.0) and
diversity (1.0), meeting the basic generation quality requirements. For target specificity measured
by FCD and Tanimoto similarity to target-binding reference molecules (Appendix B.5), CtrlMol
substantially outperforms all baselines with the lowest FCD distances (FCD Ref = 16.351, FCD
Shift = 1.210), representing 28.8% improvement over the second-best DeepBlock, and competitive
molecular similarity (Sim. Ref = 0.128), demonstrating superior ability to capture target-specific
chemical space. For molecular property control measured by Wasserstein distance over 15 molec-
ular descriptors (Appendix B.6), CtrlMol also achieves the best performance (Wass. Ref = 0.497,
Wass. Shift = 1.760).
For binding affinity, CtrlMol outperforms all four non-3D methods (DRAGONFLY et al.), achieves
comparable performance to eight 3D in situ methods (DiffSBDD et al.), but lags behind all three
optimization-based methods (DrugFlow-PA et al.). This gap highlights the effectiveness of ex-
plicit optimization techniques in improving binding affinity, suggesting a promising direction for
future enhancement of CtrlMol. 3D in situ methods generate molecules directly within the fixed
target pocket structures provided by the benchmark, naturally achieving stronger binding affinities
towards the same pockets but limiting their ability to cover the broader target-specific chemical
space required for dynamic binding in real-world scenarios. In contrast, CtrlMol decouples pocket
and molecular conditions as independent guidance with arbitrary-count retrieval, naturally favoring
7

## B-c327d96f1724c4

candidate openreview-6EN1A4ESWH PDF page 21

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
•DrugFlow-PA:DrugFlow-PA is an optimized variant of DrugFlow using preference alignment
or property-oriented optimization. It is designed to steer the DrugFlow generation process
toward more favorable molecular properties or binding-related objectives.
•MolPilot:MolPilot is an optimization-based structure-based molecular generation method
built upon MolCraft. It introduces a modality-specific optimal schedule to guide molecular
generation.
•REINVENT:REINVENT is a reinforcement-learning-based molecular generation framework.
It is a non-3D model that optimizes generated molecules toward predefined reward functions.
FAIRCOMPARISONPROTOCOL
For all baselines, we follow the TarPass evaluation protocol to ensure consistent and fair compar-
ison. Whenever available, we use the official model checkpoints, default hyperparameters, and
recommended sampling settings. All generated molecules are processed using the same validation,
canonicalization, deduplication, docking, and evaluation workflow as CtrlMol.
B.4 IMPLEMENTATIONDETAILS
Main implementations.We trained CtrlMol using the AdamW optimizer with learning rate 1e-4
and batch size 64. To leverage our proposed on-the-fly conformer generation, we randomly sampled
10,000 molecules per epoch and trained for∼12,000epochs. The diffusion process used 1,000
steps with cosine noise schedule. We adopted ECFP for molecular condition encoder and DrugCLIP
for pocket condition encoder. We set dual-axis CFG dropout rates 0.2, slightly higher than standard
single-axis CFG, to balance four possible condition combinations. We implemented CtrlMol using
PyTorch. Training took∼72hours on a single H100 GPU with more than 40 GB of memory.
Model architecture.The model totally contains 8.6 M trainable parameters. The architecture
consists of input projection layers that encode atomic coordinates, atom types, bond types, and
timestep information into 64-dimensional embeddings. Conditions are integrated via proposed
ACCE, SACM, and IDA-CFG to modulate the embeddings. The modulated features are then pro-
cessed by an SE(3)-equivariant GotenNet backbone with 1 attention layer, 8 heads, and 64 hidden
dimensions. The maximum SE(3) degree is set to 2. Output projection layers decode the backbone
features into predicted coordinates, atom type distributions, and bond type distributions.
On-the-fly conformer generation.For each epoch, we used RDKit’s ETKDG algorithm to gen-
erate a single 3D conformer for each randomly sampled molecule, followed by MMFF94s optimiza-
tion with maximum 200 iterations.
Generation validation.Generated molecules with any atomic coordinate outside [-16, 16] ˚A
are considered invalid and discarded. Valid molecules are further filtered by MMFF94s energy Z-
score within [-3, 3], and chemical filter catalogs including PAINS A, NIH, and ZINC. MMFF94s
optimization uses a maximum of 1,000 iterations with convergence required.
21

## B-c6d8c29f475285

candidate openreview-6EN1A4ESWH PDF page 16

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
APPENDIX
A METHODDETAILS
A.1 CONTINUOUSDIFFUSION FORCOORDINATES
Coordinates are diffused with a continuous Gaussian process (Ho et al., 2020). The forward process
follows
Xt = √¯αtX0 +
√
1−¯αtϵ, ϵ∼ N(0, I),
where¯αt follows a cosine schedule (Nichol & Dhariwal, 2021):
¯αt = f(t)
f(0) , f(t) = cos 2
(︃t+s
1 +s · π
2
)︃
,
with offsets= 0.008andt∈[0,1]. The reverse process iteratively denoises from noise back to
structured coordinates:
Xt−1 = 1√αt
(︂
Xt − βt√1−¯αt
ϵθ(Xt, t)
)︂
+σ tz, z∼ N(0, I),
with posterior varianceσ 2
t =β t
1−¯αt−1
1−¯αt
, whereα t = ¯αt/¯αt−1,β t = 1−α t, andϵ θ(Xt, t)is a
learned noise predictor. Sampling starts fromX 1 ∼ N(0, I)and iteratively denoises toX 0.
Before diffusion, coordinates are centered at the origin to remove translational degrees of freedom.
The denoising networkϵ θ(Xt, t)is built on GotenNet (Aykent & Xia, 2025), a SE(3)-equivariant
GNN backbone, with time steptencoded via sinusoidal positional embeddings (Vaswani et al.,
2023). Training minimizes the noise-prediction mean squared error
LX =E t,X0,ϵ
⃦⃦ϵ−ϵ θ(Xt, t)
⃦⃦2
.
A.2 DISCRETEDIFFUSION FORATOM ANDBONDTYPES
The forward process follows a categorical transition (Hoogeboom et al., 2021) that introduces uni-
form noise with probabilityβ t,
q(ct |c t−1) =C(c t |(1−β t), ct−1 +β t/K),
whereCdenotes a categorical distribution andKis the number of classes as described in Section 3.3.
The forward marginal fromc 0 toc t follows
q(ct |c 0) =C(c t |¯αt c0 + (1−¯αt)/K),
whereα t = 1−β t and¯αt = ∏︁t
τ=1 ατ .
The reverse process is characterized by the categorical posterior in closed form
q(ct−1 |c t, c0) =C(c t−1 |θ post(ct, c0)), θ post(ct, c0) =
˜θ∑︁K
k=1
˜θk
,
˜θ= [α tct + (1−α t)/K]⊙[¯αt−1c0 + (1−¯αt−1)/K].
The denoising network predicts the clean probability distributionˆc0 =µ θ(ct, t)via a softmax out-
put, and the reverse process is parametrized as
pθ(ct−1 |c t) =C(c t−1 |θ post(ct,ˆc0)).
Training minimizes the KL divergence between the true posterior and the predicted posterior:
Lc =E t,c0 KL
[︁
q(ct−1 |c t, c0)∥p θ(ct−1 |c t)
]︁
, c∈ {A, B},
yieldingL A for atom types andL B for bond types. The three diffusion channels are jointly opti-
mized under a hybrid lossL=L X +L A +L B.
16

## B-c70036716b381a

candidate openreview-6EN1A4ESWH PDF page 23

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
B.7 CHEMICALSPACE
We analyzed the distribution of generated molecules in chemical space across for each of the exper-
iments. Three representative distributions are selected for presentation.
Figure 4:Generated, reference and random molecules in chemical space.Generated, reference
and random molecules are scattered in red, blue and light gray, respectively. (A) unconditional
generated distribution corresponds toK= 0, L= 0in Table 2. (B) overfocused generated distri-
bution corresponds toK= 1, L= 0in Table 2. (C) optimal generated distribution corresponds to
gM = 2, gP = 1in Table 3.
B.8 DRUGCANDIDATES
We ultimately screened out several ADRB2 drug candidates from the molecules generated by Ctrl-
Mol.
Figure 5:CtrlMol-designed ADRB2 drug candidates.The top-10 generated molecules with high
binding affinity correspond tog M = 2, gP = 1in Table 3.
23

## B-c76f1c1c1ccfd0

candidate openreview-6EN1A4ESWH PDF page 22

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
B.5 TARGETSPECIFICITY
We evaluated FCD between every pair of 18 targets and random to verify target specificity. The
diagonal elements represent self-comparisons within the same target, where lower FCD values in-
dicate better target-specificity or target-awareness. Their non-random average corresponds to the
Wass. Ref in Table 1. The random-random element corresponds to the minimum FCD achiev-
able for a 1,000-molecule set mentioned in Section 4.3. The off-diagonal elements represent cross-
target comparisons, where higher FCD values indicate better target-specificity. The targets comprise
5-HT2A, BCL2,β2AR, BRAF, BRD4, BTK, DRD2, HDAC6, JAK2, MEK1, NAMPT, NQO1,
PI3Kα, PPARα, PRMT5, RARα, ROCK1, and TYK2.
Figure 2:FCD matrix highlighting target-specific evaluation across 18 targets.The X-axis and
Y-axis denote the reference molecules and the generated molecules across 18 targets and random
background, respectively.
B.6 MOLECULARDESCRIPTORS
We evaluated the property similarity of the generated molecules to the reference molecules using 15
representative molecular descriptors. The average of these 15 descriptors corresponds to Wass. Ref
and Wass. Shift in Table 1.
Figure 3:Wasserstein distances of 15 molecular properties across CtrlMol and baselines.
22

## B-caddb127f75be4

candidate openreview-6EN1A4ESWH PDF page 17

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
B EXPERIMENTALDETAILS
B.1 DATACURATION
All datasets were processed in a consistent manner. We performed comprehensive molecular data
curation to construct the training dataset. Starting from raw SMILES strings in source databases,
we first standardized molecular representations to obtain consistent canonical forms, then applied
strict drug-likeness criteria to extract high-quality molecules that improved training stability and
generalization.
Molecular Standardization.We preprocessed raw SMILES to ensure consistent representations
for reliable filtering and deduplication:
• Extracted parent molecules using ChEMBL Structure Pipeline (Bento et al., 2020) with neu-
tralization
• Adjusted protonation states to pH 7.4 using Open Babel (O’Boyle et al., 2011)
• Generated canonical SMILES with stereochemistry preserved
Composition Constraints.We enforced element composition and ring topology requirements to
ensure chemically reasonable structures:
• Allowed elements: C, N, O, S, P, H, F, Cl, Br, I
• Number of heavy atoms: 10–50
• Number of rings:≤5(aromatic≤5, aliphatic≤2)
• No 3- or 4-membered rings (small rings)
• No rings larger than 6-membered (big rings)
Physicochemical Properties.We applied extended drug-likeness criteria to ensure favorable
ADME profiles:
• Hydrogen bond donors:≤6
• Hydrogen bond acceptors:≤10
• Rotatable bonds:≤11
• TPSA: 20–140 ˚A
2
• LogP: -5 to 6
• Structural alerts:≤2(Bickerton et al., 2012)
• Chiral centers:≤5
Quality Metrics.We filtered by computational assessments of drug-likeness and synthetic acces-
sibility:
• QED (Quantitative Estimate of Drug-likeness):≥0.28
• SA Score (Synthetic Accessibility):<6
Substructure Filters.We removed molecules containing problematic substructures or functional
groups:
• Passed PAINS A filter (pan-assay interference compounds) (Baell & Holloway, 2010)
• Passed NIH filter (reactive/promiscuous compounds) (Jadhav et al., 2010)
• Passed ZINC filter (biologically implausible structures) (Tingle et al., 2023)
All filtering criteria were computed using RDKit molecular descriptors and filter catalogs. After
filtering and deduplication by canonical SMILES, for ChEMBL as an example, we obtained ap-
proximately 1.4 M high-quality drug-like molecules from 2.8 M initial entries for training.
17

## B-dbe247feeb9965

candidate openreview-6EN1A4ESWH PDF page 12

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
Zhilin Huang, Ling Yang, Xiangxin Zhou, Chujun Qin, Yijie Yu, Xiawu Zheng, Zikun Zhou,
Wentao Zhang, Yu Wang, and Wenming Yang. Interaction-based retrieval-augmented diffu-
sion models for protein-specific 3D molecule generation. In Ruslan Salakhutdinov, Zico Kolter,
Katherine Heller, Adrian Weller, Nuria Oliver, Jonathan Scarlett, and Felix Berkenkamp (eds.),
Proceedings of the 41st International Conference on Machine Learning, volume 235 ofPro-
ceedings of Machine Learning Research, pp. 20348–20364. PMLR, 21–27 Jul 2024. URL
https://proceedings.mlr.press/v235/huang24ab.html.
Clemens Isert, Kenneth Atz, and Gisbert Schneider. Structure-based drug design with geometric
deep learning.Current Opinion in Structural Biology, 79:102548, 2023. ISSN 0959-440X.
doi: https://doi.org/10.1016/j.sbi.2023.102548. URLhttps://www.sciencedirect.
com/science/article/pii/S0959440X23000222.
Ajit Jadhav, Rafaela S. Ferreira, Carleen Klumpp, Bryan T. Mott, Christopher P. Austin, James In-
glese, Craig J. Thomas, David J. Maloney, Brian K. Shoichet, and Anton Simeonov. Quantitative
analyses of aggregation, autofluorescence, and reactivity artifacts in a screen for inhibitors of a
thiol protease.Journal of Medicinal Chemistry, 53(1):37–51, 01 2010. ISSN 0022-2623. doi:
10.1021/jm901070c. URLhttps://doi.org/10.1021/jm901070c.
Xiaohong Ji, Zhen Wang, Zhifeng Gao, Hang Zheng, Linfeng Zhang, Guolin Ke, and Weinan E.
Exploring molecular pretraining model at scale. In A. Globerson, L. Mackey, D. Belgrave,
A. Fan, U. Paquet, J. Tomczak, and C. Zhang (eds.),Advances in Neural Information Pro-
cessing Systems, volume 37, pp. 46956–46978. Curran Associates, Inc., 2024. doi: 10.52202/
079017-1489. URLhttps://proceedings.neurips.cc/paper_files/paper/
2024/file/53923bb44655a7defb31c7744c01b62b-Paper-Conference.pdf.
Yinjun Jia, Bowen Gao, Jiaxin Tan, Jiqing Zheng, Xin Hong, Wenyu Zhu, Haichuan Tan, Yuan
Xiao, Liping Tan, Hongyi Cai, Yanwen Huang, Zhiheng Deng, Xiangwei Wu, Yue Jin, Yafei
Yuan, Jiekang Tian, Wei He, Weiying Ma, Yaqin Zhang, Lei Liu, Chuangye Yan, Wei Zhang,
and Yanyan Lan. Deep contrastive learning enables genome-wide virtual screening.Science, 391
(6781):eads9530, 2026. doi: 10.1126/science.ads9530. URLhttps://www.science.org/
doi/abs/10.1126/science.ads9530.
Nandan Joshi and Erhan Guven. Improved molecular generation through attribute-driven integrative
embeddings and gan selectivity. In2025 IEEE Conference on Artificial Intelligence (CAI), pp.
463–468, 2025. doi: 10.1109/CAI64502.2025.00085.
Sunghwan Kim, Jie Chen, Tiejun Cheng, Asta Gindulyte, Jia He, Siqian He, Qingliang Li, Ben-
jamin A Shoemaker, Paul A Thiessen, Bo Yu, Leonid Zaslavsky, Jian Zhang, and Evan E Bolton.
Pubchem 2025 update.Nucleic Acids Research, 53(D1):D1516–D1525, 01 2025. ISSN 1362-
4962. doi: 10.1093/nar/gkae1059. URLhttps://doi.org/10.1093/nar/gkae1059.
Craig Knox, Mike Wilson, Christen M Klinger, Mark Franklin, Eponine Oler, Alex Wilson, Allison
Pon, Jordan Cox, Na Eun (Lucy) Chin, Seth A Strawbridge, Marysol Garcia-Patino, Ray Kruger,
Aadhavya Sivakumaran, Selena Sanford, Rahil Doshi, Nitya Khetarpal, Omolola Fatokun, Daph-
nee Doucet, Ashley Zubkowski, Dorsa Yahya Rayat, Hayley Jackson, Karxena Harford, Afia
Anjum, Mahi Zakir, Fei Wang, Siyang Tian, Brian Lee, Jaanus Liigand, Harrison Peters, Ruo
Qi (Rachel) Wang, Tue Nguyen, Denise So, Matthew Sharp, Rodolfo da Silva, Cyrella Gabriel,
Joshua Scantlebury, Marissa Jasinski, David Ackerman, Timothy Jewison, Tanvir Sajed, Vasuk
Gautam, and David S Wishart. Drugbank 6.0: the drugbank knowledgebase for 2024.Nucleic
Acids Research, 52(D1):D1265–D1275, 2024. ISSN 0305-1048. doi: 10.1093/nar/gkad976. URL
https://doi.org/10.1093/nar/gkad976.
Greg Landrum, Paolo Tosco, Brian Kelley, et al. Rdkit: Open-source cheminformatics.
Tianxiao Li, Haoran Liu, Hongyu Guo, Mark Gerstein, and Martin Renqiang Min. Disentangled
autoencoding equivariant diffusion model for controlled generation of 3d molecules. 17(1):4824,
2026. ISSN 2041-1723. doi: 10.1038/s41467-026-71441-9. URLhttps://doi.org/10.
1038/s41467-026-71441-9.
Yi-Lun Liao, Alexander J. Hoffman, Sabrina C. Shen, Alexandre Duval, Sam Walton Norwood,
and Tess Smidt. Equiformerv3: Scaling efficient, expressive, and general se(3)-equivariant graph
attention transformers, 2026. URLhttps://arxiv.org/abs/2604.09130.
12

## B-e6634bd1a06ea6

candidate openreview-6EN1A4ESWH PDF page 1

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
CTRLMOL: CONTROLLABLEMOLECULARGENERA-
TION FORDRUGDESIGN VIAFLEXIBLECONDITION-
ADAPTIVEDIFFUSION
Anonymous authors
Paper under double-blind review
ABSTRACT
Conditional molecular generation is critical for drug design, where generated
molecules need to satisfy varying design requirements. However, existing molec-
ular generation methods lack flexibility in handling diverse reference conditions
and controllability in adjusting generation toward desired molecular profiles, lim-
iting their ability to meet some customized requirements. To address these lim-
itations, we propose CtrlMol, a novel controllable molecular generation frame-
work via flexible condition-adaptive diffusion model. CtrlMol achieves flexibility
through Arbitrary-Count Condition Encoding that accommodates zero or more re-
trieved molecular and pocket conditions, followed by Self-Adaptive Modulation
aggregating them into the denoising process in a unified manner. CtrlMol also
achieves controllability through Independent Dual-Axis Classifier-Free Guidance
that separately adjusts the guidance strengths of molecular and pocket conditions
during inference, allowing controllable generation trade-offs between precision
and diversity. Experiments on the TarPass benchmark demonstrate that CtrlMol
consistently outperforms competing methods, achieving 28.8% improvement in
target specificity and superior molecular property control. Case studies on a car-
diovascular target ADRB2 further validate that the flexibility and controllability
jointly enable effective adjustment of the generation distribution.
1 INTRODUCTION
Molecular generation is a central task in drug design, aiming to discover candidate compounds with
desired properties and biological activities (Sun et al., 2025). In recent years, deep learning-based
conditional molecular generation methods have significantly accelerated this process by encoding
specific design requirements into conditional signals that guide generation (Sousa et al., 2021; Du
et al., 2024). In practical drug discovery, two types of prior knowledge as conditions are particularly
valuable. Known active ligands provide desired molecular property profiles and support ligand-
based drug design (L ´opez-L´opez et al., 2026), while known binding pockets from protein-ligand
complexes provide binding interaction information and support structure-based drug design (Pala &
Clark, 2024). Integrating both conditions is essential for generating molecules with desired proper-
ties and target specificity.
However, in real-world scenarios, the types and counts of available conditions often vary depending
on the design requirements or data availability. Consequently, an ideal molecular generation system
should flexibly adapt to different condition configurations and provide control over the generation
process during inference. In practice, when faced with a new drug design task, researchers gener-
ally begin by retrieving relevant known active ligands and target binding pocket information from
databases, using them as reference conditions to guide the generation of novel molecules. However,
the counts of retrieved reference ligands and target pockets are uncertain or even absent, and the two
types of conditions are often unrelated or unpaired. Existing conditional molecular generation meth-
ods, whether accepting ligands (Li et al., 2026), pockets (Guan et al., 2023), or paired ligand-pocket
complexes (Cremer et al., 2026) as conditions, are typically designed to accept fixed types and fixed
counts of condition inputs, making it difficult to directly adapt to such variability in the types and
counts of condition configurations in real-world retrieval scenarios.
1
Reviewers:pleasereadtheReviewerGuidelines(iclr.cc/Conferences/2027/ReviewerGuidelines)andtheAIPolicyforReviewers(iclr.cc/Conferences/2027/AIPolicyForReviewers).
If you used AI to expand, edit, or polish your review, please provide the input text to the LLM. Better still, consider skipping the LLM and submitting your original text: we,
and the authors, are much more interested in your unedited thoughts than in what an LLM has to say. AI-assisted or not, you are putting your name and reputation behind
your review: LLM-generated falsehoods, hallucinations or misrepresentations are subject to disciplinary action, which may include desk-rejecting all papers you have authored.

## B-fc9f596f26c62b

candidate openreview-6EN1A4ESWH PDF page 14

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
13(40):e75411, 2026. doi: https://doi.org/10.1002/advs.75411. URLhttps://advanced.
onlinelibrary.wiley.com/doi/abs/10.1002/advs.75411.
David Rogers and Mathew Hahn. Extended-connectivity fingerprints.Journal of Chemical Infor-
mation and Modeling, 50(5):742–754, 05 2010. ISSN 1549-9596. doi: 10.1021/ci100050t. URL
https://doi.org/10.1021/ci100050t.
Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Bj ¨orn Ommer. High-
resolution image synthesis with latent diffusion models. InProceedings of the IEEE/CVF Con-
ference on Computer Vision and Pattern Recognition (CVPR), pp. 10684–10695, June 2022.
Daniel M. Rosenbaum, Vadim Cherezov, Michael A. Hanson, Søren G. F. Rasmussen, Foon Sun
Thian, Tong Sun Kobilka, Hee-Jung Choi, Xiao-Jie Yao, William I. Weis, Raymond C.
Stevens, and Brian K. Kobilka. GPCR engineering yields high-resolution structural insights
intoβ 2-adrenergic receptor function.Science, 318(5854):1266–1273, 2007. doi: 10.1126/
science.1150609. URLhttps://www.science.org/doi/abs/10.1126/science.
1150609.
Chitwan Saharia, Jonathan Ho, William Chan, Tim Salimans, David J. Fleet, and Mohammad
Norouzi. Image super-resolution via iterative refinement.IEEE Trans. Pattern Anal. Mach. In-
tell., 45(4):4713–4726, April 2023. ISSN 0162-8828. doi: 10.1109/TPAMI.2022.3204461. URL
https://doi.org/10.1109/TPAMI.2022.3204461.
Jacob Schnell, Aditya Makkar, Gunadi Gani, Aniket Srinivasan Ashok, Darren Lo, Mike Optis,
Alexander Wong, and Yuhao Chen. Composite classifier-free guidance for multi-modal condi-
tioning in wind dynamics super-resolution, 2025. URLhttps://arxiv.org/abs/2512.
13729.
Tiago Sousa, Jo ˜ao Correia, and Miguel Pereira, V ´ıtorand Rocha. Generative deep learning for
targeted compound design.Journal of Chemical Information and Modeling, 61(11):5343–5361,
11 2021. ISSN 1549-9596. doi: 10.1021/acs.jcim.0c01496. URLhttps://doi.org/10.
1021/acs.jcim.0c01496.
Qun Su, Qiaolin Gou, Hui Zhang, Jike Wang, Huiyong Sun, Renling Hu, Rui Qin, Huanxiang Liu,
Tingjun Hou, and Yu Kang. LaMGen: LLM-based 3D molecular generation for multi-target
drug design.Nature Communications, 17(1):5091, April 2026. ISSN 2041-1723. doi: 10.1038/
s41467-026-71737-w. URLhttps://doi.org/10.1038/s41467-026-71737-w.
Yan Sun, Lianghong Chen, Zihao Jing, Yan Yi Li, Dongkyu Kim, Jing-Yan Gao, Reza Noroozi,
Grace Y . Yi, Conrard Giresse Tetsassi Feugmo, Anna Klinkova, Kyla Sask, Agustinus Kristiadi,
Boyu Wang, Elizabeth R. Gillies, Kun Ping Lu, HaoTian Harvey Shi, and Pingzhao Hu. Gener-
ative ai for the design of molecules: Advances and challenges.Journal of Chemical Information
and Modeling, 65(23):12668–12690, 12 2025. ISSN 1549-9596. doi: 10.1021/acs.jcim.5c02234.
URLhttps://doi.org/10.1021/acs.jcim.5c02234.
Benjamin I. Tingle, Khanh G. Tang, Mar Castanon, John J. Gutierrez, Munkhzul Khurelbaatar,
Chinzorig Dandarchuluun, Yurii S. Moroz, and John J. Irwin. ZINC-22: A free multi-billion-
scale database of tangible compounds for ligand discovery.Journal of Chemical Information and
Modeling, 63(4):1166–1176, 02 2023. ISSN 1549-9596. doi: 10.1021/acs.jcim.2c01253. URL
https://doi.org/10.1021/acs.jcim.2c01253.
Atabey ¨Unl¨u, Elif C ¸ evrim, Melih G¨okay Yi˘git, Ahmet Sarıg¨un, Hayriye C ¸ elikbilek, Osman Bayram,
Deniz Cansen Kahraman, Abdurrahman Ol ˘gac ¸, Ahmet Sureyya Rifaioglu, Erden Bano ˘glu,
and Tunca Do ˘gan. Target-specific de novo design of drug candidate molecules with graph-
transformer-based generative adversarial networks.Nature Machine Intelligence, 7(9):1524–
1540, Sep 2025. ISSN 2522-5839. doi: 10.1038/s42256-025-01082-y. URLhttps://doi.
org/10.1038/s42256-025-01082-y.
Mihaly Varadi, Stephen Anyango, Mandar Deshpande, et al. AlphaFold protein structure database:
massively expanding the structural coverage of protein-sequence space with high-accuracy mod-
els.Nucleic Acids Research, 50(D1):D439–D444, 2022. doi: 10.1093/nar/gkab1061.
14
