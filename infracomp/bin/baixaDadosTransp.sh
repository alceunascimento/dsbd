#!/bin/bash

#!/bin/bash

# Função para verificar se a quantidade de parâmetros está correta
if [ "$#" -ne 4 ]; then
    echo "Uso: $0 diaIni diaFim mes ano"
    exit 1
fi

# Recebendo os parâmetros
diaIni=$1
diaFim=$2
mes=$3
ano=$4

# Formatação de mês e ano para garantir o formato correto
formattedMonth=$(printf "%02d" $mes)
formattedYear=$(printf "%04d" $ano)

# Criação dos diretórios para armazenar os dados temporários e finais
mkdir -p ./data
mkdir -p ./extracted
mkdir -p ./output

# Loop para baixar os dados de cada dia dentro do intervalo especificado
for (( dia=$diaIni; dia<=$diaFim; dia++ ))
do
    formattedDay=$(printf "%02d" $dia)
    fileName="${formattedYear}${formattedMonth}${formattedDay}"
    zipFile="${fileName}.zip"
    url="http://portaldatransparencia.gov.br/download-de-dados/despesas/${zipFile}"

    # Download do arquivo
    wget -q $url -O "./data/$zipFile"

    # Verifica se o arquivo foi baixado e então extrai os arquivos específicos
    if [ -f "./data/$zipFile" ]; then
        unzip -q "./data/$zipFile" "${fileName}_Despesas_Empenho.csv" "${fileName}_Despesas_Pagamento.csv" -d ./extracted
    fi
done

# Função para concatenar os arquivos, evitando cabeçalhos repetidos
concat_files() {
    outputFile="./output/${formattedYear}${formattedMonth}${diaIni}-${diaFim}_Despesas_$1.csv"
    first=1
    for file in ./extracted/*_$1.csv; do
        if [ "$first" -eq 1 ]; then
            # Copia o arquivo inteiro se for o primeiro (inclui cabeçalho)
            cat $file > $outputFile
            first=0
        else
            # Para outros arquivos, pula o cabeçalho
            tail -n +2 $file >> $outputFile
        fi
    done
}

# Concatenação dos arquivos de Empenho e Pagamento
concat_files "Empenho"
concat_files "Pagamento"

# Limpeza dos arquivos temporários
rm -r ./data
rm -r ./extracted

echo "Arquivos processados e salvos em ./output"
