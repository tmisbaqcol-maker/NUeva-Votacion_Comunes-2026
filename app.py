import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Mapa Atlántico - Votación",
    layout="wide"
)

st.title("MAPA INTERACTIVO DE VOTACIÓN - ATLÁNTICO")

html_file = Path("mapa_interactivo_atlantico_votos.html")

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=700, scrolling=True)
