from fastapi import FastAPI
from joblib import load
from services.rules import apply_rules

app = FastAPI()

model = load("models/moderation_model.joblib")

@app.post("/moderate")
async def moderate(payload: dict):
    text = payload.get("text", "")

    # Step 1: rule engine first
    rule = apply_rules(text)
    if rule:
        return {
            "action": rule["action"],
            "reason": rule["reason"],
            "source": "rule_engine"
        }

    # Step 2: ML model
    pred = model.predict([text])[0]
    return {
        "action": pred,
        "source": "ml_model"
    }
