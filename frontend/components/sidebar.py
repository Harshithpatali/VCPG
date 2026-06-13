import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("🚀 VCPG")

        st.markdown("---")

        st.page_link(
            "pages/dashboard.py",
            label="Dashboard"
        )

        st.page_link(
            "pages/generator.py",
            label="Generator"
        )

        st.page_link(
            "pages/results.py",
            label="Results"
        )

        st.markdown("---")

        st.info(
            "Version 1.0"
        )