import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from the project root (one level up from utils/)
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

USAJOBS_API_KEY = os.getenv("USAJOBS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")