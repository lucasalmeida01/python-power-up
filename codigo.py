#site fictício da empresa
#https://dlp.hashtagtreinamentos.com/python/intensivao/login

#lib usada para automação -> pyautogui
#pip install pyautogui
import pyautogui
import time
import pandas as pd   

#inserindo um pause de 0.5 segundo entre os comandos
pyautogui.PAUSE = 0.5

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#automação pora abrir o navegador
pyautogui.hotkey("win", "r")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

#automação para fazer o login no site
time.sleep(1)
pyautogui.press("tab")
pyautogui.write("lucas.almeida@email.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")

#importando a base de dados para realizar os cadastros
tabela = pd.read_csv("E:\Jornada Python\Python Power Up\produtos.csv")

time.sleep(2)
#laço para repetir o processo de cadastro de todos os proditos da nossa base de dados
for linha in tabela.index:  
    pyautogui.click(x=783, y=291)
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #condição para apenas preencher o campo "obs" se ele não for vazio
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(tabela.loc[linha, "obs"])
 
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)