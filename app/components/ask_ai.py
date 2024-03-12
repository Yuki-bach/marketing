import base64
import io
import os
import streamlit as st
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from openai import OpenAI

# setup OpenAI client
load_dotenv()
os.environ["OPENAI_API_KEY"] = (
    os.getenv("OPENAI_API_KEY")
    if os.getenv("IS_LOCAL")
    else st.secrets["OPENAI_API_KEY"]
)
client = OpenAI()


def ask_ai(fig=None):
    if st.button("Ask AI"):
        image_base64 = __convert_plot_to_base64(fig)
        __call_api_and_display_answer(image_base64)


def __convert_plot_to_base64(fig=None):
    buf = io.BytesIO()
    if fig:
        fig.savefig(buf, format="png", bbox_inches="tight")
    else:
        plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode("utf-8")
    buf.close()
    return image_base64


def __call_api_and_display_answer(image_base64):
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Interpret this chart briefly."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_base64}",
                        "detail": "high",
                    },
                },
            ],
        }
    ]

    # Get AI response
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=messages,
        max_tokens=300,
        stream=True,  # stream response
    )

    # Display AI response
    expander = st.expander("AI Answer", expanded=True)
    placeholder = expander.empty()
    message = ""
    for chunk in response:
        chunk_message = (
            chunk.choices[0].delta.content
            if chunk.choices[0].delta.content is not None
            else ""
        )
        if chunk_message:
            message += chunk_message
            placeholder.write(message)

    return chunk_message
