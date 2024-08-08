estados = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", 
    "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", 
    "SP", "SE", "TO"
]

votos = [0] * len(estados)

while True:
    voto = input("Digite seu voto: ").upper()

    if voto not in estados:
        break

    votos[estados.index(voto)] += 1


mais_votados = []
maior_qtd_votos = max(votos)

for i in range(len(votos)):
    if votos[i] == maior_qtd_votos:
        mais_votados.append((estados[i], votos[i]))

print(mais_votados)