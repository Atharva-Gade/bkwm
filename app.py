import streamlit as st
import random

st.set_page_config(
    page_title="bkwm",
    page_icon="bkwmfavicon.jpg",
    layout="centered"
)

books_data = {
    "Fantasy": [
    {"title": "Caraval", "author": "Stephanie Garber", "description": "A young adult fantasy novel about two sisters who enter a magical, immersive game where reality and illusion blur"},
    {"title": "Fourth Wing", "author": "Rebecca Yarros", "description": "A brutal war college for aspiring dragon riders where a fragile newcomer must survive lethal trials and a dangerous, magnetic rival."},
    {"title": "Once Upon a Broken Heart", "author": "Stephanie Garber", "description": "Evangeline Fox strikes a bargain with the charismatic, wicked Prince of Hearts. It features the same magical, circus-like wonder and high-stakes curses."},
    {"title": "Powerless", "author": "Lauren Roberts", "description": "An ordinary girl without magical powers must fake her abilities to survive a deadly royal competition while hiding her identity from the prince sworn to hunt her kind"},
    {"title": "The Cruel Prince", "author": "Holly Black", "description": "A dark fantasy novel about a human girl named Jude who fights for power and survival in the lethal, magical Court of Faerie after her parents are murdered."},
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