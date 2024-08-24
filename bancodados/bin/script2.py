import pandas as pd
import os
import subprocess
import time

start_time = time.time()
csv_path = '~/dsbd/bancodados/data/microdados_ed_basica_2022.csv'
df = pd.read_csv(csv_path, sep=',')
end_time = time.time()
elapsed_time = end_time - start_time
print("Tempo para ler:", elapsed_time, "segundos")
input("Pressione Enter para continuar...")

print(df.head()) 


# Identifica o encoding usando o comando `file -bi`
result = subprocess.run(['file', '-bi', csv_path], capture_output=True, text=True)
print(result)
output = result.stdout

# Extrai o encoding do output
encoding = 'utf-8'  # Default
if 'charset=' in output:
    encoding = output.split('charset=')[-1].strip()

# Exibe o encoding detectado e permite ao usuário escolher outro
print(f"Encoding detectado: {encoding}")
user_encoding = input("Digite o encoding a ser utilizado ou pressione Enter para usar o detectado: ")

# Usa o encoding escolhido pelo usuário ou o detectado
final_encoding = user_encoding if user_encoding else encoding

# Lê o arquivo CSV com o encoding especificado
start_time = time.time()
df = pd.read_csv(csv_path, sep=',', encoding=final_encoding)
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Tempo para ler: {elapsed_time} segundos")
input("Pressione Enter para continuar...")








start_time = time.time()
filtro = df.loc[df['Product'] == 'PRODUTO DE TESTES']
end_time = time.time()
elapsed_time = end_time - start_time
print("Tempo para buscar:", elapsed_time, "segundos")
print(filtro)

