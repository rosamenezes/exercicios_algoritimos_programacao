#Exercício 08
print("Notas do Grau A")
nota1A = float(input("Digite o valor da nota da atividade prática: ")) * 0.45
nota2A = float(input("Digite o valor da nota da atividade teórica: ")) * 0.55

print("\nNotas do Grau B")
nota1B = float(input("Digite o valor da nota da atividade em laboratório: ")) * 0.6
nota2B = float(input("Digite o valor da nota da atividade teórica: ")) * 0.2
nota3B = float(input("Digite o valor da nota da atividade extraclasse: ")) * 0.2

notaTotalA = (nota1A + nota2A) * 0.33
notaTotalB = (nota1B + nota2B + nota3B) * 0.67

notaTotalAB = notaTotalA + notaTotalB

print("\n\nA nota final do aluno é " + str(notaTotalAB) + "!")