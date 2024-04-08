""" Faça um programa que leia um número inteiro N, calcule e mostre o maior
quadrado perfeito menor ou igual a N. Por exemplo, se N for igual a 38, o
resultado é 36. """


n = int(input())

quadrados_perfeito = []
for i in range(1,n+1):
    quadrado = i ** (1/2)
    if i == int(quadrado) ** 2:
        quadrados_perfeito.append(i)
print(quadrados_perfeito[-1])