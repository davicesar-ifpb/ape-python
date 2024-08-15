n = int(input("N = "))

vetor = [int(input(f"Vetor[{i}] = ")) for i in range(n)]

print("\nVetor antes:", vetor)

#vetor = vetor[::-1]
#vetor = [vetor[i] for i in range(n - 1, -1, -1)]
#vetor = reveserd(vetor)

for i in range(n // 2):
    vetor[i], vetor[n-1-i] = vetor[n-1-i], vetor[i]

print("Vetor depois:",vetor)