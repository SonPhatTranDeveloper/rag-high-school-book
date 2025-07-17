import hydra
from llama_index.core.agent.workflow import AgentWorkflow
from omegaconf import DictConfig


@hydra.main(config_name="config", config_path="../config", version_base=None)
def create_agentic_workflow(cfg: DictConfig) -> AgentWorkflow:
    """
    Create an agentic workflow using the specified configuration.

    Args:
        cfg (DictConfig): The configuration for the workflow.
    """
    return hydra.utils.instantiate(cfg)
