import streamlit as st

st.title("📖 Materiais")

materiais = [
    "Apostila de Python",
    "PDF Banco de Dados",
    "Slides de IA",
    "Exercícios de Programação"
]

pesquisa = st.text_input("🔍 Pesquisar material")

for material in materiais:
    if pesquisa.lower() in material.lower():
        st.success(material)