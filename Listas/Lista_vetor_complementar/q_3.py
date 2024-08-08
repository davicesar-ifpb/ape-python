numeros = [int(input()) for _ in range(6)]


for i in numeros:
    if numeros.count(i) > 1:
        print(f"{i} possui repeticoes")
    else:
        print(f"{i} é distinto")
