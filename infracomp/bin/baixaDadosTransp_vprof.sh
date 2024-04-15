#!/bin/bash

# Este exemplo baixa os dados dos cinco primeiros dias de um determinado mês e ano 
# que são passados como parâmetros para o script
# Um exemple de execução do script é: ./baixaDadosTransp.sh 05 2015

#set -x
#  Indicando qual o endereço do site - Link Novo
siteDownload="https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/despesas"

#Variáveis indicando o mês e o ano que irá buscar
mes=$1
ano=$2

# Variáveis que indicam os dias do mês da busca
inicioPeriodo=1
fimPeriodo=5

# Diretórios que serão utilizados para baixar os dados e processá-los
dataDir="./dados"
tmpDir="./tmp"

# cria diretório
mkdir $dataDir

# Executa o for para cada dia (inicio e fim) do período
for dia in $(seq -f "%02g" $inicioPeriodo $fimPeriodo); do
  zipFile=$ano$mes$dia'_Despesas.zip'

  # O comando wget vai baixar o arquivo zip com os dados do site 
  echo -n "Baixando arquivo $zipFile ..."
  wget $siteDownload/$zipFile 2> /dev/null
  echo OK

  # Aqui os dados são descompactados no diretório temporário
  echo -n "Descompactando arquivo $zipFile ..."
  unzip -o $zipFile '*ItemEmpenho.csv' -d $tmpDir > /dev/null
  echo OK

  # Arquivo zip é removido
  echo -n "Removendo arquivo $zipFile ..."
  rm -f $zipFile
  echo OK
done

# Dados são copiados do diretório temporário para o diretório dados
cat $tmpDir/*.csv > $dataDir/$ano$mes-ItemEmpenho.csv
# Diretório temporário é apagado
rm -f $tmpDir/*.csv
