# Use the official Python 3.13-slim-bookworm image as the base
FROM python:3.13-slim-bookworm

# Install system dependencies required for the application, including git.
# The 'rm -rf /var/lib/apt/lists/*' command cleans up apt caches to reduce image size.
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy the 'uv' and 'uvx' binaries from the official uv image into /bin/.
# This leverages a multi-stage build to efficiently get the UV tool.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory inside the container to /app.
# All subsequent commands will be executed relative to this directory.
WORKDIR /app

# Add the entire project code from the build context into the /app directory in the container.
ADD . /app

# Install the project dependencies using uv, ensuring locked dependencies are respected.
RUN uv sync --locked

# Create a shell script named 'start.sh' to orchestrate the application startup.
# This script sets the PYTHONPATH, starts the API server in the background,
# waits, runs a deployment command, waits again, and then starts the main server.
RUN echo '#!/bin/sh' > start.sh && \
    echo 'echo "Setting PYTHONPATH..."' >> start.sh && \
    echo 'export PYTHONPATH=.' >> start.sh && \
    echo '' >> start.sh && \
    echo 'echo "Starting llama_deploy.apiserver in background..."' >> start.sh && \
    echo 'uv run python -m llama_deploy.apiserver &' >> start.sh && \
    echo '' >> start.sh && \
    echo 'echo "Waiting 15 seconds before next command..."' >> start.sh && \
    echo 'sleep 15' >> start.sh && \
    echo '' >> start.sh && \
    echo 'echo "Running llamactl deploy..."' >> start.sh && \
    echo 'uv run llamactl deploy src/deployment.yml' >> start.sh && \
    echo '' >> start.sh && \
    echo 'echo "Waiting 15 seconds before next command..."' >> start.sh && \
    echo 'sleep 15' >> start.sh && \
    echo '' >> start.sh && \
    echo 'echo "Starting main server..."' >> start.sh && \
    echo 'exec uv run src/server/server.py' >> start.sh

# Make the 'start.sh' script executable.
RUN chmod +x start.sh

# Define the default command to run when the container starts.
# This will execute the 'start.sh' script.
CMD ["./start.sh"]