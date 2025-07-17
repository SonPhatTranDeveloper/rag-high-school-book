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


class VectorIndexManager:
    """
    Singleton class for managing LlamaIndex vector store operations.
    Ensures only one index instance exists throughout the application lifecycle.
    """

    _instance = None
    _index = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(
        self,
        storage_dir: str,
        data_dir: str,
        chunk_size: int,
        chunk_overlap: int,
        show_progress: bool,
    ):
        """
        Initialize the VectorIndexManager (only happens once due to singleton pattern).

        Args:
            storage_dir (str): Directory to load/save the index.
            data_dir (str): Directory containing documents to index.
            chunk_size (int): Number of tokens per chunk during ingestion.
            chunk_overlap (int): Number of overlapping tokens between chunks.
            show_progress (bool): Whether to show progress bar.
        """
        # Only initialize once
        if not self._initialized:
            self.storage_dir = storage_dir
            self.data_dir = data_dir
            self.chunk_size = chunk_size
            self.chunk_overlap = chunk_overlap
            self.show_progress = show_progress
            self._index = self._create_or_load_index()
            self._initialized = True
        else:
            logger.warning(
                "VectorIndexManager is already initialized. "
                "Using existing instance with original parameters."
            )

    def _create_or_load_index(self) -> VectorStoreIndex:
        """
        Create or load a LlamaIndex index from the specified storage directory.
        If the index does not exist, it ingests documents from data_dir and creates one.

        Returns:
            VectorStoreIndex: The loaded or newly created index.
        """
        # Check if index already exists
        if os.path.exists(self.storage_dir):
            logger.info("Loading existing index...")
            storage_context = StorageContext.from_defaults(persist_dir=self.storage_dir)
            index = load_index_from_storage(storage_context)
        else:
            logger.info("Creating new index...")

            # Create ingestion pipeline
            pipeline = IngestionPipeline(
                transformations=[
                    SentenceSplitter(
                        chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap
                    ),
                    Settings.embed_model,
                ]
            )

            # Split documents into nodes
            documents = SimpleDirectoryReader(
                input_dir=self.data_dir, recursive=True
            ).load_data()
            nodes = pipeline.run(documents=documents, show_progress=self.show_progress)

            # Create and save
            index = VectorStoreIndex(nodes)
            index.storage_context.persist(persist_dir=self.storage_dir)

        return index

    def get_index(self) -> VectorStoreIndex:
        """
        Get the managed vector index instance.

        Returns:
            VectorStoreIndex: The vector index instance.
        """
        if self._index is None:
            raise RuntimeError("VectorIndexManager not properly initialized")
        return self._index

    @classmethod
    def is_initialized(cls) -> bool:
        """
        Check if the singleton instance has been initialized.

        Returns:
            bool: True if initialized, False otherwise.
        """
        return cls._instance is not None and cls._instance._initialized

    @classmethod
    def reset(cls):
        """
        Reset the singleton instance. Use with caution.
        This will clear the current instance and allow reinitialization.
        """
        if cls._instance is not None:
            logger.info("Resetting VectorIndexManager singleton instance")
        cls._instance = None
        cls._index = None
        cls._initialized = False


# Backward compatibility function (optional)
def create_or_load_index(
    storage_dir: str,
    data_dir: str,
    chunk_size: int,
    chunk_overlap: int,
    show_progress: bool,
) -> VectorStoreIndex:
    """
    Backward compatibility function that uses the singleton VectorIndexManager.

    Args:
        storage_dir (str): Directory to load/save the index.
        data_dir (str): Directory containing documents to index.
        chunk_size (int): Number of tokens per chunk during ingestion.
        chunk_overlap (int): Number of overlapping tokens between chunks.
        show_progress (bool): Whether to show progress bar.
    Returns:
        VectorStoreIndex: The loaded or newly created index.
    """
    manager = VectorIndexManager(
        storage_dir=storage_dir,
        data_dir=data_dir,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        show_progress=show_progress,
    )
    return manager.get_index()
