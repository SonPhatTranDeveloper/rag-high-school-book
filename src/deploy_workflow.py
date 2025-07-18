import asyncio

from hydra import compose, initialize
from llama_deploy import (
    ControlPlaneConfig,
    WorkflowServiceConfig,
    deploy_workflow,
)

from src.workflow.agent import build_workflow

# Initialize the RAG Agent
with initialize(version_base=None, config_path="config"):
    cfg = compose(config_name="config")
    workflow = build_workflow(cfg)


async def main():
    """
    Deploy workflow to the control plane
    """
    deploy_workflow(
        workflow=workflow,
        workflow_config=WorkflowServiceConfig(
            service_name="rag-book-workflow",
            service_port=8000,
            host="0.0.0.0",
        ),
        control_plane_config=ControlPlaneConfig(
            control_plane_url="http://localhost:8000",
        ),
    )


if __name__ == "__main__":
    asyncio.run(main())
