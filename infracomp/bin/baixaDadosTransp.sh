#!/bin/bash

# script em BASH que baixa dados do Portal da Tranparência 
# Seleciona um período determinado, extrai estes dados em arquivos de interesse e os agrupa em um único arquivo .csv
# O script recebe 4 (quatro) parâmetros, invocados da seguinte forma:

# `baixaDadosTransp diaIni diaFim mes ano` , onde:
#     `baixaDadosTransp` é o nome do script
#     `diaIni` é o dia inicial a ser baixado
#     `diaFim` é o dia final a ser baixado
#     `mes` é o mes dos dados requeridos
#     `ano` é o ano dos dados requeridos

# exemplo: ./baixaDadosTransp.sh 1 10 01 2020

# Atribui os parâmetros a variáveis locais
diaIni=$1
diaFim=$2
mes=$3
ano=$4

# Website contendo os dados
website="https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/despesas"

# Diretórios de trabalho
## nota: o script esta na pasta bin e os diretorios sao criados no nivel acima "../"
tmpDir="../tmp"
dataDir="../data"

# Cria o diretório temporário se não existir
mkdir -p $tmpDir
# Cria o diretório de dados se não existir
mkdir -p $dataDir

# Loop para baixar os arquivos por cada dia especificado
for dia in $(seq -f "%02g" $diaIni $diaFim); do
  zipFile=$ano$mes$dia'_Despesas.zip'

  # Baixa o arquivo ZIP
  echo -n "Baixando arquivo $zipFile ..."
  wget $website/$zipFile 2> /dev/null
  echo OK

  # Descompacta o arquivo no diretório temporário
  echo -n "Descompactando arquivo $zipFile ..."
  unzip -o $zipFile '*Empenho.csv' -d $tmpDir > /dev/null
  unzip -o $zipFile '*Pagamento.csv' -d $tmpDir > /dev/null
  # Remove arquivos indesejados que incluem "ItemEmpenho" no nome
  rm -f $tmpDir/*ItemEmpenho.csv
  echo OK

  # Remove o arquivo ZIP
  echo -n "Removendo arquivo $zipFile ..."
  rm -f $zipFile
  echo OK
done


# Consolida todos os CSVs de Empenho extraídos em um único arquivo, removendo cabeçalhos
echo -n "Consolidando arquivos de Empenho CSV..."
for file in $tmpDir/*Empenho.csv; do
    # Pula a primeira linha de cada arquivo e adiciona a um arquivo temporario
    tail -n +2 $file >> $tmpDir/consolidado_empenho.tmp
done

# Adiciona o cabeçalho do primeiro arquivo ao arquivo a ser consolidado no final
head -n 1 $(ls $tmpDir/*Empenho.csv | head -n 1) > $dataDir/${ano}${mes}${diaIni}-${diaFim}_Despesas_Empenho.csv

# Adiciona os dados concatenando o arquivo temporario no arquivo final
cat $tmpDir/consolidado_empenho.tmp >> $dataDir/${ano}${mes}${diaIni}-${diaFim}_Despesas_Empenho.csv
rm $tmpDir/consolidado_empenho.tmp
echo "OK"


# Consolida todos os CSVs de Pagamento extraídos em um único arquivo, removendo cabeçalhos
echo -n "Consolidando arquivos de Pagamento CSV..."
for file in $tmpDir/*Pagamento.csv; do
    # Pula a primeira linha de cada arquivo e adiciona a um arquivo temporario
    tail -n +2 $file >> $tmpDir/consolidado_pagamento.tmp
done

# Adiciona o cabeçalho do primeiro arquivo ao arquivo a ser consolidado no final
head -n 1 $(ls $tmpDir/*Pagamento.csv | head -n 1) > $dataDir/${ano}${mes}${diaIni}-${diaFim}_Despesas_Pagamento.csv

# Adiciona os dados concatenando o arquivo temporario no arquivo final
cat $tmpDir/consolidado_pagamento.tmp >> $dataDir/${ano}${mes}${diaIni}-${diaFim}_Despesas_Pagamento.csv
rm $tmpDir/consolidado_pagamento.tmp
echo "OK"


# Remove os arquivos CSV temporários
echo -n "Limpando diretório temporário..."
rm -f $tmpDir/*.csv
echo "OK"
