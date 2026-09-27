import streamlit as st

st.set_page_config(
    page_title="bkwm",
    page_icon="bkwmfavicon.jpg",
    layout="centered"
)

if "username" not in st.session_state:
    st.session_state.username = None

if st.session_state.username is None:
    with st.form("name_form"):
        name = st.text_input("Enter your name:")
        submitted = st.form_submit_button("Submit")
        if submitted and name:
            st.session_state.username = name
            st.rerun()
else:
    st.title(f"Welcome, {st.session_state.username}!")