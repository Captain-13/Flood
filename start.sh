#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Update package list
echo "Updating package list..."
sudo apt update -y

# Ensure Python3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 not found. Installing..."
    sudo apt install -y python3
fi

# Ensure pip3 is installed
if ! command -v pip3 &>/dev/null; then
    echo "pip3 not found. Installing..."
    sudo apt install -y python3-pip
fi

# Ensure virtual environment is set up (optional but recommended)
VENV_DIR="venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating a virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Install required Python packages
echo "Installing required Python packages..."
pip3 install --upgrade pip
pip3 install yarl==1.7.2 datetime cfscrape socks pysocks colorama cloudscraper

# Run main.py
if [ -f "main.py" ]; then
    echo "Running main.py..."
    python3 main.py
else
    echo "Error: main.py not found!"
    exit 1
fi