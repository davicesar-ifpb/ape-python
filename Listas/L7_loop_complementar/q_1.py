""" Faça um programa que leia um número N, calcule e mostre os N primeiros
termos da sequência de Fibonacci (0, 1, 1, 2, 3, 5, 8, 13, ...). O valor lido para
N sempre será maior ou igual a 2. """


def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        print(a, end=', ')    
        a,b = b,a+b


n = int(input("Valor de N: "))
fibonacci(n)