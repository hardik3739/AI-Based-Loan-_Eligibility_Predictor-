import pandas as pd

def calculate_fairness_metrics(data_path: str):
    df = pd.read_csv(data_path)
    
    if 'income_group' not in df.columns:
        df['income_group'] = pd.qcut(df['income'], q=3, labels=["Low", "Medium", "High"])

    approval_rates = df.groupby('income_group', observed=False)['eligibility'].mean().to_dict()
    
    return {
        "approval_rates_by_income": approval_rates,
        "mitigation_suggestion": "If Disparate Impact < 0.8, standard mitigation techniques (like resampling or reweighting the lower approval group) should be applied to the training dataset."
    }
