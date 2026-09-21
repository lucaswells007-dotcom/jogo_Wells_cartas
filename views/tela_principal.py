from scripts.auxiliar import ler_google_sheets
import streamlit as st

if 'df_personagem' not in st.session_state:
    df_personagem = ler_google_sheets(
                        spreadsheet_id="1obdFvz7z50Ejzjv9NeYhZNV-OFbxLG_cHRRtJUIJn80",
                        nome_aba="base de personagens",
                    )
    st.session_state['df_personagem'] = df_personagem

else:
    df_personagem = st.session_state['df_personagem']

if 'df_problemas' not in st.session_state:
    df_problemas = ler_google_sheets(
                        spreadsheet_id="1obdFvz7z50Ejzjv9NeYhZNV-OFbxLG_cHRRtJUIJn80",
                        nome_aba="problemas",
                    )
    st.session_state['df_problemas'] = df_problemas

else:
    df_problemas = st.session_state['df_problemas']

st.title('meu jogo')

botao_problema = st.button('escolher problema')
if botao_problema:
  
    problemas = df_problemas['problemas'].sample(1).values[0]
    st.write(problemas)