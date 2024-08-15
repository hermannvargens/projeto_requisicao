import datetime
import pandas as pd

def obter_df_final(nome_arquivo):
    
    df_itens = pd.read_csv(nome_arquivo, sep = ';')
    
    df_itens_dispensa = df_itens[df_itens['Tipo de Compra'] == 'Dispensa']

    df_itens['Qtd. Saldo'] = df_itens['Qtd. Saldo'].astype(float)
   
    df_itens = df_itens[df_itens['Qtd. Saldo']>0]
    df_itens = df_itens[df_itens['Fim da Vigência'] != '-']
    df_itens['Fim da Vigência'] = pd.to_datetime(df_itens['Fim da Vigência'], format='%d/%m/%Y')
    df_itens = df_itens[df_itens['Fim da Vigência'] >= pd.to_datetime(datetime.date.today())]

    df_itens = pd.concat([df_itens_dispensa,df_itens])
    

    return df_itens