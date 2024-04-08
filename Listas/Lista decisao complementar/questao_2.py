""" Escreva um programa que solicite a digitação de um caractere qualquer do teclado e imprima
sua classificação: vogal, consoante, número e caractere especial. """


caractere = input("Digite um caractere: ")

if caractere.isdigit():
    print("Número")
elif caractere in "aeiou":
    print("Vogal")
elif caractere in "bcdfghjlkmnpqrstvwxyz":
    print("Consoante")
elif not caractere.isalnum():
    print("Caractere especial")
else:
    print("Digite apenas um caratere!")