import streamlit as st


def render_stepper(step):

    labels = [
        "Idea",
        "OS",
        "Language",
        "Purpose",
        "Deploy",
        "Generate"
    ]

    cols = st.columns(len(labels))

    for i,label in enumerate(labels):

        if i < step:
            cols[i].success(label)

        elif i == step:
            cols[i].warning(label)

        else:
            cols[i].info(label)