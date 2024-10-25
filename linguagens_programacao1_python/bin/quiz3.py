

"""
Considere que matrizes estão sendo armazenadas em arquivos .csv, onde o separador é a vírgula.

Cada linha do arquivo representa uma linha da matriz, e as matrizes são sempre quadradas (a quantidade de linhas é a mesma da de colunas).

A seguir é dado um exemplo de conteúdo de um arquivo csv contendo uma matriz de 4x4:

1,2,3,4
5,6,7,8
9,10,11,12
13,14,15,16

Baseado nisso, responda o que o programa a seguir faz:
"""

import csv

path = r"C:\Users\DELL\OneDrive\python\python_projects\dsbd\lingprog\data\matriz.csv"

arq = open(path, "r")
csv_reader = csv.reader(arq, delimiter = ',')
i = 0
for linha in csv_reader:
    print(linha[i])
    i = i + 1
arq.close()


# Ao executar os comandos a seguir, o que será impresso na tela?

frase1 = "laranja laranja"
frase2 = frase1.replace("laranja", "banana", 1)
frase2
frase3 = frase1[0:3] + " " + frase1 + " " + frase2
frase3
print(frase3)


"""
Escreva um programa em Python que use um laço e um teste condicional para contar quantos números pares a variável abaixo possui. 
Depois responda quantos números pares a variável possui.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 8, 2, 4, 5, 4, 9, 9, 12, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 40, 44, 4, 4, 4)
"""

# Tupla de números fornecida
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 8, 2, 4, 5, 4, 9, 9, 12, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 40, 44, 4, 4, 4)

# Variável para contar os números pares
count_pares = 0

# Laço para iterar sobre cada número na tupla
for number in numbers:
    if number % 2 == 0:  # Teste condicional para verificar se o número é par (resto da divisao por 2 igual a 0)
        count_pares += 1  # Incrementa o contador se o número for par

# Exibe o resultado
print("Quantidade de números pares na tupla:", count_pares)



"""
Considere um arquivo chamado exemplo.csv que possui o seguinte conteúdo:
Nome;Idade;Salário
Maria Silva;45;8500,85
José Oliveira;30;5500,4
Marcos Santos;35;8000
Ao executar o programa a seguir, o que é impresso na tela?
"""

import csv

path = r"C:\Users\DELL\OneDrive\python\python_projects\dsbd\lingprog\data\exemplo_quiz.csv"

arq = open(path, "r")
csv_reader = csv.reader(arq, delimiter = ';')
for linha in csv_reader:
    print(linha[1])
    next(csv_reader)
arq.close()


# Considere o seguinte programa em Python e indique qual será o conteúdo do arquivo documento.txt ao final da execução do programa.

path = r"C:\Users\DELL\OneDrive\python\python_projects\dsbd\lingprog\data\documento.txt"

arq = open(path, "a")
arq.write("Olá mundo\n")
arq.write("Cruel\n")
arq.close()

arq = open(path, "w")
arq.write("este é um documento texto")
arq.close()