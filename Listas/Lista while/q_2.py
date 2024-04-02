
soma = 0
i = 0
while True:
    n = int(input())

    if n == 999:
        break

    soma += n
    i += 1


print(f"{soma/i:.1f}")

    