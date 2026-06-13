import streamlit as st


def render_hero():

    st.markdown(
        """
        <div class='hero'>

        <h1>
        🚀 VCPG
        </h1>

        <h3>
        Vibe Coding Prompt Generator
        </h3>

        <p>
        Generate production-ready
        AI coding prompts using
        OpenRouter + Groq.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )