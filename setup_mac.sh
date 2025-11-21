#!/bin/bash

# ShortGPT Mac Setup Script
# This script automates the setup process for running ShortGPT on macOS

set -e  # Exit on error

echo "🚀 ShortGPT Mac Setup"
echo "===================="
echo ""

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew is not installed. Please install it first:"
    echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    exit 1
fi
echo "✅ Homebrew is installed"

# Check if Python 3.10+ is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Installing via Homebrew..."
    brew install python@3.10
else
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
    echo "✅ Python $PYTHON_VERSION is installed"

    # Check if version is at least 3.10
    if [[ $(echo "$PYTHON_VERSION 3.10" | awk '{print ($1 >= $2)}') == 0 ]]; then
        echo "⚠️  Python 3.10+ is recommended. Installing Python 3.10..."
        brew install python@3.10
    fi
fi

# Check if FFmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  FFmpeg is not installed. Installing via Homebrew..."
    brew install ffmpeg
else
    echo "✅ FFmpeg is installed"
fi

# Create virtual environment
echo ""
echo "📦 Setting up Python virtual environment..."
if [ -d "venv" ]; then
    echo "   Virtual environment already exists. Skipping..."
else
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "🔧 Installing Python dependencies..."
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

echo ""
echo "✅ All dependencies installed!"

# Check for .env file
if [ ! -f ".env" ]; then
    echo ""
    echo "⚠️  No .env file found. Creating from template..."
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "✅ Created .env file from template"
    else
        cat > .env << 'EOF'
# ShortGPT API Keys Configuration
# Get your API keys from the respective services:
# - Gemini: https://makersuite.google.com/app/apikey (FREE - recommended)
# - OpenAI: https://platform.openai.com/api-keys
# - ElevenLabs: https://elevenlabs.io/ (optional for voice synthesis)
# - Pexels: https://www.pexels.com/api/ (FREE for stock footage)

GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
PEXELS_API_KEY=your_pexels_api_key_here
EOF
        echo "✅ Created .env file template"
    fi
    echo ""
    echo "⚠️  IMPORTANT: Edit the .env file and add your API keys before running!"
    echo "   You can edit it with: nano .env"
else
    echo "✅ .env file already exists"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To run ShortGPT:"
echo "1. Make sure you've added your API keys to the .env file"
echo "2. Run: ./run_mac.sh"
echo ""
echo "Or manually:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the application: python runShortGPT.py"
echo ""
echo "The web interface will be available at: http://localhost:31415"
echo ""
