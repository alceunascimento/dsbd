import csv

# deste jeito o arquivo fecha depois de sair do suite de forma automatica
# os dados ficam na memoria dentro do dataframe (como lista)

df = []
with open('dsbd_trab1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        df.append(row)    
print(df)
