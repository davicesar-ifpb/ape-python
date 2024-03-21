# Faça um programa que leia um número N, inteiro, e some todos os números
# de 1 até N, mostrando o resultado.

entrada = int(input())
soma = 0
for i in range(1,entrada+1):
    soma += i
print(f"{soma = }")
