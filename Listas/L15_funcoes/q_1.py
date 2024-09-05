"""
Escreva uma função chamada menor que receba como parâmetros 3 números e
retorne o menor deles. Faça também um programa para testar a função.
"""

def menor(a, b, c):
    if a < b and a < c:
        return a
    
    if  b < c:
        return b
    
    return c


numeros = list(map(float, input("Digite 3 numeros: ").split()))

print(menor(numeros[0], numeros[1], numeros[2]))