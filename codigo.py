#site fictício da empresa
#https://dlp.hashtagtreinamentos.com/python/intensivao/login

#pip install pyautogui
import pyautogui
import time
import pandas as pd   

pyautogui.PAUSE = 0.5

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.hotkey("win", "r")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(1)
pyautogui.press("tab")
pyautogui.write("lucas.almeida@email.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")

tabela = pd.read_csv("E:\Jornada Python\Python Power Up\produtos.csv")

time.sleep(2)
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

    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(tabela.loc[linha, "obs"])
 
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)