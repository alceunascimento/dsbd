# trabalhando com datas

# setup
import pandas as pd
import matplotlib.pyplot as plt

# * Item 1


# * Item 2

dados = {'nome': ["Ana", "Bob", "Cleo"],
         'idade': [50, 36, 2],
         'altura': [1.5, 1.73, .61]}

df = pd.DataFrame(dados, columns = ['nome', 'idade', 'altura'])
df

df.plot(x='idade', y='altura', kind='bar')
plt.show()


sdf = df.sort_values('idade')
sdf.plot(x='idade', y='altura', kind='bar')
plt.show()


# * Item 3

df = pd.read_csv("/home/espinf/aenascimento/dsbd/lingprog/data/informe_epidemiologico_21_05_2020.csv",
                 delimiter=",",
                 usecols=['RS','IBGE','Casos','Óbitos','Município de residência'])
df

df.sort_values(by=['Casos'], inplace=True, ascending=False)
top5 = df.head(5) # Obtém os 5 maiores valores
top5


ax = top5.plot(kind='bar', x='Município de residência',
y='Casos')
top5.plot(kind='bar',
x='Município de residência',
y='Óbitos',
ax=ax,
color='red')
plt.show()


top5.plot(kind='pie',y='Casos')
plt.show()


top5.plot(kind='pie', y='Casos', labels=top5['Muncípio de residência'])
plt.show()


