""" Escreva um programa que solicite a digitação de um número (de 1 a 7) correspondente a um dia
da semana e imprima o nome do dia da semana e se é dia útil (de segunda a sexta) ou final de
semana (sábado e domingo). Considere que o dia 1 é o domingo. """


dia = input("Digite um dia (1 a 7): ")
match dia:
    case "1":
        print("Domingo, é fim de semana")
    case "2":
        print("Segunda-feira, é dia útil")
    case "3":
        print("Terça-feira, é dia útil")
    case "4":
        print("Quarta-feira, é dia útil")
    case "5":
        print("Quinta-feira, é dia útil")
    case "6":
        print("Sexta-feira, é dia útil")
    case "7":
        print("Sábado, é fim de semana.")


""" dia = int(input("Digite um dia (1 a 7): "))
semanas = ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"]

index = dia - 1

if index in range(0,7):
    print(semanas[index].capitalize())
    if index == 0 or index == 6:
        print("Fim de semana.\n")
    else:
        print("Dia útil\n")
else:
    print("Dia da semana não encontrado.\n")
 """