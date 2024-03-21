# Faça um programa que leia 3 números inteiros (N, X, Y) e mostre todos os
# números múltiplos de N entre X e Y.

n,x,y = map(int, input().split())

passo = 1

if x > y:
    y -= 1
    passo = -1
else:
    y += 1

for i in range(x,y,passo):
    if i % 5 == 0:
        print(i)
        