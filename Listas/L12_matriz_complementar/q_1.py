""" Uma matriz de permutação é uma matriz quadrada cujos elementos são 0's
ou 1's, tal que em cada linha e em cada coluna exista apenas um elemento
igual a 1. Por exemplo, a matriz seguinte é uma matriz de permutação.
1 0 0
0 1 0
0 0 1
Com base na definição apresentada, escreva um programa que preencha uma
matriz quadrada com valores fornecidos pelo usuário, determine e mostre se
ela é uma matriz de permutação. """

ordem = 3

matriz = [0] * ordem

for i in range(ordem):
    matriz[i] = list(map(int, input(f"Linha {i}: ").split()))

matriz_perm = True
for i in range(ordem):
    qtd_1_por_linha = 0
    qtd_1_por_coluna = 0
    
    for j in range(ordem):
        if matriz[i][j] not in [0, 1]:
            matriz_perm = False
            break
        
        if matriz[i][j] == 1:
            qtd_1_por_linha += 1
        
        if matriz[j][i] == 1:
            qtd_1_por_coluna += 1

    if qtd_1_por_linha > 1 or qtd_1_por_linha == 0:
        matriz_perm = False
        
    if qtd_1_por_coluna == 0 or qtd_1_por_coluna > 1:
        matriz_perm = False
        
    if not matriz_perm:
        break

if matriz_perm:
    print("\nÉ uma matriz permutação")
else:
    print("\nNão é uma matriz permutação")
    
    