# LISTAS e TUPLES


lista1 = ['Uma string qualquer', 234]
lista1

lista2 = [1,56,8756]
lista2

# lista dentro de lista
lista2.append(lista1)
lista2

lista2[3]
lista2[3][1]
lista2[-1]

lista2.append(56)
lista2
lista2.count(56)
lista2.index(56)

lista2
lista2.pop()
lista2
lista2.pop(0)
lista2



# 

lista_compras = ['maça','leite','arroz','frango','macarrão']
sublista = lista_compras[1:4]
sublista

qty_vezes = lista_compras.count('maça')
qty_vezes


lista_compras.sort()
for item in lista_compras:
    print(item)


# TUPLES
    
tupla_compras = ('maçãs', 'leite', 'arroz', 'frango', 'trigo')
for item in tupla_compras:
    print(item)

print("O item 1 é", tupla_compras[1])

# DICIONARIOS

dic1 = {}
len(dic1)

dic1["a"] = ""
dic1
dic1["d"] = "segundo valor"
dic1
dic1["a"] = lista1
dic1
dic1["a"]
dic1["a"][0]


arq = "/data/texto.txt"
fh = open(arq)
fh
fh.read()
fh.readline()
fh.seek(0)
fh.readline()

arq = "/data/texto.txt"
fh = open(arq)
fh
fh.read().splitlines()
fh.seek(0)
fh.read().split()
fh.read()


