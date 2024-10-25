"""
Trabalho 2 (extra)
Aplique os conhecimentos aprendidos no curso. 
Agora vamos obter informações sobre o desempenho geral de estudantes do curso de computação. 
O dataset do arquivo historico-alg1_SIE_ANONIMIZADO.csv contém a situação de 424 estudantes entre 2011 e 2020 em várias disciplinas. 
Cada estudante é representado por um número inteiro na primeira coluna (MATR_ALUNO).
Analise o dataset e responda as seguintes perguntas:
1. Quais as top 5 disciplinas que mais geram cancelamentos por parte dos estudantes ao longo dos anos (plote a resposta em um gráfico);
2. Quais as top 5 disciplinas que possuem aprovações em geral?
3. Quais disciplinas possuem taxa de aprovação maior que 70% durante o todo o período?
4. Quais disciplinas possuem taxa de reprovação maior que 70% a cada vez que são oferecidas (ex.: DiscXYZ teve 75% de reprovação em 2012; DiscABC teve 99% de reprovação em 2019, etc.)?
5. Das disciplinas com reprovações, qual o máximo de vezes que um estudante teve que se matricular, excluindo cancelamentos, para ser aprovado?
6. Como evoluem as taxas aprovados/reprovados nas disciplinas ao longo do tempo?
Atenção: algumas matérias (códigos) "deixam" de existir, enquanto outras "surgem", pois houve modificação curricular no período abrangido pelo dataset.

"""

print("UFPR")
print("Data Science Big Data")
print("Linguagens de Programação")
print("Trabalho EXTRA - Usar : dataset3")
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
dir()


#------------------------------------------------------------------------
# GET DATA
#------------------------------------------------------------------------

# Caminho do arquivo CSV
# path =  "/home/aenascimento/dsbd/lingprog/data/dataset3.csv"  # rodar em casa
path = "/home/espinf/aenascimento/dsbd/lingprog/data/dataset3.csv"  # rodar na UFPR
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
print("------------------------------------------------------------------")
print("B. Organizando os dados:")       
print("------------------------------------------------------------------")



#------------------------------------------------------------------------
# ANALIZE DATA
#------------------------------------------------------------------------
print("------------------------------------------------------------------")
print("C. Analisando os dados:")       
print("------------------------------------------------------------------")
print("Analise o dataset e responda as seguintes perguntas:")
print("1. Quais as top 5 disciplinas que mais geram cancelamentos por parte dos estudantes ao longo dos anos (plote a resposta em um gráfico);")
print("2. Quais as top 5 disciplinas que possuem aprovações em geral?")
print("3. Quais disciplinas possuem taxa de aprovação maior que 70% durante o todo o período?")
print("4. Quais disciplinas possuem taxa de reprovação maior que 70% a cada vez que são oferecidas (ex.: DiscXYZ teve 75% de reprovação em 2012; DiscABC teve 99% de reprovação em 2019, etc.)?")
print("5. Das disciplinas com reprovações, qual o máximo de vezes que um estudante teve que se matricular, excluindo cancelamentos, para ser aprovado?")
print("6. Como evoluem as taxas aprovados/reprovados nas disciplinas ao longo do tempo?")