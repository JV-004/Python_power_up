# Importação das bibliotecas necessárias
import pyautogui  # Automação de ações no computador (teclado e mouse)
import pandas as pd  # Manipulação de dados em tabelas (DataFrame)
import time  # Controle de tempo e pausas

# Leitura da tabela de produtos a partir de um arquivo CSV
tabela = pd.read_csv("produtos.csv")

# Configuração de pausa padrão entre comandos do PyAutoGUI para evitar ações rápidas demais
pyautogui.PAUSE = 0.7

# Abrindo o navegador Edge usando o menu Iniciar
pyautogui.press("win")  # Pressiona a tecla Windows
pyautogui.write("chrome")  # Digita "edge" para buscar o navegador
pyautogui.press("enter")  # Pressiona Enter para abrir o navegador

# Aguardar alguns segundos para o navegador abrir
time.sleep(2)

# Abrir o link do sistema na barra de endereços
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")  # Pressiona Enter para acessar o link

# Pausa para garantir que a página carregue
time.sleep(2)

# Simula o preenchimento de login e senha no formulário da página
pyautogui.click(x=673, y=451)  # Clica no campo de e-mail (posição da tela)
pyautogui.write("cleitin157666@gmail.com")  # Digita o e-mail
pyautogui.press("tab")  # Navega para o próximo campo (senha)
pyautogui.write("minhasenha123")  # Digita a senha
pyautogui.press("tab")  # Navega para o botão de login
pyautogui.press("enter")  # Simula o clique no botão de login

# Loop para preencher informações dos produtos na tabela
for linha in tabela.index:
    # Clica no campo para começar o preenchimento do produto
    pyautogui.click(x=637, y=308)
    
    # Preenche os campos com as informações da tabela
    pyautogui.write(tabela.loc[linha, "codigo"])  # Código do produto
    pyautogui.press("tab")  # Navega para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))  # Marca do produto
    pyautogui.press("tab")  # Navega para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))  # Tipo do produto
    pyautogui.press("tab")  # Navega para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "categoria"]))  # Categoria do produto
    pyautogui.press("tab")  # Navega para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))  # Preço unitário
    pyautogui.press("tab")  # Navega para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "custo"]))  # Custo do produto
    pyautogui.press("tab")  # Navega para o próximo campo
    
    # Preenche o campo de observação, se existir
    obs = (str(tabela.loc[linha, "obs"]))  # Obtém o valor do campo de observação
    if obs != "nan":  # Verifica se o valor não é "nan" (campo vazio)
        pyautogui.write(obs)  # Preenche o campo de observação
    
    pyautogui.press("tab")  # Navega para o botão de envio
    pyautogui.press("enter")  # Envia o formulário
    pyautogui.scroll(10000)  # Faz scroll para o topo (facilita a navegação)


