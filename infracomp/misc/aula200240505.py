
mod = 10 % 6
print(mod)


# chaves cripto
"""
dois primos grandes
p = 
q = 

n = p*q

Do "n" apura-se o "z":
z = (p-1)(q-1)

Escolhe-se um "e" menor que n, os dois não possuem fatores comuns, exceto 1.
escolher o "e" como se fosse outro primo

Do "z" e do "e" apura-se o "d":
e*d-1 mod z = 0
e*d mod z = 1


chaves sao 

publica (n,e)
privada (n,d)

Cifrar: c = m^e mod n
Descifrar: m = c^d mod n
"""

p = 5
q = 7
n = p*q
n
z = (p-1)*(q-1)
z

e = 5  # (primo)
e
# 0 = e*d % z  # descobrir como calcular o d com a manipulação algébrica
# d = 1 - 

# d


# CIFRANDO
# mensagem é "3"
m1 = 3
# chave publica é 35,5
n = 35
e = 5
c = (m**e) % n
c

# DESCIFRANDO
# chave privada é 35,29
d = 29

m2 = c**d % n
m2

m2 == m1


# Exercicios
M = (20,5,15,17)
n = 35
e = 5
d = 29

c1 = M[0]**e % n
c1

f 

primo = 2**1024 # primo minimo
primo


 

