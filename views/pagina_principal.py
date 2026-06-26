from scripts.auxiliar import consultar_juiz
import streamlit as st

st.write("pagina principal")

prompt = st.chat_input(
    "Say something",
    accept_audio=True,
)

if prompt:
    user_text = prompt.text or "Transcreva este áudio e responda ao conteúdo dele."

    if prompt.audio:
        st.audio(prompt.audio)
        st.write("Audio file:", prompt.audio.name)

    resultado = consultar_juiz(
        input_text=user_text,
        audio_file=prompt.audio,
    )

    st.write(resultado)


