""" Faça um programa que leia vários números, calcule e exiba a média desses
números.
Obs: a leitura do número 999 indica o fim dos dados de entrada e não deve ser
computado na média) """


soma = 0
i = 0
while True:
    n = int(input())

    if n == 999: break

    soma += n
    i += 1


print(f"{soma/i:.1f}")

    