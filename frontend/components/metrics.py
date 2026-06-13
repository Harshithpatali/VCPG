import streamlit as st


def render_metrics():

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric(
            "Prompts",
            "120+"
        )

    with col2:
        st.metric(
            "Agents",
            "2"
        )

    with col3:
        st.metric(
            "Models",
            "OpenRouter + Groq"
        )

    with col4:
        st.metric(
            "Version",
            "1.0"
        )