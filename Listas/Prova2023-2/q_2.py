""" Escreva um programa que:
• Leia uma matriz M de ordem 20 x 50 contendo valores inteiros;
• Leia um valor inteiro K;
• Imprima todas as posições (linha e coluna) em que se encontra o valor K dentro da matriz M. """

import random

matriz = [0] * 20

for i in range(20):
    matriz[i] = [random.randint(1,50) for _ in range(50)]

k = int(input("Digite um número inteiro: "))

posicoes = []

print("\nPosicoes na matriz")
for i in range(20):
    for j in range(50):
        if matriz[i][j] == k:
            print(matriz[i][j], end=' ')
            posicoes.append((i, j))
            continue
        
        print(".", end=' ')
    print()
        

print("\nIndices do número encontrado na matriz")   
print(posicoes)

        