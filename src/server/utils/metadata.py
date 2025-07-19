import logging

from llama_index.core.agent.workflow import AgentOutput

from src.server.model import DocumentMetadata

logger = logging.getLogger(__name__)


def extract_metadata(agent_output: AgentOutput) -> list[DocumentMetadata] | None:
    """
    Extract the metadata from the agent output

    Args:
        agent_output: The agent output

    Returns:
        A list of DocumentMetadata
    """
    # Get the source nodes
    source_nodes = []

    for tool_call in agent_output.tool_calls:
        if tool_call.tool_name == "rag_book_search_tool":
            source_nodes = tool_call.tool_output.raw_output.source_nodes
            break

    # Extract the metadata from the source nodes
    metadata = []
    for node in source_nodes:
        metadata.append(
            DocumentMetadata(
                grade=node.node.metadata["grade"],
                book_type=node.node.metadata["book_type"],
                book_subject=node.node.metadata["book_subject"],
                page_number=node.node.metadata["page_number"],
            )
        )

    return metadata
