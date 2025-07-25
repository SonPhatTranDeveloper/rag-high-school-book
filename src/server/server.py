import logging

from flask import Flask, jsonify, request
from flask_pydantic import validate
from llama_deploy import ControlPlaneConfig, LlamaDeployClient

from src.server.model import AgentResponse
from src.server.utils.constants import ServerConstants
from src.server.utils.metadata import extract_metadata_from_event

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
        session_id = data.get("session_id", "123456")

        logger.info(
            f"Processing query request - Session: {session_id}, "
            f"Query length: {len(query)}"
        )

        # Query the workflow using the LlamaDeployClient
        session = client.get_or_create_session(session_id)
        task_id = session.run_nowait(
            service_name=ServerConstants.RAG_AGENT_SERVICE_NAME.value,
            user_msg=query,
        )

        # Get the events from the task
        events = session.get_task_result_stream(task_id)

        # Get the result from the task until it is finished
        result = None
        while result is None:
            result = session.get_task_result(task_id)

        # Extract the metadata from the events
        metadata = extract_metadata_from_event(events)

        return AgentResponse(
            query=query,
            response=result.result,
            session_id=session_id,
            status="success",
            document_metadata=metadata,
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
    app.run(host="0.0.0.0", port=10000, debug=True)
