import os
import random
diretorio = os.path.dirname(__file__)

file = open(diretorio + "\\numeros.txt", 'w', encoding="UTF-8")

for comb in range(100):
    numeros_distintos = []
    while len(numeros_distintos) < 6:
        numero = random.randint(1,10)
        if numero not in numeros_distintos:
            numeros_distintos.append(numero)

    file.write(f"{numeros_distintos}\n")
file.close()