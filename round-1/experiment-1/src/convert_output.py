#!/usr/bin/env python3
"""
Convert experiment results to exp_gen_sol_out schema format.
"""
import json
from pathlib import Path

# Load original results
with open('method_out.json', 'r') as f:
    results = json.load(f)

# Convert to exp_gen_sol_out format
output = {
    "metadata": {
        "method_name": "Rateless MinHash",
        "description": "Progressive MinHash with Fountain Code Principles",
        "experiments": ["error_vs_sketch", "progressive_estimation", "space_efficiency"],
        "parameters": {
            "k_values": [16, 32, 64, 128],
            "max_stream_len": 128,
            "num_base_hashes": 128,
            "num_pairs": 50,
            "set_size": 100
        }
    },
    "datasets": []
}

# Convert experiment 1 results
exp1_examples = []
for k, data in results['experiment_1']['results'].items():
    mse_val = data['mse']
    std_val = data['std']
    exp1_examples.append({
        "input": f"Standard MinHash with k={k}",
        "output": f"MSE={mse_val:.6f}, std={std_val:.6f}",
        "metadata_k": int(k),
        "metadata_mse": mse_val,
        "metadata_std": std_val
    })

output["datasets"].append({
    "dataset": "experiment_1_error_vs_sketch",
    "examples": exp1_examples
})

# Convert experiment 2 results
exp2_examples = []
for j, data in results['experiment_2']['results'].items():
    mse_curve = data['mse_curve']
    estimate_curve = data['estimate_curve']
    final_mse = mse_curve[-1]
    exp2_examples.append({
        "input": f"Rateless MinHash progressive estimation for true Jaccard={j}",
        "output": f"Final MSE={final_mse:.6f}",
        "metadata_target_jaccard": float(j),
        "metadata_final_mse": final_mse,
        "metadata_mse_curve": mse_curve[:10],
        "metadata_estimate_curve": estimate_curve[:10]
    })

output["datasets"].append({
    "dataset": "experiment_2_progressive_estimation",
    "examples": exp2_examples
})

# Convert experiment 3 results
exp3_examples = []

# Standard MinHash results
for k, data in results['experiment_3']['results']['standard'].items():
    avg_error = data['avg_error']
    avg_bits = data['avg_bits']
    exp3_examples.append({
        "input": f"Standard MinHash with k={k}",
        "output": f"Avg error={avg_error:.4f}, Bits={avg_bits}",
        "predict_baseline": f"error={avg_error:.4f}",
        "metadata_k": int(k),
        "metadata_avg_error": avg_error,
        "metadata_avg_bits": avg_bits
    })

# Rateless MinHash results
rtl_data = results['experiment_3']['results']['rateless']
rtl_avg_error = rtl_data['avg_error']
rtl_avg_bits = rtl_data['avg_bits']
rtl_bits_std = rtl_data['bits_std']
exp3_examples.append({
    "input": "Rateless MinHash with adaptive stopping",
    "output": f"Avg error={rtl_avg_error:.4f}, Avg bits={rtl_avg_bits:.1f}",
    "predict_our_method": f"error={rtl_avg_error:.4f}",
    "metadata_avg_error": rtl_avg_error,
    "metadata_avg_bits": rtl_avg_bits,
    "metadata_bits_std": rtl_bits_std
})

output["datasets"].append({
    "dataset": "experiment_3_space_efficiency",
    "examples": exp3_examples
})

# Write converted output
Path("method_out.json").write_text(json.dumps(output, indent=2))
print("Converted output written to method_out.json")
