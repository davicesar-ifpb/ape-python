""" Faça um programa que calcule e mostre o fatorial de um número N, fornecido
pelo usuário. A definição de fatorial é mostrada a seguir: """


n = int(input())
n2 = n

# metodo 1
for i in reversed(range(1,n)):
    n = n * i
print(n)

# metodo 2
for i in range(n2-1,1,-1):
    n2 = n2 * i
print(n2)