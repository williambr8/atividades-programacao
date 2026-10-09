import pyautogui
import pandas as pd
import pyperclip
import time
import os


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

pasta_destino = os.path.join(os.getcwd(), "Fichas de Envio")
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

df = pd.read_excel("Envios.xlsx", dtype=str, engine="openpyxl")

df = df.dropna(how='all')


df = df[df['Nome_Cliente'].notna() & (df['Nome_Cliente'].astype(str).str.strip() != '')]

print("Iniciando a automação RPA em 5 segundos...")
print("Mova o cursor do mouse para qualquer canto da tela para interromper se necessário.")
time.sleep(5)


for indice, linha in df.iterrows():
    nome = str(linha['Nome_Cliente']).strip()
    logradouro = str(linha['Logradouro']).strip()
    bairro = str(linha['Bairro']).strip()
    cidade = str(linha['Cidade']).strip()
    cep = str(linha['CEP']).strip()
    codigo = str(linha['Codigo_Rastreamento']).strip()

    texto_ficha = f"""=========================================
FICHA DE EXPEDIÇÃO
Código de Rastreamento: {codigo}
=========================================
Destinatário: {nome}
----------------------------------------------------------------
Endereço de Entrega
Logradouro: {logradouro}
Bairro / Cidade: {bairro} / {cidade}
CEP: {cep}
----------------------------------------------------------------"""


    pyautogui.press('win')
    time.sleep(1)

    pyperclip.copy("Word")
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)  


    pyautogui.press('enter')
    time.sleep(2)


    pyperclip.copy(texto_ficha)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

  
    pyautogui.press('f12')
    time.sleep(2)

    nome_formatado = nome.replace(' ', '_')
    nome_arquivo = f"{nome_formatado}_{codigo}.docx"
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)


    pyperclip.copy(caminho_completo)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    pyautogui.press('enter')
    time.sleep(2)


    pyautogui.hotkey('alt', 'f4')
    time.sleep(1.5)

print("Processo concluído! Todas as fichas foram salvas na pasta Fichas de Envio.")