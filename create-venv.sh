#!/bin/bash

# Script to create a virtual environment named "venv"

# Check if the venv directory already exists
if [ -d "venv" ]; then
    echo "The virtual environment 'venv' already exists."
    exit 1
fi

# Create the virtual environment
python3 -m venv venv

# Check if the virtual environment was created successfully
if [ $? -eq 0 ]; then
    echo "Virtual environment 'venv' created successfully."
    echo "Run 'source activate_venv.sh' to activate it."
else
    echo "Failed to create the virtual environment 'venv'."
    exit 1
fi
