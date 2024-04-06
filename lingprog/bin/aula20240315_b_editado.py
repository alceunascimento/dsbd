import csv
import re

# caminho do arquivo
caminho = 'dsbd_trab2.csv'

# abrir o arquivo para leitura
with open(caminho, 'r', encoding='utf=8') as arquivo:
    # ler o conteudo do arquivo
    conteudo = arquivo.read()
    
    # user REGEX para substituir ",_" por "_"
    conteudo_edit = re.sub(r',_',';_',conteudo)

# sobreescrever o arquivo com o conteudo corrigido
with open(caminho, 'w', encoding='utf-8') as arquivo:
    arquivo.write(conteudo_edit)
