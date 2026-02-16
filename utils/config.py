import os
from pathlib import Path

# Try Streamlit secrets first (for Streamlit Cloud deployment)
# Fall back to .env file (for local development)
try:
    import streamlit as st
    USAJOBS_API_KEY = st.secrets.get("USAJOBS_API_KEY", None)
    GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", None)
    RAPIDAPI_KEY = st.secrets.get("RAPIDAPI_KEY", None)
except Exception:
    USAJOBS_API_KEY = None
    GEMINI_API_KEY = None
    RAPIDAPI_KEY = None

# If secrets weren't found via Streamlit, try .env file
if not GEMINI_API_KEY:
    from dotenv import load_dotenv
    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)
    USAJOBS_API_KEY = os.getenv("USAJOBS_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")