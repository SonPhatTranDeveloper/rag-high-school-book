import logging
import os
from abc import ABC, abstractmethod

from llama_index.core import (
    Settings,
    SimpleDirectoryReader,
    VectorStoreIndex,
)
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.vector_stores import VectorStore
from llama_index.vector_stores.pinecone import PineconeVectorStore
from pinecone import Pinecone

from src.utils.document import file_metadata_extractor

logger = logging.getLogger(__name__)


class BaseVectorIndexManager(ABC):
    """
    Abstract base class for managing LlamaIndex vector store operations.
    Handles common functionalities like document loading and ingestion pipeline setup.
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
        data_dir: str,
        chunk_size: int,
        chunk_overlap: int,
        show_progress: bool,
    ):
        """
        Initialize the BaseVectorIndexManager.

        Args:
            data_dir (str): Directory containing documents to index.
            chunk_size (int): Number of tokens per chunk per chunk during ingestion.
            chunk_overlap (int): Number of overlapping tokens between chunks.
            show_progress (bool): Whether to show progress bar.
        """
        if not self._initialized:
            self.data_dir = data_dir
            self.chunk_size = chunk_size
            self.chunk_overlap = chunk_overlap
            self.show_progress = show_progress
            self._initialized = True
        else:
            logger.warning(
                f"{self.__class__.__name__} is already initialized. "
                "Using existing instance with original parameters."
            )

    @abstractmethod
    def _create_or_load_vector_store(self) -> VectorStore:
        """
        Abstract method to create or connect to a specific vector store.
        Derived classes must implement this.
        """
        pass

    def _load_documents(self):
        """
        Loads documents from the specified data directory.
        """
        logger.info(f"Loading documents from {self.data_dir}...")
        documents = SimpleDirectoryReader(
            input_dir=self.data_dir,
            recursive=True,
            file_metadata=file_metadata_extractor,
        ).load_data()
        logger.info(f"Loaded {len(documents)} documents.")
        return documents

    def _create_ingestion_pipeline(self) -> IngestionPipeline:
        """
        Creates and returns the LlamaIndex ingestion pipeline.
        """
        logger.info("Creating ingestion pipeline...")
        pipeline = IngestionPipeline(
            transformations=[
                SentenceSplitter(
                    chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap
                ),
                Settings.embed_model,
            ]
        )
        return pipeline

    def _ingest_documents(
        self, documents, vector_store: VectorStore
    ) -> VectorStoreIndex:
        """
        Ingests documents into the given vector store.
        """
        if not documents:
            logger.warning("No documents to ingest. Returning an empty index.")
            return VectorStoreIndex([], vector_store=vector_store)

        pipeline = self._create_ingestion_pipeline()
        logger.info(f"Ingesting {len(documents)} documents...")
        nodes = pipeline.run(documents=documents, show_progress=self.show_progress)
        index = VectorStoreIndex(nodes, vector_store=vector_store)
        logger.info("Documents ingested successfully.")
        return index

    @abstractmethod
    def _create_or_load_index(self) -> VectorStoreIndex:
        """
        Abstract method to create or load the LlamaIndex index  .
        Derived classes must implement this.
        """
        pass

    def get_index(self) -> VectorStoreIndex:
        """
        Get the managed vector index instance.
        """
        if self._index is None:
            # This ensures _create_or_load_index is called only once after init
            # and is responsible for setting self._index
            self._index = self._create_or_load_index()
            if self._index is None:
                raise RuntimeError(
                    "VectorIndexManager not properly initialized: "
                    "_create_or_load_index did not return an index."
                )
        return self._index

    @classmethod
    def is_initialized(cls) -> bool:
        """
        Check if the singleton instance has been initialized.
        """
        return cls._instance is not None and cls._instance._initialized

    @classmethod
    def reset(cls):
        """
        Reset the singleton instance. Use with caution.
        This will clear the current instance and allow reinitialization.
        """
        if cls._instance is not None:
            logger.info(f"Resetting {cls.__name__} singleton instance")
        cls._instance = None
        cls._index = None
        cls._initialized = False


class PineconeVectorIndexManager(BaseVectorIndexManager):
    """
    Concrete class for managing LlamaIndex vector store operations with Pinecone.
    """

    def __init__(
        self,
        pinecone_environment: str,
        pinecone_index_name: str,
        data_dir: str,
        chunk_size: int,
        chunk_overlap: int,
        show_progress: bool,
        embedding_dimension: int = 3072,
        metric: str = "cosine",
    ):
        """
        Initialize the PineconeVectorIndexManager.

        Args:
            pinecone_environment (str): Pinecone environment (e.g., 'us-west-2').
            pinecone_index_name (str): The name of the Pinecone index to use.
            data_dir (str): Directory containing documents to index.
            chunk_size (int): Number of tokens per chunk during ingestion.
            chunk_overlap (int): Number of overlapping tokens between chunks.
            show_progress (bool): Whether to show progress bar.
            embedding_dimension (int): The dimension of the embeddings.
            metric (str): The distance metric for the Pinecone index.
        """
        # Call the base class constructor
        super().__init__(
            data_dir=data_dir,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            show_progress=show_progress,
        )

        # Pinecone specific initialization (only if not already initialized by base)
        if (
            not self._initialized
        ):  # Check _initialized from base class to prevent re-init
            self._pinecone_client = None
            self._pinecone_index_name = pinecone_index_name
            self._embedding_dimension = embedding_dimension
            self._metric = metric

            try:
                self._pinecone_client = Pinecone(
                    api_key=os.getenv("PINECONE_API_KEY"),
                    environment=pinecone_environment,
                )
                logger.info("Pinecone client initialized successfully.")
            except Exception as e:
                logger.error(f"Failed to initialize Pinecone client: {e}")
                raise

    def _create_or_load_vector_store(self) -> PineconeVectorStore:
        """
        Connects to or creates the Pinecone index and returns a PineconeVectorStore.
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
                    dimension=self._embedding_dimension,
                    metric=self._metric,
                )
                logger.info(f"Pinecone index '{self._pinecone_index_name}' created.")
            except Exception as e:
                logger.error(
                    f"Failed to create Pinecone index '{self._pinecone_index_name}'"
                    f"with error: {e}"
                )
                raise

        # Connect to the Pinecone index
        pinecone_index = self._pinecone_client.Index(self._pinecone_index_name)
        vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
        return vector_store

    def _create_or_load_index(self) -> VectorStoreIndex:
        """
        Creates or loads a LlamaIndex index using Pinecone as the vector store.
        Documents are ingested if the Pinecone index is newly created or empty.
        """
        vector_store = self._create_or_load_vector_store()
        documents = self._load_documents()

        # Ingest documents into Pinecone.
        # This will add new documents or update existing ones based on IDs.
        # Note: A more robust check for "empty" Pinecone index might be needed
        # if you want to avoid re-ingestion every time. For simplicity, we
        # always attempt ingestion if documents are loaded.
        return self._ingest_documents(documents, vector_store)

    @classmethod
    def reset(cls):
        """
        Reset the singleton instance.
        Overrides base class reset to clear Pinecone specific attributes.
        """
        super().reset()
        cls._instance = None  # Ensure the instance itself is cleared for re-creation
        cls._pinecone_client = None
        cls._pinecone_index_name = None
        cls._embedding_dimension = None
        cls._metric = None


# Backward compatibility function
def create_or_load_query_engine(
    pinecone_environment: str,
    pinecone_index_name: str,
    data_dir: str,
    chunk_size: int,
    chunk_overlap: int,
    top_k: int,
    show_progress: bool,
    embedding_dimension: int,
    metric: str,
) -> VectorStoreIndex:
    """
    Backward compatibility function that uses the singleton PineconeVectorIndexManager.

    Args:
        pinecone_environment (str): Pinecone environment (e.g., 'us-west-2').
        pinecone_index_name (str): The name of the Pinecone index to use.
        data_dir (str): Directory containing documents to index.
        chunk_size (int): Number of tokens per chunk during ingestion.
        chunk_overlap (int): Number of overlapping tokens between chunks.
        top_k (int): Number of results to return.
        show_progress (bool): Whether to show progress bar.
        embedding_dimension (int): The dimension of the embeddings your model produces.
        metric (str): The distance metric for the Pinecone index.

    Returns:
        VectorStoreIndex: The loaded or newly created index.
    """
    manager = PineconeVectorIndexManager(
        pinecone_environment=pinecone_environment,
        pinecone_index_name=pinecone_index_name,
        data_dir=data_dir,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        show_progress=show_progress,
        embedding_dimension=embedding_dimension,
        metric=metric,
    )
    return manager.get_index().as_query_engine(similarity_top_k=top_k)
