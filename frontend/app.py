import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="VCPG",
    page_icon="🚀",
    layout="wide"
)

css_file = (
    Path(__file__).parent
    / "styles"
    / "theme.css"
)

with open(css_file) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.switch_page(
    "pages/dashboard.py"
)