import pyautogui
import time
import pandas as pd
import openpyxl

#abrir navegador 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")    
pyautogui.sleep(0.7)

#fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
pyautogui.sleep(0.7)
pyautogui.click(x=694, y=376) 
pyautogui.write("jrebs@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.sleep(0.5)
tabela = pd.read_csv("produtos.csv")

#cadastro de produtos da tabela
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=674, y=254)
    # pegar da tabela 
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
   
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") #enviar
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim

