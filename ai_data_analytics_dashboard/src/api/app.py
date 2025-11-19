from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
import pandas as pd
from src.model.train import train_demo_model
from src.etl.etl_demo import run_etl

app = FastAPI(title="Sales Insights API")

MODEL_PATH = os.environ.get("MODEL_PATH", "models/sales_model.joblib")

class PredictRequest(BaseModel):
    units_sold: float
    price: float
    marketing_spend: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/train")
def train():
    model_path = train_demo_model(MODEL_PATH)
    return {"model_path": model_path}

@app.post("/etl")
def etl():
    data_path = run_etl()
    return {"data_path": data_path}

@app.post("/predict")
def predict(req: PredictRequest):
    if not os.path.exists(MODEL_PATH):
        train_demo_model(MODEL_PATH)
    model = joblib.load(MODEL_PATH)
    X = pd.DataFrame([{"units_sold": req.units_sold, "price": req.price, "marketing_spend": req.marketing_spend}])
    pred = model.predict(X)[0]
    return {"predicted_revenue": float(pred)}
