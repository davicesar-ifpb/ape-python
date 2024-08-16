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

matriz = [0] * 9

for i in range(9):
    rua = [0] * 10
    for j in range(10):
        #rua[j] = int(input(f"Acidentes no cruzamento da rua {i + 30} com a avenida {j + 1}: "))
        rua[j] = random.randint(1,9)
        
    matriz[i] = rua

rua_label = '||RUAS|||'

print(f"{'AVENIDAS':_^22}")
for i in range(9):
    print(rua_label[i], end=' ')
    for j in range(10):
        
        print(matriz[i][j], end=' ')
    print()