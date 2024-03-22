import math

# Dado que um retangulo tem 63 de area e 7 de um lado
A = 63
a = 7
print("Dado que um retangulo tem", A, "de área e", a, "de lado.")

# Item a. Calcular o valor do lado b
b = A / a
print("O valor do lado b é:", b)

# Item b. Calcular a diagonal do retangulo
def calcular_diagonal_retangulo(a, b):
    d = math.sqrt(a**2 + b**2)
    return d
# Atribuir o valor da diagonal à variável diagonal
d = calcular_diagonal_retangulo(a, b)
print("O valor da diagonal do retangulo é", d)

# Item c. Definir uma função para a area e diagonal
def calcular_area_e_diagonal_retangulo(a, b):
    area = a * b
    diagonal = math.sqrt(a**2 + b**2)
    return area, diagonal
a = int(input("Insira a medida de um dos lados do regtangulo: "))
b = int(input("Insira a medida do outro lado do retangulo: "))
area, diagonal = calcular_area_e_diagonal_retangulo(a, b)
print("Área:", area)
print("Diagonal:", diagonal)
