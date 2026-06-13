import requests

BACKEND_URL = "http://127.0.0.1:8000"


def generate_prompt(payload: dict):

    response = requests.post(
        f"{BACKEND_URL}/generate-prompt",
        json=payload,
        timeout=300
    )

    response.raise_for_status()

    return response.json()