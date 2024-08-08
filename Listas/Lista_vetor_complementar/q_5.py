numeros = [6,7,13,14,26]

qtd_acertados = 0

for i in range(20):
    v = []
    while len(v) < 8:
        n = int(input())
        if n in numeros:
            qtd_acertados += 1

        if n in range(1, 81) and n not in v:
            v.append(n)


print(qtd_acertados)