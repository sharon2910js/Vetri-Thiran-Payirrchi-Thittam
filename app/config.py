from pathlib import Path
import os

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY",
    ""
)

GEMINI_OUTLINE_MODEL = os.getenv(
    "GEMINI_OUTLINE_MODEL",
    "gemini-2.5-flash"
)

GEMINI_STORY_MODEL = os.getenv(
    "GEMINI_STORY_MODEL",
    "gemini-2.5-flash"
)

HF_TOKEN = os.getenv(
    "HF_TOKEN",
    ""
)

HF_IMAGE_MODEL = os.getenv(
    "HF_IMAGE_MODEL",
    "black-forest-labs/FLUX.1-schnell"
)

HF_PROVIDER = os.getenv(
    "HF_PROVIDER",
    "auto"
)

MOCK_AI = os.getenv(
    "MOCK_AI",
    "true"
).lower() == "true"