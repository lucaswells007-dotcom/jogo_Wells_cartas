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
imagem = linha_selecionada['img'].item()
imagem = imagem if imagem != '' else 'imagens/sem_imagem.jpeg'
altura = linha_selecionada['altura'].item()
peso = linha_selecionada['peso'].item()
inteligencia =  linha_selecionada['inteligencia'].item()
idade = linha_selecionada['idade'].item()


coluna1,coluna2 = st.columns(2)

with coluna1:
    st.image(imagem,width=400)

with coluna2:
    st.markdown(
    f"""
    <div style="font-size: 20px; line-height: 1.8;">
        <b>altura:</b> {altura}<br>
        <b>peso:</b> {peso}<br>
        <b>inteligencia:</b> {inteligencia}<br>
        <b>idade:</b> {idade}<br>
    </div>
    """,
    unsafe_allow_html=True,
)


