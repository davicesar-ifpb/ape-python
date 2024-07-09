""" Faça um programa que leia vários números, determine e mostre o maior e o
menor deles.
Obs: a leitura do número 0 (zero) encerra o programa. """


maior_menor = []

while True:
    n = int(input())

    if n == 0: break

    maior_menor.append(n)

maior_menor.sort()
print(f"menor = {maior_menor[0]}\nmaior = {maior_menor[-1]}")

# -------------------------------------------------------------------

n = int(input())
maior = n
menor = n
while True:
    n = int(input())
    
    if n == 0: break
    
    if n > maior:
        maior = n
    if n < menor:
        menor = n
        
print(f"{menor = }")
print(f"{maior = }")