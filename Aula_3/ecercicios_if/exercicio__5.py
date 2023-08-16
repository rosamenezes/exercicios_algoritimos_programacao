price = int(input("Insira o preço do produto: "))

if price <= 0:
    print("Preço inválido")
elif price > 0 and price <= 30:
    print("Preço baixo")
elif price > 30 and price <= 50:
    print("Preço médio")
else:
    print("Preço alto")