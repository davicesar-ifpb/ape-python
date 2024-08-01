soma = 0
qtd_acima_20 = 0
n = 6
numeros = [0] * n

for i in range(n):
    numeros[i] = int(input())

    soma += numeros[i]

    if numeros[i] > 20:
        qtd_acima_20 += 1

media = soma / n
print(f"{soma = }")
print(f"{qtd_acima_20 = }")
print(f"{media = }")

qtd_acima_media = 0
for i in numeros:
    if i > media:
        qtd_acima_media += 1

print(f"{qtd_acima_media = }")

#print(len(list(filter(lambda x: x > 20, numeros))))

