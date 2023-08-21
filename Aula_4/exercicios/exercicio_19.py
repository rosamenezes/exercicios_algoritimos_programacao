
jogador1 = input("Nome do jogador 1: ")
jogador2 = input("Nome do jogador 2: ")

jogada1 = input(f"{jogador1}, escolha sua jogada: pedra, papel, tesoura, lagarto ou Spock: ")
jogada2 = input(f"{jogador2}, escolha sua jogada: pedra, papel, tesoura, lagarto ou Spock: ")

vencedor = None

if jogada1 == jogada2:
    resultado = "Empate!"
elif (
    (jogada1 == "pedra" and (jogada2 == "tesoura" or jogada2 == "lagarto")) or
    (jogada1 == "tesoura" and (jogada2 == "papel" or jogada2 == "lagarto")) or
    (jogada1 == "papel" and (jogada2 == "pedra" or jogada2 == "Spock")) or
    (jogada1 == "lagarto" and (jogada2 == "papel" or jogada2 == "Spock")) or
    (jogada1 == "Spock" and (jogada2 == "tesoura" or jogada2 == "pedra"))
):
    vencedor = jogador1
else:
    vencedor = jogador2

if vencedor:
    print(f"O jogador vencedor é: {vencedor}")
else:
    print("jogada inválida.")