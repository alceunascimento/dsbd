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
dir()

# GET DATA

# Caminho do arquivo CSV
path = '/home/aenascimento/dsbd_project1/data/dsbd_trab2.csv'

# Lista para armazenar as linhas do CSV
data = []

# Abrir o arquivo CSV e ler as linhas
with open(path, 'r', newline='') as file:
    reader = csv.reader(file)
    # Iterar sobre as linhas do CSV e adicioná-las à lista
    for line in reader:
        data.append(line)
data

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

## Setting a new dataframe cleaned
target_variables = [0, 3, 4, 7, 8, 9, 10]  
data_clean = [[line[i] for i in target_variables] for line in data]

### Print for better visual
col_widths = [max(len(str(item)) for item in col) for col in zip(*data_clean)]
header = data_clean[0]
header_line = " | ".join(f"{item:{col_widths[i]}}" for i, item in enumerate(header))
print(header_line)
print("-" * len(header_line))
for row in data_clean[1:]:
    print(" | ".join(f"{str(item):{col_widths[i]}}" for i, item in enumerate(row)))

### Save the new dataframe cleand as CSV file
path_new = '/home/aenascimento/dsbd_project1/data/dsbd_trab2_clean0.csv'
with open(path_new, 'w', newline='') as file:
    writer = csv.writer(file)
    for line in data_clean:
        writer.writerow(line)


## Working with the new dataframe cleaned
       
### Lista para armazenar as linhas do CSV
data_clean = []
data_clean

### Open CSV (use Dic.Reader to dictionary output)
with open(path_new, 'r', newline='') as file:
    reader = csv.DictReader(file)
    for line in reader:
        data_clean.append(line)
data_clean
data_clean[0]

### checar os valores das variaveis
value_matricula = {line['matricula'] for line in data_clean}
value_matricula
value_periodo = {line['periodo'] for line in data_clean}
value_periodo
value_ano = {line['ano'] for line in data_clean}
value_ano
value_nota = {line['nota'] for line in data_clean}
value_nota
value_freq = {line['frequencia'] for line in data_clean}
value_freq
value_status = {line['status'] for line in data_clean}
value_tipo = {linha['tipo'] for linha in data_clean}
value_tipo


### Setting string to integer when applicable

#### functions to check if value in a integer and to iterate transformation to integer
def is_convertible_to_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def verificar_e_converter_inteiros(data_clean):
    for col_name in data_clean[0].keys():  # Assumindo que todas as linhas têm as mesmas chaves
        # Verificar se algum valor na coluna NÃO é convertível para int
        if not all(is_convertible_to_int(line[col_name]) for line in data_clean):
            print(f"Não foi possível converter todos os valores na coluna '{col_name}' para inteiros.")
        else:
            # Se todos os valores forem convertíveis, realizar a conversão
            for line in data_clean:
                line[col_name] = int(line[col_name])
            print(f"Todos os valores na coluna '{col_name}' foram convertidos para inteiros.")

#### Iterate transformation
verificar_e_converter_inteiros(data_clean)



### Find missing values 

def check_missing_values(data_clean):
    columns_with_missing = set()  # Set to store the names of columns with missing values

    for line in data_clean:
        for key, value in line.items():
            if value == '' or value is None:  # Add more conditions as needed
                columns_with_missing.add(key)
    
    if not columns_with_missing:
        print("There are no missing values.")
    else:
        print("There are missing values in the following columns:", columns_with_missing)

check_missing_values(data_clean)


### Removing outliers

#### removing data of 'tipo' de 'EQUIVALENCIA' (zero and non zero)
#### (assuming the non zero is an error)

##### list of zero grades
notas_zero_equivalencia = []
for row in data_clean:
    if row['tipo'] == 'EQUIVALENCIA' and int(row['nota']) == 0:
        notas_zero_equivalencia.append(row)

headers = list(notas_zero_equivalencia[0].keys())
col_widths = [max(len(str(item)) for item in (row[col] for row in notas_zero_equivalencia)) for col in headers]
header_line = " | ".join(f"{header:{col_widths[i]}}" for i, header in enumerate(headers))
print(header_line)
print("-" * len(header_line))
for row in notas_zero_equivalencia:
    print(" | ".join(f"{str(row[col]):{col_widths[i]}}" for i, col in enumerate(headers)))


##### list of non zero grades
notas_nonzero_equivalencia = []
for row in data_clean:
    if row['tipo'] == 'EQUIVALENCIA' and int(row['nota']) != 0:
        notas_nonzero_equivalencia.append(row)

headers = list(notas_nonzero_equivalencia[0].keys())
col_widths = [max(len(str(item)) for item in (row[col] for row in notas_nonzero_equivalencia)) for col in headers]
header_line = " | ".join(f"{header:{col_widths[i]}}" for i, header in enumerate(headers))
print(header_line)
print("-" * len(header_line))
for row in notas_nonzero_equivalencia:
    print(" | ".join(f"{str(row[col]):{col_widths[i]}}" for i, col in enumerate(headers)))



#### removing data of 'tipo' de 'APROVEITAMENTO'
notas_aproveitamento = []
for row in data_clean:
    if row['tipo'] == 'APROVEITAMENTO':
        notas_aproveitamento.append(row)

headers = list(notas_aproveitamento[0].keys())
col_widths = [max(len(str(item)) for item in (row[col] for row in notas_aproveitamento)) for col in headers]
header_line = " | ".join(f"{header:{col_widths[i]}}" for i, header in enumerate(headers))
print(header_line)
print("-" * len(header_line))
for row in notas_aproveitamento:
    print(" | ".join(f"{str(row[col]):{col_widths[i]}}" for i, col in enumerate(headers)))




#### Combine list to remove from dataframe
outliers = notas_zero_equivalencia + notas_nonzero_equivalencia + notas_aproveitamento

#### Crie um novo dataframe de 'data_clean' excluindo as linhas que estão em 'linhas_para_remover'
data_clean_noOutliers = [row for row in data_clean if row not in outliers]


### Removing duplicates

# Open a blanik set for uniques
unique = set()

# Open a list for duplicates
duplicates = []

for row in data_clean_noOutliers:
    # Convert list (dict) to tuple (hashable)
    row_tuple = tuple(sorted(row.items()))
    
    # Conditions
    if row_tuple in unique:
        # If yes, add to duplicates
        duplicates.append(row)
    else:
        # If not, add to uniques
        unique.add(row_tuple)

# Now duplicates has all duplicates found
if duplicates:
    print(f"Duplicates found: {len(duplicates)} rows.")
else:
    print("There are no duplicates.")

duplicates

#### Set a new dataframe from 'data_clean_nonOutliers' deleting duplicates
data_clean_noOutliers_noDuplicates = [row for row in data_clean_noOutliers if row not in duplicates]

# Print new dataframe cleaned
headers = list(data_clean_noOutliers_noDuplicates[0].keys())
col_widths = [max(len(str(item)) for item in (row[col] for row in data_clean_noOutliers_noDuplicates)) for col in headers]
header_line = " | ".join(f"{header:{col_widths[i]}}" for i, header in enumerate(headers))
print(header_line)
print("-" * len(header_line))
for row in data_clean_noOutliers_noDuplicates:
    print(" | ".join(f"{str(row[col]):{col_widths[i]}}" for i, col in enumerate(headers)))


### Save the new dataframe cleand as CSV file
path_new = '/home/aenascimento/dsbd_project1/data/dsbd_trab2_clean1.csv'
with open(path_new, 'w') as file:
    writer = csv.writer(file)
    for line in data_clean_noOutliers_noDuplicates:
        writer.writerow(line)



### Uniforming 'status' 

#### Checking errors
    
def check_errors(data):
    errors = []
    for i, row in enumerate(data):
        expected_status = ''
        if row['frequencia'] < 75:
            expected_status = 'R-freq'
        elif row['frequencia'] >= 75 and row['nota'] < 50:
            expected_status = "R-nota"
        elif row['frequencia'] >= 75 and row['nota'] >= 50:
            expected_status = 'Aprovado'
        # Assuming other status determination rules here if needed
        
        if row['status'] != expected_status:
            errors.append((i, row['status'], expected_status))
    
    return errors

# Check for errors
errors = check_errors(data_clean_noOutliers_noDuplicates)

if errors:
    for error in errors:
        print(f"Row {error[0]}: Incorrect status '{error[1]}', expected '{error[2]}'")
else:
    print("No errors found.")












#### There should be only two values for failed 'R-freq' or 'R-nota'
status = []


for row in data_clean_noOutliers_noDuplicates:
    if row['status'] == 'APROVEITAMENTO':
        notas_aproveitamento.append(row)


unique_statuses = {row['status'] for row in data_clean_noOutliers_noDuplicates}

print(unique_statuses)


# ANALYSE DATA


# REPORTS

