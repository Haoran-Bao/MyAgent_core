from fastapi import FastAPI
from .db import init_db
from .audit import audit_event

app = FastAPI()

@app.on_event("startup")
def _startup():
    init_db()

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.post("/chat")
def chat(payload: dict):
    # v0: just store an audit row and echo
    audit_event(actor="user", action="CHAT", target_type="message", target_id="n/a", reason="incoming")
    text = payload.get("text", "")
    return {"reply": f"Got it: {text}"}
