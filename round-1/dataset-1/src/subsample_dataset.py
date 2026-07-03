#!/usr/bin/env python3
"""Subsample the dataset to reduce file size under 300MB."""

from loguru import logger
from pathlib import Path
import json
import random
import os

logger.remove()
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
logger.add(__import__('sys').stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")

def main():
    """Subsample dataset to meet size requirements."""
    logger.info("Loading full dataset...")
    with open('data_out.json', 'r') as f:
        all_docs = json.load(f)

    logger.info(f"Total documents: {len(all_docs)}")

    # Group by source dataset
    datasets = {}
    for doc in all_docs:
        source = doc['metadata']['source_dataset']
        if source not in datasets:
            datasets[source] = []
        datasets[source].append(doc)

    # Sample to target ~250MB (leaving buffer)
    sampled_docs = []
    target_per_dataset = {
        'quora': 50000,  # Reduce from 808K
        '20_newsgroups': 11314,  # Keep all
        'ms_marco': 29994,  # Keep all
        'c4': 5000,  # Keep all
        'ag_news': 50000,  # Reduce from 120K
        'synthetic': 1000  # Keep all
    }

    random.seed(42)
    for source, docs in datasets.items():
        num_sample = min(len(docs), target_per_dataset.get(source, len(docs)))
        sampled = random.sample(docs, num_sample)
        sampled_docs.extend(sampled)
        logger.info(f"{source}: kept {len(sampled)} from {len(docs)}")

    # Save subsampled dataset
    output_path = Path('data_out.json')
    output_path.write_text(json.dumps(sampled_docs, indent=2))
    logger.info(f"Saved {len(sampled_docs)} documents to {output_path}")

    file_size = os.path.getsize(output_path) / (1024**2)
    logger.info(f"File size: {file_size:.2f}MB")

    # Update dataset summary
    summary = {
        'total_documents': len(sampled_docs),
        'datasets': {source: len([d for d in sampled_docs if d['metadata']['source_dataset'] == source])
                     for source in datasets.keys()},
        'total_tokens': sum(len(doc['tokens']) for doc in sampled_docs),
        'avg_document_length': sum(doc['metadata']['document_length'] for doc in sampled_docs) / len(sampled_docs),
        'file_size_mb': file_size
    }

    summary_path = Path('dataset_summary.json')
    summary_path.write_text(json.dumps(summary, indent=2))
    logger.info(f"Updated dataset summary")

if __name__ == "__main__":
    main()
