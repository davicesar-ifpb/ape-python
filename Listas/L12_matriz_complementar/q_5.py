""" A distância entre várias cidades é dada pela tabela abaixo (em km).
Cidade 1  2  3  4  5 
     1 -  15 30 5  12
     2 15 -  10 17 28
     3 30 10 -  3  11
     4 5  17 3  -  80
     5 12 28 11 80 -
Faça um programa que:
• Armazene estas informações em uma matriz;
• Mostre a distância percorrida para um determinado percurso (informado
pelo usuário).
Exemplo: Dado o percurso 1, 2, 3, 2, 5, 1, 4, a distância percorrida é
15+10+10+28+12+5 = 80km. """

matriz = [
    [0, 15, 13, 5, 12],
    [15, 0, 10, 17, 28],
    [30, 10, 0, 3, 11],
    [5, 17, 3, 0, 80],
    [12, 28, 11, 80, 0]
]

percurso = list(map(int, input().split()))
distancia = 0

for i in range(len(percurso) - 1):
    distancia += matriz[percurso[i] - 1][percurso[i + 1] - 1]

print(distancia)