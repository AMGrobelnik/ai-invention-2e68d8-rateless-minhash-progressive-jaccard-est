#!/usr/bin/env python3
"""Validate the collected dataset structure and duplicate pairs."""

from loguru import logger
from pathlib import Path
import json
from collections import defaultdict

logger.remove()
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
logger.add(__import__('sys').stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")

def main():
    """Validate dataset structure and duplicate pairs."""
    logger.info("Loading dataset for validation...")

    # Load dataset
    with open('data_out.json', 'r') as f:
        docs = json.load(f)

    logger.info(f"Total documents: {len(docs)}")

    # Create index for efficient lookup
    doc_index = {doc['id']: doc for doc in docs}

    # Check duplicate structure
    logger.info("\nChecking duplicate structure...")
    duplicate_pairs = []
    datasets_with_duplicates = defaultdict(int)
    datasets_total = defaultdict(int)

    for doc in docs:
        source = doc['metadata']['source_dataset']
        datasets_total[source] += 1

        dup_id = doc['metadata'].get('duplicate_id')
        if dup_id and dup_id in doc_index:
            duplicate_pairs.append((doc['id'], dup_id))
            datasets_with_duplicates[source] += 1

    logger.info(f"Total duplicate pairs: {len(duplicate_pairs)}")

    # Report by dataset
    logger.info("\nDuplicate statistics by dataset:")
    for source in datasets_total.keys():
        total = datasets_total[source]
        with_dups = datasets_with_duplicates.get(source, 0)
        logger.info(f"  {source}: {with_dups}/{total} documents have duplicates")

    # Sample duplicate pair
    if duplicate_pairs:
        logger.info("\nSample duplicate pair:")
        id1, id2 = duplicate_pairs[0]
        doc1 = doc_index[id1]
        doc2 = doc_index[id2]
        logger.info(f"  Doc 1 ({id1}): {doc1['text'][:100]}...")
        logger.info(f"  Doc 2 ({id2}): {doc2['text'][:100]}...")

    # Check tokenization
    logger.info("\nChecking tokenization...")
    empty_tokens = 0
    for doc in docs:
        if not doc.get('tokens'):
            empty_tokens += 1

    logger.info(f"Documents with empty tokens: {empty_tokens}")

    # Check metadata completeness
    logger.info("\nChecking metadata completeness...")
    required_fields = ['source_dataset', 'document_length']
    missing_fields = defaultdict(int)

    for doc in docs:
        for field in required_fields:
            if field not in doc['metadata']:
                missing_fields[field] += 1

    if missing_fields:
        logger.warning("Missing metadata fields:")
        for field, count in missing_fields.items():
            logger.warning(f"  {field}: {count} documents")
    else:
        logger.info("All required metadata fields present")

    # Create validation report
    report = {
        'total_documents': len(docs),
        'duplicate_pairs': len(duplicate_pairs),
        'datasets': {
            source: {
                'total': datasets_total[source],
                'with_duplicates': datasets_with_duplicates.get(source, 0)
            }
            for source in datasets_total.keys()
        },
        'tokenization': {
            'empty_tokens': empty_tokens,
            'total_tokens': sum(len(doc.get('tokens', [])) for doc in docs)
        },
        'metadata_completeness': {
            field: missing_fields.get(field, 0)
            for field in required_fields
        }
    }

    report_path = Path('validation_report.json')
    report_path.write_text(json.dumps(report, indent=2))
    logger.info(f"\nValidation report saved to {report_path}")

    logger.info("\n" + "=" * 60)
    logger.info("Validation complete!")
    logger.info("=" * 60)

if __name__ == "__main__":
    main()
