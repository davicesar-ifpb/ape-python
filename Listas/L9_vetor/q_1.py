n = int(input("N = "))
k = int(input("K = "))


vetorA = [0] * n
vetorB = [0] * n

for i in range(n):
    vetorA[i] = int(input(f"Vetor[{i}] = "))

for i in range(n):
    vetorB[i] = vetorA[i] * k 

# vetorA = [int(input(f"vetorA[{i}] = ")) for i in range(n)]
# vetorB = list(map(lambda x: x * k, vetorA))
    
print("\nVetor A =",vetorA)
print("Vetor B =",vetorB)
