import csv
import os

# Criar um ambiente virtual e ativar
os.system('python3 -m venv venv')
print('Para ativar o ambiente virtual, execute: source venv/bin/activate')

# Carregar o arquivo CSV original
input_file = '/home/espinf/aenascimento/Downloads/Microdados do Censo Escolar da Educação Báica 2022/dados/microdados_ed_basica_2022.csv'
output_file = 'microdados_ed_basica_2022_amostra_1000.csv'

try:
    # Ler o arquivo CSV manualmente e armazenar as primeiras 1.000 linhas
    with open(input_file, 'r', encoding='utf-8', errors='replace') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        rows = [header]
        for i, row in enumerate(reader):
            if i < 1000:
                rows.append(row)
            else:
                break

    # Salvar as primeiras 1.000 linhas em um novo arquivo CSV
    with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

    print(f"Novo arquivo CSV com 1.000 linhas salvo como '{output_file}'")
except FileNotFoundError:
    print(f"Erro: O arquivo '{input_file}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")