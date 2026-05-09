from fastapi import FastAPI
import joblib
import numpy as np
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MLOps Pipeline Running"}

@app.get("/metrics")
def get_metrics():
    # Read fresh from disk every time — never use cached value
    with open("metrics.json") as f:
        return json.load(f)

@app.post("/predict")
def predict(data: dict):
    model = joblib.load("model.pkl")
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)[0]
    return {"prediction": int(prediction)}
