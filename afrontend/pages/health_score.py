import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api/health-score"

def show_health_score():
    st.header("💯 Money Health Score")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 80)
        income = st.number_input("Monthly Income (₹)", min_value=0)
        expenses = st.number_input("Monthly Expenses (₹)", min_value=0)

    with col2:
        savings = st.number_input("Current Savings (₹)", min_value=0)
        loan = st.number_input("Loan Amount (₹)", min_value=0)
        insurance = st.selectbox("Insurance", ["Yes", "No"])

    if st.button("Analyze 🚀"):

        payload = {
            "age": age,
            "income": income,
            "expenses": expenses,
            "savings": savings,
            "loan": loan,
            "insurance": True if insurance == "Yes" else False
        }

    try:
        response = requests.post(API_URL, json=payload)

        # 🔥 DEBUG LINE
        st.write("Full API Response:", response.json())

        result = response.json()["data"]

        st.success(f"💯 Your Score: {result['score']}/100")

        st.subheader("📊 Breakdown")
        for key, value in result["breakdown"].items():
            st.write(f"{key}: {value}")

        st.subheader("🤖 Recommendations")
        for rec in result["recommendations"]:
            st.write(f"✅ {rec}")

    except Exception as e:
        st.error(f"Error: {e}")