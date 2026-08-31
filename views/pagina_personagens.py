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
from streamlit_carousel import carousel

st.title("Streamlit Image Carousel")

# Publicly hosted images via Unsplash CDN
carousel_items = [
    {
        "title": "Mountain Lake",
        "text": "Glacier lake surrounded by peaks",
        "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&auto=format&fit=crop",
    },
    {
        "title": "Forest Misty Path",
        "text": "Sunlight filtering through trees",
        "img": "https://images.unsplash.com/photo-1448375240586-882707db888b?w=800&auto=format&fit=crop",
    },
    {
        "title": "Ocean Sunset",
        "text": "Golden hour over calm water",
        "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop",
    },
]

# Render carousel
carousel(items=carousel_items, height=400)