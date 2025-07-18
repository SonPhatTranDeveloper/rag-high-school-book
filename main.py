import asyncio

import hydra
from dotenv import load_dotenv
from omegaconf import DictConfig

from src.workflow.agent import RAGAgent


async def run_agent(cfg: DictConfig) -> None:
    """
    Run the agent with the given configuration.

    Args:
        cfg (DictConfig): The configuration for the workflow,
                          retrieved from the config file.

    Returns:
        None
    """
    agent = RAGAgent(cfg.workflow)
    result = await agent.run("Phản ứng oxi hoá khử là gì?")
    print(result)


@hydra.main(config_name="config", config_path="src/config", version_base=None)
def main(cfg: DictConfig) -> None:
    """
    Main function to run the agent.

    Args:
        cfg (DictConfig): The configuration for the workflow,
                          retrieved from the config file.

    Returns:
        None
    """
    load_dotenv()
    asyncio.run(run_agent(cfg))


if __name__ == "__main__":
    main()
