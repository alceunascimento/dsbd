import pandas as pd
import os
import time

start_time = time.time()
csv_path = '~/dsbd/bancodados/data/complaints.csv'
df = pd.read_csv(csv_path, sep=',')
end_time = time.time()
elapsed_time = end_time - start_time
print("Tempo para ler:", elapsed_time, "segundos")
input("Pressione Enter para continuar...")

start_time = time.time()
filtro = df.loc[df['Product'] == 'PRODUTO DE TESTES']
end_time = time.time()
elapsed_time = end_time - start_time
print("Tempo para buscar:", elapsed_time, "segundos")
print(filtro)

