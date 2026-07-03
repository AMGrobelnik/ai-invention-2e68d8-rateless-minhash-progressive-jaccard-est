#!/usr/bin/env python3
"""Dataset collection script for near-duplicate text detection evaluation.

This script collects and processes multiple text datasets suitable for evaluating
Rateless MinHash against baselines on near-duplicate detection and Jaccard similarity estimation.
"""

from loguru import logger
from pathlib import Path
import json
import re
import random
from datasets import load_dataset
import nltk
from sklearn.datasets import fetch_20newsgroups
from typing import List, Dict, Any

# Download NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

logger.remove()
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
logger.add(__import__('sys').stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")

def tokenize_text(text: str) -> List[str]:
    """Tokenize text into words."""
    return re.findall(r'\w+', text.lower())

def create_synthetic_near_duplicates(texts: List[str], num_pairs: int = 100) -> List[Dict[str, Any]]:
    """Create synthetic near-duplicate pairs with controlled Jaccard similarity."""
    documents = []
    doc_id = 0

    for text in texts[:num_pairs]:
        # Original document
        doc_id += 1
        tokens = tokenize_text(text)
        documents.append({
            'id': f'synthetic_{doc_id}',
            'text': text,
            'tokens': tokens,
            'metadata': {
                'source_dataset': 'synthetic',
                'duplicate_id': f'synthetic_{doc_id}_duplicate',
                'similarity_level': 'original',
                'document_length': len(tokens)
            }
        })

        # Create near-duplicate with modifications
        doc_id += 1
        modified_tokens = tokens.copy()
        num_modifications = random.randint(1, max(1, len(modified_tokens) // 3))

        for _ in range(num_modifications):
            if random.random() < 0.5 and len(modified_tokens) > 10:
                # Remove a token
                idx = random.randint(0, len(modified_tokens) - 1)
                modified_tokens.pop(idx)
            else:
                # Replace or add a token
                if random.random() < 0.5 and len(modified_tokens) > 10:
                    idx = random.randint(0, len(modified_tokens) - 1)
                    modified_tokens[idx] = f' modified_{random.randint(1, 1000)}'
                else:
                    idx = random.randint(0, len(modified_tokens))
                    modified_tokens.insert(idx, f'added_{random.randint(1, 1000)}')

        modified_text = ' '.join(modified_tokens)
        documents.append({
            'id': f'synthetic_{doc_id}',
            'text': modified_text,
            'tokens': modified_tokens,
            'metadata': {
                'source_dataset': 'synthetic',
                'duplicate_id': f'synthetic_{doc_id - 1}',
                'similarity_level': 'near_duplicate',
                'document_length': len(modified_tokens)
            }
        })

    return documents

def process_quora_dataset() -> List[Dict[str, Any]]:
    """Process Quora duplicate questions dataset."""
    logger.info("Processing Quora dataset...")
    documents = []
    doc_id = 0

    try:
        dataset = load_dataset('sentence-transformers/quora-duplicates', 'pair-class', split='train')
        logger.info(f"Loaded Quora dataset with {len(dataset)} pairs")

        for item in dataset:
            # Process sentence1
            doc_id += 1
            tokens = tokenize_text(item['sentence1'])
            documents.append({
                'id': f'quora_{doc_id}',
                'text': item['sentence1'],
                'tokens': tokens,
                'metadata': {
                    'source_dataset': 'quora',
                    'duplicate_id': f'quora_{doc_id + 1}' if item['label'] == 1 else None,
                    'similarity_level': 'duplicate' if item['label'] == 1 else 'different',
                    'document_length': len(tokens),
                    'label': item['label']
                }
            })

            # Process sentence2
            doc_id += 1
            tokens = tokenize_text(item['sentence2'])
            documents.append({
                'id': f'quora_{doc_id}',
                'text': item['sentence2'],
                'tokens': tokens,
                'metadata': {
                    'source_dataset': 'quora',
                    'duplicate_id': f'quora_{doc_id - 1}' if item['label'] == 1 else None,
                    'similarity_level': 'duplicate' if item['label'] == 1 else 'different',
                    'document_length': len(tokens),
                    'label': item['label']
                }
            })

    except Exception as e:
        logger.error(f"Error processing Quora dataset: {e}")

    return documents

def process_20_newsgroups() -> List[Dict[str, Any]]:
    """Process 20 Newsgroups dataset."""
    logger.info("Processing 20 Newsgroups dataset...")
    documents = []

    try:
        newsgroups = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'))
        logger.info(f"Loaded 20 Newsgroups with {len(newsgroups.data)} documents")

        for i, (text, label) in enumerate(zip(newsgroups.data, newsgroups.target)):
            tokens = tokenize_text(text)
            documents.append({
                'id': f'newsgroups_{i}',
                'text': text,
                'tokens': tokens,
                'metadata': {
                    'source_dataset': '20_newsgroups',
                    'duplicate_id': None,
                    'similarity_level': None,
                    'document_length': len(tokens),
                    'label': int(label),
                    'label_text': newsgroups.target_names[label]
                }
            })

    except Exception as e:
        logger.error(f"Error processing 20 Newsgroups: {e}")

    return documents

def process_ms_marco() -> List[Dict[str, Any]]:
    """Process MS MARCO dataset."""
    logger.info("Processing MS MARCO dataset...")
    documents = []

    try:
        dataset = load_dataset('microsoft/ms_marco', 'v1.1', split='train', streaming=True)
        logger.info("Streaming MS MARCO dataset")

        for i, item in enumerate(dataset):
            if i >= 10000:  # Limit to 10K passages
                break

            # MS MARCO has passages
            if 'passages' in item:
                for j, passage in enumerate(item['passages']['passage_text'][:3]):  # Take first 3 passages
                    tokens = tokenize_text(passage)
                    documents.append({
                        'id': f'msmarco_{i}_{j}',
                        'text': passage,
                        'tokens': tokens,
                        'metadata': {
                            'source_dataset': 'ms_marco',
                            'duplicate_id': None,
                            'similarity_level': None,
                            'document_length': len(tokens),
                            'query_id': item.get('query_id', None)
                        }
                    })

    except Exception as e:
        logger.error(f"Error processing MS MARCO: {e}")

    return documents

def process_c4_subset(num_docs: int = 5000) -> List[Dict[str, Any]]:
    """Process C4 dataset subset."""
    logger.info(f"Processing C4 dataset (subset of {num_docs} docs)...")
    documents = []

    try:
        dataset = load_dataset('allenai/c4', 'en', split='train', streaming=True)
        logger.info("Streaming C4 dataset")

        for i, item in enumerate(dataset):
            if i >= num_docs:
                break

            text = item.get('text', '')
            tokens = tokenize_text(text)
            documents.append({
                'id': f'c4_{i}',
                'text': text,
                'tokens': tokens,
                'metadata': {
                    'source_dataset': 'c4',
                    'duplicate_id': None,
                    'similarity_level': None,
                    'document_length': len(tokens),
                    'timestamp': item.get('timestamp', None)
                }
            })

    except Exception as e:
        logger.error(f"Error processing C4: {e}")

    return documents

def process_ag_news() -> List[Dict[str, Any]]:
    """Process AG News dataset."""
    logger.info("Processing AG News dataset...")
    documents = []

    try:
        dataset = load_dataset('fancyzhx/ag_news', split='train')
        logger.info(f"Loaded AG News with {len(dataset)} documents")

        for i, item in enumerate(dataset):
            text = item['text']
            tokens = tokenize_text(text)
            documents.append({
                'id': f'agnews_{i}',
                'text': text,
                'tokens': tokens,
                'metadata': {
                    'source_dataset': 'ag_news',
                    'duplicate_id': None,
                    'similarity_level': None,
                    'document_length': len(tokens),
                    'label': item['label']
                }
            })

    except Exception as e:
        logger.error(f"Error processing AG News: {e}")

    return documents

def main():
    """Main function to collect and process all datasets."""
    logger.info("Starting dataset collection for near-duplicate text detection")

    all_documents = []

    # Process each dataset
    logger.info("=" * 60)
    logger.info("Processing datasets...")
    logger.info("=" * 60)

    # 1. Quora Duplicate Questions
    quora_docs = process_quora_dataset()
    logger.info(f"Quora: {len(quora_docs)} documents")
    all_documents.extend(quora_docs)

    # 2. 20 Newsgroups
    newsgroups_docs = process_20_newsgroups()
    logger.info(f"20 Newsgroups: {len(newsgroups_docs)} documents")
    all_documents.extend(newsgroups_docs)

    # 3. MS MARCO (subset)
    msmarco_docs = process_ms_marco()
    logger.info(f"MS MARCO: {len(msmarco_docs)} documents")
    all_documents.extend(msmarco_docs)

    # 4. C4 (subset)
    c4_docs = process_c4_subset(num_docs=5000)
    logger.info(f"C4: {len(c4_docs)} documents")
    all_documents.extend(c4_docs)

    # 5. AG News
    agnews_docs = process_ag_news()
    logger.info(f"AG News: {len(agnews_docs)} documents")
    all_documents.extend(agnews_docs)

    # 6. Synthetic near-duplicates
    logger.info("Creating synthetic near-duplicate documents...")
    sample_texts = [doc['text'] for doc in all_documents if len(doc['text']) > 100][:500]
    synthetic_docs = create_synthetic_near_duplicates(sample_texts, num_pairs=1000)
    logger.info(f"Synthetic: {len(synthetic_docs)} documents")
    all_documents.extend(synthetic_docs)

    # Save merged dataset
    logger.info("=" * 60)
    logger.info("Saving merged dataset...")
    logger.info("=" * 60)

    output_path = Path('data_out.json')
    output_path.write_text(json.dumps(all_documents, indent=2))
    logger.info(f"Saved {len(all_documents)} total documents to {output_path}")

    # Create dataset summary
    summary = {
        'total_documents': len(all_documents),
        'datasets': {
            'quora': len(quora_docs),
            '20_newsgroups': len(newsgroups_docs),
            'ms_marco': len(msmarco_docs),
            'c4': len(c4_docs),
            'ag_news': len(agnews_docs),
            'synthetic': len(synthetic_docs)
        },
        'total_tokens': sum(len(doc['tokens']) for doc in all_documents),
        'avg_document_length': sum(doc['metadata']['document_length'] for doc in all_documents) / len(all_documents)
    }

    summary_path = Path('dataset_summary.json')
    summary_path.write_text(json.dumps(summary, indent=2))
    logger.info(f"Saved dataset summary to {summary_path}")

    logger.info("=" * 60)
    logger.info("Dataset collection complete!")
    logger.info("=" * 60)

if __name__ == "__main__":
    main()
