from utils import read_prompt, chat_json

# Simple policy thresholds
BLOCK_AT = 0.70
REVIEW_AT = 0.50

def moderate_content(text: str, lang="en", age=18, region="global") -> dict:
    system = read_prompt("moderation_system.txt", fallback="""
Output JSON with keys violence,hate,sexual,scam,abuse,overallRisk,action,rationale.
""")
    user = read_prompt("moderation_user.txt", fallback="text: {{text}}").replace("{{text}}", text)
    user = user.replace("{{lang}}", str(lang)).replace("{{age}}", str(age)).replace("{{region}}", str(region))

    data = chat_json(system, user)

    # Post-process if model omitted fields
    for k in ["violence","hate","sexual","scam","abuse","overallRisk"]:
        data[k] = float(data.get(k, 0.0))
    data["action"] = data.get("action") or "allow"

    # Enforce local thresholds regardless of model suggestion
    risk = max(data["violence"], data["hate"], data["sexual"], data["scam"], data["abuse"], data["overallRisk"])
    if risk >= BLOCK_AT:
        action = "block"
    elif risk >= REVIEW_AT:
        action = "review"
    else:
        action = "allow"

    data["action"] = action
    return data
