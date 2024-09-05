"""
Escreva uma função chamada identidade que receba como parâmetro uma
matriz quadrada e retorne True se ela for uma matriz identidade, ou False caso
contrário.
Obs: Matriz identidade é uma matriz quadrada em que os elementos da diagonal
principal são iguais a 1 e os demais elementos são iguais a 0.
Escreva também um programa que leia uma matriz 3x3 de inteiros e diga se ela
é ou não uma matriz identidade (usando a função identidade criada).
"""

def isMatrizIdentidade(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0 and i != j:
                return False
            
            if i == j and matriz[i][j] != 1:
                return False
    
    return True


ordem = int(input("Digite a ordem da matriz: "))

matriz = [list(map(float, input().split())) for _ in range(ordem)]

print(isMatrizIdentidade(matriz))