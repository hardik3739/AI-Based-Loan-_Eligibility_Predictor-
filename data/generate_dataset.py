import pandas as pd
import numpy as np
import os

def generate_data(num_samples=5000):
    np.random.seed(42)
    
    # 1. Traditional Data
    age = np.random.randint(21, 60, size=num_samples)
    income = np.random.normal(60000, 20000, size=num_samples)
    income = np.clip(income, 20000, 200000)
    employment_years = np.random.randint(0, 30, size=num_samples)
    
    # Income groups for fairness later
    income_group = pd.qcut(income, q=3, labels=["Low", "Medium", "High"])
    
    # 2. Alternative Data & Engineered Features
    # Savings ratio (savings/income)
    savings_ratio = np.random.beta(2, 5, size=num_samples) 
    
    # Expense ratio (expenses/income)
    expense_ratio = np.random.beta(5, 2, size=num_samples)
    expense_ratio = np.clip(expense_ratio, 0.1, 0.95)
    
    # Transaction frequency (transactions per month)
    transaction_frequency = np.random.poisson(30, size=num_samples)
    
    # Income stability score (0.0 to 1.0)
    income_stability_score = np.random.uniform(0.3, 1.0, size=num_samples)
    # Give higher income guys slightly higher stability
    income_stability_score += (income / 200000) * 0.2
    income_stability_score = np.clip(income_stability_score, 0, 1)

    # Payment consistency (0.0 to 1.0, representing % of bills paid on time)
    payment_consistency = np.random.beta(8, 2, size=num_samples)
    
    # Create a base score for eligibility based on sensible financial indicators
    # High savings, low expense, high consistency -> higher score
    base_score = (
        0.3 * (income / 100000) + 
        0.2 * savings_ratio - 
        0.3 * expense_ratio + 
        0.2 * income_stability_score + 
        0.3 * payment_consistency
    )
    
    # Add some noise
    base_score += np.random.normal(0, 0.2, size=num_samples)
    
    # Determine eligibility (top 60% approx approved)
    threshold = np.percentile(base_score, 40)
    eligibility = (base_score >= threshold).astype(int)
    
    # Create DataFrame
    df = pd.DataFrame({
        'age': age,
        'income': income,
        'income_group': income_group,
        'employment_years': employment_years,
        'savings_ratio': savings_ratio,
        'expense_ratio': expense_ratio,
        'transaction_frequency': transaction_frequency,
        'income_stability_score': income_stability_score,
        'payment_consistency': payment_consistency,
        'eligibility': eligibility
    })
    
    # Save to CSV
    os.makedirs(os.path.dirname(__file__), exist_ok=True)
    df.to_csv(os.path.join(os.path.dirname(__file__), 'sample_transactions.csv'), index=False)
    print(f"Generated dataset with {num_samples} samples.")

if __name__ == "__main__":
    generate_data()
