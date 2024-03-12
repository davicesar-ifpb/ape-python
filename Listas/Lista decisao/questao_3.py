num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))
num3 = float(input("Digite o número 3: "))


if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num3:
    print(num2)
else:
    print(num3)


lista = []
for i in range(1,4):
    num = float(input(f"Digite o número {i}: "))
    lista.append(num)
lista.sort()
print(lista[-1])