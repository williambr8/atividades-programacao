from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

print("Iniciando...")

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10)

print("Abrindo Aba 0...")

driver.get("https://the-internet.herokuapp.com/dropdown")

print("Aba 0 aberta!")

print("Abrindo Aba 1...")

quantidade_antes = len(driver.window_handles)

driver.execute_script(
    "window.open('https://the-internet.herokuapp.com/dynamic_loading/2', '_blank');"
)

WebDriverWait(driver, 15).until(
    lambda d: len(d.window_handles) > quantidade_antes
)

print("Aba 1 aberta!")

print("Abrindo Aba 2...")

quantidade_antes = len(driver.window_handles)

driver.execute_script(
    "window.open('https://pt.wikipedia.org', '_blank');"
)

WebDriverWait(driver, 15).until(
    lambda d: len(d.window_handles) > quantidade_antes
)

print("Aba 2 aberta!")

print("Quantidade total de abas:", len(driver.window_handles))


print("\nVoltando para a Aba 0...")

driver.switch_to.window(driver.window_handles[0])

print("Aba 0 selecionada!")


dropdown_element = driver.find_element(By.ID, "dropdown")


dropdown = Select(dropdown_element)

dropdown.select_by_visible_text("Option 1")


primeira_opcao = dropdown.first_selected_option

valor = primeira_opcao.get_attribute("value")

print("Opção selecionada:", primeira_opcao.text)
print("Valor:", valor)



print("\nVoltando para a Aba 1...")

driver.switch_to.window(driver.window_handles[1])

print("Aba 1 selecionada!")


botao_start = driver.find_element(By.CSS_SELECTOR, "#start button")

botao_start.click()

print("Botão Start clicado!")

print("Aguardando o elemento finish...")

elemento_finish = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "finish"))
)

WebDriverWait(driver, 15).until(
    EC.visibility_of(elemento_finish)
)

texto_finish = elemento_finish.text

print("Texto encontrado:", texto_finish)

print("\nVoltando para a Aba 2...")

driver.switch_to.window(driver.window_handles[2])

print("Aba 2 selecionada!")

barra_pesquisa = driver.find_element(By.NAME, "search")

barra_pesquisa.send_keys("Automação")

print("Automação digitada na barra de pesquisa!")

link_menu = driver.find_element(
    By.CSS_SELECTOR,
    "#p-navigation a"
)

texto_link = link_menu.text

href_link = link_menu.get_attribute("href")

print("Texto do link:", texto_link)
print("Destino (href):", href_link)

driver.save_screenshot("evidencia_wiki.png")

print("Screenshot salvo como evidencia_wiki.png")

driver.quit()

print("Navegador encerrado com sucesso!")