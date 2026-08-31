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

colunas_mostrar = ['nome','altura','peso','inteligencia','idade']

event = st.dataframe(
    df_personagem[colunas_mostrar],
    key="data",
    on_select="rerun",
    selection_mode=["single-row-required"],
)

selecionado = event.selection
linha_selecionada = selecionado['rows'][0]

dados_personagem = df_personagem.iloc[linha_selecionada]
st.dataframe[dados_personagem]