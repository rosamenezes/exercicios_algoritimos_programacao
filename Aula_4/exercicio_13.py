usuario = str(input("Digite o nome do usuário: "))
senha = input("Digite a senha do usuário: ")

if senha == usuario + "9876":
    print("Acesso concedido")
else:
    print("Acesso negado")