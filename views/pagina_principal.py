from scripts.auxiliar import consultar_juiz
import streamlit as st
st.write('pagina principal')

pergunta = st.chat_input("Say something")

if pergunta:
    resultado = consultar_juiz(pergunta)
    st.write(resultado)

