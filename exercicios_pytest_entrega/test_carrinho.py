import pytest
from carrinho import CarrinhoDeCompras


def test_adicionar_item():
    # Arrange
    carrinho = CarrinhoDeCompras()
    item = "Mouse"

    # Act
    carrinho.adicionar_item(item)

    # Assert
    assert item in carrinho.listar_itens()


def test_remover_item():
    # Arrange
    carrinho = CarrinhoDeCompras()
    item = "Teclado"
    carrinho.adicionar_item(item)

    # Act
    carrinho.remover_item(item)

    # Assert
    assert item not in carrinho.listar_itens()


def test_remover_item_inexistente():
    # Arrange
    carrinho = CarrinhoDeCompras()
    item = "Monitor"

    # Act
    with pytest.raises(ValueError):
        carrinho.remover_item(item)

    # Assert
    assert item not in carrinho.listar_itens()
