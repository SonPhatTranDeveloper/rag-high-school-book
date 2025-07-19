FROM python:3.13-slim-bookworm

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Add the project code
ADD . /app

# Set the working directory
WORKDIR /app

# Install the project dependencies
RUN uv sync --locked

# Create a script to start the server
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

# Make the script executable
RUN chmod +x start.sh

# Start the server
CMD ["./start.sh"]