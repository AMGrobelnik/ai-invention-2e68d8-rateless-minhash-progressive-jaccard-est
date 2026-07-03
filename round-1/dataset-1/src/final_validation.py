#!/usr/bin/env python3
"""Final validation and summary of the collected dataset."""

from loguru import logger
from pathlib import Path
import json
from collections import defaultdict

logger.remove()
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
logger.add(__import__('sys').stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")

def main():
    """Generate final validation report and summary."""
    logger.info("Loading final dataset...")

    # Load dataset
    with open('data_out.json', 'r') as f:
        docs = json.load(f)

    logger.info(f"Total documents: {len(docs)}")

    # Create index for duplicate checking
    doc_index = {doc['id']: doc for doc in docs}

    # Analyze datasets
    datasets = defaultdict(lambda: {'total': 0, 'with_duplicates': 0, 'total_tokens': 0})
    similarity_levels = defaultdict(int)
    duplicate_pairs = []

    for doc in docs:
        source = doc['metadata']['source_dataset']
        datasets[source]['total'] += 1
        datasets[source]['total_tokens'] += len(doc.get('tokens', []))

        dup_id = doc['metadata'].get('duplicate_id')
        if dup_id and dup_id in doc_index:
            datasets[source]['with_duplicates'] += 1
            duplicate_pairs.append((doc['id'], dup_id))

        sim_level = doc['metadata'].get('similarity_level')
        if sim_level:
            similarity_levels[sim_level] += 1

    # Calculate statistics
    total_docs = len(docs)
    total_duplicates = len(duplicate_pairs)
    total_tokens = sum(len(doc.get('tokens', [])) for doc in docs)
    avg_doc_length = sum(doc['metadata']['document_length'] for doc in docs) / total_docs

    # Check file size
    import os
    file_size = os.path.getsize('data_out.json') / (1024**2)

    # Create comprehensive summary
    summary = {
        'total_documents': total_docs,
        'total_duplicate_pairs': total_duplicates,
        'total_tokens': total_tokens,
        'avg_document_length': avg_doc_length,
        'file_size_mb': file_size,
        'datasets': dict(datasets),
        'similarity_levels': dict(similarity_levels),
        'schema_validation': {
            'has_id': all('id' in doc for doc in docs),
            'has_text': all('text' in doc for doc in docs),
            'has_tokens': all('tokens' in doc for doc in docs),
            'has_metadata': all('metadata' in doc for doc in docs),
            'metadata_has_source': all('source_dataset' in doc['metadata'] for doc in docs),
            'metadata_has_duplicate_id': all('duplicate_id' in doc['metadata'] for doc in docs),
        }
    }

    # Save summary
    summary_path = Path('dataset_summary.json')
    summary_path.write_text(json.dumps(summary, indent=2))
    logger.info(f"Dataset summary saved to {summary_path}")

    # Print summary
    logger.info("=" * 60)
    logger.info("FINAL DATASET SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Total documents: {total_docs}")
    logger.info(f"Total duplicate pairs: {total_duplicates}")
    logger.info(f"Total tokens: {total_tokens}")
    logger.info(f"Average document length: {avg_doc_length:.2f} tokens")
    logger.info(f"File size: {file_size:.2f}MB")

    logger.info("\nDatasets included:")
    for source, stats in datasets.items():
        logger.info(f"  {source}: {stats['total']} docs, {stats['with_duplicates']} with duplicates")

    logger.info("\nSimilarity levels:")
    for level, count in similarity_levels.items():
        logger.info(f"  {level}: {count} docs")

    logger.info("\nSchema validation:")
    for field, valid in summary['schema_validation'].items():
        logger.info(f"  {field}: {'✓' if valid else '✗'}")

    # Check requirements
    logger.info("\n" + "=" * 60)
    logger.info("REQUIREMENTS CHECK")
    logger.info("=" * 60)

    checks = [
        ("File size < 300MB", file_size < 300, f"{file_size:.2f}MB"),
        ("Has duplicate pairs", total_duplicates > 0, f"{total_duplicates} pairs"),
        ("Has multiple datasets", len(datasets) >= 5, f"{len(datasets)} datasets"),
        ("Has controlled similarity", len(similarity_levels) > 0, f"{len(similarity_levels)} levels"),
        ("Schema complete", all(summary['schema_validation'].values()), "All fields present"),
    ]

    all_passed = True
    for check_name, passed, detail in checks:
        status = "✓" if passed else "✗"
        logger.info(f"{status} {check_name}: {detail}")
        if not passed:
            all_passed = False

    if all_passed:
        logger.info("\n✓ All requirements met!")
    else:
        logger.warning("\n✗ Some requirements not met!")

    logger.info("=" * 60)

if __name__ == "__main__":
    main()
