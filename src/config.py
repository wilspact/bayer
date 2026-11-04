"""
Configuration module for the campaign engine.
Handles API keys, environment settings, and system-wide constants.
"""
import os
from dotenv import load_dotenv

load_dotenv()

def get_gemini_api_key() -> str:
    """
    Retrieves the Gemini API key.
    Checks streamlit secrets first (for Streamlit Community Cloud), then environment variables.
    """
    try:
        import streamlit as st
        if "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass
    return os.getenv("GEMINI_API_KEY")

DEFAULT_MODEL = "gemini-2.5-flash"
