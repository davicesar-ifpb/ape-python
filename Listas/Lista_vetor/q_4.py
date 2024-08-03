numeros = [int(input(f"Vetor[{i}] = ")) for i in range(10)]

print("\nNumeros de INDICES pares:")
for i in range(0, 10, 2):
    print(f"numeros{i} =", numeros[i])

print("\nNumeros de INDICES impares:")
for i in range(1, 10, 2):
    print(f"numeros{i} =", numeros[i])