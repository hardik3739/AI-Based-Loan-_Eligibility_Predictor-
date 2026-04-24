from pydantic import BaseModel
from typing import Optional

class LoanApplication(BaseModel):
    age: int
    income: float
    employment_years: int
    savings_ratio: float
    expense_ratio: float
    transaction_frequency: int
    income_stability_score: float
    payment_consistency: float

class PredictionResponse(BaseModel):
    eligibility: bool
    probability: float
    risk_level: str
    explanation: dict
