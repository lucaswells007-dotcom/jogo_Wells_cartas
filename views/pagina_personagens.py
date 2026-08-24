from scripts.auxiliar import ler_google_sheets
import streamlit as st
import pandas as pd

st.title("conheça seu personagem")

df_personagem = ler_google_sheets(
    spreadsheet_id="1obdFvz7z50Ejzjv9NeYhZNV-OFbxLG_cHRRtJUIJn80",
    nome_aba="base de personagens",
)



event = st.dataframe(
    df_personagem,
    key="data",
    on_select="rerun",
    selection_mode=["single-row-required"],
)

event.selection

