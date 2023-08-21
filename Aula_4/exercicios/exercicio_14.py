nome = str(input("Insira seu nome: "))
peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso")
if imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
if imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
if imc >= 30 and imc <= 34.9:
    print("Obesidade grau 1")
if imc >= 35 and imc <= 39.9:
    print("Obesidade grau 2")
if imc > 40:
    print("Obesidade grau 3")