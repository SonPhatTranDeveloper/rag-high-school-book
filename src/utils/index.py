import logging
import os

from llama_index.core import (
    Settings,
    SimpleDirectoryReader,
    VectorStoreIndex,
)
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.vector_stores.pinecone import PineconeVectorStore
from pinecone import Pinecone

from src.utils.document import file_metadata_extractor

logger = logging.getLogger(__name__)


class VectorIndexManager:
    """
    Singleton class for managing LlamaIndex vector store operations with Pinecone.
    Ensures only one index instance exists throughout the application lifecycle.
    """

    _instance = None
    _index = None
    _initialized = False
    _pinecone_client = None
    _pinecone_index_name = None  # Store the Pinecone index name

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(
        self,
        pinecone_environment: str,
        pinecone_index_name: str,
        data_dir: str,
        chunk_size: int,
        chunk_overlap: int,
        show_progress: bool,
        embedding_dimension: int,
        metric: str,
    ):
        """
        Initialize the VectorIndexManager (only happens once due to singleton pattern).

        Args:
            pinecone_environment (str): Your Pinecone environment (e.g., 'us-west-2').
            pinecone_index_name (str): The name of the Pinecone index to use.
            data_dir (str): Directory containing documents to index.
            chunk_size (int): Number of tokens per chunk during ingestion.
            chunk_overlap (int): Number of overlapping tokens between chunks.
            show_progress (bool): Whether to show progress bar.
        """
        # Only initialize once
        if not self._initialized:
            self.data_dir = data_dir
            self.chunk_size = chunk_size
            self.chunk_overlap = chunk_overlap
            self.show_progress = show_progress
            self._pinecone_index_name = pinecone_index_name
            self.embedding_dimension = embedding_dimension
            self.metric = metric
            # Initialize Pinecone client
            try:
                self._pinecone_client = Pinecone(
                    api_key=os.getenv("PINECONE_API_KEY"),
                    environment=pinecone_environment,
                )
                logger.info("Pinecone client initialized successfully.")
            except Exception as e:
                logger.error(f"Failed to initialize Pinecone client: {e}")
                raise

            self._index = self._create_or_load_index()
            self._initialized = True
        else:
            logger.warning(
                "VectorIndexManager is already initialized. "
                "Using existing instance with original parameters."
            )

    def _create_or_load_index(self) -> VectorStoreIndex:
        """
        Create or load a LlamaIndex index using Pinecone as the vector store.
        If the Pinecone index does not exist, it will be created.
        Documents from data_dir will be ingested if the index is new or empty.

        Returns:
            VectorStoreIndex: The loaded or newly created index.
        """
        if self._pinecone_client is None:
            raise RuntimeError("Pinecone client not initialized.")

        # Check if the Pinecone index exists, create if not
        if self._pinecone_index_name not in self._pinecone_client.list_indexes():
            logger.info(
                f"Pinecone index '{self._pinecone_index_name}' not found. "
                f"Creating new index..."
            )
            try:
                self._pinecone_client.create_index(
                    name=self._pinecone_index_name,
                    dimension=self.embedding_dimension,
                    metric=self.metric,
                )
                logger.info(f"Pinecone index '{self._pinecone_index_name}' created.")
            except Exception as e:
                logger.error(
                    f"Failed to create Pinecone index "
                    f"'{self._pinecone_index_name}': {e}"
                )
                raise

        # Connect to the Pinecone index
        pinecone_index = self._pinecone_client.Index(self._pinecone_index_name)
        vector_store = PineconeVectorStore(pinecone_index=pinecone_index)

        # Create ingestion pipeline
        pipeline = IngestionPipeline(
            transformations=[
                SentenceSplitter(
                    chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap
                ),
                Settings.embed_model,
            ]
        )

        # Load documents from the data directory
        documents = SimpleDirectoryReader(
            input_dir=self.data_dir,
            recursive=True,
            file_metadata=file_metadata_extractor,
        ).load_data()

        # Ingest documents into Pinecone
        logger.info(
            f"Ingesting {len(documents)} documents into Pinecone index "
            f"'{self._pinecone_index_name}'..."
        )
        nodes = pipeline.run(documents=documents, show_progress=self.show_progress)
        index = VectorStoreIndex(nodes, vector_store=vector_store)
        logger.info("Documents ingested into Pinecone.")

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
        cls._pinecone_client = None
        cls._pinecone_index_name = None


# Backward compatibility function (optional)
def create_or_load_query_engine(
    pinecone_environment: str,
    pinecone_index_name: str,
    data_dir: str,
    chunk_size: int,
    chunk_overlap: int,
    top_k: int,
    show_progress: bool,
) -> VectorStoreIndex:
    """
    Backward compatibility function that uses the singleton VectorIndexManager.

    Args:
        pinecone_environment (str): Your Pinecone environment (e.g., 'us-west-2').
        pinecone_index_name (str): The name of the Pinecone index to use.
        data_dir (str): Directory containing documents to index.
        chunk_size (int): Number of tokens per chunk during ingestion.
        chunk_overlap (int): Number of overlapping tokens between chunks.
        top_k (int): Number of results to return.
        show_progress (bool): Whether to show progress bar.

    Returns:
        VectorStoreIndex: The loaded or newly created index.
    """
    manager = VectorIndexManager(
        pinecone_environment=pinecone_environment,
        pinecone_index_name=pinecone_index_name,
        data_dir=data_dir,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        show_progress=show_progress,
    )
    return manager.get_index().as_query_engine(similarity_top_k=top_k)
