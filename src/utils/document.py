import re


def file_metadata_extractor(file_path: str) -> dict:
    """
    Extract metadata from a file path.

    Args:
        file_path (str): The path to the file.

    Returns:
        dict: A dictionary containing the extracted metadata.
    """
    return {
        **extract_metadata_from_filename(file_path.split("/")[-1]),
        "file_path": file_path,
        "file_name": file_path.split("/")[-1],
    }


def extract_metadata_from_filename(file_name: str) -> dict:
    """
    Extract metadata from a filename formatted as
    '[grade]_[book_type]_[book_subject]_page_[page_number].md'
    using regular expressions.

    Args:
        file_name (str): The filename to extract metadata from.

    Returns:
        dict: A dictionary containing the extracted metadata.
    """
    # Define the pattern for the filename with page number
    pattern = (
        r"^(grade_\d+)_((?:chan_troi_sang_tao|ket_noi_tri_thuc|canh_dieu))_(\w+)"
        r"_page_(\d+)\.md$"
    )

    match = re.match(pattern, file_name)

    if match:
        grade = match.group(1)
        book_type = match.group(2)
        book_subject = match.group(3)
        page_number = int(match.group(4))

        return {
            "grade": grade,
            "book_type": book_type,
            "book_subject": book_subject,
            "page_number": page_number,
        }
    else:
        raise ValueError(
            f"Filename '{file_name}' does not match the expected pattern: "
            "'grade_X_booktype_subject_page_N.md'"
        )
