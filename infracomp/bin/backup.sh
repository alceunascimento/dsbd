
#!/bin/bash
# salva o conteudo de um diretorio (backup)

data=$(date +%F) # define a data para YYYY-MM-DD
dir=$1
destino=#HOME/backups/

mkdir -p $destino
cp -R $dir $destino/$dir-$data
echo "Backup do diretorio $dir completo"


