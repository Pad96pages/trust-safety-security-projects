from fastapi import FastAPI
import pandas as pd
from joblib import load

app = FastAPI()

model = load("models/fake_account_model.joblib")

@app.post("/predict")
async def predict(data: dict):
    followers = data.get("followers", 0)
    friends = data.get("friends", 0)
    statuses = data.get("statuses", 0)

    X = pd.DataFrame([{
        "followers": followers,
        "friends": friends,
        "statuses": statuses
    }])

    prediction = model.predict(X)[0]
    prob = model.predict_proba(X)[0][prediction]

    return {
        "is_bot": bool(prediction),
        "confidence": float(prob)
    }
