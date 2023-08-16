import math

X1 = int(input("Digite o valor de X1: "))
X2 = int(input("Digite o valor de X2: "))
X3 = int(input("Digite o valor de X3: "))
u = (X1 + X2 + X3)/3
n = 3

desvio_padrao = math.sqrt((X1 - u)**2 + (X2 - u)**2 + (X3 - u)**2)/n

print("O desvio padrão é: ", desvio_padrao)

## 50 40 10 ----- 