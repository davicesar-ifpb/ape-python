tamanho = int(input())

notas = list(map(int, input().split()))

notas.sort(reverse=True)

if notas[11] != notas[12]:
    print("YES")
else:
    print("NO")