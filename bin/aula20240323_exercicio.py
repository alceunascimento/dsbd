# exercicio em sala : tokenizar um texto por dicionario
""" 
Criar um dicionario com quantas palavras contem no arquivo
sistema chave : valor, exemplo, palavras : 12
(isto é uma forma de "tokenizar" o texto)
quando a plavra repete, tem que contar uma vez somente
"""

arq = "data/acordao.txt"
fh = open(arq)
tokens = fh.read().split()

# cria um dicionario vazio
dic2 = {}

# itera para gerar o dicionario
for item in tokens:
    if item in dic2:
        dic2[item] += 1  # leia: se o item está no dicionario adiciona mais um numero para ele
    else:
        dic2[item] = 1 # leia: se o item não esta no dicionario, lança o valor 1
print(dic2)

"""
NOTAS:
A criação do dicionario tem o seguinte racional.
O 'else' lança o elemento pela primeira vez, com o valor de 1.
O 'if' incrementa em 1 o valor lançado pelo 'else', quando o elemento já está no dicionario.

Ou ao contrario:
o 'if' só executa se o elemento já está no dicionario.
Quanto nao está, executa o 'else', incluindo a palavra pela primeira vez e colocando '1'.
Se, iterando, ele acha a mesma palavra, executa o 'if', incrementando a contagem em '+1'.
"""