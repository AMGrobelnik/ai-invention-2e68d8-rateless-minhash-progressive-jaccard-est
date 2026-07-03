# gen_paper_text — test_idea

> Phase: `invention_loop` · round 2 · `gen_paper_text`
> Run: `run_sAQsTTaaqjOV` — Rateless MinHash: Progressive Jaccard Estimation via Fountain Codes
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-03 19:24:45 UTC

````
<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-multi-llm-agents** — Guide for implementing Multi-LLM Agent Systems research using Mirascope orchestration, HuggingFace datasets/evaluation, and proven multi-agent patterns.
</available_domain_handbooks>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

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
</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

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

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

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
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 5 research artifacts across all iterations.

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
NEW THIS ITERATION: These 2 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

title: Rateless MinHash MSE Penalty Proof
id: art_50tMXu2lMfkc
type: proof
summary: >-
  This artifact provides a formally verified Lean 4 proof explaining the theoretical bounds for the MSE penalty observed in
  Rateless MinHash experiments (1.01-1.93x). The key result proved is that the penalty formula equals 1 + d²/k² where d is
  the degree and k is the number of base hashes. The proof uses simplified arithmetic bounds (avoiding complex probability
  theory) and was fully verified by the Lean 4 compiler with no 'sorry' placeholders remaining. The experimental range 1.01-1.93x
  corresponds to d/k ∈ [0.1, 0.96], which matches the degree distribution analysis in the paper.

title: Rateless MinHash vs Standard MinHash Evaluation
id: art_0XRo6tTpAffY
type: experiment
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
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison):
  {"id": "fig3", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: latency (seconds, 0-5). Values: PostgreSQL=4.6s (red), Bao=2.8s (blue), RLQOpt=2.0s (green). Error bars +/-0.3-0.8. Sans-serif font, white background.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero):
  {"id": "fig1", "title": "System Architecture", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "Detailed image generation prompt \u2014 axes, labels, ALL numeric values, colors, aspect ratio, layout. The image generator cannot read files; this is its ONLY input.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-03 19:24:45 UTC

```
A simple and efficient MinHash-based method for detecting near-duplicate text passages in large corpora.
```

### [3] SKILL-INPUT — aii-paper-writing · 2026-07-03 19:25:02 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: Academic paper writing guidance for AI research. Covers paper structure, figure placeholders, bibliography building with Semantic Scholar, and citation rules. Does NOT cover LaTeX compilation or figure file generation — see aii-paper-to-latex for that.
---

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-03 19:25:06 UTC

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
