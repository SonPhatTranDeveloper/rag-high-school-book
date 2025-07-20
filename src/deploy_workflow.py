from dotenv import load_dotenv
from hydra import compose, initialize

from src.workflow.agent import build_workflow

# Initialize the RAG Agent
load_dotenv()
with initialize(version_base=None, config_path="config"):
    cfg = compose(config_name="config")
    workflow = build_workflow(cfg)
