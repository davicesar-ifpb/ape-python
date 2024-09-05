"""
Escreva uma função chamada primo para determinar se um número é primo ou não. A função
deve receber um número inteiro, retornar True se o número for primo, ou False caso contrário.
Escreva também um programa que, usando a função primo criada, exiba os números primos
entre 1 e 100.
"""

import math

def isPrime(n):
    # Verifica se o número é menor ou igual a 1
    if n <= 1:
        return False
    # 2 e 3 são primos
    if n <= 3:
        return True
    # Elimina múltiplos de 2 e 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Verifica divisores a partir de 5 até a raiz quadrada de n
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# Teste
numero = 29
if isPrime(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")