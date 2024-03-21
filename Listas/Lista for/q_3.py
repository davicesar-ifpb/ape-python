# Faça um programa que calcule e mostre o fatorial de um número N, fornecido
# pelo usuário. A definição de fatorial é mostrada a seguir:

n = int(input())

for i in reversed(range(1,n)):
    n = n * i
print(n)