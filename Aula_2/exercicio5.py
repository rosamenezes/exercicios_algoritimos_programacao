#Exercício 05

numeros = []
soma = 0
multiplicacao = 1

for i in range(0, 5):
  numeros.append(int(input(f"Digite o {i+1}º valor: ")))
  multiplicacao = multiplicacao * numeros[i]

soma = sum(numeros)

print("\n\nA soma de todos os números é " + str(soma) + '.')
print("O produto de todos os números é " + str(multiplicacao) + '.')
