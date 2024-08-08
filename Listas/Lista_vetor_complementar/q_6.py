unidades_federativas = [
    "pb",
    "pe",
    "sp",
    "rj"
]

votacao = [0] * len(unidades_federativas)


while True:
    a = input()

    if a not in unidades_federativas:
        break

    votacao[unidades_federativas.index(a)] += 1


mais_votados = []
maior_valor = 0

for i in range(len(votacao)):
    if votacao[i] > maior:
        maior = votacao[i]

    