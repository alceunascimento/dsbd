import sys

texto = open(sys.argv[1]).read().splitlines()

print(texto)
print(type(texto))

arq.close()