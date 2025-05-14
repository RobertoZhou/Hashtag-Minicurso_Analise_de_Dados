"""
    - Passo 1: Importar a base de dados
    - Passo 2: Visualizar e tratar essa base de dados
    - Passo 3: "Dar uma olhada" na sua base de dados
    - passo 4: Construir uma análise oara identificar o motivo de cancelamento
        - Identificar qual o motivo ou os principaís motivos dos clientes estarem cancelando o cartão de crédito
"""

import pandas as pd

tabela = pd.read_csv("ClientesBanco.csv", encoding="latin-1")

tabela = tabela.drop("CLIENTNUM", axis=1)

print(tabela.info())

print(tabela.describe().round(1))

