# Gemini API Setup Guide for AutoHedge

This guide explains how to configure AutoHedge to use Google's Gemini API instead of OpenAI.

## What Changed

All AI agents in AutoHedge have been configured to use **Gemini 2.0 Flash** model instead of OpenAI GPT-4 or Groq models.

### Modified Agents:
- ✅ **Sentiment Agent**: `gemini-2.0-flash-exp`
- ✅ **Risk Manager**: `gemini-2.0-flash-exp`
- ✅ **Execution Agent**: `gemini-2.0-flash-exp`
- ✅ **Trading Director**: `gemini-2.0-flash-exp`
- ✅ **Quant Analyst**: `gemini-2.0-flash-exp`

## Setup Instructions

### Step 1: Get Your Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Click **"Get API Key"** or **"Create API Key"**
4. Copy your API key (it will look like: `AIza...`)

### Step 2: Configure Environment Variables

Edit your `.env` file in the project root:

```bash
# Gemini API Configuration
OPENAI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
OPENAI_API_BASE=https://generativelanguage.googleapis.com/v1beta/openai/
WORKSPACE_DIR=agent_workspace
```

**Important Notes:**
- Replace `AIzaSyXXX...` with your actual Gemini API key
- The `OPENAI_API_BASE` tells the system to use Gemini's OpenAI-compatible endpoint
- Keep the variable name as `OPENAI_API_KEY` (the swarms library uses this name)

### Step 3: Install Dependencies

Make sure you have all required packages installed:

```bash
# Activate your virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install the missing langchain-community package
pip install langchain-community
```

### Step 4: Run the Application

```bash
# Make sure venv is activated
source .venv/bin/activate

# Run the example
python3 example.py
```

## Alternative: Set Environment Variables in Terminal

If you don't want to use a `.env` file, you can set environment variables directly:

```bash
export OPENAI_API_KEY="AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
export OPENAI_API_BASE="https://generativelanguage.googleapis.com/v1beta/openai/"
export WORKSPACE_DIR="agent_workspace"

python3 example.py
```

## Available Gemini Models

You can use different Gemini models by changing the `model_name` in `autohedge/main.py`:

| Model Name | Description |
|------------|-------------|
| `gemini-2.0-flash-exp` | Latest experimental flash model (fastest) |
| `gemini-1.5-flash` | Stable flash model |
| `gemini-1.5-pro` | More capable, slower |
| `gemini-2.5-flash` | Newer flash version |

## Troubleshooting

### Error: "Did not find openai_api_key"
- Make sure your `.env` file has `OPENAI_API_KEY` set
- Verify the API key is valid
- Try setting it directly in terminal: `export OPENAI_API_KEY="your-key"`

### Error: "ModuleNotFoundError: No module named 'langchain_community'"
```bash
pip install langchain-community
```

### Error: "Invalid API key"
- Verify your Gemini API key is correct
- Check if you have API quota remaining at [Google AI Studio](https://aistudio.google.com/)

### Model Not Found
- Make sure you're using a valid Gemini model name
- Check the [Gemini API documentation](https://ai.google.dev/gemini-api/docs/models) for available models

## Testing Your Setup

Create a simple test file `test_gemini.py`:

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.0-flash-exp",
    messages=[
        {"role": "user", "content": "Say hello!"}
    ]
)

print(response.choices[0].message.content)
```

Run it:
```bash
python3 test_gemini.py
```

If this works, your Gemini API is configured correctly!

## Cost Comparison

Gemini API is generally more cost-effective than OpenAI:

- **Gemini 2.0 Flash**: Free tier available, very affordable
- **OpenAI GPT-4**: More expensive
- **Groq**: Fast but requires separate API key

## Support

- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [Google AI Studio](https://aistudio.google.com/)
- [AutoHedge GitHub Issues](https://github.com/The-Swarm-Corporation/AutoHedge/issues)
