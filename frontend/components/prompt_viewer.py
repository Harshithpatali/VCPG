import streamlit as st


def render_prompt(prompt):

    tab1,tab2 = st.tabs(
        [
            "Preview",
            "Raw"
        ]
    )

    with tab1:
        st.markdown(prompt)

    with tab2:
        st.code(
            prompt,
            language="markdown"
        )

    st.download_button(
        "Download TXT",
        prompt,
        "vcpg_prompt.txt"
    )