from scripts.auxiliar import consultar_juiz
import streamlit as st
st.write('pagina principal')

prompt = st.chat_input("Say something",accept_audio=True)

if prompt and prompt.text:
    resultado = consultar_juiz(prompt.text)
    st.write(resultado)

if prompt and prompt.audio:
    st.audio(prompt.audio)
    st.write("Audio file:", prompt.audio.name)


