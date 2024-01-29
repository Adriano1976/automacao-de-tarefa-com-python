import time
import pyautogui
import pandas as pd

# Passo 1: Entrar no sistema da empresa
pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

# Entrar no link
pyautogui.click(x=365, y=51)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)

# Passo 2: Fazer login
pyautogui.click(x=522, y=386)  # Selecionar o campo de email
pyautogui.write("pythonimpressionador@gmail.com")  # Escrever o seu email
pyautogui.press("tab")
pyautogui.write("sua senha")  # Escrever a senha
pyautogui.click(x=657, y=551)  # Clicar no botão de login

# Passo 3: Importar a base de produtos pra cadastrar
dataFrame = pd.read_csv('produtos.csv')

# Passo 4: Cadastrar um produto
for linha in dataFrame.index:
    pyautogui.click(x=478, y=272)  # Clicar no campo de código
    # Preencher o campo com os valores da tabela
    pyautogui.write(str(dataFrame.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(dataFrame.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(dataFrame.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(dataFrame.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(dataFrame.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(dataFrame.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = dataFrame.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(dataFrame.loc[linha, "obs"]))
    # Cadastra o produto (botao enviar)
    pyautogui.press("tab")
    pyautogui.press("enter")
    # Dar scroll de tudo pra cima
    pyautogui.scroll(5000)
