import math

print("Vamos calcular o perímetro e a área de um círculo, dado o raio")
raio = float(input("informe o raio do círculo: "))
c = 2 * math.pi * raio
a = math.pi * raio ** 2
print("Dado o raio de", raio, "o círculo possui uma circunferência de", c, "e uma área de", a)