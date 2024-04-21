
# Questão 1

import numpy as np
import matplotlib.pyplot as plt

# Definindo a função f(x) = x^2 + 2
def f(x):
    return x**2 + 2

# Gerando valores de x para plotar
x_values = np.linspace(-10, 10, 400)
y_values = f(x_values)

# Criando o gráfico
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label="f(x) = x^2 + 2", color='blue')
plt.title("Gráfico da função f(x) = x^2 + 2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()


# Questao 2
import sympy as sp

# Definindo a variável simbólica
x = sp.symbols('x')

# Definindo a função
y = sp.exp(3*x)

# Calculando a primeira derivada
y_prime = sp.diff(y, x)

# Calculando a segunda derivada
y_double_prime = sp.diff(y_prime, x)

# Avaliando as derivadas no ponto x = 2
y_prime_at_2 = y_prime.subs(x, 2).evalf()
y_double_prime_at_2 = y_double_prime.subs(x, 2).evalf()

y_prime_at_2, y_double_prime_at_2


# Questao 5

import sympy as sp

# Definir a variável simbólica x
x = sp.symbols('x')

# Definir a função a ser integrada
f = x**(-1)

# Calcular a integral definida de 2 a 4
integral_result = sp.integrate(f, (x, 2, 4))

# Avaliar o resultado com uma casa decimal
integral_result_evaluated = round(integral_result.evalf(), 1)

integral_result_evaluated

# Questao 14

# Importar o pacote SymPy
import sympy as sp


# Definir as variáveis simbólicas
x, y = sp.symbols('x y')

# Definir a função
f = 120*x - 2.25*x**2 - 4*x*y - 2.4*y**2 + 200*y

# Calcular as derivadas parciais de primeira ordem
fx = sp.diff(f, x)
fy = sp.diff(f, y)

# Calcular as derivadas parciais de segunda ordem (matriz Hessiana)
fxx = sp.diff(fx, x)
fxy = sp.diff(fx, y)
fyy = sp.diff(fy, y)

# Determinar o ponto crítico (sistema de equações)
sistema_eq = sp.solve([fx, fy], (x, y))

# Avaliar a matriz Hessiana no ponto crítico
hessiana = sp.Matrix([[fxx, fxy], [fxy, fyy]])
hessiana_ponto_critico = hessiana.subs({x: sistema_eq[x], y: sistema_eq[y]})

# Determinar a natureza do ponto crítico (máximo, mínimo ou sela)
if hessiana_ponto_critico.det() > 0:
    if fxx.subs({x: sistema_eq[x], y: sistema_eq[y]}) > 0:
        print("O ponto crítico é um ponto de mínimo.")
    else:
        print("O ponto crítico é um ponto de máximo.")
elif hessiana_ponto_critico.det() < 0:
    print("O ponto crítico é um ponto de sela.")
else:
    print("A natureza do ponto crítico não pode ser determinada com este método.")

# Exibir o ponto crítico
print("O ponto crítico é (x =", sistema_eq[x], ", y =", sistema_eq[y], ")")


# Questao 25

from sympy import symbols, exp, diff


# Define the variables
x, y = symbols('x y')

# Define the function u
u = exp(2*x**2 + 3*y)

# Calculate first partial derivative with respect to x
u_x = diff(u, x)

# Calculate second partial derivative with respect to x
u_xx = diff(u_x, x)
u_x, u_xx
