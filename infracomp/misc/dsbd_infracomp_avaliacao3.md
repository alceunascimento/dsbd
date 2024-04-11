# Avaliação 3
Condições de conclusão
Aberto: sexta-feira, 5 abr. 2024, 00:00
Vencimento: segunda-feira, 29 abr. 2024, 23:59

# BASH script

Escreva um script em BASH que baixe dados do portal da tranparência 
[link](http://portaldatransparencia.gov.br/download-de-dados/despesas) 
de um período pré-determinado, extraia destes dados arquivos de interesse e os agrupe em um único arquivo .csv

O script deve receber 4 (quatro) parâmetros e ser invocado da seguinte forma:

* `baixaDadosTransp diaIni diaFim mes ano` , onde:
    * `baixaDadosTransp` é o nome do script
    * `diaIni` é o dia inicial a ser baixado
    * `diaFim` é o dia final a ser baixado
    * `mes` é o mes dos dados requeridos
    * `ano` é o ano dos dados requeridos

* O nome dos arquivos a serem baixados possui o formato: "AAAAMMDD.zip" onde:
    * AAAA é o ano com 4 dígitos
    * MM é o mês com 2 dígitos
    * DD é o dia com 2 dígitos

* De cada arquivo de dados baixado (.zip) você deve extrair os arquivos:
    * AAAAMMDD_Despesas_Empenho.csv
    * AAAAMMDD_Despesas_Pagamento.csv

* O resultado final do script deve produzir DOIS arquivos:
    * AAAAMMdiaIni-diaFim_Despesas_Empenho.csv contendo a concatenação de todos os arquivos de "Empenho" baixados
    * AAAAMMdiaIni-diaFim_Despesas_Pagamento.csv contendo a concatenação de todos os arquivos de "Pagamento" baixados

Os arquivos resultantes NÃO devem repetir a linha de cabeçalho do seu conteúdo, ou seja, a primeira linha de todos .csv com excessão do primeiro deve ser removida antes da concatenação.

# Dicas
Resolva esta avaliação utilizando o exemplo discutido em sala de aula e disponível no aqui.
Soluções parciais serão consideradas proporcionalmente.
Nomeie as variáveis de forma que seja fácil entender o que elas representam (não esqueça que eu tenho que corrigir o script...)