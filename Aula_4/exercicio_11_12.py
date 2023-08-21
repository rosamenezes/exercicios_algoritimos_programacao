produto = str(input("Digite o nome do produto: "))
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))
total = preco * quantidade

if quantidade >= 3 and quantidade <= 4: 
    total = total - (total * 0.1)
if quantidade >= 5 and quantidade <= 10:
    total = total - (total * 0.15)
if quantidade > 10:
    total = total - (total * 0.2)
else:
    total = total

print("O valor total da compra é: R${:.2f}".format(total))