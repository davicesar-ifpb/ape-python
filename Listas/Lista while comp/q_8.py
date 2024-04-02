import os
a = 0
b = 0


while True:
    ponto = input("Digite o time que ganhou o ponto (a/b): ").upper()

    if ponto == "A":
        a += 1
    elif ponto == "B":
        b += 1