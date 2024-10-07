
Quiz PBD Aula 5 - Paulo
Iniciado em	sexta-feira, 4 out. 2024, 20:36
Estado	Finalizada
Concluída em	sexta-feira, 4 out. 2024, 20:42
Tempo empregado	6 minutos 5 segundos
Avaliar	75,00 de um máximo de 100,00


Questão 1
Correto
Atingiu 25,00 de 25,00
Marcar questão
Texto da questão

Ao executar o seguinte programa em Python, o que acontece?


import sqlite3

con = sqlite3.connect("dsbd.db")



cursor = con.cursor()

cursor.execute("INSERT INTO estado (uf, nome, regiao) VALUES ('BB', 'TesteB', 'NORTE')")

con.rollback()

con.close()

Questão 1 Resposta
a.

Um estado de nome TesteB é inserido no banco.
b.

A tabela estado não é alterada.
c.

Um estado de nome TesteB é inserido no banco, mas isso ocorre apenas se esse estado já não existisse no banco.
Feedback

Sua resposta está correta.
A resposta correta é: A tabela estado não é alterada.



Questão 2
Correto
Atingiu 25,00 de 25,00
Marcar questão
Texto da questão

Considere o trecho Python a seguir, e indique o que deve ser usado para substituir o ??? no código.

import sqlite3

con = sqlite3.connect("dsbd.db")



cursor = con.cursor()

cursor.execute("SELECT nome FROM escola WHERE codigo = 11024275")

resultado = cursor.???()



# Aqui faz o processamento do resultado



con.close()

Questão 2 Resposta
a.

fetchNome
b.

fetchall
c.

fetchone
d.

fetchPrimaryKey
e.

nome
Feedback

Sua resposta está correta.
A resposta correta é: fetchone



Questão 3
Incorreto
Atingiu 0,00 de 25,00
Marcar questão
Texto da questão

Considere o trecho Python a seguir, e indique o que deve ser usado para substituir o ??? no código.

import sqlite3

con = sqlite3.connect("dsbd.db")



cursor = con.cursor()



cursor.execute("SELECT codigo FROM escola WHERE nome = 'EIEEF HAP BITT TUPARI'")



resultado = cursor.???()



# Aqui faz o processamento do resultado



con.close()

Questão 3 Resposta
a.

fetchPrimaryKey
b.

fetchall
c.

fetchone
d.

nome
e.

fetchNome
Feedback

Sua resposta está incorreta.
A resposta correta é: fetchall



Questão 4
Correto
Atingiu 25,00 de 25,00
Marcar questão
Texto da questão

Considere que precisamos escrever um programa em que o usuário digita o código completo de uma escola, e o nome e endereço da escola são exibidos na tela.

Depois disso, o programa termina.

Marque a alternativa que contém uma versão correta desse programa.
Questão 4 Resposta
a.

import sqlite3

con = sqlite3.connect("dsbd.db")



codigo = input("Digite o codigo da escola: ")

codigo = int(codigo)



cursor = con.cursor()

cursor.execute("SELECT nome, endereco FROM escola WHERE codigo = ?", (codigo,))

resultado = cursor.fetchone()



if resultado is not None:

 print(resultado)

else:

 print("Escola não encontrada.")



con.close()

b.

import sqlite3

con = sqlite3.connect("dsbd.db")



codigo = input("Digite o codigo da escola: ")



cursor = con.cursor()

cursor.execute("SELECT nome, endereco FROM escola WHERE codigo = " + codigo)

resultado = cursor.fetchall()



if len(resultado) > 0:

 print(resultado)

else:

 print("Escola não encontrada.")



con.close()

c.

import sqlite3

con = sqlite3.connect("dsbd.db")



codigo = input("Digite o codigo da escola: ")



cursor = con.cursor()

cursor.execute("SELECT nome, endereco FROM escola WHERE codigo = " + codigo)

resultado = cursor.fetchone()



if resultado is not None:

 print(resultado)

else:

 print("Escola não encontrada.")



con.close()

d.

import sqlite3

con = sqlite3.connect("dsbd.db")



codigo = input("Digite o codigo da escola: ")



cursor = con.cursor()

cursor.execute("SELECT nome, endereco FROM escola WHERE codigo = codigo")

resultado = cursor.fetchone()



if resultado is not None:

 print(resultado)

else:

 print("Escola não encontrada.")



con.close()

Feedback

Sua resposta está correta.
A resposta correta é:

import sqlite3

con = sqlite3.connect("dsbd.db")



codigo = input("Digite o codigo da escola: ")

codigo = int(codigo)



cursor = con.cursor()

cursor.execute("SELECT nome, endereco FROM escola WHERE codigo = ?", (codigo,))

resultado = cursor.fetchone()



if resultado is not None:

 print(resultado)

else:

 print("Escola não encontrada.")



con.close()

