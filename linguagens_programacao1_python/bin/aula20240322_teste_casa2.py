import re

def corrigir_arquivo_csv(arquivo_entrada, arquivo_saida):
    # Define um padrão regex para encontrar vírgulas que NÃO sejam seguidas pelos indicadores especificados
    # Usamos uma negative lookahead assertion para esse propósito.
    regex_padrao = r',(?!(date|srcIP|srcPort|dstIP|dstPort|protocol|IDSID|SignatureGroup|Classification))'

    with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
        for linha in entrada:
            # Substitui as vírgulas encontradas pelo padrão regex por ponto e vírgula
            linha_corrigida = re.sub(regex_padrao, ';', linha)
            # Escreve a linha corrigida no arquivo de saída
            saida.write(linha_corrigida)

# Exemplo de uso
corrigir_arquivo_csv('dsbd_trab1.csv', 'dsbd_trab1_corrigida.csv')


# NOTAS sobre o REGEX:
# O r antes da string indica que ela é uma string bruta (raw string) em Python. 
# Quando você usa o prefixo r, o Python não processa caracteres de escape dentro da string. 
# Isso é particularmente útil em expressões regulares, onde os caracteres de escape são comuns (como \b, \d, etc.), 
# porque você não precisa duplicá-los. 
# Por exemplo, em uma string regular Python, você precisaria escrever "\\d" para representar um dígito, 
# mas em uma string bruta, você pode simplesmente escrever r"\d".

# O ?! faz parte de uma construção chamada *negative lookahead*. 
#Em expressões regulares, um lookahead é uma asserção que verifica se o que segue a posição atual corresponde a um 
# determinado padrão, sem consumir qualquer parte da string (ou seja, sem avançar através da string durante a busca). 
# O negative lookahead especificamente verifica se o que segue não corresponde ao padrão especificado dentro dos 
# parênteses (?!...). No seu caso, , seguido de um negative lookahead significa "encontre uma vírgula que não seja 
# seguida por qualquer uma das palavras especificadas". Então, a expressão regular vai combinar com vírgulas que 
# não sejam seguidas diretamente por date, srcIP, srcPort, dstIP, dstPort, protocol, IDSID, SignatureGroup, ou 
# Classification, permitindo que você substitua essas vírgulas específicas por ponto e vírgula, enquanto mantém 
# as vírgulas que fazem parte da estrutura esperada do seu arquivo CSV