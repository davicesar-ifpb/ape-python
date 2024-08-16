""" Escreva um programa que:
• Leia uma matriz quadrada de ordem 30 contendo números inteiros;
• Gere e imprima um vetor que deverá conter os elementos da diagonal principal da matriz;
• Gere e imprima um vetor que deverá conter os elementos da diagonal secundária da matriz. """

import random

ordem = 30
matriz = [0] * ordem

diagonal_principal = []
diagonal_secundaria = []

for i in range(ordem):
    matriz[i] = [random.randint(1,9) for _ in range(ordem)]

for l in range(2):
    for i in range(ordem):
        for j in range(ordem):
            if (i == j) and l == 0:
                print(matriz[i][j], end=' ')
                diagonal_principal.append(matriz[i][j])
                continue

            if ((i + j) == (ordem - 1)) and l == 1:
                print(matriz[i][j], end=' ')
                diagonal_secundaria.append(matriz[i][j])
                continue
            
            print(".", end=' ')
        print()
    print()
                

print("Diagonal principal")      
print(diagonal_principal)
print("\nDiagonal secundaria")      
print(diagonal_secundaria)
print("\nMatriz original")
print(*matriz, sep='\n')