import streamlit as st

from components.sidebar import render_sidebar
from components.prompt_viewer import render_prompt

render_sidebar()

st.title(
    "Generated Prompt"
)

prompt = st.session_state.get(
    "generated_prompt",
    ""
)

if prompt:

    render_prompt(prompt)

else:

    st.warning(
        "No prompt generated yet."
    )