# scripts/generate_data.py
import numpy as np
import pandas as pd

# Generate mock data
np.random.seed(0)  # For reproducibility
n_samples = 100
income = np.random.normal(50000, 10000, n_samples)
expenses = np.random.normal(30000, 5000, n_samples)
investment_preferences = np.random.choice(['Low', 'Medium', 'High'], n_samples)

# Create a DataFrame
data = pd.DataFrame({'Income': income, 'Expenses': expenses, 'Risk Preference': investment_preferences})

# Save the mock data to a CSV file
data.to_csv('data/financial_data.csv', index=False)
