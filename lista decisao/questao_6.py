nome = input("Digite seu nome: ")
conceito = input("Digite qual o seu conceito: ")
match conceito:
    case "a"|"A":
        print(f"{nome}: Fortemente recomendado.")
    case "b"|"B"|"c"|"C":
        print(f"{nome}: Recomendado.")
    case "d"|"D":
        print(f"{nome}: Não recomendado.")
