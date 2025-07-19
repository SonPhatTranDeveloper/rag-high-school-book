# Stage 1: Build Stage
# Use a slim Python image as the base for building uv
FROM python:3.11-slim-bookworm AS builder

# Set the working directory inside the container
WORKDIR /app

# Install uv itself
# We use pip to install uv, which will also install its dependencies.
# The --no-cache-dir flag helps keep the image size down.
RUN pip install --no-cache-dir uv

# Copy all content from the current directory into the container's /app directory.
# This ensures all project files, including pyproject.toml, uv.lock, and your source code,
# are available for the build process and for the final application.
COPY . .

# Install project dependencies using uv sync
# This command will read pyproject.toml (and uv.lock if present)
# and install the specified dependencies into the virtual environment.
RUN uv sync

# Create the startup script
# This script will execute your three commands sequentially with a 15-second delay between them.
# - The first command (llama_deploy.apiserver) is run in the background (&)
#   assuming it's a service that should start and continue running.
# - A 15-second sleep is added.
# - The 'llamactl deploy' command runs next.
# - Another 15-second sleep is added.
# - The final command (src/server/server.py) is run using 'exec',
#   which replaces the shell process with the server process, ensuring
#   proper signal handling (e.g., stopping the container with Ctrl+C).
RUN echo '#!/bin/sh' > start.sh && \
    echo '' >> start.sh && \
    echo 'echo "Starting llama_deploy.apiserver in background..."' >> start.sh && \
    echo 'uv run python -m llama_deploy.apiserver &' >> start.sh && \
    echo '' >> start.sh && \
    echo 'echo "Waiting 15 seconds before next command..."' >> start.sh && \
    echo 'sleep 15' >> start.sh && \
    echo '' >> start.sh && \
    echo 'echo "Running llamactl deploy..."' >> start.sh && \
    echo 'llamactl deploy src/deployment.yml' >> start.sh && \
    echo '' >> start.sh && \
    echo 'echo "Waiting 15 seconds before next command..."' >> start.sh && \
    echo 'sleep 15' >> start.sh && \
    echo '' >> start.sh && \
    echo 'echo "Starting main server..."' >> start.sh && \
    echo 'exec uv run src/server/server.py' >> start.sh

# Make the startup script executable
RUN chmod +x start.sh

# Stage 2: Production Stage
# Use a minimal base image for the final production image
# This ensures a smaller attack surface and faster downloads.
FROM python:3.11-slim-bookworm AS production

# Set the working directory inside the container
WORKDIR /app

# Copy uv and its dependencies from the builder stage
# This ensures only the necessary files are copied, not the build tools.
COPY --from=builder /usr/local/bin/uv /usr/local/bin/uv
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy the installed project dependencies from the builder stage's site-packages
# This includes all packages installed by 'uv sync'.
COPY --from=builder /app/.venv/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy your application code from the builder stage
# This ensures your actual project files are present in the final image.
COPY --from=builder /app .

# Copy the startup script from the builder stage
COPY --from=builder /app/start.sh ./start.sh

# Set the startup script as the default command to run when the container starts
# We use CMD here because the script itself handles the execution flow.
CMD ["./start.sh"]