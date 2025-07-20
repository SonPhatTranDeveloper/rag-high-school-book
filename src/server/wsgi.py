import logging

from src.server.server import app
from src.server.utils.constants import ServerConstants
from src.server.utils.image import init_cloudinary

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Initialize the cloudinary client for image processing
    logger.info("Initializing cloudinary client...")
    init_cloudinary()

    # Start the Flask server
    logger.info("Starting Flask server...")
    logger.info(
        "Make sure your LlamaDeploy workflow is running on http://localhost:10000"
    )
    logger.info("Available endpoints:")
    logger.info("  GET  /health - Health check")
    logger.info("  POST /query - Query the RAG workflow")
    logger.info("  GET  /sessions - List all sessions")
    logger.info("  DELETE /sessions/<session_id> - Delete a session")
    logger.info("  GET  /services - List all services")

    app.run(
        host=ServerConstants.SERVER_HOST.value,
        port=ServerConstants.SERVER_PORT.value,
    )
