# upd_hypo — test_idea

> Phase: `invention_loop` · round 1 · `upd_hypo`
> Run: `run_sAQsTTaaqjOV` — Rateless MinHash: Progressive Jaccard Estimation via Fountain Codes
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-03 18:34:45 UTC

````
<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: 'Rateless MinHash: Progressive Jaccard Estimation via Fountain Codes'
hypothesis: >-
  By viewing MinHash as a lossy compression channel and applying fountain code (rateless erasure code) principles, we can
  create a rateless MinHash sketch that generates a potentially infinite sequence of hash values, enabling progressive refinement
  of Jaccard similarity estimates. The optimal stopping point (sketch size) can be determined from rate-distortion theory,
  achieving optimal space-accuracy trade-offs without knowing the target similarity distribution beforehand.
motivation: >-
  MinHash and its variants require fixing the sketch size (number of hash functions) upfront, before knowing the desired estimation
  accuracy or the distribution of Jaccard similarities in the dataset. This leads to either wasted space (oversized sketches)
  or insufficient accuracy (undersized sketches). A rateless MinHash would solve this by generating hash values on-demand,
  allowing progressive refinement of estimates until a target accuracy is reached. This is particularly valuable for distributed
  deduplication, streaming data, and applications where the optimal sketch size is data-dependent.
assumptions:
- >-
  Jaccard similarity estimation can be framed as a rate-distortion problem where rate = sketch size and distortion = mean
  squared error in similarity estimation
- >-
  Fountain code principles (rateless coding) can be applied to generate a sequence of dependent hash values that together
  provide progressive Jaccard estimation
- >-
  The hash value sequence can be designed such that the estimation error decays monotonically as more values are received
- >-
  Rate-distortion theory can provide a computable bound for the optimal stopping point given a target estimation error
investigation_approach: >-
  1. Formalize MinHash as a rate-distortion problem: define the rate (sketch bits) and distortion (estimation error) for Jaccard
  similarity estimation. 2. Design a rateless MinHash scheme inspired by LT/Raptor fountain codes: generate a potentially
  infinite sequence of coded hash values from the set elements. 3. Derive the rate-distortion function for Jaccard estimation
  and use it to determine optimal stopping rules. 4. Implement the rateless MinHash algorithm and compare against standard
  MinHash, b-bit MinHash, and SetSketch on near-duplicate detection tasks. 5. Evaluate on LLM training data deduplication
  benchmarks (e.g., The Pile, C4) measuring space efficiency, estimation accuracy, and runtime.
success_criteria: >-
  The rateless MinHash scheme should: (1) Achieve the same Jaccard estimation accuracy as standard MinHash with less space
  on average (by adapting sketch size to each pair's similarity); (2) Provide progressive estimates that improve monotonically
  as more hash values are processed; (3) Have a computable stopping rule based on rate-distortion theory that achieves near-optimal
  space-accuracy trade-off; (4) Outperform fixed-size MinHash variants on datasets with diverse Jaccard similarity distributions.
related_works:
- >-
  Standard MinHash (Broder et al.) - uses k independent random permutations to estimate Jaccard similarity; our approach generalizes
  this to a rateless setting where k is not fixed upfront.
- >-
  b-bit MinHash (Li & Konig) - reduces sketch size by storing only b bits per hash value; our approach achieves variable sketch
  size through progressive refinement rather than fixed-size compression.
- >-
  SetSketch (Ertl) - bridges MinHash and HyperLogLog with a configurable parameter; our approach differs by making the sketch
  size itself adaptive rather than fixed at creation time.
- >-
  Polar Code Nearest-Neighbor (Touitou & Halabi) - uses error-correcting codes for LSH clustering; our approach applies coding
  theory to the hash function design itself, not just to the clustering step.
- >-
  ProbMinHash (Ertl) - computes probability Jaccard similarity for weighted sets; our approach addresses a different problem
  (rateless/progressive estimation) for unweighted Jaccard similarity.
- >-
  Odd Sketch (Mitzenmacher et al.) - uses binary sketches with XOR properties for high similarities; our approach targets
  the general case with progressive refinement rather than a fixed binary sketch.
inspiration: >-
  The hypothesis combines three cross-domain inspirations: (1) Fountain codes / rateless erasure codes from coding theory
  - where encoded symbols can be generated indefinitely and decoding becomes possible after receiving enough symbols; (2)
  Rate-distortion theory from information theory - which provides the optimal trade-off between compression rate and estimation
  distortion; (3) Progressive refinement from numerical analysis - where estimates are improved incrementally. The key insight
  is that MinHash sketches are essentially 'encoded' representations of sets, and by using coding-theoretic principles we
  can make this encoding rateless (adaptive to the desired accuracy).
terms:
- term: MinHash
  definition: >-
    A locality-sensitive hashing technique that estimates Jaccard similarity between two sets by computing the probability
    that the minimum hash value under a random permutation is the same for both sets.
- term: Jaccard similarity
  definition: >-
    A similarity measure for sets defined as the ratio of the intersection size to the union size: J(A,B) = |A∩B| / |A∪B|.
    It ranges from 0 (disjoint sets) to 1 (identical sets).
- term: Fountain code / rateless code
  definition: >-
    An erasure code that can generate an unlimited number of encoded symbols from a source message. The receiver can recover
    the original message after receiving any sufficient subset of encoded symbols, making the code 'rateless' (no fixed rate).
- term: Rate-distortion theory
  definition: >-
    A framework in information theory that studies the optimal trade-off between the compression rate (bits per symbol) and
    the resulting distortion (loss) in lossy data compression.
- term: Locality-sensitive hashing (LSH)
  definition: >-
    A family of hash functions where similar items are more likely to hash to the same value than dissimilar items. MinHash
    is an LSH family for Jaccard similarity.
- term: Progressive estimation
  definition: >-
    An estimation procedure where the accuracy improves monotonically as more computational resources (time, space, or data)
    are invested, without requiring the total resource budget to be fixed upfront.
summary: >-
  We propose Rateless MinHash, a new sketching approach that applies fountain code principles to MinHash, enabling progressive
  Jaccard similarity estimation where hash values are generated on-demand and the sketch size adapts to the desired accuracy.
  Rate-distortion theory provides the optimal stopping rule.
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

--- Item 1 ---
id: art_9jz-SfB9wrwJ
type: research
title: Rateless MinHash Theory Foundations Research
summary: >-
  This research provides the theoretical foundations for Rateless MinHash, a novel sketching approach addressing the fundamental
  limitation of fixed sketch size in existing MinHash variants. Key findings include: (1) All current MinHash variants (Standard,
  b-bit, SetSketch, Odd Sketch, ProbMinHash) require upfront sketch size selection [1, 4, 6, 7, 8]. (2) Fountain codes (LT
  codes, Raptor codes) provide a proven rateless encoding framework where infinite symbol sequences can be generated with
  decoding possible from any slightly larger set [9, 10]. (3) The rate-distortion function for Jaccard similarity estimation
  remains undiscovered, though lower bounds exist from information complexity [3, 11, 12]. (4) A mathematical framework for
  Rateless MinHash is proposed, featuring encoding via degree-distributed hash generation, progressive decoding with decreasing
  variance O(1/k), and optimal stopping rules based on sequential estimation theory. The expected contribution is a sketch
  achieving near-optimal rate-distortion performance while adapting to diverse similarity regimes without upfront parameter
  tuning.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 2 ---
id: art_ZpaiuGemkOnz
type: dataset
title: Near-Duplicate Text Datasets for MinHash Evaluation
summary: >-
  This artifact provides 6 text datasets (Quora, 20 Newsgroups, MS MARCO, C4, AG News, synthetic) with 30K total documents
  and 3.5K duplicate pairs. The datasets include diverse text types from short questions to long documents, with controlled
  Jaccard similarity levels (0.1, 0.3, 0.5, 0.7, 0.9). Each document is tokenized and includes metadata with source dataset,
  duplicate ID, and similarity level. The data supports evaluation of Rateless MinHash and baseline methods on near-duplicate
  detection and Jaccard similarity estimation tasks. File size is 46MB, under the 100MB limit.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 3 ---
id: art_Q8_IBJsGhfEE
type: experiment
title: Progressive MinHash with Fountain Code Principles
summary: >-
  This experiment implements and evaluates a novel Rateless MinHash approach that uses fountain code principles (inspired
  by LT codes) to generate hash values progressively for adaptive Jaccard similarity estimation. The implementation includes
  StandardMinHash as baseline and RatelessMinHash as the novel method. Three experiments were conducted: (1) Error vs sketch
  size for standard MinHash showing expected MSE decrease with increasing k, (2) Progressive estimation with rateless MinHash
  achieving 55-80% improvement rate, (3) Space efficiency comparison showing adaptive rateless uses ~853 bits vs fixed 1024+
  bits. An additional equal-bits comparison reveals that rateless MinHash trades some statistical efficiency (1.01-1.93x higher
  error) for the flexibility of progressive estimation and adaptive stopping. The output includes method.py with complete
  implementation, method_out.json with experiment results validated against exp_gen_sol_out schema, visualization plots, and
  comprehensive documentation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
</all_artifacts>

<new_artifacts_this_iteration>
These 3 artifacts were created THIS iteration.

id: art_9jz-SfB9wrwJ
type: research
title: Rateless MinHash Theory Foundations Research
summary: >-
  This research provides the theoretical foundations for Rateless MinHash, a novel sketching approach addressing the fundamental
  limitation of fixed sketch size in existing MinHash variants. Key findings include: (1) All current MinHash variants (Standard,
  b-bit, SetSketch, Odd Sketch, ProbMinHash) require upfront sketch size selection [1, 4, 6, 7, 8]. (2) Fountain codes (LT
  codes, Raptor codes) provide a proven rateless encoding framework where infinite symbol sequences can be generated with
  decoding possible from any slightly larger set [9, 10]. (3) The rate-distortion function for Jaccard similarity estimation
  remains undiscovered, though lower bounds exist from information complexity [3, 11, 12]. (4) A mathematical framework for
  Rateless MinHash is proposed, featuring encoding via degree-distributed hash generation, progressive decoding with decreasing
  variance O(1/k), and optimal stopping rules based on sequential estimation theory. The expected contribution is a sketch
  achieving near-optimal rate-distortion performance while adapting to diverse similarity regimes without upfront parameter
  tuning.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

id: art_ZpaiuGemkOnz
type: dataset
title: Near-Duplicate Text Datasets for MinHash Evaluation
summary: >-
  This artifact provides 6 text datasets (Quora, 20 Newsgroups, MS MARCO, C4, AG News, synthetic) with 30K total documents
  and 3.5K duplicate pairs. The datasets include diverse text types from short questions to long documents, with controlled
  Jaccard similarity levels (0.1, 0.3, 0.5, 0.7, 0.9). Each document is tokenized and includes metadata with source dataset,
  duplicate ID, and similarity level. The data supports evaluation of Rateless MinHash and baseline methods on near-duplicate
  detection and Jaccard similarity estimation tasks. File size is 46MB, under the 100MB limit.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

id: art_Q8_IBJsGhfEE
type: experiment
title: Progressive MinHash with Fountain Code Principles
summary: >-
  This experiment implements and evaluates a novel Rateless MinHash approach that uses fountain code principles (inspired
  by LT codes) to generate hash values progressively for adaptive Jaccard similarity estimation. The implementation includes
  StandardMinHash as baseline and RatelessMinHash as the novel method. Three experiments were conducted: (1) Error vs sketch
  size for standard MinHash showing expected MSE decrease with increasing k, (2) Progressive estimation with rateless MinHash
  achieving 55-80% improvement rate, (3) Space efficiency comparison showing adaptive rateless uses ~853 bits vs fixed 1024+
  bits. An additional equal-bits comparison reveals that rateless MinHash trades some statistical efficiency (1.01-1.93x higher
  error) for the flexibility of progressive estimation and adaptive stopping. The output includes method.py with complete
  implementation, method_out.json with experiment results validated against exp_gen_sol_out schema, visualization plots, and
  comprehensive documentation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# Rateless MinHash: Progressive Jaccard Estimation via Fountain Codes

## Abstract

MinHash and its variants require fixing the sketch size (number of hash functions) upfront, before knowing the desired estimation accuracy or the distribution of Jaccard similarities in the dataset. This leads to either wasted space (oversized sketches) or insufficient accuracy (undersized sketches). We propose **Rateless MinHash**, a novel sketching approach that applies fountain code principles to MinHash, enabling progressive Jaccard similarity estimation where hash values are generated on-demand and the sketch size adapts to the desired accuracy. Inspired by LT codes, our method generates a potentially infinite sequence of coded hash values, allowing estimates to improve monotonically as more values are processed. Evaluation on synthetic and real-world text datasets shows that Rateless MinHash achieves adaptive space-accuracy trade-offs: with progressive estimation, the method achieves 55-80% improvement in estimation error as more hash values are processed, and adaptive stopping reduces average space usage to ~853 bits compared to fixed 1024+ bits for standard MinHash. While the coding process introduces dependencies that reduce statistical efficiency by 1.01-1.93x compared to independent hashes, Rateless MinHash provides the first Progressive Jaccard estimation capability, enabling applications where the optimal sketch size is data-dependent or unknown beforehand.

**Keywords**: MinHash, Jaccard similarity, fountain codes, rateless codes, progressive estimation, sketching algorithms

## 1 Introduction

Estimating Jaccard similarity between sets is a fundamental operation in computer science, with applications in near-duplicate detection, clustering, recommendation systems, and graph analysis. Given two sets A and B, their Jaccard similarity is defined as J(A,B) = |A∩B| / |A∪B|, ranging from 0 (disjoint sets) to 1 (identical sets).

**The Problem**: MinHash, introduced by Broder [1], estimates Jaccard similarity by computing the probability that the minimum hash value under a random permutation is the same for both sets. The standard approach uses k independent hash functions, producing a sketch of size k. The variance of the estimator is Var[Ĵ] = J(1-J)/k, so the mean squared error (MSE) decreases as O(1/k) [1].

The critical limitation is that **the sketch size k must be fixed upfront**, before seeing the data. This creates a fundamental trade-off:
- If k is too small, the estimation error may be unacceptably high for the actual Jaccard similarities in the dataset.
- If k is too large, space is wasted, especially for sets with high Jaccard similarity where fewer hash functions suffice.

This problem is exacerbated in practice: datasets often have diverse Jaccard similarity distributions, and the optimal sketch size is data-dependent and unknown beforehand. Applications like distributed deduplication and streaming data would benefit from a sketch that can be refined progressively, using more space only when needed.

**Prior Solutions and Their Limitations**: Several MinHash variants attempt to address space efficiency, but all require fixed sketch sizes:
- **b-bit MinHash** [4] reduces storage by storing only the b lowest bits of each hash value, but the compression is lossy and irreversible.
- **SetSketch** [6] bridges MinHash and HyperLogLog with configurable parameters, but these parameters must be set before sketch construction.
- **Odd Sketch** [7] optimizes for high Jaccard similarities using binary sketches, but the sketch size must be fixed upfront.
- **ProbMinHash** [8] extends to weighted Jaccard similarity but produces fixed-size signatures.

**Our Approach**: We introduce **Rateless MinHash**, which applies fountain code principles to MinHash. Fountain codes (LT codes [9], Raptor codes [10]) are rateless erasure codes that can generate an infinite sequence of encoded symbols from a source message. The receiver can recover the original message after receiving any slightly larger set of encoded symbols.

The key insight is that MinHash sketches can be viewed as encoded representations of sets, and by using coding-theoretic principles, we can make this encoding rateless. Our method:
1. Generates a sequence of coded hash values using a degree distribution inspired by LT codes
2. Preserves the MinHash property: the probability that two coded hash values match equals the Jaccard similarity
3. Enables progressive estimation: accuracy improves monotonically as more hash values are processed
4. Supports adaptive stopping: estimation can stop when the error is sufficiently low

**Contributions**:

1. **Novel Algorithm**: We present the first rateless MinHash algorithm that generates hash values on-demand using fountain code principles [ARTIFACT:art_Q8_IBJsGhfEE].

2. **Progressive Estimation**: We demonstrate that Jaccard similarity can be estimated progressively, with error decreasing as more coded hash values are processed. Experimental results show a 55-80% improvement rate in estimation error [ARTIFACT:art_Q8_IBJsGhfEE].

3. **Adaptive Space Efficiency**: We show that Rateless MinHash with adaptive stopping uses ~853 bits on average (±148), compared to fixed 1024+ bits for standard MinHash with equivalent accuracy [ARTIFACT:art_Q8_IBJsGhfEE].

4. **Theoretical Analysis**: We formalize the rate-distortion problem for Jaccard similarity estimation and discuss optimal stopping rules based on sequential estimation theory [ARTIFACT:art_9jz-SfB9wrwJ].

The remainder of this paper is organized as follows. Section 2 reviews related work. Section 3 describes the Rateless MinHash algorithm. Section 4 presents the experimental evaluation. Section 5 discusses limitations and future work. Section 6 concludes.

[FIGURE:fig1]

## 2 Related Work

### 2.1 MinHash and Its Variants

MinHash was introduced by Broder [1] for estimating Jaccard similarity between sets. The standard MinHash algorithm uses k independent random permutations and computes the minimum hash value for each permutation. The Jaccard similarity is estimated as the fraction of matching minimum hash values.

**b-bit MinHash** [4] reduces the storage cost by storing only the b lowest bits of each minhash value. The variance of the b-bit estimator is Var[Ĵ_b] = (1-J)/k · (J + 1/(2^b - 1)) [5]. While more space-efficient, the compression is lossy and the sketch cannot be refined after creation.

**SetSketch** [6] unifies MinHash and HyperLogLog into a single data structure with configurable parameters (m, b, a, q) that must be set before sketch construction. It provides estimators for both cardinality and Jaccard similarity but does not support progressive refinement.

**Odd Sketch** [7] is optimized for high Jaccard similarities using a binary sketch based on the parity (XOR) of hash values. The sketch size must be fixed upfront, and the estimator's accuracy depends on the fraction of 1s being bounded away from 1/2.

**ProbMinHash** [8] extends MinHash to weighted Jaccard similarity, generating a fixed-size signature of k hash values.

**One Permutation MinHash** [14] reduces the number of hash computations needed but still requires fixing k beforehand.

### 2.2 Fountain Codes

Fountain codes are rateless erasure codes that can generate an infinite sequence of encoded symbols. The receiver can recover the original message after receiving any slightly larger set of encoded symbols.

**LT Codes** [9] (Luby Transform) are the first practical fountain codes. Each encoding symbol is generated by: (1) choosing a degree d from distribution ρ(d), (2) selecting d distinct input symbols uniformly at random, (3) XORing these d symbols. The Robust Soliton distribution ensures successful decoding with high probability.

**Raptor Codes** [10] improve upon LT codes with linear-time encoding and decoding by applying a fixed-rate outer code before LT coding.

### 2.3 Rate-Distortion Theory

Rate-distortion theory [11, 12] studies the optimal trade-off between compression rate (bits per symbol) and resulting distortion (loss) in lossy data compression. For a Bernoulli(p) source with Hamming distortion, the rate-distortion function is R(D) = H_b(p) - H_b(D) for 0 ≤ D ≤ min(p, 1-p), where H_b is the binary entropy function.

For Jaccard similarity estimation, the rate-distortion function has not been derived, though lower bounds exist from information complexity [3]. Any sketch must use Ω((1-J)/(εJ)²) bits per set for estimating Jaccard similarity with relative error εJ [3, Theorem 1.2].

### 2.4 Progressive Estimation

Progressive estimation appears in sketching techniques for approximate query processing [15], where initial estimates improve with more data. However, no existing MinHash implementation uses a sequential stopping rule or enables progressive Jaccard estimation.

## 3 Methods

### 3.1 Standard MinHash Background

Standard MinHash estimates Jaccard similarity using k independent hash functions. For each hash function h_i, the minimum hash value for set A is m_i(A) = min_{x∈A} h_i(x). The Jaccard similarity is estimated as:

Ĵ = (1/k) · Σ_{i=1}^k 1[m_i(A) = m_i(B)]

where 1[·] is the indicator function. The estimator is unbiased with variance Var[Ĵ] = J(1-J)/k.

### 3.2 Rateless MinHash Algorithm

Our Rateless MinHash algorithm adapts fountain code principles to generate a potentially infinite sequence of hash values for progressive Jaccard estimation.

#### 3.2.1 Encoding

Given a set of elements, we first compute `num_base_hashes` base hash values using independent hash functions. Then, we generate coded hash values using the following process:

1. **Degree Sampling**: Sample a degree d from the Robust Soliton distribution ρ(d) (adapted from LT codes [9]).
2. **Element Selection**: Select d distinct base hashes uniformly at random.
3. **Coded Hash Generation**: Compute the coded hash value as the **minimum** of the selected base hash values (not XOR as in LT codes). This preserves the MinHash property.

The Robust Soliton distribution is computed as:
- τ(d) = R/(d·k) for d < k/R, plus a spike at d = k
- ρ(d) = 1/(d·(d-1)) for the ideal Soliton distribution
- μ(d) = (τ + ρ) / sum(τ + ρ)

where R = c·log(k/δ)·√k for constants c and δ.

**Algorithm 1** summarizes the encoding process.

```
Algorithm 1: Rateless MinHash Encoding
Input: Set S, number of base hashes k, random seed
Output: Infinite stream of coded hash values

1. Compute base hash values: for each i ∈ {1,...,k}, compute h_i(S) = min_{x∈S} hash_i(x)
2. Initialize index stream using Robust Soliton distribution
3. For j = 1, 2, ... (infinite):
   a. Sample degree d_j from μ(d)
   b. Select indices I_j = {i_1, ..., i_d_j} uniformly at random from {1,...,k}
   c. Compute coded hash: c_j = min_{i∈I_j} h_i(S)
   d. Yield c_j and I_j (indices must be shared between sets)
```

#### 3.2.2 Progressive Decoding

To estimate Jaccard similarity from two coded hash streams, we process hash values sequentially:

1. Initialize `matches = 0`
2. For each position i = 1, 2, ...:
   - If `coded_hash_i(A) == coded_hash_i(B)` (within floating-point tolerance), increment `matches`
   - Estimate Ĵ_i = matches / i
   - Compute running MSE if true Jaccard is known

The key property is that **the probability of a match at any position equals the Jaccard similarity**: Pr[c_i(A) = c_i(B)] = J(A,B). This preserves the MinHash property and ensures unbiased estimation.

#### 3.2.3 Adaptive Stopping Rule

Rateless MinHash enables adaptive stopping: we can stop processing hash values when the estimation error is sufficiently low. While the optimal stopping rule based on rate-distortion theory requires the rate-distortion function R(D) for Jaccard estimation (which is unknown), we can use heuristic stopping rules:

1. **Fixed Error Tolerance**: Stop when the confidence interval width falls below 2ε
2. **Sequential Probability Ratio Test (SPRT)**: Adapt SPRT to test whether |Ĵ - J| < ε
3. **Variance-Based Stopping**: Stop when the estimated variance falls below a threshold

In our experiments, we use a simple stopping rule based on the number of processed hash values reaching a target budget, which can be determined adaptively based on the application's accuracy requirements.

### 3.3 Theoretical Properties

**MinHash Property Preservation**: The coded hash values preserve the MinHash property because the minimum operation over a random subset of base hashes maintains the probability of collision equal to Jaccard similarity. Formally, if indices I are sampled uniformly at random, then Pr[min_{i∈I} h_i(A) = min_{i∈I} h_i(B)] = J(A,B).

**Variance Analysis**: The variance of the Rateless MinHash estimator after k coded hash values is more complex than standard MinHash due to dependencies introduced by the coding process. Let π_i be the indicator that coded hash i matches. Then Ĵ_k = (1/k) Σ_{i=1}^k π_i. The variance is:

Var[Ĵ_k] = (1/k²) [Σ_i Var[π_i] + 2 Σ_{i<j} Cov[π_i, π_j]]

The dependencies (non-zero covariance) arise because the same base hashes can be selected multiple times across different coded hash values. This is the cost of the rateless property: we trade some statistical efficiency for the ability to generate hash values on-demand.

**Space Complexity**: Rateless MinHash uses `num_base_hashes` base hash values, each requiring 32-64 bits. The adaptive stopping rule determines the actual number of coded hash values used, which can be less than `num_base_hashes` if high accuracy is achieved early.

[FIGURE:fig2]

## 4 Experiments

We evaluate Rateless MinHash on synthetic datasets and compare it against standard MinHash baselines. Our experiments address three questions:

1. How does the estimation error of Rateless MinHash compare to standard MinHash as the number of hash values increases?
2. Can Rateless MinHash achieve space efficiency through adaptive stopping?
3. What is the trade-off between the flexibility of progressive estimation and statistical efficiency?

### 4.1 Experimental Setup

**Datasets**: We use synthetic datasets with controlled Jaccard similarity [ARTIFACT:art_ZpaiuGemkOnz]. For each experiment, we generate set pairs with Jaccard similarity ranging from 0.1 to 0.9. Each experiment uses 50 set pairs.

**Baselines**: 
- **Standard MinHash** with fixed sketch sizes k ∈ {16, 32, 64, 128}

**Implementation**: Both Standard MinHash and Rateless MinHash are implemented in Python using NumPy and hashlib for hash computation [ARTIFACT:art_Q8_IBJsGhfEE]. Rateless MinHash uses `num_base_hashes = 128` and the Robust Soliton distribution for degree sampling.

**Metrics**:
- **Mean Squared Error (MSE)**: (Ĵ - J)², averaged over set pairs
- **Space (bits)**: Number of hash values used × bits per hash value (32 bits for float32)
- **Improvement Rate**: The percentage reduction in MSE as more hash values are processed

### 4.2 Experiment 1: Error vs Sketch Size (Standard MinHash)

We first verify that standard MinHash exhibits the expected O(1/k) MSE decrease. Figure 2 (left) shows the results:

- k=16: MSE = 0.0140 (std = 0.0210)
- k=32: MSE = 0.0056 (std = 0.0085)
- k=64: MSE = 0.0022 (std = 0.0025)
- k=128: MSE = 0.0011 (std = 0.0021)

The MSE decreases as expected, confirming the theoretical variance formula.

### 4.3 Experiment 2: Progressive Estimation (Rateless MinHash)

We evaluate whether Rateless MinHash enables progressive Jaccard estimation. For set pairs with true Jaccard similarities J ∈ {0.1, 0.3, 0.5, 0.7, 0.9}, we process up to 128 coded hash values and record the MSE at each step.

**Results**: Rateless MinHash successfully enables progressive estimation. The error decreases as more coded hash values are processed, with an improvement rate of 55-80% (measured as the reduction in MSE from the first 10 to 128 hash values).

Figure 2 (right) shows the progressive MSE curves for different true Jaccard values:
- J=0.1: Final MSE = 0.0017 after 128 hashes
- J=0.3: Final MSE = 0.0027 after 128 hashes
- J=0.5: Final MSE = 0.0053 after 128 hashes
- J=0.7: Final MSE = 0.0036 after 128 hashes
- J=0.9: Final MSE = 0.0016 after 128 hashes

The estimation error decreases monotonically for most Jaccard values, confirming that Rateless MinHash provides progressive refinement.

[FIGURE:fig3]

### 4.4 Experiment 3: Space Efficiency with Adaptive Stopping

We compare the space efficiency of standard MinHash (fixed sketch size) and Rateless MinHash (adaptive stopping). For Rateless MinHash, we simulate adaptive stopping by using a target error threshold and stopping when the estimated error falls below the threshold.

**Results**: 
- Standard MinHash uses fixed bits: 512 (k=16), 1024 (k=32), 2048 (k=64), or 4096 (k=128)
- Rateless MinHash with adaptive stopping uses ~853 bits on average (±148), achieving an average error of 0.0655

Compared to standard MinHash with k=32 (1024 bits, error=0.0559), Rateless MinHash uses less space but with slightly higher error. This demonstrates the adaptive trade-off: Rateless MinHash can achieve near-equivalent accuracy with less space on average.

### 4.5 Equal-Bits Comparison: Statistical Efficiency Trade-off

To understand the trade-off between progressive estimation flexibility and statistical efficiency, we compare Rateless MinHash and standard MinHash at equal bit budgets.

**Results**: At equal bit budgets, standard MinHash outperforms Rateless MinHash. The ratio of MSE (Rateless / Standard) ranges from 1.01 to 1.93 depending on the bit budget. This is expected: standard MinHash uses independent hash functions, while Rateless MinHash introduces dependencies via the coding process. The dependencies reduce statistical efficiency but enable progressive estimation.

This trade-off is analogous to the trade-off in fountain codes: LT codes introduce dependencies to achieve the rateless property, at the cost of some decoding overhead compared to ideal independent symbols.

[FIGURE:fig4]

### 4.6 Discussion of Results

The experimental results demonstrate that Rateless MinHash achieves its primary goal: **progressive Jaccard estimation with adaptive space-accuracy trade-offs**. The key findings are:

1. **Progressive Estimation Works**: The error decreases as more hash values are processed, with 55-80% improvement rates.

2. **Adaptive Stopping Saves Space**: Rateless MinHash with adaptive stopping uses ~853 bits on average, compared to fixed 1024+ bits for standard MinHash.

3. **Statistical Efficiency Trade-off**: Rateless MinHash trades 1.01-1.93x higher error for the flexibility of progressive estimation. This trade-off is acceptable in applications where the optimal sketch size is unknown or data-dependent.

**Limitation**: The current implementation uses the Robust Soliton distribution from LT codes, which may not be optimal for MinHash. The degree distribution affects the dependence structure between coded hash values and hence the statistical efficiency. Deriving an optimal degree distribution for Rateless MinHash is an open problem.

## 5 Discussion and Limitations

### 5.1 Theoretical Gap: Rate-Distortion Function for Jaccard Estimation

A key theoretical gap is the unknown rate-distortion function R(D) for Jaccard similarity estimation. Such a function would provide the optimal trade-off between sketch bits (rate) and estimation MSE (distortion). Currently, only lower bounds exist from information complexity [3]. Deriving R(D) for Jaccard estimation would enable optimal stopping rules for Rateless MinHash.

### 5.2 Computational Overhead

Rateless MinHash has higher computational overhead than standard MinHash. Generating each coded hash value requires: (1) sampling a degree from the Robust Soliton distribution, (2) selecting random indices, (3) computing the minimum over selected base hashes. In contrast, standard MinHash simply computes independent hash values. The overhead is acceptable for applications where estimation accuracy is more important than computation speed, but it may be prohibitive for very high-throughput scenarios.

### 5.3 Dependency Structure

The coding process introduces dependencies between coded hash values, reducing statistical efficiency. The dependency structure is determined by the degree distribution and the random index selection. A careful theoretical analysis of these dependencies and their effect on estimator variance is needed.

### 5.4 Future Work

1. **Optimal Degree Distribution**: Derive the optimal degree distribution for Rateless MinHash that minimizes the variance of the estimator while maintaining the rateless property.

2. **Raptor-Inspired Rateless MinHash**: Explore using Raptor codes (with linear-time encoding/decoding) instead of LT codes for improved computational efficiency.

3. **Real-World Evaluation**: Evaluate Rateless MinHash on real-world datasets for near-duplicate detection in web-scale corpora (e.g., The Pile, C4).

4. **Rate-Distortion Derivation**: Derive the rate-distortion function for Jaccard similarity estimation to enable theoretically optimal stopping rules.

5. **Multi-Set Extension**: Extend Rateless MinHash to estimate Jaccard similarities for multiple sets simultaneously, enabling clustering and near-duplicate group detection.

## 6 Conclusion

We have presented **Rateless MinHash**, the first MinHash variant that enables progressive Jaccard similarity estimation. By applying fountain code principles (inspired by LT codes), Rateless MinHash generates a potentially infinite sequence of coded hash values, allowing estimates to improve monotonically as more values are processed.

Experimental evaluation demonstrates that Rateless MinHash achieves:
- **Progressive estimation**: 55-80% improvement in MSE as more hash values are processed
- **Adaptive space efficiency**: ~853 bits average usage with adaptive stopping, compared to fixed 1024+ bits for standard MinHash
- **Reasonable trade-off**: 1.01-1.93x higher error than standard MinHash at equal bit budgets, in exchange for progressive estimation capability

While theoretical questions remain (rate-distortion function, optimal degree distribution), Rateless MinHash opens a new direction in sketching algorithms: **rateless sketches that adapt to the desired accuracy at estimation time rather than at sketch creation time**. This capability is valuable for distributed deduplication, streaming data, and applications where the optimal sketch size is data-dependent.

## Acknowledgments

[To be filled based on funding sources]

## References

[1] Broder, A. "On the resemblance and containment of documents." Proceedings of the Compression and Complexity of Sequences. 1997.

[2] Li, P. and König, A. "b-Bit minwise hashing." The Web Conference, 2009.

[3] Pagh, R., Stöckel, M., and Woodruff, D. P. "Is min-wise hashing optimal for summarizing set intersection?" 2014.

[4] Li, P. and König, A. "Theory and applications of b-bit minwise hashing." Communications of the ACM, 2011.

[5] Mitzenmacher, M., Pagh, R., and Pham, N. D. "Efficient estimation for high similarities using odd sketches." The Web Conference, 2014.

[6] Ertl, O. "SetSketch: Filling the Gap between MinHash and HyperLogLog." Proceedings of the VLDB Endowment, 2021.

[7] Mitzenmacher, M., Pagh, R., and Pham, N. D. "Efficient estimation for high similarities using odd sketches." The Web Conference, 2014.

[8] Ertl, O. "ProbMinHash - A Class of Locality-Sensitive Hash Algorithms for the (Probability) Jaccard Similarity." IEEE Transactions on Knowledge and Data Engineering, 2019.

[9] Luby, M. "LT codes." IEEE Transactions on Information Theory, 2002.

[10] Shokrollahi, A. "Raptor codes." IEEE Transactions on Information Theory, 2006.

[11] Cover, T. M. and Thomas, J. A. "Elements of Information Theory." Chapter 13: Rate Distortion Theory, 1991.

[12] Wikipedia contributors. "Rate-distortion theory." Wikipedia, 2023.

[13] Lai, T. L. "On optimal stopping problems in sequential hypothesis testing." Statistica Sinica, 1997.

[14] Motion, F. and others. "One Permutation MinHash." 2014.

[15] Cormode, G. and others. "Sketch Techniques for Approximate Query Processing." 2012.

---

**Bibliography (BibTeX)**

The following BibTeX entries are fetched from Semantic Scholar and should be saved to `references.bib` for LaTeX compilation:

```bibtex
@inproceedings{Li2009,
  author = {Ping Li and A. K{\"o}nig},
  booktitle = {The Web Conference},
  pages = {671-680},
  title = {b-Bit minwise hashing},
  year = {2009},
  doi = {10.1145/1772690.1772759}
}

@inproceedings{Ertl2021,
  author = {Otmar Ertl},
  booktitle = {Proceedings of the VLDB Endowment},
  journal = {ArXiv},
  title = {SetSketch: Filling the Gap between MinHash and HyperLogLog},
  volume = {abs/2101.00314},
  year = {2021},
  doi = {10.14778/3476249.3476276}
}

@inproceedings{Mitzenmacher2014,
  author = {M. Mitzenmacher and R. Pagh and Ninh D. Pham},
  booktitle = {The Web Conference},
  journal = {Proceedings of the 23rd international conference on World wide web},
  title = {Efficient estimation for high similarities using odd sketches},
  year = {2014},
  doi = {10.1145/2566486.2568017}
}

@inproceedings{Ertl2019,
  author = {Otmar Ertl},
  booktitle = {IEEE Transactions on Knowledge and Data Engineering},
  journal = {IEEE Transactions on Knowledge and Data Engineering},
  pages = {3491-3506},
  title = {ProbMinHash -- A Class of Locality-Sensitive Hash Algorithms for the (Probability) Jaccard Similarity},
  volume = {34},
  year = {2019},
  doi = {10.1109/tkde.2020.3021176}
}

@inproceedings{Shokrollahi2011,
  author = {A. Shokrollahi},
  booktitle = {IEEE Transactions on Information Theory},
  journal = {IEEE Transactions on Information Theory},
  pages = {2551-2567},
  title = {Raptor codes},
  volume = {52},
  year = {2011},
  doi = {10.1109/TIT.2006.874390}
}
```

**Note**: The full BibTeX file with all references (including Broder 1997 and Luby 2002, which need to be added manually) should be compiled from the references.bib file. For papers not found via Semantic Scholar, we provide verified bibliographic information based on the original sources.

[FIGURE:fig5]
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (rigor) The theoretical analysis is incomplete. The paper correctly claims that 'Pr[c_i(A) = c_i(B)] = J(A,B)' (the MinHash property holds for any single coded hash value), but fails to analyze the critical issue: the samples are NOT INDEPENDENT across positions. The Robust Soliton distribution and random index selection create dependencies - the same base hashes can be selected multiple times across different coded hash values. Section 3.3 states the variance formula with covariance terms Var[Ĵ_k] = (1/k²)[Σ_i Var[π_i] + 2Σ_{i<j} Cov[π_i, π_j]], but does NOT analyze or bound these covariance terms. This is the most important theoretical contribution missing from the paper.
  Action: Add theoretical analysis of the dependencies: (1) Derive E[π_i π_j] = Pr[match at both positions i and j]. This depends on the overlap in selected indices and the degree distribution. (2) Bound the covariance terms Cov[π_i, π_j] based on the degree distribution. (3) Show how this relates to the 1.01-1.93x MSE penalty observed in experiments. (4) Consider deriving the optimal degree distribution that minimizes total covariance while maintaining the rateless property.
- [MAJOR] (evidence) The experimental evaluation has multiple issues: (1) The paper claims 'The estimation error decreases monotonically for most Jaccard values' (Section 4.3), but the provided data shows NON-MONOTONIC behavior. For J=0.1, MSE goes from 0.0098 to 0.0249 (increase) from position 1 to 2. (2) The '55-80% improvement' claim references 'from the first 10 to 128 hash values' but the full_method_out.json only contains the first 10 MSE values, not 128. (3) Only synthetic datasets with 100-element sets are used - no real-world evaluation. (4) The high variance in early MSE values (e.g., J=0.5: MSE ranges from 0.038 to 0.253 in first 10 positions) suggests the method is unstable initially.
  Action: Fix the monotonic decrease claim - either show data supporting it (the current data contradicts it) or remove the claim. Provide complete MSE curves for all 128 hash values as promised. Evaluate on real-world datasets from artifact art_ZpaiuGemkOnz. Add error bars/confidence intervals to MSE curves to show variance. The non-monotonic behavior is expected with dependent samples - acknowledge and analyze this theoretically.
- [MAJOR] (novelty) The novelty is overstated. While applying fountain codes to MinHash is new, the idea of progressive estimation via sequential sampling is not novel in sketching (Cormode et al. 2012, 'Sketch Techniques for Approximate Query Processing'). The paper does not compare against simple adaptive baselines like iteratively adding more MinHash values. The dependency structure introduced by fountain codes may not be necessary for progressive estimation - simple independent sampling with adaptive stopping could achieve similar results.
  Action: Add a baseline that uses standard MinHash with sequential estimation: start with k=1, keep adding independent hash values until error estimate is sufficiently low. Compare this simple adaptive baseline against Rateless MinHash. If the simple baseline achieves similar space-accuracy trade-offs, then the fountain code complexity is not justified.
- [MAJOR] (methodology) The coding process uses min operation over selected base hashes, which is different from XOR in LT codes. The paper does not justify why min operation preserves the MinHash property better than XOR (or other aggregation functions). The choice of Robust Soliton distribution from LT codes is arbitrary - the optimal degree distribution for MinHash may be different. The paper acknowledges this as a limitation but does not provide any analysis or intuition.
  Action: Justify the design choices: (1) Why min operation over selected base hashes? Analyze alternative aggregation functions (mean, median, XOR). (2) Analyze how the degree distribution affects statistical efficiency. (3) Consider deriving an optimal degree distribution for Rateless MinHash, or at least provide heuristics. The current arbitrary choice of Robust Soliton weakens the methodology.
- [MINOR] (clarity) The paper has misleading claims in the abstract and introduction. '55-80% improvement in estimation error' is not compared to any baseline - it's the improvement from using 10 vs 128 hashes. The abstract also claims 'adaptive stopping reduces average space usage to ~853 bits compared to fixed 1024+ bits for standard MinHash' but the comparison is unfair: standard MinHash with k=32 uses 1024 bits and achieves LOWER error (0.0559) than Rateless MinHash (0.0655 error).
  Action: Revise misleading claims: (1) Change '55-80% improvement in estimation error' to '55-80% reduction in MSE from processing 10 to 128 coded hash values'. (2) Clarify that the space efficiency comparison is at different error levels. (3) Add a fair comparison table: for similar error levels, compare space usage. The current presentation overstates the benefits.
- [MINOR] (scope) The paper's scope is limited. It only addresses Jaccard similarity for sets (not weighted sets, not other similarity measures). The application to distributed deduplication and streaming data is mentioned but not evaluated. The computational overhead analysis (Section 5.2) is qualitative - no actual runtime measurements are provided.
  Action: Expand the evaluation scope: (1) Measure and report computational overhead compared to standard MinHash. (2) Evaluate on at least one application scenario (distributed deduplication or streaming). (3) Discuss extension to weighted Jaccard (ProbMinHash) as future work. This would strengthen the paper's scope and practical relevance.
- [MINOR] (rigor) The related work section misses some relevant references. 'One Permutation MinHash' [14] is cited but the reference is incomplete (author 'Motion, F. and others' - should be 'Li, P. et al.'). The paper also does not discuss 'Weighted MinHash' or 'Densified One Permutation MinHash' which are relevant variants. The discussion of rate-distortion theory cites Wikipedia and a PDF link, not the original Shannon 1948 paper or relevant information theory textbooks.
  Action: Complete and verify all references. Add discussion of Weighted MinHash and Densified One Permutation MinHash in related work. Cite original sources for rate-distortion theory (Shannon 1948, or Cover & Thomas textbook). Ensure all citations are accurate and complete.
</reviewer_feedback>



<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_1/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); may be unchanged if still accurate.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_1/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-03 18:34:45 UTC

```
A simple and efficient MinHash-based method for detecting near-duplicate text passages in large corpora.
```

### [3] SYSTEM-USER prompt · 2026-07-03 18:35:27 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Narrowing scope: focusing on dependency analysis and honest baseline comparison rather than claiming rate-distortion optimality.' is too long (at most 120 characters, got 128)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.sdk_openhands_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
