# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_sAQsTTaaqjOV` — Near Duplicate Finder
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-03 20:02:41 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: 'Rateless MinHash: Progressive Jaccard Estimation via Fountain Codes'
abstract: >-
  MinHash and its variants require fixing the sketch size (number of hash functions) upfront, before knowing the desired estimation
  accuracy or the distribution of Jaccard similarities in the dataset. This leads to either wasted space (oversized sketches)
  or insufficient accuracy (undersized sketches). We propose Rateless MinHash, a novel sketching approach that applies fountain
  code principles to MinHash, enabling progressive Jaccard similarity estimation where hash values are generated on-demand.
  Inspired by LT codes, our method generates a potentially infinite sequence of coded hash values using a minimum-based aggregation
  over randomly selected base hashes. Evaluation on synthetic and real-world text datasets shows that: (1) Rateless MinHash
  enables progressive estimation with 55-80% reduction in mean squared error (MSE) when processing 128 hash values compared
  to using only 10; (2) adaptive stopping reduces average space usage to ~853 bits compared to fixed 1024+ bits for standard
  MinHash at comparable accuracy levels; (3) the method introduces dependencies between hash positions, resulting in 1.01-1.93x
  higher MSE than independent hashes at equal bit budgets. We provide a formal theoretical analysis explaining this efficiency
  penalty: the ratio equals 1 + d²/k² where d is the degree and k is the number of base hashes, verified through Lean 4 proofs.
  While simple adaptive baselines (sequentially adding independent MinHash values) can achieve similar space-accuracy trade-offs,
  Rateless MinHash provides a principled framework for progressive estimation with analyzable dependency structure.
paper_text: "# Rateless MinHash: Progressive Jaccard Estimation via Fountain Codes\n\n## Abstract\n\nMinHash and its variants\
  \ require fixing the sketch size (number of hash functions) upfront, before knowing the desired estimation accuracy or the\
  \ distribution of Jaccard similarities in the dataset. This leads to either wasted space (oversized sketches) or insufficient\
  \ accuracy (undersized sketches). We propose **Rateless MinHash**, a novel sketching approach that applies fountain code\
  \ principles to MinHash, enabling progressive Jaccard similarity estimation where hash values are generated on-demand. Inspired\
  \ by LT codes, our method generates a potentially infinite sequence of coded hash values using a minimum-based aggregation\
  \ over randomly selected base hashes. Evaluation on synthetic and real-world text datasets shows that: (1) Rateless MinHash\
  \ enables progressive estimation with 55-80% reduction in mean squared error (MSE) when processing 128 hash values compared\
  \ to using only 10; (2) adaptive stopping reduces average space usage to ~853 bits compared to fixed 1024+ bits for standard\
  \ MinHash at comparable accuracy levels; (3) the method introduces dependencies between hash positions, resulting in 1.01-1.93x\
  \ higher MSE than independent hashes at equal bit budgets. We provide a formal theoretical analysis explaining this efficiency\
  \ penalty: the ratio equals 1 + d²/k² where d is the degree and k is the number of base hashes, verified through Lean 4\
  \ proofs. While simple adaptive baselines (sequentially adding independent MinHash values) can achieve similar space-accuracy\
  \ trade-offs, Rateless MinHash provides a principled framework for progressive estimation with analyzable dependency structure.\n\
  \n**Keywords**: MinHash, Jaccard similarity, fountain codes, rateless codes, progressive estimation, sketching algorithms\n\
  \n## 1 Introduction\n\nEstimating Jaccard similarity between sets is a fundamental operation in computer science, with applications\
  \ in near-duplicate detection, clustering, recommendation systems, and graph analysis. Given two sets A and B, their Jaccard\
  \ similarity is defined as J(A,B) = |A∩B| / |A∪B|, ranging from 0 (disjoint sets) to 1 (identical sets).\n\n**The Problem**:\
  \ MinHash, introduced by Broder [1], estimates Jaccard similarity by computing the probability that the minimum hash value\
  \ under a random permutation is the same for both sets. The standard approach uses k independent hash functions, producing\
  \ a sketch of size k. The variance of the estimator is Var[Ĵ] = J(1-J)/k, so the mean squared error (MSE) decreases as\
  \ O(1/k) [1].\n\nThe critical limitation is that **the sketch size k must be fixed upfront**, before seeing the data. This\
  \ creates a fundamental trade-off:\n- If k is too small, the estimation error may be unacceptably high for the actual Jaccard\
  \ similarities in the dataset.\n- If k is too large, space is wasted, especially for sets with high Jaccard similarity where\
  \ fewer hash functions suffice.\n\nThis problem is exacerbated in practice: datasets often have diverse Jaccard similarity\
  \ distributions, and the optimal sketch size is data-dependent and unknown beforehand. Applications like distributed deduplication\
  \ and streaming data would benefit from a sketch that can be refined progressively, using more space only when needed.\n\
  \n**Prior Solutions and Their Limitations**: Several MinHash variants attempt to address space efficiency, but all require\
  \ fixed sketch sizes:\n- **b-bit MinHash** [4] reduces storage by storing only the b lowest bits of each hash value, but\
  \ the compression is lossy and irreversible.\n- **SetSketch** [6] bridges MinHash and HyperLogLog with configurable parameters,\
  \ but these parameters must be set before sketch construction.\n- **Odd Sketch** [7] optimizes for high Jaccard similarities\
  \ using binary sketches, but the sketch size must be fixed upfront.\n- **ProbMinHash** [8] extends to weighted Jaccard similarity\
  \ but produces fixed-size signatures.\n\n**Our Approach**: We introduce **Rateless MinHash**, which applies fountain code\
  \ principles to MinHash. Fountain codes (LT codes [9], Raptor codes [10]) are rateless erasure codes that can generate an\
  \ infinite sequence of encoded symbols from a source message. The receiver can recover the original message after receiving\
  \ any slightly larger set of encoded symbols.\n\nThe key insight is that MinHash sketches can be viewed as encoded representations\
  \ of sets, and by using coding-theoretic principles, we can make this encoding rateless. Our method:\n1. Generates a sequence\
  \ of coded hash values using a degree distribution inspired by LT codes\n2. Uses minimum operation over selected base hashes\
  \ (preserving the MinHash property)\n3. Enables progressive estimation: accuracy improves as more values are processed\n\
  4. Supports adaptive stopping: estimation can stop when sufficient accuracy is reached\n\n**Key Theoretical Contribution**:\
  \ Unlike standard MinHash which uses independent hash functions, Rateless MinHash introduces dependencies between coded\
  \ hash values through the coding process. We provide a formal theoretical analysis of these dependencies, deriving the exact\
  \ covariance structure. The analysis shows that the MSE ratio between Rateless MinHash and independent MinHash equals 1\
  \ + d²/k², where d is the degree and k is the number of base hashes. This result is verified through Lean 4 formal proofs\
  \ \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-2e68d8-rateless-minhash-progressive-jaccard-est/tree/main/round-2/proof-1}}.\n\
  \n**Contributions**:\n\n1. **Novel Algorithm**: We present the first rateless MinHash algorithm that generates hash values\
  \ on-demand using fountain code principles \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-2e68d8-rateless-minhash-progressive-jaccard-est/tree/main/round-1/experiment-1}}.\n\
  \n2. **Theoretical Analysis**: We derive the covariance structure of Rateless MinHash, proving that E[π_i π_j] = J² + O(d²/k²)\
  \ and the MSE penalty equals 1 + d²/k², verified through formal Lean 4 proofs .\n\n3. **Progressive Estimation**: We demonstrate\
  \ that Jaccard similarity can be estimated progressively, with 55-80% reduction in MSE when processing 128 hash values compared\
  \ to using only 10 .\n\n4. **Adaptive Space Efficiency**: We show that Rateless MinHash with adaptive stopping uses ~853\
  \ bits on average (±148), compared to fixed 1024+ bits for standard MinHash with equivalent accuracy .\n\n5. **Honest Baseline\
  \ Comparison**: We compare against simple adaptive baselines (sequentially adding independent MinHash values) and analyze\
  \ when the fountain code complexity is justified \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-2e68d8-rateless-minhash-progressive-jaccard-est/tree/main/round-2/experiment-1}}.\n\
  \nThe remainder of this paper is organized as follows. Section 2 reviews related work. Section 3 describes the Rateless\
  \ MinHash algorithm and provides theoretical analysis of the dependency structure. Section 4 presents the experimental evaluation\
  \ on synthetic and real-world datasets. Section 5 discusses limitations and future work. Section 6 concludes.\n\n[FIGURE:fig1]\n\
  \n## 2 Related Work\n\n### 2.1 MinHash and Its Variants\n\nMinHash was introduced by Broder [1] for estimating Jaccard similarity\
  \ between sets. The standard MinHash algorithm uses k independent random permutations and computes the minimum hash value\
  \ for each permutation. The Jaccard similarity is estimated as the fraction of matching minimum hash values.\n\n**b-bit\
  \ MinHash** [4] reduces the storage cost by storing only the b lowest bits of each minhash value. The variance of the b-bit\
  \ estimator is Var[Ĵ_b] = (1-J)/k · (J + 1/(2^b - 1)) [5]. While more space-efficient, the compression is lossy and the\
  \ sketch cannot be refined after creation.\n\n**SetSketch** [6] unifies MinHash and HyperLogLog into a single data structure\
  \ with configurable parameters (m, b, a, q) that must be set before sketch construction. It provides estimators for both\
  \ cardinality and Jaccard similarity but does not support progressive refinement.\n\n**Odd Sketch** [7] is optimized for\
  \ high Jaccard similarities using a binary sketch based on the parity (XOR) of hash values. The sketch size must be fixed\
  \ upfront, and the estimator's accuracy depends on the fraction of 1s being bounded away from 1/2.\n\n**ProbMinHash** [8]\
  \ extends MinHash to weighted Jaccard similarity, generating a fixed-size signature of k hash values.\n\n**One Permutation\
  \ MinHash** [14] reduces the number of hash computations needed but still requires fixing k beforehand.\n\n**Densified One\
  \ Permutation MinHash** [15] addresses the sparse sketch problem in one permutation MinHash by densifying the hash values.\n\
  \n### 2.2 Fountain Codes\n\nFountain codes are rateless erasure codes that can generate an infinite sequence of encoded\
  \ symbols. The receiver can recover the original message after receiving any slightly larger set of encoded symbols.\n\n\
  **LT Codes** [9] (Luby Transform) are the first practical fountain codes. Each encoding symbol is generated by: (1) choosing\
  \ a degree d from distribution ρ(d), (2) selecting d distinct input symbols uniformly at random, (3) XORing these d symbols.\
  \ The Robust Soliton distribution ensures successful decoding with high probability.\n\n**Raptor Codes** [10] improve upon\
  \ LT codes with linear-time encoding and decoding by applying a fixed-rate outer code before LT coding.\n\n### 2.3 Rate-Distortion\
  \ Theory\n\nRate-distortion theory [11, 12] studies the optimal trade-off between compression rate (bits per symbol) and\
  \ resulting distortion (loss) in lossy data compression. For a Bernoulli(p) source with Hamming distortion, the rate-distortion\
  \ function is R(D) = H_b(p) - H_b(D) for 0 ≤ D ≤ min(p, 1-p), where H_b is the binary entropy function.\n\nFor Jaccard similarity\
  \ estimation, the rate-distortion function has not been derived, though lower bounds exist from information complexity [3].\
  \ Any sketch must use Ω((1-J)/(εJ)²) bits per set for estimating Jaccard similarity with relative error εJ [3, Theorem 1.2].\n\
  \n### 2.4 Progressive Estimation and Adaptive Sketches\n\nProgressive estimation appears in sketching techniques for approximate\
  \ query processing [13], where initial estimates improve with more data. However, no existing MinHash implementation uses\
  \ a sequential stopping rule or enables progressive Jaccard estimation with analyzable dependency structure.\n\n**Weighted\
  \ MinHash** schemes [16] extend MinHash to weighted sets but do not address the progressive estimation problem.\n\n## 3\
  \ Methods\n\n### 3.1 Standard MinHash Background\n\nStandard MinHash estimates Jaccard similarity using k independent hash\
  \ functions. For each hash function h_i, the minimum hash value for set A is m_i(A) = min_{x∈A} h_i(x). The Jaccard similarity\
  \ is estimated as:\n\nĴ = (1/k) · Σ_{i=1}^k 1[m_i(A) = m_i(B)]\n\nwhere 1[·] is the indicator function. The estimator is\
  \ unbiased with variance Var[Ĵ] = J(1-J)/k.\n\n### 3.2 Rateless MinHash Algorithm\n\nOur Rateless MinHash algorithm adapts\
  \ fountain code principles to generate a potentially infinite sequence of hash values for progressive Jaccard estimation.\n\
  \n#### 3.2.1 Encoding\n\nGiven a set of elements, we first compute `num_base_hashes` base hash values using independent\
  \ hash functions. Then, we generate coded hash values using the following process:\n\n1. **Degree Sampling**: Sample a degree\
  \ d from the Robust Soliton distribution ρ(d) (adapted from LT codes [9]).\n2. **Element Selection**: Select d distinct\
  \ base hashes uniformly at random.\n3. **Coded Hash Generation**: Compute the coded hash value as the **minimum** of the\
  \ selected base hash values (not XOR as in LT codes). This preserves the MinHash property.\n\nThe choice of minimum operation\
  \ is critical: it ensures that Pr[min_{i∈I} h_i(A) = min_{i∈I} h_i(B)] = J(A,B) for any random subset I, preserving the\
  \ MinHash property. Alternative aggregation functions (mean, median, XOR) do not preserve this property .\n\nThe Robust\
  \ Soliton distribution is computed as:\n- τ(d) = R/(d·k) for d < k/R, plus a spike at d = k\n- ρ(d) = 1/(d·(d-1)) for the\
  \ ideal Soliton distribution\n- μ(d) = (τ + ρ) / sum(τ + ρ)\n\nwhere R = c·log(k/δ)·√k for constants c and δ.\n\n**Algorithm\
  \ 1** summarizes the encoding process.\n\n```\nAlgorithm 1: Rateless MinHash Encoding\nInput: Set S, number of base hashes\
  \ k, random seed\nOutput: Infinite stream of coded hash values\n\n1. Compute base hash values: for each i ∈ {1,...,k}, compute\
  \ h_i(S) = min_{x∈S} hash_i(x)\n2. Initialize index stream using Robust Soliton distribution\n3. For j = 1, 2, ... (infinite):\n\
  \   a. Sample degree d_j from μ(d)\n   b. Select indices I_j = {i_1, ..., i_d_j} uniformly at random from {1,...,k}\n  \
  \ c. Compute coded hash: c_j = min_{i∈I_j} h_i(S)\n   d. Yield c_j and I_j (indices must be shared between sets)\n```\n\n\
  #### 3.2.2 Progressive Decoding\n\nTo estimate Jaccard similarity from two coded hash streams, we process hash values sequentially:\n\
  \n1. Initialize `matches = 0`\n2. For each position i = 1, 2, ...:\n   - If `coded_hash_i(A) == coded_hash_i(B)` (within\
  \ floating-point tolerance), increment `matches`\n   - Estimate Ĵ_i = matches / i\n   - Compute running MSE if true Jaccard\
  \ is known\n\nThe key property is that **the probability of a match at any position equals the Jaccard similarity**: Pr[c_i(A)\
  \ = c_i(B)] = J(A,B). This preserves the MinHash property and ensures unbiased estimation.\n\n#### 3.2.3 Adaptive Stopping\
  \ Rule\n\nRateless MinHash enables adaptive stopping: we can stop processing hash values when the estimation error is sufficiently\
  \ low. While the optimal stopping rule based on rate-distortion theory requires the rate-distortion function R(D) for Jaccard\
  \ estimation (which is unknown), we can use heuristic stopping rules:\n\n1. **Fixed Error Tolerance**: Stop when the confidence\
  \ interval width falls below 2ε\n2. **Sequential Probability Ratio Test (SPRT)**: Adapt SPRT to test whether |Ĵ - J| <\
  \ ε\n3. **Variance-Based Stopping**: Stop when the estimated variance falls below a threshold\n\nIn our experiments, we\
  \ use a simple stopping rule based on the number of processed hash values reaching a target budget, which can be determined\
  \ adaptively based on the application's accuracy requirements.\n\n### 3.3 Theoretical Analysis of Dependencies\n\n**MinHash\
  \ Property Preservation**: The coded hash values preserve the MinHash property because the minimum operation over a random\
  \ subset of base hashes maintains the probability of collision equal to Jaccard similarity. Formally, if indices I are sampled\
  \ uniformly at random, then Pr[min_{i∈I} h_i(A) = min_{i∈I} h_i(B)] = J(A,B).\n\n**Dependency Structure**: Unlike standard\
  \ MinHash which uses independent hash functions, Rateless MinHash introduces dependencies between coded hash values. Let\
  \ π_i be the indicator that coded hash i matches. Then Ĵ_k = (1/k) Σ_{i=1}^k π_i. The variance is:\n\nVar[Ĵ_k] = (1/k²)\
  \ [Σ_i Var[π_i] + 2 Σ_{i<j} Cov[π_i, π_j]]\n\nThe dependencies (non-zero covariance) arise because the same base hashes\
  \ can be selected multiple times across different coded hash values.\n\n**Covariance Analysis**: We derive E[π_i π_j] =\
  \ Pr[match at both positions i and j]. Let I_i and I_j be the randomly selected index sets at positions i and j, with degrees\
  \ d_i and d_j. The probability of joint match depends on the overlap between I_i and I_j:\n\nE[π_i π_j] = J^{|I_i ∪ I_j|/|I_i\
  \ ∩ I_j|} ≈ J² · (1 + O(d²/k²))\n\nwhere the approximation holds when d/k is small. The covariance is:\n\nCov[π_i, π_j]\
  \ = E[π_i π_j] - J² = O(J² · d²/k²)\n\n**MSE Penalty**: The ratio of MSE between Rateless MinHash and standard MinHash is:\n\
  \nMSE_ratio = Var[Rateless] / Var[Standard] = 1 + d²/k²\n\nThis result is formally verified using Lean 4 . The experimental\
  \ range 1.01-1.93x corresponds to d/k ∈ [0.1, 0.96], matching the degree distribution analysis.\n\n**Proof Sketch**: The\
  \ penalty formula MSE_ratio = 1 + d²/k² is derived by:\n1. Bounding the total covariance sum: Σ_{i<j} Cov[π_i, π_j] = O(k\
  \ · d²/k²)\n2. Showing this adds d²/k² to the normalized variance\n3. Verifying with concrete examples: d=1, k=10 → 1.01x;\
  \ d=96, k=100 → 1.93x\n\n[FIGURE:fig2]\n\n### 3.4 Space Complexity\n\nRateless MinHash uses `num_base_hashes` base hash\
  \ values, each requiring 32-64 bits. The adaptive stopping rule determines the actual number of coded hash values used,\
  \ which can be less than `num_base_hashes` if high accuracy is achieved early.\n\n## 4 Experiments\n\nWe evaluate Rateless\
  \ MinHash on synthetic and real-world datasets and compare it against standard MinHash baselines. Our experiments address\
  \ five questions:\n\n1. How does the estimation error of Rateless MinHash compare to standard MinHash as the number of hash\
  \ values increases?\n2. Can Rateless MinHash achieve space efficiency through adaptive stopping?\n3. What is the trade-off\
  \ between the flexibility of progressive estimation and statistical efficiency?\n4. How does Rateless MinHash compare to\
  \ simple adaptive baselines?\n5. What is the effect of different aggregation functions?\n\n### 4.1 Experimental Setup\n\n\
  **Datasets**: We use synthetic datasets with controlled Jaccard similarity \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-2e68d8-rateless-minhash-progressive-jaccard-est/tree/main/round-1/dataset-1}}\
  \ and real-world text datasets (Quora, MS MARCO, 20 Newsgroups, AG News, C4) with 60 total document pairs .\n\n**Baselines**:\
  \ \n- **Standard MinHash** with fixed sketch sizes k ∈ {16, 32, 64, 128}\n- **Adaptive Independent MinHash**: Sequentially\
  \ add independent hash values until error estimate stabilizes\n\n**Implementation**: Both Standard MinHash and Rateless\
  \ MinHash are implemented in Python using NumPy and hashlib for hash computation . Rateless MinHash uses `num_base_hashes\
  \ = 128` and the Robust Soliton distribution for degree sampling.\n\n**Metrics**:\n- **Mean Squared Error (MSE)**: (Ĵ -\
  \ J)², averaged over set pairs\n- **Space (bits)**: Number of hash values used × bits per hash value (32 bits for float32)\n\
  - **Improvement Rate**: The percentage reduction in MSE as more hash values are processed\n- **Non-monotonicity Frequency**:\
  \ Percentage of runs where MSE increases between consecutive positions\n\n### 4.2 Experiment 1: Error vs Sketch Size (Standard\
  \ MinHash)\n\nWe first verify that standard MinHash exhibits the expected O(1/k) MSE decrease. Figure 2 (left) shows the\
  \ results:\n\n- k=16: MSE = 0.0140 (std = 0.0210)\n- k=32: MSE = 0.0056 (std = 0.0085)\n- k=64: MSE = 0.0022 (std = 0.0025)\n\
  - k=128: MSE = 0.0011 (std = 0.0021)\n\nThe MSE decreases as expected, confirming the theoretical variance formula.\n\n\
  ### 4.3 Experiment 2: Progressive Estimation (Rateless MinHash)\n\nWe evaluate whether Rateless MinHash enables progressive\
  \ Jaccard estimation. For set pairs with true Jaccard similarities J ∈ {0.1, 0.3, 0.5, 0.7, 0.9}, we process up to 128 coded\
  \ hash values and record the MSE at each step.\n\n**Results**: Rateless MinHash successfully enables progressive estimation.\
  \ The error decreases as more coded hash values are processed, with a 55-80% reduction in MSE from the first 10 to 128 hash\
  \ values.\n\nFigure 2 (right) shows the progressive MSE curves for different true Jaccard values:\n- J=0.1: Final MSE =\
  \ 0.0017 after 128 hashes (79% improvement)\n- J=0.3: Final MSE = 0.0027 after 128 hashes (56% improvement)\n- J=0.5: Final\
  \ MSE = 0.0053 after 128 hashes (71% improvement)\n- J=0.7: Final MSE = 0.0036 after 128 hashes (81% improvement)\n- J=0.9:\
  \ Final MSE = 0.0016 after 128 hashes (61% improvement)\n\n**Non-Monotonic Behavior**: Due to dependencies between coded\
  \ hash values, the MSE does not decrease monotonically. Our analysis shows that non-monotonic behavior occurs in 80-90%\
  \ of runs . This is expected: dependent samples produce higher variance in early estimates compared to independent samples.\
  \ Figure 3 shows example MSE curves with confidence intervals illustrating this behavior.\n\n[FIGURE:fig3]\n\n### 4.4 Experiment\
  \ 3: Space Efficiency with Adaptive Stopping\n\nWe compare the space efficiency of standard MinHash (fixed sketch size)\
  \ and Rateless MinHash (adaptive stopping). For Rateless MinHash, we simulate adaptive stopping by using a target error\
  \ threshold and stopping when the estimated error falls below the threshold.\n\n**Results**: \n- Standard MinHash uses fixed\
  \ bits: 512 (k=16), 1024 (k=32), 2048 (k=64), or 4096 (k=128)\n- Rateless MinHash with adaptive stopping uses ~853 bits\
  \ on average (±148), achieving an average error of 0.0655\n\nCompared to standard MinHash with k=32 (1024 bits, error=0.0559),\
  \ Rateless MinHash uses less space but with slightly higher error. This demonstrates the adaptive trade-off: Rateless MinHash\
  \ can achieve near-equivalent accuracy with less space on average.\n\n### 4.5 Equal-Bits Comparison: Statistical Efficiency\
  \ Trade-off\n\nTo understand the trade-off between progressive estimation flexibility and statistical efficiency, we compare\
  \ Rateless MinHash and standard MinHash at equal bit budgets.\n\n**Results**: At equal bit budgets, standard MinHash outperforms\
  \ Rateless MinHash. The ratio of MSE (Rateless / Standard) ranges from 1.01 to 1.93 depending on the bit budget (Table 1).\
  \ This is expected: standard MinHash uses independent hash functions, while Rateless MinHash introduces dependencies via\
  \ the coding process. The dependencies reduce statistical efficiency but enable progressive estimation.\n\n**Theoretical\
  \ vs Experimental**: The experimental ratios closely match our theoretical prediction of 1 + d²/k². For example, with d/k\
  \ ≈ 0.1, the ratio is 1.01x; with d/k ≈ 0.96, the ratio is 1.93x .\n\n| Bits | Standard Error | Rateless Error | Ratio |\n\
  |-------|----------------|----------------|-------|\n| 512   | 0.0911 ± 0.0757 | 0.0915 ± 0.0599 | 1.01  |\n| 1024  | 0.0559\
  \ ± 0.0494 | 0.0739 ± 0.0582 | 1.32  |\n| 2048  | 0.0394 ± 0.0263 | 0.0659 ± 0.0481 | 1.67  |\n| 4096  | 0.0241 ± 0.0227\
  \ | 0.0466 ± 0.0417 | 1.93  |\n\n*Table 1: Equal-bits comparison showing MSE ratio (Rateless / Standard).*\n\n### 4.6 Experiment\
  \ 4: Comparison with Adaptive Baselines\n\nA natural question is whether the complexity of fountain codes is necessary for\
  \ progressive estimation. We compare Rateless MinHash against a simple adaptive baseline: **Adaptive Independent MinHash**\
  \ which starts with k=1 and sequentially adds independent hash values until the error estimate stabilizes.\n\n**Results**:\
  \ The simple adaptive baseline achieves similar space-accuracy trade-offs to Rateless MinHash (efficiency ratio 0.972x in\
  \ our experiments, meaning Rateless performed slightly better in this run) . However, Rateless MinHash provides:\n1. **Principled\
  \ framework**: The dependency structure is analyzable through our theoretical framework\n2. **Controlled degree distribution**:\
  \ The Robust Soliton distribution provides predictable dependency patterns\n3. **Potential for optimization**: Future work\
  \ can derive optimal degree distributions for MinHash\n\n**When is Rateless MinHash justified?** The fountain code complexity\
  \ is justified when:\n- Theoretical understanding of dependencies is important (e.g., for deriving optimal stopping rules)\n\
  - The degree distribution can be optimized for specific datasets or accuracy requirements\n- Integration with other fountain\
  \ code applications is needed\n\n### 4.7 Experiment 5: Aggregation Function Ablation\n\nWe analyze the choice of aggregation\
  \ function in the coding process. The method.py supports four aggregation functions: min, mean, median, and XOR.\n\n**Results**:\
  \ XOR aggregation achieves the best performance with MSE=0.1452 at position 16, followed by min (MSE=0.1837), median (MSE=0.1923),\
  \ and mean (MSE=0.2108) . However, XOR does not preserve the MinHash property (Pr[match] ≠ J), making it unsuitable for\
  \ unbiased Jaccard estimation. The min operation is the only aggregation function that both preserves the MinHash property\
  \ and achieves reasonable accuracy.\n\n### 4.8 Near-Duplicate Detection Application\n\nWe evaluate Rateless MinHash on near-duplicate\
  \ text detection across 6 real-world datasets. Using a threshold of 0.3 on estimated Jaccard similarity, both Rateless MinHash\
  \ and Standard MinHash achieve F1=1.000 on the test sets .\n\n**Computational Overhead**: Rateless MinHash has higher computational\
  \ overhead than standard MinHash. Generating each coded hash value requires: (1) sampling a degree from the Robust Soliton\
  \ distribution, (2) selecting random indices, (3) computing the minimum over selected base hashes. In our implementation,\
  \ Rateless MinHash takes ~3x longer per hash value compared to standard MinHash. This overhead is acceptable for applications\
  \ where estimation accuracy is more important than computation speed, but it may be prohibitive for very high-throughput\
  \ scenarios.\n\n[FIGURE:fig4]\n\n### 4.9 Discussion of Results\n\nThe experimental results demonstrate that Rateless MinHash\
  \ achieves its primary goal: **progressive Jaccard estimation with adaptive space-accuracy trade-offs**. The key findings\
  \ are:\n\n1. **Progressive Estimation Works**: The error decreases (on average) as more hash values are processed, with\
  \ 55-80% improvement from 10 to 128 hash values.\n\n2. **Adaptive Stopping Saves Space**: Rateless MinHash with adaptive\
  \ stopping uses ~853 bits on average, compared to fixed 1024+ bits for standard MinHash.\n\n3. **Statistical Efficiency\
  \ Trade-off**: Rateless MinHash trades 1.01-1.93x higher error for the flexibility of progressive estimation. This trade-off\
  \ is acceptable in applications where the optimal sketch size is unknown or data-dependent.\n\n4. **Non-Monotonic Behavior**:\
  \ Dependencies cause non-monotonic MSE curves in 80-90% of runs. This is expected and should be considered when using progressive\
  \ estimation.\n\n5. **Simple Baselines Competitive**: Adaptive independent MinHash achieves similar space-accuracy trade-offs,\
  \ but lacks the analyzable dependency structure of Rateless MinHash.\n\n**Limitation**: The current implementation uses\
  \ the Robust Soliton distribution from LT codes, which may not be optimal for MinHash. The degree distribution affects the\
  \ dependence structure between coded hash values and hence the statistical efficiency. Deriving an optimal degree distribution\
  \ for Rateless MinHash is an open problem.\n\n## 5 Discussion and Limitations\n\n### 5.1 Theoretical Gap: Rate-Distortion\
  \ Function for Jaccard Estimation\n\nA key theoretical gap is the unknown rate-distortion function R(D) for Jaccard similarity\
  \ estimation. Such a function would provide the optimal trade-off between sketch bits (rate) and estimation MSE (distortion).\
  \ Currently, only lower bounds exist from information complexity [3]. Deriving R(D) for Jaccard estimation would enable\
  \ optimal stopping rules for Rateless MinHash.\n\n### 5.2 Computational Overhead\n\nRateless MinHash has higher computational\
  \ overhead than standard MinHash. Generating each coded hash value requires: (1) sampling a degree from the Robust Soliton\
  \ distribution, (2) selecting random indices, (3) computing the minimum over selected base hashes. In contrast, standard\
  \ MinHash simply computes independent hash values. The overhead is acceptable for applications where estimation accuracy\
  \ is more important than computation speed, but it may be prohibitive for very high-throughput scenarios.\n\n### 5.3 Dependency\
  \ Structure\n\nThe coding process introduces dependencies between coded hash values, reducing statistical efficiency. The\
  \ dependency structure is determined by the degree distribution and the random index selection. A careful theoretical analysis\
  \ of these dependencies and their effect on estimator variance is needed. Our work provides the first such analysis, showing\
  \ the penalty equals 1 + d²/k².\n\n### 5.4 Novelty Considerations\n\nWhile applying fountain codes to MinHash is novel,\
  \ the idea of progressive estimation via sequential sampling is not new in sketching [13]. Simple adaptive baselines (sequentially\
  \ adding independent MinHash values) can achieve similar space-accuracy trade-offs. The contribution of Rateless MinHash\
  \ is:\n1. A principled framework for progressive estimation with analyzable dependencies\n2. The first theoretical analysis\
  \ of dependency structure in progressive MinHash\n3. A foundation for future optimizations (optimal degree distribution,\
  \ integration with other fountain code techniques)\n\n### 5.5 Future Work\n\n1. **Optimal Degree Distribution**: Derive\
  \ the optimal degree distribution for Rateless MinHash that minimizes the variance of the estimator while maintaining the\
  \ rateless property.\n\n2. **Raptor-Inspired Rateless MinHash**: Explore using Raptor codes (with linear-time encoding/decoding)\
  \ instead of LT codes for improved computational efficiency.\n\n3. **Real-World Evaluation**: Evaluate Rateless MinHash\
  \ on real-world datasets for near-duplicate detection in web-scale corpora (e.g., The Pile, C4).\n\n4. **Rate-Distortion\
  \ Derivation**: Derive the rate-distortion function for Jaccard similarity estimation to enable theoretically optimal stopping\
  \ rules.\n\n5. **Multi-Set Extension**: Extend Rateless MinHash to estimate Jaccard similarities for multiple sets simultaneously,\
  \ enabling clustering and near-duplicate group detection.\n\n6. **Hybrid Approaches**: Combine Rateless MinHash with simple\
  \ adaptive baselines, using independent hashes initially and switching to coded hashes when more accuracy is needed.\n\n\
  ## 6 Conclusion\n\nWe have presented **Rateless MinHash**, a MinHash variant that enables progressive Jaccard similarity\
  \ estimation. By applying fountain code principles (inspired by LT codes), Rateless MinHash generates a potentially infinite\
  \ sequence of coded hash values, allowing estimates to improve as more values are processed.\n\nThe key theoretical contribution\
  \ is the analysis of dependencies introduced by the coding process. We prove that the MSE penalty equals 1 + d²/k², where\
  \ d is the degree and k is the number of base hashes. This result is verified through both mathematical analysis and formal\
  \ Lean 4 proofs.\n\nExperimental evaluation demonstrates that Rateless MinHash achieves:\n- **Progressive estimation**:\
  \ 55-80% reduction in MSE from processing 10 to 128 coded hash values\n- **Adaptive space efficiency**: ~853 bits average\
  \ usage with adaptive stopping, compared to fixed 1024+ bits for standard MinHash\n- **Reasonable trade-off**: 1.01-1.93x\
  \ higher error than standard MinHash at equal bit budgets, in exchange for progressive estimation capability\n- **Honest\
  \ baseline comparison**: Similar performance to simple adaptive baselines, but with analyzable dependency structure\n\n\
  While theoretical questions remain (rate-distortion function, optimal degree distribution), Rateless MinHash opens a new\
  \ direction in sketching algorithms: **rateless sketches that adapt to the desired accuracy at estimation time rather than\
  \ at sketch creation time**. This capability is valuable for distributed deduplication, streaming data, and applications\
  \ where the optimal sketch size is data-dependent.\n\n**Reproducibility**: All code, data, and proofs are available as artifacts\
  \ [ARTIFACT:art_Q8_IBJsGhfEE, art_50tMXu2lMfkc, art_0XRo6tTpAffY, art_ZpaiuGemkOnz].\n\n## Acknowledgments\n\n[To be filled\
  \ based on funding sources]\n\n## References\n\n[1] Broder, A. \"On the resemblance and containment of documents.\" Proceedings\
  \ of the Compression and Complexity of Sequences. 1997.\n\n[2] Li, P. and König, A. \"b-Bit minwise hashing.\" The Web Conference,\
  \ 2009.\n\n[3] Pagh, R., Stöckel, M., and Woodruff, D. P. \"Is min-wise hashing optimal for summarizing set intersection?\"\
  \ ACM SIGACT-SIGMOD-SIGART Symposium on Principles of Database Systems, 2014.\n\n[4] Li, P. and König, A. \"Theory and applications\
  \ of b-bit minwise hashing.\" Communications of the ACM, 2011.\n\n[5] Mitzenmacher, M., Pagh, R., and Pham, N. D. \"Efficient\
  \ estimation for high similarities using odd sketches.\" The Web Conference, 2014.\n\n[6] Ertl, O. \"SetSketch: Filling\
  \ the Gap between MinHash and HyperLogLog.\" Proceedings of the VLDB Endowment, 2021.\n\n[7] Mitzenmacher, M., Pagh, R.,\
  \ and Pham, N. D. \"Efficient estimation for high similarities using odd sketches.\" The Web Conference, 2014.\n\n[8] Ertl,\
  \ O. \"ProbMinHash -- A Class of Locality-Sensitive Hash Algorithms for the (Probability) Jaccard Similarity.\" IEEE Transactions\
  \ on Knowledge and Data Engineering, 2019.\n\n[9] Luby, M. \"LT codes.\" IEEE Transactions on Information Theory, 2002.\n\
  \n[10] Shokrollahi, A. \"Raptor codes.\" IEEE Transactions on Information Theory, 2006.\n\n[11] Cover, T. M. and Thomas,\
  \ J. A. \"Elements of Information Theory.\" Chapter 13: Rate Distortion Theory, 1991.\n\n[12] Wikipedia contributors. \"\
  Rate-distortion theory.\" Wikipedia, 2023.\n\n[13] Cormode, G. et al. \"Sketch Techniques for Approximate Query Processing.\"\
  \ Foundations and Trends in Databases, 2012.\n\n[14] Li, P. et al. \"One Permutation MinHash.\" International Conference\
  \ on Machine Learning, 2014.\n\n[15] Shrivastava, A. \"Densified One Permutation MinHash.\" ACM SIGKDD International Conference\
  \ on Knowledge Discovery and Data Mining, 2017.\n\n[16] Ioffe, S. \"Improved consistent sampling, weighted minhash and L1\
  \ sketching.\" IEEE International Conference on Data Mining, 2010.\n\n---\n\n**Bibliography (BibTeX)**\n\nThe following\
  \ BibTeX entries are fetched from Semantic Scholar and should be saved to `references.bib` for LaTeX compilation:\n\n```bibtex\n\
  @inproceedings{Pagh2014,\n  author = {R. Pagh and Morten St\\\"{o}ckel and David P. Woodruff},\n  booktitle = {ACM SIGACT-SIGMOD-SIGART\
  \ Symposium on Principles of Database Systems},\n  title = {Is min-wise hashing optimal for summarizing set intersection?},\n\
  \  year = {2014},\n  doi = {10.1145/2594538.2594554}\n}\n\n@inproceedings{Mitzenmacher2014,\n  author = {M. Mitzenmacher\
  \ and R. Pagh and Ninh D. Pham},\n  booktitle = {The Web Conference},\n  title = {Efficient estimation for high similarities\
  \ using odd sketches},\n  year = {2014},\n  doi = {10.1145/2566486.2568017}\n}\n\n@inproceedings{Ertl2019,\n  author = {Otmar\
  \ Ertl},\n  booktitle = {IEEE Transactions on Knowledge and Data Engineering},\n  title = {ProbMinHash -- A Class of Locality-Sensitive\
  \ Hash Algorithms for the (Probability) Jaccard Similarity},\n  volume = {34},\n  pages = {3491-3506},\n  year = {2019},\n\
  \  doi = {10.1109/tkde.2020.3021176}\n}\n```\n\n**Note**: The full BibTeX file with all references should be compiled from\
  \ the references.bib file. For papers not found via Semantic Scholar (Broder 1997, Luby 2002, Shokrollahi 2006, Cover &\
  \ Thomas 1991), we provide verified bibliographic information based on the original sources.\n\n[FIGURE:fig5]"
summary: >-
  This paper presents Rateless MinHash, the first MinHash variant enabling progressive Jaccard similarity estimation using
  fountain code principles. The key contributions are: (1) novel algorithm generating hash values on-demand, (2) theoretical
  analysis of dependency structure with formal Lean 4 proofs showing MSE penalty = 1 + d²/k², (3) experimental validation
  with 55-80% MSE reduction from progressive estimation, (4) adaptive space efficiency using ~853 bits vs fixed 1024+ bits,
  (5) honest comparison against simple adaptive baselines. The method trades 1.01-1.93x statistical efficiency for progressive
  estimation capability. While simple baselines achieve similar results, Rateless MinHash provides a principled framework
  with analyzable dependencies, opening new directions for rateless sketching algorithms.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
title: Rateless MinHashOverview
caption: >-
  Overview of Rateless MinHash. The method generates coded hash values by sampling degrees from Robust Soliton distribution
  and computing minimum over selected base hashes, enabling progressive Jaccard estimation.
image_gen_detailed_description: >-
  Horizontal flow diagram, left to right. Five labeled boxes: 'Input Sets A,B' (gray), 'Base Hash Computation' (blue, with
  k=128 base hashes), 'Degree Sampling from Robust Soliton' (orange), 'Min Aggregation over Selected Hashes' (green), 'Progressive
  Jaccard Estimation' (purple). Arrows between boxes showing data flow. Below the diagram: equation Pr[c_i(A)=c_i(B)] = J(A,B).
  Sans-serif font, clean white background, no 3D.
aspect_ratio: '21:9'
summary: >-
  Hero architecture diagram showing Rateless MinHash encoding and progressive estimation pipeline
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
title: MSE vs Number of Hash Values
caption: >-
  Left: Standard MinHash MSE decreases as O(1/k) with k=16 (MSE=0.0140), k=32 (MSE=0.0056), k=64 (MSE=0.0022), k=128 (MSE=0.0011).
  Right: Rateless MinHash progressive MSE curves for J∈{0.1, 0.3, 0.5, 0.7, 0.9} showing 55-80% reduction from 10 to 128 hash
  values.
image_gen_detailed_description: >-
  Two subplots side by side (16:9 aspect). Left plot: Standard MinHash MSE vs k. X-axis: k = [16, 32, 64, 128]. Y-axis: MSE
  = [0.0140, 0.0056, 0.0022, 0.0011]. Log-log scale. Right plot: Rateless MinHash progressive MSE. X-axis: positions 1 to
  128 (log scale). Y-axis: MSE (log scale). Five curves for J=0.1 (MSE final=0.0017), J=0.3 (0.0027), J=0.5 (0.0053), J=0.7
  (0.0036), J=0.9 (0.0016). Shows decreasing trends with non-monotonic behavior. Sans-serif font, white background.
aspect_ratio: '21:9'
summary: >-
  Compares Standard MinHash error vs sketch size and Rateless MinHash progressive estimation curves
figure_path: figures/fig2_v0.jpg

--- Item 3 ---
id: fig3
title: Non-Monotonic Behavior Example
caption: >-
  Example MSE curves for Rateless MinHash showing non-monotonic behavior (80-90% frequency). Shaded regions show bootstrap
  confidence intervals (95% CI). The dependencies between coded hash values cause variance in early estimates.
image_gen_detailed_description: >-
  Line plot with confidence intervals. X-axis: positions 1 to 32. Y-axis: MSE (log scale, 0.001 to 0.1). Three example curves
  for J=0.3, J=0.5, J=0.7 showing non-monotonic behavior where MSE increases between some consecutive positions. Shaded regions:
  bootstrap 95% CI (light blue). Mean curves: solid lines (blue, orange, green). Horizontal dashed line: standard MinHash
  MSE with k=32 (0.0056). Sans-serif font, white background.
aspect_ratio: '21:9'
summary: Illustrates non-monotonic MSE behavior due to dependencies in Rateless MinHash
figure_path: figures/fig3_v0.jpg

--- Item 4 ---
id: fig4
title: Statistical Efficiency Trade-off
caption: >-
  Equal-bits comparison showing MSE ratio (Rateless / Standard) ranging from 1.01x to 1.93x. The theoretical prediction (1
  + d²/k²) matches experimental results. Rateless MinHash trades statistical efficiency for progressive estimation capability.
image_gen_detailed_description: >-
  Grouped bar chart. X-axis: bit budgets = [512, 1024, 2048, 4096]. Y-axis: MSE ratio (1.0 to 2.0). Bars: blue (Standard MinHash,
  all at 1.0), orange (Rateless MinHash = [1.01, 1.32, 1.67, 1.93]). Overlaid line: theoretical prediction 1 + d²/k². Error
  bars: ±0.05. Annotations: '1.01x (d/k=0.1)', '1.93x (d/k=0.96)'. Table inset showing exact values. Sans-serif font, white
  background.
aspect_ratio: '21:9'
summary: >-
  Visualizes the statistical efficiency trade-off between Rateless and Standard MinHash
figure_path: figures/fig4_v0.jpg

--- Item 5 ---
id: fig5
title: Aggregation Function Comparison
caption: >-
  Ablation study comparing min, mean, median, and XOR aggregation functions. XOR achieves lowest MSE (0.1452 at position 16)
  but does not preserve MinHash property. Min is the only function that preserves Pr[match]=J while achieving reasonable accuracy.
image_gen_detailed_description: >-
  Bar chart. X-axis: aggregation functions = ['min', 'mean', 'median', 'xor']. Y-axis: MSE at position 16 (0.0 to 0.25). Values:
  min=0.1837, mean=0.2108, median=0.1923, xor=0.1452. Color code: red for XOR (does not preserve MinHash property), blue for
  others. Annotation: 'XOR: lowest MSE but Pr[match] ≠ J'. Below bars: checkmarks/crosses for 'Preserves MinHash Property'.
  Sans-serif font, white background.
aspect_ratio: '21:9'
summary: >-
  Compares different aggregation functions for coded hash generation in Rateless MinHash
figure_path: figures/fig5_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-03 20:02:41 UTC

```
A simple and efficient MinHash-based method for detecting near-duplicate text passages in large corpora.
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-07-03 20:02:51 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figure JPEGs, and bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.jpg}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS use `[!htbp]` float placement (NOT `[t]` or `[h]` alone)
- ALWAYS constrain with `width` and `keepaspectratio` to prevent page takeover
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/*.jpg` — all figure images (pre-generated, copied into workspace)
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-03 20:02:51 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
