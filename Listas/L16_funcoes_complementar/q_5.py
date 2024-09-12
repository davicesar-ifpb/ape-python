"""
5. Faça um programa que leia duas matrizes de inteiros e gere uma terceira matriz que
corresponderá a soma das duas matrizes lidas. A ordem das matrizes também será lida.
O programa deverá conter as seguintes funções:
• Uma função para gerar e ler uma matriz, sendo passados como parâmetros a ordem da
matriz.
• Uma função para exibir uma matriz em sua representação clássica (linhas e colunas).
• Uma função para somar duas matrizes.
"""

def ler_matriz(ordem):
    matriz = [
        [float(x) for x in input(f"Linha {i}: ").split()]
        for i in range(ordem)
    ]
    return matriz

def somar_matrizes(m1, m2):
    ordem = len(m1)
    matriz_somada = [0] * ordem

    for i in range(ordem):
        linha = [0] * ordem
        for j in range(ordem):
            linha[j] = m1[i][j] + m2[i][j]
        matriz_somada[i] = linha

    return matriz_somada

def printar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(matriz[i][j], end=' ')
        print()


# Programa
ordem = int(input("Digite a ordem das matrizes: "))
print("Matriz 1:")
matriz_1 = ler_matriz(ordem)
print("Matriz 2:")
matriz_2 = ler_matriz(ordem)
print("Matriz 1:")
printar_matriz(matriz_1)
print("Matriz 2:")
printar_matriz(matriz_2)
matriz_somada = somar_matrizes(matriz_1, matriz_2)
print("Matriz Somada:")
printar_matriz(matriz_somada)