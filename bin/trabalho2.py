# UFPR - DSBD : trabalho 2
"""
UFPR
Data Science Big Data
Linguagens de Programação

Trabalho 1 - Usar Dataset 2

Aberto: sábado, 23 mar. 2024, 00:00
Vencimento: sábado, 27 abr. 2024, 23:00

Vamos obter informações sobre o rendimento de alunos de um curso em algumas disciplinas ao longo dos anos.

O primeiro arquivo contido no Dataset Notas, historico-alg1_SIGA_ANONIMIZADO.csv, refere-se ao aproveitamento 
de estudantes na disciplina ALGORITMOS 1 entre os anos de 2011 e 2022.

A primeira coluna ("matricula") é composta por números inteiros, onde cada número representa um indivíduo. 
Assim, repetições nessa coluna indicam que o estudante fez mais de uma vez a mesma matéria.

Atenção: R-nota indica REPROVAÇÃO POR NOTA e R-freq REPROVAÇÃO POR FALTA. 
Se houver outro "status" para representar reprovação, este dever ser trocado para o rótulo adequado (R-nota ou R-freq). 
Frequências < 75 causam reprovação por falta; Médias abaixo de 50 causam reprovação por nota.

Analise o dataset do referido arquivo para responder as seguintes perguntas:

1. Qual é a média de nota dos aprovados (no período total e por ano)?

2. Qual é a média de nota dos reprovados por nota (período total e ano)?

3. Qual é a frequência dos reprovados por nota (período total e por ano)?

4. Qual a porcentagem de evasões (total e anual)?

5. Como os anos de pandemia impactaram no rendimento dos estudantes em relação aos anos anteriores, 
considerando o rendimento dos aprovados, a taxa de cancelamento e as reprovações? 
Considere como anos de pandemia os anos de 2020 e 2021.

6. Compare a volta às aulas híbrida (2022 período 1) com os anos de pandemia e os anos anteriores.

7. Compare a volta às aulas presencial (2022 período 2) com a volta híbrida do item anterior.

"""


# SETUP 
import csv
import re


# GET DATA

# Caminho do arquivo CSV
path = '/home/aenascimento/dsbd_project1/data/dsbd_trab2.csv'

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

# CLEAN DATA
"""
    1. Remove duplicates.
    2. Remove irrelevant data.
    3. Standardize capitalization.
    4. Convert data type.
    5. Clear formatting.
    6. Fix errors.
    7. Language translation.
    8. Handle missing values.
    """
## New dataframe : 

colunas_desejadas = [0, 4, 7, 8, 9, 10]  
data_clean = [[linha[i] for i in colunas_desejadas] for linha in data]
print(data_clean)

# Salvar o novo objeto como um arquivo CSV
path_novo = '/home/aenascimento/dsbd_project1/data/dsbd_trab2_clean.csv'
with open(path_novo, 'w', newline='') as file:
    writer = csv.writer(file)
    # Escrever as linhas no arquivo CSV
    for linha in data_clean:
        writer.writerow(linha)


# ANALYSE DATA


# REPORTS