n = int(input())
vetor = [0] * n


qtd_pares = 0
qtd_impares = 0

for i in range(n):
    vetor[i] = int(input())
    if vetor[i] % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares += 1

soma = sum(vetor)
media = soma / n

print(qtd_pares)
print(qtd_impares)
print(soma)
print(f"{media:.2f}")


