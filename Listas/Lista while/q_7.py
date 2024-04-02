idade_soma = 0
qtd_pessoas_idades_18_21 = 0
pessoas_geral = []

while True:

    idade = int(input())

    if idade == 0:
        break

    idade_soma += idade
    if 18 <= idade <= 21:
        qtd_pessoas_idades_18_21 += 1

    pessoas_geral.append(idade)


print(f"Media das idades: {idade_soma / len(pessoas_geral):.0f}")
print(f"Quantidade pessoas entre 18 - 21: {qtd_pessoas_idades_18_21}")
print(f"Pessoa mais nova: {sorted(pessoas_geral)[0]}")

    