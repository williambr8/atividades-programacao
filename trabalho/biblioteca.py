import streamlit as st

st.set_page_config(
    page_title="Sistema Biblioteca",
    page_icon="📚",
    layout="wide"
)

# Inicializa a lista de livros
if "livros" not in st.session_state:
    st.session_state.livros = [
        {
            "titulo": "Python para Iniciantes",
            "autor": "João Silva",
            "categoria": "Programação",
            "capa": "",
            "disponivel": True
        },
        {
            "titulo": "Banco de Dados",
            "autor": "Maria Souza",
            "categoria": "Banco de Dados",
            "capa": "",
            "disponivel": True
        }
    ]

# Menu lateral
pagina = st.sidebar.selectbox(
    "📋 Menu",
    [
        "Início",
        "Biblioteca",
        "Materiais",
        "Configurações"
    ]
)

# Página Inicial
if pagina == "Início":

    st.title("🏠 Sistema de Biblioteca")

    st.write("Bem-vindo ao sistema!")

# Biblioteca
elif pagina == "Biblioteca":

    # COLE AQUI TODO O CÓDIGO DA BIBLIOTECA QUE VOCÊ ENVIOU

# Materiais
elif pagina == "Materiais":

    st.title("📖 Materiais")

    st.write("Página de materiais.")

# Configurações
elif pagina == "Configurações":

    st.title("⚙️ Configurações")

    nome = st.text_input("Nome")

    if st.button("Salvar"):
        st.success("Configurações salvas!")