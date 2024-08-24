import sqlite3

# SET DB ---------------------------------
# Conectar ao banco de dados (ou criar um se não existir)
conn = sqlite3.connect('dsbd.db')
cursor = conn.cursor()

# SET TABLES ---------------------------------
# Criar a tabela 'estado' se ela não existir
cursor.execute('''
CREATE TABLE estado(
    uf TEXT PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
)
''')

# Criar a tabela 'municipio' se ela não existir
cursor.execute('''
CREATE TABLE municipio (
    codigo INT		  PRIMARY KEY,
    nome 	 TEXT NOT NULL,
    uf	 TEXT	  NOT NULL,
    FOREIGN KEY (uf) REFERENCES estado(uf)
''')


# INSERT DATA ---------------------------------

# Dados dos municípios para inserir
municipio = [
    ('São Paulo', 'SP', 3550308),
    ('Rio de Janeiro', 'RJ', 3304557),
    ('Belo Horizonte', 'MG', 3106200),
    ('Porto Alegre', 'RS', 4314902),
    ('Recife', 'PE', 2611606)
]

# Inserir dados na tabela
cursor.executemany('''
INSERT INTO municipio (nome, uf, codigo)
VALUES (?, ?, ?)
''', municipio)

# Confirmar a inserção e fechar a conexão
conn.commit()
conn.close()

print("Dados inseridos com sucesso no banco de dados 'dsbd.db'.")
