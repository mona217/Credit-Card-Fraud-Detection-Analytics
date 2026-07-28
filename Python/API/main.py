import uuid
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from datetime import datetime

app = FastAPI(
    title="Credit Card Fraud Detection API",
    version="1.0"
)

# Load model and scaler
model = joblib.load("../Model/rf_model.pkl")
scaler = joblib.load("../Model/scaler.pkl")

class Transaction(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float


@app.get("/")
def home():
    return {
        "message": "Credit Card Fraud Detection API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "model": "Random Forest",
        "version": "1.0"
    }


@app.get("/model-info")
def model_info():
    return {
        "model": "Random Forest",
        "features": 30,
        "algorithm": "RandomForestClassifier",
        "best_precision": 0.97,
        "best_recall": 0.73,
        "best_f1": 0.84
    }
@app.post("/predict")
def predict(transaction: Transaction):

    # Convert incoming JSON into a DataFrame
    input_data = pd.DataFrame([transaction.dict()])

    # Predict Fraud or Genuine
    prediction = model.predict(input_data)[0]

    # Get Fraud Probability
    probability = model.predict_proba(input_data)[0][1]
    transaction_id = "TXN-" + str(uuid.uuid4())[:8].upper()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Risk Level
    if probability < 0.30:
        risk_level = "Low Risk"
        recommendation = "Approve Transaction"

    elif probability <= 0.70:
        risk_level = "Medium Risk"
        recommendation = "Send OTP Verification"

    else:
        risk_level = "High Risk"
        recommendation = "Hold Transaction and Alert Fraud Team"

    # Risk Score
    risk_score = round(probability * 100, 2)

    # Return API Response
    return {
        "Transaction ID": transaction_id,
        "Timestamp": timestamp,
        "Prediction": "Fraud" if prediction == 1 else    "Genuine",
        "Fraud Probability": round(probability, 4),
        "Risk Score (%)": risk_score,
        "Risk Level": risk_level,
        "Recommendation": recommendation,
        "Model": "Random Forest",
        "API Version": "1.0"
    }