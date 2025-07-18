import logging

import hydra
from omegaconf import DictConfig


class RAGAgent:
    """
    RAGAgent is a class that implements the RAG workflow.
    It uses the workflow configuration to create an agentic workflow.
    It then runs the workflow with the given query.
    It returns the result of the workflow.

    Args:
        cfg (DictConfig): The configuration for the workflow.
    """

    def __init__(self, cfg: DictConfig) -> None:
        self.logger = logging.getLogger(__name__)
        self.workflow = hydra.utils.instantiate(cfg)

    async def run(self, query: str) -> any:
        """
        Run the workflow with the given query.

        Args:
            query (str): The query to run the workflow with.

        Returns:
            any: The result of the workflow.
        """
        return await self.workflow.run(query)
