import streamlit as st

st.title("⚙️ Configurações")

nome = st.text_input("Nome do Usuário")

tema = st.selectbox(
    "Tema",
    ["Claro", "Escuro"]
)

notificacoes = st.checkbox(
    "Receber notificações"
)

if st.button("Salvar"):
    st.success("Configurações salvas!")