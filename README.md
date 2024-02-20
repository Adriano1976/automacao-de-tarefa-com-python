# Automacao de tarefa com python

## Introdução

O código em python trata de um projeto de automação em Python utilizando a biblioteca Pyautogui. O objetivo é automatizar o cadastro de uma lista de produtos em um sistema, lendo as informações de um arquivo CSV.

Serão automatizadas as seguintes tarefas:

- Abrir o navegador 
- Fazer login no sistema
- Ler as informações do CSV
- Preencher os dados de cada produto nos campos do sistema
- Clicar em enviar para salvar cada produto
- Repetir o processo para todos os produtos

Assim é possível automatizar um trabalho manual e repetitivo, ganhando produtividade.

## Importando os dados

Utiliza-se o Pandas para importar o arquivo CSV com os dados dos produtos a serem cadastrados.

## Biblioteca Pyautogui

Pyautogui permite controlar o mouse e o teclado para automatizar tarefas no computador.

Principais funcionalidades utilizadas:

- `.press()` - Pressionar teclas
- `.write()` - Escrever textos
- `.click()` - Clicar com o mouse

É importante pegar as coordenadas de posição da tela para garantir os cliques nos locais corretos.

## Automação

Passos automatizados:

- Abrir navegador
- Login no sistema 
- Para cada produto:
  - Preencher dados 
  - Clicar em enviar
  - Repetir

Utiliza loops para iterar sobre todos os produtos cadastrados de forma automatizada.

## Conclusão

O projeto mostra na prática os benefícios de automatizar tarefas repetitivas com Python, resultando em ganhos de produtividade e redução de erros.

<hr>

<div align="center">
<br><p align="centre"><b>Contagem de visitantes</b></p>  
<p align="center"><img align="center" src="https://profile-counter.glitch.me/{automacao-de-tarefa-com-python}/count.svg" /></p> 
<br>  

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=87CEFA&height=120&section=footer"/>**** 
</div>
