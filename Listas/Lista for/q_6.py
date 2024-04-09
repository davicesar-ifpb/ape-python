""" Faça um programa que leia 3 números inteiros (N, X, Y) e mostre todos os
números múltiplos de N entre X e Y. """


n,x,y = map(int, input().split())

if x > y:
    x,y = y,x
    
for i in range(x,y+1):
    if i % n == 0:
        print(i)