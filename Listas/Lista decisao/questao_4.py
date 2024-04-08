""" Escreva um programa que leia o nome e o sexo (M ou F) de uma pessoa e exiba a mensagem
"Olá, Sr. Fulano!" ou "Olá, Sra. Fulana!", de acordo com o sexo da pessoa. Obs: Fulano e Fulana
são nomes exemplos. """


nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M/F): ")

if sexo.upper() == "M":
    print(f"Olá, Sr. {nome}!")
elif sexo.upper() == "F":
    print(f"Olá. Sra. {nome}!")
else:
    print(f"Olá {nome}")