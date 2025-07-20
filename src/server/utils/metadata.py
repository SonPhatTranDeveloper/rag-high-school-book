import logging

from src.server.model import DocumentMetadata
from src.server.utils.image import get_image_url

logger = logging.getLogger(__name__)

# Constants for better maintainability
GRADE_MAPPING = {
    "grade_10": "Lớp 10",
    "grade_11": "Lớp 11",
    "grade_12": "Lớp 12",
}

BOOK_TYPE_MAPPING = {
    "canh_dieu": "Cánh Diều",
    "ket_noi_tri_thuc": "Kết nối tri thức",
    "chan_troi_sang_tao": "Chân trời sáng tạo",
}

BOOK_SUBJECT_MAPPING = {
    "toan_1": "Toán 1",
    "toan_2": "Toán 2",
    "ngu_van_1": "Ngữ văn 1",
    "ngu_van_2": "Ngữ văn 2",
    "lich_su": "Lịch sử",
    "dia_ly": "Địa lý",
    "hoa_hoc": "Hóa học",
    "sinh_hoc": "Sinh học",
}


def has_source_nodes(event: dict) -> bool:
    """
    Check if the event has source nodes

    Args:
        event: The event to check

    Returns:
        bool: True if the event has source nodes, False otherwise
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
        str: The appropriate presentation of the book grade in Vietnamese
    """
    if grade not in GRADE_MAPPING:
        raise ValueError(f"Invalid book grade: {grade}")
    return GRADE_MAPPING[grade]


def get_book_type(book_type: str) -> str:
    """
    Get the book type to the appropriate presentation

    Args:
        book_type: The type of the book

    Returns:
        str: The appropriate presentation of the book type in Vietnamese
    """
    if book_type not in BOOK_TYPE_MAPPING:
        raise ValueError(f"Invalid book type: {book_type}")
    return BOOK_TYPE_MAPPING[book_type]


def get_book_subject(book_subject: str) -> str:
    """
    Get the book subject to the appropriate presentation

    Args:
        book_subject: The subject of the book

    Returns:
        str: The appropriate presentation of the book subject in Vietnamese
    """
    if book_subject not in BOOK_SUBJECT_MAPPING:
        raise ValueError(f"Invalid book subject: {book_subject}")
    return BOOK_SUBJECT_MAPPING[book_subject]


def extract_metadata_from_event(events: list[dict]) -> list[DocumentMetadata]:
    """
    Extract the metadata from the event

    Args:
        events: The events to extract metadata from

    Returns:
        list[DocumentMetadata]: A list of DocumentMetadata
    """
    result = []

    for event in events:
        if has_source_nodes(event):
            # Extract the source nodes
            source_nodes = event["tool_output"]["raw_output"]["source_nodes"]
            for node in source_nodes:
                node_metadata = node["node"]["metadata"]

                # Create DocumentMetadata object
                result.append(
                    DocumentMetadata(
                        text=node["node"]["text"],
                        score=node["score"],
                        grade=get_book_grade(node_metadata["grade"]),
                        book_type=get_book_type(node_metadata["book_type"]),
                        book_subject=get_book_subject(node_metadata["book_subject"]),
                        page_number=node_metadata["page_number"],
                        image_url=get_image_url(node_metadata["file_path"]),
                    )
                )

    return result
