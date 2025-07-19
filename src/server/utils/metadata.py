import logging

from src.server.model import DocumentMetadata

logger = logging.getLogger(__name__)


def has_source_nodes(event: dict) -> bool:
    """
    Check if the event has source nodes
    """
    return (
        "tool_output" in event
        and "raw_output" in event["tool_output"]
        and "source_nodes" in event["tool_output"]["raw_output"]
    )


def extract_metadata_from_event(events: list[dict]) -> list[DocumentMetadata]:
    """
    Extract the metadata from the event

    Args:
        event: The event

    Returns:
        A list of DocumentMetadata
    """
    result = []

    for event in events:
        if has_source_nodes(event):
            # Extract the source nodes
            source_nodes = event["tool_output"]["raw_output"]["source_nodes"]
            for node in source_nodes:
                # Get the node
                result.append(
                    DocumentMetadata(
                        text=node["node"]["text"],
                        score=node["node"]["score"],
                        grade=node["node"]["metadata"]["grade"],
                        book_type=node["node"]["metadata"]["book_type"],
                        book_subject=node["node"]["metadata"]["book_subject"],
                        page_number=node["node"]["metadata"]["page_number"],
                    )
                )

    return result
