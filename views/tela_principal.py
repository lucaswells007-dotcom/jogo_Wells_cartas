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

st.subheader("gere o problema", divider='blue')

botao_problema = st.button('escolher problema')
if botao_problema:
  
    problemas = df_problemas['problemas'].sample(1).values[0]
    st.write(problemas)

st.subheader("selecione os personagens", divider='red')

lista_personagens = df_personagem['nome']

coluna1, coluna2 = st.columns(2)

personagem1 = coluna1.selectbox('selecione o personagem 1',lista_personagens)
coluna1.subheader("argumantacao")
argumantacao = coluna1.text_area("argumento to personagem 1")

personagem2 = coluna2.selectbox('selecione o personagem 2',lista_personagens)
coluna2.subheader("argumantacao")
argumantacao = coluna2.text_area("argumento do perdonagem 2")
