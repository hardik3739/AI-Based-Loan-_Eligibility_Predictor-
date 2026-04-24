import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'rf_model.joblib')

def train_and_save_model(data_path: str):
    df = pd.read_csv(data_path)
    
    X = df.drop(columns=['eligibility', 'income_group'])
    y = df['eligibility']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Baseline Model
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train, y_train)
    lr_preds = lr.predict(X_test)
    print(f"Logistic Regression Accuracy: {accuracy_score(y_test, lr_preds):.4f}")
    
    # Advanced Model
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    rf_preds = rf.predict(X_test)
    print(f"Random Forest Accuracy: {accuracy_score(y_test, rf_preds):.4f}")
    
    joblib.dump(rf, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

def load_model():
    return joblib.load(MODEL_PATH)

def predict(model, input_data: pd.DataFrame):
    proba = model.predict_proba(input_data)[0][1]
    eligibility = bool(model.predict(input_data)[0])
    
    if proba > 0.7:
        risk_level = "Low"
    elif proba > 0.4:
        risk_level = "Medium"
    else:
        risk_level = "High"
        
    return eligibility, float(proba), risk_level
