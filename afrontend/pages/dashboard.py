import streamlit as st

def show_dashboard():
    st.header("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Monthly Income", "₹50,000")
    col2.metric("📉 Expenses", "₹30,000")
    col3.metric("💯 Score", "72/100")

    st.subheader("📈 Financial Overview")
    st.info("Track your savings, investments, and financial health here.")