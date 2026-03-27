import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api/ai-advice"

def show_ai_chat():
    st.header("🤖 AI Financial Advisor")

    income = st.number_input("Income", 0)
    expenses = st.number_input("Expenses", 0)
    savings = st.number_input("Savings", 0)
    loan = st.number_input("Loan", 0)

    if st.button("Get AI Advice 🚀"):

        payload = {
            "age": 25,
            "income": income,
            "expenses": expenses,
            "savings": savings,
            "loan": loan,
            "insurance": True
        }

        try:
            response = requests.post(API_URL, json=payload)

            # 🔹 Debug output
            st.write("Status Code:", response.status_code)
            st.write("Raw Response:", response.text)

            # 🔹 Safe JSON handling
            if response.status_code == 200:
                try:
                    data = response.json()

                    # ✅ Score
                    st.subheader("💯 Score")
                    st.write(data.get("score", {}).get("score", "No score found"))

                    # ✅ AI Advice
                    st.subheader("🤖 AI Advice")
                    st.write(data.get("advice", "No advice found"))

                except Exception as e:
                    st.error("❌ JSON decode error")
                    st.write(response.text)

            else:
                st.error(f"❌ API Error: {response.status_code}")
                st.write(response.text)

        except Exception as e:
            st.error("❌ Connection Error (Backend not running?)")
            st.write(str(e))