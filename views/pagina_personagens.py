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
st.dataframe(dados_personagem)

import streamlit as st

st.title("Interactive Image Carousel")

# Define your image items
carousel_items = [
    {
        "id": "slide_1",
        "title": "Camu",
        "img": "imagens/camu.png",
    },
    {
        "id": "slide_2",
        "title": "Kora",
        "img": "imagens/kora.png",
    },
]

# Initialize active index state
if "active_index" not in st.session_state:
    st.session_state.active_index = 0

current_item = carousel_items[st.session_state.active_index]

# Display current slide image and details
st.image(current_item["img"], use_container_width=True)
st.subheader(current_item["title"])

# Carousel navigation controls
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("Previous", use_container_width=True):
        st.session_state.active_index = (
            st.session_state.active_index - 1
        ) % len(carousel_items)
        st.rerun()

with col3:
    if st.button("Next", use_container_width=True):
        st.session_state.active_index = (
            st.session_state.active_index + 1
        ) % len(carousel_items)
        st.rerun()
