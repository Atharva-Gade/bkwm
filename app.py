import streamlit as st
import random

st.set_page_config(
    page_title="bkwm",
    page_icon="bkwmfavicon.jpg",
    layout="centered"
)

books_data = {
    "Fantasy": [
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
    ],
    "Mystery": [
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
    ],
    "Romance": [
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
    ],
    "Sci-Fi": [
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
    ],
    "Horror": [
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
    ],
    "Non-fiction": [
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
        {"title": "", "author": "", "description": ""},
    ],
}

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
        book = random.choice(books_data[genre])

        if book["title"]:
            st.markdown("---")
            st.markdown(f"**{book['title']}**")
            st.write(f"by {book['author']}")
            st.caption(book["description"])
        else:
            st.warning("No books added for this genre yet!")