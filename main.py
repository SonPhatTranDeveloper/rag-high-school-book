import asyncio

import hydra
from omegaconf import DictConfig
from dotenv import load_dotenv

from src.workflow.agent import RAGAgent


async def run_agent(cfg: DictConfig):
    agent = RAGAgent(cfg.workflow)
    result = await agent.run("Phản ứng oxi hoá khử là gì?")
    print(result)


@hydra.main(config_name="config", config_path="src/config", version_base=None)
def main(cfg: DictConfig):
    asyncio.run(run_agent(cfg))


if __name__ == "__main__":
    load_dotenv()
    main()
