import sqlite3

# SET DB ---------------------------------
# Conectar ao banco de dados (ou criar um se não existir)
conn = sqlite3.connect('dsbd.db')
cursor = conn.cursor()


# SET TABLES ---------------------------------
# Criar a tabela 'estado' se ela não existir
cursor.execute('''
DROP TABLE IF EXISTS escola;
''')

cursor.execute('''
CREATE TABLE escola (
    co_entidade INT PRIMARY KEY,
    no_entidade TEXT NOT NULL,
    co_municipio INT NOT NULL,
    ds_endereco TEXT NULL,
    ds_complemento TEXT NULL,
    no_bairro TEXT NULL,
    FOREIGN KEY (co_municipio) REFERENCES municipio(codigo)
)
''')

# INSERT DATA ---------------------------------
cursor.execute('''
INSERT INTO escola (co_entidade, no_entidade, co_municipio, ds_endereco, ds_complemento, no_bairro)
VALUES (53084071, 'ESC DIVINO MESTRE', 5300108, 'QUADRA QNP 21 CONJUNTO H', NULL,'CEILANDIA NORTE')
''')


# QUERY ---------------------
#SELECT * FROM escola WHERE bairro IS NULL;
#SELECT * FROM escola WHERE bairro IS NULL;
#SELECT COUNT(*) FROM ESCOLA WHERE endereco IS NULL;
#SELECT COUNT(*) FROM ESCOLA WHERE endereco IS NULL AND bairro IS NULL AND compl_endereco IS NULL;
#SELECT * FROM escola WHERE bairro IS NOT NULL;
#SELECT COUNT(*) FROM ESCOLA WHERE endereco IS NOT NULL;
#SELECT COUNT(*) FROM ESCOLA
#WHERE endereco IS NOT NULL OR bairro IS NOT NULL OR compl_endereco IS NOT NULL;

