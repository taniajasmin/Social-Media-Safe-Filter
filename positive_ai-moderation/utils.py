from pathlib import Path
import json
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

client = OpenAI(api_key=OPENAI_API_KEY)

BASE_DIR = Path(__file__).resolve().parent
PROMPTS_DIR = BASE_DIR / "prompts"

def read_prompt(name: str, fallback: str = "") -> str:
    p = PROMPTS_DIR / name
    if p.exists():
        return p.read_text(encoding="utf-8")
    return fallback  # never crash if file is missing

def chat_json(system: str, user: str, model: str = "gpt-4o-mini") -> dict:
    """Call GPT and parse JSON content; return {} on failure."""
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        temperature=0.1,
    )
    content = resp.choices[0].message.content or "{}"
    try:
        # Model may return fenced code blocks; strip if present
        if content.strip().startswith("```"):
            content = content.split("```")[1]
            if content.startswith("json"):
                content = content[len("json"):].strip()
        return json.loads(content)
    except Exception:
        return {}
