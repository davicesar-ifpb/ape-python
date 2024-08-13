import random

matriz = [0] * 3

for i in range(3):
    linha = [0] * 4
    for j in range(4):
        linha[j] = random.randint(0,20)
    matriz[i] = linha

print(*matriz, sep="\n")