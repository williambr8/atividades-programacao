from unittest.mock import Mock, call

from exercicio3.app import ProcessadorDeAcoes


def test_executar_processo_na_ordem_correta(mocker):

    # Arrange
    processador = ProcessadorDeAcoes()

    mock_validar = mocker.patch.object(
        processador,
        "validar_dados",
        return_value=True
    )

    mock_salvar = mocker.patch.object(
        processador,
        "salvar_dados",
        return_value=True
    )

    dados = {
        "nome": "William",
        "idade": 20
    }

    # Mock para registrar a ordem das chamadas
    mock_objeto = Mock()

    mock_validar.side_effect = lambda dados: (
        mock_objeto.validar_dados(dados)
        or True
    )

    mock_salvar.side_effect = lambda dados: (
        mock_objeto.salvar_dados(dados)
        or True
    )

    # Act
    resultado = processador.executar_processo(dados)

    # Assert
    assert resultado == "Processo executado com sucesso."

    roteiro_esperado = [
        call.validar_dados(dados),
        call.salvar_dados(dados)
    ]

    mock_objeto.assert_has_calls(
        roteiro_esperado,
        any_order=False
    )

    mock_validar.assert_called_once_with(dados)
    mock_salvar.assert_called_once_with(dados)