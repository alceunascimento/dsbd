#!/bin/bash
# Uso: ./plotar2.sh grafico.csv
# O nome do arquivo é passado como argumento na chamada do script ($1).

gnuplot -persist <<-EOFMaker
	plot "$1" using 1:2 with lines title "TREINOP", "$1" using 1:3 with lines title "VAL"
EOFMaker
