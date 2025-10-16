import os
from dotenv import load_dotenv

# Load .env if present
load_dotenv()

# Telegram bot token
BOT_TOKEN = os.getenv(
    "BOT_TOKEN",
    "8331695593:AAE77xNYXtS5c7MX6u97Nnx-pMrKu09RE80"  # fallback for local testing
)

# Base API URL for future backend integration (FastAPI, etc.)
API_BASE_URL = "http://localhost:8000"

# Upload limit
MAX_FILE_SIZE_MB = 25
