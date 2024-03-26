import sys

texto = open(sys.argv[1]).readlines()
linhas = texto.split("\n")

print(linhas)
print(type(linhas))

arq.close()