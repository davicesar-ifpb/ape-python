nome = input().split()

print(nome[-1] + ",", end=' ')

for i in range(len(nome) - 1):
    print(nome[i][0] + ".", end=' ')