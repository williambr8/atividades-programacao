from idade import pode_dirigir


def test_pode_dirigir_maior_de_idade():
    # Arrange
    idade = 20
    esperado = True

    # Act
    resultado = pode_dirigir(idade)

    # Assert
    assert resultado is esperado


def test_nao_pode_dirigir_menor_de_idade():
    # Arrange
    idade = 16
    esperado = False

    # Act
    resultado = pode_dirigir(idade)

    # Assert
    assert resultado is esperado
