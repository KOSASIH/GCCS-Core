#!/bin/bash

# deploy.sh

set -e  # Exit immediately if a command exits with a non-zero status

# Define variables
PROJECT_DIR=$(pwd)
VENV_DIR="$PROJECT_DIR/venv"
REQUIREMENTS_FILE="$PROJECT_DIR/requirements.txt"

# Create a virtual environment
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Install dependencies
echo "Installing dependencies from $REQUIREMENTS_FILE..."
pip install -r "$REQUIREMENTS_FILE"

# Run database migrations (if applicable)
# Uncomment the following line if using a database with migrations
# echo "Running database migrations..."
# python manage.py migrate

echo "Deployment completed successfully!"
