# SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks

## B-ocr-00db9b7d3893d1

B PDF page 1

arXiv:2602.12670v4 [cs.AI] 14 Jun 2026

# SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks

Xiangyi Li \( ^{1,*} \) , Yimin Liu \( ^{1,2,*} \) , Wenbo Chen \( ^{3,*} \) , Bingran You \( ^{1,4,*} \) , Zonglin Di \( ^{5,1} \) , Yifeng He \( ^{6,1} \) , Shenghan Zheng \( ^{7,1} \) , Kyoung Whan Choe \( ^{8,1} \) , Jiankai Sun \( ^{9,1} \) , Shuyi Wang \( ^{9,1} \) , Chujun Tao \( ^{14,1} \) , Binxu Li \( ^{10,1} \) , Xuandong Zhao \( ^{4,1} \) , Hejia Geng \( ^{11} \) , Xiaojun Wu \( ^{35} \) , Junwei Zhou \( ^{9} \) , Xiaokun Chen \( ^{12} \) , Hanwen Xing \( ^{13} \) , Yubo Li \( ^{14} \) , Qunhong Zeng \( ^{9} \) , Di Wang \( ^{15} \) , Yuanli Wang \( ^{16} \) , Roey Ben Chaim \( ^{17} \) , Penghao Jiang \( ^{18} \) , Haotian Shen \( ^{9} \) , Luyang Kong \( ^{9} \) , Xinyi Liu \( ^{9} \) , Runhui Wang \( ^{9} \) , Xuanqing Liu \( ^{9} \) , Jiachen Li \( ^{19} \) , Xin Lan \( ^{20} \) , Yueqian Lin \( ^{21} \) , Wengao Ye \( ^{11} \) , Junwei He \( ^{22} \) , Songlin Li \( ^{12} \) , Yue Zhang \( ^{23} \) , Yipeng Gao \( ^{13} \) , Yijiang Li \( ^{24} \) , Ze Ma \( ^{25} \) , Liqiang Jing \( ^{23} \) , Tianyu Wang \( ^{9} \) , Kaixin Li \( ^{9} \) , Yiqi Xue \( ^{13} \) , Haoran Lyu \( ^{9} \) , Yizhuo He \( ^{14} \) , Yuchen Tian \( ^{9} \) , Shutong Wu \( ^{26} \) , Bowei Wang \( ^{9} \) , Yixuan Gao \( ^{27} \) , Bo Chen \( ^{9} \) , Litong Liu \( ^{28} \) , Sikai Cheng \( ^{28} \) , Jiajun Bao \( ^{14} \) , Shuaicheng Tong \( ^{28} \) , Shuwen Xu \( ^{9} \) , Terry Yue Zhuo \( ^{9} \) , Tinghan Ye \( ^{28} \) , Qi Qi \( ^{9} \) , Miao Li \( ^{28} \) , Longtai Liao \( ^{9} \) , Zelin Tan \( ^{34} \) , Chang Shi \( ^{19} \) , Xilin Tang \( ^{29} \) , Srinath Tankasala \( ^{3,1} \) , Boqin Yuan \( ^{24} \) , Yaoyao Qian \( ^{30} \) , Jianhong Tu \( ^{5} \) , Chenguang Wang \( ^{5} \) , Yizhou Sun \( ^{31} \) , Wei Wang \( ^{31} \) , Aaron Taylor \( ^{33} \) , Ziyue Yang \( ^{6} \) , Changkun Guan \( ^{28} \) , Zhikang Dong \( ^{32} \) , Xinyu Zhang \( ^{36} \) , Steven Dillmann \( ^{12} \) , Han-chung Lee \( ^{9} \) , Dawn Song \( ^{4} \)

## Abstract

Agent Skills are structured packages of procedural knowledge that augment large language model (LLM) agents at inference time. Despite rapid adoption, there is no standard way to measure whether they actually help. We present SKILLSBENCH, a benchmark whose current inventory contains 87 tasks across 8 domains paired with curated Skills and deterministic verifiers. Our latest aggregate evaluation runs the 87-task benchmark under matched no-Skills and curated-Skills conditions for 18 model–harness configurations. Curated Skills raise the average pass rate from 33.9% to 50.5% (+16.6 percentage points; 25.5% normalized gain), with configuration-level gains ranging from +4.1 to +25.7 pp. Focused Skills with at most three modules outperform larger or exhaustive bundles, and smaller models with Skills can match larger models without them. SKILLSBENCH establishes paired evaluation as the foundation for rigorous measurement of Skill efficacy on agentic, expertise-heavy work.

![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

Figure 1: Agent architecture stack and resolution rates across 18 model–harness configurations on 87 SkillsBench tasks. Each bar stacks the no-Skills baseline and curated-Skills lift; open/filled interval markers denote 95% CIs for the baseline/total. Bars are ordered by Curated-Skills pass rate and colored by model family. Harness abbreviations: OH = OpenHands, CC = Claude Code, GCLI = Gemini CLI.
