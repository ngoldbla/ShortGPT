#!/bin/bash

# ShortGPT Mac Run Script
# Quick launcher for ShortGPT on macOS

echo "🚀 Starting ShortGPT..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run ./setup_mac.sh first"
    exit 1
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found. Please create one with your API keys"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Run the application
echo "🎬 Launching ShortGPT web interface..."
echo "   The interface will open at: http://localhost:31415"
echo ""
python runShortGPT.py
