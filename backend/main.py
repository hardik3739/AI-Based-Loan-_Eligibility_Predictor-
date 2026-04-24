from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from io import StringIO
import os

from schemas import LoanApplication, PredictionResponse
from feature_engineering import process_features
from model import load_model, predict, train_and_save_model
from explain import get_explanation
from fairness import calculate_fairness_metrics

app = FastAPI(title="AI Loan Predictor API", description="Predicts loan eligibility using ML and alternative data.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = None
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'sample_transactions.csv')

@app.on_event("startup")
def startup_event():
    global model
    try:
        model = load_model()
        print("Model loaded successfully.")
    except FileNotFoundError:
        print("Model not found. Initializing training...")
        if os.path.exists(DATA_PATH):
            train_and_save_model(DATA_PATH)
            model = load_model()
        else:
            print("WARNING: Dataset not found. Please run generate_dataset.py first.")

@app.post("/predict", response_model=PredictionResponse)
def predict_eligibility(application: LoanApplication):
    df = pd.DataFrame([application.model_dump()])
    features = process_features(df)
    
    eligibility, probability, risk = predict(model, features)
    explanation = get_explanation(model, features)
    
    return PredictionResponse(
        eligibility=eligibility,
        probability=probability,
        risk_level=risk,
        explanation=explanation
    )

@app.post("/explain")
async def explain_from_csv(file: UploadFile = File(...)):
    contents = await file.read()
    s = str(contents, 'utf-8')
    data = StringIO(s) 
    df = pd.read_csv(data)
    
    features = process_features(df)
    
    results = []
    for i in range(len(features)):
        row = features.iloc[[i]]
        eligibility, probability, risk = predict(model, row)
        explanation = get_explanation(model, row)
        results.append({
            "id": i,
            "eligibility": eligibility,
            "probability": probability,
            "risk_level": risk,
            "explanation": explanation
        })
        
    return {"results": results}

@app.get("/fairness")
def get_fairness_report():
    if not os.path.exists(DATA_PATH):
        return {"error": "Dataset not found"}
    return calculate_fairness_metrics(DATA_PATH)

@app.get("/")
def health_check():
    return {"status": "Backend is running correctly"}
