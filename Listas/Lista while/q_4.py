while True:

    matricula = int(input("Matricula: "))
    if matricula == 0:
        break


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
    



