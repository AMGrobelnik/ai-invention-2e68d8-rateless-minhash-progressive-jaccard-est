# Rateless MinHash Experiment

## Overview

This experiment implements and evaluates a novel **Rateless MinHash** approach that uses fountain code principles (inspired by LT codes) to generate hash values progressively for adaptive Jaccard similarity estimation.

## Hypothesis

By using fountain code principles (specifically, generating coded hash values by taking the minimum of randomly selected base hash functions), we can create a rateless MinHash scheme that:
1. Enables progressive Jaccard similarity estimation
2. Allows adaptive stopping when estimate is sufficiently accurate
3. Uses less space on average compared to fixed-size MinHash

## Implementation

### Files

- `method.py`: Complete implementation with:
  - `StandardMinHash`: Baseline fixed-k MinHash
  - `RatelessMinHash`: Novel rateless MinHash using fountain code principles
  - Synthetic dataset generation with controlled Jaccard similarity
  - Three experiments + equal-bits comparison

- `method_out.json`: Main experiment results (schema-compliant)
- `rateless_minhash_results.png`: Visualization of results
- `logs/run.log`: Full experiment log
- `RESULTS.md`: Detailed results summary

### Key Design Decisions

1. **Coding Strategy**: Instead of XOR (which doesn't preserve MinHash properties), we use the **minimum** of selected base hash values. This preserves the MinHash property that P(hash_match) = Jaccard.

2. **Shared Indices**: For valid Jaccard estimation, both sets must use the **same random indices** to select base hashes.

3. **Degree Distribution**: Uses Robust Soliton Distribution from LT codes (may not be optimal for MinHash - future work).

## Results

### Experiment 1: Error vs Sketch Size (Standard MinHash)
- As expected, MSE decreases with increasing k
- k=128 achieves MSE ≈ 0.0011

### Experiment 2: Progressive Estimation (Rateless MinHash)
- **Success**: Error decreases as more coded hash values are processed
- Improvement rates: 55-80% (varies by true Jaccard)
- Final MSE after 128 hashes: 0.0017-0.0053

### Experiment 3: Space Efficiency
- Adaptive rateless uses ~853 bits on average (±148)
- Comparable to standard MinHash with k=32 (1024 bits)

### Equal-Bits Comparison
- At equal bit budgets, standard MinHash still outperforms rateless
- Error ratio (Rateless/Standard): 1.01 to 1.93
- This is expected: coding introduces dependencies that reduce statistical efficiency

## Key Findings

1. **Progressive Estimation Works**: Rateless MinHash successfully enables progressive Jaccard estimation with decreasing error.

2. **Adaptive Stopping Potential**: The adaptive stopping approach shows promise for reducing average space usage.

3. **Trade-off Identified**: Rateless MinHash provides flexibility (progressive estimation, adaptive stopping) at the cost of some statistical efficiency.

## Limitations

1. **Dependent Hashes**: Coding introduces dependencies, reducing efficiency compared to independent hash functions.

2. **Suboptimal Degree Distribution**: Using Robust Soliton from LT codes may not be optimal for MinHash.

3. **Synthetic Data Only**: Not yet tested on real-world datasets.

## Future Work

1. Derive optimal degree distribution for MinHash (not borrowed from LT codes)
2. Explore other coding strategies (e.g., Raptor codes)
3. Test on real-world near-duplicate detection tasks
4. Theoretical analysis of variance bounds

## Usage

```bash
# Set up environment
uv venv .venv --python=3.12
source .venv/bin/activate
uv pip install numpy matplotlib loguru scipy

# Run experiment
python method.py

# Output files generated:
# - method_out.json (results in schema format)
# - rateless_minhash_results.png (plots)
# - logs/run.log (detailed log)
```

## Dependencies

- Python 3.12+
- numpy
- matplotlib
- loguru
- scipy
