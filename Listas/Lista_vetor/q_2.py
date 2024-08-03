k = int(input("K = "))


vetor = [0] * 30
for i in range(30):
    vetor[i] = int(input(f"Vetor[{i}] = "))
#vetor = [int(input(f"vetorA[{i}] = ")) for i in range(30)]


qtd_ocorrencias_k = 0
for i in range(30):
    if (vetor[i] == k):
        qtd_ocorrencias_k += 1
#qtd_ocorrencias_k = vetor.count(k)


print(f"Quantidade de ocorrencias de {k} = {qtd_ocorrencias_k}")