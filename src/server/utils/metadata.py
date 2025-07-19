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


def get_book_grade(grade: str) -> str:
    """
    Get the book grade to the appropriate presentation

    Args:
        grade: The grade of the book

    Returns:
        The appropriate presentation of the book grade in Vietnamese
    """
    if grade == "grade_10":
        return "Lớp 10"
    elif grade == "grade_11":
        return "Lớp 11"
    elif grade == "grade_12":
        return "Lớp 12"
    else:
        raise ValueError(f"Invalid book grade: {grade}")


def get_book_type(book_type: str) -> str:
    """
    Get the book type to the appropriate presentation

    Args:
        book_type: The type of the book

    Returns:
        The appropriate presentation of the book type in Vietnamese
    """
    if book_type == "canh_dieu":
        return "Cánh Diều"
    elif book_type == "key_noi_tri_thuc":
        return "Kết nối tri thức"
    elif book_type == "chan_troi_sang_tao":
        return "Chân trời sáng tạo"
    else:
        raise ValueError(f"Invalid book type: {book_type}")


def get_book_subject(book_subject: str) -> str:
    """
    Get the book subject to the appropriate presentation

    Args:
        book_subject: The subject of the book

    Returns:
        The appropriate presentation of the book subject in Vietnamese
    """
    if book_subject == "toan_1":
        return "Toán 1"
    elif book_subject == "toan_2":
        return "Toán 2"
    elif book_subject == "ngu_van_1":
        return "Ngữ văn 1"
    elif book_subject == "ngu_van_2":
        return "Ngữ văn 2"
    elif book_subject == "lich_su":
        return "Lịch sử"
    elif book_subject == "dia_ly":
        return "Địa lý"
    elif book_subject == "hoa_hoc":
        return "Hóa học"
    elif book_subject == "sinh_hoc":
        return "Sinh học"
    else:
        raise ValueError(f"Invalid book subject: {book_subject}")


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
                        score=node["score"],
                        grade=get_book_grade(node["node"]["metadata"]["grade"]),
                        book_type=get_book_type(node["node"]["metadata"]["book_type"]),
                        book_subject=get_book_subject(
                            node["node"]["metadata"]["book_subject"]
                        ),
                        page_number=node["node"]["metadata"]["page_number"],
                    )
                )

    return result
