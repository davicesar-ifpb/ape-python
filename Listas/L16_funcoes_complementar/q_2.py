"""
Escreva uma função chamada vogal que receba uma letra e verifique se a letra é uma vogal,
retornando o valor True nesse caso, ou o valor False caso contrário.
Escreva também um programa que leia uma frase e, usando a função vogal criada, imprima a
quantidade de vogais existentes na frase lida.
"""

def isVogal(char:str) -> bool:
    return char in "aeiouAEIOU"


frase = input("digite um afrase: ")

contador = 0
for i in frase:
    if isVogal(i):
        contador += 1

print(contador)