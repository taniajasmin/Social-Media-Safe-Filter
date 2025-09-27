from utils import read_prompt, chat_json

POSITIVITY_THRESHOLD = 70  # tweak per audience

def score_positivity(text: str, category="general", lang="en", region="global") -> dict:
    system = read_prompt("positivity_system.txt", fallback="""
Output JSON with keys positivity,tags,rationale.
""")
    user = read_prompt("positivity_user.txt", fallback="text: {{text}}").replace("{{text}}", text)
    user = (user
            .replace("{{category}}", category)
            .replace("{{lang}}", lang)
            .replace("{{region}}", region))

    data = chat_json(system, user)
    data["positivity"] = int(data.get("positivity", 0))
    data["tags"] = data.get("tags") or []
    data["passesPositiveOnly"] = data["positivity"] >= POSITIVITY_THRESHOLD
    return data
