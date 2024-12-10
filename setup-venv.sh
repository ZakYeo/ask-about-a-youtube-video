#!/bin/bash

# Script to activate the virtual environment named "venv"

# Check if the venv directory exists
if [ ! -d "venv" ]; then
    echo "The virtual environment 'venv' does not exist."
    echo "Run 'bash create_venv.sh' to create it."
    exit 1
fi

# Activate the virtual environment
source venv/bin/activate

# Check if activation was successful
if [ $? -eq 0 ]; then
    echo "Virtual environment 'venv' activated."
else
    echo "Failed to activate the virtual environment 'venv'."
    exit 1
fi

