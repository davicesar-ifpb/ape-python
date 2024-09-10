"""
Escreva uma função chamada primo para determinar se um número é primo ou não. A função
deve receber um número inteiro, retornar True se o número for primo, ou False caso contrário.
Escreva também um programa que, usando a função primo criada, exiba os números primos
entre 1 e 100.
"""

def isPrime(n):
    if n <= 1:
        return False
    
    if n <= 3:
        return True
    
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    
    i = 5
    while i * i <= n:
        if (n % i == 0) or (n % (i+2) == 0):
            return False
        i += 6
    
    return True

numero = int(input())

if isPrime(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")