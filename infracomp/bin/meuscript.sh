#!/bin/bash
# 
# Comentarios

echo "Arquivos no diretorio HOME"
ls $HOME


var="Hello World"  # atribuição de variavel SEM ESPAÇO
echo $var


data=$(date)
echo "Hoje e dia $data"
echo "Meu nome e $0 e recebi $# parametros"
echo "Os parametros são $*"




# cria a variavel 'fotos'
fotos=$ls(./2023)


# troca o nome do arquivo
# o 'f' é de 'file name', pode ser qualquer coisa, 
for f in $fotos; do cp $f ${f/messi/Messi}; done

                                                                  
# CRIAR UM SCRIPT para executar os comandos


data=$(date +%F)
dir=$1
destino