import pydantic


class DocumentMetadata(pydantic.BaseModel):
    """
    Model for the document metadata

    Args:
        text: The text of the document
        score: The score of the document
        grade: The grade of the book (grade_10, grade_11, grade_12)
        book_type: The type of the book (canh_dieu, chan_troi_sang_tao, ...)
        book_subject: The subject of the book (toan, ngu_van, vat_ly, ...)
        page_number: The page number of the book
        image_url: The url of the image of the book
    """

    text: str
    score: float
    grade: str
    book_type: str
    book_subject: str
    page_number: int
    image_url: str


class AgentResponse(pydantic.BaseModel):
    """
    Model for the agent response

    Args:
        query: The query of the user
        response: The response of the agent
        session_id: The session id
        status: The status of the agent
        document_metadata: A list of metadata of the documents used to answer the query
    """

    query: str
    response: str
    session_id: str
    status: str
    document_metadata: list[DocumentMetadata]
