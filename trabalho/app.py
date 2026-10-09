import streamlit as st

st.set_page_config(
    page_title="Sistema de Biblioteca",
    page_icon="📚",
    layout="wide"
)

# Inicialização
if "livros" not in st.session_state:
    st.session_state.livros = [
        {
            "titulo": "Python para Iniciantes",
            "autor": "João Silva",
            "categoria": "Programação",
            "disponivel": True
        },
        {
            "titulo": "Banco de Dados",
            "autor": "Maria Souza",
            "categoria": "Tecnologia",
            "disponivel": True
        }
    ]

# Menu
pagina = st.sidebar.selectbox(
    "Navegação",
    ["Início", "Biblioteca", "Materiais", "Configurações"]
)

# INÍCIO
if pagina == "Início":

    st.title("🏠 Sistema de Biblioteca")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Livros", len(st.session_state.livros))

    with col2:
        st.metric(
            "Disponíveis",
            len([l for l in st.session_state.livros if l["disponivel"]])
        )

    with col3:
        st.metric(
            "Emprestados",
            len([l for l in st.session_state.livros if not l["disponivel"]])
        )

    st.success("Bem-vindo ao sistema da biblioteca!")

# BIBLIOTECA
elif pagina == "Biblioteca":

    st.title("📚 Biblioteca")

    st.subheader("Cadastrar Livro")

    with st.form("cadastro"):

        titulo = st.text_input("Título")
        autor = st.text_input("Autor")
        categoria = st.selectbox(
            "Categoria",
            [
                "Programação",
                "Tecnologia",
                "Banco de Dados",
                "IA",
                "Outros"
            ]
        )

        salvar = st.form_submit_button("Cadastrar")

        if salvar:

            st.session_state.livros.append({
                "titulo": titulo,
                "autor": autor,
                "categoria": categoria,
                "disponivel": True
            })

            st.success("Livro cadastrado!")

    st.divider()

    st.subheader("Acervo")

    for i, livro in enumerate(st.session_state.livros):

        with st.expander(livro["titulo"]):

            st.write("Autor:", livro["autor"])
            st.write("Categoria:", livro["categoria"])

            status = (
                "Disponível"
                if livro["disponivel"]
                else "Emprestado"
            )

            st.write("Status:", status)

            if livro["disponivel"]:

                if st.button(
                    "Emprestar",
                    key=f"emp_{i}"
                ):
                    st.session_state.livros[i]["disponivel"] = False
                    st.rerun()

            else:

                if st.button(
                    "Devolver",
                    key=f"dev_{i}"
                ):
                    st.session_state.livros[i]["disponivel"] = True
                    st.rerun()

# MATERIAIS
elif pagina == "Materiais":

    st.title("📖 Materiais")

    busca = st.text_input("Pesquisar")

    resultados = []

    for livro in st.session_state.livros:

        if busca.lower() in livro["titulo"].lower():
            resultados.append(livro)

    st.subheader("Resultados")

    for livro in resultados:

        st.container(border=True)

        st.write("📚", livro["titulo"])
        st.write("Autor:", livro["autor"])
        st.write("Categoria:", livro["categoria"])

# CONFIGURAÇÕES
elif pagina == "Configurações":

    st.title("⚙️ Configurações")

    nome = st.text_input(
        "Nome do Bibliotecário",
        "Administrador"
    )

    tema = st.selectbox(
        "Tema",
        ["Claro", "Escuro"]
    )

    notificacoes = st.checkbox(
        "Receber notificações",
        value=True
    )

    if st.button("Salvar"):

        st.success("Configurações salvas!")

        st.write("Nome:", nome)
        st.write("Tema:", tema)
        st.write("Notificações:", notificacoes)