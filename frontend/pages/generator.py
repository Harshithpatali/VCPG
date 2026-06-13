import streamlit as st

from components.sidebar import render_sidebar
from components.stepper import render_stepper

from utils.api_client import generate_prompt

render_sidebar()

st.title(
    "Generate Prompt"
)

render_stepper(0)

idea = st.text_area(
    "Project Idea"
)

os_choice = st.selectbox(
    "Operating System",
    [
        "Windows",
        "Linux",
        "macOS"
    ]
)

language = st.selectbox(
    "Language",
    [
        "Python",
        "JavaScript",
        "Java",
        "C++"
    ]
)

purpose = st.selectbox(
    "Purpose",
    [
        "Portfolio Project",
        "Production Application"
    ]
)

explanation = st.checkbox(
    "Detailed Explanation"
)

backend = st.selectbox(
    "Backend Deployment",
    [
        "Render",
        "AWS",
        "Railway",
        "Docker"
    ]
)

frontend = st.selectbox(
    "Frontend Deployment",
    [
        "Streamlit Cloud",
        "Vercel",
        "Netlify"
    ]
)

if st.button(
    "🚀 Generate Prompt"
):

    with st.spinner(
        "AI Agents Working..."
    ):

        payload = {
            "project_idea": idea,
            "os": os_choice,
            "language": language,
            "purpose": purpose,
            "explanation": explanation,
            "backend_deployment": backend,
            "frontend_deployment": frontend
        }

        result = generate_prompt(
            payload
        )

        st.session_state[
            "generated_prompt"
        ] = result[
            "final_prompt"
        ]

        st.success(
            "Prompt Generated"
        )