from scripts.auxiliar import ler_google_sheets
import streamlit as st
import pandas as pd

# Initialization
if 'df_personagem' not in st.session_state:
    df_personagem = ler_google_sheets(
                        spreadsheet_id="1obdFvz7z50Ejzjv9NeYhZNV-OFbxLG_cHRRtJUIJn80",
                        nome_aba="base de personagens",
                    )
    st.session_state['df_personagem'] = df_personagem

else:
    df_personagem = st.session_state['df_personagem']

st.title("conheça seu personagem")

nome_personagens = df_personagem['nome']
nome_selecionado = st.selectbox('Selecione seu personagem',nome_personagens)

linha_selecionada = df_personagem.loc[df_personagem['nome']==nome_selecionado]
st.write(linha_selecionada)