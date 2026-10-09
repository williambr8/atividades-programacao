from exercicio1 import app


def test_processar_envio(mocker):

    # Arrange
    mock_funcao = mocker.patch(
        "exercicio1.app.enviar_mensagem_externa"
    )

    mock_funcao.return_value = "Mensagem simulada"

    destinatario = "joao@email.com"
    texto = "Olá João!"

    # Act
    resultado = app.processar_envio(destinatario, texto)

    # Assert
    mock_funcao.assert_called_once_with(destinatario, texto)
    assert resultado == "Mensagem simulada"