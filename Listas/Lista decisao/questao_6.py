nome = input("Digite seu nome: ")
conceito = input("Digite qual o seu conceito: ")
match conceito.upper():
    case "A":
        print(f"{nome}: Fortemente recomendado.")
    case "B"|"C":
        print(f"{nome}: Recomendado.")
    case "D":
        print(f"{nome}: Não recomendado.")
