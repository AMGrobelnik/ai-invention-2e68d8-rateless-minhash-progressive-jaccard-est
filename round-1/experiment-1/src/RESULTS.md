# Rateless MinHash Experiment Results

## Summary

This experiment implements and evaluates a novel "Rateless MinHash" approach that uses fountain code principles (inspired by LT codes) to generate hash values progressively for adaptive Jaccard similarity estimation.

## Key Findings

### Experiment 1: Error vs Sketch Size (Standard MinHash)
- Standard MinHash shows expected behavior: MSE decreases as k increases
- k=16: MSE = 0.0140
- k=32: MSE = 0.0056
- k=64: MSE = 0.0022
- k=128: MSE = 0.0011

### Experiment 2: Progressive Estimation (Rateless MinHash)
- Rateless MinHash successfully enables progressive estimation
- Error decreases as more coded hash values are processed (55-80% improvement rate)
- Final MSE after 128 hashes ranges from 0.0017 to 0.0053 depending on true Jaccard

### Experiment 3: Space Efficiency
- Standard MinHash uses fixed bits: 512, 1024, 2048, or 4096 bits
- Rateless MinHash with adaptive stopping uses ~853 bits on average (±148)
- Adaptive approach can reduce space usage compared to using large fixed sketches

### Equal-Bits Comparison
- At equal bit budgets, standard MinHash still outperforms rateless MinHash
- This is expected: standard MinHash uses independent hash functions, while rateless introduces dependencies via the coding process
- Ratio of errors (Rateless/Standard): 1.01 to 1.93 depending on bit budget

## Contributions

1. **Novel Algorithm**: First implementation of rateless MinHash using fountain code principles
2. **Progressive Estimation**: Demonstrated that Jaccard similarity can be estimated progressively
3. **Adaptive Stopping**: Showed that estimation can stop when error is sufficiently low

## Limitations

1. **Dependent Hashes**: The coding process introduces dependencies that reduce statistical efficiency
2. **Computational Overhead**: Generating coded hashes is more expensive than independent hashes
3. **Theoretical Gap**: The degree distribution from LT codes may not be optimal for MinHash

## Future Work

1. Derive optimal degree distribution specifically for MinHash (not borrowed from LT codes)
2. Explore other coding strategies (e.g., Raptor codes instead of LT codes)
3. Test on real-world datasets (not just synthetic)
4. Analyze theoretical variance bounds for rateless MinHash

## Files

- `method.py`: Complete implementation of StandardMinHash and RatelessMinHash
- `method_out.json`: Detailed experiment results
- `rateless_minhash_results.png`: Visualization of results
- `logs/run.log`: Full experiment log
