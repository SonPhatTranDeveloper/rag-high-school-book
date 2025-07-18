from hydra import compose, initialize

from src.workflow.agent import build_workflow

# Initialize the RAG Agent
with initialize(version_base=None, config_path="config"):
    cfg = compose(config_name="config")
    agent = build_workflow(cfg)
