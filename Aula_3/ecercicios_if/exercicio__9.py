def calculoGrauC(notaA, notaB):
    if ((notaA * 0.33) + (notaB * 0.67)) >= 6:
        return "Aprovado"
    else:
        return "Sera nessesario fazer Grau C"

notaA = float(input("Digite a nota do Grau A: "))
notaB = float(input("Digite a nota do Grau B: "))
resultado = calculoGrauC(notaA, notaB)
print(resultado)