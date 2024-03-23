import csv
import re

# Caminho do arquivo CSV
path = 'data/dsbd_trab2.csv'

# Lista para armazenar as linhas do CSV
data = []

# Abrir o arquivo CSV e ler as linhas
with open(path, 'r', newline='') as file:
    reader = csv.reader(file)
    # Iterar sobre as linhas do CSV e adicioná-las à lista
    for linha in reader:
        data.append(linha)

# Imprimir o conteúdo do objeto linhas_csv
print(data)