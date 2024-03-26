import math

# Função para calcular as raízes da equação de segundo grau
def calcular_raizes(a, b, c):
    # Verifica se é uma equação de segundo grau
    if a == 0:
        return None
    
    # Calcula o discriminante
    delta = b**2 - 4*a*c
    
    # Verifica se há raízes reais
    if delta > 0:
        # Duas raízes reais distintas
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        # Apenas uma raiz real
        x = -b / (2*a)
        return x, None
    else:
        # Não há raízes reais
        return None, None

# Função principal
def main():
    # Entrada dos coeficientes a, b e c
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))

    # Calcula as raízes
    raiz1, raiz2 = calcular_raizes(a, b, c)

    # Verifica se houveram raízes reais
    if raiz1 is not None:
        if raiz2 is not None:
            # Exibe as duas raízes
            print("As raízes da equação são:", raiz1, "e", raiz2)
        else:
            # Exibe apenas uma raiz
            print("A equação possui apenas uma raiz real:", raiz1)
    else:
        # Não há raízes reais
        print("A equação não possui raízes reais.")

# Chama a função principal
if __name__ == "__main__":
    main()
