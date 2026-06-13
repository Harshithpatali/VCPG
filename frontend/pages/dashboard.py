import streamlit as st

from components.sidebar import render_sidebar
from components.hero import render_hero
from components.metrics import render_metrics

render_sidebar()

render_hero()

st.markdown("## Dashboard")

render_metrics()

st.markdown("---")

st.markdown(
"""
### Workflow

User Idea
↓
OpenRouter Blueprint
↓
Groq Refinement
↓
Professional Mega Prompt
"""
)