# Documentação do Usuário

## Visão Geral
Este programa automatiza a coleta e o processamento de informações sobre pregões eletrônicos, incluindo a obtenção de dados de itens, fornecedores e valores unitários. Ele também permite a gestão e atualização de saldos dos itens adquiridos.

O programa utiliza Selenium para interagir com o site do Comprasnet e Pandas para manipulação de dados.

---

## Requisitos
- Google Chrome instalado
- Chromedriver compatível com a versão do Chrome
- Python 3.x
- Bibliotecas necessárias: `selenium`, `bs4`, `requests`, `pandas`, `numpy`

### Instalação das Dependências
Execute o seguinte comando no terminal para instalar as dependências:
```bash
pip install selenium beautifulsoup4 requests pandas numpy
```

---

## Como Usar o Programa
### Execução
Para iniciar o programa, execute o seguinte comando no terminal:
```bash
python app.py
```

Você verá um menu com as seguintes opções:

### 1 - Atualizar Saldo
Esta opção verifica e atualiza os saldos dos itens cadastrados no banco de dados.
Caso não haja um arquivo de dados (`df_itens_gerenciadora.csv`), o programa informará que não há registros para atualizar.

### 2 - Ver Pregões Salvos
Mostra a lista de pregões salvos no arquivo `df_itens_gerenciadora.csv`, exibindo os números das compras armazenadas.

### 3 - Obter Dados de Novo Pregão
Permite capturar os dados de um novo pregão eletrônico. O usuário deve inserir:
- **Número da UASG**
- **Número da Licitação**
- **Ano da Licitação**
- **Fim da Vigência (DD/MM/AAAA)**

Após a coleta, os dados serão salvos em `df_itens_gerenciadora_novo.csv`. Caso já haja um arquivo `df_itens_gerenciadora.csv`, o novo pregão será adicionado a ele.

O programa também pergunta se o usuário deseja atualizar o saldo após a obtenção dos dados do pregão.

### 4 - Apagar Dados de Pregão Existente
O usuário pode visualizar os pregões salvos e escolher um para excluir do banco de dados.

### 5 - Sair
Finaliza o programa.

---

## Arquivos Utilizados
### Entrada
- `df_itens_gerenciadora.csv` - Armazena os dados dos pregões coletados.
- `dados_empenho_tratado.csv` - Contém os dados de empenhos processados.

### Saída
- `df_itens_gerenciadora.csv` - Arquivo atualizado com os novos pregões e saldos calculados.
- `df_itens_gerenciadora_novo.csv` - Contém os dados do último pregão coletado antes da fusão com `df_itens_gerenciadora.csv`.

---

## Possíveis Problemas e Soluções
### 1. O Chrome não abre ou o Selenium falha
- Verifique se o `chromedriver` está atualizado e compatível com sua versão do Google Chrome.
- Reinstale o `chromedriver` e o configure corretamente no PATH.

### 2. O site do Comprasnet mudou e os dados não estão sendo coletados
- Atualize os seletores no código fonte para refletir eventuais mudanças na estrutura do site.

### 3. Erro ao carregar arquivos CSV
- Verifique se os arquivos estão no mesmo diretório que `app.py`.
- Certifique-se de que os arquivos estejam no formato correto, com separadores `;` e codificação UTF-8.

---

## Conclusão
Este programa permite a automação da coleta e gestão de dados de pregões eletrônicos, facilitando a análise e controle de saldos de itens adquiridos. Caso precise de ajustes ou melhorias, modifique os seletores do Selenium conforme necessário ou expanda as funcionalidades do script.

