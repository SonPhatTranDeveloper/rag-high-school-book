import logging
import os

from llama_index.core import (
    Settings,
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter

logger = logging.getLogger(__name__)


def create_or_load_index(
    storage_dir: str,
    data_dir: str,
    chunk_size: int,
    chunk_overlap: int,
    show_progress: bool,
):
    """
    Create or load a LlamaIndex index from the specified storage directory.
    If the index does not exist, it ingests documents from `data_dir` and creates one.

    Args:
        storage_dir (str): Directory to load/save the index.
        data_dir (str): Directory containing documents to index.
        chunk_size (int): Number of tokens per chunk during ingestion.
        chunk_overlap (int): Number of overlapping tokens between chunks.
        show_progress (bool): Whether to show progress bar.
    Returns:
        VectorStoreIndex: The loaded or newly created index.
    """
    # Check if index already exists
    if os.path.exists(storage_dir):
        logger.info("Loading existing index...")
        storage_context = StorageContext.from_defaults(persist_dir=storage_dir)
        index = load_index_from_storage(storage_context)
    else:
        logger.info("Creating new index...")

        # Create ingestion pipeline
        pipeline = IngestionPipeline(
            transformations=[
                SentenceSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap),
                Settings.embed_model,
            ]
        )

        # Split documents into nodes
        documents = SimpleDirectoryReader(data_dir, recursive=True).load_data()
        nodes = pipeline.run(documents=documents, show_progress=show_progress)

        # Create and save
        index = VectorStoreIndex(nodes)
        index.storage_context.persist(persist_dir=storage_dir)

    return index
