import streamlit as st
st.set_page_config(layout="wide")

main_page = st.Page(
    "views/pagina_principal.py",
    title="Testes Playground",
    icon=":material/experiment:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "pagina principal": [main_page],
    }
)

# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")


# --- RUN NAVIGATION ---
pg.run()
