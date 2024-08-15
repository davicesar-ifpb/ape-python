""" 
Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3, com
valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente). O programa
deverá somar as duas matrizes, armazenando o resultado em uma terceira matriz (C).
Ao final, exiba as 3 matrizes (no formato de matriz).
"""


import random

matriz_A = [0] * 2
matriz_B = [0] * 2
matriz_C = [0] * 2

# Preencher matriz A
for i in range(2):
    matriz_A[i] = [random.randint(1,9) for _ in range(3)]

# Preencher matriz B
for i in range(2):
    matriz_B[i] = [random.randint(1,9) for _ in range(3)]

# Preencher matriz C
for i in range(2):
    linha_c = [0] * 3
    for j in range(3):
        linha_c[j] = matriz_A[i][j] + matriz_B[i][j]
    matriz_C[i] = linha_c


# Exibir matrizes
print("Matriz A")
print(*matriz_A, sep='\n')


print("\nMatriz B")
print(*matriz_B, sep='\n')


print("\nMatriz C")
print(*matriz_C, sep='\n')
