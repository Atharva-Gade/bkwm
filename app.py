import streamlit as st
import requests
import random

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
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": f"subject:{genre}",
            "maxResults": 20
        }
        response = requests.get(url, params=params)
        st.write("Status code:", response.status_code)
        st.write(response.json())
        data = response.json()

        if "items" in data and len(data["items"]) > 0:
            book = random.choice(data["items"])
            info = book["volumeInfo"]

            title = info.get("title", "Unknown Title")
            authors = ", ".join(info.get("authors", ["Unknown Author"]))
            description = info.get("description", "No description available.")
            thumbnail = info.get("imageLinks", {}).get("thumbnail", None)

            st.markdown("---")
            col1, col2 = st.columns([1, 2])
            with col1:
                if thumbnail:
                    st.image(thumbnail, use_container_width=True)
            with col2:
                st.markdown(f"**{title}**")
                st.write(f"by {authors}")
                st.caption(description[:200] + "..." if len(description) > 200 else description)
        else:
            st.error("Couldn't find a book for that genre, try another one.")