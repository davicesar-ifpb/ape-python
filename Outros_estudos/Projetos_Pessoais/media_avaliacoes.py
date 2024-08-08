nota0 = 0

while True:
    quantidade = input("Digite a quantidade de notas: ")
    if not quantidade.isdigit():
        print("\nDigite um número inteiro.\n")
    else:
        quantidade = int(quantidade)
        break

for i in range(1, (quantidade + 1)):
    while True:
        nota1 = input(f"Digite a nota da avaliação {i}: ")
        if not nota1.isdigit():
            print("\nDigite um número.\n")
        else:
            nota1 = float(nota1)
            nota0 = nota0 + nota1
            break

print(f"\nMédia das avaliações é {(nota0 / quantidade):.1f}\n")
