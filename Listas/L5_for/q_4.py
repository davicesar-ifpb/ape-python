""" Faça um programa que leia 20 números inteiros, determine e mostre o maior
deles. """


lista = []             # <------ Usando lista
for i in range(20):
    entrada = int(input())
    lista.append(entrada)

print(max(lista))

# ------------------------------

maior = int(input())   # <------ Sem lista
for i in range(19):
    entrada = int(input())
    if entrada > maior:
        maior = entrada
print(maior)
