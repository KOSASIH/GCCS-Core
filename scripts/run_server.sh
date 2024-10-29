#!/bin/bash

# run_server.sh

set -e  # Exit immediately if a command exits with a non-zero status

# Define variables
PROJECT_DIR=$(pwd)
VENV_DIR="$PROJECT_DIR/venv"

# Activate the virtual environment
if [ -d "$VENV_DIR" ]; then
    echo "Activating virtual environment..."
    source "$VENV_DIR/bin/activate"
else
    echo "Error: Virtual environment not found. Please run deploy.sh first."
    exit 1
fi

# Start the server
echo "Starting the GCCS-Core server..."
python3 -m src.main

# Note: You can replace 'src.main' with the actual entry point of your application
