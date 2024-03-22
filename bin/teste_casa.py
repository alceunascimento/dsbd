import csv
import re

# Caminho do arquivo CSV
path = 'dsbd_trab1.csv'

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

# Criar um novo objeto para armazenar o texto encontrado com a regex
search = []

# Iterar sobre as linhas do CSV e procurar por vírgulas com três caracteres antes e depois
for line in data:
    # Usar regex para encontrar vírgulas com três caracteres antes e depois
    resultados = re.findall(r'(\w{3}),(\w{3})', ','.join(line))
    # Adicionar os valores encontrados à lista
    search.extend(resultados)

# Imprimir os valores encontrados
print(search)
