"""
def funcao(lista):
       fim = len(lista)-1
       inicio = 0
       while(inicio < fim):
               aux = lista[inicio]
               lista[inicio] = lista[fim]
               lista[fim] = aux
               inicio = inicio + 1
               fim = fim - 1
               

# Criação correta de uma lista
minha_lista = ['arroz', 'banana', 'cão']
minha_lista
# Chamando a função com a lista correta
funcao(minha_lista)
print(minha_lista)



if(aparelho == 'tv'):
     if(marca == 'sony'):
         if(tamanho == 48):
             print('Equipamento:', aparelho, marca, tamanho)
         else: 
             tamanho = 50
     elif(marca == 'samsung'):
             print('Equipamento:', aparelho, marca, tamanho)
     else:
             print('Equipamento:', aparelho, marca, tamanho)



lista = [1,2,58,10,19,30,58,100]
lista
lista.remove(58)
lista
del lista[1]
lista
lista.append(-3)
lista
lista.insert(2, 77)
lista
lista.insert(2, 77)
lista
print(lista)


carro = 'honda'
not (carro == 'honda'  or  carro == 'toyota')
(carro == 'honda'  or  carro == 'toyota')
(carro == 'honda'  and  carro == 'toyota')
not (carro == 'honda'  and  carro == 'toyota')

carro = 'honda'
cor = 'prata'
(carro == 'honda'  or  carro == 'toyota') and (cor == 'prata')


def minha_funcao(valor):
        if(valor == 1):
                return valor + 1;   
        valor = valor + 10
        return valor + 20

minha_funcao(2)


a = 1
resultado = minha_funcao(a)
print(resultado)
"""



idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Pode dirigir no Brasil...")
if idade < 18:
    print("Não pode dirigir no Brasil!")
if idade > 15:
    print("Pode dirigir nos EUA...")
if idade >= 16 and idade < 21:
    print("Pode dirigir, mas não comprar álcool nos EUA")
    


# Considerando as funções a seguir e suas chamadas, indique o que será impresso na tela.

def funcao(a, b):
        a = a + 1
        b[1] = a
    
def imprimir(lista):
        for item in lista:
                #o end = seguido de duas aspas simples serve para não pular de linha
                print(item, ' ', end= '')
        print()

var = 10
lista = [1,2,3]
funcao(var, lista)

print(var)

imprimir(lista)


for num in range(10):
    if (num%2 == 0):
        print(num)
        

n = 2
for i in range(10):
    produto = n*i
    print(produto)
    
i = 0
while i <= 10:
    print(i)
    i += 1
    
    
for i in range(10):
    print(i)
    
    

objetos = ["cadeira", "mesa", "vaso"]
objetos
objetos.remove("cadeira")
objetos
objetos.append("caneta")
objetos
del objetos[0]
objetos