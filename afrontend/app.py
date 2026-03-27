import streamlit as st

st.set_page_config(page_title="AI Money Mentor", layout="wide")

st.title("💰 AI Money Mentor")
st.markdown("Your AI-powered financial advisor")

st.sidebar.title("Navigation")

# page = st.sidebar.radio("Go to", [
#     "Dashboard",
#     "Health Score",
# ])
page = st.sidebar.radio("Go to", [
    "Dashboard",
    "Health Score",
    "AI Advisor"
])

if page == "Dashboard":
    from pages.dashboard import show_dashboard
    show_dashboard()

elif page == "Health Score":
    from pages.health_score import show_health_score
    show_health_score()

elif page == "AI Advisor":
    from pages.ai_chat import show_ai_chat
    show_ai_chat()