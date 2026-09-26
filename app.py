import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "home"
if "genre" not in st.session_state:
    st.session_state.genre = None

if st.session_state.page == "home":
    st.title("📚 bkwm")
    st.write("Let's find your next book!")

    genre = st.selectbox(
        "Pick a genre you like:",
        ["Fantasy", "Mystery", "Romance", "Sci-Fi", "Horror", "Non-fiction"]
    )

    if st.button("Suggest a book"):
        st.session_state.genre = genre
        st.session_state.page = "results"
        st.rerun()

elif st.session_state.page == "results":
    st.title(f"{st.session_state.genre} books you might like:")
    
    if st.button("← Back"):
        st.session_state.page = "home"
        st.rerun()