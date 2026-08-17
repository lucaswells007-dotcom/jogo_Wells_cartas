from scripts.auxiliar import ler_google_sheets
import streamlit as st

st.write("pagina banco de dados")

df = ler_google_sheets(
    spreadsheet_id="1obdFvz7z50Ejzjv9NeYhZNV-OFbxLG_cHRRtJUIJn80",
    nome_aba="base de personagens",
)

st.dataframe(df)