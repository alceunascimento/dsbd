#!/usr/bin/gnuplot -persist
# Uso: ./plotar.sh
# O nome do arquivo que será plotado (grafico.csv) tem seu nome fixo no script

plot 'grafico.csv' using 1:2 with lines title 'TREINOP', 'grafico.csv' using 1:3 with lines title 'VAL',
