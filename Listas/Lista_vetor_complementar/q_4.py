numeros = []

while len(numeros) < 6:
    n = int(input())

    if n not in numeros:
        numeros.append(n)

print(numeros)
