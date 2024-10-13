
# Exercícios
# Linguagens de Programação
# Módulo 1
# Prof. André Grégio

# setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Exercícios - crime

# Dado o arquivo SacramentocrimeJanuary2006.csv:
file1 = "/home/espinf/aenascimento/dsbd/lingprog/data/sacramentocrimeJanuary2006.csv"
df1 = pd.read_csv(file1)
df1

# 1. Qual a quantidade de crimes por data?
df1['cdatetime'].count()
df1.groupby(['cdatetime']).count()
df1.groupby(['cdatetime']).size()
df1.groupby(['cdatetime', 'crimedescr']).size()
df1['cdatetime'] = pd.to_datetime(df1['cdatetime'])

# 2. Qual a porcentagem de crimes por tipo de crime no mês inteiro?
# 3. Qual a porcentagem de crimes por tipo de crime por dia?
# 4. Qual a média de ocorrências de crime (total de crimes) por distrito no mês?


# Exercícios - imóveis

# No arquivo Sacramentorealestatetransactions.csv
file2 = "/home/espinf/aenascimento/dsbd/lingprog/data/sacramentorealestatetransactions.csv"
df2 = pd.read_csv(file2)
df2


# 1. Quantos e quais são os tipos de imóveis?
# 2. Quantos imóveis de cada tipo estão à venda?
# 3. Considerando o dataset inteiro, qual a média de:
# a. Banheiros por casa?
# b. Quartos por casa?
# c. Tamanho das casas em metros quadrados (deve ser convertido de square feet)?
# 4. Qual CEP:
# a. Tem os imóveis mais baratos (em média)?
# b. E os mais caros (em média)?
# c. O imóvel mais barato?
# d. O imóvel mais caro?
# 5. Qual o preço médio dos imóveis em Sacramento?


# Exercícios - pagamentos

# No arquivo SalesJan2009.csv:
file3 = "/home/espinf/aenascimento/dsbd/lingprog/data/SalesJan2009.csv"
df3 = pd.read_csv(file3)
df3


# 1. Quantos países estão listados no dataset?
# 2. Qual a distribuição dos tipos de pagamento no dataset (em porcentagem)?
# 3. Qual a média de gasto por bandeira de cartão disponível (“Payment_Type”)?
