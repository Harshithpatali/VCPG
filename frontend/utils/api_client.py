import requests
import streamlit as st
BACKEND_URL = st.secrets["BACKEND_URL"]


def generate_prompt(payload: dict):

    response = requests.post(
        f"{BACKEND_URL}/generate-prompt",
        json=payload,
        timeout=300
    )

    response.raise_for_status()

    return response.json()