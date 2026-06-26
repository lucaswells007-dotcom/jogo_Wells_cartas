import streamlit as st
import os
from google import genai
from google.genai import types
from google.genai.errors import ClientError



GEMINI_API_KEY = st.secrets['GEMINI_API_KEY']

def consultar_juiz(
    input_text: str = "What is in this audio?",
    audio_file=None,
):
    client = genai.Client(
        api_key=GEMINI_API_KEY,
    )

    model = "gemini-3-flash-preview"

    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="MINIMAL",
        ),
        max_output_tokens=1024,
        tools=None,
    )

    parts = [
        types.Part.from_text(text=input_text)
    ]

    if audio_file is not None:
        # Streamlit's prompt.audio is file-like.
        # It is usually audio/wav when recorded from st.chat_input.
        audio_bytes = audio_file.getvalue()

        mime_type = getattr(audio_file, "type", None) or "audio/wav"

        parts.append(
            types.Part.from_bytes(
                data=audio_bytes,
                mime_type=mime_type,
            )
        )

    contents = [
        types.Content(
            role="user",
            parts=parts,
        )
    ]

    resultado = []

    try:
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            if text := chunk.text:
                resultado.append(text)

    except ClientError as e:
        print(f"\n[API Error]: {e}")
        return f"[API Error]: {e}"

    return "".join(resultado)