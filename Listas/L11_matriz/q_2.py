""" Escreva um programa que:
• Leia (ou gere aleatoriamente) uma matriz quadrada de ordem N contendo elementos
inteiros (N será lido);
• Exiba a matriz lida (no formato de matriz);
• Exiba os elementos da diagonal principal, isto é, os elementos onde I = J. """


import random

n = int(input())

matriz = [0] * n

# Preencher matriz com numeros aleatorios
for i in range(n):
    matriz[i] = [random.randint(1,9) for _ in  range(n)]

# Exibir matriz
print(*matriz, sep="\n")

print()

# Exibir itens da diagonal principal
for i in range(n):
    for j in range(n):
        if i == j:
            print(matriz[i][j], end=' ')
            continue

        print(".", end=' ')
    print()