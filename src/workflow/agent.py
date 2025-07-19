import hydra
from llama_index.core.settings import Settings
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from omegaconf import DictConfig


def initialize_llm(cfg: DictConfig) -> None:
    """
    Initialize the LLM via LlamaIndex settings.

    Args:
        cfg: The configuration object.

    Returns:
        None
    """
    llm_config = cfg.llm.model
    embedding_config = cfg.llm.embeddings

    # Initialize the LLM via LlamaIndex settings
    Settings.llm = OpenAI(
        model=llm_config.model_name, temperature=llm_config.temperature
    )

    # Initialize the embedding via LlamaIndex settings
    Settings.embed_model = OpenAIEmbedding(model_name=embedding_config.model_name)


def build_workflow(cfg: DictConfig) -> any:
    """
    Build the workflow from the configuration.

    Args:
        cfg: The configuration object.

    Returns:
        The workflow object.
    """
    # Get the llm and embedding config
    initialize_llm(cfg)
    return hydra.utils.instantiate(cfg.workflow)
