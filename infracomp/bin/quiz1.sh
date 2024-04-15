#!/bin/bash

# Define o caminho para o arquivo quiz.txt
# (linux) arquivo_quiz="/home/aenascimento/dsbd/infracomp/data/quiz.txt"
arquivo_quiz="C:\Users\DELL\OneDrive\python\python_projects\dsbd\infracomp\data\quiz.txt"

# a. Mostrar apenas o NOME e o CONCEITO dos alunos
echo "a. Mostrar apenas o NOME e o CONCEITO dos alunos:"
cut -d ',' -f 1,3 "$arquivo_quiz"
# cut: É um comando utilizado para extrair partes específicas de linhas de texto.
# -d ',': Especifica que o delimitador de campos é a vírgula (',').
# -f 1,3: Indica quais campos devem ser extraídos. O campo 1 é o nome do aluno e o campo 3 é o conceito do aluno


# b. Substituir o CONCEITO 'A' por "APROVADO"
echo -e "\nb. Substituir o CONCEITO 'A' por 'APROVADO':"
sed 's/,A,/,APROVADO,/g' "$arquivo_quiz"
# sed: é o comando utilizado para processar texto, permitindo a realização de substituições e outras manipulações.
# 's/,A,/,APROVADO,/g': é uma expressão regular que define a substituição a ser realizada no texto. Aqui, estamos substituindo todas as ocorrências de ",A," por ",APROVADO,".
#    s: indica que é uma substituição.
#    ,A,: é o padrão de busca que corresponde à letra 'A' entre duas vírgulas, indicando o conceito 'A'.
#    ,APROVADO,: é o padrão de substituição que substituirá o conceito 'A' pelo termo 'APROVADO'.
#    g: é uma opção que indica para substituir todas as ocorrências encontradas na linha, não apenas a primeira.

echo

# c. Mostrar apenas as linhas que tenham duas vogais consecutivas
echo -e "\nc. Mostrar apenas linhas que tenham duas vogais consecutivas:"
grep -E '[aeiou]{2}' "$arquivo_quiz"
# grep: é um comando utilizado para buscar padrões em arquivos de texto.
# -E: é uma opção que indica ao grep para usar expressões regulares estendidas.
# [aeiou]{2}: é uma expressão regular que busca por duas vogais consecutivas em uma linha de texto.
#    [aeiou]: especifica um conjunto de caracteres que o grep irá procurar na linha. Neste caso, estamos buscando pelas vogais 'a', 'e', 'i', 'o' e 'u'.
#    {2}: indica ao grep que as vogais especificadas devem ocorrer duas vezes consecutivas na linha


# d. Mostrar os dados ordenados numericamente pela NOTA
echo -e "\nd. Mostrar os dados ordenados numericamente pela NOTA:"
sort -n -t ',' -k2 "$arquivo_quiz"
# sort: Este é o comando utilizado para classificar as linhas de texto em ordem numérica ou alfabética.
# -n: É a opção que indica que a ordenação deve ser feita de forma numérica. 
#      Isso significa que os valores serão interpretados como números ao invés de strings, e serão ordenados de acordo com sua magnitude.
# -t ',': Esta opção especifica o delimitador a ser usado para separar os campos. 
#      Neste caso, a vírgula (,) é definida como o delimitador.
# -k2: Esta opção especifica qual campo deve ser usado como chave para a ordenação. 
#      No comando -k2, 2 indica que a ordenação deve ser feita com base no segundo campo.


# e. Mostrar quantos alunos há na turma
echo -e "\ne. Mostrar quantos alunos há na turma:"
wc -l "$arquivo_quiz"
# wc: word count 
# -l: é uma opção que determina contar as linhas


# f. Mostrar apenas alunos que tenham conceito 'B'
echo -e "\nf. Mostrar apenas alunos que tenham conceito 'B':"
grep ',B,' "$arquivo_quiz"
# grep: é um comando utilizado para buscar padrões em arquivos de texto.
# ',B,' : procura exatamente onde há o texto ,B, 