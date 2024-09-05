"""
Escreva uma função chamada fatorial que receba como parâmetro um número
inteiro e retorne seu fatorial. Faça também um programa para testar a função.
"""

def fatorial(n):
    if n == 0:
        return 1

    return fatorial(n - 1) * n


num = int(input("Digite um número: "))
print(fatorial(num))