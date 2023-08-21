idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Responda às perguntas a seguir:")
    
    acertos = 0
    
    resposta1 = input("1 - Ao prestar socorro à vítima de um acidente, NÃO se deve:\n"
    "a) acionar imediatamente o Corpo de Bombeiros\n"
    "b) dar água, comida ou qualquer substância para a vítima cheirar\n"
    "c) conversar com a vítima para saber de suas condições gerais\n"
    "d) deixar a vítima confortável até a chegada do socorro especializado\n"
    "Resposta: ")

    if resposta1 == "b":
        acertos += 1

    resposta2 = input("\n2 - Ao se deparar com uma sinaleira na cor vermelha, você deve:\n"
    "a) rir dela\n"
    "b) passar mais rápido, pois é perigoso parar\n"
    "c) dobrar a direita, pois vermelho indica direita\n"
    "d) parar\n"
    "Resposta: ")

    if resposta2 == "d":
        acertos += 1

    resposta3 = input("\n3 - Segundo a direção defensiva, quando você está em uma via e um pedestre vai atravessar você:\n"
    "a) buzina muito forte para que o pedestre se assuste\n"
    "b) atropela o pedestre, pois lugar de pedestre é na calçada\n"
    "c) para e dá uma carona para o pedestre, pois é uma lei de trânsito\n"
    "d) para e aguarda ele atravessar\n"
    "Resposta: ")

    if resposta3 == "d":
        acertos += 1

    if acertos >= 2:
        print("\nParabéns! Você está apto para tirar a carteira de motorista.")
    else:
        print("\nVocê não está apto para tirar a carteira de motorista.")

else:
    print("Você não tem idade suficiente para tirar a carteira de motorista.")
