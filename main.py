"""
    - Passo 1: Importar a base de dados
    - Passo 2: Visualizar e tratar essa base de dados
    - Passo 3: "Dar uma olhada" na sua base de dados
    - passo 4: Construir uma análise oara identificar o motivo de cancelamento
        - Identificar qual o motivo ou os principaís motivos dos clientes estarem cancelando o cartão de crédito
"""

import pandas as pd
import plotly.express as px


tabela = pd.read_csv("ClientesBanco.csv", encoding="latin-1")

tabela = tabela.drop("CLIENTNUM", axis=1)

#   Agora vamos tratar valores vazios e exibir um resumo das colunas da base de dados
tabela = tabela.dropna()

print(tabela.info())
print(tabela.describe().round(1))

#   Vamos avaliar como está a diviso entre Clientes x Cancelados
qtde_categoria = tabela["Categoria"].value_counts()
print(qtde_categoria)

qtde_percentual = tabela["Categoria"].value_counts(normalize=True)
print(qtde_percentual)

print("=" * 25)

#   Temos várias formas de descobrir o motivo de cancelamento
#       - Podemos olhar a comparação entre Clientes e Cancelados em cada uma das colunas da nossa base de dados, para ver se essa informação traz algum insight novo para a gente

for coluna in tabela:
    grafico = px.histogram(tabela, x=coluna, color="Categoria")
    print(grafico.show())

#   Informaçôes retiradas da análise:
#       - Me parece que quanto mais produtos contratados um cliente tem, menor a chance dele cancelar
#       - E quanto mais transaçôes e quanto maior o valor de transação, menor a chance dele cancelar
#       - Quanto maior a quantidade de contatos que a pessoa teve que fazer, maior a chance dela cancelar