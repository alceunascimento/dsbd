import csv

csv_file = open('dsbd_trab1.csv')
csv_reader = csv.reader(csv_file)
for line in csv_reader:
     print(line)
csv_file.close()





