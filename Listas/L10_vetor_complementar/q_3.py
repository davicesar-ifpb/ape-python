numeros = [int(input()) for _ in range(6)]

numeros_unicos = set(numeros)

print("\n", numeros, sep='')
for i in numeros_unicos:
    if (repeticoes := numeros.count(i)) > 1:
        print(f"{i} possui {repeticoes} repeticoes")
    else:
        print(f"{i} é distinto")
