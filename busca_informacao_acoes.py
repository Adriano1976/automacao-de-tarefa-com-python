'''
PROJETO: Você trabalha em uma empresa de investimentos e todos os dias precisa enviar um e-mail com o
valor da cotação de algumas ações. O e-mail precisa conter as informações dos últimos seis meses:
Cotação mínima da ação
Cotação máxima da ação
Cotação do dia
'''

import yfinance
import pyautogui
import pyperclip

# Buscar automaticamente os dados das ações
codigo = input("Digite o código da ação desejada: ")
dados = yfinance.Ticker(codigo).history("6mo")
fechamento = dados.Close
imagem = fechamento.plot()
print(fechamento)

# Gerar as análises de forma automática
maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento.iloc[-1]

print(maxima)
print(minima)
print(atual)

# Criando o e-mail que vamos enviar
destinatario = "aquivocetempromocao@gmail.com"
assunto = "Análise diária"
mensagem = f"""
Bom dia,

Segue abaixo as análises da ação {codigo} dos últimos seis meses:

{imagem}

- Cotação máxima: R$ {round(maxima,2)}
- Cotação mínima: R$ {round(minima,2)}
- Cotação atual: R$ {round(atual,2)}

Atenciosamente,

Sr. Adriano Santos
"""

# Enviar um e-mail para o nosso gestor
pyautogui.PAUSE = 5
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')

# configurar uma pausa entre as ações do pyautogui
pyautogui.PAUSE = 8

# abrir uma nova aba
pyautogui.hotkey("ctrl", "t")

# copiar o endereço do gmail para o clipboard
pyperclip.copy("https://www.gmail.com")

# colar o endereço do gmail e dar um ENTER
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# clicando no botão Escrever
pyautogui.PAUSE = 10
pyautogui.click(x=124, y=211)

# Preenchendo o destinatário
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# Preenchendo o assunto
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# Preenchendo a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# Clicar no botão Enviar
pyautogui.click(x=827, y=697)

# fechar a aba do gmail
pyautogui.hotkey("ctrl", "f4")

print('E-mail enviado com sucesso!')
