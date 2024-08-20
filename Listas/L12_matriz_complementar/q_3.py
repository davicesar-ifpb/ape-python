""" Escreva um programa que preencha uma matriz quadrada de ordem 3 com
valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente),
calcule e exiba:
• A soma dos elementos de cada linha;
• A soma dos elementos de cada coluna;
• A soma dos elementos da diagonal principal da matriz;
• A soma dos elementos da diagonal secundária da matriz;
• A soma de todos os elementos da matriz. """

import random

ordem = 3

matriz = [
    [random.randint(1,9) for _ in range(ordem)]
    for _ in range(ordem)
]
    
soma_linhas = [0] * ordem
soma_colunas = [0] * ordem
soma_diag_p = 0
soma_diag_s = 0
soma_total = 0

for i in range(ordem):
    soma_linhas[i] = sum(matriz[i])
    coluna = [i] * ordem
    for j in range(ordem):
        soma_total += matriz[i][j]
        coluna[j] = matriz[j][i]
        
        if i == j:
            soma_diag_p += matriz[i][j]
            
        if (i + j) == (ordem - 1):
            soma_diag_s += matriz[i][j]
        
        soma_total += matriz[i][j]
    
    soma_colunas[i] = sum(coluna)    

print("Matriz")
print(*matriz, sep='\n')
print()
print("Soma linhas")
print(soma_linhas)
print("\nSoma colunas")
print(soma_colunas)
print("\nSoma diagonal principal")
print(soma_diag_p)
print("\nSoma diagonal secundaria")
print(soma_diag_s)
print("\nSoma total")
print(soma_total)