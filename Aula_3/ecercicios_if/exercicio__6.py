def calcularTaxaDeJuros(preco):
    if preco < 100:
        return preco + preco * 0.1
    if preco < 300:
        return preco + preco * 0.2
    if preco < 1000:
        return preco + preco * 0.5
    else:
        return "Preço inválido"

preco = int(input("Insira o preço do produto: "))
resultado = calcularTaxaDeJuros(preco)
print(resultado)
