num_a = int(input("Digite o número A: "))
num_b = int(input("Digite o número B: "))
num_c = int(input("Digite o número C: "))

if num_a < num_b and num_a < num_c:
    print("O número A é o menor.")
elif num_b < num_a and num_b < num_c:
    print("O número B é o menor.")
else:
    print("O número C é o menor.")