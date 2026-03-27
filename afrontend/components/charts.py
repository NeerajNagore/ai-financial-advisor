import streamlit as st
import matplotlib.pyplot as plt

def show_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    st.pyplot(fig)