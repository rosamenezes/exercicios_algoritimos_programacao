ano = int(input("Digite o ano entre 0 e 2022: "))
mes = int(input("Digite o mês entre 1 e 12: "))
dia = int(input("Digite o dia entre 1 e 31: "))

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
data_valida = False

if 0 <= ano <= 2022:
    if 1 <= mes <= 12:
        if mes == 2:
            if bissexto:
                if 1 <= dia <= 29:
                    data_valida = True
            else:
                if 1 <= dia <= 28:
                    data_valida = True
        elif mes in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= dia <= 31:
                data_valida = True
        else:
            if 1 <= dia <= 30:
                data_valida = True

if data_valida:
    print("A data informada é válida.")
else:
    print("A data informada é inválida.")
