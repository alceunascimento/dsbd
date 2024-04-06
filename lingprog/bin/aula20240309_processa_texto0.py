import sys

arq_nome = sys.argv[1]
arq_handle = open(arq_nome)
texto = arq_handle.read()

print(texto)
print(type(texto))

arq.close()