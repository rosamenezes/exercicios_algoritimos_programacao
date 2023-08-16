def vogalOuConsoante(letra):
    vogais = "aeiouAEIOU"
    if letra in vogais:
        return "Essa letra é uma vogal"
    else:
        return "Essa letra é uma consoante"

letra = input("Digite uma letra: ")
resultado = vogalOuConsoante(letra)
print(resultado)