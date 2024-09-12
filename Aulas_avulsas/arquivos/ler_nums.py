import os
diretorio = os.path.dirname(__file__)

file = open(diretorio + "\\numeros.txt", "r", encoding="UTF-8")

numeros = [0] * 11 # 11 - 1 é o maior numero que pode ser gerado

arq_lido = file.read().splitlines()

for linha in arq_lido:
    for num in linha[1:-1].split(', '):
        numeros[int(num)] += 1

maior_qtd = max(numeros)
print(numeros)
for num, qtd in enumerate(numeros):
    if qtd == maior_qtd:
        print(num)

file.close()