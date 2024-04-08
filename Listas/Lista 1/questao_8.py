""" Faça um programa que leia o nome de um aluno e as notas das três provas que ele
obteve no semestre. No final informar o nome do aluno e a sua média (aritmética). """


nome = input("Qual teu nome otario? ")
nota1 = int(input("Digite a nota da avaliação 1: "))
nota2 = int(input("Digite a nota da avaliação 2: "))
nota3 = int(input("Digite a nota da avaliação 3: "))
print(f"Média das avaliações de {nome}: {(nota1 + nota2 + nota3) / 3:.2f}")