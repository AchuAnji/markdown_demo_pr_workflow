import streamlit as st
import config

st.title("Defect Dashboard")

name = st.text_input("Enter your name")
x = 1 / 0

if name:
    st.write(f"Hello {name}")
