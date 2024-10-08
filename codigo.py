# 1º - Entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# 2º - Fazer Login
# 3º - Importar base de dados
# 4º - Cadastrar um produto
# 5º - Replicar para todos os produtos

# pip install pyautogui - Automatizador de cursor;

# Bibliotecas necessárias:
import pyautogui
import time
import pandas

# Delay do programa:
pyautogui.PAUSE = 0.3

# Inicializando navegador (OperaGX):
pyautogui.press("win")
pyautogui.write("Opera")
pyautogui.press("enter")
time.sleep(2)

# Entrando no site pela URL:
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# Logando com usuário e senha:
pyautogui.click(x=813, y=482)
pyautogui.write("teste@gmail.com")

pyautogui.press("tab")
pyautogui.write("123456789")

pyautogui.click(x=977, y=688)
time.sleep(2)

# Importação do BD:
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    pyautogui.click(x=721, y=348)

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
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
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)













