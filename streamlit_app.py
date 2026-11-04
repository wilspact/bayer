"""
Root entry point for Streamlit Community Cloud deployment.
Routes execution to src/ui/app.py.
"""
import sys
import os
from pathlib import Path

# Ensure root and src directory are on sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(1, str(PROJECT_ROOT))

from ui.app import main

if __name__ == "__main__":
    main()
