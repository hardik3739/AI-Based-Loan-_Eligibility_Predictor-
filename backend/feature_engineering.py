import pandas as pd
import numpy as np

def engineer_transaction_features(raw_tx_df: pd.DataFrame) -> pd.DataFrame:
    """
    Simulates feature engineering from raw transaction data.
    Aggregates a transaction log and engineers the required alternative data features.
    """
    # 1. Transaction Frequency
    tx_freq = len(raw_tx_df)
    
    # 2. Income and Expense calculations
    if 'amount' in raw_tx_df.columns:
        # Identify incoming vs outgoing money
        credits = raw_tx_df[raw_tx_df['amount'] > 0]['amount'].sum()
        debits = raw_tx_df[raw_tx_df['amount'] < 0]['amount'].abs().sum()
    else:
        credits = 60000.0
        debits = 20000.0
        
    income = credits if credits > 0 else 60000.0
    
    # 3. Ratios
    savings_ratio = (income - debits) / income if income > 0 else 0.1
    savings_ratio = np.clip(savings_ratio, 0.0, 1.0)
    
    expense_ratio = debits / income if income > 0 else 0.5
    expense_ratio = np.clip(expense_ratio, 0.0, 1.0)
    
    # 4. Behavioral Indicators
    income_stability_score = 0.85 if 'date' in raw_tx_df.columns else 0.75
    payment_consistency = 0.90 
    
    # Base demographics (use existing or fallback to averages)
    age = raw_tx_df['age'].iloc[0] if 'age' in raw_tx_df.columns else 35
    employment_years = raw_tx_df['employment_years'].iloc[0] if 'employment_years' in raw_tx_df.columns else 5
    
    engineered_data = {
        'age': age,
        'income': income,
        'employment_years': employment_years,
        'savings_ratio': float(savings_ratio),
        'expense_ratio': float(expense_ratio),
        'transaction_frequency': int(tx_freq),
        'income_stability_score': float(income_stability_score),
        'payment_consistency': float(payment_consistency)
    }
    
    return pd.DataFrame([engineered_data])


def process_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Main feature engineering pipeline.
    Handles both pre-processed json payloads (from UI) and raw transaction CSVs.
    """
    required_features = [
        'age', 'income', 'employment_years', 'savings_ratio', 
        'expense_ratio', 'transaction_frequency', 
        'income_stability_score', 'payment_consistency'
    ]
    
    # Check if the data is already pre-engineered (e.g., from the web form)
    if all(col in df.columns for col in required_features):
        return df[required_features]
        
    # If missing ML columns, it must be raw data: engineer the features
    engineered_df = engineer_transaction_features(df)
    
    return engineered_df[required_features]
