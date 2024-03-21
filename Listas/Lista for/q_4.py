# Faça um programa que leia 20 números inteiros, determine e mostre o maior
# deles.

lista = []             # <------ Usando lista
for i in range(20):
    entrada = int(input())
    lista.append(entrada)
lista.sort()
print(lista[-1])

# ------------------------------

entrada = 0           
a = entrada            # <------ Sem lista
for i in range(20):
    entrada = int(input())
    if entrada > a:
        a = entrada
print(a)