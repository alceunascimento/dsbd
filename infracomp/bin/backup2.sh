#!/bin/bash
# salva o conteudo de um diretorio (backup)

data=$(date +%F)             # define a data para YYYY-MM-DD
dir=$1                       # aqui a variavel 'dir' vai ser o primeiro parametro passado

destino=$HOME/backups/
if [ $# != 1 ] ; then        # se o numero de parametros (S#) é diferente de 1 
    echo "Uso: um argumento que e o diretorio a ser salvo"
    exit
fi

if [ ! -d $dir ]; then         # 
    echo "O diretorio $dir não existe"
    exit
fi

if [ -d $destino/$dir-$data ]; then     # se 
    echo "Este diretorio ja foi salvo hoje. Sobrescrever?"
    read resposta
    if [ $resposta != 's' ]; then
        exit
    fi
else
    mkdir -p $destino/$dir-$data
fi

cp -R $dir $destino/$dir-$data
echo "Backup do diretorio $dir completo"

