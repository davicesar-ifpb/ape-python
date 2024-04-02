maior_menor = []

while True:
    n = int(input())

    if n == 0:
        break

    maior_menor.append(n)

maior_menor.sort()
print(f"menor = {maior_menor[0]} maior = {maior_menor[-1]}")


