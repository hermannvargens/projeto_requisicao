from github import Github
import base64
import pandas as pd

def salvar_arquivo_bruto(df_itens, nome_arquivo):
    
    df_itens['Número do Item'] = df_itens['Número do Item'].astype(int)
    
    df_itens.sort_values(['Número da Compra','Número do Item'], inplace = True)
    df_itens.to_csv(nome_arquivo, sep=';', encoding='utf-8', index=False)        
    
    return 'Arquivo com a tabela dos itens (completa) salva com sucesso!'


def salvar_arquivo_tratado(df_itens, nome_arquivo):

    #Salvando o df final apenas com itens válidos e saldo >0
    df_itens.to_csv(nome_arquivo, sep=';', encoding='utf-8', index=False)


def salvar_itens_github(nome_arquivo_local):
        
    # Token de acesso pessoal do GitHub
    ACCESS_TOKEN = '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'
    
    # Nome do repositório (formato: 'usuario/repositorio')
    REPO_NAME = 'hermannvargens/projeto_requisicao'
    
    # Caminho do arquivo no repositório
    FILE_PATH = nome_arquivo_local
    
    # Conteúdo do arquivo CSV
    csv_content = open(FILE_PATH, 'r', encoding='utf-8').read()
    
    # Conectando-se ao GitHub usando o token de acesso
    g = Github(ACCESS_TOKEN)
    
    # Obter o repositório
    repo = g.get_repo(REPO_NAME)
    
    # Verificar se o arquivo já existe no repositório
    try:
        contents = repo.get_contents(FILE_PATH)
        # Atualizar o arquivo existente
        repo.update_file(contents.path, "Atualizando arquivo CSV", csv_content, contents.sha)
        print(f"Arquivo {FILE_PATH} atualizado com sucesso!")
    except:
        # Se o arquivo não existir, criar um novo arquivo
        repo.create_file(FILE_PATH, "Enviando arquivo CSV pela primeira vez", csv_content)
        print(f"Arquivo {FILE_PATH} criado com sucesso!")