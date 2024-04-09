""" Faça um programa que acompanhe um set de uma partida de vôlei. O
programa deve ler o código da equipe (A ou B) que ganhou o ponto e
responder quem ganha a partida. O set chega ao final se uma das equipes
chega a 25 pontos e a diferença de pontos entre elas é maior ou igual a dois.
A equipe que conseguir isso é a vencedora do set. """


import os
a = 0
b = 0

while True:
    os.system('cls||clear')
    print(f"Pontos do time A: {a}")    
    print(f"Pontos do time B: {b}")    
    
    if (a == 25 and a - b >= 2) or (b == 25 and b - a >= 2): 
        break
    
    elif (a > 25 and a - b >=2) or (b > 25 and b - a >= 2): 
        break

    ponto = input("\nDigite o time que ganhou o ponto (a/b): ").upper()
    
    if ponto == "A": a += 1
    
    elif ponto == "B": b += 1


if a > b: print("Vencedor: A")
else: print("Vencedor: B")
    
