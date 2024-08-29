texto = input()

for i in range(len(texto)):
    print(texto[i] * (i + 1))

for i in reversed(range(len(texto) - 1)):
    print(texto[i] * (i + 1))