import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_financial_advice(data):

    income = data.get("income", 0)
    expenses = data.get("expenses", 0)
    savings = data.get("savings", 0)
    loan = data.get("loan", 0)

    score = max(0, min(100, int((savings - loan) / (income + 1) * 100)))

    prompt = f"""
    You are a financial advisor for Indian users.

    User Profile:
    Income: {income}
    Expenses: {expenses}
    Savings: {savings}
    Loan: {loan}

    Financial Score: {score}/100

    Give 5 simple actionable bullet points for financial improvement.
    """

    response = model.generate_content(prompt)

    advice = response.text

    return {
        "status": "success",
        "data": {
            "score": score,
            "breakdown": {
                "income": income,
                "expenses": expenses,
                "savings": savings,
                "loan": loan
            },
            "advice": advice
        }
    }