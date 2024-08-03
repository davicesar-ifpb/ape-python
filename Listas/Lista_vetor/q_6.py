n = int(input("N = "))

vetor = [int(input(f"Vetor[{i}] = ")) for i in range(n)]

print("\nVetor antes:", vetor)

vetor = vetor[::-1]

print("Vetor depois:",vetor)