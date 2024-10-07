import sqlite3

con = sqlite3.connect("dsbd04.db")
cursor = con.cursor()

# INSERT DATA
#cursor.execute("INSERT INTO estado (uf, nome, regiao) VALUES ('AB', 'TESTEB', 'NORTE')")
#con.commit()


# QUERY

## Query para um resultado "fetchone"
cursor.execute(
"""
SELECT 
    codigo, nome, uf 
FROM 
    municipio 
WHERE 
    codigo = 4106902
"""
)
resultado = cursor.fetchone()
print(type(resultado), 
      type(resultado[0]), 
      type(resultado[1]), 
      type(resultado[2]))
print(resultado)


# Query para varios resultados "fetchall"
cursor.execute("SELECT uf, nome FROM estado ORDER BY uf")
resultado = cursor.fetchall()
print(type(resultado))
for tupla in resultado:
    print(tupla)



cursor.execute("SELECT codigo, nome, uf FROM municipio WHERE codigo = 5300108")
resultado = cursor.fetchone()
if (resultado is None):
    print("Não há resultados")
else:
    print(resultado)



# QUERY PARAMETRIZADA

uf = input("Digite uma UF: ")
nome_cidade = input("Digite um nome de cidade para buscar: ")
cursor.execute("SELECT codigo, nome, uf FROM municipio WHERE UPPER(nome) = UPPER(?) AND UPPER(uf) = UPPER(?)", (nome_cidade,uf))
resultado = cursor.fetchone()
if resultado is not None:
    print(resultado)
else:
    print("Cidade não encontrada.")


con.close()
