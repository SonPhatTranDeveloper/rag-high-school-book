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

# Make the 'start.sh' script executable.
RUN chmod +x start.sh

# Define the default command to run when the container starts.
# This will execute the 'start.sh' script.
CMD ["./start.sh"]