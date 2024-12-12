from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

def obter_empenhos_SAG(): #essa função entra no SAG, obtém as tabelas de dados dos empenhos, e grava um arquivo CSV 'dados_empenho_tratado.csv'

    CPF = input("Digite o Login no SAG:")
    SENHA = input("Digite a senha do SAG:")

    print('Abrindo SAG...')

    url = "https://sag.eb.mil.br/index.php"

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    #driver = webdriver.Chrome()
    driver.get(url)
    
    fechar_botao = driver.find_element(By.XPATH, "//button[@class='btn btn-default fechar' and @data-dismiss='modal']")
    fechar_botao.click()
    
    # Encontrar e clicar no botão "Login"
    login_botao = driver.find_element(By.ID, "login")
    login_botao.click()
    
    time.sleep(2)
    
    # Encontrar o campo de CPF e digitar o número
    cpf_input = driver.find_element(By.ID, "cpf")
    cpf_input.send_keys(CPF)
    
    # Encontrar o campo de senha e digitar a senha
    senha_input = driver.find_element(By.ID, "senha")
    senha_input.send_keys(SENHA)
    
    enviar_botao = driver.find_element(By.ID, "btn")
    enviar_botao.click()

    print('Fazendo LOGIN no SAG...')
    
    time.sleep(10)

    print('Abrindo página de empenhos no SAG...')
    
    driver.get('https://sag.eb.mil.br/php/docNeuq1.php')
    time.sleep(3)
    
    # Localizar o botão "EXIBIR FILTROS" pelo ID
    botao_exibir_filtros = driver.find_element(By.ID, 'btnShowFilters')
    
    # Clicar no botão
    botao_exibir_filtros.click()
    
    # Clique no segundo botão de dropdown dentro de uma <div> com a classe específica
    dropdown2 = driver.find_element(By.XPATH, "//div[@class='col-md-2']//button[@type='button' and @class='btn dropdown-toggle btn-default']")
    dropdown2.click()
    
    # Clicar no botão "Select All"
    select_all_button = driver.find_element(By.XPATH, "//button[@class='actions-btn bs-select-all btn btn-default']")
    select_all_button.click()
    
    # Localiza o elemento <select>
    select_element = driver.find_element("name", "example_length")
    
    # Cria um objeto Select
    select = Select(select_element)
    
    # Seleciona a opção "1000"
    select.select_by_value("1000")
    time.sleep(3)
    
    # Capturar o HTML da nova página após o login
    page_source = driver.page_source
    
    # Usar BeautifulSoup para analisar o HTML da nova página
    soup = BeautifulSoup(page_source, 'html.parser')

    print('Obtendo dados de empenhos no SAG...')

    headers = soup.find_all('table')[1].find_all('td')[1].text.strip().split(',')

    cabecalho = [coluna.strip() for coluna in headers]
    
    tabela = soup.find_all('table')[0]
    
    # Encontrar todas as linhas da tabela
    linhas = tabela.find_all('tr')
    
    # Criar uma lista para armazenar os dados da tabela
    tabela_dados = []
    
    # Iterar sobre as linhas da tabela
    for linha in linhas:
        # Encontrar todas as células de dados (colunas) em cada linha
        colunas = linha.find_all('td')
    
        # Extrair o texto de cada coluna e armazenar em uma lista
        dados_linha = [coluna.text.strip() for coluna in colunas]
    
        # Adicionar os dados da linha na variável tabela_dados
        if dados_linha:  # Adiciona somente se houver dados (para evitar linhas vazias)
            tabela_dados.append(dados_linha)

    proxima_pagina = True

    while proxima_pagina:
        
        try:    
        
            next_button = driver.find_element("id", "example_next")
            next_button.click()
    
            time.sleep(10)
    
            # Capturar o HTML da nova página após o login
            page_source = driver.page_source
            
            # Usar BeautifulSoup para analisar o HTML da nova página
            soup = BeautifulSoup(page_source, 'html.parser')
            
            # Encontrar a tabela (pode ser necessário ajustar dependendo da estrutura da página)
            tabela = soup.find_all('table')[0]
    
            # Encontrar todas as linhas da tabela
            linhas = tabela.find_all('tr')
            
            # Iterar sobre as linhas da tabela
            for linha in linhas:
                # Encontrar todas as células de dados (colunas) em cada linha
                colunas = linha.find_all('td')
            
                # Extrair o texto de cada coluna e armazenar em uma lista
                dados_linha = [coluna.text.strip() for coluna in colunas]
            
                # Adicionar os dados da linha na variável tabela_dados
                if dados_linha:  # Adiciona somente se houver dados (para evitar linhas vazias)
                    tabela_dados.append(dados_linha)
                
        except:
            
            proxima_pagina = False

    # Fechar o driver
    driver.quit()
    
    #Tratamento dos dados

    print('Tratando os dados...')
        
    df = pd.DataFrame(tabela_dados, columns = cabecalho)
    
    df = df[['NR','INFO_COMPLEMENTAR','OBS_LI','QUANTIDADE']].copy()
    df.loc[:, 'UASG'] = df['INFO_COMPLEMENTAR'].str[:6]
    df.loc[:, 'Ano do Pregão'] = df['INFO_COMPLEMENTAR'].str[13:17]
    df.loc[:, 'Número do Pregão'] = df['INFO_COMPLEMENTAR'].str[8:13]
    df = df[df['OBS_LI'].str.contains('ITEM', na=False)]
    df['OBS_LI'].str.split(' ')
    df['Número do Item'] = df['OBS_LI'].str.split(' ').str[2]
    df = df[['UASG','Número do Pregão','Ano do Pregão','Número do Item', 'QUANTIDADE']]

    df.to_csv('dados_empenho_tratado.csv', sep=';', encoding='utf-8', index=False)

    print('Arquivo dados_empenho_tratado.csv salvo com sucesso!')

