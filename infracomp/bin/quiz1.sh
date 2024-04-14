#!/bin/bash

# Define o caminho para o arquivo quiz.txt
arquivo_quiz="/home/aenascimento/dsbd/infracomp/data/quiz.txt"

# a. Mostrar apenas o NOME e o CONCEITO dos alunos
echo "a. Mostrar apenas o NOME e o CONCEITO dos alunos:"
cut -d ',' -f 1,3 "$arquivo_quiz"

# b. Substituir o CONCEITO 'A' por "APROVADO"
echo -e "\nb. Substituir o CONCEITO 'A' por 'APROVADO':"
sed 's/,A,/,APROVADO,/g' "$arquivo_quiz"


# c. Mostrar apenas as linhas que tenham duas vogais consecutivas
echo -e "\nc. Mostrar apenas linhas que tenham duas vogais consecutivas:"
grep -E '[aeiou]{2}' "$arquivo_quiz"

# d. Mostrar os dados ordenados numericamente pela NOTA
echo -e "\nd. Mostrar os dados ordenados numericamente pela NOTA:"
sort -n -t ',' -k2 "$arquivo_quiz"





# e. Mostrar quantos alunos há na turma
echo -e "\ne. Mostrar quantos alunos há na turma:"
wc -l "$arquivo_quiz"

# f. Mostrar apenas alunos que tenham conceito 'B'
echo -e "\nf. Mostrar apenas alunos que tenham conceito 'B':"
grep ',B,' "$arquivo_quiz"
