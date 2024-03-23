# Criar um dicionario com quantas palavras contem no arquivo
# sistema chave : valor, exemplo, palavras : 12
# (isto é uma forma de "tokenizar" o texto)

# quando a plavra repete, tem que contar uma vez so


arq = "data/texto.txt"
fh = open(arq)
tokens = fh.read().split()

# cria um dicionario vazio
dic2 = {}
# itera para gerar o dicionario
for item in tokens:
    if item in dic2:
        dic2[item] += 1
    else:
        dic2[item] = 1
print(dic2)