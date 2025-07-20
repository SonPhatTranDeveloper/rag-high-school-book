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
from llama_index.vector_stores.pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

from src.utils.document import file_metadata_extractor

logger = logging.getLogger(__name__)


class BaseQueryEngineCreator(ABC):
    @abstractmethod
    def create_query_engine(self, **kwargs) -> any:
        pass


class PineconeQueryEngineCreator(BaseQueryEngineCreator):
    QUERY_ENGINE = None

    def _if_index_exists(
        self, pinecone_client: Pinecone, pinecone_index_name: str
    ) -> bool:
        """
        Check if the Pinecone index exists.

        Args:
            pinecone_client (Pinecone): The Pinecone client.
            pinecone_index_name (str): The name of the Pinecone index.

        Returns:
            bool: True if the index exists, False otherwise.
        """
        for item in pinecone_client.list_indexes():
            if item["name"] == pinecone_index_name:
                return True
        return False

    def create_query_engine(
        self,
        data_dir: str,
        chunk_size: int,
        chunk_overlap: int,
        top_k: int,
        show_progress: bool,
        additional_args: dict,
    ) -> any:
        """
        Create a query engine for the Pinecone index.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            any: The query engine.
        """

        if PineconeQueryEngineCreator.QUERY_ENGINE is not None:
            return PineconeQueryEngineCreator.QUERY_ENGINE

        # Extract Pinecone configuration from kwargs
        pinecone_cloud_provider = additional_args.get("pinecone_cloud_provider")
        pinecone_environment = additional_args.get("pinecone_environment")
        pinecone_index_name = additional_args.get("pinecone_index_name")
        embedding_dimension = additional_args.get("embedding_dimension")
        metric = additional_args.get("metric")

        # Create Pinecone client
        pinecone_client = Pinecone(
            api_key=os.getenv("PINECONE_API_KEY"),
        )

        # Check if index exists
        index_exists = self._if_index_exists(
            pinecone_client=pinecone_client,
            pinecone_index_name=pinecone_index_name,
        )

        # Check if the Pinecone index exists, create if not
        if not index_exists:
            logger.info(
                f"Pinecone index '{pinecone_index_name}' not found. "
                f"Creating new index..."
            )
            pinecone_client.create_index(
                name=pinecone_index_name,
                dimension=embedding_dimension,
                metric=metric,
                spec=ServerlessSpec(
                    cloud=pinecone_cloud_provider,
                    region=pinecone_environment,
                ),
            )
            logger.info(f"Pinecone index '{pinecone_index_name}' created.")

        # Connect to the Pinecone index
        pinecone_index = pinecone_client.Index(pinecone_index_name)
        vector_store = PineconeVectorStore(pinecone_index=pinecone_index)

        if not index_exists:
            # New index - ingest documents
            logger.info("Building new index by ingesting documents...")

            # Create ingestion pipeline
            pipeline = IngestionPipeline(
                transformations=[
                    SentenceSplitter(
                        chunk_size=chunk_size, chunk_overlap=chunk_overlap
                    ),
                    Settings.embed_model,
                ],
                vector_store=vector_store,
            )

            # Load documents from the data directory
            documents = SimpleDirectoryReader(
                input_dir=data_dir,
                recursive=True,
                file_metadata=file_metadata_extractor,
            ).load_data()

            # Ingest documents into Pinecone
            logger.info(
                f"Ingesting {len(documents)} documents into Pinecone index "
                f"'{pinecone_index_name}'..."
            )
            nodes = pipeline.run(documents=documents, show_progress=show_progress)
            index = VectorStoreIndex(nodes, vector_store=vector_store)
            logger.info("Documents ingested into Pinecone.")
        else:
            # Existing index - load from vector store
            logger.info("Loading existing index from Pinecone...")
            index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
            logger.info("Index loaded from existing vector store.")

        PineconeQueryEngineCreator.QUERY_ENGINE = index.as_query_engine(
            similarity_top_k=top_k
        )
        return PineconeQueryEngineCreator.QUERY_ENGINE


def create_or_load_query_engine(
    type: str,
    data_dir: str,
    chunk_size: int,
    chunk_overlap: int,
    top_k: int,
    show_progress: bool,
    additional_args: dict,
) -> VectorStoreIndex:
    """
    Create a query engine for RAG

    Args:
        type (str): The type of index to use.
        data_dir (str): Directory containing documents to index.
        chunk_size (int): Number of tokens per chunk during ingestion.
        chunk_overlap (int): Number of overlapping tokens between chunks.
        top_k (int): Number of results to return.
        show_progress (bool): Whether to show progress bar.
        additional_args (dict): Additional arguments for the index.
    Returns:
        VectorStoreIndex: The loaded or newly created index.
    """
    if type == "pinecone":
        if "pinecone_cloud_provider" not in additional_args:
            raise ValueError("pinecone_cloud_provider is required")
        if "pinecone_environment" not in additional_args:
            raise ValueError("pinecone_environment is required")
        if "pinecone_index_name" not in additional_args:
            raise ValueError("pinecone_index_name is required")
        if "embedding_dimension" not in additional_args:
            raise ValueError("embedding_dimension is required")
        if "metric" not in additional_args:
            raise ValueError("metric is required")

        return PineconeQueryEngineCreator().create_query_engine(
            data_dir=data_dir,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            top_k=top_k,
            show_progress=show_progress,
            additional_args=additional_args,
        )
    else:
        raise ValueError(f"Invalid index type: {type}")
