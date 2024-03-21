e = int(input())

for i in range(e):
    x,y = map(int, input().split())
    passo = 1
    if x > y:
        passo = -1
        x -= 1
    else:
        x += 1
    soma = 0
    for i in range(x,y,passo):
        if i % 2 != 0:
            soma += i
    print(soma)