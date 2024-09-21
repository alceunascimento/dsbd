import os
import pandas as pd
import sqlite3

# Definir o caminho para o arquivo CSV
csv_file = '/home/espinf/aenascimento/Downloads/Microdados do Censo Escolar da Educação Báica 2022/dados/microdados_ed_basica_2022.csv'

# Verificar se o arquivo CSV existe
if not os.path.exists(csv_file):
    print(f"Erro: O arquivo {csv_file} não foi encontrado.")
    exit(1)  # Sai do programa com código de erro


# Ler o arquivo CSV usando pandas
df = pd.read_csv(csv_file, usecols=[
    'CO_ENTIDADE', 'NO_ENTIDADE', 'DS_ENDERECO', 'NU_ENDERECO',
    'DS_COMPLEMENTO', 'NO_BAIRRO', 'CO_MUNICIPIO', 'TP_LOCALIZACAO_DIFERENCIADA'
])

# Conectar ao banco de dados SQLite
db_path = 'dsbd.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Certificar que a tabela existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS escola (
    codigo INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    cod_municipio INTEGER NOT NULL,
    endereco TEXT NULL,
    compl_endereco TEXT NULL,
    bairro TEXT NULL,
    cod_loc_dif INT NULL,
    FOREIGN KEY (cod_municipio) REFERENCES municipio(codigo),
    FOREIGN KEY (cod_loc_dif) REFERENCES localizacao_dif(codigo)
)
''')

# Função para inserir os dados
def inserir_dados():
    for index, row in df.iterrows():
        # Preparar a consulta SQL para inserção
        cursor.execute('''
        INSERT OR IGNORE INTO escola (codigo, nome, cod_municipio, endereco, compl_endereco, bairro)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            row['CO_ENTIDADE'],
            row['NO_ENTIDADE'],
            row['CO_MUNICIPIO'],
            f"{row['DS_ENDERECO']}, {row['NU_ENDERECO']}",
            row['DS_COMPLEMENTO'],
            row['NO_BAIRRO']
        ))

# Inserir os dados na tabela 'escola'
inserir_dados()

# Confirmar as mudanças e fechar a conexão
conn.commit()
conn.close()
