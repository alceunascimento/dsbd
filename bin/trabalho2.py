#------------------------------------------------------------------------
# UFPR - DSBD : trabalho 2
#------------------------------------------------------------------------
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

#------------------------------------------------------------------------
# SETUP 
#------------------------------------------------------------------------

import csv
import re
dir()


#------------------------------------------------------------------------
# GET DATA
#------------------------------------------------------------------------

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


#------------------------------------------------------------------------
# CLEAN DATA
#------------------------------------------------------------------------
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

#------------------------------------------------------------------------
## Setting a new dataframe clean
target_variables = [0, 3, 4, 7, 8, 9, 10]  
data_clean_raw = [[line[i] for i in target_variables] for line in data]

### Save the new dataframe cleand as CSV file
path_new = '/home/aenascimento/dsbd_project1/data/dsbd_trab2_clean0.csv'
with open(path_new, 'w', newline='') as file:
    writer = csv.writer(file)
    for line in data_clean_raw:
        writer.writerow(line)


#------------------------------------------------------------------------
## Working with the new dataframe cleaned
print("Analisando e limpado o dataframe clean do .CSV (dsbd_trab2_clean0.csv):")       

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

#------------------------------------------------------------------------
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


#------------------------------------------------------------------------
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

#------------------------------------------------------------------------
### Removing outliers
#### removing data of 'tipo' de 'EQUIVALENCIA' (zero and non zero)
#### (assuming the non zero is an error)

##### list of zero grades
notas_zero_equivalencia = []
for row in data_clean:
    if row['tipo'] == 'EQUIVALENCIA' and int(row['nota']) == 0:
        notas_zero_equivalencia.append(row)

"""
headers = list(notas_zero_equivalencia[0].keys())
col_widths = [max(len(str(item)) for item in (row[col] for row in notas_zero_equivalencia)) for col in headers]
header_line = " | ".join(f"{header:{col_widths[i]}}" for i, header in enumerate(headers))
print(header_line)
print("-" * len(header_line))
for row in notas_zero_equivalencia:
    print(" | ".join(f"{str(row[col]):{col_widths[i]}}" for i, col in enumerate(headers)))
"""

##### list of non zero grades
notas_nonzero_equivalencia = []
for row in data_clean:
    if row['tipo'] == 'EQUIVALENCIA' and int(row['nota']) != 0:
        notas_nonzero_equivalencia.append(row)

"""
headers = list(notas_nonzero_equivalencia[0].keys())
col_widths = [max(len(str(item)) for item in (row[col] for row in notas_nonzero_equivalencia)) for col in headers]
header_line = " | ".join(f"{header:{col_widths[i]}}" for i, header in enumerate(headers))
print(header_line)
print("-" * len(header_line))
for row in notas_nonzero_equivalencia:
    print(" | ".join(f"{str(row[col]):{col_widths[i]}}" for i, col in enumerate(headers)))
"""


#### removing data of 'tipo' de 'APROVEITAMENTO'
notas_aproveitamento = []
for row in data_clean:
    if row['tipo'] == 'APROVEITAMENTO':
        notas_aproveitamento.append(row)

"""
headers = list(notas_aproveitamento[0].keys())
col_widths = [max(len(str(item)) for item in (row[col] for row in notas_aproveitamento)) for col in headers]
header_line = " | ".join(f"{header:{col_widths[i]}}" for i, header in enumerate(headers))
print(header_line)
print("-" * len(header_line))
for row in notas_aproveitamento:
    print(" | ".join(f"{str(row[col]):{col_widths[i]}}" for i, col in enumerate(headers)))
"""

#### Combine list to remove from dataframe
outliers = notas_zero_equivalencia + notas_nonzero_equivalencia + notas_aproveitamento


#### Crie um novo dataframe de 'data_clean' excluindo as linhas que estão em 'linhas_para_remover'
data_clean_noOutliers = [row for row in data_clean if row not in outliers]



#------------------------------------------------------------------------
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



#### Set a new dataframe from 'data_clean_nonOutliers' deleting duplicates
data_clean_noOutliers_noDuplicates = [row for row in data_clean_noOutliers if row not in duplicates]


#------------------------------------------------------------------------

# Print new dataframe cleaned
headers = list(data_clean_noOutliers_noDuplicates[0].keys())
col_widths = [max(len(str(item)) for item in (row[col] for row in data_clean_noOutliers_noDuplicates)) for col in headers]
header_line = " | ".join(f"{header:{col_widths[i]}}" for i, header in enumerate(headers))
print(header_line)
print("-" * len(header_line))
for row in data_clean_noOutliers_noDuplicates:
    print(" | ".join(f"{str(row[col]):{col_widths[i]}}" for i, col in enumerate(headers)))


#------------------------------------------------------------------------
### Save the new dataframe cleand as CSV file
path_new = '/home/aenascimento/dsbd_project1/data/dsbd_trab2_clean1.csv'
headers = data_clean_noOutliers_noDuplicates[0].keys()
with open(path_new, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()  # Escreve os cabeçalhos das colunas
    for line in data_clean_noOutliers_noDuplicates:
        writer.writerow(line)



#------------------------------------------------------------------------
### Uniforming 'status' 
#### Assuming that 'Matriculado' deveria ser 'R-nota' ou 'R-freq'

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


#### Applying corrections
def apply_corrections(data, errors):
    for error in errors:
        index, current_status, expected_status = error
        if current_status == 'Matriculado':
            data[index]['status'] = expected_status

# Supondo que você já executou a função check_errors e tem os erros armazenados em 'errors'
errors = check_errors(data_clean_noOutliers_noDuplicates)

# Aplicar correções com base nos erros identificados
apply_corrections(data_clean_noOutliers_noDuplicates, errors)




#------------------------------------------------------------------------
# (re)setting strings to interger when applicable
verificar_e_converter_inteiros(data_clean_noOutliers_noDuplicates)



#------------------------------------------------------------------------
### Save the new dataframe cleand as CSV file
path_new = '/home/aenascimento/dsbd_project1/data/dsbd_trab2_clean2.csv'
headers = data_clean_noOutliers_noDuplicates[0].keys()
with open(path_new, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()  # Escreve os cabeçalhos das colunas
    for line in data_clean_noOutliers_noDuplicates:
        writer.writerow(line)


#------------------------------------------------------------------------
# Setting final dataframe
data_clean_final = data_clean_noOutliers_noDuplicates



#------------------------------------------------------------------------
# CLEANING MEMORY
dir()
#------------------------------------------------------------------------


#------------------------------------------------------------------------
# ANALYSE DATA
#------------------------------------------------------------------------

print("-" * len(header_line))
print("-" * len(header_line))
print("Analisando o dataset")
print("-" * len(header_line))
print("-" * len(header_line))

print("1. Qual é a média de nota dos aprovados (no período total e por ano)?")
print("-" * len(header_line))


#------------------------------------------------------------------------
# 1.a.0 media de nota dos aprovados NO PERIODO TOTAL
aprovados_notas = [row['nota'] for row in data_clean_final if row['status'] == 'Aprovado']
media_total = sum(aprovados_notas) / len(aprovados_notas)
print(f"Média de nota dos aprovados no período total: {media_total:.2f}")



# 1.a.1 Média de nota dos aprovados NO PERÍODO PRE-PANDEMIA, excluindo os anos de 2020 e 2021
aprovados_notas_excluindo_anos = [row['nota'] for row in data_clean_final if row['status'] == 'Aprovado' and row['ano'] not in [2020, 2021]]
if aprovados_notas_excluindo_anos:
    media_total_excluindo_anos = sum(aprovados_notas_excluindo_anos) / len(aprovados_notas_excluindo_anos)
    print(f"Média de nota dos aprovados no período pré-pandemia (excluindo 2020 e 2021): {media_total_excluindo_anos:.2f}")
else:
    print("Não há notas de aprovados para calcular a média, excluindo 2020 e 2021.")



# 1.a.2 Média de nota dos aprovados NO PERÍODO TOTAL dos anos de 2020 e 2021
aprovados_notas_2020_2021 = [row['nota'] for row in data_clean_final if row['status'] == 'Aprovado' and row['ano'] in [2020, 2021]]

if aprovados_notas_2020_2021:
    media_2020_2021 = sum(aprovados_notas_2020_2021) / len(aprovados_notas_2020_2021)
    print(f"Média de nota dos aprovados somente em 2020 e 2021: {media_2020_2021:.2f}")
else:
    print("Não há notas de aprovados para calcular a média em 2020 e 2021.")

variacao_rendimento_pandemia = ((media_2020_2021 / media_total_excluindo_anos) - 1) *100
variacao_rendimento_pandemia


# 1.b.0 media de nota dos aprovados POR ANO
grades_by_year = {}
for row in data_clean_final:
    if row['status'] == 'Aprovado':
        year = row['ano']
        grade = row['nota']
        if year not in grades_by_year:
            grades_by_year[year] = []
        grades_by_year[year].append(grade)
# Calculating and printing the average grades by year
for year in sorted(grades_by_year.keys(), key=int):
    grades = grades_by_year[year]
    average_grade = sum(grades) / len(grades) if grades else 0
    print(f"Média de nota dos aprovados em {year}: {average_grade:.2f}")


# 1.b.1. media de nota dos aprovados por PERIODO de 2022
grades_2022_period_1 = []
grades_2022_period_2 = []

for row in data_clean_final:
    if row['status'] == 'Aprovado' and row['ano'] == 2022:
        grade = row['nota']
        if row['periodo'] == 1:
            grades_2022_period_1.append(grade)
        elif row['periodo'] == 2:
            grades_2022_period_2.append(grade)

if grades_2022_period_1:
    average_grade_period_1 = sum(grades_2022_period_1) / len(grades_2022_period_1)
    print(f"Média de nota dos aprovados em 2022 - Período 1: {average_grade_period_1:.2f}")
else:
    print("Não há notas de aprovados em 2022 - Período 1 para calcular a média.")

if grades_2022_period_2:
    average_grade_period_2 = sum(grades_2022_period_2) / len(grades_2022_period_2)
    print(f"Média de nota dos aprovados em 2022 - Período 2: {average_grade_period_2:.2f}")
else:
    print("Não há notas de aprovados em 2022 - Período 2 para calcular a média.")



#------------------------------------------------------------------------
# 2. Qual é a média de nota dos reprovados por nota (período total e ano)?
print("-" * len(header_line))
print("2. Qual é a média de nota dos reprovados por nota (período total e ano)?")
print("-" * len(header_line))



# 2.a.0 média do notas dos reprovados no periodo TOTAL
reprovados_notas = [float(row['nota']) for row in data_clean_final if row['status'] == 'R-nota']
media_total_reprovados = sum(reprovados_notas) / len(reprovados_notas) if reprovados_notas else 0
print(f"Média de nota dos reprovados por nota no período total: {media_total_reprovados:.2f}")



# 2.a.1 Média de nota dos reprovados NO PERÍODO PRE-PANDEMIA, excluindo os anos de 2020 e 2021
reprovados_notas_excluindo_anos = [row['nota'] for row in data_clean_final if row['status'] == 'R-nota' and row['ano'] not in [2020, 2021]]
if reprovados_notas_excluindo_anos:
    media_reprovados_total_excluindo_anos = sum(reprovados_notas_excluindo_anos) / len(reprovados_notas_excluindo_anos)
    print(f"Média de nota dos reprovados no período pré-pandemia (excluindo 2020 e 2021): {media_reprovados_total_excluindo_anos:.2f}")
else:
    print("Não há notas de reprovados para calcular a média, excluindo 2020 e 2021.")



# 2.a.2 Média de nota dos reprovados NO PERÍODO TOTAL dos anos de 2020 e 2021
reprovados_notas_2020_2021 = [row['nota'] for row in data_clean_final if row['status'] == 'R-nota' and row['ano'] in [2020, 2021]]

if reprovados_notas_2020_2021:
    media_reprovados_2020_2021 = sum(reprovados_notas_2020_2021) / len(reprovados_notas_2020_2021)
    print(f"Média de nota dos reprovados somente em 2020 e 2021: {media_reprovados_2020_2021:.2f}")
else:
    print("Não há notas de reprovados para calcular a média em 2020 e 2021.")

variacao_rendimento_reprovados_pandemia = ((media_reprovados_2020_2021 / media_reprovados_total_excluindo_anos) - 1) *100
variacao_rendimento_reprovados_pandemia



# 2.b.0 média de notas dos reprovados POR ANO
grades_by_year_reprovados = {}
for row in data_clean_final:
    if row['status'] == 'R-nota':
        year = row['ano']
        grade = row['nota']
        if year not in grades_by_year_reprovados:
            grades_by_year_reprovados[year] = []
        grades_by_year_reprovados[year].append(grade)

for year in sorted(grades_by_year_reprovados.keys(), key=int):
    grades = grades_by_year_reprovados[year]
    average_grade_reprovados = sum(grades) / len(grades) if grades else 0
    print(f"Média de nota dos reprovados por nota em {year}: {average_grade_reprovados:.2f}")



# 2.b.1. media de nota dos aprovados por PERIODO de 2022
grades_failed_2022_period_1 = []
grades_failed_2022_period_2 = []

for row in data_clean_final:
    if row['status'] == 'R-nota' and row['ano'] == 2022:
        grade = row['nota']
        if row['periodo'] == 1:
            grades_failed_2022_period_1.append(grade)
        elif row['periodo'] == 2:
            grades_failed_2022_period_2.append(grade)

if grades_failed_2022_period_1:
    average_failed_grade_period_1 = sum(grades_failed_2022_period_1) / len(grades_failed_2022_period_1)
    print(f"Média de nota dos reprovados em 2022 - Período 1: {average_failed_grade_period_1:.2f}")
else:
    print("Não há notas de reprovados em 2022 - Período 1 para calcular a média.")

if grades_failed_2022_period_2:
    average_failed_grade_period_2 = sum(grades_failed_2022_period_2) / len(grades_failed_2022_period_2)
    print(f"Média de nota dos reprovados em 2022 - Período 2: {average_failed_grade_period_2:.2f}")
else:
    print("Não há notas de reprovados em 2022 - Período 2 para calcular a média.")








#------------------------------------------------------------------------
# 3. Qual é a frequência dos reprovados por nota (período total e por ano)?
print("-" * len(header_line))
print("3. Qual é a frequência dos reprovados por nota (período total e por ano)?")
print("-" * len(header_line))



# 3.a. frequencia media do periodo
frequencias_reprovados_nota = [row['frequencia'] for row in data_clean_final if row['status'] == 'R-nota']
media_frequencia_total = sum(frequencias_reprovados_nota) / len(frequencias_reprovados_nota) if frequencias_reprovados_nota else 0
print(f"Média de frequência dos reprovados por nota no período total: {media_frequencia_total:.2f}")

frequencias_reprovados_nota



# 3.b. frequencia media POR ANO

frequencias_por_ano = {}

for row in data_clean_final:
    if row['status'] == 'R-nota':
        year = row['ano']
        frequency = row['frequencia']  # 'frequencia' já é um integer
        if year not in frequencias_por_ano:
            frequencias_por_ano[year] = []
        frequencias_por_ano[year].append(frequency)

for year in sorted(frequencias_por_ano.keys(), key=int):
    frequencies = frequencias_por_ano[year]
    average_frequency = sum(frequencies) / len(frequencies) if frequencies else 0
    print(f"Média de frequência dos reprovados por nota em {year}: {average_frequency:.2f}")



#------------------------------------------------------------------------
# 4. Qual a porcentagem de evasões (total e anual)?
print("-" * len(header_line))
print("4. Qual a porcentagem de evasões (total e anual)?")
print("-" * len(header_line))



# 4.a. evasao total
total_alunos = len(data_clean_final)
total_cancelados = sum(1 for row in data_clean_final if row['status'] == 'Cancelado')
taxa_evasao_total = (total_cancelados / total_alunos) * 100
print(f"Taxa de evasão total: {taxa_evasao_total:.2f}%")




# 4.b. evasao por anos
# Inicializando dicionários para contar alunos e cancelamentos por ano
alunos_por_ano = {}
cancelamentos_por_ano = {}

for row in data_clean_final:
    ano = row['ano']
    # Contar alunos por ano
    if ano in alunos_por_ano:
        alunos_por_ano[ano] += 1
    else:
        alunos_por_ano[ano] = 1

    # Contar cancelamentos por ano
    if row['status'] == 'Cancelado':
        if ano in cancelamentos_por_ano:
            cancelamentos_por_ano[ano] += 1
        else:
            cancelamentos_por_ano[ano] = 1



# Calculando e imprimindo a taxa de evasão por ano, ordenado pelo ano
taxas_evasao_por_ano = {}

for ano in sorted(alunos_por_ano.keys(), key=int):
    total_alunos_ano = alunos_por_ano[ano]
    cancelamentos_ano = cancelamentos_por_ano.get(ano, 0)
    taxa_evasao_ano = (cancelamentos_ano / total_alunos_ano) * 100
    taxas_evasao_por_ano[ano] = taxa_evasao_ano  # Armazena a taxa de evasão no dicionário
    print(f"Taxa de evasão em {ano}: {taxa_evasao_ano:.2f}%")



# Inicializa a soma das taxas de evasão e conta quantos anos estão sendo considerados
soma_taxa_evasao_prepandemia = 0
contagem_anos_prepandemia = 0

for ano in range(2011, 2020):  # Inclui de 2011 até 2019
    if ano in alunos_por_ano:  # Verifica se o ano possui dados
        total_alunos_ano = alunos_por_ano[ano]
        cancelamentos_ano = cancelamentos_por_ano.get(ano, 0)  # Usa .get() para evitar KeyError caso não haja cancelamentos
        taxa_evasao_ano = (cancelamentos_ano / total_alunos_ano) * 100
        soma_taxa_evasao_prepandemia += taxa_evasao_ano
        contagem_anos_prepandemia += 1

# Calcula a média da taxa de evasão pré-pandemia
media_evasao_prepandemia = soma_taxa_evasao_prepandemia / contagem_anos_prepandemia
print(f"Média de evasão pré-pandemia (2011-2019): {media_evasao_prepandemia:.2f}%")



#------------------------------------------------------------------------
# 5. Como os anos de pandemia impactaram no rendimento dos estudantes em relação aos anos anteriores, 
# considerando o rendimento dos aprovados, a taxa de cancelamento e as reprovações? 
# Considere como anos de pandemia os anos de 2020 e 2021.
print("-" * len(header_line))
print(f"5. Como os anos de pandemia impactaram no rendimento dos estudantes em relação aos anos anteriores, considerando o rendimento dos aprovados, a taxa de cancelamento e as reprovações? Considere como anos de pandemia os anos de 2020 e 2021.\n")
print("-" * len(header_line))



print(f"Nos anos de pandemia é possível ver que o rendimento dos aprovados teve um incremento de {variacao_rendimento_pandemia:.2f}%")
print(f"Já as taxas de evasão, que tinham um histórico de {media_evasao_prepandemia:.2f}%, foram para {taxas_evasao_por_ano[2020]:.2f}% em 2020.")
print(f"Por fim, com relação as reprovações, observa-se que a média das notas baixou de [media pre pandemia] para [media de 2020] e [media de 2021], mesmo a frequencia tendo subido de [media pre pandemia] para [media de 2020] e [media de 2021] ")


#------------------------------------------------------------------------
# 6. Compare a volta às aulas híbrida (2022 período 1) com os anos de pandemia e os anos anteriores.
print("-" * len(header_line))
print("6. Compare a volta às aulas híbrida (2022 período 1) com os anos de pandemia e os anos anteriores.")
print("-" * len(header_line))

print(f"")



#------------------------------------------------------------------------
# 7. Compare a volta às aulas presencial (2022 período 2) com a volta híbrida do item anterior.
print("-" * len(header_line))
print("7. Compare a volta às aulas presencial (2022 período 2) com a volta híbrida do item anterior.")
print("-" * len(header_line))

print(f"")


