import streamlit as st
import config

st.title("Defect Dashboard")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello {name}")
