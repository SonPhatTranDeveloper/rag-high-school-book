import logging

import hydra
from omegaconf import DictConfig


class RAGAgent:
    def __init__(self, cfg: DictConfig):
        self.logger = logging.getLogger(__name__)
        self.workflow = hydra.utils.instantiate(cfg)
        self.logger.info(self.workflow)

    async def run(self, query: str) -> str:
        return await self.workflow.run(query)
