#par ou impar
nome_1 = input("Digite seu nome jogador 1: ")
nome_2 = input("Digite seu nome jogador 2: ")

par_impar = input("Escolha par ou impar {}: ".format(nome_1))

numero_1 = int(input("Digite um numero {}: ".format(nome_1)))
numero_2 = int(input("Digite um numero {}: ".format(nome_2)))

if par_impar == "par":
    if (numero_1 + numero_2) % 2 == 0:
        print(nome_1 + " ganhou!")
    else:
        print(nome_2 + " ganhou!")
if par_impar == "impar":
    if (numero_1 + numero_2) % 2 != 0:
        print(nome_1 + " ganhou!")
    else:
        print(nome_2 + " ganhou!")