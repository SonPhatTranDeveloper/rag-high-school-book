import asyncio

from dotenv import load_dotenv
from hydra import compose, initialize

from src.workflow.agent import RAGAgent

# Initialize the RAG Agent
with initialize(version_base=None, config_path="src/config"):
    cfg = compose(config_name="config")
    agent = RAGAgent(cfg)


async def run_agent() -> None:
    """
    Run the agent with the given configuration.

    Args:
        cfg (DictConfig): The configuration for the workflow,
                          retrieved from the config file.

    Returns:
        None
    """
    result = await agent.run("Hồ Chí Minh là ai?")
    print(result)


def main() -> None:
    """
    Main function to run the agent.

    Args:
        cfg (DictConfig): The configuration for the workflow,
                          retrieved from the config file.

    Returns:
        None
    """
    load_dotenv()
    asyncio.run(run_agent())


if __name__ == "__main__":
    main()
