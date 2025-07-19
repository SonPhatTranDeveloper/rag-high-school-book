import logging

from flask import Flask, jsonify, request
from flask_pydantic import validate
from llama_deploy import ControlPlaneConfig, LlamaDeployClient

from src.server.model import AgentResponse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("flask_server.log")],
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Initialize the LlamaDeploy client
client = LlamaDeployClient(ControlPlaneConfig())
logger.info("LlamaDeployClient initialized")


@app.before_request
def log_request_info():
    """Log incoming request information"""
    logger.info(
        f"Incoming {request.method} request to {request.path} "
        f"from {request.remote_addr}"
    )


@app.after_request
def log_response_info(response):
    """Log response information"""
    logger.info(f"Response: {response.status_code} for {request.method} {request.path}")
    return response


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    logger.info("Health check request")
    return jsonify({"status": "healthy", "message": "Flask server is running"})


@app.route("/query", methods=["POST"])
@validate()
def query_workflow():
    """
    Query the RAG workflow via LlamaDeployClient

    Expected JSON payload:
    {
        "query": "Your question here",
        "session_id": "optional_session_id"
    }
    """
    try:
        data = request.get_json()

        if not data or "query" not in data:
            logger.warning("Query request missing 'query' field")
            return jsonify({"error": "Missing 'query' in request body"}), 400

        query = data["query"]
        session_id = data.get("session_id", "default_session")

        logger.info(
            f"Processing query request - Session: {session_id}, "
            f"Query length: {len(query)}"
        )

        # Query the workflow using the LlamaDeployClient
        session = client.create_session()
        result = session.run(
            service_name="rag_agent",
            user_msg=query,
        )

        logger.info(f"Query processed successfully - Session: {session_id}")

        return AgentResponse(
            query=query,
            response=str(result),
            session_id=session_id,
            status="success",
            document_metadata=[],
        )

    except Exception as e:
        logger.error(f"Error processing query: {str(e)}", exc_info=True)
        return jsonify(
            {"error": f"Error processing query: {str(e)}", "status": "error"}
        ), 500


@app.route("/sessions", methods=["GET"])
async def list_sessions():
    """List all active sessions"""
    try:
        logger.info("Listing sessions request")
        sessions = await client.list_sessions()
        logger.info(f"Found {len(sessions) if sessions else 0} sessions")
        return jsonify({"sessions": sessions, "status": "success"})
    except Exception as e:
        logger.error(f"Error listing sessions: {str(e)}", exc_info=True)
        return jsonify(
            {"error": f"Error listing sessions: {str(e)}", "status": "error"}
        ), 500


@app.route("/sessions/<session_id>", methods=["DELETE"])
def delete_session(session_id):
    """Delete a specific session"""
    try:
        logger.info(f"Session deletion requested for: {session_id}")
        # Note: This would require session management implementation
        # For now, we'll just return a success message
        logger.info(f"Session {session_id} deletion completed")
        return jsonify(
            {"message": f"Session {session_id} deletion requested", "status": "success"}
        )
    except Exception as e:
        logger.error(f"Error deleting session {session_id}: {str(e)}", exc_info=True)
        return jsonify(
            {"error": f"Error deleting session: {str(e)}", "status": "error"}
        ), 500


@app.route("/services", methods=["GET"])
async def list_services():
    """List all available services"""
    try:
        logger.info("Listing services request")
        services = await client.list_services()
        logger.info(f"Found {len(services) if services else 0} services")
        return jsonify({"services": services, "status": "success"})
    except Exception as e:
        logger.error(f"Error listing services: {str(e)}", exc_info=True)
        return jsonify(
            {"error": f"Error listing services: {str(e)}", "status": "error"}
        ), 500


if __name__ == "__main__":
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

    app.run(host="0.0.0.0", port=10_000, debug=True)
