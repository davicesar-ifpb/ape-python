""" Escreva um programa que gere aleatoriamente uma matriz quadrada A (cuja ordem
será lida) e gere uma matriz B (da mesma ordem de A), onde cada elemento de B
corresponderá ao respectivo elemento de A somado a ele os seus índices, sendo que se
o elemento for de alguma diagonal (principal ou secundária) deverá ser colocado 0
(zero). """


import random

n = int(input())

matriz_A = [0] * n
matriz_B = [0] * n

# Preencher matriz A com números aleatórios
for i in range(n):
    matriz_A[i] = [random.randint(1,9) for _ in range(n)]

# Preencher matriz B
for i in range(n):
    linha_B = [0] * n
    for j in range(n):
        if (i == j) or ((i + j) == (n - 1)):
            linha_B[j] = 0
            continue

        linha_B[j] = matriz_A[i][j] + i + j
    
    matriz_B[i] = linha_B


# Exibir  matrizes
print("Matriz A")
print(*matriz_A, sep='\n')
print()
print("Matriz B")
print(*matriz_B, sep='\n')
        