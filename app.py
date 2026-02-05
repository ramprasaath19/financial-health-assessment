from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load the trained risk assessment model
model = joblib.load('./models/risk_assessment_model_xgb.joblib')

# Define a request model to receive user data
class FinancialData(BaseModel):
    income: float
    expenses: float

@app.post("/assess_risk/")
async def assess_risk(data: FinancialData):
    # Use the loaded model to assess risk
    features = [[data.income, data.expenses]]
    risk_level = model.predict(features)[0]
    return {"risk_level": risk_level}
