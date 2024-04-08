""" Faça um programa que leia 30 números inteiros, calcule e mostre a soma deles
Obs: não use o comando for, use while. """


soma = 0
i = 0
while i < 30:
    n = int(input())
    soma += n
    i += 1

print(soma)