import streamlit as st
import os
from google import genai
from google.genai import types
from google.genai.errors import ClientError
import gspread
import pandas as pd



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

def ler_google_sheets(spreadsheet_id: str, nome_aba: str) -> pd.DataFrame:
    credenciais = dict(st.secrets["gcp_service_account"])

    cliente = gspread.service_account_from_dict(credenciais)
    planilha = cliente.open_by_key(spreadsheet_id)
    aba = planilha.worksheet(nome_aba)

    dados = aba.get_all_records()

    return pd.DataFrame(dados)