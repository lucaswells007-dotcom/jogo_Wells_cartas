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
        "title": "Mountain Lake",
        "text": "Glacier lake surrounded by peaks",
        "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&auto=format&fit=crop",
    },
    {
        "id": "slide_2",
        "title": "Forest Misty Path",
        "text": "Sunlight filtering through trees",
        "img": "https://images.unsplash.com/photo-1448375240586-882707db888b?w=800&auto=format&fit=crop",
    },
    {
        "id": "slide_3",
        "title": "Ocean Sunset",
        "text": "Golden hour over calm water",
        "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop",
    },
]

# Initialize active index state
if "active_index" not in st.session_state:
    st.session_state.active_index = 0

current_item = carousel_items[st.session_state.active_index]

# Display current slide image and details
st.image(current_item["img"], use_container_width=True)
st.subheader(current_item["title"])
st.caption(current_item["text"])

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

# Access the active selection anywhere in your app
st.divider()
st.write(
    f"**Selected Image ID:** `{current_item['id']}` (Index: {st.session_state.active_index})"
)