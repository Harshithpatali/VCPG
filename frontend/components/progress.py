import streamlit as st


def render_progress(step):

    progress_map = {
        1: 0.33,
        2: 0.66,
        3: 1.0
    }

    st.progress(
        progress_map.get(step, 0)
    )