nota0 = 0

while True:
    try:
        quantidade = int(input("Digite a quantidade de notas: "))
        break
    except ValueError:
        print("\nDigite um número inteiro.\n")
    
for i in range(1, (quantidade + 1)):
    while True:
        try:
            nota1 = float(input(f"Digite a nota da avaliação {i}: "))
            nota0 = nota0 + nota1
            break
        except ValueError:
            print("\nDigite um número.\n")

print(f"\nMédia das avaliações é {(nota0 / quantidade):.1f}\n")
