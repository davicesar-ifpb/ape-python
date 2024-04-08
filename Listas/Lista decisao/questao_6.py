""" Recomendam-se estudantes para bolsas de estudo em função de seu desempenho.
A natureza das recomendações é baseada na seguinte tabela:

Escreva um programa que leia o nome e o conceito de um estudante e exiba o nome do
estudante e sua respectiva recomendação. """


nome = input("Digite seu nome: ")
conceito = input("Digite qual o seu conceito: ")
match conceito.upper():
    case "A":
        print(f"{nome}: Fortemente recomendado.")
    case "B"|"C":
        print(f"{nome}: Recomendado.")
    case "D":
        print(f"{nome}: Não recomendado.")
