""" Faça um programa que leia um número inteiro e determine se ele é par ou
ímpar. Ao final, o programa deve perguntar se o usuário deseja continuar
(digitar outro número) ou sair. Se o usuário quiser continuar, o programa deve
repetir tudo de novo, caso contrário o programa deve ser encerrado. """


while True:
    n = int(input())

    if n & 1:
        print(f"O número {n} é impar")
    else:
        print(f"O número {n} é par")

    continuar = input("Continuar? (s/n): ")

    if continuar.lower() == "n": break


    