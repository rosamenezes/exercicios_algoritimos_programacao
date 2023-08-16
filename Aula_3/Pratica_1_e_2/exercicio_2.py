A = int(input("Digite um número inteiro: "))
B = int(input("Digite um número inteiro: "))
C = int(input("Digite um número inteiro: "))

delta = (B ** 2) - (4 * A * C)
X1 = (-B + delta ** (1 / 2)) / (2 * A)
X2 = (-B - delta ** (1 / 2)) / (2 * A)


if delta < 0:
    print("A equação não possui raízes reais")
else:
    print("{} é a raiz positiva".format(X1))
    print("{} é a raiz negativa".format(X2))