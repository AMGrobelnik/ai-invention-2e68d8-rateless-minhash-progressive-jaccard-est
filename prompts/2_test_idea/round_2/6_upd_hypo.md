# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_sAQsTTaaqjOV` — Rateless MinHash: Progressive Jaccard Estimation via Fountain Codes
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-03 19:34:12 UTC

````
<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: 'Rateless MinHash: Progressive Jaccard Estimation with Adaptive Stopping'
hypothesis: >-
  By generating MinHash values sequentially using a coded scheme inspired by fountain codes, we can create a MinHash variant
  that enables progressive Jaccard similarity estimation with adaptive stopping. The method trades statistical efficiency
  (1.01-1.93x higher MSE than independent hashes at equal bit budgets) for the ability to refine estimates on-demand without
  fixing sketch size upfront. The key theoretical challenge is analyzing the dependencies introduced by the coding process,
  which determine the variance penalty. The method is most useful in applications where the optimal sketch size is data-dependent
  and unknown beforehand, such as distributed deduplication with diverse similarity distributions.
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
_relation_rationale: >-
  Narrowing scope to dependency analysis and honest baseline comparison, not rate-distortion optimality.
_confidence_delta: decreased
_key_changes:
- >-
  Added honest acknowledgment of 1.01-1.93x statistical efficiency penalty from experiments
- >-
  Narrowed investigation approach: now includes comparing against simple adaptive baselines (sequential independent MinHash)
- >-
  Reframed contribution: from 'optimal rate-distortion' to 'analyzing dependency structure in progressive MinHash'
- >-
  Added theoretical analysis of dependencies as primary investigation goal (deriving E[π_i π_j] and covariance bounds)
- >-
  Clarified that the method's value depends on applications where progressive estimation justifies the efficiency penalty
- Added real-world evaluation on near-duplicate detection as success criterion
- >-
  Removed overstated claims about rate-distortion theory providing 'computable bound for optimal stopping' (function is unknown)
relation_type: evolution
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

--- Item 4 ---
id: art_50tMXu2lMfkc
type: proof
in_dependencies:
- id: art_9jz-SfB9wrwJ
  label: theory_background
title: Rateless MinHash MSE Penalty Proof
summary: >-
  This artifact provides a formally verified Lean 4 proof explaining the theoretical bounds for the MSE penalty observed in
  Rateless MinHash experiments (1.01-1.93x). The key result proved is that the penalty formula equals 1 + d²/k² where d is
  the degree and k is the number of base hashes. The proof uses simplified arithmetic bounds (avoiding complex probability
  theory) and was fully verified by the Lean 4 compiler with no 'sorry' placeholders remaining. The experimental range 1.01-1.93x
  corresponds to d/k ∈ [0.1, 0.96], which matches the degree distribution analysis in the paper.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_2/gen_art/gen_art_proof_1
out_expected_files:
- proof.lean
- proof_out.json

--- Item 5 ---
id: art_0XRo6tTpAffY
type: experiment
in_dependencies:
- id: art_ZpaiuGemkOnz
  label: datasets
title: Rateless MinHash vs Standard MinHash Evaluation
summary: |-
  This experiment comprehensively evaluates Rateless MinHash against Standard MinHash (baseline) on near-duplicate text detection tasks.

  Key components implemented:
  1. RatelessMinHash: Fountain code-inspired design with Robust Soliton degree distribution for progressive estimation
  2. StandardMinHash: Baseline with independent hash functions
  3. MSE curve computation with bootstrap confidence intervals
  4. Adaptive stopping experiment (fixed positions and CI-based)
  5. Aggregation function ablation (min, mean, median, xor)
  6. Non-monotonic behavior analysis (90% frequency observed)
  7. Near-duplicate detection evaluation across 6 datasets

  Results summary:
  - MSE curves: Both methods show decreasing MSE with more positions
  - Efficiency ratio: 0.972x (Rateless slightly better in this run)
  - Non-monotonicity: 90% frequency (expected due to dependencies in Rateless MinHash)
  - Aggregation: XOR performs best (MSE=0.1452 at position 16)
  - Near-duplicate detection: F1=1.000 at threshold 0.3

  The experiment validates the theoretical dependency penalty in Rateless MinHash while demonstrating practical utility for progressive estimation tasks. Output follows exp_gen_sol_out schema with 60 examples across 6 datasets.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
</all_artifacts>

<new_artifacts_this_iteration>
These 2 artifacts were created THIS iteration.

id: art_50tMXu2lMfkc
type: proof
in_dependencies:
- id: art_9jz-SfB9wrwJ
  label: theory_background
title: Rateless MinHash MSE Penalty Proof
summary: >-
  This artifact provides a formally verified Lean 4 proof explaining the theoretical bounds for the MSE penalty observed in
  Rateless MinHash experiments (1.01-1.93x). The key result proved is that the penalty formula equals 1 + d²/k² where d is
  the degree and k is the number of base hashes. The proof uses simplified arithmetic bounds (avoiding complex probability
  theory) and was fully verified by the Lean 4 compiler with no 'sorry' placeholders remaining. The experimental range 1.01-1.93x
  corresponds to d/k ∈ [0.1, 0.96], which matches the degree distribution analysis in the paper.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_2/gen_art/gen_art_proof_1
out_expected_files:
- proof.lean
- proof_out.json

id: art_0XRo6tTpAffY
type: experiment
in_dependencies:
- id: art_ZpaiuGemkOnz
  label: datasets
title: Rateless MinHash vs Standard MinHash Evaluation
summary: |-
  This experiment comprehensively evaluates Rateless MinHash against Standard MinHash (baseline) on near-duplicate text detection tasks.

  Key components implemented:
  1. RatelessMinHash: Fountain code-inspired design with Robust Soliton degree distribution for progressive estimation
  2. StandardMinHash: Baseline with independent hash functions
  3. MSE curve computation with bootstrap confidence intervals
  4. Adaptive stopping experiment (fixed positions and CI-based)
  5. Aggregation function ablation (min, mean, median, xor)
  6. Non-monotonic behavior analysis (90% frequency observed)
  7. Near-duplicate detection evaluation across 6 datasets

  Results summary:
  - MSE curves: Both methods show decreasing MSE with more positions
  - Efficiency ratio: 0.972x (Rateless slightly better in this run)
  - Non-monotonicity: 90% frequency (expected due to dependencies in Rateless MinHash)
  - Aggregation: XOR performs best (MSE=0.1452 at position 16)
  - Near-duplicate detection: F1=1.000 at threshold 0.3

  The experiment validates the theoretical dependency penalty in Rateless MinHash while demonstrating practical utility for progressive estimation tasks. Output follows exp_gen_sol_out schema with 60 examples across 6 datasets.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
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

MinHash and its variants require fixing the sketch size (number of hash functions) upfront, before knowing the desired estimation accuracy or the distribution of Jaccard similarities in the dataset. This leads to either wasted space (oversized sketches) or insufficient accuracy (undersized sketches). We propose **Rateless MinHash**, a novel sketching approach that applies fountain code principles to MinHash, enabling progressive Jaccard similarity estimation where hash values are generated on-demand. Inspired by LT codes, our method generates a potentially infinite sequence of coded hash values using a minimum-based aggregation over randomly selected base hashes. Evaluation on synthetic and real-world text datasets shows that: (1) Rateless MinHash enables progressive estimation with 55-80% reduction in mean squared error (MSE) when processing 128 hash values compared to using only 10; (2) adaptive stopping reduces average space usage to ~853 bits compared to fixed 1024+ bits for standard MinHash at comparable accuracy levels; (3) the method introduces dependencies between hash positions, resulting in 1.01-1.93x higher MSE than independent hashes at equal bit budgets. We provide a formal theoretical analysis explaining this efficiency penalty: the ratio equals 1 + d²/k² where d is the degree and k is the number of base hashes, verified through Lean 4 proofs. While simple adaptive baselines (sequentially adding independent MinHash values) can achieve similar space-accuracy trade-offs, Rateless MinHash provides a principled framework for progressive estimation with analyzable dependency structure.

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
2. Uses minimum operation over selected base hashes (preserving the MinHash property)
3. Enables progressive estimation: accuracy improves as more values are processed
4. Supports adaptive stopping: estimation can stop when sufficient accuracy is reached

**Key Theoretical Contribution**: Unlike standard MinHash which uses independent hash functions, Rateless MinHash introduces dependencies between coded hash values through the coding process. We provide a formal theoretical analysis of these dependencies, deriving the exact covariance structure. The analysis shows that the MSE ratio between Rateless MinHash and independent MinHash equals 1 + d²/k², where d is the degree and k is the number of base hashes. This result is verified through Lean 4 formal proofs [ARTIFACT:art_50tMXu2lMfkc].

**Contributions**:

1. **Novel Algorithm**: We present the first rateless MinHash algorithm that generates hash values on-demand using fountain code principles [ARTIFACT:art_Q8_IBJsGhfEE].

2. **Theoretical Analysis**: We derive the covariance structure of Rateless MinHash, proving that E[π_i π_j] = J² + O(d²/k²) and the MSE penalty equals 1 + d²/k², verified through formal Lean 4 proofs [ARTIFACT:art_50tMXu2lMfkc].

3. **Progressive Estimation**: We demonstrate that Jaccard similarity can be estimated progressively, with 55-80% reduction in MSE when processing 128 hash values compared to using only 10 [ARTIFACT:art_Q8_IBJsGhfEE].

4. **Adaptive Space Efficiency**: We show that Rateless MinHash with adaptive stopping uses ~853 bits on average (±148), compared to fixed 1024+ bits for standard MinHash with equivalent accuracy [ARTIFACT:art_Q8_IBJsGhfEE].

5. **Honest Baseline Comparison**: We compare against simple adaptive baselines (sequentially adding independent MinHash values) and analyze when the fountain code complexity is justified [ARTIFACT:art_0XRo6tTpAffY].

The remainder of this paper is organized as follows. Section 2 reviews related work. Section 3 describes the Rateless MinHash algorithm and provides theoretical analysis of the dependency structure. Section 4 presents the experimental evaluation on synthetic and real-world datasets. Section 5 discusses limitations and future work. Section 6 concludes.

[FIGURE:fig1]

## 2 Related Work

### 2.1 MinHash and Its Variants

MinHash was introduced by Broder [1] for estimating Jaccard similarity between sets. The standard MinHash algorithm uses k independent random permutations and computes the minimum hash value for each permutation. The Jaccard similarity is estimated as the fraction of matching minimum hash values.

**b-bit MinHash** [4] reduces the storage cost by storing only the b lowest bits of each minhash value. The variance of the b-bit estimator is Var[Ĵ_b] = (1-J)/k · (J + 1/(2^b - 1)) [5]. While more space-efficient, the compression is lossy and the sketch cannot be refined after creation.

**SetSketch** [6] unifies MinHash and HyperLogLog into a single data structure with configurable parameters (m, b, a, q) that must be set before sketch construction. It provides estimators for both cardinality and Jaccard similarity but does not support progressive refinement.

**Odd Sketch** [7] is optimized for high Jaccard similarities using a binary sketch based on the parity (XOR) of hash values. The sketch size must be fixed upfront, and the estimator's accuracy depends on the fraction of 1s being bounded away from 1/2.

**ProbMinHash** [8] extends MinHash to weighted Jaccard similarity, generating a fixed-size signature of k hash values.

**One Permutation MinHash** [14] reduces the number of hash computations needed but still requires fixing k beforehand.

**Densified One Permutation MinHash** [15] addresses the sparse sketch problem in one permutation MinHash by densifying the hash values.

### 2.2 Fountain Codes

Fountain codes are rateless erasure codes that can generate an infinite sequence of encoded symbols. The receiver can recover the original message after receiving any slightly larger set of encoded symbols.

**LT Codes** [9] (Luby Transform) are the first practical fountain codes. Each encoding symbol is generated by: (1) choosing a degree d from distribution ρ(d), (2) selecting d distinct input symbols uniformly at random, (3) XORing these d symbols. The Robust Soliton distribution ensures successful decoding with high probability.

**Raptor Codes** [10] improve upon LT codes with linear-time encoding and decoding by applying a fixed-rate outer code before LT coding.

### 2.3 Rate-Distortion Theory

Rate-distortion theory [11, 12] studies the optimal trade-off between compression rate (bits per symbol) and resulting distortion (loss) in lossy data compression. For a Bernoulli(p) source with Hamming distortion, the rate-distortion function is R(D) = H_b(p) - H_b(D) for 0 ≤ D ≤ min(p, 1-p), where H_b is the binary entropy function.

For Jaccard similarity estimation, the rate-distortion function has not been derived, though lower bounds exist from information complexity [3]. Any sketch must use Ω((1-J)/(εJ)²) bits per set for estimating Jaccard similarity with relative error εJ [3, Theorem 1.2].

### 2.4 Progressive Estimation and Adaptive Sketches

Progressive estimation appears in sketching techniques for approximate query processing [13], where initial estimates improve with more data. However, no existing MinHash implementation uses a sequential stopping rule or enables progressive Jaccard estimation with analyzable dependency structure.

**Weighted MinHash** schemes [16] extend MinHash to weighted sets but do not address the progressive estimation problem.

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

The choice of minimum operation is critical: it ensures that Pr[min_{i∈I} h_i(A) = min_{i∈I} h_i(B)] = J(A,B) for any random subset I, preserving the MinHash property. Alternative aggregation functions (mean, median, XOR) do not preserve this property [ARTIFACT:art_0XRo6tTpAffY].

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

### 3.3 Theoretical Analysis of Dependencies

**MinHash Property Preservation**: The coded hash values preserve the MinHash property because the minimum operation over a random subset of base hashes maintains the probability of collision equal to Jaccard similarity. Formally, if indices I are sampled uniformly at random, then Pr[min_{i∈I} h_i(A) = min_{i∈I} h_i(B)] = J(A,B).

**Dependency Structure**: Unlike standard MinHash which uses independent hash functions, Rateless MinHash introduces dependencies between coded hash values. Let π_i be the indicator that coded hash i matches. Then Ĵ_k = (1/k) Σ_{i=1}^k π_i. The variance is:

Var[Ĵ_k] = (1/k²) [Σ_i Var[π_i] + 2 Σ_{i<j} Cov[π_i, π_j]]

The dependencies (non-zero covariance) arise because the same base hashes can be selected multiple times across different coded hash values.

**Covariance Analysis**: We derive E[π_i π_j] = Pr[match at both positions i and j]. Let I_i and I_j be the randomly selected index sets at positions i and j, with degrees d_i and d_j. The probability of joint match depends on the overlap between I_i and I_j:

E[π_i π_j] = J^{|I_i ∪ I_j|/|I_i ∩ I_j|} ≈ J² · (1 + O(d²/k²))

where the approximation holds when d/k is small. The covariance is:

Cov[π_i, π_j] = E[π_i π_j] - J² = O(J² · d²/k²)

**MSE Penalty**: The ratio of MSE between Rateless MinHash and standard MinHash is:

MSE_ratio = Var[Rateless] / Var[Standard] = 1 + d²/k²

This result is formally verified using Lean 4 [ARTIFACT:art_50tMXu2lMfkc]. The experimental range 1.01-1.93x corresponds to d/k ∈ [0.1, 0.96], matching the degree distribution analysis.

**Proof Sketch**: The penalty formula MSE_ratio = 1 + d²/k² is derived by:
1. Bounding the total covariance sum: Σ_{i<j} Cov[π_i, π_j] = O(k · d²/k²)
2. Showing this adds d²/k² to the normalized variance
3. Verifying with concrete examples: d=1, k=10 → 1.01x; d=96, k=100 → 1.93x

[FIGURE:fig2]

### 3.4 Space Complexity

Rateless MinHash uses `num_base_hashes` base hash values, each requiring 32-64 bits. The adaptive stopping rule determines the actual number of coded hash values used, which can be less than `num_base_hashes` if high accuracy is achieved early.

## 4 Experiments

We evaluate Rateless MinHash on synthetic and real-world datasets and compare it against standard MinHash baselines. Our experiments address five questions:

1. How does the estimation error of Rateless MinHash compare to standard MinHash as the number of hash values increases?
2. Can Rateless MinHash achieve space efficiency through adaptive stopping?
3. What is the trade-off between the flexibility of progressive estimation and statistical efficiency?
4. How does Rateless MinHash compare to simple adaptive baselines?
5. What is the effect of different aggregation functions?

### 4.1 Experimental Setup

**Datasets**: We use synthetic datasets with controlled Jaccard similarity [ARTIFACT:art_ZpaiuGemkOnz] and real-world text datasets (Quora, MS MARCO, 20 Newsgroups, AG News, C4) with 60 total document pairs [ARTIFACT:art_0XRo6tTpAffY].

**Baselines**: 
- **Standard MinHash** with fixed sketch sizes k ∈ {16, 32, 64, 128}
- **Adaptive Independent MinHash**: Sequentially add independent hash values until error estimate stabilizes

**Implementation**: Both Standard MinHash and Rateless MinHash are implemented in Python using NumPy and hashlib for hash computation [ARTIFACT:art_Q8_IBJsGhfEE]. Rateless MinHash uses `num_base_hashes = 128` and the Robust Soliton distribution for degree sampling.

**Metrics**:
- **Mean Squared Error (MSE)**: (Ĵ - J)², averaged over set pairs
- **Space (bits)**: Number of hash values used × bits per hash value (32 bits for float32)
- **Improvement Rate**: The percentage reduction in MSE as more hash values are processed
- **Non-monotonicity Frequency**: Percentage of runs where MSE increases between consecutive positions

### 4.2 Experiment 1: Error vs Sketch Size (Standard MinHash)

We first verify that standard MinHash exhibits the expected O(1/k) MSE decrease. Figure 2 (left) shows the results:

- k=16: MSE = 0.0140 (std = 0.0210)
- k=32: MSE = 0.0056 (std = 0.0085)
- k=64: MSE = 0.0022 (std = 0.0025)
- k=128: MSE = 0.0011 (std = 0.0021)

The MSE decreases as expected, confirming the theoretical variance formula.

### 4.3 Experiment 2: Progressive Estimation (Rateless MinHash)

We evaluate whether Rateless MinHash enables progressive Jaccard estimation. For set pairs with true Jaccard similarities J ∈ {0.1, 0.3, 0.5, 0.7, 0.9}, we process up to 128 coded hash values and record the MSE at each step.

**Results**: Rateless MinHash successfully enables progressive estimation. The error decreases as more coded hash values are processed, with a 55-80% reduction in MSE from the first 10 to 128 hash values.

Figure 2 (right) shows the progressive MSE curves for different true Jaccard values:
- J=0.1: Final MSE = 0.0017 after 128 hashes (79% improvement)
- J=0.3: Final MSE = 0.0027 after 128 hashes (56% improvement)
- J=0.5: Final MSE = 0.0053 after 128 hashes (71% improvement)
- J=0.7: Final MSE = 0.0036 after 128 hashes (81% improvement)
- J=0.9: Final MSE = 0.0016 after 128 hashes (61% improvement)

**Non-Monotonic Behavior**: Due to dependencies between coded hash values, the MSE does not decrease monotonically. Our analysis shows that non-monotonic behavior occurs in 80-90% of runs [ARTIFACT:art_0XRo6tTpAffY]. This is expected: dependent samples produce higher variance in early estimates compared to independent samples. Figure 3 shows example MSE curves with confidence intervals illustrating this behavior.

[FIGURE:fig3]

### 4.4 Experiment 3: Space Efficiency with Adaptive Stopping

We compare the space efficiency of standard MinHash (fixed sketch size) and Rateless MinHash (adaptive stopping). For Rateless MinHash, we simulate adaptive stopping by using a target error threshold and stopping when the estimated error falls below the threshold.

**Results**: 
- Standard MinHash uses fixed bits: 512 (k=16), 1024 (k=32), 2048 (k=64), or 4096 (k=128)
- Rateless MinHash with adaptive stopping uses ~853 bits on average (±148), achieving an average error of 0.0655

Compared to standard MinHash with k=32 (1024 bits, error=0.0559), Rateless MinHash uses less space but with slightly higher error. This demonstrates the adaptive trade-off: Rateless MinHash can achieve near-equivalent accuracy with less space on average.

### 4.5 Equal-Bits Comparison: Statistical Efficiency Trade-off

To understand the trade-off between progressive estimation flexibility and statistical efficiency, we compare Rateless MinHash and standard MinHash at equal bit budgets.

**Results**: At equal bit budgets, standard MinHash outperforms Rateless MinHash. The ratio of MSE (Rateless / Standard) ranges from 1.01 to 1.93 depending on the bit budget (Table 1). This is expected: standard MinHash uses independent hash functions, while Rateless MinHash introduces dependencies via the coding process. The dependencies reduce statistical efficiency but enable progressive estimation.

**Theoretical vs Experimental**: The experimental ratios closely match our theoretical prediction of 1 + d²/k². For example, with d/k ≈ 0.1, the ratio is 1.01x; with d/k ≈ 0.96, the ratio is 1.93x [ARTIFACT:art_50tMXu2lMfkc].

| Bits | Standard Error | Rateless Error | Ratio |
|-------|----------------|----------------|-------|
| 512   | 0.0911 ± 0.0757 | 0.0915 ± 0.0599 | 1.01  |
| 1024  | 0.0559 ± 0.0494 | 0.0739 ± 0.0582 | 1.32  |
| 2048  | 0.0394 ± 0.0263 | 0.0659 ± 0.0481 | 1.67  |
| 4096  | 0.0241 ± 0.0227 | 0.0466 ± 0.0417 | 1.93  |

*Table 1: Equal-bits comparison showing MSE ratio (Rateless / Standard).*

### 4.6 Experiment 4: Comparison with Adaptive Baselines

A natural question is whether the complexity of fountain codes is necessary for progressive estimation. We compare Rateless MinHash against a simple adaptive baseline: **Adaptive Independent MinHash** which starts with k=1 and sequentially adds independent hash values until the error estimate stabilizes.

**Results**: The simple adaptive baseline achieves similar space-accuracy trade-offs to Rateless MinHash (efficiency ratio 0.972x in our experiments, meaning Rateless performed slightly better in this run) [ARTIFACT:art_0XRo6tTpAffY]. However, Rateless MinHash provides:
1. **Principled framework**: The dependency structure is analyzable through our theoretical framework
2. **Controlled degree distribution**: The Robust Soliton distribution provides predictable dependency patterns
3. **Potential for optimization**: Future work can derive optimal degree distributions for MinHash

**When is Rateless MinHash justified?** The fountain code complexity is justified when:
- Theoretical understanding of dependencies is important (e.g., for deriving optimal stopping rules)
- The degree distribution can be optimized for specific datasets or accuracy requirements
- Integration with other fountain code applications is needed

### 4.7 Experiment 5: Aggregation Function Ablation

We analyze the choice of aggregation function in the coding process. The method.py supports four aggregation functions: min, mean, median, and XOR.

**Results**: XOR aggregation achieves the best performance with MSE=0.1452 at position 16, followed by min (MSE=0.1837), median (MSE=0.1923), and mean (MSE=0.2108) [ARTIFACT:art_0XRo6tTpAffY]. However, XOR does not preserve the MinHash property (Pr[match] ≠ J), making it unsuitable for unbiased Jaccard estimation. The min operation is the only aggregation function that both preserves the MinHash property and achieves reasonable accuracy.

### 4.8 Near-Duplicate Detection Application

We evaluate Rateless MinHash on near-duplicate text detection across 6 real-world datasets. Using a threshold of 0.3 on estimated Jaccard similarity, both Rateless MinHash and Standard MinHash achieve F1=1.000 on the test sets [ARTIFACT:art_0XRo6tTpAffY].

**Computational Overhead**: Rateless MinHash has higher computational overhead than standard MinHash. Generating each coded hash value requires: (1) sampling a degree from the Robust Soliton distribution, (2) selecting random indices, (3) computing the minimum over selected base hashes. In our implementation, Rateless MinHash takes ~3x longer per hash value compared to standard MinHash. This overhead is acceptable for applications where estimation accuracy is more important than computation speed, but it may be prohibitive for very high-throughput scenarios.

[FIGURE:fig4]

### 4.9 Discussion of Results

The experimental results demonstrate that Rateless MinHash achieves its primary goal: **progressive Jaccard estimation with adaptive space-accuracy trade-offs**. The key findings are:

1. **Progressive Estimation Works**: The error decreases (on average) as more hash values are processed, with 55-80% improvement from 10 to 128 hash values.

2. **Adaptive Stopping Saves Space**: Rateless MinHash with adaptive stopping uses ~853 bits on average, compared to fixed 1024+ bits for standard MinHash.

3. **Statistical Efficiency Trade-off**: Rateless MinHash trades 1.01-1.93x higher error for the flexibility of progressive estimation. This trade-off is acceptable in applications where the optimal sketch size is unknown or data-dependent.

4. **Non-Monotonic Behavior**: Dependencies cause non-monotonic MSE curves in 80-90% of runs. This is expected and should be considered when using progressive estimation.

5. **Simple Baselines Competitive**: Adaptive independent MinHash achieves similar space-accuracy trade-offs, but lacks the analyzable dependency structure of Rateless MinHash.

**Limitation**: The current implementation uses the Robust Soliton distribution from LT codes, which may not be optimal for MinHash. The degree distribution affects the dependence structure between coded hash values and hence the statistical efficiency. Deriving an optimal degree distribution for Rateless MinHash is an open problem.

## 5 Discussion and Limitations

### 5.1 Theoretical Gap: Rate-Distortion Function for Jaccard Estimation

A key theoretical gap is the unknown rate-distortion function R(D) for Jaccard similarity estimation. Such a function would provide the optimal trade-off between sketch bits (rate) and estimation MSE (distortion). Currently, only lower bounds exist from information complexity [3]. Deriving R(D) for Jaccard estimation would enable optimal stopping rules for Rateless MinHash.

### 5.2 Computational Overhead

Rateless MinHash has higher computational overhead than standard MinHash. Generating each coded hash value requires: (1) sampling a degree from the Robust Soliton distribution, (2) selecting random indices, (3) computing the minimum over selected base hashes. In contrast, standard MinHash simply computes independent hash values. The overhead is acceptable for applications where estimation accuracy is more important than computation speed, but it may be prohibitive for very high-throughput scenarios.

### 5.3 Dependency Structure

The coding process introduces dependencies between coded hash values, reducing statistical efficiency. The dependency structure is determined by the degree distribution and the random index selection. A careful theoretical analysis of these dependencies and their effect on estimator variance is needed. Our work provides the first such analysis, showing the penalty equals 1 + d²/k².

### 5.4 Novelty Considerations

While applying fountain codes to MinHash is novel, the idea of progressive estimation via sequential sampling is not new in sketching [13]. Simple adaptive baselines (sequentially adding independent MinHash values) can achieve similar space-accuracy trade-offs. The contribution of Rateless MinHash is:
1. A principled framework for progressive estimation with analyzable dependencies
2. The first theoretical analysis of dependency structure in progressive MinHash
3. A foundation for future optimizations (optimal degree distribution, integration with other fountain code techniques)

### 5.5 Future Work

1. **Optimal Degree Distribution**: Derive the optimal degree distribution for Rateless MinHash that minimizes the variance of the estimator while maintaining the rateless property.

2. **Raptor-Inspired Rateless MinHash**: Explore using Raptor codes (with linear-time encoding/decoding) instead of LT codes for improved computational efficiency.

3. **Real-World Evaluation**: Evaluate Rateless MinHash on real-world datasets for near-duplicate detection in web-scale corpora (e.g., The Pile, C4).

4. **Rate-Distortion Derivation**: Derive the rate-distortion function for Jaccard similarity estimation to enable theoretically optimal stopping rules.

5. **Multi-Set Extension**: Extend Rateless MinHash to estimate Jaccard similarities for multiple sets simultaneously, enabling clustering and near-duplicate group detection.

6. **Hybrid Approaches**: Combine Rateless MinHash with simple adaptive baselines, using independent hashes initially and switching to coded hashes when more accuracy is needed.

## 6 Conclusion

We have presented **Rateless MinHash**, a MinHash variant that enables progressive Jaccard similarity estimation. By applying fountain code principles (inspired by LT codes), Rateless MinHash generates a potentially infinite sequence of coded hash values, allowing estimates to improve as more values are processed.

The key theoretical contribution is the analysis of dependencies introduced by the coding process. We prove that the MSE penalty equals 1 + d²/k², where d is the degree and k is the number of base hashes. This result is verified through both mathematical analysis and formal Lean 4 proofs.

Experimental evaluation demonstrates that Rateless MinHash achieves:
- **Progressive estimation**: 55-80% reduction in MSE from processing 10 to 128 coded hash values
- **Adaptive space efficiency**: ~853 bits average usage with adaptive stopping, compared to fixed 1024+ bits for standard MinHash
- **Reasonable trade-off**: 1.01-1.93x higher error than standard MinHash at equal bit budgets, in exchange for progressive estimation capability
- **Honest baseline comparison**: Similar performance to simple adaptive baselines, but with analyzable dependency structure

While theoretical questions remain (rate-distortion function, optimal degree distribution), Rateless MinHash opens a new direction in sketching algorithms: **rateless sketches that adapt to the desired accuracy at estimation time rather than at sketch creation time**. This capability is valuable for distributed deduplication, streaming data, and applications where the optimal sketch size is data-dependent.

**Reproducibility**: All code, data, and proofs are available as artifacts [ARTIFACT:art_Q8_IBJsGhfEE, art_50tMXu2lMfkc, art_0XRo6tTpAffY, art_ZpaiuGemkOnz].

## Acknowledgments

[To be filled based on funding sources]

## References

[1] Broder, A. "On the resemblance and containment of documents." Proceedings of the Compression and Complexity of Sequences. 1997.

[2] Li, P. and König, A. "b-Bit minwise hashing." The Web Conference, 2009.

[3] Pagh, R., Stöckel, M., and Woodruff, D. P. "Is min-wise hashing optimal for summarizing set intersection?" ACM SIGACT-SIGMOD-SIGART Symposium on Principles of Database Systems, 2014.

[4] Li, P. and König, A. "Theory and applications of b-bit minwise hashing." Communications of the ACM, 2011.

[5] Mitzenmacher, M., Pagh, R., and Pham, N. D. "Efficient estimation for high similarities using odd sketches." The Web Conference, 2014.

[6] Ertl, O. "SetSketch: Filling the Gap between MinHash and HyperLogLog." Proceedings of the VLDB Endowment, 2021.

[7] Mitzenmacher, M., Pagh, R., and Pham, N. D. "Efficient estimation for high similarities using odd sketches." The Web Conference, 2014.

[8] Ertl, O. "ProbMinHash -- A Class of Locality-Sensitive Hash Algorithms for the (Probability) Jaccard Similarity." IEEE Transactions on Knowledge and Data Engineering, 2019.

[9] Luby, M. "LT codes." IEEE Transactions on Information Theory, 2002.

[10] Shokrollahi, A. "Raptor codes." IEEE Transactions on Information Theory, 2006.

[11] Cover, T. M. and Thomas, J. A. "Elements of Information Theory." Chapter 13: Rate Distortion Theory, 1991.

[12] Wikipedia contributors. "Rate-distortion theory." Wikipedia, 2023.

[13] Cormode, G. et al. "Sketch Techniques for Approximate Query Processing." Foundations and Trends in Databases, 2012.

[14] Li, P. et al. "One Permutation MinHash." International Conference on Machine Learning, 2014.

[15] Shrivastava, A. "Densified One Permutation MinHash." ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2017.

[16] Ioffe, S. "Improved consistent sampling, weighted minhash and L1 sketching." IEEE International Conference on Data Mining, 2010.

---

**Bibliography (BibTeX)**

The following BibTeX entries are fetched from Semantic Scholar and should be saved to `references.bib` for LaTeX compilation:

```bibtex
@inproceedings{Pagh2014,
  author = {R. Pagh and Morten St\"{o}ckel and David P. Woodruff},
  booktitle = {ACM SIGACT-SIGMOD-SIGART Symposium on Principles of Database Systems},
  title = {Is min-wise hashing optimal for summarizing set intersection?},
  year = {2014},
  doi = {10.1145/2594538.2594554}
}

@inproceedings{Mitzenmacher2014,
  author = {M. Mitzenmacher and R. Pagh and Ninh D. Pham},
  booktitle = {The Web Conference},
  title = {Efficient estimation for high similarities using odd sketches},
  year = {2014},
  doi = {10.1145/2566486.2568017}
}

@inproceedings{Ertl2019,
  author = {Otmar Ertl},
  booktitle = {IEEE Transactions on Knowledge and Data Engineering},
  title = {ProbMinHash -- A Class of Locality-Sensitive Hash Algorithms for the (Probability) Jaccard Similarity},
  volume = {34},
  pages = {3491-3506},
  year = {2019},
  doi = {10.1109/tkde.2020.3021176}
}
```

**Note**: The full BibTeX file with all references should be compiled from the references.bib file. For papers not found via Semantic Scholar (Broder 1997, Luby 2002, Shokrollahi 2006, Cover & Thomas 1991), we provide verified bibliographic information based on the original sources.

[FIGURE:fig5]
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (evidence) The paper's central experimental claim is UNSUPPORTED by the provided data. The abstract and Section 4.3 claim '55-80% reduction in MSE when processing 128 hash values compared to using only 10'. However, the experimental data in full_method_out.json only contains the first 10 MSE values, not 128. The paper explicitly states 'from the first 10 to 128 hash values' but the data stops at 10. This is a critical issue - the flagship experimental result cannot be verified.
  Action: Provide complete experimental results for 128 hash positions. Run the experiment with max_stream_len=128 and include the full MSE curves in the paper. If 128 positions were not actually evaluated, revise the claim to only report results that are actually available (first 10 positions). The 55-80% improvement claim specifically references 'from 10 to 128' which requires data at position 128.
- [MAJOR] (rigor) The theoretical analysis in Section 3.3 is incomplete. The paper correctly identifies that dependencies introduce covariance terms: Var[Ĵ_k] = (1/k²)[Σ_i Var[π_i] + 2Σ_{i<j} Cov[π_i, π_j]]. However, it does NOT derive or bound these covariance terms. The paper states 'E[π_i π_j] = J^{|I_i ∪ I_j|/|I_i ∩ I_j|} ≈ J² · (1 + O(d²/k²))' but this approximation is not derived. The MSE penalty formula (1 + d²/k²) is stated without proof derivation in the paper (the Lean 4 proof only verifies arithmetic examples).
  Action: Complete the theoretical analysis by deriving the covariance bounds. Specifically: (1) Derive the exact formula for E[π_i π_j] based on index overlap. (2) Bound the sum of covariances Σ_{i<j} Cov[π_i, π_j]. (3) Show how this leads to the 1 + d²/k² penalty. The current section only states the result without derivation.
- [MAJOR] (novelty) The paper's contribution is weakened by the honest comparison with adaptive baselines (Section 4.6). The results show that 'Adaptive Independent MinHash' (simply adding independent hash values sequentially) achieves similar space-accuracy trade-offs (efficiency ratio 0.972x in the experiment). The paper acknowledges this but does not adequately address the question: when is the fountain code complexity justified? The contribution section (Section 1, Contributions) lists 'Novel Algorithm' and 'Theoretical Analysis' but the practical benefit over simple adaptive baselines is unclear.
  Action: Strengthen the justification for Rateless MinHash over simple adaptive baselines. Possible angles: (1) The analyzable dependency structure enables optimal stopping rules (derive one). (2) The degree distribution can be optimized for specific data distributions. (3) The framework enables integration with other fountain code techniques (Raptor codes for linear-time operations). Without a clear advantage, the fountain code complexity seems unnecessary.
- [MAJOR] (rigor) The Lean 4 'formal verification' is misleading. The proof in proof.lean only verifies two arithmetic identities: 1² + 10² = 101 and 96² + 100² = 19216. These are the examples mentioned in the paper, but they are NOT a verification of the MSE penalty formula 1 + d²/k². The actual theorem that needs verification is: Var[RatelessMinHash] / Var[StandardMinHash] = 1 + d²/k² (+ lower order terms). The current 'proof' does not verify any probabilistic bound.
  Action: Either: (1) Actually verify the MSE penalty formula in Lean 4 (this would require formalizing probability theory), or (2) Remove the claim of 'formal verification via Lean 4 proofs'. The current proof is misleading - it suggests theoretical bounds are formally verified when they are only arithmetic examples. If keeping the examples, frame them as 'illustrative examples' not 'verified proofs'.
- [MAJOR] (clarity) The space efficiency comparison in Section 4.4 and abstract is misleading. The paper claims 'adaptive stopping reduces average space usage to ~853 bits compared to fixed 1024+ bits for standard MinHash at comparable accuracy levels'. However, the actual numbers show: Rateless MinHash uses ~853 bits for error=0.0655, while Standard MinHash with k=32 uses 1024 bits for error=0.0559 (LOWER error). This is NOT 'comparable accuracy' - Standard MinHash achieves BETTER accuracy. The fair comparison would be at equal error levels or equal bit budgets.
  Action: Revise the space efficiency comparison to be fair: (1) Compare at EQUAL error levels: find the Standard MinHash k that achieves error≈0.0655 and compare bits. (2) Compare at EQUAL bit budgets: compare error for ~853 bits. (3) Alternatively, plot a trade-off curve (bits vs error) for both methods. The current comparison selects different operating points and claims one is better.
- [MINOR] (methodology) The choice of Robust Soliton distribution from LT codes is arbitrary. The paper acknowledges this ('may not be optimal for MinHash', Section 4.9 Limitation). However, there is no analysis of how the degree distribution affects the dependency structure or the MSE penalty. The Robust Soliton distribution is designed for erasure coding (ensuring successful decoding), not for minimizing variance in similarity estimation.
  Action: Add analysis of how degree distribution affects performance. Simulate different degree distributions (uniform, geometric, etc.) and compare their MSE. This would provide intuition for why Robust Soliton may or may not be appropriate, and guide future optimization. At minimum, acknowledge this gap more prominently in the limitations.
- [MINOR] (evidence) The non-monotonic behavior (MSE increasing between consecutive positions) is mentioned briefly but not analyzed in detail. The paper states it occurs in 80-90% of runs (Section 4.3, Experiment 2 results mention 90% frequency in art_0XRo6tTpAffY). This is expected due to dependencies, but a deeper analysis would strengthen the paper: quantify how often the MSE is non-monotonic, show distribution of non-monotonic jumps, analyze whether confidence intervals capture the true Jaccard despite non-monotonicity.
  Action: Expand the analysis of non-monotonic behavior: (1) Show the frequency and magnitude of non-monotonic increases across different Jaccard values. (2) Analyze whether confidence intervals (if computed) capture the true value despite non-monotonic point estimates. (3) Discuss implications for stopping rules - should stopping be based on point estimates or confidence intervals?
- [MINOR] (scope) The experimental evaluation uses small sets (100 elements) and only 50-60 document pairs. The paper would be stronger with: (1) Larger sets with more diverse Jaccard similarities, (2) Evaluation on downstream tasks (clustering, near-duplicate detection with real duplicates not just synthetic), (3) Comparison with other progressive estimation approaches from the sketching literature (Cormode et al. 2012 is cited but not compared).
  Action: Expand experimental evaluation: (1) Test on larger sets (1000+ elements) to verify theoretical predictions hold at scale. (2) Evaluate on a downstream task (e.g., near-duplicate detection F1 score as function of bits used). (3) Compare with progressive estimation from sketching literature (e.g., adaptive sampling approaches). This would strengthen the empirical contribution.
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

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json`

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

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-03 19:34:12 UTC

```
A simple and efficient MinHash-based method for detecting near-duplicate text passages in large corpora.
```
