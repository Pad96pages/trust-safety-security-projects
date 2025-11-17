from fastapi import FastAPI
from joblib import load
from services.ioc_extractor import extract_iocs
import pandas as pd

app = FastAPI()

model = load("models/threat_model.joblib")
vectorizer = load("models/vectorizer.joblib")

@app.post("/scan")
async def scan(payload: dict):
    text = payload.get("text", "")

    # Step 1: IOC Extraction
    iocs = extract_iocs(text)

    # Step 2: ML Threat Classification
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0].max()

    return {
        "prediction": pred,
        "confidence": float(prob),
        "iocs": iocs
    }
