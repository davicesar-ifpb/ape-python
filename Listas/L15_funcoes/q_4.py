"""
Escreva uma função chamada somar que receba como parâmetro um vetor e
retorne a soma dos seus elementos (obs: não use a função sum).
Escreva também um programa que, dado o vetor V = [6, 3, 8, 7, 2, 5] e usando a
função somar criada, imprima a soma dos elementos do vetor V.
"""

def somar(vetor):
    soma = 0
    for i in vetor:
        soma += i
    return soma

v = map(float, input("Me digit eum vetor ai pfv: ").split())

print(somar(v))