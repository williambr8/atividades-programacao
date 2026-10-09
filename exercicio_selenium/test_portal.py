import pytest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def navegador():
    driver = webdriver.Chrome()

    caminho_html = Path(__file__).parent / "portal.html"
    caminho_absoluto = caminho_html.resolve()

    driver.get(caminho_absoluto.as_uri())

    yield driver

    driver.quit()


def test_preencher_formulario(navegador):

    assert navegador.title == "Portal do Colaborador"

    campo_nome = navegador.find_element(By.ID, "nome")

    campo_nome.send_keys("João da Silva")

    campo_email = navegador.find_element(By.ID, "email")

    campo_email.send_keys("joao@empresa.com")

    botao_enviar = navegador.find_element(By.ID, "enviar")
    botao_enviar.click()

    mensagem = navegador.find_element(By.ID, "mensagem")

    assert mensagem.is_displayed()

    assert mensagem.text == "Dados enviados com sucesso!"


def test_acoes_avancadas_mouse(navegador):

    acoes = ActionChains(navegador)

    botao_duplo_clique = navegador.find_element(
        By.ID, "duploClique"
    )
    acoes.double_click(botao_duplo_clique).perform()

    assert botao_duplo_clique.text == "Autorizado!"

    botao_clique_direito = navegador.find_element(
        By.ID, "cliqueDireito"
    )
    acoes.context_click(botao_clique_direito).perform()

    assert botao_clique_direito.text == "Menu Aberto!"


def test_acoes_teclado(navegador):

    campo_texto = navegador.find_element(
        By.ID, "observacoes"
    )

    campo_texto.click()

    acoes = ActionChains(navegador)

    acoes.key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.BACKSPACE) \
        .perform()

    novo_texto = "Teste automatizado finalizado."

    campo_texto.send_keys(novo_texto)
    
    assert campo_texto.get_attribute("value") == novo_texto