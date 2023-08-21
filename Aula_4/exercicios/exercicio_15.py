a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))
c = int(input("Insira o terceiro número: "))\

if a == b and a == c:
    if a < b + c or b < a + c or c < b + a:
        print("Triangulo equilatero")
    else:
        print("Não é um triangulo")
if a != b and a != c and b != c:
    if a < b + c or b < a + c or c < b + a:
        print("Triangulo escaleno")
    else:
        print("Não é um triangulo")
if a == b and a != c or a == c and a != b or b == c and b != a:
    if a < b + c or b < a + c or c < b + a:
        print("Triangulo isosceles")
    else:
        print("Não é um triangulo")
