# streamlit.py

import streamlit as st
import requests

st.set_page_config(page_title="AI Movie Mashup", page_icon="🎬", layout="centered")

st.title("🎬 AI Movie Mashup Generator")

tabs = st.tabs(["🎥 Mashup Plot", "🗣️ Dialogue Generator", "🎭 Scene Generator"])

with tabs[0]:
    st.header("Mashup Plot")
    movie1 = st.text_input("Enter First Movie/Show")
    movie2 = st.text_input("Enter Second Movie/Show")
    genre = st.text_input("Genre")
    extra = st.text_area("Any extra context (Optional)")

    if st.button("Generate Mashup Plot"):
        with st.spinner("Generating..."):
            response = requests.post("http://localhost:8000/generate", json={
                "movie1": movie1,
                "movie2": movie2,
                "genre": genre,
                "extra_context": extra
            })
            output = response.json()
            if 'output' in output:
                st.success("Mashup Plot Generated!")
                st.markdown(output['output'])
            else:
                st.error(output.get('error', 'API didn\'t return output'))

with tabs[1]:
    st.header("Dialogue Generator")
    movie1_d = st.text_input("First Movie/Show", key="dlg1")
    movie2_d = st.text_input("Second Movie/Show", key="dlg2")
    genre_d = st.text_input("Genre", key="dlg3")
    scene_desc = st.text_area("Describe the Scene")

    if st.button("Generate Dialogue"):
        with st.spinner("Generating Dialogue..."):
            response = requests.post("http://localhost:8000/dialogue", json={
                "movie1": movie1_d,
                "movie2": movie2_d,
                "genre": genre_d,
                "scene_desc": scene_desc
            })
            output = response.json()
            if 'output' in output:
                st.success("Dialogue Generated!")
                st.markdown(output['output'])
            else:
                st.error(output.get('error', 'API didn\'t return output'))

with tabs[2]:
    st.header("Scene Generator")
    movie1_s = st.text_input("First Movie/Show", key="scn1")
    movie2_s = st.text_input("Second Movie/Show", key="scn2")
    genre_s = st.text_input("Genre", key="scn3")
    scene_idea = st.text_area("Scene Idea")

    if st.button("Generate Scene"):
        with st.spinner("Generating Scene..."):
            response = requests.post("http://localhost:8000/scene", json={
                "movie1": movie1_s,
                "movie2": movie2_s,
                "genre": genre_s,
                "scene_idea": scene_idea
            })
            output = response.json()
            if 'output' in output:
                st.success("Scene Generated!")
                st.markdown(output['output'])
            else:
                st.error(output.get('error', 'API didn\'t return output'))
