""" Escreva um programa que preencha uma matriz 3x5 com valores inteiros fornecidos
pelo usuário (ou gerados aleatoriamente) e gere a sua transposta. Ao final, imprima as
duas matrizes (no formato de matriz). """


import random

matriz = [0] * 3
matriz_transposta = [0] * 5


# Preencher matriz
for i in range(3):
    matriz[i] = [random.randint(1,9) for _ in range(5)]

# Transpor matriz e preencher matriz transposta
for i in range(5):
    linha_transposta = [0] * 3
    for j in range(3):
        linha_transposta[j] = matriz[j][i]

    matriz_transposta[i] = linha_transposta


# Exibir matrizes
print(*matriz, sep='\n')
print()
print(*matriz_transposta, sep='\n')
