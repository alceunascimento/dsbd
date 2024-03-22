import math

# do texto
int("42")
int(3.1415)
float(42)
str(42)

math.sqrt(144)
math.log10(3) # x na base 10
math.log(2) # x na base e
math.log(2, 100) # x na base 100
math.sin(2)
math.pi
math.e

n = 400
result = math.sqrt(n)
print(result)

r = 2
v = 4/3 * math.pi * r ** 3
print(v)
v = 4/3 * math.pi * math.pow(r, 3)
print(v)
v = 4/3 * math.pi * math.pow(r, math.sqrt(9))
print(v)


# EXERCICIOS

# 1. Refaça o exercício da fórmula de Bhaskara da seguinte forma:
# Item a. Com quatro raízes de saída (x1_0 e x2_0, com o resultado real, e x1_1 e x2_1 com resultado arredondado para baixo);
# Item b. Use funções do módulo math, sempre que possível;
# Item c. Calcule o erro resultante do arredondamento.

def calcular_raizes_bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return None, None, None, None, None
    
    x1_0 = (-b + math.sqrt(delta)) / (2*a)
    x2_0 = (-b - math.sqrt(delta)) / (2*a)
    
    x1_1 = math.floor(x1_0)
    x2_1 = math.floor(x2_0)
    
    erro_x1 = abs(x1_0 - x1_1)
    erro_x2 = abs(x2_0 - x2_1)
    
    return x1_0, x2_0, x1_1, x2_1, erro_x1, erro_x2

# Testando a função com a=1, b=-5 e c=6 (equação: x^2 - 5x + 6 = 0)
a = 1
b = -5
c = 6
x1_0, x2_0, x1_1, x2_1, erro_x1, erro_x2 = calcular_raizes_bhaskara(a, b, c)

print("x1_0:", x1_0)
print("x2_0:", x2_0)
print("x1_1:", x1_1)
print("x2_1:", x2_1)
print("Erro x1:", erro_x1)
print("Erro x2:", erro_x2)



# 2. Escreva uma instrução que calcule a raiz cúbica de uma variável “x”.
def f_raiz_cubica(x):
    y = x ** (1/3)
    return y
x = 9
raiz_cubica = f_raiz_cubica(x)
print("A raiz cúbica de", x, "é:", raiz_cubica)

# 3. Qual o resultado da expressão “23+7*50”?
x = 23+7*50
print(x)

# item a. Como obter o resultado 1500 da expressão acima? Escreva essa instrução em Python.
x = (23+7)*50
print(x)

# 4. Como saber se um número é par ou ímpar? Escreva uma instrução que resolva esse problema.
def ver_par_ou_impar(numero):
    # se par é n = 2k, usando o operador resto, encontramos a divisão com resto zero 
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Exemplos de uso da função
print(ver_par_ou_impar(4))


# 5. Escreva uma instrução que calcule a área de um círculo (use função pow())
def f_area_circulo(raio):
    a = math.pi * pow(raio, 2)
    return a

# Exemplo de uso da função
raio = 5
a = f_area_circulo(raio)
print("A área do círculo com raio", raio, "é:", a)