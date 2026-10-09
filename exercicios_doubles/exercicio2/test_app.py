import pytest
from exercicio2.app import RepositorioUsuariosFake, GerenciadorUsuarios


@pytest.fixture
def gerenciador():
    repositorio = RepositorioUsuariosFake()
    return GerenciadorUsuarios(repositorio)


def test_adicionar_e_buscar_usuario(gerenciador):

    # Arrange
    nome = "William"

    # Act
    gerenciador.registrar_usuario(nome)
    resultado = gerenciador.encontrar_usuario(nome)

    # Assert
    assert resultado == "William"


def test_buscar_usuario_inexistente(gerenciador):

    # Arrange
    nome = "João"

    # Act
    resultado = gerenciador.encontrar_usuario(nome)

    # Assert
    assert resultado is None