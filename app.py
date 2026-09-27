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
    st.subheader("📚 bkwm")
    st.markdown(f"#### Welcome, {st.session_state.username}!")
    st.write("Let's find your next book!")

    genre = st.selectbox(
        "Pick a genre you like:",
        ["Fantasy", "Mystery", "Romance", "Sci-Fi", "Horror", "Non-fiction"]
    )

    if st.button("Suggest a book"):
        st.success(f"Great! We'll find you a {genre} book soon 📖")