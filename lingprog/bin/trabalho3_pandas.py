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
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt
import numpy as np
import sys 
dir()


#------------------------------------------------------------------------
# GET DATA
#------------------------------------------------------------------------

# Caminho do arquivo CSV
# path = sys.argv[1] # para chamar o arquivo com o dataset como argumento no terminal
# path =  "/home/aenascimento/dsbd/lingprog/data/dsbd_trab2.csv"  # rodar em casa
path = "/home/espinf/aenascimento/dsbd/lingprog/data/dsbd_trab2.csv"  # rodar na UFPR

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
print("A. Limpando o dataframe do arquivo .CSV (dsbd_trab2_clean0.csv):")       
print("------------------------------------------------------------------")
print("\n")
print("A. I. Premissas da analise:")
print(f"- Variáveis escolhidas: matricula, período, ano, nota, frequencia, status, tipo.")
print(f"- Variáveis desconsideradas: código, disciplina, curriculo, ch, obs, natureza, situacaoDiscente, nomeTurma, codigoCuriculoSie.")
print("\n")

# Colunas escolhidas
colunas_escolhidas = ['matricula', 'periodo', 'ano', 'nota', 'frequencia', 'status', 'tipo']

# Selecionando apenas as colunas escolhidas
df_limpo = df[colunas_escolhidas]
df_limpo

# Verificando dados faltantes
print("Dados Faltantes por Coluna:")
print(df_limpo.isnull().sum())
print("\n")

# Convertendo tipos de dados se necessário
df_limpo['nota'] = pd.to_numeric(df_limpo['nota'], errors='coerce')
df_limpo['frequencia'] = pd.to_numeric(df_limpo['frequencia'], errors='coerce')
df_limpo
print("\n")

# Verificar os primeiros registros após limpeza
print("DataFrame Limpo:")
print(df_limpo.head())
print(f"Total de registros após limpeza: {df_limpo.shape[0]}")
print("\n")

# Aplicando o filtro para manter apenas os registros que não são de 'EQUIVALENCIA' ou 'APROVEITAMENTO'
print(r"Dado que se quer analisar os alunos que efetivamente frequentaram as aulas, foram retirados os `status` de `EQUIVALENCIA` e `APROVEITAMENTO` , restando o seguinte dataFrame após remoção:")
df_limpo = df_limpo[~df_limpo['tipo'].isin(['EQUIVALENCIA', 'APROVEITAMENTO'])]
print(df_limpo.head())
print(f"Total de registros após limpeza: {df_limpo.shape[0]}")
print("\n")

# Homogenizando o status para R-nota ou R-freq
print(r"Dado que se houver outro `status` para representar reprovação, este dever ser trocado para o rótulo adequado (R-nota ou R-freq), resta o seguinte dataFrame após remoção:")

## função para identificar e ajustar
def check_and_correct_status(df):
    # Define a nova coluna 'expected_status' baseada nas condições dadas
    conditions = [
        (df['frequencia'] < 75),
        (df['frequencia'] >= 75) & (df['nota'] < 50),
        (df['frequencia'] >= 75) & (df['nota'] >= 50)
    ]
    choices = ['R-freq', 'R-nota', 'Aprovado']
    df['expected_status'] = np.select(conditions, choices, default=df['status'])

    print("Etapa 1: condições aplicadas e 'expected_status' definido:")
    print(df[['frequencia', 'nota', 'status', 'expected_status']].head())
    print("\n")
    
    
    # Corrige todos os status discrepantes
    mask = df['status'] != df['expected_status']
    print("Etapa 2: máscara de discrepâncias antes da correção:")
    print(df.loc[mask, ['status', 'expected_status']].head())
    print("\n")
    
    df.loc[mask, 'status'] = df.loc[mask, 'expected_status']

    print("Final: DataFrame após correção de status:")
    print(df[['status', 'expected_status']].head())
    print("\n")

  # Verificação se correções foram aplicadas
    if mask.any():  # Verifica se há algum True na máscara
        print("Foram realizadas correções nos status:")
        print(df.loc[mask, ['status', 'expected_status']])  # Mostra as correções feitas
    else:
        print("Todos os status estão corretos.")   

    # Remover a coluna 'expected_status' após todas as verificações necessárias
    df.drop(columns=['expected_status'], inplace=True)

    return df  # Retorna o DataFrame modificado


## Chamar a função para verificar e corrigir o status
df_limpo = check_and_correct_status(df_limpo)  # Substitua 'df_limpo' pelo nome do seu DataFrame
print(f"Total de registros após limpeza: {df_limpo.shape[0]}")
print("\n")

## DataFrame limpo para analise
print("#--------------------------------------------------------------------")
print("Dataframe limpo para analise:")
print(df_limpo)
print("\n")



# excluindo a coluna 'tipo'
del df_limpo['tipo']
df_limpo

print("\n")
#------------------------------------------------------------------------
# ANALYSE DATA
#------------------------------------------------------------------------
print("#--------------------------------------------------------------------")
print("B. Analisando o dataset")
print("#--------------------------------------------------------------------")

print("\n")
print("#--------------------------------------------------------------------")
print("1. Qual é a média de nota dos aprovados (no período total e por ano)?")

#------------------------------------------------------------------------
# 1.a.0 media de nota dos aprovados NO PERIODO TOTAL

aprovados_notas = df_limpo[df_limpo['status'] == 'Aprovado']['nota']  # Filtra notas dos aprovados
media_total = aprovados_notas.mean()  # Calcula a média de notas dos aprovados
print(f"Média de nota dos aprovados no período total: {media_total:.2f}")



# 1.a.1 Média de nota dos aprovados NO PERÍODO PRE-PANDEMIA, excluindo os anos de 2020 e 2021
aprovados_pre_pandemia = df_limpo[(df_limpo['status'] == 'Aprovado') & (~df_limpo['ano'].isin([2020, 2021]))]['nota']
media_pre_pandemia = aprovados_pre_pandemia.mean()
print(f"Média de nota dos aprovados no período pré-pandemia: {media_pre_pandemia:.2f}")




# 1.a.2 Média de nota dos aprovados NO PERÍODO TOTAL dos anos de 2020 e 2021
aprovados_pandemia = df_limpo[(df_limpo['status'] == 'Aprovado') & (df_limpo['ano'].isin([2020, 2021]))]['nota']
media_pandemia = aprovados_pandemia.mean()
print(f"Média de nota dos aprovados nos anos de 2020 e 2021: {media_pandemia:.2f}")



# 1.b.0 media de nota dos aprovados POR ANO
media_por_ano = df_limpo[df_limpo['status'] == 'Aprovado'].groupby('ano')['nota'].mean()
print("Média de nota dos aprovados por ano:")
print(media_por_ano)


# 1.b.1. media de nota dos aprovados por PERIODO de 2022
# ha dois periodos em 2022 o periodo 1 e o periodo 2   
aprovados_2022 = df_limpo[(df_limpo['status'] == 'Aprovado') & (df_limpo['ano'] == 2022)]
media_2022_por_periodo = aprovados_2022.groupby('periodo')['nota'].mean()
print("Média de nota dos aprovados por período em 2022:")
print(media_2022_por_periodo)



print("\n")
print("#--------------------------------------------------------------------")
#------------------------------------------------------------------------
print("2. Qual é a média de nota dos reprovados por nota (período total e ano)?")

# 2.a.0 média do notas dos reprovados no periodo TOTAL
reprovados_notas_total = df_limpo[df_limpo['status'] == 'R-nota']['nota']
media_reprovados_total = reprovados_notas_total.mean()
print(f"Média de nota dos reprovados por nota no período total: {media_reprovados_total:.2f}")


# 2.a.1 Média de nota dos reprovados NO PERÍODO PRE-PANDEMIA, excluindo os anos de 2020 e 2021
reprovados_pre_pandemia = df_limpo[(df_limpo['status'] == 'R-nota') & (~df_limpo['ano'].isin([2020, 2021]))]['nota']
media_reprovados_pre_pandemia = reprovados_pre_pandemia.mean()
print(f"Média de nota dos reprovados por nota no período pré-pandemia: {media_reprovados_pre_pandemia:.2f}")



# 2.a.2 Média de nota dos reprovados NO PERÍODO TOTAL dos anos de 2020 e 2021
reprovados_pandemia = df_limpo[(df_limpo['status'] == 'R-nota') & (df_limpo['ano'].isin([2020, 2021]))]['nota']
media_reprovados_pandemia = reprovados_pandemia.mean()
print(f"Média de nota dos reprovados por nota nos anos de 2020 e 2021: {media_reprovados_pandemia:.2f}")


# 2.b.0 média de notas dos reprovados POR ANO
media_reprovados_por_ano = df_limpo[df_limpo['status'] == 'R-nota'].groupby('ano')['nota'].mean()
print("Média de notas dos reprovados por ano:")
for year, average in media_reprovados_por_ano.items():
    print(f"{year}: {average:.2f}")


# 2.b.1. media de nota dos aprovados por PERIODO de 2022
reprovados_2022 = df_limpo[(df_limpo['status'] == 'R-nota') & (df_limpo['ano'] == 2022)]
media_reprovados_2022_por_periodo = reprovados_2022.groupby('periodo')['nota'].mean()
print("Média de nota dos reprovados por período em 2022:")
for period, average in media_reprovados_2022_por_periodo.items():
    print(f"Período {period}: {average:.2f}")







print("\n")
print("#--------------------------------------------------------------------")
#------------------------------------------------------------------------
# 3. Qual é a frequência dos reprovados por nota (período total e por ano)?
print("3. Qual é a frequência dos reprovados por nota (período total e por ano)?")

# 3.a. TOTAL
# 1. Filtrar alunos que reprovaram por nota
reprovados_por_nota = df_limpo[df_limpo['status'] == 'R-nota']

# 2. Determinar a média da frequência desses alunos NO TOTAL
media_frequencia_reprovados = reprovados_por_nota['frequencia'].mean()
print(f"A média de frequência dos reprovados por nota é de {media_frequencia_reprovados:.2f}, para todos os períodos")


# 3. POR ANOS - Calcular a média da frequência dos reprovados por nota para cada ano e exibir
media_frequencia_reprovados_por_ano = reprovados_por_nota.groupby('ano')['frequencia'].mean()
print("Média de frequência dos reprovados por nota por ano:")
for ano, media in media_frequencia_reprovados_por_ano.items():
    print(f"Ano {ano}: {media:.2f}")




# GRAFICOS
"""
# 3. Plotar um histograma das frequências dos alunos reprovados por nota
plt.figure(figsize=(10, 6))
plt.hist(reprovados_por_nota['frequencia'], bins=10, color='blue', alpha=0.7)
plt.title('Histograma de Frequência dos Reprovados por Nota')
plt.xlabel('Frequência')
plt.ylabel('Quantidade de Alunos')
plt.grid(True)
plt.show()

# 3.b. POR ANOS
# Filtrar alunos que reprovaram por nota
reprovados_por_nota = df_limpo[df_limpo['status'] == 'R-nota']
# Configurando o gráfico
plt.figure(figsize=(12, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(reprovados_por_nota['ano'].unique())))  # Gerar cores diferentes
# Agrupar por ano e plotar as frequências
for i, (ano, group) in enumerate(reprovados_por_nota.groupby('ano')):
    # Criar um histograma de frequências para cada ano e plotar como linha
    freq_counts, freq_edges = np.histogram(group['frequencia'], bins=10, range=(75, 100))
    freq_centers = (freq_edges[:-1] + freq_edges[1:]) / 2  # Calcular os centros dos bins para plotar como linha
    plt.plot(freq_centers, freq_counts, label=f'Ano {ano}', color=colors[i], marker='o')

plt.title('Distribuição de Frequências dos Reprovados por Nota por Ano (75-100)')
plt.xlabel('Frequência')
plt.ylabel('Quantidade de Alunos')
plt.xlim(75, 100)  # Restringir o eixo X para mostrar apenas frequências entre 75 e 100
plt.legend(title='Ano')
plt.grid(True)
plt.show()
"""


print("\n")
print("#--------------------------------------------------------------------")
#------------------------------------------------------------------------
# 4. Qual a porcentagem de evasões (total e anual)?
print("4. Qual a porcentagem de evasões (total e anual)?")

# 4.a. evasao total
# Calcular o total de 'R-freq' e o total de registros
total_r_freq = df_limpo[df_limpo['status'] == 'R-freq'].shape[0]
total_registros = df_limpo.shape[0]
porcentagem_total_r_freq = (total_r_freq / total_registros) * 100
print(f"Foram considerados como 'evasão' os {total_r_freq:.2f} alunos que reprovaram por frequencia (incluídos aqui aqueles que cancelaram a disciplina).")
print(f"A porcentaem de evasão é de: {porcentagem_total_r_freq:.2f}%")

# 4.b. evasao por anos
# Calcular a porcentagem de 'R-freq' por ano
r_freq_por_ano = df_limpo[df_limpo['status'] == 'R-freq'].groupby('ano').size()
total_por_ano = df_limpo.groupby('ano').size()
porcentagem_r_freq_por_ano = (r_freq_por_ano / total_por_ano) * 100

print("A porcentagem de evasão por ano é de:")
print(porcentagem_r_freq_por_ano)

print("\n")
print("#--------------------------------------------------------------------")
#------------------------------------------------------------------------
# 5. Como os anos de pandemia impactaram no rendimento dos estudantes em relação aos anos anteriores, 
# considerando o rendimento dos aprovados, a taxa de cancelamento e as reprovações? 
# Considere como anos de pandemia os anos de 2020 e 2021.

print(f"5. Como os anos de pandemia impactaram no rendimento dos estudantes em relação aos anos anteriores, considerando o rendimento dos aprovados, a taxa de cancelamento e as reprovações? Considere como anos de pandemia os anos de 2020 e 2021.")
print("\n")

# Definindo os anos de pandemia
anos_pandemia = [2020, 2021]

# 1. Rendimento dos Aprovados: médida de notas dos aprovados
media_notas_aprovados_pandemia = df_limpo[(df_limpo['status'] == 'Aprovado') & (df_limpo['ano'].isin(anos_pandemia))]['nota'].mean()
media_notas_aprovados_pre_pandemia = df_limpo[(df_limpo['status'] == 'Aprovado') & (~df_limpo['ano'].isin(anos_pandemia))]['nota'].mean()

# 2. Taxa de Cancelamento: totais de "R-freq" em relação à todos os alunos
taxa_cancelamento_pandemia = (df_limpo[(df_limpo['status'] == 'R-freq') & (df_limpo['ano'].isin(anos_pandemia))].shape[0] / df_limpo[df_limpo['ano'].isin(anos_pandemia)].shape[0]) * 100
taxa_cancelamento_pre_pandemia = (df_limpo[(df_limpo['status'] == 'R-freq') & (~df_limpo['ano'].isin(anos_pandemia))].shape[0] / df_limpo[~df_limpo['ano'].isin(anos_pandemia)].shape[0]) * 100

# 3. Reprovações: média de notas dos reprovados por nota ('R-nota')
media_notas_reprovacoes_pandemia = df_limpo[(df_limpo['status'] == 'R-nota') & (df_limpo['ano'].isin(anos_pandemia))]['nota'].mean()
media_notas_reprovacoes_pre_pandemia = df_limpo[(df_limpo['status'] == 'R-nota') & (~df_limpo['ano'].isin(anos_pandemia))]['nota'].mean()

# Resultados
print(f"Média de notas dos aprovados antes da pandemia: {media_notas_aprovados_pre_pandemia:.2f}")
print(f"Média de notas dos aprovados durante a pandemia: {media_notas_aprovados_pandemia:.2f}")
print("\n")
print(f"Taxa média de evasão antes da pandemia: {taxa_cancelamento_pre_pandemia:.2f}%")
print(f"Taxa média de evasão durante a pandemia: {taxa_cancelamento_pandemia:.2f}%")
print("\n")
print(f"Média de notas dos reprovados por nota antes da pandemia: {media_notas_reprovacoes_pre_pandemia:.2f}")
print(f"Média de notas dos reprovados por nota durante a pandemia: {media_notas_reprovacoes_pandemia:.2f}")
print("\n")

print(f"Nos anos de pandemia é possível ver que o rendimento dos aprovados teve um incremento de {(media_notas_aprovados_pandemia - media_notas_aprovados_pre_pandemia):.2f}%")
print(f"Já as taxas de evasão, que tinham um histórico de {taxa_cancelamento_pre_pandemia:.2f}%, foram para {taxa_cancelamento_pandemia:.2f}% em 2020/2021, um incremeno de {(taxa_cancelamento_pandemia-taxa_cancelamento_pre_pandemia):.2f}%")
print(f"Por fim, com relação as reprovações, observa-se que a média das notas dos reprovados baixou em {(1-(media_notas_reprovacoes_pandemia/media_notas_reprovacoes_pre_pandemia)):.2f}%.")

print("\n")
print("#--------------------------------------------------------------------")
#------------------------------------------------------------------------
# 6. Compare a volta às aulas híbrida (2022 período 1) com os anos de pandemia e os anos anteriores.

print("6. Compare a volta às aulas híbrida (2022 período 1) com os anos de pandemia e os anos anteriores.")

# Definindo os anos de pandemia e anos pré-pandemia
anos_pandemia = [2020, 2021]
anos_pre_pandemia = df_limpo[df_limpo['ano'] < 2020]['ano'].unique()

# 1. Rendimento dos Aprovados
media_notas_2022_periodo1 = df_limpo[(df_limpo['status'] == 'Aprovado') & (df_limpo['ano'] == 2022) & (df_limpo['periodo'] == '1')]['nota'].mean()
media_notas_pandemia = df_limpo[(df_limpo['status'] == 'Aprovado') & (df_limpo['ano'].isin(anos_pandemia))]['nota'].mean()
media_notas_pre_pandemia = df_limpo[(df_limpo['status'] == 'Aprovado') & (df_limpo['ano'].isin(anos_pre_pandemia))]['nota'].mean()

# 2. Taxa de "R-freq"
taxa_r_freq_2022_periodo1 = (df_limpo[(df_limpo['status'] == 'R-freq') & (df_limpo['ano'] == 2022) & (df_limpo['periodo'] == '1')].shape[0] / df_limpo[(df_limpo['ano'] == 2022) & (df_limpo['periodo'] == '1')].shape[0]) * 100
taxa_r_freq_pandemia = (df_limpo[(df_limpo['status'] == 'R-freq') & (df_limpo['ano'].isin(anos_pandemia))].shape[0] / df_limpo[df_limpo['ano'].isin(anos_pandemia)].shape[0]) * 100
taxa_r_freq_pre_pandemia = (df_limpo[(df_limpo['status'] == 'R-freq') & (df_limpo['ano'].isin(anos_pre_pandemia))].shape[0] / df_limpo[df_limpo['ano'].isin(anos_pre_pandemia)].shape[0]) * 100

# 3. Média de notas dos reprovados por nota ('R-nota')
media_notas_reprovados_2022_periodo1 = df_limpo[(df_limpo['status'] == 'R-nota') & (df_limpo['ano'] == 2022) & (df_limpo['periodo'] == '1')]['nota'].mean()
media_notas_reprovados_pandemia = df_limpo[(df_limpo['status'] == 'R-nota') & (df_limpo['ano'].isin(anos_pandemia))]['nota'].mean()
media_notas_reprovados_pre_pandemia = df_limpo[(df_limpo['status'] == 'R-nota') & (df_limpo['ano'].isin(anos_pre_pandemia))]['nota'].mean()

# Resultados
print("Comparação de Rendimento dos Aprovados, Taxa de 'R-freq' e Média de Notas dos Reprovados:")
print(f"Rendimento dos Aprovados em 2022 (Período 1): {media_notas_2022_periodo1:.2f}")
print(f"Rendimento dos Aprovados durante a pandemia: {media_notas_pandemia:.2f}")
print(f"Rendimento dos Aprovados antes da pandemia: {media_notas_pre_pandemia:.2f}\n")

print(f"Taxa de 'R-freq' em 2022 (Período 1): {taxa_r_freq_2022_periodo1:.2f}%")
print(f"Taxa de 'R-freq' durante a pandemia: {taxa_r_freq_pandemia:.2f}%")
print(f"Taxa de 'R-freq' antes da pandemia: {taxa_r_freq_pre_pandemia:.2f}%\n")

print(f"Média de notas dos reprovados por nota em 2022 (Período 1): {media_notas_reprovados_2022_periodo1:.2f}")
print(f"Média de notas dos reprovados durante a pandemia: {media_notas_reprovados_pandemia:.2f}")
print(f"Média de notas dos reprovados antes da pandemia: {media_notas_reprovados_pre_pandemia:.2f}")


print("\n")
print("#--------------------------------------------------------------------")
#------------------------------------------------------------------------
# 7. Compare a volta às aulas presencial (2022 período 2) com a volta híbrida do item anterior.

print("7. Compare a volta às aulas presencial (2022 período 2) com a volta híbrida do item anterior.")

# 1. Rendimento dos Aprovados
media_notas_aprovados_2022_periodo1 = df_limpo[(df_limpo['status'] == 'Aprovado') & (df_limpo['ano'] == 2022) & (df_limpo['periodo'] == '1')]['nota'].mean()
media_notas_aprovados_2022_periodo2 = df_limpo[(df_limpo['status'] == 'Aprovado') & (df_limpo['ano'] == 2022) & (df_limpo['periodo'] == '2')]['nota'].mean()

# 2. Taxa de 'R-freq'
taxa_r_freq_2022_periodo1 = (df_limpo[(df_limpo['status'] == 'R-freq') & (df_limpo['ano'] == 2022) & (df_limpo['periodo'] == '1')].shape[0] / df_limpo[(df_limpo['ano'] == 2022) & (df_limpo['periodo'] == '1')].shape[0]) * 100
taxa_r_freq_2022_periodo2 = (df_limpo[(df_limpo['status'] == 'R-freq') & (df_limpo['ano'] == 2022) & (df_limpo['periodo'] == '2')].shape[0] / df_limpo[(df_limpo['ano'] == 2022) & (df_limpo['periodo'] == '2')].shape[0]) * 100

# 3. Média de Notas dos Reprovados por Nota
media_notas_reprovados_2022_periodo1 = df_limpo[(df_limpo['status'] == 'R-nota') & (df_limpo['ano'] == 2022) & (df_limpo['periodo'] == '1')]['nota'].mean()
media_notas_reprovados_2022_periodo2 = df_limpo[(df_limpo['status'] == 'R-nota') & (df_limpo['ano'] == 2022) & (df_limpo['periodo'] == '2')]['nota'].mean()

# Resultados
print("Comparação entre a volta às aulas híbrida e presencial em 2022:")
print(f"Rendimento dos Aprovados - Período 1: {media_notas_aprovados_2022_periodo1:.2f}, Período 2: {media_notas_aprovados_2022_periodo2:.2f}")
print(f"Taxa de 'R-freq' - Período 1: {taxa_r_freq_2022_periodo1:.2f}%, Período 2: {taxa_r_freq_2022_periodo2:.2f}%")
print(f"Média de Notas dos Reprovados por Nota - Período 1: {media_notas_reprovados_2022_periodo1:.2f}, Período 2: {media_notas_reprovados_2022_periodo2:.2f}")
