#!/bin/sh
echo "Setting PYTHONPATH..."
export PYTHONPATH=.

echo "Starting llama_deploy.apiserver in background..."
uv run python -m llama_deploy.apiserver &

echo "Waiting 15 seconds before next command..."
sleep 15

echo "Running llamactl deploy..."
uv run llamactl deploy src/deployment.yml

echo "Waiting 60 seconds before next command..."
sleep 60

echo "Starting main server..."
exec uv run gunicorn src.server.wsgi:app --bind 0.0.0.0:8080 --log-level=debug --workers=4