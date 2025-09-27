# server_api.py

from fastapi import FastAPI, Response
from pydantic import BaseModel
from moderation import moderate_content
from positive_only import score_positivity

app = FastAPI(title="PopBom AI Gate")

FEED = []  # pretend DB

# --- simple routes so browser doesn't 404 ---
@app.get("/")
def home():
    return {
        "service": "PopBom AI Gate",
        "status": "ok",
        "docs": "/docs",
        "endpoints": ["/api/upload (POST)", "/api/feed (GET)", "/health"]
    }

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/favicon.ico")
def favicon():
    return Response(status_code=204)
# --------------------------------------------

class UploadIn(BaseModel):
    caption: str
    category: str = "general"
    lang: str = "en"
    region: str = "global"

def should_publish(m, p):
    return m["action"] == "allow" and p["passesPositiveOnly"]

@app.post("/api/upload")
def upload_post(d: UploadIn):
    m = moderate_content(d.caption, lang=d.lang, region=d.region)
    p = score_positivity(d.caption, category=d.category, lang=d.lang, region=d.region)
    publish = should_publish(m, p)

    item = {
        "id": len(FEED) + 1,
        "caption": d.caption,
        "moderation": m,
        "positivity": p,
        "status": "published" if publish else ("review" if m["action"] == "review" else "blocked"),
    }
    if publish:
        FEED.append(item)
    return item

@app.get("/api/feed")
def get_feed():
    return [x for x in FEED if x["status"] == "published"]
