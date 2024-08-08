n = int(input())

vetorA = [int(input()) for _ in range(n)]
vetorB = [int(input()) for _ in range(n)]

vetorC = []

for i in range(n):
    vetorC.append(vetorA[i])
    vetorC.append(vetorB[i])


print(vetorA)
print(vetorB)
print(vetorC)