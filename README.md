# 1 - Documentação do Arquivo Gerador-de-Requisições.html

## Visão Geral
O arquivo **Gerador-de-Requisições.html** é uma interface web interativa desenvolvida para facilitar a geração e gerenciamento de requisições de compra. Ele permite aos usuários visualizar produtos, aplicar filtros dinâmicos, calcular valores totais e gerar documentos de requisição automaticamente.

## Estrutura do Arquivo
O arquivo é composto por três seções principais:
1. **Cabeçalho (Header)**: Exibe o título, a capacidade de empenho e um campo de busca.
2. **Filtros (Topbar e Sidebar)**: Contêm opções para filtrar produtos por tipo de compra, número da compra, ano do pregão, UASG, objeto, unidade de fornecimento e fornecedor.
3. **Lista de Produtos (Main Content)**: Apresenta os produtos em um layout dinâmico, permitindo seleção de quantidade e cálculo automático do total.
4. **Seção de Requisição (Overlay)**: Mostra um resumo da requisição e gera um documento HTML baseado nas seleções feitas.

## Funcionalidades
### 1. Filtros Interativos
- Os filtros são expansíveis e incluem busca por texto em "Fornecedor" e "Objeto".
- Seleção de filtros atualiza automaticamente a lista de produtos.

### 2. Seleção e Cálculo de Valores
- Cada produto exibe detalhes como descrição, unidade de fornecimento, valor unitário e capacidade de empenho.
- O usuário pode selecionar quantidades e visualizar o valor total do item.
- A soma total da requisição é atualizada automaticamente.

### 3. Geração de Requisição
- Os itens selecionados são agrupados por fornecedor e unidade.
- A requisição gerada é formatada automaticamente em HTML.
- O usuário pode copiar o documento finalizado ou baixá-lo como um arquivo HTML.

## Tecnologias Utilizadas
- **HTML5**: Estrutura do documento.
- **CSS3**: Estilização responsiva e temas baseados no padrão Gov.br.
- **JavaScript**: Lógica para interações dinâmicas, manipulação do DOM e requisição de dados CSV via fetch API.

## Uso
1. **Abrir o arquivo HTML** no navegador.
2. **Pesquisar e filtrar produtos** conforme necessidade.
3. **Selecionar quantidades e revisar valores** da requisição.
4. **Gerar a requisição** e copiar ou baixar o documento finalizado.

## Possíveis Problemas e Soluções
### 1. Dados não carregam
- Verifique a URL do CSV na função `fetchCSVData(url)`, garantindo que o arquivo esteja disponível online.

### 2. Erros de cálculo no total da requisição
- Certifique-se de que os valores numéricos estão sendo convertidos corretamente no formato brasileiro (ponto para milhar, vírgula para decimal).

### 3. Campos de busca não filtram corretamente
- Verifique a estrutura do CSV e os identificadores das colunas para garantir a compatibilidade com os filtros aplicados.

## Conclusão
O **Gerador-de-Requisições.html** é uma ferramenta eficiente para automatizar a gestão de requisições de compra, proporcionando praticidade e precisão no processo. Caso precise de personalizações adicionais, ajustes podem ser feitos nos seletores, estilos e lógica JavaScript.

# 2 - Documentação do Arquivo Gerador-de-Requisições - Capacidade de Empenho.html

## Visão Geral
O arquivo **Gerador-de-Requisições - Capacidade de Empenho.html** é uma interface web destinada ao acompanhamento e gerenciamento da capacidade de empenho de itens. Ele permite a seleção de tipo de compra, número da compra, fornecedor e itens específicos, calculando automaticamente o saldo disponível para empenho.

## Estrutura do Arquivo
O arquivo HTML é composto pelas seguintes seções:
1. **Cabeçalho**: Exibe o título "Capacidade de Empenho".
2. **Filtros**:
   - Tipo de Compra
   - Número da Compra
   - Fornecedor
   - Itens (CATMAT, Descrição, Valor Unitário, Saldo para Empenho)
3. **Indicador de Capacidade de Empenho**: Exibe o total acumulado para os itens selecionados.
4. **Script JavaScript**: Responsável pelo carregamento dinâmico dos dados, filtragem e cálculo dos valores de empenho.

## Funcionalidades
### 1. Carregamento de Dados via CSV
- O script busca os dados de um arquivo CSV externo hospedado online.
- Os dados são processados e apresentados no formato de listas suspensas interativas.

### 2. Filtros Interativos
- O usuário pode selecionar um ou mais valores para os filtros disponíveis.
- A seleção de um filtro atualiza automaticamente os demais para exibir apenas opções válidas.

### 3. Cálculo Automático da Capacidade de Empenho
- Cada item possui um saldo para empenho baseado na fórmula: `Quantidade Disponível * Valor Unitário`.
- A soma dos valores dos itens selecionados é exibida no topo da página.

### 4. Estilização e Usabilidade
- A interface é responsiva, com elementos bem espaçados e estilizados para facilitar a leitura.
- O destaque visual dos campos e valores facilita a interação e análise.

## Tecnologias Utilizadas
- **HTML5**: Estrutura da interface.
- **CSS3**: Estilização responsiva e layout organizado.
- **JavaScript**: Manipulação de dados, interatividade e cálculo dinâmico.
- **Fetch API**: Carregamento de dados a partir de um arquivo CSV externo.

## Uso
1. **Abrir o arquivo no navegador**.
2. **Selecionar filtros conforme necessidade**.
3. **Visualizar a capacidade de empenho total calculada automaticamente**.

## Possíveis Problemas e Soluções
### 1. Dados não carregam
- Verifique a URL do CSV utilizada no script JavaScript.
- Confirme se o servidor onde o CSV está hospedado está acessível.

### 2. Filtros não exibem opções corretamente
- Certifique-se de que o CSV segue o formato esperado pelo script.
- Verifique se os dados carregados contêm valores válidos.

### 3. Cálculo incorreto do saldo de empenho
- Garanta que os valores de quantidade e valor unitário estão sendo lidos corretamente.
- Ajuste a função de parseamento do CSV caso os separadores sejam diferentes do esperado.

## Conclusão
O **Gerador-de-Requisições - Capacidade de Empenho.html** é uma ferramenta eficiente para o acompanhamento da capacidade de empenho, proporcionando uma interface intuitiva e cálculos automáticos para facilitar a tomada de decisão. Caso sejam necessárias personalizações, ajustes podem ser feitos nos seletores, funções de cálculo e layout da página.



# 3 - Documentação do Usuário - app.py

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

