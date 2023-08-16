def calcular_operacao(opcao, num_a, num_b):
    if opcao == 1:
        return num_a + num_b
    elif opcao == 2:
        return num_a - num_b
    elif opcao == 3:
        return num_a * num_b
    elif opcao == 4:
        if num_b == 0:
            return "Não é possível dividir por zero!"
        return num_a / num_b
    elif opcao == 5:
        return num_a ** num_b
    elif opcao == 6:
        if num_b == 0:
            return "Não é possível calcular a radiciação com um expoente zero!"
        return num_a ** (1 / num_b)
    else:
        return "Você digitou uma opção inválida!"

opcao = int(input("Digite o número da operação desejada: "))
num_a = int(input("Digite o número A: "))
num_b = int(input("Digite o número B: "))

resultado = calcular_operacao(opcao, num_a, num_b)
print(resultado)

