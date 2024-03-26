
# basico
print("Olá")
print("um", "tres")

# Condicionais basicos
# Definindo uma variável
idade = 20
# Verificando a idade e imprimindo uma mensagem dependendo do valor
if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 60:
    print("Você é adulto.")
else:
    print("Você é idoso.")

# Lacos basicos
# Imprimindo os números de 0 a 4
for i in range(5):
    print(i)

# Imprimindo os números de 1 a 10, de 2 em 2
for i in range(1, 11, 2):
    print(i)

# Notas: o range é numero inteiro, de 1 em 1 comeca em zero.
# tres argumentos, inicial, final (exclusivo) e passo

while True:
    resposta = input("Digite 's' para sair: ")
    if resposta.lower() == 's':
        break

