from pathlib import Path


PROMPTS_DIR = Path("prompts")


def load_prompt(filename: str) -> str:
    file_path = PROMPTS_DIR / filename

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:
        return file.read()