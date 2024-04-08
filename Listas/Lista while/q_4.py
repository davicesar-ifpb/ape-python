""" Faça um programa que leia os seguintes dados de um conjunto de alunos:
matrícula, nome e as duas notas que ele obteve em suas avaliações. A
condição de parada será a digitação de uma matrícula igual 0 (zero). O
programa deverá mostrar, para cada aluno, as seguintes informações:
matrícula, nome, média e situação (aprovado, se a média for igual ou superior
a 7 e, reprovado, se a média for inferior a 7). """


while True:

    matricula = int(input("Matricula: "))
    if matricula == 0: break


    nome = input("Nome: ")
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))

    media = (nota1 + nota2) / 2
    
    print(f"Matricula: {matricula}")
    print(f"Nome: {nome}")
    print(f"Media: {media:.2f}")
    aprovado = media >= 7
    if aprovado:
        print("Situação: Aprovado\n")
    else:
        print("Situação: Reprovado\n")
    



