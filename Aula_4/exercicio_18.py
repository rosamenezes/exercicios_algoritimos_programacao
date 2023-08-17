saldo = float(input("Digite o saldo: "))
saque_deposito = input("1 - Realizar saque: \n2 - Realizar depósito: \n")

valor = 0
if saque_deposito == "1":
    valor = float(input("Digite o valor do saque:      "))
    if valor > saldo:
        print("Operação não permitida")
    else:
        print("Operaçao realizada com sucesso")
if saque_deposito == "2":
    valor = float(input("Digite o valor do depósito: "))
    if saque_deposito == "2" and valor > 300:
        print("Operação não permitida")
    else:
        print("Operaçao realizada com sucesso ")



