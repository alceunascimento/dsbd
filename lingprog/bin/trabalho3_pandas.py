#------------------------------------------------------------------------
# UFPR - DSBD : trabalho 2
# Escopo: importa, limpar e analisar um dataset
#------------------------------------------------------------------------
"""
Informações sobre o rendimento de alunos de um curso em algumas disciplinas ao longo dos anos.
O primeiro arquivo contido no Dataset Notas, historico-alg1_SIGA_ANONIMIZADO.csv, refere-se ao aproveitamento 
de estudantes na disciplina ALGORITMOS 1 entre os anos de 2011 e 2022.
A primeira coluna ("matricula") é composta por números inteiros, onde cada número representa um indivíduo. 
Assim, repetições nessa coluna indicam que o estudante fez mais de uma vez a mesma matéria.
Atenção: R-nota indica REPROVAÇÃO POR NOTA e R-freq REPROVAÇÃO POR FALTA. 
Se houver outro "status" para representar reprovação, este dever ser trocado para o rótulo adequado (R-nota ou R-freq). 
Frequências < 75 causam reprovação por falta; Médias abaixo de 50 causam reprovação por nota.
"""
print("UFPR")
print("Data Science Big Data")
print("Linguagens de Programação")
print("Trabalho 1 - Usar Dataset 2")
print("Vencimento: sábado, 27 abr. 2024, 23:00")
print("Aluno: Alceu Eilert Nascimento")


#------------------------------------------------------------------------
# SETUP 
#------------------------------------------------------------------------
import csv
import re
import pandas as pd
import matplotlib.pyplot as plt
dir()


#------------------------------------------------------------------------
# GET DATA
#------------------------------------------------------------------------

# Caminho do arquivo CSV
path =  r"C:\Users\DELL\OneDrive\python\python_projects\dsbd\lingprog\data\dsbd_trab2.csv"

df = pd.read_csv(path, encoding='UTF-8')
df


#------------------------------------------------------------------------
# CLEAN DATA
#------------------------------------------------------------------------
"""
Remove irrelevant data.
Convert data type.
Remove duplicates.
Clear formatting.
Fix errors.
Handle missing values.
"""
print("\n")
print("------------------------------------------------------------------")
print("------------------------------------------------------------------")
print("A. Limpado o dataframe do arquivo .CSV (dsbd_trab2_clean0.csv):")       
print("------------------------------------------------------------------")
print("------------------------------------------------------------------")
print("\n")
print("A. I. Premissas da analise:")
print(f"- Variáveis escolhidas: matricula, período, ano, nota, frequencia, status, tipo.")
print(f"- Variáveis desconsideradas: código, disciplina, curriculo, ch, obs, natureza, situacaoDiscente, nomeTurma, codigoCuriculoSie.")

# Colunas escolhidas
colunas_escolhidas = ['matricula', 'periodo', 'ano', 'nota', 'frequencia', 'status', 'tipo']

# Selecionando apenas as colunas escolhidas
df_limpo = df[colunas_escolhidas]
df_limpo

# Verificando dados faltantes
print("Dados Faltantes por Coluna:")
print(df_limpo.isnull().sum())

# Convertendo tipos de dados se necessário
df_limpo['nota'] = pd.to_numeric(df_limpo['nota'], errors='coerce')
df_limpo['frequencia'] = pd.to_numeric(df_limpo['frequencia'], errors='coerce')

df_limpo

# Verificar os primeiros registros após limpeza
print("DataFrame Limpo:")
print(df_limpo.head())
print(f"Total de registros após limpeza: {df_limpo.shape[0]}")

# Aplicando o filtro para manter apenas os registros que não são de 'EQUIVALENCIA' ou 'APROVEITAMENTO'
df_limpo = df_limpo[~df_limpo['tipo'].isin(['EQUIVALENCIA', 'APROVEITAMENTO'])]

# Verificando o resultado
print("DataFrame após remoção de outliers:")
print(df_limpo.head())
print(f"Total de registros após limpeza: {df_limpo.shape[0]}")




import numpy as np  # Importando NumPy


def check_and_correct_status(df):
    # Define a nova coluna 'expected_status' baseada nas condições dadas
    conditions = [
        (df['frequencia'] < 75),
        (df['frequencia'] >= 75) & (df['nota'] < 50),
        (df['frequencia'] >= 75) & (df['nota'] >= 50)
    ]
    choices = ['R-freq', 'R-nota', 'Aprovado']
    df['expected_status'] = np.select(conditions, choices, default=df['status'])

    # Identificar onde o status atual não coincide com o esperado
    mask = (df['status'] != df['expected_status']) & (df['status'] == 'Matriculado')
    
    # Aplicar correções
    df.loc[mask, 'status'] = df.loc[mask, 'expected_status']

    # Verificação de discrepâncias
    discrepant_statuses = df[df['status'] != df['expected_status']]
    if not discrepant_statuses.empty:
        print("Status corrigidos com discrepâncias:")
        print(discrepant_statuses)
    else:
        print("Todos os status estão corretos.")

    # Remover a coluna 'expected_status' após todas as verificações necessárias
    df.drop(columns=['expected_status'], inplace=True)

# Chamar a função para verificar e corrigir o status
check_and_correct_status(df_limpo)  # Substitua 'df_limpo' pelo nome do seu DataFrame
df_limpo
