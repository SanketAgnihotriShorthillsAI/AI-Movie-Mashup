# streamlit.py

import streamlit as st
import requests

st.set_page_config(page_title="AI Movie Mashup", page_icon="🎬", layout="centered")

st.title("🎬 AI Movie Mashup")
st.caption("Create fun & surprising mashups between your favorite characters and genres.")

tabs = st.tabs(["Mashup Plot Generator", "Dialogue Generator", "Scene Generator", "Quick Mashup ✨"])

# --- Tab 1: Plot Generator ---
with tabs[0]:
    st.header("Mashup Plot Generator")

    genre = st.text_input("Genre", placeholder="e.g., Fantasy, Comedy, Sci-Fi")
    char1 = st.text_input("Character 1", placeholder="e.g., Naruto")
    char2 = st.text_input("Character 2", placeholder="e.g., Sherlock Holmes")

    if st.button("Generate Mashup"):
        if genre and char1 and char2:
            with st.spinner("Generating..."):
                response = requests.post("http://localhost:8000/mashup", json={
                    "genre": genre,
                    "character1": char1,
                    "character2": char2
                })
                output = response.json()
                if 'output' in output:
                    st.success("Plot Generated!")
                    st.markdown(output['output'])
                    st.toast("Plot ready! 🎉")
                else:
                    st.error(output.get('error', 'API didn\'t return output'))
        else:
            st.warning("Please fill all inputs.")

# --- Tab 2: Dialogue Generator ---
with tabs[1]:
    st.header("Dialogue Generator")

    genre_d = st.text_input("Genre", placeholder="e.g., Action, Romance, Horror")
    char1_d = st.text_input("Character 1", placeholder="e.g., Batman")
    char2_d = st.text_input("Character 2", placeholder="e.g., Light Yagami")

    if st.button("Generate Dialogue"):
        if genre_d and char1_d and char2_d:
            with st.spinner("Generating Dialogue..."):
                response = requests.post("http://localhost:8000/dialogue", json={
                    "genre": genre_d,
                    "character1": char1_d,
                    "character2": char2_d
                })
                output = response.json()
                if 'output' in output:
                    st.success("Dialogue Generated!")
                    st.markdown(output['output'])
                    st.toast("Dialogue cooked! 🗨️")
                else:
                    st.error(output.get('error', 'API didn\'t return output'))
        else:
            st.warning("Please fill all inputs.")

# --- Tab 3: Scene Generator ---
with tabs[2]:
    st.header("AI Scene Generator")

    genre_s = st.text_input("Genre", placeholder="e.g., Thriller, Mystery")
    char1_s = st.text_input("Character 1", placeholder="e.g., Iron Man")
    char2_s = st.text_input("Character 2", placeholder="e.g., L from Death Note")

    if st.button("Generate Scene"):
        if genre_s and char1_s and char2_s:
            with st.spinner("Generating Scene..."):
                response = requests.post("http://localhost:8000/scene", json={
                    "genre": genre_s,
                    "character1": char1_s,
                    "character2": char2_s
                })
                output = response.json()
                if 'output' in output:
                    st.success("Scene Generated!")
                    st.markdown(output['output'])
                    st.toast("Scene created! 🎥")
                else:
                    st.error(output.get('error', 'API didn\'t return output'))
        else:
            st.warning("Please fill all inputs.")

# --- Tab 4: Quick Mashup ---
with tabs[3]:
    st.header("Quick Mashup ✨")

    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        quick_input = st.text_area("Describe your mashup", 
                                   placeholder="e.g., What if Tony Stark from Marvel met Death Note's L?")

    with col2:
        if st.button("Random Example"):
            quick_input = "What if Tony Stark from Marvel met Death Note's L?"
            st.experimental_rerun()

    if st.button("Generate Quick Mashup"):
        if quick_input.strip() == "":
            st.warning("Please enter a scenario.")
        else:
            with st.spinner("Generating Quick Mashup..."):
                response = requests.post("http://localhost:8000/quick_mashup", json={
                    "user_input": quick_input
                })
                output = response.json()
                if 'output' in output:
                    st.success("Quick Mashup Generated!")
                    st.markdown(output['output'])
                    st.toast("Quick Mashup ready! ✨")
                else:
                    st.error(output.get('error', 'API didn\'t return output'))
