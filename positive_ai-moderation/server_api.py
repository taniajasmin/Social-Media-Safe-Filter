from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

from moderation import moderate_content
from positive_only import score_positivity

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY missing in .env")

app = FastAPI(title="PopBom AI Content Guard")

# NEW: root + health
@app.get("/")
def root():
    return {"service": "PopBom AI Content Guard", "docs": "/docs", "check": "/check"}

@app.get("/health")
def health():
    return {"status": "ok"}

# ---- existing schema/routes (keep or paste if missing) ----
POSITIVE_ONLY_THRESHOLD = 70
REVIEW_RISK_THRESHOLD   = 0.4
BLOCK_RISK_THRESHOLD    = 0.6

class CheckPayload(BaseModel):
    content_id: str
    user_id: str
    type: str = Field(..., pattern="^(post|comment)$")
    text: str
    lang: str = "en"
    region: str = "global"
    audience: str = "general"
    positive_only: bool = False

class CheckResult(BaseModel):
    content_id: str
    action: str
    positivity: int
    positive_only_pass: bool
    safety: dict
    rationale: str

@app.post("/check", response_model=CheckResult)
def check_content(payload: CheckPayload):
    safety_json = moderate_content(payload.text, payload.lang, payload.region)
    risk = float(safety_json.get("overallRisk", 0.0))
    safety_action = safety_json.get("action", "allow")
    if risk >= BLOCK_RISK_THRESHOLD:
        safety_action = "block"
    elif risk >= REVIEW_RISK_THRESHOLD and safety_action != "block":
        safety_action = "review"

    positivity_json = score_positivity(payload.text, payload.lang, payload.region, payload.audience)
    positivity = int(positivity_json.get("positivity", 0))
    positive_only_pass = positivity >= POSITIVE_ONLY_THRESHOLD

    final_action = safety_action
    if final_action == "allow" and payload.positive_only and not positive_only_pass:
        final_action = "review"

    return CheckResult(
        content_id=payload.content_id,
        action=final_action,
        positivity=positivity,
        positive_only_pass=positive_only_pass,
        safety=safety_json,
        rationale=safety_json.get("rationale","") or positivity_json.get("rationale","")
    )
