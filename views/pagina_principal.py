from scripts.auxiliar import consultar_juiz
import streamlit as st
st.write('testes')

if st.button('testes'):
    resultado = consultar_juiz('quem vai ganhar a copa do mundo?')
    st.write(resultado)
