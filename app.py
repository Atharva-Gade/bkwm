import streamlit as st

username = st.text_input("Enter your name: ")
st.title(f"Welcome, {username}!")