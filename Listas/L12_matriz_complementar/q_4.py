""" Uma análise dos acidentes de trânsito está sendo realizada em Manhattan,
New York. Os cruzamentos das ruas 30 a 38 com as avenidas 1a a 10a foram
estudadas.
Faça um programa para, a partir da informação acima, processar a matriz de
acidentes resultante desse estudo.
Para cada acidente, será informado o local do cruzamento (Avenida x Rua). O
programa deverá ler um número desconhecido de acidentes (utilize qualquer
condição de parada a sua escolha).
Ao final da leitura dos dados, o programa deverá gerar e exibir a matriz de
acidentes (obs: exiba na matriz os cabeçalhos de linha e de coluna mostrando
a identificação das ruas e das avenidas) """
import random

matriz = [[0] * 10 for _ in range(9)]

i = 0
qtd_acidentes = 10
while True:
    if i == qtd_acidentes:
        break

    rua, ave = map(int, input("Digite a rua (30, 38) e a avenida (1, 10): ").split())
    
    if rua not in range(30, 39) or ave not in range(1,11):
        print("Invalido")
        continue

    matriz[rua - 30][ave - 1] += 1
    i += 1


print(" " * 4, end=' ')
for i in range(9):
    print(f"{f'A0{i + 1}':4}", end=' ')
print(f"{'A10':4}")

for i in range(9):
    print(f"R{i + 30}", end=' ')
    for j in range(10):
        print(f"{matriz[i][j]:4}", end=' ')
    print()