n = int(input("N = "))
k = int(input("K = "))


vetor = [0] * n
for i in range(n):
    vetor[i] = int(input(f"Vetor[{i}] = "))
# vetor = [int(input(f"vetorA[{i}] = ")) for i in range(n)]


posicoes = []
for i in range(n):
    if (vetor[i] == k):
        posicoes.append(i)
# posicoes = [i for i in range(n) if vetor[i] == k]


if not posicoes:
    print("Não encontrado")
else:
    print(posicoes)