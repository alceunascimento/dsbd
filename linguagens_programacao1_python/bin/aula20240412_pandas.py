import pandas as pd

dados = {
    'nome': ["Ana", "Bob", "Cleo"],
    'idade': [50, 36, 2],
    'altura': [1.4, 1.73, 0.61]
}
dados

# serie
serie1 = pd.Series(dados)
serie1


# dataframe
df1 = pd.DataFrame(serie1)
df1

df2 = pd.DataFrame(dados)
df2

df2.describe()

# qual a maior idade
df2['idade'].max()
# quem é o mais baixo
df2['altura'].min()
# qual é a média de altura
df2['altura'].mean()
# qual é a soma das idades
df2['idade'].sum()

 
Pesos = [50.8, 75, 11.3]
df2['peso'] = Pesos
df2

del df2['nome']
df2

df3 = df2.drop(['peso'], axis=1)
df3

df4 = {'idade': [50], 'altura': [1.50]}
df4
df4 = pd.DataFrame(df4)
df4

df5 = pd.concat([df3, df4], ignore_index=True)

df6 = pd.concat([df2, df4], ignore_index=True)
df6.isna()


