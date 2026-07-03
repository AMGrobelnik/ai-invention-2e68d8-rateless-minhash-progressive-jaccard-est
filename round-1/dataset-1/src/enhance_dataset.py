#!/usr/bin/env python3
"""Enhance dataset with additional near-duplicate pairs for evaluation."""

from loguru import logger
from pathlib import Path
import json
import random
import re
from typing import List, Dict, Any, Tuple

logger.remove()
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
logger.add(__import__('sys').stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")

def tokenize_text(text: str) -> List[str]:
    """Tokenize text into words."""
    return re.findall(r'\w+', text.lower())

def compute_jaccard(tokens1: List[str], tokens2: List[str]) -> float:
    """Compute Jaccard similarity between two token sets."""
    set1 = set(tokens1)
    set2 = set(tokens2)
    if not set1 or not set2:
        return 0.0
    return len(set1 & set2) / len(set1 | set2)

def create_near_duplicate_with_similarity(text: str, target_similarity: float) -> str:
    """Create a near-duplicate with approximately target Jaccard similarity."""
    tokens = tokenize_text(text)

    if len(tokens) < 10:
        return text

    # Determine how many tokens to keep
    num_tokens = len(tokens)
    num_keep = int(num_tokens * target_similarity)

    # Randomly keep some tokens and modify others
    random.seed(42)
    indices = list(range(num_tokens))
    random.shuffle(indices)

    new_tokens = tokens.copy()
    for i in range(num_tokens):
        if i not in indices[:num_keep]:
            # Modify this token
            if random.random() < 0.5:
                # Replace with similar token
                new_tokens[i] = f"modified_{random.randint(1, 1000)}"
            else:
                # Remove token (shift left)
                new_tokens[i] = None

    # Remove None values
    new_tokens = [t for t in new_tokens if t is not None]

    return ' '.join(new_tokens)

def add_near_duplicates_to_dataset(docs: List[Dict[str, Any]],
                                   dataset_name: str,
                                   num_pairs: int = 1000) -> List[Dict[str, Any]]:
    """Add near-duplicate pairs to a dataset."""
    logger.info(f"Adding near-duplicates to {dataset_name}...")

    # Filter docs from this dataset
    dataset_docs = [doc for doc in docs if doc['metadata']['source_dataset'] == dataset_name]

    if len(dataset_docs) < 10:
        logger.warning(f"Not enough documents in {dataset_name}")
        return []

    # Create near-duplicate pairs with various similarity levels
    similarity_levels = [0.1, 0.3, 0.5, 0.7, 0.9]
    new_docs = []

    random.seed(42)
    for i, doc in enumerate(dataset_docs[:num_pairs]):
        if i >= num_pairs:
            break

        # Create original document entry with duplicate_id
        original_doc = doc.copy()
        original_doc['metadata'] = doc['metadata'].copy()
        original_doc['metadata']['duplicate_id'] = f"{doc['id']}_duplicate"
        new_docs.append(original_doc)

        # Create near-duplicate with random similarity
        target_sim = random.choice(similarity_levels)
        duplicate_text = create_near_duplicate_with_similarity(doc['text'], target_sim)

        duplicate_doc = {
            'id': f"{doc['id']}_duplicate",
            'text': duplicate_text,
            'tokens': tokenize_text(duplicate_text),
            'metadata': {
                'source_dataset': dataset_name,
                'duplicate_id': doc['id'],
                'similarity_level': f"jaccard_{target_sim}",
                'document_length': len(duplicate_text.split()),
                'target_jaccard': target_sim
            }
        }
        new_docs.append(duplicate_doc)

    logger.info(f"  Added {len(new_docs)} documents ({len(new_docs)//2} pairs)")
    return new_docs

def main():
    """Enhance dataset with near-duplicate pairs."""
    logger.info("Loading dataset...")

    # Load existing dataset
    with open('data_out.json', 'r') as f:
        docs = json.load(f)

    logger.info(f"Original dataset: {len(docs)} documents")

    # Add near-duplicates to datasets that don't have them
    enhanced_docs = docs.copy()

    # Add to 20 newsgroups
    new_docs = add_near_duplicates_to_dataset(docs, '20_newsgroups', num_pairs=2000)
    enhanced_docs.extend(new_docs)

    # Add to MS MARCO
    new_docs = add_near_duplicates_to_dataset(docs, 'ms_marco', num_pairs=3000)
    enhanced_docs.extend(new_docs)

    # Add to C4
    new_docs = add_near_duplicates_to_dataset(docs, 'c4', num_pairs=1000)
    enhanced_docs.extend(new_docs)

    # Add to AG News
    new_docs = add_near_duplicates_to_dataset(docs, 'ag_news', num_pairs=2000)
    enhanced_docs.extend(new_docs)

    # Save enhanced dataset
    logger.info(f"\nSaving enhanced dataset with {len(enhanced_docs)} documents...")

    output_path = Path('data_out.json')
    output_path.write_text(json.dumps(enhanced_docs, indent=2))

    import os
    file_size = os.path.getsize(output_path) / (1024**2)
    logger.info(f"File size: {file_size:.2f}MB")

    if file_size > 300:
        logger.warning("File size exceeds 300MB! Need to subsample further.")
        # TODO: Implement further subsampling if needed

    logger.info("\n" + "=" * 60)
    logger.info("Dataset enhancement complete!")
    logger.info("=" * 60)

if __name__ == "__main__":
    main()
