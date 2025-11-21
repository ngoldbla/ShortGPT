# 🍎 ShortGPT - Mac Setup Guide

Get ShortGPT running on your Mac with minimal effort!

## Quick Start (3 Simple Steps)

### Step 1: Run the Setup Script

```bash
./setup_mac.sh
```

This will automatically:
- Check for Homebrew (and prompt you to install if needed)
- Install Python 3.10+ if not present
- Install FFmpeg if not present
- Create a Python virtual environment
- Install all required Python packages
- Create a `.env` file template for your API keys

### Step 2: Add Your API Keys

Edit the `.env` file and add your API keys:

```bash
nano .env
```

**Minimum Required:**
- **Gemini API Key** (FREE) - Get it from https://makersuite.google.com/app/apikey
  - ShortGPT prioritizes Gemini as it's free and powerful
- **Pexels API Key** (FREE) - Get it from https://www.pexels.com/api/

**Optional:**
- OpenAI API Key - Fallback option if you prefer OpenAI
- ElevenLabs API Key - For premium voice synthesis (EdgeTTS is used as free alternative)

### Step 3: Run ShortGPT

```bash
./run_mac.sh
```

The web interface will open at: **http://localhost:31415**

## Manual Setup (Alternative)

If you prefer to set things up manually:

### Prerequisites

1. **Homebrew** (if not installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Python 3.10+**:
   ```bash
   brew install python@3.10
   ```

3. **FFmpeg**:
   ```bash
   brew install ffmpeg
   ```

### Installation

1. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   ```

2. **Activate virtual environment**:
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup API keys**:
   ```bash
   cp .env.example .env
   nano .env  # Add your API keys
   ```

5. **Run the application**:
   ```bash
   python runShortGPT.py
   ```

## Getting API Keys

### Gemini API (FREE - Recommended)
1. Go to https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key to your `.env` file

### Pexels API (FREE)
1. Go to https://www.pexels.com/api/
2. Sign up for a free account
3. Your API key will be shown in your account dashboard
4. Copy the key to your `.env` file

### OpenAI API (Optional - Paid)
1. Go to https://platform.openai.com/api-keys
2. Create an account and add payment method
3. Create a new API key
4. Copy the key to your `.env` file

### ElevenLabs API (Optional - Paid)
1. Go to https://elevenlabs.io/
2. Sign up for an account
3. Navigate to your profile settings to find your API key
4. Copy the key to your `.env` file

Note: If you don't provide an ElevenLabs key, ShortGPT will use Microsoft's free EdgeTTS for voice synthesis.

## Troubleshooting

### Python version issues
If you have multiple Python versions installed, you may need to specify Python 3.10:
```bash
python3.10 -m venv venv
```

### FFmpeg not found
Make sure Homebrew's bin directory is in your PATH:
```bash
echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Port 31415 already in use
Kill the process using the port:
```bash
lsof -ti:31415 | xargs kill -9
```

### Dependencies installation fails
Try upgrading pip first:
```bash
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## What ShortGPT Can Do

- Create automated YouTube Shorts and TikTok videos
- Generate scripts using AI (Gemini/OpenAI)
- Source video footage automatically from Pexels
- Add AI voiceovers in 30+ languages
- Generate captions automatically
- Translate and dub videos to different languages

## Need Help?

- Check the main README.md for more details
- Join the Discord: https://discord.gg/uERx39ru3R
- Or use the Google Colab version: https://colab.research.google.com/drive/1_2UKdpF6lqxCqWaAcZb3rwMVQqtbisdE

## Docker Alternative

If you prefer Docker:
```bash
docker build -t short_gpt_docker:latest .
docker run -p 31415:31415 --env-file .env short_gpt_docker:latest
```
